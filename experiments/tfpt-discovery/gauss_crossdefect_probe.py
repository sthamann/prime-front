#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gauss_crossdefect_probe -- PRIME.GAUSS.CROSSDEFECT.01
(EXPLORATION ONLY, experiments/; round 33 late, probe B,
after GAUSS-STILL-DEFECTIVE, 2026-08-08).

THE QUESTION: is the O(1) co-isometry defect of the
Gauss-frame transition U^G FINITE-RANK and pole-organized
(then U = U_0 + R_pole and the wall shrinks to a small
matrix -- the Uvarov reading), or does its rank grow with h
(diffuse -- the Prufer route activates)?

DERIVED BEFORE RUNNING (frozen):
  (P1) STRUCTURAL SPLIT: E_R = I - U^H U contains the kernel
       block P_ker (dim h - r_-, eigenvalue exactly 1, the
       minus arm's rank compression) which grows with h
       REGARDLESS of cross-measure structure.  The Uvarov
       question lives in the nonzero-sigma pairing =
       E_L = I - U U^H on the minus side.  E_L is EXACTLY
       traceless (unit rows), so the over-normalization
       (negative part) and the loss (positive part) balance
       in trace -- both signs typed.
  (P2) POLE POINT: in x = cos th coordinates the pole is
       x_pole = cosh(D/2) (the task's 2cosh(D/2) in the
       z + 1/z convention -- the same point): the port
       v_k = e^{kD/2} is the kernel evaluation at the complex
       angle th = iD/2; the odd-extended evaluation vector
       f_k(iD/2) = e^{kD/2} - e^{(2h-1-k)D/2} is REAL.
       Two predeclared pole vectors, both Christoffel-
       normalized to U's row coordinates: kpol (kernel column
       at x_pole, task-frozen primary) and kv (the deployed
       plain port v, kappa-probe secondary).
  (P3) CLOSEST CO-ISOMETRY: U_0 = (U U^H)^{-1/2} U satisfies
       U_0 U_0^H = I exactly; with D_- <= 1 the base term
       I - U_0^H D_-^2 U_0 is PSD BY THEOREM, so the entire
       wall relocates into the bracket built from
       R = U - U_0: Delta = base - [U_0^H D_-^2 R + h.c.
       + R^H D_-^2 R].  If R is (near) finite rank the wall
       is a small-matrix condition -- the compensation
       statement.

VERDICT (frozen): CROSSDEFECT-POLE-RANK-ONE /
CROSSDEFECT-FINITE-RANK / CROSSDEFECT-DIFFUSE.
NO RH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gauss_crossdefect_probe.py
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

