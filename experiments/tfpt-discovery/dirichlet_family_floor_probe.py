#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""dirichlet_family_floor_probe -- PRIME.FLOOR.DIRICHLET_FAMILY.01:
the chi_4 finding extended to a FAMILY of real primitive characters,
plus the depth trend of the margin (EXPLORATION ONLY, experiments/;
2026-08-08 afternoon probe 2, successor of
PRIME.FLOOR.DIRICHLET_L4.01).

THE QUESTION: probe 1 showed the deployed window mechanism carries
over to L(s, chi_4) with a razor-thin margin (no cushion despite the
missing pole).  Three follow-ups, typed BEFORE running:
(a) chi_3 mod 3 (odd, a = 1, q = 3): same digamma-3/4 kernel as
    chi_4, different conductor constant log(3) and different comb --
    does the floor carry?
(b) chi_5 mod 5 (the quadratic character, EVEN, a = 0, q = 5): the
    clean DIFFERENTIAL test -- the archimedean kernel is IDENTICAL to
    zeta's (Gamma(s/2), digamma 1/4); the window differs from zeta by
    ONLY the lag-0 constant +log(5) and the signed comb.  If the
    floor carries here too, the mechanism is comb-and-constant deep,
    not kernel-tuned.
(c) THE DEPTH TREND: lam_min vs alpha across every reachable frame-A
    rung (h <= 900) for zeta and all three characters -- does the
    chi-margin shrink like the zeta margin (the wall is universal)
    or diverge from it (the wall is zeta-special)?

BOOKKEEPING (derived, wards below): explicit formula for a real
primitive chi mod q with parity a in {0, 1}: zero side ==
[DG_{1/4 + a/2} + log(q/pi) g(0)] - C_{chi Lambda}, no pole.  In the
deployed lag convention: c_chi = c_ar_zeta + log(q) tri_s
+ [a == 1] * SMEAR(e^{-w/2}/(1 + e^{-w})) + c_at_chi, with the smear
exactly probe 1's DELTA-integral (kernel difference of digamma 1/4 vs
3/4, sympy-proven there) and c_at_chi the tent assembly at uu = log n,
mm = 2 chi(n) Lambda(n)/sqrt(n) over prime powers with chi(n) != 0.

