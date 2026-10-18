#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dirichlet_wall_anatomy_probe -- PRIME.FLOOR.DIRICHLET_ANATOMY.01:
the anatomy of the family wall (EXPLORATION ONLY, experiments/;
2026-08-08 probe 3, successor of PRIME.FLOOR.DIRICHLET_FAMILY.01).

WHAT PROBE 2 LEFT OPEN: all three real primitive characters carry the
floor with the SAME depth slope d log lam_min / d alpha ~ -1 as zeta,
the zeta level sits ~2x above the character levels, and the per-rung
fluctuations LOOK synchronised across the family.  This probe is a
MEASUREMENT INSTRUMENT, not a certificate: it dissects (A) the
scaling law and the synchronisation, (B) the soft-mode structure
(is the family wall rank-one-like, and is the wall DIRECTION shared
across objects?), and (C) the frequency content of the soft mode
against each object's OWN first zeros, computed independently.

FIREWALL NOTE (typed): L-function zeros enter the ANALYSIS side only
(the instrument that reads the measured soft mode), never the window
construction -- exactly the round-28+ instrument precedent (GUE /
pair-correlation probes).  The windows are built from primes and
closed archimedean data alone, as in probes 1-2.

TYPED HYPOTHESES (before running; the probe reports, it does not
assume): (H-sync) the per-rung log-margin fluctuations are strongly
positively correlated across the family -- the FLUCTUATION is window
geometry, the LEVEL is arithmetic.  (H-mode) two honest alternatives
typed: either the bottom modes of K_zeta and K_chi are essentially
the same direction (wall direction geometric, height arithmetic) or
they differ and carry object-specific frequency content.  (H-freq)
if object-specific: the dominant tau-frequency gamma* of each bottom
mode should sit near that object's OWN lowest zeros gamma_1 (zeta
14.13, chi_4 ~6.02, chi_3 ~8.04, chi_5 measured here) -- REPORTED
against the independently computed zero lists, gated only at the
level of the machinery wards.

