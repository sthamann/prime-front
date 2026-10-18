#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""arbiter_assembly_precision_probe -- PRIME.COFINAL.ARBITERHP.01

CCCXXXV.  FROZEN SPEC v1 (2026-08-13).

EXPLORATION ONLY.  This probe writes no files.  It changes no verification
module, paper, ledger, website, manifest, or status marker.  It makes no RH
claim, no counterexample claim, and no all-h claim.

MISSION.  Attack the float64 assembly below the direct Weil-kernel arbiter.
The chain-route defect found by CCCXXIII is not under test here.  The three
predeclared cells are

    A  (h, kz) = (9447, 196),   former case-D cell;
    B  (h, kz) = (10513, 341),  the named deep decider;
    C  (h, kz) = (11504, 528),  one blind-ladder straddle cell.

The probe rebuilds every input at MP_DPS = 70 decimal digits:

* an independent Eratosthenes prime-power comb, retaining the prime base so
  that Lambda(p^j) = log p is recomputed with mpmath;
* alpha, the adjacent prime-power gap, M and D from that comb;
* every compactly supported atom/tent read;
* every archimedean lag from the analytically integrated Lerch series

      L(t) = sum_{k>=0} exp(-(2k+1/2)t)/(2k+1/2)^2,

  with L(0) = (pi^2 + 8 Catalan)/4 and a geometric omitted-tail bound;
* the complete lag profile, the second-difference sequence G, and hence

      Omega[m,n] = (G[m+n] + G[|m-n|])/2.

The deployed comparator is the actual float64 core.arch_lags +
core.atom_lags_at assembly.  For every cell the probe computes an entrywise
assembly-error certificate and an induced infinity-norm/Weyl bound without
sampling matrix entries.  The two bottom eigenpairs are then measured from
the dense float64 matrices assembled from (i) deployed G and (ii) the
70-digit G rounded once to float64.  The latter is a high-precision-input
assembly measurement, not an arbitrary-precision eigensolve.  Its sign is
called CERTIFIED only if the one-round cast Weyl bound is below lam_min.

HALF-WIDTH ADVERSARY.  The deployed decisive E3 enclosure prices product
rounding and the coefficient transform, whose half-width is

    max(a-priori transform model, 8 * measured deviation).

It prices no error in the lag/assembly input.  On each high-precision-input
bottom eigenvector, INJECT_N = 128 deterministic sandbox trials inject one
lag-entry perturbation of exactly the measured max |c64-c70| scale, at
high-sensitivity coefficients and with alternating sign.  The unperturbed
70-digit contraction is truth.  Coverage means truth lies inside the
unchanged deployed E3 enclosure around the perturbed read.  No perturbation
larger than the measured assembly discrepancy is used.

FAITHFULNESS / NORMALIZATION WARD.  On cells A and B, fresh sparse basis-pair
code checks the identification in three independently written coordinates:

    (1) the direct Omega[m,n] entry;
    (2) (1/2) sum_r phi_r c_r;
    (3) (1/2) sum_r phi_r A_r
        - (1/4) sum_{p^j} mu_{p^j} phi~(log p^j).

The test set includes m or n equal to 0, adjacent modes, middle modes and the
top mode h-1.  This explicitly exercises the outer 1/2, the atom -1/2, the
folded measure normalization and the sign convention.  It is a two-cell
normalization check, not an exhaustion theorem.

NON-VACUITY.  A sandbox copy of each lag profile is doctored at M//3 by a
relative PLANT_REL = 1e-6 before G is assembled.  The entrywise certificate
must detect every planted bug outside the clean certified entry enclosure.
The deployed arrays are never mutated.

AMENDMENT A1 (implementation-only, after the first attempted frozen run).
The setup passed 2/2, then this installed mpmath version rejected the spelling
``mp.zero`` before the first numerical cell was built.  Every occurrence was
replaced by the version-portable ``mp.mpf("0")``.  No formula, bar, target,
trial, tolerance, verdict rule, or measured value changed.

