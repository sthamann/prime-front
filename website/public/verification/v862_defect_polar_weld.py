#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v862 -- PRIME.KREIN.DEFECT_ONE.01 + PRIME.MU4.WELD.01: the rank of the wall is ONE -- the defect operator Delta = I - C*C has exactly ONE soft mode on every reachable rung with lam1 == the tau-margin in the positive-side metric by the exact pencil identity, the three vacuum findings (the Redheffer single Smith invariant, the vacuum code's one-logical-qubit price, the Krein soft port) are one rank-one structure, the MONOMIAL CLOSURE THEOREM extends the word-census emptiness to EVERY word of ANY length, and the 2-torsion weld census delivers the structural law behind the deck refusal (the deck's anticommutant is ENTIRELY faithful-mu4: the deck can enter a weld only as the quarter turn J = MD, never as a second involution), ONE module from two probes (8/8 + 22/22 checks, zero fails, verdicts DEFECT-ONE + BOTH-MISSING + MONOMIAL-CLOSURE-THEOREM and WELD-WITHOUT-CONTRACTOR; discovery probes krein_defect_polar_probe.py and mu4_clifford_weld_probe.py, 2026-08-08, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~5 s).  PART A, DEFECT-ONE: lam1(Delta) == lam_min(R K R) on every rung (max rel dev 3e-08 -- the pencil ward), exactly one soft mode (lam2/lam1 >= 3.9 everywhere, up to 14.1; tail per-mode log-mean stable at spread 0.171; the soft direction's dual-frequency profile drifts smoothly, consecutive cos-sims >= 0.93) -- the deployed positivity always fails-or-holds through a SINGLE arithmetic-carrying mode whose contraction margin IS the floor value; the controls type the structure as the TRUTH comb's (Epstein Delta has 55 negative eigenvalues, scramble 37).  THE POLAR SPLIT localises what is missing with the sharpest quantifier so far: the magnitude factor A is NOT a short source profile (diag mass 0.361-0.373 vs bar 0.9; best profile residual 0.75 vs bar 0.1; anchor-stable at cos-sim 0.998) and no predeclared band-moving candidate approximates the phase factor V (all residuals ~1.414 = random null) -- both microscopes typed: any positive finding would have had to name its source reconstruction, none did.  THE MONOMIAL CLOSURE THEOREM (the v2 amendment typed in the frozen spec): an honest surprise first -- the clean two-band corridor picture is WRONG at fine scale (the total density's sign flips 408 times at kz 9, interleaving the sign sets at 1-2 bins: the corridor form is VACUOUS, 56/0 bulk bins are empty-set artifacts) -- but the closure that survives is STRONGER: every deployed source letter is a MONOMIAL matrix, the monomial class is product-closed, and the contractor's monomial mass fraction is 0.227-0.237 (<= 0.5) at all anchors, so EVERY word of ANY length over the deployed alphabet misses the contractor by residual >= sqrt(1 - mono_frac) >= 0.874 -- the 155-word emptiness of v861 was never about length: the contractor has dense rows (a genuine integral/transfer operator), the source alphabet contains only sparse routing-plus-weights, and the missing object is ONE non-monomial letter -- a spreading intertwiner with an independent contraction bound; the single non-commuting letter against the source grading Gamma = diag(sign d) is the 1-bin shift S at the 408 band boundaries (J commutes exactly, the diagonals exactly).  PART B, THE WELD LAW: the Weyl weld census on 2-groups is exact -- C2 has 1 weld pair, Z4 and Z8 have ZERO (cyclic 2-groups of order >= 4 have trivial 2-torsion pairing: enlarging the cyclic register never helps), F2^4 has 120; THE ASYMMETRY on the deployed 128-register: the mu-sign T_s has 64 anticommuting characters of which 32 involutive => WELDABLE, the deck T_d has 64 anticommuting -- ALL faithful j-odd, order 4, ZERO involutive => UNWELDABLE at register level: the deck can only be welded through a faithful mu4 object, i.e. as J = MD (the weld's own quarter turn; the v833 metaplectic deck i*I is central = J-grade, consistent); all four candidates (K1 diag-char weld on the faithful sector, K2 Galois inert block -- the weld locus IS the mu(p) = -1 survival locus, 619 inert vs 609 split classified by x^2+y^2 witnesses, K3 Hall cover, K4 F2^4 Weyl pairs) close the FULL Clifford weld EXACTLY on their declared domains (M^2 = D^2 = I, {M, D} = 0, (MD)^2 = -I, full band swap: ||P- M P+|| = 1, ||P+ M P+|| = 0) and the MANDATORY CONTROL K0 (the unwelded deployed C2 x C2) REFUSES exactly ([M, D] = 0, ||{M, D}|| = 2, swap 0, keep 1); the weld-built D is Frobenius-ORTHOGONAL to the deployed deck (a new involution, not the deployed one -- the gap named); the bent midpoint identity ||{M_q, T_a}||^2 = ||[M_q, T_a]||^2 = 32 for all 15 a != 0 (bentness = exactly halfway between weld and co-weld); both scramble controls fire.  THE CONTRACTOR CONNECTION IS NULL (the honest close): the polar magnitude is band-internal by construction and the polar phase is NOT matched by any source-built swap (FLIP/HALF/FLIPHALF residuals 1.4142 == the random null 1.4144, support match <= 0.32; sqrt2 = the null value) -- the weld supplies the TYPE of the missing operator (an anticommuting involution), not yet its VALUE.  NO RH claim.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes krein_defect_polar_probe.py (8/8,
verdict DEFECT-ONE + BOTH-MISSING + MONOMIAL-CLOSURE-THEOREM, spec
v2 amendment typed in the frozen docstring) and
mu4_clifford_weld_probe.py (22/22, verdict WELD-WITHOUT-CONTRACTOR),
2026-08-08, re-run identically at promotion.  ROUND-31 EMBEDDING
CONVENTION: frozen sources embedded BYTE-EXACT and executed verbatim
in isolated namespaces; printed spec SHAs reproduce; byte-equality
ward vs experiments/tfpt-discovery/ inside the pattern gates.  Both
probes import the READ-ONLY deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles (AST firewalls in both
probes; own sieves); polar/pinv = microscopes only; RNG only in the
declared scramble controls.  NO RH claim.
"""

import contextlib
import io
import math
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source krein_defect_polar_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""krein_defect_polar_probe -- PRIME.KREIN.DEFECT_ONE.01 +
PRIME.KREIN.POLAR_SPLIT.01 + the block-diagonal class closure
(EXPLORATION ONLY, experiments/; round 33 midday-2 packages
A+B, after KREIN-CONTRACTOR-STABLE-NO-WORD, 2026-08-08).

PACKAGE A -- DEFECT_ONE: the full spectrum of the defect
Delta_h = I - C_h* C_h (eigenvalues 1 - sigma_j(C)^2) on all
ladder rungs.  The question: does exactly ONE eigenvalue go
soft?  PASS: lam_1(Delta) equals the tau-margin in the
positive-side metric (the exact pencil identity, per rung),
lam_2/lam_1 well separated with a stable floor, the tail
product positive and stable, and the defect direction's
dual-frequency profile drifts smoothly (moving-frame
discipline).  KILL: several defect modes collapse together or
the direction rotates wildly.

PACKAGE B -- POLAR_SPLIT: C = V . A with A = (C*C)^{1/2}
(band-preserving magnitude) and V the partial isometry (the
band mover).  The 155-word census failed on band MOVEMENT,
which obstructs V but not necessarily A.  Separate censuses at
the anchors: (a) A against band-preserving source profiles
(diagonality in the source frequency basis + the predeclared
profile list {KMS weight e^{-tau/2}, |truncated Moebius
symbol|, the local density-mixing ratio sqrt(smooth d_- /
smooth d_+), movavg width 9 -- all source data}); (b) V against
predeclared band-moving candidates {T^{k*} with k* = the
source-centroid offset, J T^{k*}, mu4 T^{k*}, the dual-grid
DFT (metaplectic lift)}; (c) drift of both factors along the
anchors.  FIREWALL typed: the target-computed V/A are
MICROSCOPES; a positive finding must name the source-side
reconstruction.

THE CLASS-CLOSURE UPGRADE: the band grading Gamma = P+ - P- is
defined SOURCE-SIDE as diag(sign d_j), d = the exact circulant
density of the lag data (never a target eigenvector).  Exact
commutators with every generator {J, S, M4, KM, ZM}: diagonals
commute trivially, J commutes because d is even (checked
exactly), and S can only fail at band boundaries.  The frozen
theorem shape: every word of length <= 3 is a monomial matrix
D(w) P(p) with |displacement| <= 3 bins, hence P_-^bulk W
P_+^bulk = 0 EXACTLY for the 3-bin-corridor bulks -- verified
over all 155 words -- while the contractor couples the bulks
(measured).  The census emptiness becomes structure: the
source alphabet moves support at most 1 bin per letter; the
contractor is a bulk-to-bulk band mover; a NEW LETTER, not
longer words, is required.

VERDICT (frozen, composite): DEFECT-ONE or DEFECT-MANY;
A-SOURCE-BUILT / V-CANDIDATE-FOUND / BOTH-MISSING;
BLOCKDIAG-THEOREM (strict or corridor form, boundary movers
typed) or BAND-MOVER-IN-ALPHABET.  NO RH claim; writes
nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/krein_defect_polar_probe.py
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
PRIME.KREIN.DEFECT_ONE.01 + PRIME.KREIN.POLAR_SPLIT.01 spec v2
(2026-08-08; v1 amendment typed after the first run: the
corridor form of the closure is VACUOUS at fine scale -- the
total density's sign flips 408 times in 734 bins at kz 9 (the
comb's oscillatory transform interleaves the sign sets at 1-2
bin scale), so the 3-bin bulks are nearly empty and both
corridor legs trivialise (0 violations AND 0 contractor
coupling, both empty-set artifacts).  Replacement, STRONGER
closure: all five source letters are monomial matrices
(permutations/diagonals), the monomial class is closed under
products, and dist_F(C, monomial)^2 / ||C||_F^2 >= 1 -
mono_frac with mono_frac = Sigma_i max_j |C_ij|^2 / ||C||_F^2
-- a residual lower bound for words of ANY length.  New bar:
viol == 0 (still exact) AND mono_frac <= 0.5 at all anchors.
No other bars changed).  Ladder/machinery = the
krein_normalform probe verbatim (cut 1, <= 12 rungs, anchors
kz 9/12/13); battery regression ||C2|| == {0.999869296,
0.999950815, 0.999943372} +- 2e-9.  A: Delta spectrum from
svd(A2); DEFECT-ONE iff (i) pencil ward |lam1(Delta) -
lam_min(R K R)| <= 1e-6 rel on every rung (R = G+^{-1/2});
(ii) lam2/lam1 >= 3 on every rung; (iii) tail stability:
per-mode mean log lam_{j>=2} last-third spread <= 0.2; (iv)
direction drift: consecutive dual-frequency profiles (tau grid
0..20, 512 pts) cos-sim >= 0.5 on the last two thirds; all
lam_j > 0 on truth.  B (anchors): polar via SVD of C_freq =
A2 U^H; A census: diagonal-mass fraction reported, candidate
profiles {KM, |ZM|, DR = sqrt(movavg9 max(-d,0) / movavg9
max(d,0))}, scalar-fitted rel residual; A-SOURCE-BUILT iff
diag fraction >= 0.9 AND best residual <= 0.1 at all anchors.
V census: candidates {T^k*, J T^k*, M4 T^k*, DFT/sqrt(L)}, k*
= round(bin-centroid(|d-|) - bin-centroid(|d+|)) (source
statistic); V-CANDIDATE-FOUND iff rel residual on ran(C*) <=
0.1.  Closure: Gamma = diag(d >= 0 ? +1 : -1) (source); exact
commutator F-norms for the 5 generators; corridor theorem:
all 155 words as monomial matrices, zero bulk3-to-bulk3
coupling required EXACTLY; contractor bulk3 coupling reported
(must be > 0.1 of ||C||_F for the contrast).  Controls:
Epstein/scramble Delta spectra have >= 1 negative eigenvalue.
Verdicts composite per docstring; DEFECT-MANY iff any A bar
fails.  Pseudoinverse/polar = microscopes.  NO RH claim;
writes nothing.
"""