FROZEN_SPEC = """\
PRIME.GAUSS.CROSSDEFECT.01 spec v1 (2026-08-08, frozen before
run).  Machinery = gauss_node_unitary probe verbatim (arm
Gauss systems, U^G, D_-^G); ladder = ALL frame_a_zones with
h <= 900; heavy rungs {9, 12, 13, 26, 40}; anchors
{9, 12, 13}.  S1 DEFECT OPERATORS per rung: E_L = I - UU^H
(minus side, primary -- no structural block; traceless ward
|tr E_L| <= 1e-8 r_-), E_R = I - U^H U (plus side; kernel
block dim h - r_- typed, nonzero-sigma part mirrors E_L);
full eigh; sign structure (pos/neg counts + trace masses);
rank censuses #{|eig| > t max|eig|} at t in {1e-2, 1e-4,
1e-8}.  S2 POLE TEST (fit-free): fpole_k = e^{kD/2} -
e^{(2h-1-k)D/2}; kpol_g = K_+(th_g^-, x_pole) via zp = Rm
fpole (ward: two routes, conj(Zm) zp vs conj(Fm) solve(Gp,
fpole), rel <= 1e-8); kv from plain v; normalized kappa =
kpol/sqrt(Kdiag_-); overlaps o_pole = |<e_top(E_L),
kappa^>|, o3 = ||P_top3 kappa^|| (and same for kv); Rayleigh
gamma = kappa^H E_L kappa / ||kappa||^2 (source-determined,
no fit); residual E_res = E_L - gamma kappa kappa^H/
||kappa||^2; residual rank censuses at the same thresholds
(relative to max|eig E_L|); gamma_h series typed
(descriptive Pearson vs h, alpha; never gates).  S3
STABILITY: o_pole series along the ladder; frozen bar:
std(o_pole over the last 10 rungs) <= 0.15 (wild-rotation
kill); top-3 |eig| ratios at anchors (shape stability,
descriptive); boundary localization of top residual modes
(mass on nodes with th in the outer 5% of [0, pi],
descriptive).  S4 CONSEQUENCE at heavy rungs: U_0 =
(UU^H)^{-1/2} U (eigh route); wards ||U_0 U_0^H - I||_F <=
1e-8 and base = I - U_0^H D_-^2 U_0 PSD (lam_min >= -1e-10,
theorem P3); R = U - U_0: sigma profile, rank censuses,
top-mode pole overlap; bracket B = Delta_pos - base with
Delta_pos = I - (C^G)^H C^G: ||B||_2, rank@1e-2, and the tau
ward |lam_min(Delta_pos) - lam1(Delta_grid)| <= max(1e-9,
0.01 lam1).  GATE WARDS: the Gauss-frame regressions --
frame tightness/rows (max rel <= 1e-8), D_-^G(kz9) in
[0.98, 0.99], max D_-^G ladder <= 0.9975, cert(kz9) in
[1.0, 1.2], sigmax(U^G)(kz9) in [1.40, 1.49], bridge tauerr
<= max(1e-10, lam1/10) every rung; kpol two-route ward;
U_0/base wards; tau ward.  S5 controls at kz 9: Epstein
(x^2+5y^2) + scramble seed 1: lam1 < 0 AND the triple
(max|eig E_L|, o_pole, rank@1e-2(E_L)) differs from truth by
>= 5 percent in >= 1 component.  VERDICT (keyed to E_L,
predeclared): CROSSDEFECT-POLE-RANK-ONE iff gates pass AND
residual rank@1e-2 <= 3 on every rung; CROSSDEFECT-FINITE-
RANK iff gates pass AND residual rank@1e-2 <= 10 on every
rung AND mean(last third by h) < 1.5 mean(first third);
CROSSDEFECT-DIFFUSE otherwise (rank growth typed: the
first/last-third means, the h-correlation).  Float64;
budget ~15 min.  NO RH claim; writes nothing.
"""

HEAVY = (9, 12, 13, 26, 40)
ANCHORS = (9, 12, 13)
THRS = (1e-2, 1e-4, 1e-8)
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


# ------------------------------------------------ Krein machinery (verbatim)
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


def build_rung(kz, scramble_seed=None, comb=None):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    Ktoe = core.odd_toeplitz(c_ar + c_at, M)
    L = 2 * (2 * h) - 2
    E = odd_extend_mat(h)
    F = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    dp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))
    dm = np.sqrt(np.maximum(-d, 0.0) / (2.0 * L))
    Bp = dp[:, None] * F
    Bm = dm[:, None] * F
    pos, neg = d > 0.0, d < 0.0
    Gp = np.real(Bp.conj().T @ Bp)
    Gm = np.real(Bm.conj().T @ Bm)
    ev, Vp = np.linalg.eigh(Gp)
    Rm = Vp @ np.diag(ev ** -0.5) @ Vp.T
    Delta = Rm @ Ktoe @ Rm
    Delta = 0.5 * (Delta + Delta.T)
    return dict(rr=rr, d=d, L=L, h=h, D=D, alpha=alpha, F=F,
                pos=pos, neg=neg, Gp=Gp, Gm=Gm, Rm=Rm,
                Delta=Delta)