VERDICT (frozen): FAMILY-CONTRACTS-DISCRIMINATING (floor >= 0 for all
three characters on all 7 rungs AND every kz-9 sign-scramble control
indefinite) / FAMILY-CONTRACTS-CUSHIONED (floors hold, >= 1 control
stays PSD -- typed) / FAMILY-INDEFINITE (a floor fails -- typed per
character and rung; a statement about THIS window form, NOT about
GRH) / FAMILY-PARTIAL (wards or Loewner consistency broken).  The
depth trend is REPORTED fit-free (Spearman + log-log slope), never
gated.  NO RH claim, NO GRH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/dirichlet_family_floor_probe.py
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
PRIME.FLOOR.DIRICHLET_FAMILY.01 spec v1 (2026-08-08, frozen before
run).  Characters (real, primitive, values from residue tables, no
oracles): chi_3 mod 3 (1 -> +1, 2 -> -1, 0 mod 3 -> 0; odd, a = 1),
chi_4 mod 4 (1 -> +1, 3 -> -1, even -> 0; odd, a = 1), chi_5 mod 5
(quadratic residues {1, 4} -> +1, {2, 3} -> -1, 0 mod 5 -> 0; even,
a = 0).  Window: c_chi = c_ar_zeta + log(q) tri_s + [a == 1] SMEAR
+ c_at_chi (SMEAR = probe 1's Gauss-Legendre-48 tent integral of
e^{-w/2}/(1 + e^{-w}); lag grid: only i = 0 near-field).  W1 parity
ward: chi(q - 1) == +1 iff a == 0 for each character, and complete
multiplicativity chi(m n) == chi(m) chi(n) on 2000 random pairs.
W2 chi_4 cross-probe regression: this probe's kz-9 lam_min(K_chi4)
== +1.591319e-04 (abs dev <= 1e-9; frozen from
PRIME.FLOOR.DIRICHLET_L4.01's first run).  W3 even-character
bookkeeping: the chi_5 lag vector == c_ar_zeta + log(5) at lag 0
+ c_at_chi5 EXACTLY (max abs dev 0.0; the a = 0 path adds no smear).
S2 gate: lam_min(K_chi) >= -1e-12 ||K||_2 for all three characters
on the CDCORE seven rungs -- construction {9, 12, 13, 26}, FROZEN
HOLDOUT {40, 49, 60}.  S3 gate: sign(1 - ||C_chi||) ==
sign(lam_min(K_chi)) wherever the density splits (band 1e-9), all
characters, all 7 rungs.  S4 THE DEPTH TREND (reported, never
gated): every frame-A rung with h <= 900, subsampled to <= 24 rungs
(every k-th by count, deepest always kept), lam_min for zeta + all
three characters; per character: Spearman(log lam_min, alpha) and
the log-log slope of lam_min vs e^alpha, side by side with zeta's;
ratio profile lam_min(chi)/lam_min(zeta) printed.  S5 controls at
kz 9: per character ONE sign-scramble (seed 2, positions/magnitudes
kept, random +-1 replacing chi(n)); expectation typed pre-run as
EXPECTED-NEGATIVE, honestly NOT structural (routes to CUSHIONED,
not to a kill).  VERDICT: FAMILY-CONTRACTS-DISCRIMINATING iff
W1-W3 + S2 + S3 pass AND all three controls indefinite;
FAMILY-CONTRACTS-CUSHIONED iff W1-W3 + S2 + S3 pass and >= 1
control PSD; FAMILY-INDEFINITE iff S2 fails (typed per character/
rung; a statement about THIS window form, not about GRH); else
FAMILY-PARTIAL.  Float64; NO RH/GRH claim; writes nothing; v563
READ-ONLY.
"""

CONSTRUCTION = (9, 12, 13, 26)
HOLDOUT = (40, 49, 60)
RUNGS = CONSTRUCTION + HOLDOUT
KZ_CTRL = 9
SEED_SIGN = 2
H_TREND_CAP = 900
N_TREND_MAX = 24
CHI4_KZ9_REF = 1.591319e-04     # frozen from probe 1's first run
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHARACTERS = (("chi_3", 3, 1), ("chi_4", 4, 1), ("chi_5", 5, 0))

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


# ---------------------------------------------------- characters (tables)
def chi_val(name, n):
    """Real primitive character values from residue tables only."""
    if name == "chi_3":
        r = n % 3
        return 0.0 if r == 0 else (1.0 if r == 1 else -1.0)
    if name == "chi_4":
        r = n % 4
        return 0.0 if r % 2 == 0 else (1.0 if r == 1 else -1.0)
    r = n % 5                                     # chi_5
    if r == 0:
        return 0.0
    return 1.0 if r in (1, 4) else -1.0


# ---------------------------------------------------- arch delta (probe 1)
def kdiff(w):
    """digamma-1/4 minus digamma-3/4 kernel difference:
    e^{-w/2}/(1 + e^{-w}) (sympy-proven in probe 1)."""
    return np.exp(-0.5 * w) / (1.0 + np.exp(-w))


def smear_lags(M, D, n_gl=48):
    """Probe 1's DELTA integral WITHOUT the conductor constant:
    int [tent(s-w) + tent(s+w)] kdiff(w) dw at grid lags s = iD."""
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


# ---------------------------------------------------- window machinery
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


def geometry(kz):
    """Frame-A geometry, the build_window formulas verbatim.  NOTE
    (the W2 ward caught this in run 1): D_k sizes M only -- the
    ACTUAL grid spacing is atom_lags_at's D = 2 alpha / M, which is
    what build_window returns as rr['D'] and what arch_lags must
    use."""
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return alpha, 2.0 * alpha / M, M, M // 2


def chi_comb(name, alpha, rng_sign=None):
    ka = core.atoms_in(alpha)
    nn = core._NN[:ka]
    sgn = np.array([chi_val(name, int(n)) for n in nn])
    keep = sgn != 0.0
    uu = core.U_ALL[:ka][keep].copy()
    sg = sgn[keep]
    if rng_sign is not None:
        sg = rng_sign.choice([-1.0, 1.0], size=int(np.sum(keep)))
    return uu, sg * core.MU_ALL[:ka][keep]


class RungCache:
    """Shared per-rung pieces: arch lags, smear lags, zeta floor."""

    def __init__(self, kz):
        self.kz = kz
        self.alpha, self.D, self.M, self.h = geometry(kz)
        self.c_ar = core.arch_lags(self.M, self.D)
        self.smear = smear_lags(self.M, self.D)
        ka = core.atoms_in(self.alpha)
        c_at, _ = core.atom_lags_at(self.alpha, self.M,
                                    core.U_ALL[:ka],
                                    core.MU_ALL[:ka])
        self.tau_z = float(np.linalg.eigvalsh(
            core.odd_toeplitz(self.c_ar + c_at, self.M))[0])

    def chi_lags(self, name, q, a, rng_sign=None):
        uu, mm = chi_comb(name, self.alpha, rng_sign=rng_sign)
        c_at, _ = core.atom_lags_at(self.alpha, self.M, uu, mm)
        c = self.c_ar + c_at
        c = c.copy()
        c[0] += math.log(q)
        if a == 1:
            c = c + self.smear
        return c

    def chi_floor(self, name, q, a, rng_sign=None,
                  with_contractor=False):
        c = self.chi_lags(name, q, a, rng_sign=rng_sign)
        K = core.odd_toeplitz(c, self.M)
        ev = np.linalg.eigvalsh(K)
        out = dict(lmin=float(ev[0]), lmax=float(ev[-1]))
        if not with_contractor:
            return out
        d = grid_density(c)
        L = 2 * self.M - 2
        pos, neg = d > 0.0, d < 0.0
        out["n_neg"] = int(np.sum(neg))
        if pos.any() and neg.any():
            F = np.fft.fft(np.vstack([odd_extend_mat(self.h),
                                      np.zeros((L - self.M,
                                                self.h))]), axis=0)
            wp = np.sqrt(d[pos] / (2.0 * L))
            wm = np.sqrt(-d[neg] / (2.0 * L))
            Bp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))[:, None] * F
            Gp = np.real(Bp.conj().T @ Bp)
            Mp = F[neg] @ np.linalg.solve(Gp, F[pos].conj().T)
            Cres = wm[:, None] * Mp * wp[None, :]
            out["Cnorm"] = float(np.linalg.svd(
                Cres, compute_uv=False)[0])
        return out


# ================================================================= main
def main():
    section("PRIME.FLOOR.DIRICHLET_FAMILY.01 -- chi_3 / chi_4 / "
            "chi_5 + the depth trend (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim, NO GRH claim.  Construction %s, frozen "
          "holdout %s." % (CONSTRUCTION, HOLDOUT))
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    # ---------------- S1 wards
    section("S1 -- WARDS: parity, cross-probe regression, even-"
            "character bookkeeping")
    rng = np.random.default_rng(7)
    par_ok, mult_ok = True, True
    for name, q, a in CHARACTERS:
        par_ok &= (chi_val(name, q - 1) == 1.0) == (a == 0)
        mn = rng.integers(1, 10 ** 6, size=(2000, 2))
        for m_, n_ in mn:
            if abs(chi_val(name, int(m_) * int(n_))
                   - chi_val(name, int(m_))
                   * chi_val(name, int(n_))) > 0.0:
                mult_ok = False
                break
    check("W1 [PARITY + MULTIPLICATIVITY] chi(q - 1) == +1 iff even"
          " (chi_3 odd, chi_4 odd, chi_5 even) and chi(mn) == "
          "chi(m) chi(n) on 2000 random pairs per character",
          par_ok and mult_ok)
    caches = {kz: RungCache(kz) for kz in RUNGS}
    r9 = caches[KZ_CTRL]
    f4 = r9.chi_floor("chi_4", 4, 1)
    dev4 = abs(f4["lmin"] - CHI4_KZ9_REF)
    check("W2 [CROSS-PROBE REGRESSION] kz-9 lam_min(K_chi4) = "
          "%+.6e vs probe 1's frozen %+.6e (abs dev %.1e <= 1e-9)"
          % (f4["lmin"], CHI4_KZ9_REF, dev4), dev4 <= 1e-9)
    c5 = r9.chi_lags("chi_5", 5, 0)
    uu5, mm5 = chi_comb("chi_5", r9.alpha)
    c_at5, _ = core.atom_lags_at(r9.alpha, r9.M, uu5, mm5)
    ref5 = r9.c_ar + c_at5
    ref5 = ref5.copy()
    ref5[0] += math.log(5.0)
    dev5 = float(np.max(np.abs(c5 - ref5)))
    check("W3 [EVEN-CHARACTER BOOKKEEPING] the chi_5 lag vector == "
          "zeta arch + log(5) at lag 0 + signed comb EXACTLY (max "
          "abs dev %.1e == 0; the a = 0 path adds no smear)" % dev5,
          dev5 == 0.0)

    # ---------------- S2 the family floor
    section("S2 -- THE FAMILY FLOOR on 7 rungs (chi_3, chi_4, "
            "chi_5 vs zeta)")
    print("    kz    h    alpha  | lam_min: chi_3       chi_4"
          "       chi_5       zeta")
    floor_ok = True
    floors = {nm: {} for nm, _q, _a in CHARACTERS}
    for kz in RUNGS:
        rc = caches[kz]
        row = []
        for name, q, a in CHARACTERS:
            f = rc.chi_floor(name, q, a, with_contractor=True)
            floors[name][kz] = f
            floor_ok &= f["lmin"] >= -1e-12 * abs(f["lmax"])
            row.append(f["lmin"])
        print("    %-4d %-4d %-6.3f | %+.3e  %+.3e  %+.3e  %+.3e%s"
              % (kz, rc.h, rc.alpha, row[0], row[1], row[2],
                 rc.tau_z,
                 "  (holdout)" if kz in HOLDOUT else ""),
              flush=True)
    check("S2.1 [THE FAMILY FLOOR] lam_min(K_chi) >= -1e-12 ||K|| "
          "for ALL THREE characters on ALL 7 rungs (construction + "
          "blind holdouts) -- odd (a = 1, kernel-shifted) AND even "
          "(a = 0, comb-and-constant only) characters carry the "
          "floor", floor_ok)

    # ---------------- S3 Loewner
    section("S3 -- THE LOEWNER READING (all characters, all rungs)")
    loew_ok = True
    for name, _q, _a in CHARACTERS:
        worst = None
        for kz in RUNGS:
            f = floors[name][kz]
            if "Cnorm" not in f:
                continue
            gap = 1.0 - f["Cnorm"]
            cons = (gap >= -1e-9) == (f["lmin"]
                                      >= -1e-12 * f["lmax"])
            loew_ok &= cons
            if worst is None or gap < worst[1]:
                worst = (kz, gap)
        print("    %-6s: tightest contraction gap 1 - ||C|| = "
              "%+.3e at kz %d" % (name, worst[1], worst[0]))
    check("S3.1 [LOEWNER CONSISTENCY] sign(1 - ||C_chi||) == "
          "sign(lam_min(K_chi)) for every character on every rung "
          "where the density splits", loew_ok)

    # ---------------- S4 the depth trend
    section("S4 -- THE DEPTH TREND (reported fit-free, never "
            "gated): every frame-A rung h <= %d" % H_TREND_CAP)
    fz = [kz for kz in core.frame_a_zones()
          if geometry(kz)[3] <= H_TREND_CAP]
    step = max(1, len(fz) // N_TREND_MAX)
    trend_kz = sorted(set(fz[::step]) | {fz[-1]})
    print("    %d reachable rungs, %d sampled (every %d-th + "
          "deepest)" % (len(fz), len(trend_kz), step))
    print("    kz    h    alpha  | lam_min: chi_3       chi_4"
          "       chi_5       zeta      | ratio c4/z")
    tr = {nm: [] for nm, _q, _a in CHARACTERS}
    tz, aa = [], []
    for kz in trend_kz:
        rc = caches.get(kz) or RungCache(kz)
        caches[kz] = rc
        row = []
        for name, q, a in CHARACTERS:
            f = rc.chi_floor(name, q, a)
            tr[name].append(f["lmin"])
            row.append(f["lmin"])
        tz.append(rc.tau_z)
        aa.append(rc.alpha)
        print("    %-4d %-4d %-6.3f | %+.3e  %+.3e  %+.3e  "
              "%+.3e | %5.2f"
              % (kz, rc.h, rc.alpha, row[0], row[1], row[2],
                 rc.tau_z, row[1] / rc.tau_z), flush=True)
    aa = np.array(aa)
    tz = np.array(tz)
    print("\n    trend statistics (log lam_min vs alpha; zeta "
          "slope for scale):")
    all_pos = {}
    for name in list(tr) + ["zeta"]:
        v = np.array(tr[name]) if name != "zeta" else tz
        all_pos[name] = bool(np.all(v > 0.0))
        if all_pos[name]:
            sl = np.polyfit(aa, np.log(v), 1)[0]
            sp = spearman(np.log(v), aa)
            print("      %-6s: all positive; slope d log lam_min /"
                  " d alpha = %+.3f, Spearman = %+.2f"
                  % (name, sl, sp))
        else:
            print("      %-6s: NOT all positive on the trend "
                  "rungs -- typed in the verdict" % name)
    check("S4.1 [TREND REPORTED] depth-trend table + statistics "
          "printed for all characters and zeta (informative; the "
          "floor gate is S2)", True)

    # ---------------- S5 controls
    section("S5 -- CONTROLS at kz %d: sign scramble per character "
            "(seed %d)" % (KZ_CTRL, SEED_SIGN))
    ctrl_neg = True
    for name, q, a in CHARACTERS:
        fc = r9.chi_floor(name, q, a,
                          rng_sign=np.random.default_rng(SEED_SIGN),
                          with_contractor=True)
        neg = fc["lmin"] < 0.0
        ctrl_neg &= neg
        print("    %-6s sign-scramble: lam_min = %+.6e (truth "
              "%+.6e), ||C|| = %s"
              % (name, fc["lmin"], floors[name][KZ_CTRL]["lmin"],
                 ("%.4f" % fc["Cnorm"]) if "Cnorm" in fc
                 else "n/a"))
    print("    typed pre-run: EXPECTED negative, honestly NOT "
          "structural (routes to CUSHIONED, not to a kill).")
    check("S5.1 [DISCRIMINATION] all three sign-scramble controls "
          "indefinite: %s (informative; False routes to CUSHIONED)"
          % ctrl_neg, True)

    # ---------------- V verdict
    section("V -- FROZEN VERDICT + honest consequence")
    wards_ok = all(ok for (nm, ok) in CHECKS
                   if nm.startswith(("W1", "W2", "W3")))
    if not floor_ok:
        verdict = "FAMILY-INDEFINITE"
    elif not (wards_ok and loew_ok):
        verdict = "FAMILY-PARTIAL"
    elif ctrl_neg:
        verdict = "FAMILY-CONTRACTS-DISCRIMINATING"
    else:
        verdict = "FAMILY-CONTRACTS-CUSHIONED"
    trend_note = ", ".join(
        "%s %s" % (nm, "all-positive" if all_pos[nm] else
                   "SIGN CHANGE on trend rungs")
        for nm in ["zeta", "chi_3", "chi_4", "chi_5"])
    print("\n  VERDICT: %s   [wards %s | floor %s | loewner %s | "
          "controls-negative %s | trend: %s]"
          % (verdict, wards_ok, floor_ok, loew_ok, ctrl_neg,
             trend_note))
    if verdict == "FAMILY-CONTRACTS-DISCRIMINATING":
        print("""
  HONEST CONSEQUENCE: the mechanism is FAMILY-WIDE on this frame.
  Both odd characters (kernel-shifted archimedean data) AND the
  even character chi_5 -- whose window differs from zeta's by ONLY
  the conductor constant log(5) and the signed comb, with the
  archimedean kernel bit-identical -- carry the floor and the
  Loewner contraction on construction and blind holdouts, and every
  sign-scrambled control goes indefinite.  The positivity is
  carried by the CHARACTER COHERENCE of the comb, not by any
  kernel tuning: exactly the L-function universality the essay's
  point 7 asked for, at finite window depth.  The depth-trend
  statistics above show whether the chi-margins track the zeta
  wall.  Finite windows only: NO GRH claim, NO RH claim.""")
    elif verdict == "FAMILY-CONTRACTS-CUSHIONED":
        print("""
  HONEST CONSEQUENCE (typed): all family floors hold but at least
  one scrambled control stays PSD -- at this depth that character's
  positivity is not arithmetic-sensitive; depth extension is the
  named next step.  NO GRH claim.""")
    elif verdict == "FAMILY-INDEFINITE":
        print("""
  HONEST CONSEQUENCE (typed): a family floor goes indefinite on the
  marked rungs.  A statement about THIS finite window form
  (tail/alias mechanics), NOT about GRH.  The typed follow-up: the
  failing character's alias-layer decomposition.  NO GRH claim.""")
    else:
        print("""
  HONEST CONSEQUENCE (typed): a ward or the Loewner consistency
  broke -- the construction, not the mathematics, is the suspect;
  see the FAIL lines.  NO GRH claim.""")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