AMENDMENT A2 (control semantics, after the first completed frozen run).
All three planted bugs were detected at 81.5, 54.4 and 46.1 times the clean
certified entry bound, but the first draft called the control silent because
it additionally demanded an arbitrary factor 100.  Detection by a certified
enclosure means factor > 1, so PLANT_FACTOR is corrected from 100 to 1.  The
plant, clean bounds, measurements and scientific gates are unchanged.

AMENDMENT A3 (reporting-only, after the first green 8/8 run).
The typed ledger correctly printed A_ASSEMBLY = PREMISE-HIDDEN, but the final
one-line aggregate printed CLEAN because its boolean omitted the ``uncert``
list.  The aggregate now includes that already-printed list and says
NON-CLEAN.  No numerical value, gate, row type or severity changed.

FROZEN BARS.
    MP_DPS = 70; LERCH_TAIL = 1e-62; MP_PAD = 1e-54;
    INJECT_N = 128 per cell; COEF_SAFE = 8; COEF_PROBE = 24;
    ID_ABS = 1e-52; PLANT_REL = 1e-6; PLANT_FACTOR = 1;
    expected cells exactly as listed above; runtime bar 1800 s.

VERDICT TYPES.
    BUG-CONFIRMED  a positive high-precision-input sign flips, a current
                   half-width misses truth, or the normalization identity
                   fails;
    PREMISE-HIDDEN numerical sign survives but its rigorous Weyl interval
                   still straddles zero;
    CLEAN          the high-precision-input sign survives and the Weyl
                   interval excludes zero, all coverage trials contain
                   truth, both normalization cells pass, and the planted
                   bug is detected.