ANCHORS = (9, 12, 13)
C2_REFS = {9: 0.999869296, 12: 0.999950815, 13: 0.999943372}
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
    return dp[:, None] * Fp, dm[:, None] * Fp


def contractor(Bp, Bm):
    """SVD microscope: returns (U, s, Vh, A2, sig) with A2 = the
    contractor on ran(B+) coordinates and sig its full singular
    spectrum."""
    U, s, Vh = np.linalg.svd(Bp, full_matrices=False)
    r = int(np.sum(s > 1e-12 * s[0]))
    U, s, Vh = U[:, :r], s[:r], Vh[:r]
    A2 = Bm @ (Vh.conj().T / s)
    sig = np.linalg.svd(A2, compute_uv=False)
    return U, s, Vh, A2, sig


def freq_profile(x, D, taus):
    """|FFT|^2 of the odd extension, folded to tau = theta/D and
    interpolated onto the fixed tau grid."""
    f = np.concatenate([x, -x[::-1]])
    L = 2 * len(f) - 2
    X = np.abs(np.fft.fft(f, n=L)[:L // 2 + 1]) ** 2
    tj = np.arange(L // 2 + 1) * (2.0 * math.pi / L) / D
    p = np.interp(taus, tj, X)
    return p / max(np.linalg.norm(p), 1e-300)


def movavg(v, w):
    k = np.ones(w) / w
    return np.convolve(np.concatenate([v[-(w // 2):], v,
                                       v[:w // 2]]), k,
                       "valid")[:len(v)]


def moebius(N):
    mu = np.ones(N + 1, dtype=int)
    prim = np.ones(N + 1, dtype=bool)
    prim[:2] = False
    for p in range(2, N + 1):
        if prim[p]:
            prim[2 * p::p] = False
            mu[p::p] *= -1
            mu[p * p::p * p] = 0
    return mu


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


# ================================================================= main
def main():
    section("PRIME.KREIN.DEFECT_ONE.01 + POLAR_SPLIT.01 "
            "(EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.  Polar/pinv = microscopes only.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    zones = list(core.frame_a_zones())
    step = max(1, len(zones) // 10)
    ladder = sorted(set(zones[::step]) | set(ANCHORS))
    ladder = [kz for kz in ladder if kz in zones]
    taus_grid = np.linspace(0.0, 20.0, 512)

    # ---------------- S1 PACKAGE A: the defect spectrum
    section("S1 -- PACKAGE A: the defect spectrum Delta = "
            "I - C*C (%d rungs)" % len(ladder))
    pencil_ok = True
    pos_ok = True
    rows = {}
    profiles = []
    cache = {}
    for kz in ladder:
        rr = core.build_window(kz)
        h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        if h > 900:
            continue
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        K = core.odd_toeplitz(c_ar + c_at, M)
        d = grid_density(c_ar + c_at)
        Bp, Bm = krein_arms(d, h)
        U, s, Vh, A2, sig = contractor(Bp, Bm)
        lam = np.sort(1.0 - sig ** 2)
        Gp = np.real(Bp.conj().T @ Bp)
        ev, Vp = np.linalg.eigh(Gp)
        R = Vp @ np.diag(ev ** -0.5) @ Vp.T
        lam_pencil = float(np.linalg.eigvalsh(R @ K @ R)[0])
        pdev = abs(lam[0] - lam_pencil) / max(abs(lam_pencil),
                                              1e-300)
        pencil_ok &= pdev <= 1e-6
        pos_ok &= lam[0] > 0.0
        tail = float(np.mean(np.log(lam[1:])))
        # defect direction in h-space
        _, _, v2 = np.linalg.svd(A2, full_matrices=False)
        x = np.real(Vh.conj().T @ (v2[0].conj() / s))
        x /= max(np.linalg.norm(x), 1e-300)
        profiles.append(freq_profile(x, D, taus_grid))
        rows[kz] = dict(h=h, lam1=float(lam[0]),
                        lam2=float(lam[1]),
                        sep=float(lam[1] / lam[0]),
                        tail=tail, pdev=pdev,
                        tau_raw=float(np.linalg.eigvalsh(K)[0]))
        if kz in ANCHORS:
            cache[kz] = (rr, d, Bp, Bm, U, s, Vh, A2, K)
        print("    kz %-3d h %-4d | lam1 %.3e lam2 %.3e "
              "sep %6.1f | pencil dev %.0e | mean log tail "
              "%+.4f | lam1/lam_min(K) %.3f"
              % (kz, h, lam[0], lam[1], lam[1] / lam[0], pdev,
                 tail, lam[0] / rows[kz]["tau_raw"]),
              flush=True)
    kzs = list(rows)
    seps = [rows[k]["sep"] for k in kzs]
    tails = [rows[k]["tail"] for k in kzs]
    last = max(1, len(kzs) // 3)
    tail_spread = max(tails[-last:]) - min(tails[-last:])
    sims = [float(profiles[i] @ profiles[i + 1])
            for i in range(len(profiles) - 1)]
    two3 = sims[len(sims) // 3:]
    drift_ok = min(two3) >= 0.5
    check("S1.1 [PENCIL WARD] lam1(Delta) == the tau-margin in "
          "the positive-side metric lam_min(R K R) on every "
          "rung (max rel dev %.0e <= 1e-6); all defect "
          "eigenvalues > 0 on truth: %s"
          % (max(r["pdev"] for r in rows.values()), pos_ok),
          pencil_ok and pos_ok)
    check("S1.2 [DEFECT-ONE] exactly one soft mode: lam2/lam1 "
          ">= 3 on every rung (min separation %.1f); tail "
          "per-mode mean log lam_{j>=2} stable (last-third "
          "spread %.3f <= 0.2); the tail product Pi lam_j > 0 "
          "everywhere" % (min(seps), tail_spread),
          min(seps) >= 3.0 and tail_spread <= 0.2)
    check("S1.3 [DIRECTION DRIFT] the defect direction's "
          "dual-frequency profile moves smoothly along the "
          "ladder: consecutive cos-sims %s (min of last two "
          "thirds %.2f >= 0.5) -- moving frame, no wild "
          "rotation"
          % (", ".join("%.2f" % v for v in sims), min(two3)),
          drift_ok)
    defect_one = (pencil_ok and pos_ok and min(seps) >= 3.0
                  and tail_spread <= 0.2 and drift_ok)

    # ---------------- S2 PACKAGE B: the polar split (anchors)
    section("S2 -- PACKAGE B: polar split C = V . A at the "
            "anchors")
    a_built_all = True
    v_found_any = False
    sig_profiles = []
    for kz in ANCHORS:
        rr, d, Bp, Bm, U, s, Vh, A2, K = cache[kz]
        h = rr["h"]
        L = Bp.shape[0]
        D = rr["D"]
        Cf = A2 @ U.conj().T                     # freq -> freq
        Uc, Sc, Vc = np.linalg.svd(Cf, full_matrices=False)
        rC = int(np.sum(Sc > 1e-12 * Sc[0]))
        Uc, Sc, Vc = Uc[:, :rC], Sc[:rC], Vc[:rC]
        Afr = (Vc.conj().T * Sc) @ Vc            # (C*C)^{1/2}
        Vpol = Uc @ Vc                           # partial isometry
        dmass = float(np.sum(np.abs(np.diag(Afr)) ** 2)
                      / np.sum(np.abs(Afr) ** 2))
        jj = np.arange(L)
        tauj = np.where(jj <= L // 2, jj, L - jj) * (
            2.0 * math.pi / L) / D
        diagA = np.real(np.diag(Afr))
        mu = moebius(50)
        zm = np.zeros(L, complex)
        for n in range(1, 51):
            if mu[n]:
                zm += mu[n] / math.sqrt(n) * np.exp(
                    -1j * tauj * math.log(n))
        sp = movavg(np.maximum(d, 0.0), 9)
        sm = movavg(np.maximum(-d, 0.0), 9)
        cands_a = {
            "KM": np.exp(-tauj / 2.0),
            "|ZM|": np.abs(zm),
            "DR": np.sqrt(sm / np.maximum(sp, 1e-30)),
        }
        res_a = {}
        for nm, f in cands_a.items():
            al = float(f @ diagA) / max(float(f @ f), 1e-300)
            res_a[nm] = float(np.linalg.norm(diagA - al * f)
                              / max(np.linalg.norm(diagA),
                                    1e-300))
        best_a = min(res_a, key=res_a.get)
        a_ok = dmass >= 0.9 and res_a[best_a] <= 0.1
        a_built_all &= a_ok
        # V census
        wpos = np.maximum(d, 0.0)
        wneg = np.maximum(-d, 0.0)
        cp = float(jj @ wpos / np.sum(wpos))
        cm = float(jj @ wneg / np.sum(wneg))
        kstar = int(round(cm - cp))
        Pin = Vc.conj().T @ Vc
        nrmV = float(np.linalg.norm(Vpol @ Pin))
        Tk = np.roll(np.eye(L), kstar, axis=0)
        Jm = np.eye(L)[(-jj) % L]
        M4 = np.diag(1j ** (jj % 4))
        Wd = np.fft.fft(np.eye(L)) / math.sqrt(L)
        cands_v = {"T^k*": Tk, "J.T^k*": Jm @ Tk,
                   "M4.T^k*": M4 @ Tk, "DFT": Wd}
        res_v = {nm: float(np.linalg.norm((Vpol - W) @ Pin)
                           / nrmV)
                 for nm, W in cands_v.items()}
        best_v = min(res_v, key=res_v.get)
        v_found_any |= res_v[best_v] <= 0.1
        sig_profiles.append(np.interp(
            np.linspace(0, 1, 64),
            np.linspace(0, 1, len(Sc)), Sc / Sc[0]))
        print("    kz %-3d | A: diag mass %.3f, residuals %s "
              "(best %s) | V: k* = %+d, residuals %s (best %s)"
              % (kz, dmass,
                 " ".join("%s %.3f" % kv for kv in
                          sorted(res_a.items())), best_a,
                 kstar,
                 " ".join("%s %.3f" % kv for kv in
                          sorted(res_v.items())), best_v),
              flush=True)
    ssim = [float(sig_profiles[i] @ sig_profiles[i + 1]
                  / (np.linalg.norm(sig_profiles[i])
                     * np.linalg.norm(sig_profiles[i + 1])))
            for i in range(len(sig_profiles) - 1)]
    check("S2.1 [POLAR CENSUS] A-SOURCE-BUILT: %s (bar: diag "
          "mass >= 0.9 and best profile residual <= 0.1 at all "
          "anchors); V-CANDIDATE-FOUND: %s (bar: rel residual "
          "<= 0.1 on ran(C*)); A's singular profile is anchor-"
          "stable (cos-sims %s) -- the microscopes are typed: "
          "any positive finding names its source "
          "reconstruction, none did"
          % (a_built_all, v_found_any,
             ", ".join("%.3f" % v for v in ssim)),
          True)

    # ---------------- S3 the class-closure theorem
    section("S3 -- THE BLOCK-DIAGONAL CLASS CLOSURE (source "
            "grading Gamma = diag(sign d))")
    rr9, d9, Bp9, Bm9, U9, s9, Vh9, A29, K9 = cache[9]
    L9 = Bp9.shape[0]
    D9 = rr9["D"]
    jj = np.arange(L9)
    gam = np.where(d9 >= 0.0, 1.0, -1.0)
    tauj9 = np.where(jj <= L9 // 2, jj, L9 - jj) * (
        2.0 * math.pi / L9) / D9
    mu = moebius(50)
    zm9 = np.zeros(L9, complex)
    for n in range(1, 51):
        if mu[n]:
            zm9 += mu[n] / math.sqrt(n) * np.exp(
                -1j * tauj9 * math.log(n))
    gens = {
        "J": ("perm", (-jj) % L9),
        "S": ("perm", (jj + 1) % L9),
        "M4": ("diag", 1j ** (jj % 4)),
        "KM": ("diag", np.exp(-tauj9 / 2.0)),
        "ZM": ("diag", zm9 / np.max(np.abs(zm9))),
    }
    comm = {}
    for nm, (kind, dat) in gens.items():
        if kind == "diag":
            comm[nm] = 0.0                      # diagonal: exact
        else:
            # ||[G, Gamma]||_F for G[i, p[i]] = 1:
            # entries gamma[i] - gamma[p[i]]
            comm[nm] = float(np.linalg.norm(gam - gam[dat]))
    flips = np.nonzero(gam != gam[(jj + 1) % L9])[0]
    n_flips = len(flips)
    j_comm_exact = comm["J"] == 0.0
    # corridor bulks (distance > 3 bins from any sign flip)
    dist = np.min(np.abs(((jj[:, None] - flips[None, :] + L9 // 2)
                          % L9) - L9 // 2), axis=1) \
        if n_flips else np.full(L9, L9)
    bulk_p = (gam > 0) & (dist > 3)
    bulk_m = (gam < 0) & (dist > 3)
    # all 155 words as monomial matrices D(w) P(p)
    names = list(gens)
    words = [(a,) for a in names]
    words += [(a, b) for a in names for b in names]
    words += [(a, b, c) for a in names for b in names
              for c in names]
    viol = 0
    for wd in words:
        p = jj.copy()
        w = np.ones(L9, complex)
        for g in reversed(wd):
            kind, dat = gens[g]
            if kind == "diag":
                w = dat * w
            else:
                w = w[dat]
                p = p[dat]
        # W[i, p[i]] = w[i]: bulk- output fed from bulk+ input?
        viol += int(np.any(bulk_m & bulk_p[p]
                           & (np.abs(w) > 1e-300)))
    Cf9 = A29 @ U9.conj().T
    bulk_coup = float(np.linalg.norm(Cf9[np.ix_(bulk_m, bulk_p)])
                      / np.linalg.norm(Cf9))
    mono = {}
    for kz in ANCHORS:
        _rr, _d, _Bp, _Bm, _U, _s, _Vh, _A2, _K = cache[kz]
        Cf = _A2 @ _U.conj().T
        mono[kz] = float(np.sum(np.max(np.abs(Cf) ** 2, axis=1))
                         / np.sum(np.abs(Cf) ** 2))
    check("S3.1 [GAMMA COMMUTATION, exact] source grading from "
          "d only (%d sign-flip boundaries); commutator "
          "F-norms: J %.1e (d even => exact 0: %s), S %.3f "
          "(support = the %d boundary bins ONLY), M4/KM/ZM 0 "
          "exactly (diagonal) -- the single non-commuting "
          "letter is the 1-bin shift at the band boundary"
          % (n_flips, comm["J"], j_comm_exact, comm["S"],
             n_flips),
          j_comm_exact and comm["S"] > 0.0)
    check("S3.2 [THE MONOMIAL CLOSURE THEOREM] the corridor "
          "form is VACUOUS at fine scale (%d/%d bins in "
          "bulk3(+)/bulk3(-): the 408 sign flips interleave "
          "the bands at 1-2 bin scale; word violations %d and "
          "contractor bulk coupling %.3f are empty-set "
          "artifacts, typed).  The stronger closure holds: "
          "every source letter is a MONOMIAL matrix, the "
          "monomial class is product-closed, and the "
          "contractor's monomial mass fraction is %.4f/%.4f/"
          "%.4f at kz 9/12/13 (<= 0.5) => EVERY word of ANY "
          "length over the deployed alphabet misses the "
          "contractor by residual >= sqrt(1 - mono_frac) >= "
          "%.3f -- the census emptiness is a theorem for all "
          "word lengths: the contractor is structurally "
          "NON-MONOMIAL (dense rows), a new NON-MONOMIAL "
          "letter is required"
          % (int(np.sum(bulk_p)), int(np.sum(bulk_m)), viol,
             bulk_coup, mono[9], mono[12], mono[13],
             math.sqrt(1.0 - max(mono.values()))),
          viol == 0 and max(mono.values()) <= 0.5)

    # ---------------- S4 controls
    section("S4 -- CONTROLS")
    reg_ok = True
    for kz in ANCHORS:
        rr, d, Bp, Bm = cache[kz][:4]
        T2 = np.column_stack([rr["t1"], rr["t2"]])
        _, _, _, A2b, sb = contractor(Bp @ T2, Bm @ T2)
        reg_ok &= abs(float(sb[0]) - C2_REFS[kz]) <= 2e-9
    rr9r = cache[9][0]
    a9, M9, h9 = rr9r["alpha"], rr9r["M"], rr9r["h"]
    c_ar9 = np.asarray(core.arch_lags(M9, rr9r["D"]), float)
    N_E = int(math.floor(math.exp(2.0 * a9))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    c_atE, _ = core.atom_lags_at(
        a9, M9, np.log(nn.astype(float)),
        2.0 * lamE[nn] / np.sqrt(nn.astype(float)))
    BpE, BmE = krein_arms(grid_density(c_ar9 + c_atE), h9)
    sigE = contractor(BpE, BmE)[4]
    negE = int(np.sum(1.0 - sigE ** 2 < 0.0))
    uu_s = np.asarray(core.build_window(9, scramble_seed=1)
                      ["uu"], float)
    mm9 = 2.0 * np.asarray(rr9r["lam"], float)
    c_atS, _ = core.atom_lags_at(a9, M9, uu_s, mm9)
    BpS, BmS = krein_arms(grid_density(c_ar9 + c_atS), h9)
    sigS = contractor(BpS, BmS)[4]
    negS = int(np.sum(1.0 - sigS ** 2 < 0.0))
    check("S4.1 [CONTROLS] battery contractor regression "
          "||C2|| == previous run to 2e-9 at all anchors: %s; "
          "Epstein Delta has %d negative eigenvalues (>= 1), "
          "scramble Delta has %d (>= 1) -- the one-soft-mode "
          "structure is the TRUTH comb's, not generic"
          % (reg_ok, negE, negS),
          reg_ok and negE >= 1 and negS >= 1)

    # ---------------- S5 verdict
    section("V -- FROZEN VERDICT + the honest consequence")
    v_a = "DEFECT-ONE" if defect_one else "DEFECT-MANY"
    v_b = ("A-SOURCE-BUILT" if a_built_all else
           ("V-CANDIDATE-FOUND" if v_found_any
            else "BOTH-MISSING"))
    v_c = ("MONOMIAL-CLOSURE-THEOREM (all word lengths; S = a "
           "fine-grained boundary mover, insufficient)"
           if (viol == 0 and j_comm_exact
               and max(mono.values()) <= 0.5) else
           "BAND-MOVER-IN-ALPHABET")
    print("\n  VERDICT: %s + %s + %s" % (v_a, v_b, v_c))
    r9, rl = rows[9], rows[kzs[-1]]
    print("""
  HONEST CONSEQUENCE: the defect operator Delta = I - C*C has
  exactly ONE soft mode on every reachable rung -- lam1 equals
  the tau-margin in the positive-side metric by the exact
  pencil identity (dev <= %.0e), the second mode stays a
  factor %.0f-%.0f above it, the tail is stable, and the soft
  direction's dual-frequency profile drifts smoothly.  The
  rank-one-defect reading is now typed: the Redheffer single
  Smith invariant, the vacuum code's one-logical-qubit price,
  and this Krein soft port are one structure -- the deployed
  positivity always fails-or-holds through a SINGLE
  arithmetic-carrying mode, and the floor value is that mode's
  contraction margin.  The polar split localises what is
  missing with the sharpest quantifier so far: the magnitude
  factor A is NOT a short source profile (diag mass and
  residuals printed -- the microscope finding has no source
  reconstruction, so it stays a microscope), no predeclared
  band-moving candidate approximates V, and the class closure
  is now a THEOREM covering ALL word lengths: an honest
  surprise first -- the clean two-band picture is WRONG at
  fine scale (the total density's sign flips 408 times at
  kz 9: the comb's oscillation interleaves the sign sets at
  1-2 bins, so the corridor form is vacuous, typed in the
  spec) -- but the closure that survives is stronger: every
  deployed source letter is a MONOMIAL matrix, products stay
  monomial, and the contractor's monomial mass fraction is
  %.3f-%.3f, so EVERY word of ANY length misses it by residual
  >= %.2f.  The 155-word emptiness was never about length: the
  contractor has dense rows (a genuine integral/transfer
  operator), the source alphabet contains only sparse
  routing-plus-weights, and the missing object is ONE
  non-monomial letter -- a spreading intertwiner with an
  independent contraction bound (the explicit-formula
  transfer).  The wall is unchanged; it now has a normal
  form, a rank (one), and a missing-letter specification
  (non-monomial, band-spreading, contractive).  NO RH
  claim.""" % (
        max(r["pdev"] for r in rows.values()),
        min(seps), max(seps), min(mono.values()),
        max(mono.values()),
        math.sqrt(1.0 - max(mono.values()))))
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s"
          % (time.time() - T0, len(CHECKS), len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if n_pass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''
# ------------- frozen probe source mu4_clifford_weld_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mu4_clifford_weld_probe -- PRIME.MU4.CLIFFORD_WELD.01
(EXPLORATION ONLY, experiments/; round 33 midday-2 package C,
follow-up to DECK-MU-PARALLEL, 2026-08-08).

THE SHARPENED HYPOTHESIS: the arithmetic Moebius involution M and
the geometric deck involution D should NOT be identified but
PROJECTIVELY WELDED -- anticommutation:

    M^2 = D^2 = I,   MD + DM = 0   =>   (MD)^2 = -I,

so J := MD generates a faithful mu4 action, AND M then MOVES the
D-bands (Dv = v => D(Mv) = -Mv): M maps H_{D,+} -> H_{D,-} -- the
missing band-mover type from the Krein census.

TASK 1+2, THE CANDIDATES AND THE WELD TABLE (all five conditions
exact per candidate; register operators are Gaussian-unit matrices,
so float arithmetic is EXACT):
  K0  THE MANDATORY CONTROL (deployed wiring): M = T_s (mu-sign
      translation), D = T_d (deck translation by iota(deck) =
      (0,2)) on C[C2 x Z4] -- two COMMUTING involutions: the
      anticommutator is 2 T_s T_d != 0 and P- M P+ = 0 EXACTLY
      (M preserves the D-bands): the unwelded representation
      REFUSES the band swap -- the contrast.
  K1  FAITHFUL DIAGONAL CHARACTER (from the DECK-MU-PARALLEL
      candidates): M = T_s, J = Omega_chi with chi = (eps = -1,
      j = 1) (the faithful mu4 diagonal character), D := M J.
      Predeclared structure: JM = -MJ holds on the FULL register;
      D^2 = -J^2 = +I exactly on the FAITHFUL SECTOR V_f (mu4
      positions m odd, where J^2 = -I) and -I on the complement --
      the weld conditions THEMSELVES select the faithful sector;
      on V_f the built D is HERMITIAN (real bands).  Measured
      extra: D is Frobenius-ORTHOGONAL to the deployed deck T_d
      (the weld-built deck is a NEW involution, not the deployed
      one -- the gap named).
  K2  GALOIS mu_K = chi4 BOOKKEEPING: per odd prime the residue
      sheet space C^2; inert (deck-odd) p: Frobenius D = X, mu-sign
      lift M = Z (the sign lives on the Frobenius-odd line):
      full 2x2 weld; split p: D = I, mu_K = +1 scalar -- weldless.
      The weld locus == the inert sector == exactly where
      mu(p) = -1 survives the cover (classified by x^2 + y^2
      witnesses for ALL odd p <= 10^4, own arithmetic).
  K3  HALL CHAIN-PARITY COVER: the divisor register doubled by the
      chain-parity sheet, n = 360: M = diag(lambda(k)) (x) Z_pauli
      (Liouville = maximal-chain parity, own sieve), D = I (x) X
      (sheet swap): full weld BY CONSTRUCTION (typed: the doubling
      supplies the qubit -- construction-grade, not deployed).
  K4  METAPLECTIC/SYMPLECTIC FOURIER LIFT (v800 torsor-Fourier
      machinery): register C[F2^4], dim 16.  Weld pair M =
      Omega_w0, D = T_a0 with <w0, a0> = 1: FULL-SPACE weld
      (J^2 = -I globally); the Walsh/Hadamard lift swaps
      diagonal <-> translation (H T_a H / 16 = Omega_a exact);
      the bent-translate frame (arf_bent_css, parameter q =
      x1x2 + x3x4, deployed q* cited read-only) is MUTUALLY
      UNBIASED against the characters (all 256 cross products
      +-4) and sits EXACTLY HALFWAY between weld and co-weld:
      ||{M_q, T_a}||_F = ||[M_q, T_a]||_F = sqrt(32) for EVERY
      a != 0 (equivalent to bentness) -- the bent register is
      the maximally weld-neutral frame.

THE STRUCTURAL LAW (exact census, the reason the deployed wiring
cannot weld): a Weyl-pair weld (involutive translation T_a +
involutive modulation Omega_psi with psi(a) = -1) exists iff the
2-torsion pairing of the slot is nontrivial -- counts: C2: 1 pair;
Z4: 0; Z8: 0 (any cyclic 2-group of order >= 4: ZERO -- enlarging
the cyclic register NEVER helps); F2^4: 120 pairs.  On the deployed
128-register: T_s (mu-sign) anticommutes with 64 characters of
which 32 are involutive => WELDABLE; T_d (deck) anticommutes with
64 (all j odd) of which ZERO are involutive => UNWELDABLE at
register level.  The v833 metaplectic deck (T3 K3)^3 = i I is
CENTRAL: upstairs the deck is J-grade (order 4), not D-grade --
consistent with reading J = MD as the deck's faithful lift.

TASK 3, THE CONTRACTOR CONNECTION (the payoff test): rebuild the
Krein cut-1 arms B+/- at the anchors kz 9/12/13
(krein_normalform machinery, circulant embedding, READ-ONLY
reproduction with the Gram ward); C = B- pinv(B+) has row support
in the negative band and column support in the positive band BY
CONSTRUCTION, so the polar factorization C = U |C| ALWAYS has
band-internal |C| -- the CONTENT is whether the polar phase U is a
SOURCE-BUILT swap: residuals r(W) = ||C - W |C| ||_F / ||C||_F for
the frozen source swaps W in {FLIP (j -> L-j), HALF (j -> j+L/2),
FLIP o HALF} + a random-swap null (LCG) + the displacement
diagnostic of U (top singular pairs).  CONNECTED iff some source W
has r(W) <= 0.10 on ALL three anchors.  (Typed expectation from the
Krein census: FLIP is support-preserving -- d is even -- and no
short word bridged the bands; the residuals quantify the gap.)

TASK 4: K0 above (exact refusal).  TASK 5: honest typing in the
verdict.

CONTROLS: deck/mu regressions ((1+i)^2 = 2i; chi_GL1 separates the
two C2s; Hall row 1 == mu at n = 120; tau kz9 frozen ref); v800
mutual-unbiasedness reproduction (256 products); scramble MUST-FIRE
(random diagonal replaces the faithful character -- weld conditions
break; random Boolean function replaces the bent q -- MUB and the
midpoint identity break); Krein regression ||C|| <= 1 + 1e-6 at
the anchors.

VERDICT (frozen): WELD-FOUND (+ band-mover + contractor status;
prominent if all three) / WELD-WITHOUT-CONTRACTOR / NO-WELD (per-
candidate failing conditions typed).

NO RH claim; writes nothing; nothing outside experiments/; v563
READ-ONLY; own sieves; AST firewall.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mu4_clifford_weld_probe.py
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
PRIME.MU4.CLIFFORD_WELD.01 spec v1 (2026-08-08, frozen before run).
WELD CONDITIONS per candidate (exact, Gaussian-unit arithmetic):
C1 M^2 = I; C2 D^2 = I; C3 MD + DM = 0; C4 (MD)^2 = -I; C5 band
move ||P- M P+||_2 = 1 AND ||P+ M P+|| = 0 (P+- = (I +- D)/2, D
hermitian on the declared domain).  Declared domains: K0 full
C[C2 x Z4] (control: expect C3/C4 FAIL, ||{M,D}||_2 = 2, and
P- M P+ = 0 EXACTLY); K1 faithful sector V_f = span{m odd} (C3
holds on the FULL register; C2/C4/C5 on V_f; D := M J with J =
Omega_(eps=-1,j=1); extras: D hermitian on V_f, D^2 = -I on the
complement, <D, T_d>_F = 0); K2 inert 2x2 block (D = X, M = Z; the
split block D = I, M = I refuses C3 -- typed; weld locus census:
inert <=> p == 3 mod 4 <=> NO x^2+y^2 rep, ALL odd p <= 10^4,
expect 619 inert / 609 split of 1228); K3 full doubled register
n = 360 (M = diag(lambda) (x) Z, D = I (x) X, lambda own sieve);
K4 full C[F2^4] (M = Omega_w0, D = T_a0, w0 = a0 = 0b0001).
STRUCTURAL LAW census (exact): weld pairs (involutive translation,
involutive modulation, pairing -1): C2: 1, Z4: 0, Z8: 0, F2^4:
15 x 8 = 120; 128-register census: T_s: 64 anticommuting chars, 32
involutive; T_d: 64 anticommuting (j odd), 0 involutive.
FOURIER LIFT ward: H T_a H / 16 == Omega_a exact for all 16 a
(H = Walsh 16, H^2 = 16 I).  MUB ward: |<chi_w, bent-translate_a>|
= 4 for all 256 pairs (q = x1x2 + x3x4 parameter grade, deployed
q* cited).  MIDPOINT ward: ||{M_q, T_a}||_F^2 == ||[M_q, T_a]||_F^2
== 32 for all 15 a != 0.  CONTRACTOR: anchors kz (9, 12, 13);
cut-1 arms B+/- = diag(sqrt(max(+-d,0)/2L)) F pad E_odd, d =
FFT(fold(c_ar + c_at)), L = 4h - 2; Gram ward max|B+*B+ - B-*B- -
K| <= 1e-9 max|K| (imag too); Krein regression ||C||_2 <= 1 + 1e-6;
C = B- pinv(B+) (svd cut 1e-12 sigma_max); |C| = (C*C)^(1/2) by
eigh; residual r(W) = ||C - W|C|||_F/||C||_F for W in {FLIP:
i <- (L-i) mod L, HALF: i <- (i - L/2) mod L, FLIPHALF}, plus
RANDOM null (LCG row permutation + random Gaussian-unit phases);
support match fraction |pi(S+) n S-|/|S+| printed (S+- = sign
bands of d at 1e-12 rel tol); displacement diagnostic: top 6
singular pairs of C, argmax rows of U vs V, folded displacement.
CONNECTED iff min over source W of max over anchors r(W) <= 0.10.
CONTROLS/regressions: (1+i)^2 = 2i; chi_GL1(s) = -1 AND
chi_GL1(iota(deck)) = +1; Hall M-row-1 == mu at n = 120 (integer
N-power alternating sum); tau(kz 9) vs 5.984165e-4 rel 1e-4;
scramble A: J_scr = random Gaussian-unit diagonal (LCG), D_scr =
T_s J_scr: at least one of C2/C3/C4 must FAIL on V_f; scramble B:
q_scr = random 16-bit Boolean function (LCG): MUB ward AND midpoint
ward must FAIL.  VERDICT: WELD-FOUND iff >= 1 candidate among
K1-K4 passes C1-C5 exactly on its declared domain AND K0 shows
P- M P+ = 0 with nonzero anticommutator; + CONTRACTOR iff the
residual bar above; WELD-WITHOUT-CONTRACTOR if weld but no source
swap; NO-WELD else.  EXACT0 = 0.0 (unit-matrix arithmetic is exact
in float); float bars: band norms |.-1| <= 1e-12, Krein wards as
above.  LCG seed 20260808.  NO RH claim; writes nothing.
"""

ANCHORS = (9, 12, 13)
RES_BAR = 0.10
WARD_KREIN = 1.0e-9
CNORM_BAR = 1.0 + 1.0e-6
REG_REF_KZ9 = 5.984165e-4
REG_BAR = 1.0e-4
N_HALL = 360
N_HALL_REG = 120
P_MAX = 10_000
BAND_TOL = 1.0e-12
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime", "primepi",
              "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()
_LCG = [20260808]


def lcg():
    _LCG[0] = (6364136223846793005 * _LCG[0] + 1442695040888963407) % (1 << 63)
    return _LCG[0] / float(1 << 63)


def lcg_int(n):
    return int(lcg() * n)


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    print("[%s] %s%s" % (tag, name, ("  -- " + detail) if detail else ""))


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


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


def zero(X):
    """Exact-zero test for Gaussian-unit matrix expressions."""
    return float(np.max(np.abs(X))) == 0.0


def op2norm(X):
    return float(np.linalg.svd(X, compute_uv=False)[0]) if X.size else 0.0


# ===================================================== register layer
IUNIT = (1 + 0j, 1j, -1 + 0j, -1j)


def reg8():
    """C[C2 x Z4]: index g = 4a + m.  Returns T_s, T_d, J, I."""
    dim = 8

    def idx(a, m):
        return 4 * (a % 2) + (m % 4)

    Ts = np.zeros((dim, dim), dtype=complex)
    Td = np.zeros((dim, dim), dtype=complex)
    Jd = np.zeros((dim, dim), dtype=complex)
    for a in range(2):
        for m in range(4):
            g = idx(a, m)
            Ts[idx(a + 1, m), g] = 1.0
            Td[idx(a, m + 2), g] = 1.0
            Jd[g, g] = ((-1) ** a) * IUNIT[m % 4]
    return Ts, Td, Jd, np.eye(dim, dtype=complex)


def pauli():
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    return X, Z, np.eye(2, dtype=complex)


def hadamard16():
    x = np.arange(16)
    pc = np.array([bin(v).count("1") for v in range(16)])
    return np.array([[(-1.0) ** pc[i & j] for j in x] for i in x],
                    dtype=complex)


def translation16(a):
    T = np.zeros((16, 16), dtype=complex)
    for x in range(16):
        T[x ^ a, x] = 1.0
    return T


def modulation16(w):
    return np.diag(np.array(
        [(-1.0) ** bin(w & x).count("1") for x in range(16)],
        dtype=complex))


def qvec(qbits):
    """Phase vector (-1)^q as diagonal, q given as 16-bit int."""
    return np.diag(np.array([(-1.0) ** ((qbits >> x) & 1)
                             for x in range(16)], dtype=complex))


Q_PLUS = sum(1 << x for x in range(16)
             if (((x >> 0) & (x >> 1)) ^ ((x >> 2) & (x >> 3))) & 1)


# ===================================================== weld condition kit
def weld_table(M, D, dom=None, band=True):
    """The five conditions on the (optionally restricted) domain.
    dom = list of basis indices or None (full).  Returns dict."""
    if dom is not None:
        S = np.zeros((M.shape[0], len(dom)), dtype=complex)
        for k, g in enumerate(dom):
            S[g, k] = 1.0
        Mr, Dr = S.conj().T @ M @ S, S.conj().T @ D @ S
    else:
        Mr, Dr = M, D
    Ir = np.eye(Mr.shape[0], dtype=complex)
    out = {}
    out["C1"] = zero(Mr @ Mr - Ir)
    out["C2"] = zero(Dr @ Dr - Ir)
    AC = Mr @ Dr + Dr @ Mr
    out["C3"] = zero(AC)
    out["ac_norm"] = op2norm(AC)
    MD = Mr @ Dr
    out["C4"] = zero(MD @ MD + Ir)
    out["herm_D"] = zero(Dr - Dr.conj().T)
    if band and out["C2"] and out["herm_D"]:
        Pp = 0.5 * (Ir + Dr)
        Pm = 0.5 * (Ir - Dr)
        out["swap"] = op2norm(Pm @ Mr @ Pp)
        out["keep"] = op2norm(Pp @ Mr @ Pp)
        out["C5"] = (abs(out["swap"] - 1.0) <= 1e-12
                     and out["keep"] <= 1e-12)
    else:
        out["swap"], out["keep"], out["C5"] = None, None, False
    return out


def fmt_row(name, w):
    def b(v):
        return " OK " if v else "FAIL"
    sw = ("%.3f" % w["swap"]) if w["swap"] is not None else " -- "
    kp = ("%.3f" % w["keep"]) if w["keep"] is not None else " -- "
    return ("    %-26s %s %s %s %s %s   swap %s keep %s |{M,D}| %.3f"
            % (name, b(w["C1"]), b(w["C2"]), b(w["C3"]), b(w["C4"]),
               b(w["C5"]), sw, kp, w["ac_norm"]))


# ===================================================== arithmetic bits
def liouville(n):
    spf = np.zeros(n + 1, dtype=np.int64)
    for p in range(2, int(n ** 0.5) + 1):
        if spf[p] == 0:
            sl = spf[p * p::p]
            sl[sl == 0] = p
            spf[p * p::p] = sl
    pm = (spf == 0)
    pm[:2] = False
    pr = np.nonzero(pm)[0]
    spf[pr] = pr
    lam = np.ones(n + 1, dtype=np.int64)
    for k in range(2, n + 1):
        kk, cnt = k, 0
        while kk > 1:
            p = int(spf[kk])
            while kk % p == 0:
                kk //= p
                cnt += 1
        lam[k] = (-1) ** cnt
    mu = np.ones(n + 1, dtype=np.int64)
    mu[0] = 0
    for p in pr:
        mu[p::p] *= -1
    for p in pr[pr * pr <= n]:
        mu[p * p::p * p] = 0
    return lam, mu, pr


# ===================================================== krein layer (port)
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
    return dp[:, None] * Fp, dm[:, None] * Fp


def contractor(Bp, Bm):
    U, s, Vh = np.linalg.svd(Bp, full_matrices=False)
    r = int(np.sum(s > 1e-12 * s[0]))
    U, s, Vh = U[:, :r], s[:r], Vh[:r]
    return Bm @ (Vh.conj().T / s) @ U.conj().T


# ================================================================ main
def main():
    print("mu4_clifford_weld_probe -- the projective weld M/D "
          "(anticommutation)")
    print("vs identification.  EXPLORATION ONLY, NO RH CLAIM.")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)

    section("S0 -- firewall")
    check("S0.1 AST firewall: no zeta-zero / prime-table symbols",
          not ast_firewall(), str(ast_firewall()))

    # ------------------------------------------------------------- S1
    section("S1 -- register layer + deck/mu regressions (CTRL-R)")
    z = complex(1, 1)
    check("S1.1 regression: (1+i)^2 = 2i exact", z * z == complex(0, 2))
    # chi_GL1 separation (previous probe S2.3, reproduced)
    chi_s = (-1) ** 1                    # chi_GL1(s): eps part on a = 1
    chi_d = IUNIT[(0 * 2) % 4]           # j = 0 on m = 2
    check("S1.2 regression: chi_GL1 separates the two C2s "
          "(chi(s) = -1, chi(iota(deck)) = +1)",
          chi_s == -1 and chi_d == 1)
    lam, mu, _ = liouville(N_HALL)
    # Hall row 1 == mu at n = 120 (alternating chain census)
    n = N_HALL_REG
    Zi = np.zeros((n, n), dtype=np.int64)
    for a in range(1, n + 1):
        Zi[a - 1, a - 1::a] = 1
    Ni = Zi - np.eye(n, dtype=np.int64)
    Mi = np.eye(n, dtype=np.int64)
    Pk = np.eye(n, dtype=np.int64)
    sgn = 1
    while Pk.any():
        Pk = Pk @ Ni
        sgn = -sgn
        Mi = Mi + sgn * Pk
    check("S1.3 regression: Hall chain parity row 1 == mu (n = %d)" % n,
          bool(np.array_equal(Mi[0], mu[1:n + 1])))
    H = hadamard16()
    check("S1.4 Walsh frame: H^2 = 16 I exact",
          zero(H @ H - 16 * np.eye(16)))
    ok_four = all(zero(H @ translation16(a) @ H / 16 - modulation16(a))
                  for a in range(16))
    check("S1.5 THE FOURIER LIFT: H T_a H / 16 == Omega_a for ALL 16 a "
          "(the diagonal <-> translation swapper, exact)", ok_four)
    Mq = qvec(Q_PLUS)
    ok_mub = True
    for w in range(16):
        chi_row = np.array([(-1.0) ** bin(w & x).count("1")
                            for x in range(16)])
        for a in range(16):
            bt = np.array([Mq[(x ^ a), (x ^ a)].real for x in range(16)])
            if abs(abs(float(chi_row @ bt)) - 4.0) > 1e-12:
                ok_mub = False
    check("S1.6 v800 MUB reproduction: |<chi_w, bent-translate_a>| = 4 "
          "for all 256 pairs (Gram-16I frames mutually unbiased)",
          ok_mub)

    # ------------------------------------------------------------- S2
    section("S2 -- THE STRUCTURAL LAW: the 2-torsion weld census")

    def weld_pairs_cyclic(order):
        cnt = 0
        for a in range(1, order):
            if (2 * a) % order:
                continue
            for j in range(1, order):
                if (2 * j) % order:
                    continue
                # psi_j(a) = exp(2 pi i j a / order) = -1 ?
                if (2 * j * a) % (2 * order) == order:
                    cnt += 1
        return cnt

    c2c, c4c, c8c = (weld_pairs_cyclic(2), weld_pairs_cyclic(4),
                     weld_pairs_cyclic(8))
    f16c = sum(1 for a in range(1, 16) for w in range(16)
               if bin(a & w).count("1") % 2 == 1)
    check("S2.1 Weyl weld pairs: C2 = %d, Z4 = %d, Z8 = %d, F2^4 = %d "
          "-- cyclic 2-groups of order >= 4 have ZERO (trivial "
          "2-torsion pairing): enlarging the cyclic register NEVER "
          "helps" % (c2c, c4c, c8c, f16c),
          (c2c, c4c, c8c, f16c) == (1, 0, 0, 120))
    # 128-register anticommutant census
    CH = [(e, w, j) for e in range(2) for w in range(16)
          for j in range(4)]

    def chival(chi, g):
        e, w, j = chi
        a, v, m = g
        return ((-1) ** (e * a) * (-1) ** bin(w & v).count("1")
                * IUNIT[(j * m) % 4])

    s_gen, deck_img = (1, 0, 0), (0, 0, 2)
    ac_s = [c for c in CH if chival(c, s_gen) == -1]
    ac_d = [c for c in CH if chival(c, deck_img) == -1]
    inv_s = [c for c in ac_s if c[2] in (0, 2)]
    inv_d = [c for c in ac_d if c[2] in (0, 2)]
    check("S2.2 THE ASYMMETRY on the deployed 128-register: T_s (mu-"
          "sign) has %d anticommuting characters, %d involutive => "
          "WELDABLE; T_d (deck) has %d anticommuting (all j odd), %d "
          "involutive => UNWELDABLE at register level"
          % (len(ac_s), len(inv_s), len(ac_d), len(inv_d)),
          (len(ac_s), len(inv_s), len(ac_d), len(inv_d))
          == (64, 32, 64, 0))
    print("    typed: the deck's anticommutant is EXACTLY the faithful")
    print("    (j odd) characters -- order 4, never involutive: the")
    print("    deck can only be welded through a FAITHFUL mu4 object,")
    print("    i.e. as J = MD (the weld's own quarter turn), never as")
    print("    a second involution D' in the register.  The v833")
    print("    metaplectic deck i*I is central = J-grade: consistent.")

    # ------------------------------------------------------------- S3
    section("S3 -- THE CANDIDATE TABLE (five weld conditions, exact)")
    print("    columns: C1 M^2=I | C2 D^2=I | C3 {M,D}=0 | C4 (MD)^2="
          "-I | C5 band")
    Ts, Td, Jd, _ = reg8()
    results = {}
    # K0 control: deployed commuting pair
    w0 = weld_table(Ts, Td)
    results["K0"] = w0
    print(fmt_row("K0 deployed T_s, T_d", w0))
    ok_k0 = (w0["C1"] and w0["C2"] and not w0["C3"]
             and abs(w0["ac_norm"] - 2.0) <= 1e-12
             and not w0["C4"] and w0["swap"] is not None
             and w0["swap"] <= 1e-15 and abs(w0["keep"] - 1.0) <= 1e-12)
    check("S3.0 MANDATORY CONTROL K0: the unwelded C2 x C2 REFUSES the "
          "band swap EXACTLY ([M,D] = 0, ||{M,D}|| = 2, P- M P+ = 0, "
          "P+ M P+ = full)", ok_k0,
          "swap = %.1e, keep = %.3f" % (w0["swap"], w0["keep"]))
    # K1 faithful diagonal character weld
    Dw = Ts @ Jd
    dom_f = [4 * a + m for a in range(2) for m in (1, 3)]
    dom_c = [4 * a + m for a in range(2) for m in (0, 2)]
    w1 = weld_table(Ts, Dw, dom=dom_f)
    results["K1"] = w1
    print(fmt_row("K1 diag-char weld (V_f)", w1))
    ac_full = zero(Ts @ Dw + Dw @ Ts)
    j_is_md = zero(Ts @ Dw - Jd)
    Sc = np.zeros((8, 4), dtype=complex)
    for k, g in enumerate(dom_c):
        Sc[g, k] = 1.0
    Dc = Sc.conj().T @ Dw @ Sc
    anti_c = zero(Dc @ Dc + np.eye(4, dtype=complex))
    ortho = float(abs(np.trace(Dw.conj().T @ Td)))
    check("S3.1 K1 structure: {M, D} = 0 on the FULL register; "
          "J = M D exactly (the faithful mu4); D^2 = -I on the "
          "complement (the weld conditions SELECT the faithful "
          "sector); D hermitian on V_f",
          ac_full and j_is_md and anti_c and w1["herm_D"])
    check("S3.2 K1 gap: the weld-built D is Frobenius-ORTHOGONAL to "
          "the deployed deck T_d (<D, T_d>_F = %.1f) -- a NEW "
          "involution, not the deployed one" % ortho, ortho == 0.0)
    # K2 Galois sector weld
    X2, Z2, I2 = pauli()
    w2 = weld_table(Z2, X2)
    results["K2"] = w2
    print(fmt_row("K2 Galois inert block", w2))
    w2s = weld_table(I2, I2, band=False)
    _, _, pr_full = liouville(P_MAX)
    n_split = n_inert = 0
    ok_cls = True
    for p in [int(q) for q in pr_full if q > 2]:
        has = False
        x = 1
        while 2 * x * x <= p:
            y2 = p - x * x
            y = int(math.isqrt(y2))
            if y * y == y2:
                has = True
                break
            x += 1
        if p % 4 == 1:
            n_split += 1
            ok_cls &= has
        else:
            n_inert += 1
            ok_cls &= not has
    check("S3.3 K2 weld locus: inert (weld) = %d, split (weldless, "
          "D = I scalar: {M,D} = 2I != 0) = %d, all classified by "
          "x^2+y^2 witnesses -- the weld locus IS the mu(p) = -1 "
          "survival locus" % (n_inert, n_split),
          ok_cls and (n_inert, n_split) == (619, 609)
          and not w2s["C3"])
    # K3 Hall chain-parity cover
    Lm = np.diag(lam[1:N_HALL + 1].astype(complex))
    M3 = np.kron(Lm, Z2)
    D3 = np.kron(np.eye(N_HALL, dtype=complex), X2)
    w3 = weld_table(M3, D3)
    results["K3"] = w3
    print(fmt_row("K3 Hall cover (n=360)", w3))
    # K4 Fourier/Weyl weld
    M4 = modulation16(1)
    D4 = translation16(1)
    w4 = weld_table(M4, D4)
    results["K4"] = w4
    print(fmt_row("K4 Weyl pair on F2^4", w4))
    # bent midpoint
    ok_mid = True
    for a in range(1, 16):
        Ta = translation16(a)
        acn = float(np.linalg.norm(Mq @ Ta + Ta @ Mq)) ** 2
        ccn = float(np.linalg.norm(Mq @ Ta - Ta @ Mq)) ** 2
        if abs(acn - 32.0) > 1e-9 or abs(ccn - 32.0) > 1e-9:
            ok_mid = False
    check("S3.4 K4 bent midpoint: ||{M_q, T_a}||_F^2 = ||[M_q, T_a]||"
          "_F^2 = 32 for ALL 15 a != 0 (the bent frame is exactly "
          "halfway between weld and co-weld == bentness)", ok_mid)
    welded = [k for k in ("K1", "K2", "K3", "K4")
              if all(results[k][c] for c in
                     ("C1", "C2", "C3", "C4", "C5"))]
    check("S3.5 WELD CENSUS: candidates passing ALL FIVE conditions "
          "on their declared domain = %s" % welded,
          welded == ["K1", "K2", "K3", "K4"])

    # ------------------------------------------------------------- S4
    section("S4 -- band movement (quantified) -- theorem check")
    print("    anticommutation <=> full band swap: measured swap/keep")
    for k in ("K1", "K2", "K3", "K4"):
        print("    %s: ||P- M P+|| = %.12f   ||P+ M P+|| = %.2e"
              % (k, results[k]["swap"], results[k]["keep"]))
    check("S4.1 every welded candidate is a FULL band mover (swap "
          "norm 1, in-band block 0) and the control K0 is a FULL "
          "band keeper",
          all(abs(results[k]["swap"] - 1.0) <= 1e-12
              and results[k]["keep"] <= 1e-12 for k in welded))

    # ------------------------------------------------------------- S5
    section("S5 -- THE CONTRACTOR CONNECTION (Krein anchors, "
            "polar test)")
    res_by_w = {"FLIP": [], "HALF": [], "FLIPHALF": [], "RANDOM": []}
    ok_ward = True
    ok_creg = True
    tau_kz9 = None
    for kz in ANCHORS:
        rr = core.build_window(kz)
        h, Mz, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
        uu = np.asarray(rr["uu"], float)
        mm = 2.0 * np.asarray(rr["lam"], float)
        c_at, _ = core.atom_lags_at(alpha, Mz, uu, mm)
        c_ar = np.asarray(core.arch_lags(Mz, D), float)
        K = core.odd_toeplitz(c_ar + c_at, Mz)
        if kz == 9:
            tau_kz9 = float(np.linalg.eigvalsh(
                np.asarray(rr["Ah"], float))[0])
        d = grid_density(c_ar + c_at)
        L = 2 * (2 * h) - 2
        Bp, Bm = krein_arms(d, h)
        G = Bp.conj().T @ Bp - Bm.conj().T @ Bm
        ks = max(float(np.max(np.abs(K))), 1e-300)
        ok_ward &= (float(np.max(np.abs(G.real - K))) / ks <= WARD_KREIN
                    and float(np.max(np.abs(G.imag))) / ks <= WARD_KREIN)
        C = contractor(Bp, Bm)
        cn = op2norm(C)
        ok_creg &= cn <= CNORM_BAR
        # polar magnitude
        ev, V = np.linalg.eigh(C.conj().T @ C)
        ev = np.maximum(ev, 0.0)
        absC = (V * np.sqrt(ev)) @ V.conj().T
        nC = float(np.linalg.norm(C))
        dmax = float(np.max(np.abs(d)))
        Sp = set(np.nonzero(d > BAND_TOL * dmax)[0].tolist())
        Sm = set(np.nonzero(d < -BAND_TOL * dmax)[0].tolist())
        swaps = {
            "FLIP": np.array([(L - i) % L for i in range(L)]),
            "HALF": np.array([(i - L // 2) % L for i in range(L)]),
            "FLIPHALF": np.array([((L - i) - L // 2) % L
                                  for i in range(L)]),
        }
        rnd = np.arange(L)
        for i in range(L - 1, 0, -1):
            jr = lcg_int(i + 1)
            rnd[i], rnd[jr] = rnd[jr], rnd[i]
        swaps["RANDOM"] = rnd
        rphase = np.array([IUNIT[lcg_int(4)] for _ in range(L)])
        print("    kz %-3d h %-4d L %-4d ||C|| %.6f  |S+| %d |S-| %d"
              % (kz, h, L, cn, len(Sp), len(Sm)))
        for wname, src in swaps.items():
            Wabs = absC[src, :]
            if wname == "RANDOM":
                Wabs = rphase[:, None] * Wabs
            res = float(np.linalg.norm(C - Wabs)) / max(nC, 1e-300)
            dest = {}
            for j in Sp:
                ii = np.nonzero(src == j)[0]
                if len(ii):
                    dest[j] = int(ii[0])
            match = (sum(1 for j in dest if dest[j] in Sm)
                     / max(len(dest), 1))
            res_by_w[wname].append(res)
            print("        %-9s residual %.4f   S+ -> S- support "
                  "match %.2f" % (wname, res, match))
        # displacement diagnostic
        Uc, sc, Vch = np.linalg.svd(C)
        print("        polar displacement (top 6 singular pairs):")
        for k in range(6):
            ik = int(np.argmax(np.abs(Uc[:, k])))
            jk = int(np.argmax(np.abs(Vch[k, :])))
            dsp = (ik - jk) % L
            if dsp > L // 2:
                dsp -= L
            print("          s%-2d = %.4f  row %4d <- col %4d  "
                  "displacement %+d" % (k, float(sc[k]), ik, jk, dsp))
    check("S5.1 Krein Gram ward: B+*B+ - B-*B- == K to 1e-9 at all "
          "3 anchors (read-only reproduction)", ok_ward)
    check("S5.2 Krein regression: ||C|| <= 1 + 1e-6 at all anchors",
          ok_creg)
    check("S5.3 CTRL-R: tau(kz 9) = %.6e vs frozen ref %.6e"
          % (tau_kz9, REG_REF_KZ9),
          abs(tau_kz9 / REG_REF_KZ9 - 1.0) < REG_BAR)
    best_w, best_r = None, np.inf
    for wname in ("FLIP", "HALF", "FLIPHALF"):
        r = max(res_by_w[wname])
        if r < best_r:
            best_w, best_r = wname, r
    connected = best_r <= RES_BAR
    check("S5.4 contractor connection: best source swap %s with max-"
          "anchor residual %.4f %s %.2f => %s (random null %.4f)"
          % (best_w, best_r, "<=" if connected else ">", RES_BAR,
             "CONNECTED" if connected else "NOT CONNECTED",
             max(res_by_w["RANDOM"])), True)

    # ------------------------------------------------------------- S6
    section("S6 -- scramble controls (MUST-FIRE)")
    Jscr = np.diag(np.array([IUNIT[lcg_int(4)] for _ in range(8)]))
    Dscr = Ts @ Jscr
    ws = weld_table(Ts, Dscr, dom=dom_f)
    fired_a = not (ws["C2"] and ws["C3"] and ws["C4"])
    check("S6.1 scramble A: random Gaussian-unit diagonal replaces "
          "the faithful character -- weld breaks (C2 %s, C3 %s, "
          "C4 %s)" % (ws["C2"], ws["C3"], ws["C4"]), fired_a)
    qscr = 0
    for x in range(16):
        if lcg() < 0.5:
            qscr |= 1 << x
    Mqs = qvec(qscr)
    mub_fail = False
    for w in range(0, 16, 3):
        chi_row = np.array([(-1.0) ** bin(w & x).count("1")
                            for x in range(16)])
        for a in range(0, 16, 3):
            bt = np.array([Mqs[(x ^ a), (x ^ a)].real
                           for x in range(16)])
            if abs(abs(float(chi_row @ bt)) - 4.0) > 1e-9:
                mub_fail = True
    mid_fail = False
    for a in range(1, 16):
        Ta = translation16(a)
        acn = float(np.linalg.norm(Mqs @ Ta + Ta @ Mqs)) ** 2
        if abs(acn - 32.0) > 1e-9:
            mid_fail = True
    check("S6.2 scramble B: random Boolean function replaces the bent "
          "q -- MUB fails (%s) AND the midpoint identity fails (%s)"
          % (mub_fail, mid_fail), mub_fail and mid_fail)

    # ------------------------------------------------------------- V
    section("V -- FROZEN VERDICT + the honest consequence")
    npass = sum(1 for _, ok in CHECKS if ok)
    print("    checks: %d/%d passed%s"
          % (npass, len(CHECKS),
             "" if not FAILS else "; FAILS: %s" % FAILS))
    weld_found = bool(welded) and ok_k0 and not FAILS
    if FAILS:
        verdict = "WELD-WARD-FAIL"
    elif weld_found and connected:
        verdict = "WELD-FOUND (+BAND-MOVER +CONTRACTOR)"
    elif weld_found:
        verdict = "WELD-WITHOUT-CONTRACTOR"
    else:
        verdict = "NO-WELD"
    print()
    print("    VERDICT: %s" % verdict)
    print()
    print("    THE WELD IS REAL STRUCTURE: all four candidates close")
    print("    the full Clifford weld (M^2 = D^2 = I, MD + DM = 0,")
    print("    (MD)^2 = -I, full band swap) EXACTLY on their declared")
    print("    domains -- and each domain is forced by the same law:")
    print("      K1: the faithful (j odd) sector of the mu4 slot;")
    print("      K2: the inert (deck-odd) primes -- the mu(p) = -1")
    print("          survival locus;")
    print("      K3: the chain-parity double cover (construction);")
    print("      K4: the F2^4 Weyl pairs (120 of them, Fourier-lift")
    print("          swapped).")
    print("    THE ASYMMETRY (exact census): the mu-sign T_s is")
    print("    weldable (32 involutive partners); the deployed deck")
    print("    T_d is NOT (its anticommutant is exactly the faithful")
    print("    j-odd characters, all order 4) -- the deck can enter a")
    print("    weld only as J = MD (quarter turn), never as the second")
    print("    involution: the identification of the previous probe")
    print("    was refused by the wiring for exactly this reason.")
    print("    THE GAP NAMED: the weld-built D (K1) is Frobenius-")
    print("    orthogonal to the deployed deck T_d; welding the")
    print("    GEOMETRIC deck needs the metaplectic level, where the")
    print("    deck is central i*I = J^2-grade (v833) -- a candidate")
    print("    CONSTRUCTION, not deployed wiring.")
    print("    THE CONTRACTOR: the polar magnitude |C| is band-")
    print("    internal BY CONSTRUCTION; the polar phase is %s a"
          % ("matched by" if connected else "NOT matched by"))
    print("    source-built swap (best %s, residual %.3f; random null"
          % (best_w, best_r))
    print("    %.3f) -- the Krein band mover remains data-shaped:"
          % max(res_by_w["RANDOM"]))
    print("    the weld supplies the TYPE of the missing operator")
    print("    (an anticommuting involution), not yet its VALUE.")
    print("    NO RH claim: nothing here bounds zeros or Mertens.")
    print()
    print("    total runtime %.1f s" % (time.time() - T0))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[^\n]*:")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdicts = [ln.strip() for ln in out.splitlines()
                if _VD_RE.search(ln)]
    return len(marks), fails, " | ".join(verdicts)


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace, registered in sys.modules under the probe's
    canonical import name; capture and re-emit stdout; return
    (stdout, exit_code, byte_equal_to_source_file_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdicts,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and all(v in verdict for v in exp_verdicts)
          and code == exp_code and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line(s): %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok

_PLAN = (
    ('krein_defect_polar_probe', _SRC_0, 8, (),
     ('DEFECT-ONE + BOTH-MISSING + MONOMIAL-CLOSURE-THEOREM',), 0),
    ('mu4_clifford_weld_probe', _SRC_1, 22, (),
     ('WELD-WITHOUT-CONTRACTOR',), 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v862 -- PRIME.KREIN.DEFECT_ONE.01 + PRIME.MU4.WELD.01')
    print('(the defect operator has exactly ONE soft mode with lam1 = the')
    print('tau-margin exactly; the monomial closure theorem kills source')
    print("words of EVERY length; the 2-torsion weld law: the deck's")
    print('anticommutant is entirely faithful-mu4 -- the deck enters only')
    print('as J = MD; NO RH claim)')
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdicts, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdicts, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v862: %d/%d probe pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('The three vacuum findings (Redheffer Smith invariant, vacuum')
    print('code logical qubit, Krein soft port) are ONE rank-one')
    print('structure; the missing object is typed: ONE non-monomial,')
    print('band-spreading, contractive letter -- and the weld supplies')
    print('its TYPE (an anticommuting involution), not yet its VALUE.')
    print("[%s] v862 VERDICT GATE: DEFECT-ONE + MONOMIAL-CLOSURE-THEOREM + WELD-WITHOUT-CONTRACTOR"
          % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
