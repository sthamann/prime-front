#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wall_margin_mechanism_probe -- E8.WALL.MARGINMECH.01: what exactly
holds the deployed wall up, and what "finding the solution" would have
to prove.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no .md,
nothing outside experiments/.  NO RH CLAIM in either direction.
Read-only import of the deployed v563 tables (the v881/v882 pattern).
Frozen (spec + sha256) before the frozen run; the smoke measurements
that shaped these claims are declared below, including one REFUTED
hypothesis, because recording dead guesses is part of the method.

THE QUESTION (user-posed, frozen): "dann finde endlich eine Loesung."
An RH proof cannot be produced here and will not be claimed; what CAN
be done is to pin down mechanically WHAT the missing proof must
control.  rh_leverage (E8.RH.LEVERAGE.01) measured that the wall
margin lam_min(K) is positive on all 67 faithful rungs and falls like
h^(-1.93) -- but not WHY.  This probe measures the mechanism.

SMOKE-RUN DISCLOSURE (2026-08-09, before freezing): a first guess --
that the margin is the grid-discretization error of the FIRST RIEMANN
ZERO, i.e. that the soft mode oscillates at omega = gamma_1 = 14.13 in
u -- was tested and is WRONG (measured omega ~ 0.6..1.7).  It is kept
in S2 as a frozen refutation.  The smoke run instead revealed the
cancellation structure and the per-prime sensitivities frozen in
S1/S3/S4; the frozen run below re-derives every number ladder-wide.