VERDICT (frozen): ANATOMY-MEASURED (all wards pass; the three
findings typed from the frozen readouts) / ANATOMY-PARTIAL (a ward
or machinery gate broke -- typed).  The scaling/mode/frequency
findings themselves are REPORTED, never gated (unknown territory --
this probe generates the hypothesis for the next one).  NO RH claim,
NO GRH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/dirichlet_wall_anatomy_probe.py
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
PRIME.FLOOR.DIRICHLET_ANATOMY.01 spec v1 (2026-08-08, frozen before
run).  Windows/characters exactly as PRIME.FLOOR.DIRICHLET_FAMILY.01
(chi_3/chi_4/chi_5 real primitive; grid D = 2 alpha / M -- the W2
lesson of probe 2 encoded).  WARDS (gated): W1 cross-probe
regression kz-9 lam_min(K_chi4) == +1.591319e-04 (abs <= 1e-9).
W2 mpmath L-machinery: L(3, chi) via q^{-s} sum chi(r) zeta_H(s,
r/q) == truncated Dirichlet series (rel <= 1e-10, all three chi);
Lambda(1/2 + it) real on the line: max |Im|/|Lambda| <= 1e-12 over
the scan grid (points with |Lambda| >= 1e-30), all four objects.
W3 zeta literature anchor: first Hardy-scan zero == 14.134725142
(abs <= 1e-6).  READOUTS (reported, never gated; frozen recipes):
(A) SCALING on the 42 trend rungs (h <= 900): lam_min e^alpha
min/median/max per object; Spearman(log lam_min(chi), log
lam_min(zeta)) across rungs per character -- H-sync bar typed at
+0.5 for the VERDICT STRING only (finding, not a check); median
ratio lam_min(chi)/lam_min(zeta).  (B) MODE on the anchor rungs
{9, 26}: two lowest eigenpairs of K per object; gap lam2/lam1;
cross-object bottom-mode overlaps |<u_chi, u_zeta>| and
|<u_chi_i, u_chi_j>|; center of mass of |u|^2 in r/h.  (C)
FREQUENCY on {9, 26}: FFT of the odd-extended zero-padded bottom
mode on the L-grid (cdcore geometry), gamma = (2 pi j / L)/D,
top-3 spectral peaks (j >= 1, local maxima) vs the first five zeros
of the SAME object from the mpmath Hardy scan (t in (0.2, 32],
step 0.2, bisection 200 steps, mp.dps 30); resolution 2 pi/(L D)
printed.  VERDICT: ANATOMY-MEASURED iff W1 + W2 + W3 pass (the
findings are typed into the verdict string from the frozen
readouts); else ANATOMY-PARTIAL.  Float64 windows, mpmath dps 30
zeros; NO RH/GRH claim; writes nothing; v563 READ-ONLY.
"""

CONSTRUCTION = (9, 12, 13, 26)
HOLDOUT = (40, 49, 60)
ANCHORS = (9, 26)
H_TREND_CAP = 900
CHI4_KZ9_REF = 1.591319e-04
ZETA_G1_REF = 14.134725142
T_SCAN_MAX = 32.0
T_SCAN_STEP = 0.2
N_ZEROS_KEEP = 5
BANNED_IDS = ("nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHARACTERS = (("chi_3", 3, 1), ("chi_4", 4, 1), ("chi_5", 5, 0))
OBJECTS = ("zeta",) + tuple(nm for nm, _q, _a in CHARACTERS)

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


def spearman(a, b):
    ra = np.argsort(np.argsort(a)).astype(float)
    rb = np.argsort(np.argsort(b)).astype(float)
    ra -= ra.mean()
    rb -= rb.mean()
    dn = math.sqrt(float(ra @ ra) * float(rb @ rb))
    return float(ra @ rb) / dn if dn > 0 else 0.0


# ------------------------------------------------ family machinery (probe 2)
def chi_val(name, n):
    if name == "chi_3":
        r = n % 3
        return 0.0 if r == 0 else (1.0 if r == 1 else -1.0)
    if name == "chi_4":
        r = n % 4
        return 0.0 if r % 2 == 0 else (1.0 if r == 1 else -1.0)
    r = n % 5
    if r == 0:
        return 0.0
    return 1.0 if r in (1, 4) else -1.0


def kdiff(w):
    return np.exp(-0.5 * w) / (1.0 + np.exp(-w))


def smear_lags(M, D, n_gl=48):
    gx, gw = np.polynomial.legendre.leggauss(n_gl)
    out = np.zeros(M)
    mid, half = 0.5 * D, 0.5 * D
    w0 = mid + half * gx
    out[0] = 2.0 * half * float(np.dot(gw, (1.0 - w0 / D)
                                       * kdiff(w0)))
    ss = np.arange(1, M) * D
    for lo, hi in ((ss - D, ss), (ss, ss + D)):
        mid = 0.5 * (lo + hi)
        half = 0.5 * (hi - lo)
        w = mid[:, None] + half[:, None] * gx[None, :]
        val = (1.0 - np.abs(ss[:, None] - w) / D) * kdiff(w)
        out[1:] += half * (val @ gw)
    return out


def geometry(kz):
    """build_window geometry; grid D = 2 alpha / M (probe 2, W2)."""
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return alpha, 2.0 * alpha / M, M, M // 2


def chi_comb(name, alpha):
    ka = core.atoms_in(alpha)
    nn = core._NN[:ka]
    sgn = np.array([chi_val(name, int(n)) for n in nn])
    keep = sgn != 0.0
    return (core.U_ALL[:ka][keep].copy(),
            sgn[keep] * core.MU_ALL[:ka][keep])


class Rung:
    def __init__(self, kz):
        self.kz = kz
        self.alpha, self.D, self.M, self.h = geometry(kz)
        self.c_ar = core.arch_lags(self.M, self.D)
        self.smear = smear_lags(self.M, self.D)
        ka = core.atoms_in(self.alpha)
        c_at, _ = core.atom_lags_at(self.alpha, self.M,
                                    core.U_ALL[:ka],
                                    core.MU_ALL[:ka])
        self.c = {"zeta": self.c_ar + c_at}
        for name, q, a in CHARACTERS:
            uu, mm = chi_comb(name, self.alpha)
            c_atx, _ = core.atom_lags_at(self.alpha, self.M, uu, mm)
            cx = (self.c_ar + c_atx).copy()
            cx[0] += math.log(q)
            if a == 1:
                cx = cx + self.smear
            self.c[name] = cx

    def floor(self, name):
        return float(np.linalg.eigvalsh(
            core.odd_toeplitz(self.c[name], self.M))[0])

    def bottom(self, name, k=2):
        ev, U = np.linalg.eigh(
            core.odd_toeplitz(self.c[name], self.M))
        return ev[:k], U[:, :k]


def mode_spectrum(u, h, M, D, n_peaks=3):
    """FFT of the odd-extended, zero-padded bottom mode on the
    L-grid (cdcore geometry); returns (gamma_res, peaks) with peaks
    = [(gamma, rel_power)] at interior local maxima."""
    L = 2 * M - 2
    E = np.zeros((2 * h, h))
    E[:h] = np.eye(h)
    E[h:] = -np.eye(h)[::-1]
    z = np.fft.fft(np.concatenate([E @ u, np.zeros(L - M)]))
    p = np.abs(z[:L // 2]) ** 2
    res = (2.0 * math.pi / L) / D
    jj = [j for j in range(1, L // 2 - 1)
          if p[j] >= p[j - 1] and p[j] >= p[j + 1]]
    jj.sort(key=lambda j: -p[j])
    pmax = max(p[j] for j in jj) if jj else 1.0
    return res, [((2.0 * math.pi * j / L) / D, float(p[j] / pmax))
                 for j in jj[:n_peaks]]


# ------------------------------------------------ mpmath zero machinery
def make_lambda(name):
    """Completed Lambda(1/2 + it), REAL on the line for zeta and for
    real primitive chi (Lambda(s) = Lambda(1-s), real coefficients).
    ANALYSIS INSTRUMENT ONLY."""
    from mpmath import mp
    if name == "zeta":
        def lam(t):
            s = mp.mpf("0.5") + mp.mpc(0, 1) * t
            return (mp.pi ** (-s / 2) * mp.gamma(s / 2)
                    * mp.zeta(s))
        return lam
    q = {"chi_3": 3, "chi_4": 4, "chi_5": 5}[name]
    a = {"chi_3": 1, "chi_4": 1, "chi_5": 0}[name]

    def lfun(s):
        from mpmath import mp
        tot = mp.mpc(0)
        for r in range(1, q):
            cv = chi_val(name, r)
            if cv != 0.0:
                tot += cv * mp.zeta(s, mp.mpf(r) / q)
        return q ** (-s) * tot

    def lam(t):
        from mpmath import mp
        s = mp.mpf("0.5") + mp.mpc(0, 1) * t
        return ((mp.mpf(q) / mp.pi) ** ((s + a) / 2)
                * mp.gamma((s + a) / 2) * lfun(s))
    return lam


def hardy_zeros(name, t_max, step, n_keep):
    """Sign-scan + bisection zeros of the real Lambda on the line;
    returns (zeros, worst relative imaginary part)."""
    from mpmath import mp
    lam = make_lambda(name)
    tt = np.arange(step, t_max + 1e-9, step)
    vals = []
    worst_im = 0.0
    for t in tt:
        v = lam(mp.mpf(float(t)))
        m = abs(v)
        if m > mp.mpf("1e-30"):
            worst_im = max(worst_im, float(abs(v.imag) / m))
        vals.append(float(v.real))
    zeros = []
    for i in range(len(tt) - 1):
        if vals[i] * vals[i + 1] < 0.0:
            lo, hi = float(tt[i]), float(tt[i + 1])
            flo = vals[i]
            for _ in range(200):
                mid = 0.5 * (lo + hi)
                fm = float(lam(mp.mpf(mid)).real)
                if flo * fm <= 0.0:
                    hi = mid
                else:
                    lo, flo = mid, fm
                if hi - lo < 1e-11:
                    break
            zeros.append(0.5 * (lo + hi))
            if len(zeros) >= n_keep:
                break
    return zeros, worst_im


# ================================================================= main
def main():
    section("PRIME.FLOOR.DIRICHLET_ANATOMY.01 -- the anatomy of "
            "the family wall (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim, NO GRH claim.  Zeros enter ANALYSIS "
          "only, never construction.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no comb/window oracles; the "
          "mpmath zero scan is the DECLARED analysis instrument)",
          not ast_scan(BANNED_IDS))

    from mpmath import mp
    mp.dps = 30

    # ---------------- S1 wards
    section("S1 -- WARDS: cross-probe regression, mpmath "
            "machinery, zeta literature anchor")
    r9 = Rung(9)
    f4 = r9.floor("chi_4")
    dev4 = abs(f4 - CHI4_KZ9_REF)
    check("W1 [CROSS-PROBE REGRESSION] kz-9 lam_min(K_chi4) = "
          "%+.6e vs frozen %+.6e (abs dev %.1e <= 1e-9)"
          % (f4, CHI4_KZ9_REF, dev4), dev4 <= 1e-9)
    ok_l = True
    for name, q, a in CHARACTERS:
        s3 = mp.mpf(3)
        via_h = q ** (-s3) * sum(
            chi_val(name, r) * mp.zeta(s3, mp.mpf(r) / q)
            for r in range(1, q) if chi_val(name, r) != 0.0)
        direct = sum(chi_val(name, n) / mp.mpf(n) ** 3
                     for n in range(1, 200001))
        rel = float(abs(via_h - direct) / abs(direct))
        ok_l &= rel <= 1e-10
        print("    %s: L(3) Hurwitz route vs series rel dev %.1e"
              % (name, rel))
    check("W2a [L-MACHINERY] L(3, chi) via Hurwitz zeta == "
          "truncated Dirichlet series (rel <= 1e-10, all three)",
          ok_l)
    zeros = {}
    ok_im = True
    for name in OBJECTS:
        zs, wim = hardy_zeros(name, T_SCAN_MAX, T_SCAN_STEP,
                              N_ZEROS_KEEP)
        zeros[name] = zs
        ok_im &= wim <= 1e-12
        print("    %-6s: first zeros %s   (worst |Im|/|Lambda| "
              "%.1e)" % (name,
                         ", ".join("%.4f" % z for z in zs), wim))
    check("W2b [REALITY ON THE LINE] max |Im Lambda|/|Lambda| <= "
          "1e-12 on the scan grid for all four objects (the "
          "functional-equation reality proof holds numerically)",
          ok_im)
    devz = abs(zeros["zeta"][0] - ZETA_G1_REF)
    check("W3 [LITERATURE ANCHOR] zeta Hardy-scan gamma_1 = "
          "%.9f vs 14.134725142 (abs dev %.1e <= 1e-6)"
          % (zeros["zeta"][0], devz), devz <= 1e-6)

    # ---------------- S2 the scaling law + synchronisation
    section("S2 -- SCALING + SYNC (42 trend rungs, reported)")
    fz = [kz for kz in core.frame_a_zones()
          if geometry(kz)[3] <= H_TREND_CAP]
    logs = {nm: [] for nm in OBJECTS}
    aa = []
    scaled = {nm: [] for nm in OBJECTS}
    for kz in fz:
        rg = Rung(kz)
        aa.append(rg.alpha)
        for nm in OBJECTS:
            v = rg.floor(nm)
            logs[nm].append(math.log(v))
            scaled[nm].append(v * math.exp(rg.alpha))
    aa = np.array(aa)
    print("    lam_min * e^alpha per object (does e^{-alpha} "
          "capture the law?):")
    for nm in OBJECTS:
        sc = np.array(scaled[nm])
        print("      %-6s: min %.4f  median %.4f  max %.4f  "
              "(spread x%.1f)"
              % (nm, sc.min(), float(np.median(sc)), sc.max(),
                 sc.max() / sc.min()))
    sync = {}
    for nm, _q, _a in CHARACTERS:
        sync[nm] = spearman(np.array(logs[nm]),
                            np.array(logs["zeta"]))
    med_ratio = {nm: float(np.median(
        np.exp(np.array(logs[nm]) - np.array(logs["zeta"]))))
        for nm, _q, _a in CHARACTERS}
    print("    H-sync: Spearman(log lam_min(chi), log lam_min("
          "zeta)) across rungs: %s"
          % ", ".join("%s %+.2f" % (nm, sync[nm]) for nm in sync))
    print("    level: median lam_min(chi)/lam_min(zeta): %s"
          % ", ".join("%s %.2f" % (nm, med_ratio[nm])
                      for nm in med_ratio))
    check("S2.1 [SCALING/SYNC REPORTED] table + statistics "
          "printed (findings typed in the verdict; instrument "
          "gate only)", True)

    # ---------------- S3 the soft mode
    section("S3 -- THE SOFT MODE at the anchors %s" % (ANCHORS,))
    modes = {}
    for kz in ANCHORS:
        rg = r9 if kz == 9 else Rung(kz)
        modes[kz] = {}
        print("    kz %d (h = %d, D = %.5f):" % (kz, rg.h, rg.D))
        for nm in OBJECTS:
            ev, U = rg.bottom(nm)
            u = U[:, 0]
            rr_ = np.arange(rg.h)
            com = float(np.sum(rr_ * u ** 2) / np.sum(u ** 2)
                        / rg.h)
            modes[kz][nm] = dict(ev=ev, u=u, rg=rg, com=com)
            print("      %-6s: lam1 %+.3e  lam2 %+.3e  gap "
                  "lam2/lam1 %5.1f  mode CoM r/h = %.2f"
                  % (nm, ev[0], ev[1], ev[1] / ev[0], com))
        uz = modes[kz]["zeta"]["u"]
        ols = ["|<%s, zeta>| = %.3f"
               % (nm, abs(float(modes[kz][nm]["u"] @ uz)))
               for nm, _q, _a in CHARACTERS]
        o34 = abs(float(modes[kz]["chi_3"]["u"]
                        @ modes[kz]["chi_4"]["u"]))
        o45 = abs(float(modes[kz]["chi_4"]["u"]
                        @ modes[kz]["chi_5"]["u"]))
        print("      overlaps: %s; |<chi_3, chi_4>| = %.3f, "
              "|<chi_4, chi_5>| = %.3f"
              % ("; ".join(ols), o34, o45))
    check("S3.1 [MODE REPORTED] eigenpairs, gaps, centers of "
          "mass, cross-object overlaps printed", True)

    # ---------------- S4 the frequency reading
    section("S4 -- FREQUENCY: bottom-mode spectrum vs the "
            "object's OWN first zeros")
    match_tab = []
    for kz in ANCHORS:
        print("    kz %d:" % kz)
        for nm in OBJECTS:
            md = modes[kz][nm]
            rg = md["rg"]
            res, peaks = mode_spectrum(md["u"], rg.h, rg.M, rg.D)
            z1 = zeros[nm][0]
            best = min((abs(g - z1), g) for g, _p in peaks)[1] \
                if peaks else float("nan")
            match = abs(best - z1) <= 1.5 * res
            match_tab.append((kz, nm, match))
            print("      %-6s: res %.3f | peaks %s | own zeros "
                  "%s | nearest peak to gamma_1: %.3f (|dev| "
                  "%.3f, <= 1.5 res: %s)"
                  % (nm, res,
                     ", ".join("%.2f(%.2f)" % (g, p)
                               for g, p in peaks),
                     ", ".join("%.2f" % z for z in zeros[nm]),
                     best, abs(best - z1), match))
    check("S4.1 [FREQUENCY REPORTED] spectra vs own zero lists "
          "printed on both anchors (H-freq typed in verdict)",
          True)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + typed findings")
    wards_ok = all(ok for (nm, ok) in CHECKS
                   if nm.startswith(("W1", "W2", "W3")))
    verdict = "ANATOMY-MEASURED" if wards_ok else "ANATOMY-PARTIAL"
    sync_high = all(v >= 0.5 for v in sync.values())
    n_match = sum(1 for _kz, _nm, m in match_tab if m)
    print("\n  VERDICT: %s" % verdict)
    print("""
  TYPED FINDINGS (from the frozen readouts above):
  (1) H-sync %s: Spearman %s (bar +0.5) -- %s
  (2) levels: median chi/zeta ratios %s
  (3) H-freq: %d/%d (object, anchor) pairs have a bottom-mode
      spectral peak within 1.5 grid-resolutions of the object's
      OWN gamma_1 -- see the table for which.
  All findings are INSTRUMENT READINGS on finite windows; the next
  probe owns any gate built on them.  NO RH claim, NO GRH claim."""
          % ("HOLDS" if sync_high else "FAILS",
             ", ".join("%s %+.2f" % (nm, sync[nm])
                       for nm in sync),
             "the fluctuation is shared (geometry), the level is "
             "object-specific (arithmetic)" if sync_high else
             "the fluctuations are NOT shared -- the geometric "
             "reading dies",
             ", ".join("%s %.2f" % (nm, med_ratio[nm])
                       for nm in med_ratio),
             n_match, len(match_tab)))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