# ------------------------------------------------ Gauss machinery (verbatim)
def folded_arm_measure(b, arm):
    L = b["L"]
    mask = b["pos"] if arm > 0 else b["neg"]
    jj = np.arange(L)[mask]
    th = 2.0 * math.pi * jj / L
    mu = np.abs(b["d"][mask]) / (2.0 * L)
    wt = mu * 4.0 * np.sin(th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    thu = 2.0 * math.pi * uf / L
    keep = wagg > 0.0
    return np.cos(thu[keep]), wagg[keep], thu[keep]


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
        if bnorm <= 1e-13 * max(1.0, float(np.max(np.abs(x)))):
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def arm_gauss_system(b, arm):
    xs, ws, thu = folded_arm_measure(b, arm)
    h = b["h"]
    if len(xs) > h:
        al, be, m0, steps = lanczos_chain(xs, ws, h)
        if steps < h:
            return None, None, "breakdown@%d" % steps
        T = np.diag(al)
        if h > 1:
            T += np.diag(be, 1) + np.diag(be, -1)
        evs, V = np.linalg.eigh(T)
        xg = np.clip(evs, -1.0, 1.0)
        wg = m0 * V[0] ** 2
        th = np.arccos(xg)
        wS = wg / (4.0 * np.sin(th / 2.0) ** 2)
        return th, wS, "gauss"
    th = thu
    wS = ws / (4.0 * np.sin(th / 2.0) ** 2)
    return th, wS, "measure-tight"


def eval_frame(th, h):
    k = np.arange(h)
    ph = np.exp(-1j * np.outer(th, k))
    ph2 = np.exp(-1j * np.outer(th, 2 * h - 1 - k))
    return ph - ph2


def gauss_objects(b):
    h = b["h"]
    thp, wSp, modep = arm_gauss_system(b, +1)
    thm, wSm, modem = arm_gauss_system(b, -1)
    if thp is None or thm is None:
        return dict(mode=(modep, modem), fail=True)
    Fp = eval_frame(thp, h)
    Fm = eval_frame(thm, h)
    Zp = Fp @ b["Rm"]
    Zm = Fm @ b["Rm"]
    Kp = np.sum(np.abs(Zp) ** 2, axis=1)
    Km = np.sum(np.abs(Zm) ** 2, axis=1)
    Knp = Zm @ Zp.conj().T
    U = (1.0 / np.sqrt(Km))[:, None] * Knp \
        * (1.0 / np.sqrt(Kp))[None, :]
    Dp = np.sqrt(wSp * Kp)
    Dm = np.sqrt(wSm * Km)
    CG = np.sqrt(wSm)[:, None] * Knp * np.sqrt(wSp)[None, :]
    w1p = float(np.linalg.norm(np.real(
        (np.sqrt(wSp)[:, None] * Fp).conj().T
        @ (np.sqrt(wSp)[:, None] * Fp)) - b["Gp"])
        / np.linalg.norm(b["Gp"]))
    rown = np.sqrt(np.sum(np.abs(U) ** 2, axis=1))
    w3row = float(np.max(np.abs(rown - 1.0)))
    return dict(mode=(modep, modem), fail=False, thp=thp,
                thm=thm, Fm=Fm, Zp=Zp, Zm=Zm, Kp=Kp, Km=Km,
                U=U, Dp=Dp, Dm=Dm, CG=CG, w1=w1p, w3=w3row,
                rminus=len(thm))


def rank_census(eigs, ref):
    a = np.abs(eigs)
    return tuple(int(np.sum(a > t * ref)) for t in THRS)


def pearson(a, b):
    a = np.asarray(a, float) - np.mean(a)
    b = np.asarray(b, float) - np.mean(b)
    den = np.linalg.norm(a) * np.linalg.norm(b)
    return float(a @ b / den) if den > 0 else 0.0


def defect_analysis(b, go):
    """E_L spectral decomposition + the pole test."""
    U, Zm, Km = go["U"], go["Zm"], go["Km"]
    rmin = go["rminus"]
    EL = np.eye(rmin) - U @ U.conj().T
    EL = 0.5 * (EL + EL.conj().T)
    ev, W = np.linalg.eigh(EL)
    emax = float(np.max(np.abs(ev)))
    tr = float(np.real(np.trace(EL)))
    npos = int(np.sum(ev > 0)); nneg = int(np.sum(ev < 0))
    mpos = float(np.sum(ev[ev > 0]))
    mneg = float(-np.sum(ev[ev < 0]))
    # pole vectors (P2)
    h, D = b["h"], b["D"]
    kk = np.arange(h)
    fpole = np.exp(0.5 * D * kk) \
        - np.exp(0.5 * D * (2 * h - 1 - kk))
    zpol = b["Rm"] @ fpole
    kpol = np.conj(Zm) @ zpol
    kpol2 = np.conj(go["Fm"]) @ np.linalg.solve(b["Gp"], fpole)
    wardk = float(np.linalg.norm(kpol - kpol2)
                  / np.linalg.norm(kpol))
    v = np.exp(0.5 * D * kk)
    kv = np.conj(Zm) @ (b["Rm"] @ v)
    kap = kpol / np.sqrt(Km)
    kap = kap / np.linalg.norm(kap)
    kapv = kv / np.sqrt(Km)
    kapv = kapv / np.linalg.norm(kapv)
    # top defect mode overlaps (by |eig|)
    order = np.argsort(-np.abs(ev))
    etop = W[:, order[0]]
    o_pole = float(abs(np.vdot(etop, kap)))
    o_v = float(abs(np.vdot(etop, kapv)))
    P3 = W[:, order[:3]]
    o3 = float(np.linalg.norm(P3.conj().T @ kap))
    # Rayleigh + residual (fit-free)
    gam = float(np.real(np.vdot(kap, EL @ kap)))
    ERES = EL - gam * np.outer(kap, kap.conj())
    evr = np.linalg.eigvalsh(0.5 * (ERES + ERES.conj().T))
    return dict(EL=EL, ev=ev, emax=emax, tr=tr, npos=npos,
                nneg=nneg, mpos=mpos, mneg=mneg, kap=kap,
                kapv=kapv, wardk=wardk, o_pole=o_pole,
                o_v=o_v, o3=o3, gam=gam, evr=evr,
                rk=rank_census(ev, emax),
                rkres=rank_census(evr, emax),
                W=W, order=order)


# ================================================================= main
def main():
    section("PRIME.GAUSS.CROSSDEFECT.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    zones = list(core.frame_a_zones())

    section("S1/S2 ladder pass -- defect spectra + pole test")
    rows = []
    heavy_data = {}
    skipped = []
    wardk_max = 0.0
    print("    kz    h    r-   |eig|mx  n+/n-     rank"
          "@1e-2/4/8      gamma    o_pole o_v    o3"
          "     res@1e-2/4/8")
    for kz in zones:
        b = build_rung(kz)
        if b["h"] > 900:
            skipped.append(kz)
            continue
        go = gauss_objects(b)
        if go["fail"]:
            check("S1.x kz %d Gauss system FAILED (%s)"
                  % (kz, go["mode"]), False)
            continue
        da = defect_analysis(b, go)
        wardk_max = max(wardk_max, da["wardk"])
        lam1 = float(np.linalg.eigvalsh(b["Delta"])[0])
        svC = np.linalg.svd(go["CG"], compute_uv=False)
        tauerr = abs(float(svC[0]) ** 2 - (1.0 - lam1))
        sv = np.linalg.svd(go["U"], compute_uv=False)
        r = dict(kz=kz, h=b["h"], rminus=go["rminus"],
                 emax=da["emax"], tr=da["tr"],
                 rk=da["rk"], rkres=da["rkres"],
                 gam=da["gam"], o_pole=da["o_pole"],
                 o_v=da["o_v"], o3=da["o3"],
                 maxDm=float(np.max(go["Dm"])),
                 cert=float(np.max(np.abs(sv ** 2 - 1.0))),
                 sig=float(sv[0]), lam1=lam1, tauerr=tauerr,
                 w1=go["w1"], w3=go["w3"], alpha=b["alpha"])
        rows.append(r)
        if kz in HEAVY:
            heavy_data[kz] = (b, go, da)
        print("    %-5d %-4d %-4d %.4f  %3d/%-3d  "
              "%3d/%3d/%3d      %+.4f  %.3f  %.3f  %.3f"
              "  %3d/%3d/%3d"
              % (kz, r["h"], r["rminus"], r["emax"],
                 da["npos"], da["nneg"], *r["rk"], r["gam"],
                 r["o_pole"], r["o_v"], r["o3"], *r["rkres"]),
              flush=True)
    if skipped:
        print("    skipped (h > 900): %s" % skipped)

    # ---------------- S1 wards + sign structure
    section("S1 -- wards and the sign structure of the defect")
    w13 = max(max(r["w1"], r["w3"]) for r in rows)
    check("S1.1 [FRAME REGRESSION] tightness + unit rows "
          "(max %.2e)" % w13, w13 <= 1e-8)
    trmax = max(abs(r["tr"]) / r["rminus"] for r in rows)
    check("S1.2 [P1 TRACELESS] |tr E_L| <= 1e-8 r_- every "
          "rung (max %.2e; over-normalization == loss in "
          "trace)" % trmax, trmax <= 1e-8)
    check("S1.3 [KPOL WARD] two-route kernel column at "
          "x_pole = cosh(D/2), rel <= 1e-8 (max %.2e)"
          % wardk_max, wardk_max <= 1e-8)
    r9 = next(r for r in rows if r["kz"] == 9)
    reg_ok = (0.98 <= r9["maxDm"] <= 0.99
              and 1.0 <= r9["cert"] <= 1.2
              and 1.40 <= r9["sig"] <= 1.49
              and max(r["maxDm"] for r in rows) <= 0.9975)
    check("S1.4 [GAUSS-FRAME REGRESSIONS] D_-^G(kz9) = %.4f, "
          "cert(kz9) = %.3f, sigmax(kz9) = %.4f, ladder "
          "maxD- = %.4f" % (r9["maxDm"], r9["cert"], r9["sig"],
                            max(r["maxDm"] for r in rows)),
          reg_ok)
    tau_ok = all(r["tauerr"] <= max(1e-10, r["lam1"] / 10.0)
                 for r in rows)
    check("S1.5 [BRIDGE] tau preserved every rung", tau_ok)
    for kz in ANCHORS:
        b, go, da = heavy_data[kz]
        ev = da["ev"]
        print("    kz %-3d: E_L eig quantiles q05/q50/q95 = "
              "%+.3f/%+.3f/%+.3f; pos/neg trace mass = "
              "%.2f/%.2f; E_R kernel block dim h - r_- = %d "
              "(structural, typed)"
              % (kz, float(np.quantile(ev, 0.05)),
                 float(np.quantile(ev, 0.50)),
                 float(np.quantile(ev, 0.95)),
                 da["mpos"], da["mneg"],
                 b["h"] - go["rminus"]))

    # ---------------- S3 growth + stability
    section("S3 -- rank growth and mode stability")
    hs = sorted(rows, key=lambda r: r["h"])
    third = len(hs) // 3
    first_m = float(np.mean([r["rkres"][0] for r in
                             hs[:third]]))
    last_m = float(np.mean([r["rkres"][0] for r in
                            hs[-third:]]))
    corr_h = pearson([r["h"] for r in rows],
                     [r["rkres"][0] for r in rows])
    rkres_max = max(r["rkres"][0] for r in rows)
    print("    residual rank@1e-2: max %d; first/last-third "
          "means (by h) %.1f -> %.1f (x%.2f); Pearson vs h = "
          "%+.3f" % (rkres_max, first_m, last_m,
                     last_m / max(first_m, 1e-12), corr_h))
    rk_max = max(r["rk"][0] for r in rows)
    first_f = float(np.mean([r["rk"][0] for r in hs[:third]]))
    last_f = float(np.mean([r["rk"][0] for r in hs[-third:]]))
    print("    full E_L rank@1e-2:  max %d; first/last-third "
          "means %.1f -> %.1f (x%.2f)"
          % (rk_max, first_f, last_f,
             last_f / max(first_f, 1e-12)))
    gam_h = pearson([math.log(r["h"]) for r in rows],
                    [r["gam"] for r in rows])
    gam_a = pearson([r["alpha"] for r in rows],
                    [r["gam"] for r in rows])
    print("    gamma_h series: range [%+.4f, %+.4f], Pearson "
          "vs log h = %+.3f, vs alpha = %+.3f (descriptive)"
          % (min(r["gam"] for r in rows),
             max(r["gam"] for r in rows), gam_h, gam_a))
    tail = [r["o_pole"] for r in rows[-10:]]
    stab = float(np.std(tail))
    check("S3.1 [STABILITY] std(o_pole, last 10 rungs) = "
          "%.3f <= 0.15 (mean %.3f; wild-rotation kill "
          "otherwise)" % (stab, float(np.mean(tail))),
          stab <= 0.15)
    for kz in ANCHORS:
        b, go, da = heavy_data[kz]
        e3 = da["ev"][np.argsort(-np.abs(da["ev"]))[:3]]
        # boundary localization of top residual modes
        thm = go["thm"]
        edge = (thm <= 0.05 * math.pi) | (thm >= 0.95 * math.pi)
        wt = da["W"][:, da["order"][:3]]
        bmass = float(np.sum(np.abs(wt[edge]) ** 2)
                      / np.sum(np.abs(wt) ** 2))
        print("    kz %-3d: top-3 |eig| = %+.4f/%+.4f/%+.4f; "
              "edge-node mass of top-3 modes = %.1f%% "
              "(nodes at edge: %d/%d)"
              % (kz, e3[0], e3[1], e3[2], 100 * bmass,
                 int(np.sum(edge)), len(thm)))

    # ---------------- S4 the consequence: U0 + R
    section("S4 -- closest co-isometry U_0 + R and the "
            "bracket (heavy rungs)")
    u0_ok = True
    base_ok = True
    tau2_ok = True
    for kz in HEAVY:
        b, go, da = heavy_data[kz]
        U, Dm = go["U"], go["Dm"]
        G = U @ U.conj().T
        G = 0.5 * (G + G.conj().T)
        gv, GV = np.linalg.eigh(G)
        Gmh = GV @ np.diag(gv ** -0.5) @ GV.conj().T
        U0 = Gmh @ U
        w0 = float(np.linalg.norm(U0 @ U0.conj().T
                                  - np.eye(len(gv))))
        u0_ok &= w0 <= 1e-8
        R = U - U0
        svR = np.linalg.svd(R, compute_uv=False)
        uR = np.linalg.svd(R, compute_uv=True)[0][:, 0]
        oR = float(abs(np.vdot(uR, da["kap"])))
        rkR = rank_census(svR, float(svR[0]))
        # bracket
        base = np.eye(b["h"]) - U0.conj().T @ (Dm[:, None] ** 2
                                               * U0)
        base = 0.5 * (base + base.conj().T)
        lmb = float(np.linalg.eigvalsh(base)[0])
        base_ok &= lmb >= -1e-10
        Dpos = np.eye(b["h"]) - go["CG"].conj().T @ go["CG"]
        Dpos = 0.5 * (Dpos + Dpos.conj().T)
        lmD = float(np.linalg.eigvalsh(Dpos)[0])
        tau2_ok &= abs(lmD - r_lam1(rows, kz)) \
            <= max(1e-9, 0.01 * r_lam1(rows, kz))
        Brk = Dpos - base
        Brk = 0.5 * (Brk + Brk.conj().T)
        evB = np.linalg.eigvalsh(Brk)
        nB = float(max(np.abs(evB)))
        rkB = rank_census(evB, nB)
        print("    kz %-3d: ||U0U0*-I|| = %.1e; sigma(R) top "
              "%.3f, rank@1e-2 = %d, top-mode pole overlap = "
              "%.3f; lam_min(base) = %+.2e (PSD thm); "
              "||bracket|| = %.3f, rank@1e-2 = %d; "
              "lam_min(Delta_pos) = %+.3e vs tau %.3e"
              % (kz, w0, float(svR[0]), rkR[0], oR, lmb,
                 nB, rkB[0], lmD, r_lam1(rows, kz)))
    check("S4.1 [U0 WARD] U_0 U_0^H = I at heavy rungs "
          "(closest co-isometry constructed)", u0_ok)
    check("S4.2 [P3 BASE PSD] I - U_0^H D_-^2 U_0 >= 0 at "
          "heavy rungs (theorem: D_- <= 1 + co-isometry)",
          base_ok)
    check("S4.3 [TAU WARD] lam_min(I - C^G* C^G) == "
          "lam1(Delta_grid) at heavy rungs", tau2_ok)

    # ---------------- S5 controls
    section("S5 -- controls at kz 9 (Epstein x^2+5y^2, "
            "scramble seed 1)")
    rt = next(r for r in rows if r["kz"] == 9)
    triple_t = np.array([rt["emax"], rt["o_pole"],
                         float(rt["rk"][0])])
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        bc = build_rung(9, **kw)
        gc = gauss_objects(bc)
        lam1c = float(np.linalg.eigvalsh(bc["Delta"])[0])
        if gc["fail"]:
            print("    %-8s: Gauss system failed (%s) -- "
                  "maximal discrimination" % (nmc, gc["mode"]))
            ctrl_ok &= lam1c < 0.0
            continue
        dc = defect_analysis(bc, gc)
        triple_c = np.array([dc["emax"], dc["o_pole"],
                             float(dc["rk"][0])])
        reldiff = np.abs(triple_c - triple_t) \
            / np.maximum(triple_t, 1e-12)
        ctrl_ok &= (lam1c < 0.0
                    and bool(np.max(reldiff) >= 0.05))
        print("    %-8s: lam1 = %+.3e; (|eig|max, o_pole, "
              "rank@1e-2) = (%.3f, %.3f, %d) vs truth "
              "(%.3f, %.3f, %d); max rel diff %.1f%%"
              % (nmc, lam1c, dc["emax"], dc["o_pole"],
                 dc["rk"][0], rt["emax"], rt["o_pole"],
                 int(rt["rk"][0]),
                 100.0 * float(np.max(reldiff))))
    check("S5.1 [CONTROLS] sign break + defect-structure "
          "difference >= 5%", ctrl_ok)

    # ---------------- verdict
    section("V -- FROZEN VERDICT + honest consequence")
    gates_ok = (w13 <= 1e-8 and trmax <= 1e-8
                and wardk_max <= 1e-8 and reg_ok and tau_ok
                and stab <= 0.15 and u0_ok and base_ok
                and tau2_ok and ctrl_ok)
    growth = last_m >= 1.5 * first_m
    if gates_ok and rkres_max <= 3:
        verdict = "CROSSDEFECT-POLE-RANK-ONE"
        typed = ("residual rank@1e-2 <= %d everywhere; "
                 "gamma law above" % rkres_max)
    elif gates_ok and rkres_max <= 10 and not growth:
        verdict = "CROSSDEFECT-FINITE-RANK"
        typed = ("residual rank@1e-2 <= %d, no growth "
                 "(%.1f -> %.1f)" % (rkres_max, first_m,
                                     last_m))
    else:
        verdict = "CROSSDEFECT-DIFFUSE"
        typed = ("residual rank@1e-2 max %d, first/last "
                 "third %.1f -> %.1f (x%.2f), Pearson vs h "
                 "%+.3f%s -- the Uvarov reading dies, the "
                 "Prufer route activates"
                 % (rkres_max, first_m, last_m,
                    last_m / max(first_m, 1e-12), corr_h,
                    "" if gates_ok else
                    "; GATES FAILED: %s" % sorted(set(FAILS))))
    print("\n  VERDICT: %s" % verdict)
    print("  typed: %s" % typed)
    npass = sum(1 for _, ok in CHECKS if ok)
    print("\n  checks: %d/%d passed; elapsed %.1f s"
          % (npass, len(CHECKS), time.time() - T0))
    print("""
HONEST CONSEQUENCE (no RH claim):
  the pole share of the defect (o_pole, gamma) and the
  U_0 + R bracket sizes above are the honest inventory of
  how much of the cross-measure misalignment is
  pole-organized; the rank censuses decide whether a
  finite-matrix compensation exists at all.  EXPLORATION
  ONLY; nothing here enters verification/ or the papers.""")
    return verdict


def r_lam1(rows, kz):
    return next(r["lam1"] for r in rows if r["kz"] == kz)


if __name__ == "__main__":
    main()