FROZEN CLAIMS (2026-08-09, frozen + SHA-hashed before the frozen run):

 S1  THE CANCELLATION LAW (the mechanism).  On the lam_min eigenvector
     v of every faithful rung, split the energy by the deployed lag
     decomposition c = c_arch + c_atoms:
         E_ar = v^T K_arch v,   E_at = v^T K_atoms v,
         lam_min = E_ar + E_at   (identity, ward 1e-10 relative).
     (a) SIGNS: E_ar < 0 < E_at on EVERY faithful rung -- along the
         critical direction the archimedean/geometric side pushes the
         form NEGATIVE and the PRIME side holds it up.  (Note the
         deployed sign convention c = c_arch - c_comb with positive
         comb hats, ledger PRIME.LONGLAG.SUPP.01: "the primes hold
         the wall" means the comb term acts positively through the
         odd-Toeplitz fold.)
     (b) MAGNITUDES: both sides are O(1) and grow ~ linearly with the
         window depth alpha (slope reported; smoke: E_at ~ 0.42
         alpha), while their sum is the margin -- a relative
         cancellation lam_min/E_at that falls from ~3e-4 (shallow) to
         ~3e-6 (deep).  Ward: relative cancellation < 1e-2 on every
         rung, decreasing trend (log-log slope vs h < 0).
     Fail => MECHANISM-BROKEN.

 S2  THE REFUTED ZERO-SEAT GUESS (frozen refutation + measurement).
     The soft mode's dominant u-frequency omega (FFT of v, zero
     padded, omega = theta/D) satisfies min_k |omega - gamma_k| > 1
     for the first ten zeta ordinates (literature constants, never
     fed to any wall object): the margin does NOT sit at a zero
     frequency; it is a LOW-frequency object with omega*alpha in
     [3, 7] (recorded).  The h^(-2) law is therefore NOT "the grid
     misses the first zero".  Fail => SEAT-BROKEN.

 S3  NON-TRANSFERABILITY (valley sharpness).  Interpolate the soft
     mode of rung kz' to rung kz in the scaled variable x = u/alpha
     and evaluate the Rayleigh quotient.
     (a) self-roundtrip (kz' = kz through the x-grid) costs < 1.5x
         the margin;
     (b) cross-rung transfer costs orders of magnitude: median
         RQ/lam_min over distinct pairs of the subset > 100 (smoke:
         1e2..1e4 even at shape overlap 0.85-0.99).
     READING: each depth requires its own exquisitely retuned
     cancellation direction; there is no universal soft profile whose
     positivity one could prove once and for all.
     Fail => TRANSFER-BROKEN.

 S4  WHO HOLDS THE WALL (the per-prime audit).
     (a) EXACT single-atom deletions, full scan on rung kz = 13 (136
         atoms): report how many single deletions leave lam_min > 0.
         Ward (from smoke): deleting any of the five largest-
         sensitivity atoms breaks the wall by >= 100x the margin, on
         kz = 13 AND kz = 40.
     (b) SENSITIVITY PROFILE (first-order dLam_j = -v^T K_{atom j} v,
         validated against exact deletions in sign): the profile is
         HEAD-CARRIED -- the top decile of atoms by |dLam| carries
         the majority of the total, and the EDGE zone u > 2 alpha - 1
         (the 39%-mass port zone of v882) carries < 20% of the
         sensitivity on both audit rungs (smoke: 4..8%).  The margin
         mechanism is a SMALL-PRIME phenomenon, complementary to the
         port-mass edge law.
     (c) THE ANCHOR PUSHES BACK (recorded + one frozen ward): the
         atom n = 2 has POSITIVE removal derivative on both audit
         rungs -- removing the anchor prime would RAISE the margin;
         the sign table of the full 2-power family {2,4,8,...} vs the
         odd prime powers is recorded without a freeze.
     (d) NONLINEARITY (recorded): exact deletion effects exceed the
         first-order values (the valley narrows away from the
         bottom); both are reported for the validation atoms.
     Fail => AUDIT-BROKEN.

 S5  THE SOLUTION STATEMENT (typed; the honest answer to "find the
     solution").  With S1-S4 the open wall statement has this exact
     shape in TFPT coordinates: PROVE that the O(alpha)-sized
     archimedean deficit is covered by the prime comb along the
     retuned critical direction AT EVERY DEPTH, knowing that
     (i) the residual falls like h^(-1.93) (rh_leverage S4),
     (ii) every small prime is individually load-bearing (S4a: one
          deletion = collapse by >= 100x margin),
     (iii) the critical direction is not transferable across depths
          (S3), and
     (iv) the statement for ALL depths is equivalent to Weil
          positivity, hence to RH (prime front I5, cited typing).
     (ii)+(iii) are exactly why finite methods stall: the wall is a
     GLOBAL conspiracy of all primes jointly, with no finite
     certificate family in sight -- the analytic face, in these
     coordinates, of "the primes are exactly as random as they are
     allowed to be".  Always-true typed check; no kill.

 C   CONTROLS (must fire):
     C1 identity: v^T K v = lam_min to 1e-10 relative on every rung.
     C2 RANDOM-PROFILE transfer: a seeded random smooth profile
        (5-term low-frequency Fourier series in x) costs > 1e3 x
        lam_min on every subset rung -- S3's transfer costs are not
        an artifact of the transfer machinery.
     C3 FIREWALL: AST scan of this file for the deployed banned
        identifiers (zetazero, nzeros, primerange, isprime, primepi,
        nextprime, prevprime); none may appear as a call.  The zeta
        ordinates in S2 are literature constants used only to REFUTE
        a hypothesis about a measured frequency.
     C4 NO-RH-CLAIM: the verdict asserts nothing about RH's truth.

VERDICT (frozen precedence): MECHANISM-BROKEN / SEAT-BROKEN /
TRANSFER-BROKEN / AUDIT-BROKEN / CONTROL-DEAD on kill; else
MARGINMECH-MEASURED with the measured cancellation depth, transfer
cost, head share and survivor count.

Sources (read-only): v563_paper2_readouts (deployed tables and
assembly), rh_leverage_probe (margin law h^-1.93, 67 faithful rungs),
v884 (certified head floors), v883 (FLUCTUATIONS-REQUIRED), v882
(edge mass 1 - e^{-1/2}), v881 (port frame), tfpt_prime_front.tex
(I5 equivalence typing), ledger PRIME.LONGLAG.SUPP.01 (lag split).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wall_margin_mechanism_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

T0 = time.time()
CHECKS = []
KILLS = []
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

KZMAX = int(os.environ.get("MARGINMECH_KZMAX", 150))
SUBSET = (9, 13, 26, 40, 60, 90, 121)
AUDIT_RUNGS = (13, 40)
SEED = 20260809
# first ten zeta ordinates -- literature constants, used ONLY in the
# S2 refutation of a hypothesis about a measured frequency; they are
# never fed to any comb, window or Toeplitz object
GAMMAS = (14.134725141734693, 21.022039638771555, 25.010857580145688,
          30.424876125859513, 32.935061587739190, 37.586178158825671,
          40.918719012147495, 43.327073280914999, 48.005150881167159,
          49.773832477672302)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def build_parts(kz):
    rr = core.build_window(kz)
    alpha, M, D = rr["alpha"], rr["M"], rr["D"]
    uu = np.asarray(rr["uu"], float)
    mu = 2.0 * np.asarray(rr["lam"], float)
    c_at = core.atom_lags_at(alpha, M, uu, mu)[0]
    c_ar = np.asarray(core.arch_lags(M, D), float)
    return rr, uu, mu, core.odd_toeplitz(c_ar, M), \
        core.odd_toeplitz(c_at, M)


# ======================================================================
section("S0: setup -- rebuild the faithful ladder")
# ======================================================================
print("spec sha256 = %s" % SPEC_SHA)

RUNGS = {}
for kz in range(2, KZMAX + 1):
    try:
        rr = core.build_window(kz)
    except Exception:
        continue
    if not (core.H_MIN <= rr["h"] <= core.HCAP):
        continue
    if rr["X"] > core.ATOM_MAX:
        continue
    rr, uu, mu, K_ar, K_at = build_parts(kz)
    w, V = np.linalg.eigh(K_ar + K_at)
    v = V[:, 0]
    RUNGS[kz] = {"rr": rr, "uu": uu, "mu": mu, "K_ar": K_ar,
                 "K_at": K_at, "lmin": float(w[0]), "v": v}
print("  %d faithful rungs rebuilt (h = %d..%d)"
      % (len(RUNGS), min(r["rr"]["h"] for r in RUNGS.values()),
         max(r["rr"]["h"] for r in RUNGS.values())))

# ======================================================================
section("S1: the cancellation law")
# ======================================================================
rows = []
for kz, R in RUNGS.items():
    v = R["v"]
    e_ar = float(v @ R["K_ar"] @ v)
    e_at = float(v @ R["K_at"] @ v)
    R["e_ar"], R["e_at"] = e_ar, e_at
    rows.append((kz, R["rr"]["alpha"], R["rr"]["h"], R["lmin"],
                 e_ar, e_at, R["lmin"] / e_at))

print("      kz  alpha     h     lam_min      E_arch      E_atoms"
      "    rel.cancel")
for r in rows[:4] + rows[-4:]:
    print("    %4d %6.3f %5d %+.4e %+.5e %+.5e   %.3e"
          % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))

id_ok = all(abs(r[4] + r[5] - r[3]) <= 1e-10 * max(abs(r[5]), 1.0)
            for r in rows)
sign_ok = all(r[4] < 0.0 < r[5] for r in rows)
check("S1.a SIGNS on all %d rungs: E_arch < 0 < E_atoms -- along the "
      "critical direction the GEOMETRY pushes the form negative and "
      "the PRIMES hold it up (energy identity E_ar + E_at = lam_min "
      "verified to 1e-10 everywhere: %s)"
      % (len(rows), id_ok), sign_ok and id_ok, kill="MECHANISM-BROKEN")

al = np.array([r[1] for r in rows])
ea = np.array([r[5] for r in rows])
slope, icpt = np.polyfit(al, ea, 1)
r2_lin = 1.0 - float(np.var(ea - (slope * al + icpt)) / np.var(ea))
rel = np.array([r[6] for r in rows])
hh = np.array([float(r[2]) for r in rows])
trend = float(np.polyfit(np.log(hh), np.log(rel), 1)[0])
check("S1.b MAGNITUDES: both sides are O(1) and grow linearly with "
      "depth -- E_atoms = %.4f*alpha %+.4f (R2 = %.3f) -- while the "
      "margin is their cancellation: lam_min/E_atoms spans %.2e "
      "(shallow) to %.2e (deep), ward < 1e-2 everywhere, log-log "
      "trend vs h = %+.3f (ward < 0).  THE WALL MARGIN IS A "
      "SIX-DIGIT CANCELLATION BETWEEN GEOMETRY AND ARITHMETIC"
      % (slope, icpt, r2_lin, float(rel.max()), float(rel.min()),
         trend),
      bool(np.all(rel < 1e-2)) and trend < 0.0,
      kill="MECHANISM-BROKEN")

# ======================================================================
section("S2: the refuted zero-seat guess")
# ======================================================================
freq_rows = []
for kz in SUBSET:
    R = RUNGS[kz]
    v, D, alpha = R["v"], R["rr"]["D"], R["rr"]["alpha"]
    M = R["rr"]["M"]
    sp = np.abs(np.fft.rfft(v, n=16 * M))
    kdom = int(np.argmax(sp))
    om = (kdom * 2.0 * math.pi / (16 * M)) / D
    dmin = min(abs(om - g) for g in GAMMAS)
    freq_rows.append((kz, om, om * alpha, dmin))
    print("    kz = %3d: dominant omega = %7.4f, omega*alpha = %6.3f, "
          "min distance to the first ten zeta ordinates = %7.3f"
          % (kz, om, om * alpha, dmin))
check("S2 THE FIRST GUESS IS DEAD (frozen refutation): the soft mode "
      "is a LOW-frequency object (omega = %.2f..%.2f, omega*alpha = "
      "%.1f..%.1f), min distance to the first ten zeta ordinates "
      "%.2f (ward > 1 on every subset rung) -- the h^(-2) margin law "
      "is NOT 'the grid misses the first zero'; the naive zero-seat "
      "reading of the wall margin is refuted"
      % (min(r[1] for r in freq_rows), max(r[1] for r in freq_rows),
         min(r[2] for r in freq_rows), max(r[2] for r in freq_rows),
         min(r[3] for r in freq_rows)),
      all(r[3] > 1.0 for r in freq_rows), kill="SEAT-BROKEN")

# ======================================================================
section("S3: non-transferability of the critical direction")
# ======================================================================
XG = np.linspace(0.001, 0.999, 4000)
PROF = {}
for kz in SUBSET:
    R = RUNGS[kz]
    h, D, alpha = R["rr"]["h"], R["rr"]["D"], R["rr"]["alpha"]
    x = (np.arange(h) * D) / alpha
    p = np.interp(XG, x, R["v"])
    PROF[kz] = p


def rq_on(kz, profile):
    R = RUNGS[kz]
    h, D, alpha = R["rr"]["h"], R["rr"]["D"], R["rr"]["alpha"]
    x = (np.arange(h) * D) / alpha
    g = np.interp(x, XG, profile)
    g = g / math.sqrt(float(g @ g))
    return float(g @ (R["K_ar"] + R["K_at"]) @ g)


self_ratios, cross_ratios = [], []
print("    transfer cost RQ/lam_min (rows: donor kz, cols: target):")
print("           " + "".join("%9d" % k for k in SUBSET))
for kd in SUBSET:
    line = "    kz%4d " % kd
    for kt in SUBSET:
        ratio = rq_on(kt, PROF[kd]) / RUNGS[kt]["lmin"]
        line += "%9.1f" % ratio
        (self_ratios if kd == kt else cross_ratios).append(ratio)
    print(line)

check("S3.a self-roundtrip through the x = u/alpha grid costs at most "
      "%.2fx the margin (ward < 1.5)" % max(self_ratios),
      max(self_ratios) < 1.5, kill="TRANSFER-BROKEN")
med_cross = float(np.median(cross_ratios))
check("S3.b cross-rung transfer costs a median %.0fx the margin "
      "(ward > 100; range %.0f..%.0f): the cancellation direction "
      "must be retuned at every depth -- there is NO universal soft "
      "profile whose positivity could be proven once"
      % (med_cross, min(cross_ratios), max(cross_ratios)),
      med_cross > 100.0, kill="TRANSFER-BROKEN")

# ======================================================================
section("S4: who holds the wall -- the per-prime audit")
# ======================================================================
audit = {}
for kz in AUDIT_RUNGS:
    R = RUNGS[kz]
    rr, uu, mu, v = R["rr"], R["uu"], R["mu"], R["v"]
    alpha, M = rr["alpha"], rr["M"]
    sens = np.zeros(len(uu))
    for j in range(len(uu)):
        dc = core.atom_lags_at(alpha, M, uu[j:j + 1], mu[j:j + 1])[0]
        sens[j] = -float(v @ core.odd_toeplitz(dc, M) @ v)
    audit[kz] = sens

# (a) exact full deletion scan on kz = 13
kz = 13
R = RUNGS[kz]
rr, uu, mu = R["rr"], R["uu"], R["mu"]
alpha, M = rr["alpha"], rr["M"]
survivors, worst = [], []
for j in range(len(uu)):
    keep = np.ones(len(uu), bool)
    keep[j] = False
    c2 = core.atom_lags_at(alpha, M, uu[keep], mu[keep])[0]
    l2 = float(np.linalg.eigvalsh(
        R["K_ar"] + core.odd_toeplitz(c2, M))[0])
    if l2 > 0.0:
        survivors.append(int(round(math.exp(uu[j]))))
    worst.append((l2, int(round(math.exp(uu[j])))))
worst.sort()
print("    kz = 13 exact full scan (%d atoms): %d deletions leave the "
      "wall standing (%s); worst three collapses: %s"
      % (len(uu), len(survivors), survivors or "none",
         ["n=%d -> %+.3f" % (n, l) for l, n in worst[:3]]))

top5_ok = {}
for kz2 in AUDIT_RUNGS:
    R2 = RUNGS[kz2]
    uu2, mu2 = R2["uu"], R2["mu"]
    alpha2, M2 = R2["rr"]["alpha"], R2["rr"]["M"]
    order = np.argsort(-np.abs(audit[kz2]))
    oks, det = [], []
    for j in order[:5]:
        keep = np.ones(len(uu2), bool)
        keep[j] = False
        c2 = core.atom_lags_at(alpha2, M2, uu2[keep], mu2[keep])[0]
        l2 = float(np.linalg.eigvalsh(
            R2["K_ar"] + core.odd_toeplitz(c2, M2))[0])
        oks.append(l2 < -100.0 * R2["lmin"])
        det.append("n=%d: %+.3f" % (int(round(math.exp(uu2[j]))), l2))
    top5_ok[kz2] = all(oks)
    print("    kz = %d top-5 sensitivity atoms, exact deletion: %s"
          % (kz2, "; ".join(det)))
check("S4.a ONE PRIME OUT, WALL DOWN: deleting any of the five most "
      "sensitive atoms collapses the wall by >= 100x the margin on "
      "both audit rungs; on kz = 13 the exact full scan finds %d of "
      "%d single deletions that the wall survives"
      % (len(survivors), len(uu)),
      all(top5_ok.values()), kill="AUDIT-BROKEN")

edge_shares, head_shares = {}, {}
for kz2 in AUDIT_RUNGS:
    R2 = RUNGS[kz2]
    uu2 = R2["uu"]
    a2 = R2["rr"]["alpha"]
    s = np.abs(audit[kz2])
    edge_shares[kz2] = float(s[uu2 > 2 * a2 - 1.0].sum() / s.sum())
    order = np.argsort(-s)
    ndec = max(1, len(s) // 10)
    head_shares[kz2] = float(s[order[:ndec]].sum() / s.sum())
check("S4.b HEAD-CARRIED: the top decile of atoms carries %.0f%% / "
      "%.0f%% of the total sensitivity on kz = 13/40, while the EDGE "
      "zone u > 2 alpha - 1 (the 39%%-mass port zone of v882) carries "
      "only %.1f%% / %.1f%% (ward < 20%%): the margin mechanism is a "
      "SMALL-PRIME phenomenon -- the same head that carries the "
      "Mertens constraint carries the wall"
      % (100 * head_shares[13], 100 * head_shares[40],
         100 * edge_shares[13], 100 * edge_shares[40]),
      all(v < 0.2 for v in edge_shares.values()), kill="AUDIT-BROKEN")

anchor_rows = {}
for kz2 in AUDIT_RUNGS:
    R2 = RUNGS[kz2]
    nv = np.rint(np.exp(R2["uu"])).astype(int)
    fam = {}
    for j, n in enumerate(nv):
        if (n & (n - 1)) == 0:              # powers of two
            fam[n] = audit[kz2][j]
    anchor_rows[kz2] = fam
    print("    kz = %d two-power family removal derivatives: %s"
          % (kz2, ", ".join("n=%d: %+.3e" % (n, fam[n])
                            for n in sorted(fam))))
check("S4.c THE ANCHOR PUSHES BACK: the removal derivative of the "
      "atom n = 2 is POSITIVE on both audit rungs (%+.3e / %+.3e) -- "
      "taking the ramified prime out would RAISE the margin; the "
      "full 2-power sign table is recorded above without a freeze"
      % (anchor_rows[13][2], anchor_rows[40][2]),
      anchor_rows[13][2] > 0.0 and anchor_rows[40][2] > 0.0,
      kill="AUDIT-BROKEN")

j_top = int(np.argmax(np.abs(audit[13])))
keep = np.ones(len(RUNGS[13]["uu"]), bool)
keep[j_top] = False
c2 = core.atom_lags_at(RUNGS[13]["rr"]["alpha"], RUNGS[13]["rr"]["M"],
                       RUNGS[13]["uu"][keep], RUNGS[13]["mu"][keep])[0]
l_ex = float(np.linalg.eigvalsh(
    RUNGS[13]["K_ar"] + core.odd_toeplitz(c2, RUNGS[13]["rr"]["M"]))[0]
) - RUNGS[13]["lmin"]
check("S4.d NONLINEARITY recorded: on the top kz = 13 atom the exact "
      "deletion effect %+.3f exceeds the first-order derivative "
      "%+.3f in magnitude and agrees in sign -- the valley narrows "
      "away from its bottom" % (l_ex, audit[13][j_top]),
      l_ex < 0.0 and audit[13][j_top] < 0.0
      and abs(l_ex) >= abs(audit[13][j_top]), kill="AUDIT-BROKEN")

# ======================================================================
section("S5: the solution statement (typed)")
# ======================================================================
check("S5 WHAT 'FINDING THE SOLUTION' NOW MEANS, exactly: prove that "
      "the O(alpha) archimedean deficit is covered by the prime comb "
      "along the retuned critical direction AT EVERY DEPTH -- knowing "
      "that the residual falls like h^(-1.93) (rh_leverage S4), that "
      "every small prime is individually load-bearing (S4.a), that "
      "the critical direction is not transferable across depths "
      "(S3.b), and that the all-depth statement is equivalent to Weil "
      "positivity, hence to RH (I5 typing, cited).  The wall is a "
      "GLOBAL conspiracy of all primes jointly; no finite certificate "
      "family is in sight, and that is the analytic face -- in TFPT "
      "coordinates -- of 'the primes are exactly as random as they "
      "are allowed to be'.  NO RH claim in either direction",
      True, kill=None)

# ======================================================================
section("C: controls")
# ======================================================================
cons = max(abs(R["e_ar"] + R["e_at"] - R["lmin"])
           / max(abs(R["e_at"]), 1.0) for R in RUNGS.values())
check("C1 energy identity v^T K v = lam_min holds to %.1e relative "
      "on all %d rungs (ward 1e-10)" % (cons, len(RUNGS)),
      cons <= 1e-10, kill="CONTROL-DEAD")

rng = np.random.default_rng(SEED)
coef = rng.standard_normal(5)
rand_prof = sum(c * np.sin((k + 1) * math.pi * XG)
                for k, c in enumerate(coef))
rand_ratios = [rq_on(kz, rand_prof) / RUNGS[kz]["lmin"]
               for kz in SUBSET]
check("C2 RANDOM-PROFILE control fires: a seeded smooth random "
      "profile costs %.0f..%.0fx the margin (ward > 1e3 on every "
      "subset rung) -- the S3 transfer costs are not an artifact of "
      "the transfer machinery"
      % (min(rand_ratios), max(rand_ratios)),
      all(r > 1e3 for r in rand_ratios), kill="CONTROL-DEAD")

_tree = ast.parse(open(__file__, encoding="utf-8").read())
_called = {n.func.id for n in ast.walk(_tree)
           if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
_called |= {n.func.attr for n in ast.walk(_tree)
            if isinstance(n, ast.Call)
            and isinstance(n.func, ast.Attribute)}
hits = sorted(_called & set(BANNED_IDS))
check("C3 FIREWALL: none of the deployed banned identifiers %s is "
      "called (hits: %s); the zeta ordinates are literature "
      "constants confined to the S2 refutation"
      % (list(BANNED_IDS), hits or "none"), not hits,
      kill="CONTROL-DEAD")

# ======================================================================
section("VERDICT")
# ======================================================================
n_pass = sum(1 for _, ok in CHECKS if ok)
if KILLS:
    verdict = KILLS[0]
else:
    verdict = ("MARGINMECH-MEASURED (ARCH-NEG-PRIME-POS + "
               "CANCEL-%.0e + NONTRANSFER-x%.0f + HEAD-CARRIED-%.0f%% "
               "+ SURVIVORS-%d + NO-ZERO-SEAT)"
               % (float(rel.min()), med_cross,
                  100 * head_shares[40], len(survivors)))
check("C4 NO-RH-CLAIM: the verdict reports a mechanism, not a truth "
      "value for RH", "RH-TRUE" not in verdict
      and "RH-FALSE" not in verdict, kill="CONTROL-DEAD")

print("\nCHECKS: %d/%d passed"
      % (sum(1 for _, ok in CHECKS if ok), len(CHECKS)))
if any(not ok for _, ok in CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("""
WHAT THIS MEASURES (exploration only):
 * THE MECHANISM: the deployed wall margin is a six-digit
   cancellation.  Along the critical direction the archimedean side
   is NEGATIVE and the prime comb holds the form up; both sides grow
   linearly with depth while their sum shrinks like h^(-2).
 * WHO CARRIES IT: the smallest primes.  Removing a single one
   collapses the wall by orders of magnitude; the edge zone that
   carries the port MASS carries almost none of the margin
   SENSITIVITY; the anchor prime 2 pushes against the wall.
 * WHAT IS REFUTED: the margin does not sit at any zeta-zero
   frequency; the naive 'grid misses the first zero' story is dead.
 * WHAT A SOLUTION MUST DO: certify an ever-sharpening cancellation
   whose critical direction cannot be fixed once and whose carriers
   cannot be truncated to any finite set.  That is RH in these
   coordinates, and it is exactly why it cannot be settled by finite
   bookkeeping -- only reformulated sharply enough that the missing
   idea has a definite shape.
NO ledger/paper/website claim; NO RH claim in either direction; NO
physics claim beyond the recorded identities and measurements.
""")
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if all(ok for _, ok in CHECKS) else 1)
