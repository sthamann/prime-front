#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pole_port_kappa_probe -- PRIME.POLEPORT.KAPPA_LAW.01
(EXPLORATION ONLY, experiments/; round 33 evening, after
SOFTPORT-FOUND + CAUCHY-RANK-SMALL, 2026-08-08).

THE GAP TO CLOSE: the softport probe found s_h = kappa_h tau_h
at the POLE port (v_r = e^{rD/2}) with kappa stable in
[1.4, 2.7] and the pole carrying up to 84% of the soft mode.
This probe asks for the CLOSED SOURCE-SIDE LAW of kappa.

THE EXACT SKELETON (all warded at machine grade):
  Delta = G+^{-1/2} K G+^{-1/2},  w = G+^{1/2} v / ||.||,
  s = 1/(w' Delta^{-1} w)          (Schur identity),
  kappa^{-1} = beta^2 + lam1 * rho (exact: beta = |<w,e_soft>|,
      rho = sum_{i>=2} beta_i^2 / lam_i  -- the bulk
      admittance; kappa >= 1 always),
  a = w' Delta w = 1 - E-/E+  with  E+- = (2L)^{-1}
      sum_{+-bins} |d_j| |P_j|^2   (the pole port's own defect
      = ONE MINUS THE ARM-ENERGY RATIO of the pole direction),
  P_j = the transform of the odd-extended pole direction --
      CLOSED FORM (two geometric sums; the continuum limit of
      |P|^2 is the Cauchy kernel 1/(1/4 + tau^2): the pole
      port reads the signed density through the Poisson kernel
      at the pole point s = 1/2 -- correlation measured),
  s = a - r' G^{-1} r  with the bulk contraction resolved two
      ways: (i) MODE PARTICIPATION (how many bulk modes carry
      95% of r'G^{-1}r -- exact, the concentration census);
      (ii) NEUMANN tail with the certified bound
      T_K <= ||z_{K/2}||^2 / gmin (frontier typed).

VERDICT (frozen): KAPPA-LAW-CLOSED / KAPPA-LAW-PARTIAL /
KAPPA-EMPIRICAL-ONLY.  NO RH claim; writes nothing; v563
READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/pole_port_kappa_probe.py
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
PRIME.POLEPORT.KAPPA_LAW.01 spec v1 (2026-08-08, frozen before
run).  Machinery = krein cut 1 verbatim; ladder = ALL
frame_a_zones with h <= 900 (skips typed).  S1 kappa series:
per rung s, kappa = s/lam1, beta, a, r'G^-1 r, gmin(G), U0 =
v'G+v/v'v; regressions vs softport probe: kappa_POLE(kz9) in
[2.6, 2.8], kappa_POLE(kz40) in [1.5, 1.7], max_rungs beta in
[0.80, 0.88]; CHEAT ceiling |kappa-1| <= 1e-6 at anchors
{9,12,13}.  Fit-free law readouts (descriptive only, never in
verdict): Pearson r + slope of log(kappa-1) vs log h, vs
alpha, vs log U0; first/last-third means; Aitken limit on the
last 10 rungs.  S2 analytic wards (these DO gate the verdict):
W1 closed-form P_j (two geometric sums) vs FFT rel <= 1e-8;
W2 a = 1 - E-/E+ from densities vs w'Delta w rel <= 1e-8; W3
kappa^-1 = beta^2 + lam1*rho rel <= 1e-8; Cauchy-kernel
correlation corr(|P|^2, 1/(1/4+tau^2)) reported; mode
participation n95 = #bulk modes for 95% of r'G^-1r; Neumann
with certified tail T_K <= ||z_{K/2}||^2/gmin, K adaptive <=
3000, enclosure width / s typed per rung (frontier = first
rung with width > 0.5 s); W4 monotone consistency partial <=
r'G^-1r <= partial + tail on every rung.  S3 generator law at rungs
{9,12,13,26,40}: displacement rank@1e-3 in tau and top-pair
cos-sims vs sqrt|d|, sqrt|d_ar| per rung.  S4 discriminators
at kz 9: Epstein (x^2+5y^2) and scramble seed 1 -- bar:
gmin(G) < 0 OR s < 0 at the pole port (the Feshbach premise
or the sign must break).  VERDICT: KAPPA-LAW-CLOSED iff
W1-W3 pass everywhere AND n95 <= 20 on all rungs AND the
Neumann enclosure width <= 0.1 s on all rungs.
KAPPA-LAW-PARTIAL iff W1-W3 pass everywhere AND n95 <= 20 on
all rungs (the two-term law a - concentrated coupling with
exact remainder) with the Neumann frontier typed.
KAPPA-EMPIRICAL-ONLY else.  Float64, wards as stated.  NO RH
claim; writes nothing.
"""

ANCHORS = (9, 12, 13)
GEN_RUNGS = (9, 12, 13, 26, 40)
KAPPA_REFS = {9: (2.6, 2.8), 40: (1.5, 1.7)}
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


def krein_arms(d, h):
    M = 2 * h
    L = 2 * M - 2
    E = odd_extend_mat(h)
    Fp = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    dp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))
    dm = np.sqrt(np.maximum(-d, 0.0) / (2.0 * L))
    return dp[:, None] * Fp, dm[:, None] * Fp, Fp


def contractor(Bp, Bm):
    U, s, Vh = np.linalg.svd(Bp, full_matrices=False)
    r = int(np.sum(s > 1e-12 * s[0]))
    U, s, Vh = U[:, :r], s[:r], Vh[:r]
    A2 = Bm @ (Vh.conj().T / s)
    return U, s, Vh, A2


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
    K = core.odd_toeplitz(c_ar + c_at, M)
    d = grid_density(c_ar + c_at)
    Bp, Bm, Fp = krein_arms(d, h)
    Gp = np.real(Bp.conj().T @ Bp)
    ev, Vp = np.linalg.eigh(Gp)
    Rm = Vp @ np.diag(ev ** -0.5) @ Vp.T
    Rp = Vp @ np.diag(ev ** 0.5) @ Vp.T
    Delta = Rm @ K @ Rm
    Delta = 0.5 * (Delta + Delta.T)
    return rr, d, Bp, Bm, Fp, K, Gp, Rp, Delta, c_ar


def pole_transform_closed(h, L, D):
    """Closed form of P_j = F(odd-extended e^{rD/2})_j: two
    geometric sums (the symbolic object; ward vs FFT)."""
    x = math.exp(0.5 * D)
    om = np.exp(-2j * math.pi * np.arange(L) / L)

    def geo(z):
        out = np.empty_like(z)
        near = np.abs(1.0 - z) < 1e-12
        out[~near] = (1.0 - z[~near] ** h) / (1.0 - z[~near])
        out[near] = h
        return out

    return geo(x * om) - om ** h * x ** (h - 1) * geo(om / x)


def feshbach_pole(Delta, Gp, Rp, v):
    """All pole-port quantities in the embedded h-space."""
    h = len(v)
    w = Rp @ v
    w = w / np.linalg.norm(w)
    lam, W = np.linalg.eigh(Delta)
    lam1, lam2, esoft = lam[0], lam[1], W[:, 0]
    y = np.linalg.solve(Delta, w)
    s = 1.0 / float(w @ y)
    a = float(w @ (Delta @ w))
    beta = float(abs(w @ esoft))
    bet = W.T @ w
    rho = float(np.sum(bet[1:] ** 2 / lam[1:]))
    # bulk block via Householder w -> e1
    e1 = np.zeros(h)
    e1[0] = 1.0
    u = e1 - w
    nu = np.linalg.norm(u)
    H = np.eye(h) - 2.0 * np.outer(u / nu, u / nu) \
        if nu > 1e-12 else np.eye(h)
    Bc = H[:, 1:]
    rv = Bc.T @ (Delta @ w)
    G = Bc.T @ (Delta @ Bc)
    G = 0.5 * (G + G.T)
    gam, Gv = np.linalg.eigh(G)
    gmin = float(gam[0])
    ci = (Gv.T @ rv) ** 2 / gam
    tot = float(np.sum(ci))
    order = np.argsort(ci)[::-1]
    csum = np.cumsum(ci[order])
    n95 = int(np.searchsorted(csum, 0.95 * tot) + 1)
    return dict(s=s, a=a, lam1=float(lam1), lam2=float(lam2),
                beta=beta, rho=rho, gmin=gmin, rGr=tot,
                n95=n95, w=w, rv=rv, G=G, esoft=esoft,
                normr2=float(rv @ rv))


def neumann_enclosure(Delta, w, rv_embed, gmin, s_ref, kmax=3000):
    """Certified enclosure of r'G^-1 r via Neumann in the
    embedded space: A = I - Delta on w-perp; after 2t terms the
    tail is z_t'(I-A)^-1 z_t <= ||z_t||^2/gmin."""
    Pp = lambda x: x - w * float(w @ x)          # noqa: E731
    A = lambda x: Pp(x - Delta @ Pp(x))          # noqa: E731
    z = Pp(rv_embed)
    partial = float(z @ z)
    znorms = [float(np.linalg.norm(z))]
    zk = z
    tail = float("inf")
    used = kmax
    for k in range(1, kmax + 1):
        zk = A(zk)
        partial += float(z @ zk)
        znorms.append(float(np.linalg.norm(zk)))
        if k % 2 == 0:
            tail = znorms[k // 2] ** 2 / gmin
            if tail <= 0.05 * abs(s_ref):
                used = k
                break
    return partial, tail, used


def disp_rank_tau(Bp, Bm, d, D):
    U, sv, Vh, A2 = contractor(Bp, Bm)
    Cf = A2 @ U.conj().T
    L = Cf.shape[0]
    jj = np.arange(L)
    tau = np.where(jj <= L // 2, jj, L - jj) * (
        2.0 * math.pi / L) / D
    pos, neg = d > 0.0, d < 0.0
    Cres = Cf[np.ix_(neg, pos)]
    R = tau[neg][:, None] * Cres - Cres * tau[pos][None, :]
    uR, sR, vR = np.linalg.svd(R)
    rk = int(np.sum(sR > 1e-3 * sR[0]))
    return rk, uR[:, 0], vR[0], pos, neg, tau


# ================================================================= main
def main():
    section("PRIME.POLEPORT.KAPPA_LAW.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    zones = list(core.frame_a_zones())

    # ---------------- S1 + S2 per rung
    section("S1/S2 -- the kappa series + the analytic skeleton "
            "(all %d zones, h <= 900)" % len(zones))
    rows = []
    skipped = []
    w4_all = True
    w1max = w2max = w3max = 0.0
    corr_min = 1.0
    gen_cache = {}
    print("    kz    h    alpha  lam1      kappa  beta   a"
          "         rGr/a  n95  gmin/lam2  neuK  enclw/s")
    for kz in zones:
        out = build_rung(kz)
        rr, d, Bp, Bm, Fp, K, Gp, Rp, Delta, c_ar = out
        h, D, alpha = rr["h"], rr["D"], rr["alpha"]
        if h > 900:
            skipped.append(kz)
            continue
        L = Fp.shape[0]
        v = np.exp(0.5 * np.arange(h) * D)
        v = v / np.linalg.norm(v)
        fp = feshbach_pole(Delta, Gp, Rp, v)
        # W1: closed-form transform vs FFT
        Pc = pole_transform_closed(h, L, D)
        Pf = Fp @ v
        scale = np.linalg.norm(v_raw := np.exp(
            0.5 * np.arange(h) * D))
        w1 = float(np.linalg.norm(Pc / scale - Pf)
                   / np.linalg.norm(Pf))
        w1max = max(w1max, w1)
        # W2: a from densities
        P2 = np.abs(Pf) ** 2
        Ep = float(np.sum(d[d > 0] * P2[d > 0])) / (2.0 * L)
        Em = float(np.sum(-d[d < 0] * P2[d < 0])) / (2.0 * L)
        a_sym = 1.0 - Em / Ep
        w2 = abs(a_sym - fp["a"]) / max(abs(fp["a"]), 1e-300)
        w2max = max(w2max, w2)
        # W3: exact kappa decomposition
        kap = fp["s"] / fp["lam1"]
        w3 = abs(1.0 / kap - (fp["beta"] ** 2
                              + fp["lam1"] * fp["rho"])) * kap
        w3max = max(w3max, w3)
        # Cauchy-kernel correlation of |P|^2
        jj = np.arange(L)
        tau = np.where(jj <= L // 2, jj, L - jj) * (
            2.0 * math.pi / L) / D
        ck = 1.0 / (0.25 + tau ** 2)
        cc = float(np.corrcoef(P2, ck)[0, 1])
        corr_min = min(corr_min, cc)
        # Neumann enclosure
        rv_emb = Delta @ fp["w"] - fp["a"] * fp["w"]
        part, tail, used = neumann_enclosure(
            Delta, fp["w"], rv_emb, fp["gmin"], fp["s"])
        enclw = tail / abs(fp["s"])
        w4_ok = (part <= fp["rGr"] * (1 + 1e-8) + 1e-15
                 and fp["rGr"] <= part + tail
                 * (1 + 1e-8) + 1e-15)
        U0 = float(v @ (Gp @ v))
        w4_all &= w4_ok
        rows.append(dict(kz=kz, h=h, alpha=alpha, kap=kap,
                         beta=fp["beta"], a=fp["a"], s=fp["s"],
                         lam1=fp["lam1"], lam2=fp["lam2"],
                         rGr=fp["rGr"], n95=fp["n95"],
                         gmin=fp["gmin"], U0=U0, cc=cc,
                         enclw=enclw, neuK=used))
        if kz in GEN_RUNGS:
            gen_cache[kz] = (Bp, Bm, d, D, c_ar, rr["M"])
        print("    %-4d %-4d %.2f  %.3e %5.2f  %.3f  %.3e"
              " %.3f  %-3d  %.2f     %-5d %.2f"
              % (kz, h, alpha, fp["lam1"], kap, fp["beta"],
                 fp["a"], fp["rGr"] / fp["a"], fp["n95"],
                 fp["gmin"] / fp["lam2"], used, enclw),
              flush=True)
    print("    (skipped h > 900: %s)" % (skipped or "none"))

    kaps = {r["kz"]: r["kap"] for r in rows}
    reg_ok = all(KAPPA_REFS[k][0] <= kaps[k] <= KAPPA_REFS[k][1]
                 for k in KAPPA_REFS if k in kaps)
    bmax = max(r["beta"] for r in rows)
    reg_ok &= 0.80 <= bmax <= 0.88
    check("S1.1 [REGRESSIONS] kappa_POLE at kz 9/40 within the "
          "softport bands and the ladder-max beta in "
          "[0.80, 0.88] (kz9 %.3f, kz40 %.3f, beta_max %.3f)"
          % (kaps.get(9, -1), kaps.get(40, -1), bmax),
          reg_ok)
    # ceiling at anchors
    ceil_ok = True
    for kz in ANCHORS:
        out = build_rung(kz)
        Delta, Gp, Rp = out[8], out[6], out[7]
        lam, W = np.linalg.eigh(Delta)
        fpC = feshbach_pole(Delta, Gp, Rp,
                            np.linalg.solve(Rp, W[:, 0]))
        ceil_ok &= abs(fpC["s"] / fpC["lam1"] - 1.0) <= 1e-6
    check("S1.2 [CEILING] the target soft port gives kappa == "
          "1 to 1e-6 at all anchors", ceil_ok)
    check("S2.1 [W1+W2+W3] closed-form pole transform vs FFT "
          "(max %.1e), a == 1 - E-/E+ from the densities (max "
          "%.1e), kappa^-1 == beta^2 + lam1*rho (max %.1e) -- "
          "all <= 1e-8 on every rung"
          % (w1max, w2max, w3max),
          w1max <= 1e-8 and w2max <= 1e-8 and w3max <= 1e-8)
    check("S2.2 [W4] Neumann monotone consistency partial <= "
          "r'G^-1r <= partial + certified tail on every rung",
          w4_all)
    print("    Cauchy-kernel identification: min corr(|P|^2, "
          "1/(1/4+tau^2)) over rungs = %.4f -- the pole port "
          "reads the signed density through the Poisson kernel "
          "at s = 1/2" % corr_min)

    # fit-free law readouts (descriptive)
    kv = np.array([r["kap"] for r in rows])
    hv = np.array([float(r["h"]) for r in rows])
    av = np.array([r["alpha"] for r in rows])
    uv = np.array([r["U0"] for r in rows])
    lk = np.log(kv - 1.0)
    for nm, xx in (("log h", np.log(hv)), ("alpha", av),
                   ("log U0", np.log(uv))):
        cs = np.corrcoef(lk, xx)[0, 1]
        sl = np.polyfit(xx, lk, 1)[0]
        print("    law readout: log(kappa-1) vs %-7s: "
              "Pearson r %+.3f, slope %+.3f" % (nm, cs, sl))
    third = max(1, len(kv) // 3)
    print("    kappa first-third mean %.3f, last-third mean "
          "%.3f; last-10 Aitken limit %.3f"
          % (float(np.mean(kv[:third])),
             float(np.mean(kv[-third:])),
             aitken(kv[-10:])))
    n95v = [r["n95"] for r in rows]
    encl = [r["enclw"] for r in rows]
    frontier = next((r["kz"] for r in rows
                     if r["enclw"] > 0.5), None)
    print("    n95 range [%d, %d]; Neumann enclosure <= 0.1 s "
          "on %d/%d rungs, <= 0.5 s on %d/%d (frontier kz %s)"
          % (min(n95v), max(n95v),
             sum(1 for e in encl if e <= 0.1), len(encl),
             sum(1 for e in encl if e <= 0.5), len(encl),
             frontier))

    # ---------------- S3 generator law
    section("S3 -- the generator law (displacement rank + "
            "arm-weight identification per rung)")
    for kz in GEN_RUNGS:
        Bp, Bm, d, D, c_ar, M = gen_cache[kz]
        rk, u0, v0, pos, neg, tau = disp_rank_tau(Bp, Bm, d, D)
        dar = grid_density(c_ar)
        sims = []
        for snm, sp in (("sqrt|d|", np.sqrt(np.abs(d))),
                        ("sqrt|d_ar|", np.sqrt(np.abs(dar)))):
            su = sp[neg] / np.linalg.norm(sp[neg])
            sv = sp[pos] / np.linalg.norm(sp[pos])
            sims.append("%s u %.3f v %.3f"
                        % (snm, abs(float(np.abs(u0) @ su)),
                           abs(float(np.abs(v0) @ sv))))
        print("    kz %-3d rank@1e-3 %d | %s"
              % (kz, rk, " | ".join(sims)), flush=True)

    # ---------------- S4 discriminators
    section("S4 -- discriminators at kz 9 (Epstein x^2+5y^2, "
            "scramble seed 1)")
    rr9 = core.build_window(9)
    a9 = rr9["alpha"]
    N_E = int(math.floor(math.exp(2.0 * a9))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    disc_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        out = build_rung(9, **kw)
        rr, Gp, Rp, Delta = out[0], out[6], out[7], out[8]
        h, D = rr["h"], rr["D"]
        v = np.exp(0.5 * np.arange(h) * D)
        v = v / np.linalg.norm(v)
        fp = feshbach_pole(Delta, Gp, Rp, v)
        broke = fp["gmin"] < 0 or fp["s"] < 0
        disc_ok &= broke
        print("    %-8s: s %+.3e, gmin(G) %+.3e, lam1(Delta) "
              "%+.3e  -> premise/sign breaks: %s"
              % (nmc, fp["s"], fp["gmin"],
                 float(np.linalg.eigvalsh(Delta)[0]), broke),
              flush=True)
    check("S4.1 [DISCRIMINATOR] Epstein and scramble both "
          "break the pole-port Feshbach premise or the sign "
          "(gmin(G) < 0 or s < 0)", disc_ok)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + the positivity transfer")
    wards_ok = (w1max <= 1e-8 and w2max <= 1e-8
                and w3max <= 1e-8)
    n95_ok = max(n95v) <= 20
    encl_ok = max(encl) <= 0.1
    if wards_ok and n95_ok and encl_ok:
        verdict = "KAPPA-LAW-CLOSED"
    elif wards_ok and n95_ok:
        verdict = "KAPPA-LAW-PARTIAL"
    else:
        verdict = "KAPPA-EMPIRICAL-ONLY"
    cancel = [(r["a"] - r["s"]) / r["a"] for r in rows]
    print("\n  VERDICT: %s" % verdict)
    print("""
  POSITIVITY TRANSFER (task 3, honest): the exact skeleton is
  tau > 0  <=>  s > 0 at the pole port (Feshbach, bulk
  uniformly positive -- measured), and s = a - r'G^{-1}r with
  a = 1 - E-/E+ CLOSED FORM: the Poisson/Cauchy average of the
  signed density at the pole point s = 1/2 (corr >= %.3f).
  The cancellation ratio (a - s)/a runs %.2f -> %.2f along the
  ladder: the coupling term removes that fraction of the
  a-term before the floor remains.  Reduction vs relocation:
  the a-term is manifest source structure (one scalar, closed
  form), and the backflow r'G^{-1}r concentrates on n95 <= %d
  bulk modes -- the classical 'main term minus boundable term'
  shape EXISTS structurally, but the boundable term is not yet
  unconditionally bounded: its size is exactly what encodes
  the arithmetic.  Typed: this is a genuine reduction of FORM
  (matrix positivity -> one scalar inequality with closed-form
  leading term), while the HARDNESS is relocated into the
  concentrated coupling -- the remaining object is the
  uniform-in-h bound on a sum over ~%d bulk-mode couplings.
  NO RH claim.""" % (corr_min, cancel[0], cancel[-1],
                     max(n95v), max(n95v)))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


def aitken(x):
    x = np.asarray(x, float)
    num = x[2:] * x[:-2] - x[1:-1] ** 2
    den = x[2:] + x[:-2] - 2.0 * x[1:-1]
    good = np.abs(den) > 1e-12
    return float(np.mean(num[good] / den[good])) \
        if good.any() else float(x[-1])


if __name__ == "__main__":
    raise SystemExit(main())