The typed defect ledger is printed in section V.  No result from this
experiment is load-bearing.
"""

from __future__ import annotations

import ast
import hashlib
import math
import os
import sys
import time

import mpmath as mp
import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY comparator)


MP_DPS = 70
LERCH_TAIL = mp.mpf("1e-62")
MP_PAD = mp.mpf("1e-54")
INJECT_N = 128
COEF_SAFE = 8.0
COEF_PROBE = 24
ID_ABS = mp.mpf("1e-52")
PLANT_REL = 1.0e-6
PLANT_FACTOR = 1.0
RUNTIME_BAR = 1800.0
NU_MAIN = 4
FRAME_EPS = mp.mpf("1e-9")
CELLS = (
    ("A9447", 9447, 196),
    ("B10513", 10513, 341),
    ("C11504", 11504, 528),
)
ID_CELLS = frozenset(("A9447", "B10513"))
EXPECTED_X_MAX = 12_369_289
EXPECTED_CELL_N = {"A9447": 1021, "B10513": 2063, "C11504": 3517}
BANNED = ("zetazero", "zetazeros", "nzeros", "primerange", "isprime",
          "primepi", "nextprime", "prevprime", "factorint",
          "primefactors")

CHECKS: list[tuple[str, bool]] = []
KILLS: list[str] = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()


def check(name, ok, detail="", kill=None):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return ok


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED:
            bad.append(name)
    return sorted(set(bad))


def prime_power_table(nmax):
    """Independent sieve; return sorted (p^j, p) integer arrays."""
    sieve = np.ones(nmax + 1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(math.isqrt(nmax)) + 1):
        if sieve[p]:
            sieve[p * p::p] = False
    ns = []
    bases = []
    for p in np.nonzero(sieve)[0]:
        p = int(p)
        q = p
        while q <= nmax:
            ns.append(q)
            bases.append(p)
            q *= p
    nn = np.asarray(ns, dtype=np.int64)
    pp = np.asarray(bases, dtype=np.int64)
    order = np.argsort(nn, kind="stable")
    return nn[order], pp[order]


def frame_from_integers(tag, h_expected, kz, nn):
    alpha = mp.log(int(nn[kz]))
    gap = mp.log(int(nn[kz + 1])) - alpha
    d_k = gap / (2 * NU_MAIN)
    M = int(mp.ceil(alpha / d_k - FRAME_EPS)) + 1
    if M % 2:
        M += 1
    h = M // 2
    D = 2 * alpha / M
    return dict(tag=tag, h=h, h_expected=h_expected, kz=kz, M=M,
                D=D, alpha=alpha, gap=gap, n=int(nn[kz]),
                X=int(nn[kz]) ** 2)


def lerch_value(t):
    """L(t) midpoint plus rigorous geometric omitted-tail bound."""
    if t == 0:
        return (mp.mpf("0.25")
                * (mp.pi ** 2 + 8 * mp.catalan), mp.mpf("0"))
    q = mp.exp(-2 * t)
    ek = mp.exp(-t / 2)
    one_minus_q = -mp.expm1(-2 * t)
    total = mp.mpf("0")
    k = 0
    while True:
        lam = 2 * k + mp.mpf("0.5")
        total += ek / (lam * lam)
        k += 1
        ek *= q
        lam_next = 2 * k + mp.mpf("0.5")
        tail = ek / (lam_next * lam_next * one_minus_q)
        if tail <= LERCH_TAIL:
            return total, tail


def arch_lags_mp(M, D):
    """Analytically integrated archimedean lags with tail brackets."""
    lv = [mp.mpf("0")] * (M + 1)
    tw = [mp.mpf("0")] * (M + 1)
    for j in range(M + 1):
        lv[j], tw[j] = lerch_value(j * D)
    arch_const = (mp.euler + mp.log(mp.pi) + 3 * mp.log(2)
                  + mp.pi / 2)
    out = [mp.mpf("0")] * M
    err = [mp.mpf("0")] * M
    out[0] = -arch_const + (2 * lv[0] - 2 * lv[1]) / D
    err[0] = 2 * tw[1] / D + MP_PAD * (1 + abs(out[0]))
    for j in range(1, M):
        out[j] = (2 * lv[j] - lv[j - 1] - lv[j + 1]) / D
        err[j] = ((2 * tw[j] + tw[j - 1] + tw[j + 1]) / D
                  + MP_PAD * (1 + abs(out[j])))
    return out, err


def atom_lags_mp(frame, nn, pp):
    """Fresh high-precision prime-power tent reads."""
    M, D, X = frame["M"], frame["D"], frame["X"]
    stop = int(np.searchsorted(nn, X, side="right"))
    out = [mp.mpf("0")] * M
    for n, p in zip(nn[:stop], pp[:stop]):
        u = mp.log(int(n))
        mass = 2 * mp.log(int(p)) / mp.sqrt(int(n))
        i0 = int(mp.floor(u / D))
        for i in (i0, i0 + 1):
            if 0 <= i < M:
                value = 1 - abs(i * D - u) / D
                if value > 0:
                    out[i] -= mass * value / 2
        if u < D:
            raise AssertionError("unexpected reflected atom")
    return out, stop


def gseq_mp(lag, lag_err):
    M = len(lag)
    ext = lag + [lag[M - 2]]
    eext = lag_err + [lag_err[M - 2]]
    g = [mp.mpf("0")] * M
    ge = [mp.mpf("0")] * M
    for r in range(M):
        g[r] = ext[r] - (ext[r + 1] + ext[abs(r - 1)]) / 2
        ge[r] = (eext[r] + (eext[r + 1] + eext[abs(r - 1)]) / 2
                 + MP_PAD * (1 + abs(g[r])))
    return g, ge


def gseq_float(lag):
    M = len(lag)
    ext = np.concatenate([lag, [lag[M - 2]]])
    rr = np.arange(M)
    return ext[rr] - 0.5 * (ext[rr + 1] + ext[np.abs(rr - 1)])


def omega_rows(g, h, out):
    for m in range(h):
        row = out[m]
        np.add(g[m:m + h], 0.0, out=row)
        row[:m + 1] += g[m::-1]
        if m + 1 < h:
            row[m + 1:] += g[1:h - m]
        row *= 0.5
    return out


def bottom_eigenpair(g, h):
    omega = np.empty((h, h), dtype=float)
    omega_rows(g, h, omega)
    values, vectors = sla.eigh(
        omega, subset_by_index=[0, 0], overwrite_a=True,
        check_finite=False, driver="evr")
    value = float(values[0])
    vector = np.ascontiguousarray(vectors[:, 0])
    vector /= float(np.linalg.norm(vector))
    del omega, vectors
    return value, vector


def outward_float(value):
    return float(np.nextafter(float(value), math.inf))


def assembly_error_certificate(g64, gmp, gerr, h):
    """Exact structured max-entry and infinity-norm bounds."""
    signed = np.empty(len(g64))
    bound = np.empty(len(g64))
    for r, (fv, mv, ew) in enumerate(zip(g64, gmp, gerr)):
        delta = mp.mpf(float(fv)) - mv
        signed[r] = float(delta)
        bound[r] = outward_float(abs(delta) + ew)
    idx = np.arange(h)
    max_seen = 0.0
    max_bound = 0.0
    max_rowsum = 0.0
    for lo in range(0, h, 64):
        ii = np.arange(lo, min(h, lo + 64))[:, None]
        jj = idx[None, :]
        seen = 0.5 * (signed[ii + jj] + signed[np.abs(ii - jj)])
        bnd = 0.5 * (bound[ii + jj] + bound[np.abs(ii - jj)])
        max_seen = max(max_seen, float(np.max(np.abs(seen))))
        max_bound = max(max_bound, float(np.max(bnd)))
        max_rowsum = max(max_rowsum, float(np.max(np.sum(bnd, axis=1))))
    return dict(max_seen=max_seen, max_bound=max_bound,
                row_bound=np.nextafter(max_rowsum, math.inf),
                g_bound=bound)


def node_frame(lag):
    M = len(lag)
    L = 2 * M - 2
    ext = np.concatenate([lag, lag[-2:0:-1]])
    density = np.fft.fft(ext).real[:M]
    theta = math.pi * np.arange(M) / (M - 1)
    eps = np.full(M, 2.0)
    eps[[0, M - 1]] = 1.0
    wsig = (eps * density * 4.0 * np.sin(theta / 2.0) ** 2
            / (2.0 * L))
    return theta, wsig, L


def node_values(avec, M, L):
    padded = np.zeros(L)
    padded[:len(avec)] = avec
    return np.fft.fft(padded).real[:M]


def cheb_coeffs(avec, M, L):
    nf = 4 * L
    padded = np.zeros(nf)
    padded[:len(avec)] = avec
    qv = np.fft.fft(padded).real
    theta = 2.0 * math.pi * np.arange(nf) / nf
    phi_nodes = 4.0 * np.sin(theta / 2.0) ** 2 * qv * qv
    raw = np.fft.fft(phi_nodes).real / nf
    phi = np.concatenate([[raw[0]], 2.0 * raw[1:M]])
    return phi, phi_nodes, theta


def coefficient_deviation(nodes, theta, indices, reference):
    nf = len(nodes)
    worst = 0.0
    for r in indices:
        exact = 2.0 * math.fsum(
            (nodes * np.cos(r * theta)).tolist()) / nf
        worst = max(worst, abs(exact - reference[r]))
    return worst


def fsum_dot(a, b):
    products = np.asarray(a, float) * np.asarray(b, float)
    value = math.fsum(products.tolist())
    width = (0.5 * np.finfo(float).eps
             * math.fsum(np.abs(products).tolist()))
    return value, width


def e3_price(avec, lag, seed):
    M = len(lag)
    _theta, _wsig, L = node_frame(lag)
    phi, phi_nodes, theta = cheb_coeffs(avec, M, L)
    rng = np.random.default_rng(seed)
    sample = sorted(set(int(x) for x in rng.choice(
        M, size=min(COEF_PROBE, M), replace=False)))
    measured = coefficient_deviation(
        phi_nodes, theta, sample, phi)
    apriori = (8.0 * math.log2(max(4, len(theta)))
               * 0.5 * np.finfo(float).eps
               * math.fsum(np.abs(phi_nodes).tolist()) / len(theta))
    phi_dev = max(apriori, COEF_SAFE * measured)
    value, width = fsum_dot(phi, lag)
    width = 0.5 * (width + phi_dev
                   * math.fsum(np.abs(lag).tolist()))
    return 0.5 * value, width, phi, phi_dev, measured, apriori


def tau_scale(lag, eigenvalue, vector):
    _theta, wsig, L = node_frame(lag)
    qv = node_values(vector, len(lag), L)
    pos = wsig > 0.0
    dplus = math.fsum((wsig[pos] * qv[pos] ** 2).tolist())
    return eigenvalue / dplus, dplus


def injection_coverage(frame, lag64, lag70, vector, clean_truth):
    q0, halfwidth, phi, phi_dev, measured, apriori = e3_price(
        vector, lag64, 20260813 + frame["kz"])
    discrepancy = float(np.max(np.abs(lag64 - lag70)))
    sensitivity = np.argsort(np.abs(phi))[::-1]
    candidates = sensitivity[:max(INJECT_N, 256)]
    covered = 0
    misses = []
    for trial in range(INJECT_N):
        r = int(candidates[(37 * trial + 11) % len(candidates)])
        sign = -1.0 if trial % 2 else 1.0
        injected = q0 + 0.5 * phi[r] * sign * discrepancy
        ok = abs(clean_truth - injected) <= halfwidth
        covered += int(ok)
        if not ok and len(misses) < 3:
            misses.append((trial, r, clean_truth - injected,
                           halfwidth))
    return dict(covered=covered, total=INJECT_N,
                discrepancy=discrepancy, halfwidth=halfwidth,
                phi_dev=phi_dev, measured=measured, apriori=apriori,
                misses=misses, q0=q0)


def phi_basis_pair(m, n):
    """Cosine coefficients of 4 sin^2(theta/2) T_m T_n."""
    out = {}
    for k in (m + n, abs(m - n)):
        out[k] = out.get(k, mp.mpf("0")) + 1
        out[k + 1] = out.get(k + 1, mp.mpf("0")) - mp.mpf("0.5")
        out[abs(k - 1)] = (out.get(abs(k - 1), mp.mpf("0"))
                           - mp.mpf("0.5"))
    return {r: v for r, v in out.items() if v != 0}


def basis_identity(frame, arch, atom, lag, g, nn, pp):
    h, D, X = frame["h"], frame["D"], frame["X"]
    pairs = ((0, 0), (0, 1), (1, 1), (2, 7),
             (h // 3, h // 3 + 1), (h // 2, h // 2),
             (h - 2, h - 1), (h - 1, h - 1))
    stop = int(np.searchsorted(nn, X, side="right"))
    worst_lag = mp.mpf("0")
    worst_split = mp.mpf("0")
    factor_control = mp.mpf("0")
    sign_control = mp.mpf("0")
    for m, n in pairs:
        phi = phi_basis_pair(m, n)
        direct = (g[m + n] + g[abs(m - n)]) / 2
        from_lag = mp.fsum(phi[r] * lag[r] for r in phi) / 2
        arch_read = mp.fsum(phi[r] * arch[r] for r in phi) / 2
        prime_read = mp.mpf("0")
        for atom_n, atom_p in zip(nn[:stop], pp[:stop]):
            u = mp.log(int(atom_n))
            mass = 2 * mp.log(int(atom_p)) / mp.sqrt(int(atom_n))
            i0 = int(mp.floor(u / D))
            frac = u / D - i0
            p0 = phi.get(i0, mp.mpf("0"))
            p1 = phi.get(i0 + 1, mp.mpf("0"))
            prime_read -= mass * ((1 - frac) * p0 + frac * p1) / 4
        split = arch_read + prime_read
        worst_lag = max(worst_lag, abs(direct - from_lag))
        worst_split = max(worst_split, abs(direct - split))
        factor_control = max(factor_control, abs(direct - 2 * from_lag))
        sign_control = max(
            sign_control, abs(direct - (arch_read - prime_read)))
    return dict(n_pairs=len(pairs), lag=worst_lag, split=worst_split,
                factor_control=factor_control, sign_control=sign_control)


def planted_bug(frame, lag64, clean_cert, gmp):
    bug = lag64.copy()
    bug[len(bug) // 3] *= 1.0 + PLANT_REL
    gbug = gseq_float(bug)
    gtrue = np.asarray([float(v) for v in gmp])
    delta = gbug - gtrue
    h = frame["h"]
    idx = np.arange(h)
    max_entry = 0.0
    for lo in range(0, h, 64):
        ii = np.arange(lo, min(h, lo + 64))[:, None]
        jj = idx[None, :]
        block = 0.5 * (delta[ii + jj] + delta[np.abs(ii - jj)])
        max_entry = max(max_entry, float(np.max(np.abs(block))))
    ratio = max_entry / max(clean_cert["max_bound"], 1e-300)
    return max_entry, ratio


def float_comparator(frame, nn):
    nmax = frame["X"]
    lam = core.von_mangoldt_table(nmax)
    atoms = np.nonzero(lam > 0.0)[0]
    alpha = float(np.log(float(frame["n"])))
    D = 2.0 * alpha / frame["M"]
    stop = int(np.searchsorted(atoms, nmax, side="right"))
    use = atoms[:stop]
    positions = np.log(use.astype(float))
    masses = 2.0 * lam[use] / np.sqrt(use.astype(float))
    arch = np.asarray(core.arch_lags(frame["M"], D), float)
    atom = np.asarray(core.atom_lags_at(
        alpha, frame["M"], positions, masses)[0], float)
    return arch + atom


def run_cell(frame, nn, pp):
    tag, h, M = frame["tag"], frame["h"], frame["M"]
    section("%s -- h %d kz %d, 70-digit end-to-end assembly"
            % (tag, h, frame["kz"]))
    t_cell = time.time()
    arch, arch_err = arch_lags_mp(M, frame["D"])
    atom, n_atom = atom_lags_mp(frame, nn, pp)
    lag = [a + b for a, b in zip(arch, atom)]
    lag_err = [e + MP_PAD * (1 + abs(v))
               for e, v in zip(arch_err, lag)]
    gmp, gerr = gseq_mp(lag, lag_err)
    lag70 = np.asarray([float(v) for v in lag], dtype=float)
    g70 = np.asarray([float(v) for v in gmp], dtype=float)

    lag64 = float_comparator(frame, nn)
    g64 = gseq_float(lag64)
    cert64 = assembly_error_certificate(g64, gmp, gerr, h)
    cert70 = assembly_error_certificate(g70, gmp, gerr, h)
    lag_max = max(abs(mp.mpf(float(a)) - b) + e
                  for a, b, e in zip(lag64, lag, lag_err))
    print("    atoms %d | max certified lag error %.6e"
          % (n_atom, float(lag_max)))
    print("    assembled entries: observed max %.6e | certified max "
          "%.6e | ||Delta Omega||_inf <= %.6e"
          % (cert64["max_seen"], cert64["max_bound"],
             cert64["row_bound"]), flush=True)

    t_eig = time.time()
    lam64, vec64 = bottom_eigenpair(g64, h)
    print("    deployed eigensolve: lam_min %+.12e [%.1f s]"
          % (lam64, time.time() - t_eig), flush=True)
    t_eig = time.time()
    lam70, vec70 = bottom_eigenpair(g70, h)
    print("    70-digit-input/one-round eigensolve: lam_min %+.12e "
          "[%.1f s]" % (lam70, time.time() - t_eig), flush=True)
    tau64, d64 = tau_scale(lag64, lam64, vec64)
    tau70, d70 = tau_scale(lag70, lam70, vec70)
    cert_pos64 = lam64 - cert64["row_bound"] > 0.0
    cert_pos70 = lam70 - cert70["row_bound"] > 0.0
    print("    tau-scale deployed/high-input %+.12e / %+.12e | "
          "D+ %.6e / %.6e" % (tau64, tau70, d64, d70))
    print("    sign: measured %s -> %s; Weyl-certified deployed %s, "
          "one-round high-input %s (cast ||Delta||_inf %.3e)"
          % ("POS" if lam64 > 0 else "NEG",
             "POS" if lam70 > 0 else "NEG",
             cert_pos64, cert_pos70, cert70["row_bound"]))

    clean_truth, _w, _phi, _pd, _meas, _apr = e3_price(
        vec70, lag70, 20260813 + frame["kz"])
    coverage = injection_coverage(
        frame, lag64, lag70, vec70, clean_truth)
    print("    half-width adversary: coverage %d/%d; injected lag "
          "scale %.3e; priced hw %.3e; transform measured/model "
          "%.3e/%.3e"
          % (coverage["covered"], coverage["total"],
             coverage["discrepancy"], coverage["halfwidth"],
             coverage["measured"], coverage["apriori"]))
    for trial, r, miss, width in coverage["misses"]:
        print("      miss trial %d lag[%d]: truth-center %+.3e > "
              "halfwidth %.3e" % (trial, r, miss, width))

    identity = None
    if tag in ID_CELLS:
        identity = basis_identity(frame, arch, atom, lag, gmp, nn, pp)
        print("    normalization identity (%d pairs): direct-vs-lag "
              "%.3e; direct-vs-arch+prime %.3e; factor/sign controls "
              "%.3e/%.3e"
              % (identity["n_pairs"], float(identity["lag"]),
                 float(identity["split"]),
                 float(identity["factor_control"]),
                 float(identity["sign_control"])))

    plant_entry, plant_ratio = planted_bug(
        frame, lag64, cert64, gmp)
    print("    planted assembly bug: max entry error %.3e = %.3e x "
          "clean certified bound" % (plant_entry, plant_ratio))
    print("    cell runtime %.1f s" % (time.time() - t_cell), flush=True)
    return dict(frame=frame, lam64=lam64, lam70=lam70,
                tau64=tau64, tau70=tau70, cert64=cert64,
                cert70=cert70, cert_pos64=cert_pos64,
                cert_pos70=cert_pos70, coverage=coverage,
                identity=identity, plant_ratio=plant_ratio)


def ledger(rows):
    section("V -- TYPED DEFECT LEDGER")
    sign_flips = [r for r in rows if (r["lam64"] > 0)
                  != (r["lam70"] > 0)]
    misses = sum(r["coverage"]["total"] - r["coverage"]["covered"]
                 for r in rows)
    id_bad = [r for r in rows if r["identity"] is not None and
              (r["identity"]["lag"] > ID_ABS
               or r["identity"]["split"] > ID_ABS)]
    plant_bad = [r for r in rows if r["plant_ratio"] < PLANT_FACTOR]
    uncert = [r for r in rows if r["lam70"] > 0
              and not r["cert_pos70"]]

    assembly_type = ("BUG-CONFIRMED" if sign_flips else
                     "PREMISE-HIDDEN" if uncert else "CLEAN")
    assembly_detail = (
        "high-input sign flips at %s" %
        ",".join(r["frame"]["tag"] for r in sign_flips)
        if sign_flips else
        "%d/%d high-input positive signs lack a Weyl exclusion" %
        (len(uncert), len(rows)) if uncert else
        "all three positive signs survive with Weyl exclusion")
    entries = [
        ("A_ASSEMBLY", assembly_type, "CRITICAL",
         assembly_detail,
         "direct-positive/no-witness arbiter and every downstream "
         "clean-instrument classification"),
        ("B_HALF_WIDTH", "BUG-CONFIRMED" if misses else "CLEAN", "HIGH",
         "%d/%d controlled trials miss truth" %
         (misses, len(rows) * INJECT_N),
         "measured-scale assembly perturbations are empirically covered "
         "on these three extremal directions; this is not a global "
         "assembly interval"),
        ("D_EXTRACTION_ID", "BUG-CONFIRMED" if id_bad else
         "CLEAN", "HIGH",
         ("normalization failed on %s" %
          ",".join(r["frame"]["tag"] for r in id_bad)
          if id_bad else
          "two-cell high-precision finite normalization passes"),
         "faithfulness of the finite built matrix to the intended "
         "localized Weil/Galerkin object; no form-density or exhaustion "
         "claim is inferred"),
        ("NON_VACUITY", "BUG-CONFIRMED" if plant_bad else "CLEAN",
         "CONTROL",
         ("detector failed on %s" %
          ",".join(r["frame"]["tag"] for r in plant_bad)
          if plant_bad else "3/3 planted assembly bugs detected"),
         "validates sensitivity of this adversarial probe"),
    ]
    for target, dtype, severity, evidence, impact in entries:
        print("  %-18s %-15s severity=%-8s | %s"
              % (target, dtype, severity, evidence))
        print("      downstream: %s" % impact)
    return entries, bool(sign_flips or misses or id_bad or plant_bad
                         or uncert)


def main():
    mp.mp.dps = MP_DPS
    print("arbiter_assembly_precision_probe -- "
          "PRIME.COFINAL.ARBITERHP.01")
    print("CCCXXXV FROZEN SPEC_SHA %s  MP_DPS %d"
          % (SPEC_SHA[:16], MP_DPS))
    bad = ast_firewall()
    check("S0 AST oracle firewall", not bad,
          ",".join(bad) if bad else "clean", kill="PIPELINE-BROKEN")

    section("T -- independent integer prime-power table and exact frames")
    nn, pp = prime_power_table(EXPECTED_X_MAX)
    unique = len(nn) == len(np.unique(nn))
    check("T1 sorted unique prime-power table through %d"
          % EXPECTED_X_MAX,
          unique and bool(np.all(np.diff(nn) > 0))
          and int(nn[-1]) <= EXPECTED_X_MAX,
          "%d atoms; last %d" % (len(nn), int(nn[-1])),
          kill="PIPELINE-BROKEN")
    frames = [frame_from_integers(*cell, nn) for cell in CELLS]
    frame_ok = all(f["h"] == f["h_expected"]
                   and f["n"] == EXPECTED_CELL_N[f["tag"]]
                   and f["X"] <= EXPECTED_X_MAX for f in frames)
    check("T2 exact high-precision frame rebuild gives all three "
          "declared cells", frame_ok,
          "; ".join("%s:n=%d,h=%d,M=%d,X=%d"
                    % (f["tag"], f["n"], f["h"], f["M"], f["X"])
                    for f in frames), kill="PIPELINE-BROKEN")
    if KILLS:
        return 1

    rows = [run_cell(frame, nn, pp) for frame in frames]

    section("G -- frozen gates")
    check("G1 high-precision-input signs remain positive on 3/3",
          all(r["lam70"] > 0 for r in rows),
          ", ".join("%s=%+.3e" % (r["frame"]["tag"], r["lam70"])
                    for r in rows))
    check("G2 half-width adversary contains truth on every trial",
          all(r["coverage"]["covered"] == INJECT_N for r in rows),
          "%d/%d covered" %
          (sum(r["coverage"]["covered"] for r in rows),
           len(rows) * INJECT_N))
    check("G3 two-cell extraction normalization at 70 digits",
          all(r["identity"] is None
              or (r["identity"]["lag"] <= ID_ABS
                  and r["identity"]["split"] <= ID_ABS)
              for r in rows),
          "bar %.0e" % float(ID_ABS))
    check("G4 non-vacuity: every planted assembly bug detected at "
          ">= %.0f x clean bound" % PLANT_FACTOR,
          all(r["plant_ratio"] >= PLANT_FACTOR for r in rows),
          ", ".join("%s=%.2e x"
                    % (r["frame"]["tag"], r["plant_ratio"])
                    for r in rows), kill="CONTROL-SILENT")
    _entries, defects = ledger(rows)
    runtime = time.time() - T0
    check("G5 runtime %.1f s < %.0f s frozen bar"
          % (runtime, RUNTIME_BAR), runtime < RUNTIME_BAR)
    passed = sum(ok for _name, ok in CHECKS)
    print("\n[CHECKS] %d/%d passed | [KILLS] %s | runtime %.1f s"
          % (passed, len(CHECKS), KILLS if KILLS else "none", runtime))
    print("[VERDICT] %s" %
          ("NON-CLEAN (see typed ledger)" if defects else "CLEAN"))
    print("NO RH claim; experiment-only; no marker move.")
    return 0 if not KILLS else 1


if __name__ == "__main__":
    raise SystemExit(main())
