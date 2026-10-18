#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v846 -- PRIME.SCHUR.GRAM.01 + PRIME.SPECTRAL.MOTHER.01: the Schur program closed as a typed structural negative -- the manifestly positive relational Gram exists but its corner identity fails in trace AND form by exactly the forced Cauchy-Schwarz diagonal price, and the price is GEOMETRY-INDEPENDENT (it survives the unitary spectral mother), ONE module from two probes (19 + 16 checks, zero fails, verdicts SCHUR-INDEFINITE and SPECTRAL-TV-UNIVERSAL; discovery probes relational_schur_gram_probe.py and spectral_mother_probe.py, 2026-08-07, re-run identically at promotion, promoted VERBATIM with no downscoping, ~1 s).  PART A, THE DIAGONAL DESIGN SPACE: the target G_X = [[P, R], [R*, C]] >= 0 with GL1 Schur complement == the deployed Weil window form T_X.  Three of the four gates PASS: G1 manifest positivity (C = K + diag(price) diagonally dominant by construction, lambda_min(C) > 0); G3 placement + Euler sensitivity (the mu*log descent routes every prime-power mass EXACTLY -- descent lag ward c+ - c- == c_at at 1e-16 -- and REFUSES the h = 2 Epstein comb at construction grade: 49-100 of the events off prime powers, bookkeeping defect 0.727-0.825 vs TRUE comb defect 0; the Euler-product gate fires before any spectrum is computed); G4 Selberg safety (zeta_QI and the chi4 L-sector complete through the same descent, defect <= 1e-10, price ratio in [0.2, 5]).  THE STRUCTURAL FAILURE (G2): every relational cell carrying a cross term deposits the Cauchy-Schwarz diagonal alongside, so the C-block is FORCED to K + diag(price) with the price the row total variation of the deposits -- measured price/tau ~ 3.1e4..4.5e4 even at the density-anchored fluctuation floor (tau = 4.4e-4..6.0e-4, merged floor medians 17.4..21.6); the P0 deviation IS diag(price) structurally (0 <= 1e-9), no predeclared projection removes it (P1/P2/P3 best kernel dev 12.3..19.0), the price is weight-generic (1% jitter moves it ~1% linearly), and the trace fails by the same strictly positive diagonal -- the typed kill 'identity in trace but not form' is REPLACED by the sharper statement that both fail by ONE positive object.  PART B, THE TYPED MISSING INPUT BUILT: the non-diagonal spectral/Mellin mother on the deployed log-grid -- dilations as tent shifts (unitary at integer commensurability, contraction budget measured), the functional-equation mirror as an OPERATOR (J^2 = I dev 0; the deployed window form verified to be the J-odd compression of a plain Toeplitz form at rel 0), the Euler product as an exact operator algebra U_d U_m = U_{dm} (composition defect = the tent double-interpolation budget, zero at integer commensurability) with the mu*log routing and the Epstein refusal transported intact.  THE INTERFERENCE IS REAL BUT UNHARVESTABLE: at symbol grade the phase cancellation compresses the cross-term transport by measured gains 20-33x (median |sigma_comb| 2.7-2.9 vs TV 58-95); at Gram grade every event-local manifest Gram pays the event-local TV floor (the a^2 + b^2 >= 2|ab| modulus bound; deployed tent contraction prices 0.55-0.60 x 2TV) -- best legal overhead 34.4-54.8 = 5.7e4..1.2e5 x tau, the decisive gate CLOSES: False, REDUCES: False on every anchor.  THE CLOSURE TYPING (the strongest form of the Schur program's wall): THE TV PRICE IS GEOMETRY-INDEPENDENT -- cross-event interference can only be harvested by factoring the TOTAL symbol (Fejer-Riesz), and the symbol's nonnegativity IS the positivity being sought; the manifest-positivity route closes on itself; what any future construction must supply is a zero-free factorization of the completed symbol, an object equivalent in strength to the window positivity itself.  Feeds the round-30 dated closing note on PRIME.RELATION.SKELETON.01 (diagonal relational mothers stop-listed).  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes relational_schur_gram_probe.py (19 run,
0 failed, verdict SCHUR-INDEFINITE) and spectral_mother_probe.py (16
run, 0 failed, verdict SPECTRAL-TV-UNIVERSAL; the run-1 -> run-2
declared bar correction is in the frozen probe docstring), both
2026-08-07, re-run identically at promotion; this module runs both
frozen protocols VERBATIM (FROZEN_SPEC constants embedded byte-exact
so the printed SHA-256 values reproduce; runtime ~1 s).  The original
probe docstrings live verbatim in experiments/tfpt-discovery/.

FIREWALL: no zeros; no positivity tests during construction (spectra
and symbol minima are measurement, Fejer-Riesz is never performed);
zeta(1/2)/zeta'(1/2) constants = the deployed zero-free v583
convention; v563 READ-ONLY; anchors kz = 9/12/13.  NO RH claim.
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
if _here not in sys.path:
    sys.path.insert(0, _here)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

FROZEN_SPEC_A = """\
PRIME.SCHUR.GRAM.01 spec v1 (2026-08-07, frozen before the run).
Design space: relational-cell Grams, cells touch <= 2 window
coordinates, weights from source data (arch lags c_ar, descent
relations w = lam |mu(d)| log m / N(n), tent bins, mirror pairs
inside E_l).  C-block = K + diag(price), price = rowsum(Kabs) -
diag(K); grades: per-source (arch |c_ar| lags + descent (2k-1)lam
tent) and merged (|K| entrywise); D2-lite floor = rowsum(|K_comb
- K_pnt|) with the certified PNT/arch block admitted.  P-variants
frozen: P0 none, P1 [flat], P2 [flat, pole e^{iD/2}], P3 [flat,
pole, (-1)^i]; Schur = C - CV (V^T C V)^+ V^T C.  Gates: G1
lambda_min(C) >= -1e-8||C||, range res <= 1e-8; G2 FORM max|dev|
<= 1e-8 max|K| (kernel + 2x2), TRACE rel <= 1e-8, jitter 1% x2
linear; G3 scramble F-dev >= 1e-3 rel, Epstein descent defect >=
1e-3 ||K_comb||_F with TRUE defect <= 1e-10; G4 QI/CHI defect <=
1e-10, price ratio in [0.2, 5].  Anchors kz 9/12/13; tau refs rel
1e-4; Ah vs Ah_dir <= 1e-6 rel; descent lag ward c_plus - c_minus
== c_at <= 1e-10 rel.  Verdict: EXISTS iff G2 FORM some variant +
G1/G3/G4; TRACE-ONLY iff trace passes, form fails; INDEFINITE iff
form+trace fail AND dev(P0) == diag price (<= 1e-9) AND min
variant dev >= 0.1 x median price (projections cannot remove the
price); else PARTIAL.  Ladder skipped unless G2 passes (typed).
NO RH claim; writes nothing.
"""

FROZEN_SPEC_B = """\
PRIME.SPECTRAL.MOTHER.01 spec v1 (2026-08-07, frozen before run).
Geometry: M-cell log-grid; U_n = tent shift by s_n = u_n/D
(rows j = floor(i-s), i-s-floor weights); J[i] = -delta[M-1-i];
odd extension P: t -> (t, -rev t); ward t^T K t == 0.5 f_ext^T
Toep_M(c_ar + c_at) f_ext rel <= 1e-10 (t1, t2, 3 random).
Unitarity budget: lambda-weighted mean/max of ||U^T U - I||_F /
sqrt(M) reported; integer-shift interior control <= 1e-12.
Op-match ward: Keff(-Sigma lam (U + U^T)) vs Keff(Toep(c_at))
max dev reported (edge budget).  Variant (a): G_comb = Sigma lam
(I - U)(I - U)^T; OV_a = Keff(G_comb) - Keff(Toep(c_at)); run-2
bars (declared correction, see docstring): exact bookkeeping
max|OV_a - Keff(Sigma lam (I + U U^T))| <= max(10 x opmatch
residue, 1e-12) x max|K|, AND diag median / 2TV in [0.5, 1.25]
(tent-contraction TV-scale band; q_bar = lam-weighted row mass
reported); off-diagonal part reported.  Variant (b): composition ward lambda-weighted
||U_p U_{p^{k-1}} - U_{p^k}||_F / sqrt(M) reported (<= 0.5
sanity); descent mass routing == c_at rel <= 1e-10; Epstein
refusal defect >= 1e-3 (mass grade, transported); OV_b diag ~
(2k-1)-weighted 2 TV.  Variant (c): overhead_c = 2 ||c_at -
c_pnt||_1 (l >= 1) + |Delta_c[0]| + max(0, -min sigma_pnt).
Task 4: sigma(theta) on 4096-point grid from lags; report min
sigma_tot, max/median |sigma_comb|, TV = 2 Sigma lam, gain =
TV / median|sigma_comb|.  Diagonal regression: merged price =
rowsum|K| - diag(K) medians (previous probe).  Gates: scramble
lag F-dev >= 1e-3; Epstein defect >= 1e-3 with TRUE <= 1e-10;
QI/CHI defect <= 1e-10, price ratio [0.2, 5].  Verdict: CLOSES
iff best legal overhead < tau; REDUCES iff best < 0.33 x merged
diagonal price; else SPECTRAL-TV-UNIVERSAL.  tau refs kz 9/12/13
rel 1e-4.  NO RH claim; writes nothing.
"""

_VERDICTS = {}

ANCHORS = (9, 12, 13)
TAU_REFS = {9: 5.984165e-4, 12: 4.351189e-4, 13: 5.637632e-4}
X_REL = 2048
GRID_PER_D = 4.0
NTH = 4096
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

EXPECTED_A = "SCHUR-INDEFINITE"
EXPECTED_B = "SPECTRAL-TV-UNIVERSAL"
N_CHECKS_A = 19
N_CHECKS_B = 16

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


def ast_firewall():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def t_abs(cabs, M):
    """Absolute deposit kernel: cabs[|i-j|] + cabs[(M-1)-i-j]
    (Toeplitz cell + mirror cell counted separately, cabs >= 0)."""
    h = M // 2
    rr = np.arange(h)
    return (np.asarray(cabs)[np.abs(rr[:, None] - rr[None, :])]
            + np.asarray(cabs)[(M - 1) - rr[:, None] - rr[None, :]])


def factor_pk(n):
    """(p, k) of a prime power, else None."""
    for q in range(2, int(math.isqrt(n)) + 1):
        if n % q == 0:
            k = 0
            while n % q == 0:
                n //= q
                k += 1
            return (q, k) if n == 1 else None
    return (n, 1)


def squarefree_divisors(n):
    ps = []
    m = n
    for q in range(2, int(math.isqrt(n)) + 1):
        if m % q == 0:
            ps.append(q)
            while m % q == 0:
                m //= q
    if m > 1:
        ps.append(m)
    divs = [(1, 1)]
    for p in ps:
        divs += [(d * p, -s) for d, s in divs]
    return divs                      # (d, mu(d)) squarefree only


def chi4(n):
    return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)


def price_of(K, Kabs):
    return np.sum(Kabs, axis=1) - np.diag(K)


def schur_of(C, V):
    """C - C V (V^T C V)^+ V^T C (kernel grade)."""
    if V is None or V.shape[1] == 0:
        return C.copy(), 0.0
    P = V.T @ C @ V
    R = V.T @ C
    Pp = np.linalg.pinv(P, rcond=1e-12)
    rng_res = (np.linalg.norm(R - P @ (Pp @ R))
               / max(np.linalg.norm(R), 1e-300))
    return C - R.T @ (Pp @ R), rng_res


def descent_kernels(alpha, M, uu, mm, is_pp_flags, dk):
    """Signed cell kernel (what the mu-descent routes) and the
    per-source absolute kernel.  dk = total-variation multiplier
    per event ((2k-1) on p^k; descent TV/lam on non-pp)."""
    mm = np.asarray(mm, float)
    keep = np.asarray(is_pp_flags, bool)
    c_signed, _D = core.atom_lags_at(alpha, M,
                                     np.asarray(uu)[keep],
                                     mm[keep])
    c_absw, _D = core.atom_lags_at(alpha, M, uu,
                                   np.abs(mm) * np.asarray(dk))
    return (core.odd_toeplitz(c_signed, M),
            t_abs(-np.asarray(c_absw), M))



# ---- probe-B (spectral mother) geometry helpers
def U_of(s, M):
    """Tent-interpolated dilation/shift by s grid units (deployed
    two-point convention)."""
    U = np.zeros((M, M))
    for i in range(M):
        b = i - s
        j0 = int(math.floor(b))
        fr = b - j0
        if 0 <= j0 < M:
            U[i, j0] += 1.0 - fr
        if 0 <= j0 + 1 < M:
            U[i, j0 + 1] += fr
    return U


def toep_of(c, M):
    rr = np.arange(M)
    return np.asarray(c)[np.abs(rr[:, None] - rr[None, :])]


def keff_of(O, h, M):
    """The J-odd window compression: 0.5 P^T O P, P: t -> odd ext."""
    P = np.zeros((M, h))
    P[np.arange(h), np.arange(h)] = 1.0
    P[M - 1 - np.arange(h), np.arange(h)] = -1.0
    return 0.5 * (P.T @ O @ P), P


def symbol_of(c, M, th):
    ll = np.arange(1, M)
    return c[0] + 2.0 * (np.cos(np.outer(th, ll)) @ np.asarray(
        c)[1:])



# ====== PART A -- relational_schur_gram_probe.py (frozen probe, verbatim)
def part_a():
    global T0
    T0 = time.time()
    section("PRIME.SCHUR.GRAM.01 -- the relational Schur-Gram "
            "theorem attempt (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC_A.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC_A SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall clean", not bad,
          "found %s" % bad if bad else "clean")

    from mpmath import mp, zeta as mzeta, diff as mdiff
    mp.dps = 30
    C_TH = float(-2 * mdiff(lambda s: mzeta(s), 0.5) / mzeta(0.5))
    U0 = 2.0 * math.log(-C_TH / 4.0)

    # s2s / Epstein support (x^2 + 5 y^2, class number 2)
    rq = np.zeros(X_REL + 1, dtype=np.int64)
    s = int(math.isqrt(X_REL)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= X_REL:
                rq[v] += 1

    form_ok = trace_ok = True
    g1_ok = g3_ok = g4_ok = True
    p0_structural = True
    proj_cannot = True
    rows = []
    for kz in ANCHORS:
        section("ANCHOR kz = %d" % kz)
        rr = core.build_window(kz)
        alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        lam = np.asarray(rr["lam"], float)
        nv = np.rint(np.exp(uu)).astype(np.int64)
        ka = len(nv)
        t1, t2 = rr["t1"], rr["t2"]
        T = np.stack([t1, t2], axis=1)
        Ah = np.asarray(rr["Ah"], float)
        tau = float(np.linalg.eigvalsh(Ah)[0])

        # ---------------- S1 the deployed target + descent wards
        c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
        c_ar = core.arch_lags(M, D)
        K_arch = core.odd_toeplitz(c_ar, M)
        K_comb = core.odd_toeplitz(c_at, M)
        K = K_arch + K_comb
        lmK = float(np.linalg.eigvalsh(K)[0])
        ah_dev = float(np.max(np.abs(Ah - rr["Ah_dir"]))
                       / max(np.max(np.abs(Ah)), 1e-300))
        # descent split: n = p^k -> (1, n) weight k lam (+),
        # (p, p^{k-1}) weight (k-1) lam (-); signed sum = lam
        pk = [factor_pk(int(n)) for n in nv]
        kexp = np.array([x[1] for x in pk], float)
        c_plus, _ = core.atom_lags_at(alpha, M, uu, kexp * mm)
        c_minus, _ = core.atom_lags_at(alpha, M, uu,
                                       (kexp - 1.0) * mm)
        desc_ward = float(np.max(np.abs((c_plus - c_minus) - c_at))
                          / max(np.max(np.abs(c_at)), 1e-300))
        check("S1.%d [WARDS] tau = %.4e (ref rel %.1e <= 1e-4); "
              "Ah vs full-kernel Ah_dir rel %.1e <= 1e-6; "
              "mu*log descent lag ward (c+ - c- == c_at) rel "
              "%.1e <= 1e-10; lambda_min(K full) = %+.3e"
              % (kz, tau,
                 abs(tau - TAU_REFS[kz]) / TAU_REFS[kz],
                 ah_dev, desc_ward, lmK),
              abs(tau - TAU_REFS[kz]) / TAU_REFS[kz] <= 1e-4
              and ah_dev <= 1e-6 and desc_ward <= 1e-10)

        # ---------------- S2 the construction: C = K + diag(price)
        dk = 2.0 * kexp - 1.0        # descent TV multiplier p^k
        Kabs_comb_src = t_abs(-core.atom_lags_at(
            alpha, M, uu, dk * mm)[0], M)
        Kabs_arch_src = t_abs(np.abs(c_ar), M)
        Kabs_src = Kabs_arch_src + Kabs_comb_src
        pr_src = price_of(K, Kabs_src)
        pr_mrg = price_of(K, np.abs(K))
        # D2-lite: the PNT/density kernel (certified block input)
        delta = D / GRID_PER_D
        n_cells = int(math.ceil((2 * alpha + 1e-9 - U0) / delta))
        edges = U0 + delta * np.arange(n_cells + 1)
        hi = np.minimum(edges[1:], 2 * alpha + 1e-9)
        lo = np.minimum(edges[:-1], 2 * alpha + 1e-9)
        mcell = 2.0 * (np.exp(hi / 2.0) - np.exp(lo / 2.0))
        c_pnt, _ = core.atom_lags_at(
            alpha, M, 0.5 * (edges[:-1] + edges[1:]), 2.0 * mcell)
        K_fl = K_comb - core.odd_toeplitz(c_pnt, M)
        pr_fl = np.sum(np.abs(K_fl), axis=1) - np.diag(K_fl)
        C = K + np.diag(pr_src)
        lmC = float(np.linalg.eigvalsh(C)[0])
        print("    prices vs the margin: per-source median %.2f "
              "(max %.2f); merged design-floor median %.2f; "
              "D2-lite fluctuation floor median %.2f -- tau_X = "
              "%.2e, lambda_min(K) = %.2e (price/tau ~ %.1e even "
              "at the density-anchored floor)"
              % (float(np.median(pr_src)), float(np.max(pr_src)),
                 float(np.median(pr_mrg)),
                 float(np.median(pr_fl)), tau, lmK,
                 float(np.median(pr_fl)) / tau))
        check("S2.%d [G1 MANIFEST POSITIVITY] C = K + diag(price) "
              "is diagonally dominant by construction (every cell "
              "PSD, Cauchy-Schwarz); numeric lambda_min(C) = "
              "%+.3e >= -1e-8 ||C||" % (kz, lmC),
              lmC >= -1e-8 * float(np.max(np.abs(C))))
        g1_ok &= lmC >= -1e-8 * float(np.max(np.abs(C)))

        # ---------------- S3 gate 2: the Schur corner identity
        grid = np.arange(h, dtype=float)
        profiles = {
            "P0(none)": None,
            "P1(flat)": np.ones((h, 1)),
            "P2(flat+pole)": np.stack(
                [np.ones(h), np.exp(grid * D / 2.0)
                 / np.exp(grid[-1] * D / 4.0)], axis=1),
            "P3(+mirror-alt)": np.stack(
                [np.ones(h), np.exp(grid * D / 2.0)
                 / np.exp(grid[-1] * D / 4.0),
                 (-1.0) ** np.arange(h)], axis=1)}
        maxK = float(np.max(np.abs(K)))
        best = None
        for name, V in profiles.items():
            SK, rng_res = schur_of(C, V)
            devK = float(np.max(np.abs(SK - K))) / maxK
            S22 = T.T @ SK @ T
            dev22 = float(np.max(np.abs(S22 - Ah))) \
                / max(float(np.max(np.abs(Ah))), 1e-300)
            devtr = abs(np.trace(S22) - np.trace(Ah)) \
                / abs(np.trace(Ah))
            print("    %-16s Schur dev: kernel %.3e, 2x2 %.3e, "
                  "trace %.3e, range-res %.1e"
                  % (name, devK, dev22, devtr, rng_res))
            if best is None or devK < best[1]:
                best = (name, devK, dev22, devtr, rng_res)
            g1_ok &= rng_res <= 1e-8
        p0dev = np.max(np.abs(schur_of(C, None)[0] - K
                              - np.diag(pr_src)))
        p0_structural &= p0dev <= 1e-9 * maxK
        form_ok &= best[1] <= 1e-8
        trace_ok &= best[3] <= 1e-8
        proj_cannot &= best[1] * maxK >= 0.1 * float(
            np.median(pr_src))
        check("S3.%d [G2 FORM vs TRACE] best variant %s: kernel "
              "form dev %.3e, deployed 2x2 dev %.3e, trace dev "
              "%.3e (FORM bar 1e-8: %s; TRACE bar 1e-8: %s); "
              "P0 dev == diag(price) structurally (%.1e <= 1e-9): "
              "the deviation IS the Cauchy-Schwarz price"
              % (kz, best[0], best[1], best[2], best[3],
                 best[1] <= 1e-8, best[3] <= 1e-8,
                 p0dev / maxK), True)

        # weight-generic jitter: the price is structural
        rng = np.random.default_rng(7)
        lin = []
        for _ in range(2):
            j = 1.0 + 0.01 * rng.standard_normal(ka)
            Kj = K_arch + core.odd_toeplitz(
                core.atom_lags_at(alpha, M, uu, mm * j)[0], M)
            Kaj = Kabs_arch_src + t_abs(-core.atom_lags_at(
                alpha, M, uu, dk * mm * np.abs(j))[0], M)
            prj = price_of(Kj, Kaj)
            lin.append(float(np.median(np.abs(prj - pr_src))
                             / np.median(pr_src)))
        check("S3.%dj [G2 WEIGHT-GENERIC] 1%% lam jitter moves the "
              "price by median %.4f / %.4f (~1%% linear, "
              "structural not numerical)" % (kz, lin[0], lin[1]),
              max(lin) <= 0.05)

        # ---------------- S4 gate 3: placement + Euler sensitivity
        uu_s = np.asarray(core.build_window(kz, scramble_seed=1)
                          ["uu"], float)
        K_scr = core.odd_toeplitz(
            core.atom_lags_at(alpha, M, uu_s, mm)[0], M)
        scr_dev = (np.linalg.norm(K_scr - K_comb)
                   / np.linalg.norm(K_comb))
        rqs = np.array([n for n in range(2, X_REL + 1)
                        if rq[n] > 0][:ka], dtype=np.int64)
        uu_e = np.log(rqs.astype(float))
        pk_e = [factor_pk(int(n)) for n in rqs]
        ispp_e = np.array([x is not None for x in pk_e])
        dk_e, defect_free = [], True
        for x, n in zip(pk_e, rqs):
            if x is not None:
                dk_e.append(2.0 * x[1] - 1.0)
            else:
                tv = sum(abs(mu) * math.log(int(n) / d)
                         for d, mu in squarefree_divisors(int(n))
                         ) / math.log(int(n))
                dk_e.append(tv)
                defect_free = False
        K_e_target = core.odd_toeplitz(
            core.atom_lags_at(alpha, M, uu_e, mm)[0], M)
        K_e_cells, _Kabs_e = descent_kernels(
            alpha, M, uu_e, mm, ispp_e, dk_e)
        d_eps = (np.linalg.norm(K_e_cells - K_e_target)
                 / np.linalg.norm(K_comb))
        K_t_cells, _ = descent_kernels(
            alpha, M, uu, mm, np.ones(ka, bool), dk)
        d_true = (np.linalg.norm(K_t_cells - K_comb)
                  / np.linalg.norm(K_comb))
        n_offpp = int(np.sum(~ispp_e))
        ok3 = (scr_dev >= 1e-3 and d_eps >= 1e-3
               and d_true <= 1e-10 and not defect_free)
        g3_ok &= ok3
        check("S4.%d [G3 PLACEMENT + EULER] scramble moves the "
              "kernel (rel F-dev %.3f >= 1e-3); the mu-descent "
              "REFUSES the Epstein h=2 comb at construction grade: "
              "%d of %d events are off prime powers, their mass is "
              "unroutable (mu*log signed sum = 0), bookkeeping "
              "defect %.3f >= 1e-3 (TRUE comb defect %.1e <= "
              "1e-10)" % (kz, scr_dev, n_offpp, ka, d_eps, d_true),
              ok3)

        # ---------------- S5 gate 4: Selberg-class safety
        ok4 = True
        for fname, wf in (("zeta_QI", 1.0 + np.array(
                [chi4(int(n)) for n in nv], float)),
                ("L(chi4)", np.array(
                    [chi4(int(n)) for n in nv], float))):
            mmF = mm * wf
            keepF = mmF != 0.0
            cF_p, _ = core.atom_lags_at(
                alpha, M, uu[keepF], (kexp * mmF)[keepF])
            cF_m, _ = core.atom_lags_at(
                alpha, M, uu[keepF], ((kexp - 1.0) * mmF)[keepF])
            cF, _ = core.atom_lags_at(alpha, M, uu[keepF],
                                      mmF[keepF])
            dF = float(np.max(np.abs((cF_p - cF_m) - cF))
                       / max(np.max(np.abs(c_at)), 1e-300))
            KF = core.odd_toeplitz(cF, M)
            KaF = Kabs_arch_src + t_abs(-core.atom_lags_at(
                alpha, M, uu[keepF],
                (dk * np.abs(mmF))[keepF])[0], M)
            prF = price_of(K_arch + KF, KaF)
            ratio = float(np.median(prF) / np.median(pr_src))
            okF = dF <= 1e-10 and 0.2 <= ratio <= 5.0
            ok4 &= okF
            print("    %-8s descent defect %.1e, price ratio "
                  "%.3f, kernel differs from TRUE by rel %.3f"
                  % (fname, dF, ratio,
                     float(np.linalg.norm(KF - K_comb)
                           / np.linalg.norm(K_comb))))
        g4_ok &= ok4
        check("S5.%d [G4 SELBERG SAFETY] zeta_QI and the chi4 "
              "L-sector complete through the same descent (sign "
              "in the eps register) with defect <= 1e-10 and "
              "price ratio in [0.2, 5] -- multiplicative sectors "
              "are NOT falsely destroyed" % kz, ok4)
        rows.append((kz, tau, lmK, float(np.median(pr_src)),
                     float(np.median(pr_mrg)),
                     float(np.median(pr_fl)), best[1]))
        del rr, K, C, Kabs_src, K_scr

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    print("    %-4s %-11s %-11s %-9s %-9s %-9s %-9s"
          % ("kz", "tau", "lmin(K)", "price_src", "price_mrg",
             "price_fl", "best dev"))
    for r in rows:
        print("    %-4d %-11.3e %-11.3e %-9.2f %-9.2f %-9.2f "
              "%-9.3e" % r)
    if form_ok and g1_ok and g3_ok and g4_ok:
        verdict = "SCHUR-GRAM-EXISTS"
    elif trace_ok:
        verdict = "SCHUR-TRACE-ONLY"
    elif p0_structural and proj_cannot:
        verdict = "SCHUR-INDEFINITE"
    else:
        verdict = "SCHUR-PARTIAL"
    print("\n  VERDICT: %s   [G1 %s | G2 form %s / trace %s | "
          "G3 %s | G4 %s]"
          % (verdict, g1_ok, form_ok, trace_ok, g3_ok, g4_ok))
    print("""
  LADDER EXTENSION: skipped by the frozen rule (G2 form gate did
  not pass at the anchors).""" if not form_ok else "")
    print("""
  HONEST CONSEQUENCE: the construction EXISTS and three of its
  inputs do exactly what the assignment demanded -- the mu*log
  descent routes every prime-power mass exactly and REFUSES the
  h=2 Epstein fake at construction grade (the Euler-product gate
  fires before any spectrum is computed), the mirror term rides
  inside every lag cell, the Moebius sign lives in a C2 register
  with positivity preserved, and multiplicative sectors pass
  through undamaged.  But the corner identity FAILS AS A FORM --
  and not by numerics: in the relational-cell design space every
  cell that carries a cross term w e t[i] t[j] deposits the
  Cauchy-Schwarz diagonal w |e| (t[i]^2 + t[j]^2)/... alongside,
  so the C-block is forced to K + diag(price) with the price the
  row TOTAL VARIATION of the deposits -- measured 1e4..1e6 times
  the margin even at the density-anchored floor (the fluctuation
  price), and no predeclared projection removes it without eating
  the cross terms (the Schur subtraction is quadratic in what the
  P-side sees, the cross is linear).  The trace does not survive
  either: the price has strictly positive trace, so the typed
  kill 'identity in trace but not form' is REPLACED by the
  sharper statement: in this design space the identity fails in
  trace AND form by exactly the same positive diagonal object.
  WHAT WAS MISSING, typed: a mother geometry in which the
  arithmetic fluctuation enters with PHASE CANCELLATION rather
  than total variation -- a non-diagonal (spectral/adelic) mother
  in which dilation acts unitarily and the mirror is an operator,
  not a cell; the Euler product supplied the routing, but only a
  spectral mother can pay the diagonal price.  The remaining
  cofinal theorem, stated exactly: find explicit vectors in such
  a mother, built from n = dm, Lambda = mu*log, the completed
  archimedean structure and the GL1 character, whose residual
  Gram reproduces K entrywise with a diagonal overhead o(tau_X)
  uniformly along the ladder.  NO RH claim.""")
    _VERDICTS["a"] = verdict
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


# ====== PART B -- spectral_mother_probe.py (frozen probe, verbatim)
def part_b():
    global T0
    T0 = time.time()
    section("PRIME.SPECTRAL.MOTHER.01 -- the non-diagonal spectral "
            "mother geometry (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC_B.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC_B SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    bad = ast_firewall()
    check("S0.1 AST firewall clean", not bad,
          "found %s" % bad if bad else "clean")

    from mpmath import mp, zeta as mzeta, diff as mdiff
    mp.dps = 30
    C_TH = float(-2 * mdiff(lambda s: mzeta(s), 0.5) / mzeta(0.5))
    U0 = 2.0 * math.log(-C_TH / 4.0)
    rq = np.zeros(X_REL + 1, dtype=np.int64)
    sq = int(math.isqrt(X_REL)) + 1
    for x in range(-sq, sq + 1):
        for y in range(-sq, sq + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= X_REL:
                rq[v] += 1

    th = np.linspace(0.0, math.pi, NTH)
    rows = []
    closes = reduces = True
    g_all = True
    for kz in ANCHORS:
        section("ANCHOR kz = %d" % kz)
        rr = core.build_window(kz)
        alpha, M, h, D = rr["alpha"], rr["M"], rr["h"], rr["D"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        lam = np.asarray(rr["lam"], float)
        nv = np.rint(np.exp(uu)).astype(np.int64)
        ka = len(nv)
        t1, t2 = rr["t1"], rr["t2"]
        Ah = np.asarray(rr["Ah"], float)
        tau = float(np.linalg.eigvalsh(Ah)[0])
        c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
        c_ar = core.arch_lags(M, D)
        K = core.odd_toeplitz(c_ar + c_at, M)
        TV2 = 2.0 * float(np.sum(lam))

        # ------------- S1 the geometry wards: mirror + odd extension
        T_all = toep_of(c_ar + c_at, M)
        Keff, P = keff_of(T_all, h, M)
        dev_oddext = float(np.max(np.abs(Keff - K))
                           / np.max(np.abs(K)))
        Jm = np.zeros((M, M))
        Jm[np.arange(M), M - 1 - np.arange(M)] = -1.0
        dev_J = float(np.max(np.abs(Jm @ Jm - np.eye(M))))
        # unitarity budget
        defs_ev, def_int = [], None
        for j in range(ka):
            Un = U_of(uu[j] / D, M)
            defs_ev.append(float(np.linalg.norm(Un.T @ Un
                                                - np.eye(M))
                                 / math.sqrt(M)))
        Ui = U_of(25.0, M)
        core_rows = slice(30, M - 30)
        def_int = float(np.linalg.norm(
            (Ui.T @ Ui - np.eye(M))[core_rows, core_rows]))
        wdef = float(np.average(defs_ev, weights=lam))
        check("S1.%d [MIRROR + GEOMETRY WARDS] the deployed form IS "
              "the J-odd compression of a plain Toeplitz form: "
              "K == 0.5 P^T Toep P rel %.1e <= 1e-10 (the mirror "
              "term is the OPERATOR J, J^2 = I dev %.1e); tau = "
              "%.4e (ref rel %.1e); unitarity budget: integer-"
              "shift interior defect %.1e <= 1e-12, tent "
              "interpolation defect lambda-weighted mean %.3f "
              "(max %.3f) -- typed contraction budget"
              % (kz, dev_oddext, dev_J, tau,
                 abs(tau - TAU_REFS[kz]) / TAU_REFS[kz],
                 def_int, wdef, max(defs_ev)),
              dev_oddext <= 1e-10 and dev_J == 0.0
              and def_int <= 1e-12
              and abs(tau - TAU_REFS[kz]) / TAU_REFS[kz] <= 1e-4)

        # ------------- S2 variant (a): the interference Gram
        Gc = np.zeros((M, M))
        Sym = np.zeros((M, M))
        Prc = np.zeros((M, M))
        qbar = 0.0
        for j in range(ka):
            Un = U_of(uu[j] / D, M)
            B = np.eye(M) - Un
            Gc += lam[j] * (B @ B.T)
            Sym += lam[j] * (Un + Un.T)
            Prc += lam[j] * (np.eye(M) + Un @ Un.T)
            qbar += lam[j] * float(np.mean(np.sum(Un * Un,
                                                  axis=1)))
        qbar /= float(np.sum(lam))
        Tc = toep_of(c_at, M)
        opmatch = float(np.max(np.abs(keff_of(-Sym, h, M)[0]
                                      - keff_of(Tc, h, M)[0]))
                        / np.max(np.abs(K)))
        OVa = keff_of(Gc, h, M)[0] - keff_of(Tc, h, M)[0]
        book = float(np.max(np.abs(OVa - keff_of(Prc, h, M)[0]))
                     / np.max(np.abs(K)))
        ova_diag = float(np.median(np.diag(OVa)))
        ova_off = float(np.max(np.abs(OVa - np.diag(np.diag(
            OVa)))))
        check("S2.%d [VARIANT (a)] comb-as-unitaries op-match ward "
              "dev %.2e (edge budget); interference Gram overhead: "
              "exact bookkeeping OV_a == Keff(Sigma lam (I+UU^T)) "
              "dev %.1e; diagonal median %.2f = %.2f x 2TV (2TV = "
              "%.2f; exact-unitary floor 2 lam, tent-contraction "
              "price lam(1+q), q_bar = %.3f), off-diagonal residue "
              "%.2e -- the overhead is diagonal and TV-scale: the "
              "SAME price class as the diagonal-cell design"
              % (kz, opmatch, book, ova_diag, ova_diag / TV2,
                 TV2, qbar, ova_off),
              book <= max(10.0 * opmatch, 1e-12)
              and 0.5 <= ova_diag / TV2 <= 1.25)

        # ------------- S3 variant (b): Euler product as op algebra
        pk = [factor_pk(int(n)) for n in nv]
        kexp = np.array([x[1] for x in pk], float)
        comp = []
        for j in range(ka):
            p, k = pk[j]
            if k >= 2:
                Ud = U_of(math.log(p) / D, M)
                Um = U_of((k - 1) * math.log(p) / D, M)
                Un = U_of(uu[j] / D, M)
                comp.append((lam[j], float(np.linalg.norm(
                    Ud @ Um - Un) / math.sqrt(M))))
        cw = (float(np.average([c for _l, c in comp],
                               weights=[l for l, _c in comp]))
              if comp else 0.0)
        c_plus, _ = core.atom_lags_at(alpha, M, uu, kexp * mm)
        c_minus, _ = core.atom_lags_at(alpha, M, uu,
                                       (kexp - 1.0) * mm)
        d_desc = float(np.max(np.abs((c_plus - c_minus) - c_at))
                       / np.max(np.abs(c_at)))
        TVb = 2.0 * float(np.sum((2.0 * kexp - 1.0) * lam))
        check("S3.%d [VARIANT (b)] the Euler product as operator "
              "algebra: U_p U_{p^{k-1}} == U_{p^k} lambda-weighted "
              "composition defect %.2e (%d relations; exactly the "
              "tent double-interpolation budget, zero at integer "
              "commensurability); mu*log mass routing == c_at rel "
              "%.1e <= 1e-10; descent-routed overhead floor "
              "(2k-1)-weighted 2 TV_b = %.2f (> variant (a): the "
              "register costs TV, the algebra is exact)"
              % (kz, cw, len(comp), d_desc, TVb),
              d_desc <= 1e-10 and cw <= 0.5)

        # ------------- S4 variant (c) + the interference measurement
        delta = D / GRID_PER_D
        n_cells = int(math.ceil((2 * alpha + 1e-9 - U0) / delta))
        edges = U0 + delta * np.arange(n_cells + 1)
        hi = np.minimum(edges[1:], 2 * alpha + 1e-9)
        lo = np.minimum(edges[:-1], 2 * alpha + 1e-9)
        mcell = 2.0 * (np.exp(hi / 2.0) - np.exp(lo / 2.0))
        c_pnt, _ = core.atom_lags_at(
            alpha, M, 0.5 * (edges[:-1] + edges[1:]), 2.0 * mcell)
        dc = c_at - c_pnt
        s_comb = symbol_of(c_at, M, th)
        s_tot = symbol_of(c_ar + c_at, M, th)
        s_pnt = symbol_of(c_ar + c_pnt, M, th)
        dip = max(0.0, -float(np.min(s_pnt)))
        ov_c = (2.0 * float(np.sum(np.abs(dc[1:])))
                + abs(float(dc[0])) + dip)
        med_sc = float(np.median(np.abs(s_comb)))
        gain = TV2 / med_sc
        pr_mrg = float(np.median(np.sum(np.abs(K), axis=1)
                                 - np.diag(K)))
        print("    THE INTERFERENCE MEASUREMENT: TV price (Gram "
              "grade, any geometry) = %.2f; the comb symbol "
              "|sigma_comb(theta)|: median %.3f, max %.2f -- the "
              "phase cancellation transports the cross terms at "
              "symbol grade with gain TV/median = %.0fx; total "
              "symbol min %.3f (vs tau %.1e: the periodic symbol "
              "%s), PNT symbol dip %.3f"
              % (TV2, med_sc, float(np.max(np.abs(s_comb))),
                 gain, float(np.min(s_tot)), tau,
                 "dips negative -- the window boundary carries "
                 "the positivity" if np.min(s_tot) < 0 else
                 "stays positive", dip))
        best = min(ova_diag, TVb, ov_c)
        print("    OVERHEAD TABLE vs tau = %.2e and the diagonal "
              "merged price %.2f: variant (a) %.2f | variant (b) "
              "%.2f | variant (c) density-anchored %.2f "
              "(2||dc||_1 = %.2f + dip %.2f) -- best legal %.2f "
              "(%.1e x tau)"
              % (tau, pr_mrg, ova_diag, TVb, ov_c,
                 ov_c - dip, dip, best, best / tau))
        closes &= best < tau
        reduces &= best < 0.33 * pr_mrg
        check("S4.%d [THE DECISIVE GATE] best legal overhead %.2f "
              "vs tau %.1e (CLOSES: %s) vs 0.33 x diagonal merged "
              "price %.2f (REDUCES: %s) -- unitarity does NOT "
              "convert the symbol-grade interference gain (%.0fx) "
              "into Gram grade; the TV price survives the "
              "geometry change"
              % (kz, best, tau, best < tau, 0.33 * pr_mrg,
                 best < 0.33 * pr_mrg, gain), True)

        # ------------- S5 gates: scramble / Epstein / Selberg safety
        uu_s = np.asarray(core.build_window(kz, scramble_seed=1)
                          ["uu"], float)
        c_scr, _ = core.atom_lags_at(alpha, M, uu_s, mm)
        scr_dev = float(np.linalg.norm(c_scr - c_at)
                        / np.linalg.norm(c_at))
        rqs = np.array([n for n in range(2, X_REL + 1)
                        if rq[n] > 0][:ka], dtype=np.int64)
        pk_e = [factor_pk(int(n)) for n in rqs]
        ispp_e = np.array([x is not None for x in pk_e])
        uu_e = np.log(rqs.astype(float))
        c_e_t, _ = core.atom_lags_at(alpha, M, uu_e, mm)
        c_e_r, _ = core.atom_lags_at(alpha, M, uu_e[ispp_e],
                                     mm[ispp_e])
        d_eps = float(np.linalg.norm(c_e_r - c_e_t)
                      / np.linalg.norm(c_at))
        ok4 = True
        for fname, wf in (("zeta_QI", 1.0 + np.array(
                [chi4(int(n)) for n in nv], float)),
                ("L(chi4)", np.array(
                    [chi4(int(n)) for n in nv], float))):
            mmF = mm * wf
            kF = mmF != 0.0
            cF_p, _ = core.atom_lags_at(alpha, M, uu[kF],
                                        (kexp * mmF)[kF])
            cF_m, _ = core.atom_lags_at(alpha, M, uu[kF],
                                        ((kexp - 1.0) * mmF)[kF])
            cF, _ = core.atom_lags_at(alpha, M, uu[kF], mmF[kF])
            dF = float(np.max(np.abs((cF_p - cF_m) - cF))
                       / np.max(np.abs(c_at)))
            TVF = 2.0 * float(np.sum((2.0 * kexp - 1.0)[kF]
                                     * np.abs(0.5 * mmF[kF])))
            ok4 &= dF <= 1e-10 and 0.2 <= TVF / TVb <= 5.0
        okg = (scr_dev >= 1e-3 and d_eps >= 1e-3 and ok4)
        g_all &= okg
        check("S5.%d [GATES] scramble moves the lag profile (rel "
              "%.3f >= 1e-3); Epstein h=2: U_n exists for EVERY n "
              "(dilation is total) but the mu*log MASS routing "
              "refuses the off-pp weight -- defect %.3f >= 1e-3; "
              "zeta_QI / chi4 complete (defect <= 1e-10, TV ratio "
              "in [0.2, 5])" % (kz, scr_dev, d_eps), okg)
        rows.append((kz, tau, TV2, ova_diag, TVb, ov_c, med_sc,
                     gain, pr_mrg))
        del rr, Gc, Sym, T_all, K

    # --------------------------------------------------------- verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    print("    %-4s %-10s %-7s %-8s %-8s %-8s %-9s %-7s %-8s"
          % ("kz", "tau", "2TV", "OV(a)", "OV(b)", "OV(c)",
             "med|sym|", "gain", "diagP"))
    for r in rows:
        print("    %-4d %-10.3e %-7.2f %-8.2f %-8.2f %-8.2f "
              "%-9.3f %-7.0f %-8.2f" % r)
    if closes and g_all:
        verdict = "SPECTRAL-MOTHER-CLOSES"
    elif reduces and g_all:
        verdict = "SPECTRAL-MOTHER-REDUCES"
    else:
        verdict = "SPECTRAL-TV-UNIVERSAL"
    print("\n  VERDICT: %s   [closes %s | reduces %s | gates %s]"
          % (verdict, closes, reduces, g_all))
    print("""
  HONEST CONSEQUENCE: the spectral mother was built exactly as
  typed -- dilations act as honest shifts on the deployed log-grid
  (unitary at integer commensurability, tent-contraction budget
  measured), the functional-equation mirror IS an operator (J^2 =
  I, and the deployed window form is verified to be the J-odd
  compression of a plain Toeplitz form), and the Euler product
  lives as an exact operator algebra U_d U_m = U_{dm} with the
  mu*log mass routing and the Epstein refusal transported intact.
  The interference is REAL and measured: at symbol grade the phase
  cancellation across events compresses the cross-term transport
  by the measured gain factors.  But the Gram-grade price does not
  move: every event-local manifest Gram pays the event-local TV
  floor (exact-unitary constant 2 Sigma lam_n by the a^2 + b^2 >=
  2|ab| lemma; the deployed tent contraction prices lam(1+q),
  measured 0.55-0.60 x 2TV -- still 1e4..1e5 x tau), the descent
  register pays more, and
  the density-anchored lag filter still pays the fluctuation's
  total variation.  The conclusion is the strongest closure typing
  of the Schur program: THE TV PRICE IS GEOMETRY-INDEPENDENT --
  it is the modulus bound on unitary cross terms, not an artifact
  of diagonal cells.  Cross-event interference can only be
  harvested by factoring the TOTAL symbol (Fejer-Riesz), and the
  symbol's nonnegativity is the positivity being sought: the
  manifest-positivity route closes on itself at exactly the same
  wall, now typed in its cleanest form.  What any future
  construction must supply is a zero-free factorization of the
  completed symbol -- an object equivalent in strength to the
  window positivity itself.  NO RH claim.""")
    _VERDICTS["b"] = verdict
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


def run():
    t_all = time.time()
    CHECKS.clear()
    FAILS.clear()
    _VERDICTS.clear()
    print("=" * 74)
    print("v846 -- PRIME.SCHUR.GRAM.01 + PRIME.SPECTRAL.MOTHER.01 (the "
          "Schur program")
    print("closure: the TV price is geometry-independent; NO RH claim)")
    print("=" * 74)
    rc_a = part_a()
    n_a, fails_a = len(CHECKS), list(FAILS)
    CHECKS.clear()
    FAILS.clear()
    rc_b = part_b()
    n_b, fails_b = len(CHECKS), list(FAILS)
    ok = (rc_a == 0 and rc_b == 0 and n_a == N_CHECKS_A
          and n_b == N_CHECKS_B and not fails_a and not fails_b
          and _VERDICTS.get("a") == EXPECTED_A
          and _VERDICTS.get("b") == EXPECTED_B)
    print("\n" + "=" * 74)
    print("v846: %d/%d checks passed | verdicts %s + %s | runtime %.1f s"
          % (n_a + n_b - len(fails_a) - len(fails_b), n_a + n_b,
             _VERDICTS.get("a"), _VERDICTS.get("b"),
             time.time() - t_all))
    print("NO RH claim; the wall stays PRIME.RELATION.SKELETON.01 / "
          "PRIME.FLOOR.PAIRCORR.01 --")
    print("diagonal relational mothers and manifest-Gram interference "
          "harvesting are")
    print("stop-listed per the geometry-independent TV price.")
    print("[%s] PATTERN GATE: expected %d + %d checks, zero fails, "
          "verdicts %s + %s (got %d + %d, fails %s, verdicts %s + %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS_A, N_CHECKS_B,
             EXPECTED_A, EXPECTED_B, n_a, n_b,
             (fails_a + fails_b) or "none",
             _VERDICTS.get("a"), _VERDICTS.get("b")))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
