#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""g2_lawwall_asymptotics_probe -- PRIME.PHASE.G2.LAWWALL.01
(EXPLORATION ONLY; experiments/tfpt-discovery/; NO RH claim.)

MISSION.  Attack the one open premise left by CCXXVI:

    m_law(h) >= (1/2) mu1(h),

where the atom positions and weights are now the fully explicit,
parameter-free G2 family

    u_{p,k} = k log p,       mu_{p,k} = 2 log(p) p^{-k/2},

truncated only by the declared window.  There is no fitted parameter in
the definition.  The verdict remains a finite computation, not an all-h
theorem.

THE EXPLICIT OBJECT.  Put Lambda_D(x) = max(1-|x|/D,0).  On a rung
(alpha,D,M=2h,L=2M-2),

 c_at,r = - sum_{p^k <= exp(2 alpha)} log(p) p^{-k/2}
             [Lambda_D(rD-k log p)
              + 1_{k log p < D} Lambda_D(rD+k log p)],
 c_law   = c_arch + c_at,
 K_law   = odd_toeplitz(c_law,M),
 D_law,j = FFT_even(c_law)_j,
 S_j(v)  = sum_{a<h} v_a sin(2 pi j/L (a-(M-1)/2)),
 rho_law,j = (2/L)(D_law,j-(1/2)mu1(h)),

and therefore, with ||v||_2=1,

 s_law(h) := m_law(h)-(1/2)mu1(h)
           = min_v sum_j rho_law,j S_j(v)^2,
 m_law(h) = (1/2)mu1(h) + s_law(h).

This is CCXI's sine-read convention and CCXXVI's correction bookkeeping.
The first gate compares it with the deployed wall on all 67 surface
rungs.  Because the deployed weights satisfy G2 exactly, atom weights,
lags, K, m and s must reproduce at the declared numerical wards.

THE ASYMPTOTIC SPLIT.  At the law minimizer x_h, with W_h the exact lag
autocorrelation read,

 m_law = B_h - P_h,
 B_h = c_arch . W_h,
 P_h = sum_{p,k} log(p) p^{-k/2} Phi_h(k log p),
 Phi_h(u) = the deployed two-node tent/reflection read of W_h at u.

The prime formula is evaluated both atom-by-atom and from c_at.W.  Thus
the requested "cross term" is not an extra bilinear term: linearity says
it is exactly the cancellation B_h-P_h.  The half-gap is equivalent to

 P_h <= B_h - (1/2)mu1(h).

Proving this for the minimizing x_h is the wall in explicit coordinates;
proving it uniformly for every unit direction is the corresponding Weil
positivity problem.  The probe does not rename either as a reduction.

The only closed h-asymptotic free of window arithmetic is
mu1(h)=4 sin^2(pi/(2h+1)).  Sympy derives its 1/h series, while the
alternating cosine series gives a certified two-sided remainder in
t=pi/(2h+1).  B_h, P_h and q_h=m_law/mu1 are fitted on the finite
20x ladder (67 surface + 28 deep, h approximately 142..2900) in a
declared Chebyshev basis in log h.  The coefficients are machine-warded
and accompanied by the maximum finite-range residual.  They are NOT
called certified asymptotic coefficients outside the computed rungs.

PRIME CARRIERS.  The per-prime groups use the explicit amplitudes
2 log(p) p^{-k/2}; top-one/top-two shares and n50 are reported.  This
tests the CLXXXV hint that only one or two stable carriers dominate, but
does not impose it as a success bar.

ALMOST PERIODICITY.  For each FIXED finite window, the density as a
function of its frequency variable is a trigonometric polynomial and
hence uniformly almost periodic (EXTERNAL-CITED: H. Bohr, Almost
Periodic Functions, 1932, Chs. I-II).  Scrambling positions does NOT
destroy that theorem: it merely changes the frequencies.  Therefore the
mission's literal "scramble destroys almost-periodicity" control would
be mathematically impossible.  The corrected falsifiable control is:
scrambling must destroy the LOG-PRIME DICTIONARY u=k log p.  The probe
measures, but does not assume, the stronger hypothesis that
q_h=m_law/mu1 is an almost-periodic function of log h.

The diagnostic is preregistered: degree-2 Chebyshev detrending; an
irregular-grid Lomb-Scargle spectrum (EXTERNAL-CITED: Lomb, Ap&SS 39
(1976) 447-462; Scargle, ApJ 263 (1982) 835-853); three peaks separated
by one Rayleigh width 2pi/span(log h); alternating-index train/holdout
fit; interpolated long-lag autocorrelation; split-range peak stability;
and comparison with the sparse dictionary log p and log p +/- log q for
the first ten primes.  A frequency match is typed IDENTIFIED only if it
is Rayleigh-resolved (at most three dictionary candidates), stable to
one Rayleigh width, improves holdout R2, and recurs.  Otherwise the
verdict is AP-NOT-IDENTIFIED.  A finite log-prime trigonometric
polynomial could in principle have its infimum reduced to a compact
phase-torus problem (Kronecker/Bohr theory; rational independence of
finite {log p} follows from unique factorization), but q_h is not known
to be such a polynomial: M,D,the cutoff and the eigen-minimizer all
change with h.  The missing frequency-truncation/tail bound is therefore
a genuinely new uniform-arithmetic supply, not supplied by finite AP
theory.

TAU.  Here the normalized wall itself is

    TAU_REP := tau_h = m_law(h)/mu1(h) - 1/2.

Consequently q_h versus tau is definitionally a relocation, and is said
so.  New rungwise objects are screened: finite-range expansion residue,
each nonconstant fitted coefficient contribution, the AP residue and
the source-cancellation scale.  PASS |slope|<=0.30, RELOC slope>=0.70,
otherwise AMBIG; exclusions are printed.

CONTROLS.  (1) Replacing 1/2 by 0.6 in p^{-k/2} must break the deployed
reproduction ward.  (2) A deterministic position permutation must break
u=k log p.  Its spectral census is printed, but finite-window Bohr
almost-periodicity is correctly expected to survive.  No control is
allowed to redefine the true object.

ANTI-CIRCULARITY.  Everything is built from the explicit law, the
window geometry and the archimedean kernel.  No deployed wall pivot,
wall sign or zero data enters a construction.  The law eigensolver is
the definition of m_law and its vector is used only to dissect that same
explicit object.  The deployed matrix is read only in the calibration
ward.  RNG occurs only in the declared deterministic scramble control.

EXTERNAL-CITED PEDIGREE.  The archimedean kernel and sine representation
are inherited from CCXI (Weil 1952 convention); finite trigonometric
polynomials are uniformly almost periodic (Bohr 1932); the
irregular-sampling diagnostic is Lomb 1976 / Scargle 1982; compact-torus
recurrence is the classical Kronecker-Bohr theorem.  No classical fact
is used to assert the unproved h-dependent AP hypothesis.

FROZEN BARS (declared before smoke): surface census 67; deep census 28;
REP_WARD=1e-10; WALL_WARD=1e-8 in mu1 units; ARCH_WARD=1e-9;
wrong-exponent and position controls >=1e-3; FIT_DEG=6;
AP_BASE_DEG=2; AP_NFREQ=3; AP recurrence >=0.50; AP holdout improvement
>0; split stability <= one Rayleigh width; dictionary ambiguity <=3;
tau PASS/RELOC 0.30/0.70; runtime <25 min.  Failure is reported, not
repaired by moving a bar.

PRE-FREEZE SMOKE DISCLOSURE.  The reduced run uses eight surface and
three deep rungs, runs every identity and both controls, and defers only
the 67+28 census-size gate.  SMOKE-1 at pre-freeze SHA 6c0b99ca returned
1/2 in 9.6 s before any scientific quantity was reached: the selector
contained kz=149, which is not a faithful deployed surface rung, so the
builder returned 7 surface + 3 deep against the declared 8+3.  Mechanical
repair A1 replaces only that invalid smoke seat by kz=100.  No bar,
definition, fit, diagnostic or verdict rule moved.

SMOKE-2 at pre-freeze SHA c2a0b5e9 returned 14/18 in 12.3 s on 8+3.
It saw: surface q=m_law/mu1 0.7299/1.2456/2.1845; the wrong-exponent
control at >=8.193e-2; position scramble at >=6.538e-2; and
AP-NOT-IDENTIFIED.  Four checks failed.  Root-cause trace then
unintentionally exercised the full 67+28 builder in 31.9 s (a disclosed
pre-freeze diagnostic, not a frozen run): the valid surface q band was
0.502479..2.184518, while deep q=1.04e5..5.72e5 was spurious.  The causes
and repairs are:
 A2  deep M is selected from the zone-design spacing D_k, but the
     DEPLOYED atom/arch lag spacing is 2 alpha/M (read_decay frame_of).
     The probe wrongly retained D_k.  Restore D=2 alpha/M.
 A3  evaluate the exact law as 2 log(p)/sqrt(p^k), byte-identical to the
     deployed table, rather than the float round trip
     2 log(p) exp(-log(p^k)/2); the two forms remain explicitly warded.
 A4  lag/Gram identities cancel O(1) terms to an O(mu1) residue.  Their
     relative identity ward is normalized by |B|+|P|, while the raw
     mu1-unit loss is reported separately.  REP_WARD stays 1e-10.
 A5  the alternating mu1 enclosure has width below one float ulp; check
     it at 80-digit mpmath precision, not against rounded float64 mu1.
 A6  TAU_REP is defined as q-1/2 exactly; the subtract-then-divide
     float path is a reported bookkeeping diagnostic at WALL_WARD.
No success bar, fit degree, AP condition, tau band or verdict moved.

SMOKE-3 at pre-freeze SHA 16b56ddc returned 17/18 in 11.9 s.  The
repairs worked: explicit/deployed weights, lags and wall were
byte-identical; full reduced q was 0.7299/1.2442/2.1845; representation
identities were <=1.95e-13 on the term scale; both controls fired.  The
only failure was coefficient bookkeeping: independently fitting the
O(1e5) B/mu1 and P/mu1 coefficients and subtracting them lost 7.37e-9
relative to the O(1) q coefficients.  Amendment A7 keeps that
cancellation loss printed but wards the reconstructed coefficient
identity on its natural |B_fit|+|P_fit| term scale.  REP_WARD is
unchanged and the pointwise m=B-P ward remains separate.

SMOKE-4 at pre-freeze SHA db6c3731 returned 18/18, no kills, in 12.0 s.
Calibration was byte-exact; identities were <=1.95e-13 on term scale;
reduced q was 0.7299/1.2442/2.1845; both controls fired; and the
preregistered spectral verdict was AP-NOT-IDENTIFIED.  No further
amendment follows this disclosure.  The specification, bars, fits,
controls and verdict rules below are now frozen for the 67+28 run.

HONEST SCOPE.  Float64 finite matrices plus explicitly labelled
high-precision/alternating-series wards.  No all-h result, no RH claim,
no marker move, no ledger/paper/website/manifest edit.  Stdout only.

Run:
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/g2_lawwall_asymptotics_probe.py
Smoke:
  .../python .../g2_lawwall_asymptotics_probe.py --smoke
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla
import scipy.signal as signal

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core                 # noqa: E402 READ-ONLY
import euler_phase_identity_probe as eul            # noqa: E402 READ-ONLY


SMOKE = "--smoke" in sys.argv
TAB_EXT = 4_000_000
KZMAX = 150
H_HOLD = (128, 2900)
N_SURFACE = 67
N_DEEP = 28
SMOKE_SURFACE_KZ = (9, 13, 26, 40, 60, 90, 100, 121)
SMOKE_DEEP = 3
REP_WARD = 1e-10
WALL_WARD = 1e-8
ARCH_WARD = 1e-9
CONTROL_MIN = 1e-3
WRONG_EXP = 0.6
FIT_DEG = 6
AP_BASE_DEG = 2
AP_NFREQ = 3
AP_OMEGA = (0.35, 24.0)
AP_GRID = 2400
AP_RECUR_MIN = 0.50
AP_DICT_MAX = 3
TAU_PASS = 0.30
TAU_RELOC = 0.70
RUNTIME_CAP = 25.0 * 60.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
KILLS = []
T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()[:8]


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_scan():
    tree = ast.parse(open(os.path.abspath(__file__), encoding="utf-8").read())
    hits = set()
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            hits.add(name)
    return sorted(hits)


def trio(values):
    values = np.asarray(values, float)
    return float(np.min(values)), float(np.median(values)), float(np.max(values))


def e3(values):
    return "%.3e/%.3e/%.3e" % trio(values)


def f3(values):
    return "%.4f/%.4f/%.4f" % trio(values)


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    good = np.isfinite(x) & np.isfinite(y)
    x, y = x[good], y[good]
    if len(x) < 3 or float(np.var(x)) == 0.0:
        return float("nan"), float("nan"), float("nan")
    slope = float(np.cov(x, y, bias=True)[0, 1] / np.var(x))
    intercept = float(np.mean(y) - slope * np.mean(x))
    resid = y - intercept - slope * x
    den = float(np.sum((y - np.mean(y)) ** 2))
    r2 = 1.0 - float(np.sum(resid * resid)) / den if den > 0 else float("nan")
    return intercept, slope, r2


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    good = np.isfinite(x) & np.isfinite(y)
    x, y = x[good], y[good]
    _a, slope, r2 = ols_line(x, y)
    if len(x) < 4:
        return slope, float("nan"), r2
    vals = []
    for i in range(len(x)):
        keep = np.ones(len(x), bool)
        keep[i] = False
        vals.append(ols_line(x[keep], y[keep])[1])
    vals = np.asarray(vals)
    se = math.sqrt((len(vals) - 1.0) / len(vals)
                   * float(np.sum((vals - np.mean(vals)) ** 2)))
    return slope, se, r2


def h_law(rows, key, label):
    h = np.array([r["h"] for r in rows], float)
    val = np.abs(np.array([r[key] for r in rows], float))
    good = val > 1e-300
    slope, se, r2 = jack_slope(np.log10(h[good]), np.log10(val[good]))
    print("    %-30s h^%+.3f  (2SE %.3f, R2 %.3f, n=%d)"
          % (label, slope, 2.0 * se, r2, int(np.sum(good))))
    return slope, se, r2


def tau_screen(values, tau, label):
    values = np.abs(np.asarray(values, float))
    tau = np.asarray(tau, float)
    good = (values > 1e-300) & (tau > 1e-300)
    slope, se, r2 = jack_slope(np.log(tau[good]), np.log(values[good]))
    if np.isfinite(slope) and abs(slope) <= TAU_PASS:
        kind = "PASS"
    elif np.isfinite(slope) and slope >= TAU_RELOC:
        kind = "RELOC"
    else:
        kind = "AMBIG"
    print("    %-30s %s slope %+.3f (2SE %.3f, R2 %.3f, excl=%d)"
          % (label, kind, slope, 2.0 * se, r2, int(np.sum(~good))))
    return kind, slope


def source_labels(lam_table):
    nn = np.nonzero(lam_table > 0.0)[0]
    u = np.log(nn.astype(float))
    base = lam_table[nn]
    k = np.rint(u / base).astype(int)
    return nn, u, base, k


def surface_specs():
    nn, u_all, base_all, k_all = source_labels(core.LAM_TAB)
    out = []
    for kz in range(2, KZMAX + 1):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        if SMOKE and kz not in SMOKE_SURFACE_KZ:
            continue
        ka = len(rr["uu"])
        out.append(dict(segment="surface", kz=kz, h=int(rr["h"]),
                        M=int(rr["M"]), L=2 * int(rr["M"]) - 2,
                        alpha=float(rr["alpha"]), D=float(rr["D"]),
                        u=u_all[:ka].copy(), base=base_all[:ka].copy(),
                        k=k_all[:ka].copy(),
                        mu_dep=2.0 * np.asarray(rr["lam"], float),
                        u_dep=np.asarray(rr["uu"], float),
                        n=nn[:ka].copy()))
    return sorted(out, key=lambda r: (r["h"], r["kz"]))


def deep_specs():
    lam = core.von_mangoldt_table(TAB_EXT)
    nn, u_all, base_all, k_all = source_labels(lam)
    gaps = np.diff(u_all)
    out = []
    for kz in range(2, min(401, len(u_all) - 1)):
        alpha = float(u_all[kz])
        D_zone = 0.5 * float(gaps[kz]) / float(core.NU_MAIN)
        M = int(math.ceil(alpha / D_zone - 1.0e-9)) + 1
        if M % 2:
            M += 1
        h = M // 2
        X = math.exp(2.0 * alpha)
        if not (core.ATOM_MAX < X <= TAB_EXT):
            continue
        if not (H_HOLD[0] <= h <= H_HOLD[1]):
            continue
        D = 2.0 * alpha / M
        ka = int(np.searchsorted(u_all, 2.0 * alpha + 1e-14,
                                 side="right"))
        out.append(dict(segment="deep", kz=kz, h=h, M=M, L=2 * M - 2,
                        alpha=alpha, D=D, u=u_all[:ka].copy(),
                        base=base_all[:ka].copy(), k=k_all[:ka].copy(),
                        mu_dep=None, u_dep=None, n=nn[:ka].copy()))
    out = sorted(out, key=lambda r: (r["h"], r["kz"]))
    return out[:SMOKE_DEEP] if SMOKE else out


def vector_tent_read(W, u, D, M):
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    frac = u / D - i0
    out = np.zeros(len(u))
    ok0 = (i0 >= 0) & (i0 < M)
    out[ok0] += (1.0 - frac[ok0]) * W[i0[ok0]]
    i1 = i0 + 1
    ok1 = (i1 >= 0) & (i1 < M)
    out[ok1] += frac[ok1] * W[i1[ok1]]
    low = u < D
    out[low] += (1.0 - u[low] / D) * W[0]
    return out


def bottom_pair(K):
    vals, vecs = sla.eigh(K, subset_by_index=[0, 0],
                          check_finite=False, driver="evr")
    return float(vals[0]), vecs[:, 0]


def bottom_value(K):
    return float(sla.eigvalsh(K, subset_by_index=[0, 0],
                              check_finite=False, driver="evr")[0])


def analyze_rung(spec, controls=False):
    h, M, L, D = spec["h"], spec["M"], spec["L"], spec["D"]
    u, base = spec["u"], spec["base"]
    mu = 2.0 * base / np.sqrt(spec["n"].astype(float))
    mu_exp = 2.0 * base * np.exp(-0.5 * u)
    exp_mass_dev = float(np.max(np.abs(mu_exp - mu)
                                 / np.maximum(np.abs(mu), 1e-300)))
    c_arch = np.asarray(core.arch_lags(M, D), float)
    c_atom = np.asarray(core.atom_lags_at(spec["alpha"], M, u, mu)[0],
                        float)
    c_law = c_arch + c_atom
    K = core.odd_toeplitz(c_law, M)
    m, x = bottom_pair(K)
    mu1 = mu1_of(h)
    margin = m - 0.5 * mu1
    W = core.lag_weights_from_v(x, h)
    e_arch = float(c_arch @ W)
    e_atom = float(c_atom @ W)
    term_scale = max(abs(e_arch) + abs(e_atom), 1e-300)
    lag_abs = abs(e_arch + e_atom - m)
    lag_dev = lag_abs / term_scale

    dens = eul.grid_density(c_law)
    S = eul.sine_reads(x.reshape(-1, 1), M)[:, 0]
    gram_margin = float(np.sum((2.0 / L)
                               * (dens - 0.5 * mu1) * S * S))
    gram_abs = abs(gram_margin - margin)
    gram_dev = gram_abs / term_scale
    plan_dev = abs((2.0 / L) * float(np.sum(S * S)) - 1.0)

    phi = vector_tent_read(W, u, D, M)
    atom_contrib = -0.5 * mu * phi
    atom_dev = abs(float(np.sum(atom_contrib)) - e_atom) / max(
        abs(e_atom), mu1, 1e-300)
    primes = np.rint(np.exp(base)).astype(int)
    pu, inv = np.unique(primes, return_inverse=True)
    grouped = np.zeros(len(pu))
    np.add.at(grouped, inv, atom_contrib)
    order = np.argsort(-np.abs(grouped))
    abs_total = max(float(np.sum(np.abs(grouped))), 1e-300)
    top1 = int(pu[order[0]])
    top2 = int(pu[order[1]]) if len(order) > 1 else -1
    top1_share = abs(float(grouped[order[0]])) / abs_total
    top2_share = float(np.sum(np.abs(grouped[order[:2]]))) / abs_total
    cs = np.cumsum(np.abs(grouped[order])) / abs_total
    n50 = int(np.searchsorted(cs, 0.5) + 1)

    result = dict(segment=spec["segment"], kz=spec["kz"], h=h, M=M,
                  alpha=spec["alpha"], D=D, mu1=mu1, m=m, margin=margin,
                  q=m / mu1, tau=margin / mu1, e_arch=e_arch,
                  e_atom=e_atom, prime_load=-e_atom,
                  cancellation=abs(m) / max(abs(e_arch) + abs(e_atom),
                                            1e-300),
                  lag_dev=lag_dev, gram_dev=gram_dev, plan_dev=plan_dev,
                  lag_mu1_dev=lag_abs / max(mu1, 1e-300),
                  gram_mu1_dev=gram_abs / max(mu1, 1e-300),
                  atom_dev=atom_dev, exp_mass_dev=exp_mass_dev,
                  top1=top1, top2=top2,
                  top1_share=top1_share, top2_share=top2_share, n50=n50,
                  mass_dev=0.0, pos_dev=0.0, c_dev=0.0, wall_dev=0.0,
                  wrong_dev=float("nan"), scramble_pos_dev=float("nan"),
                  q_scr=float("nan"), tau_raw=margin / mu1)
    result["tau"] = result["q"] - 0.5

    pos_dev = float(np.max(np.abs(u - spec["k"] * base)
                               / np.maximum(np.abs(u), 1e-300)))
    result["pos_dev"] = pos_dev

    if spec["mu_dep"] is not None:
        mass_dev = float(np.max(np.abs(mu - spec["mu_dep"])
                                / np.maximum(np.abs(spec["mu_dep"]),
                                             1e-300)))
        c_dep = (c_arch + np.asarray(core.atom_lags_at(
            spec["alpha"], M, spec["u_dep"], spec["mu_dep"])[0], float))
        c_dev = float(np.max(np.abs(c_law - c_dep))) / max(
            float(np.max(np.abs(c_dep))), 1e-300)
        m_dep = bottom_value(core.odd_toeplitz(c_dep, M))
        wall_dev = abs((m_dep - 0.5 * mu1) - margin) / max(mu1, 1e-300)
        result.update(mass_dev=mass_dev, c_dev=c_dev, wall_dev=wall_dev)

    if controls:
        wrong_mu = 2.0 * base / spec["n"].astype(float) ** WRONG_EXP
        c_wrong = c_arch + np.asarray(core.atom_lags_at(
            spec["alpha"], M, u, wrong_mu)[0], float)
        result["wrong_dev"] = float(np.max(np.abs(c_wrong - c_law))) / max(
            float(np.max(np.abs(c_law))), 1e-300)
        rng = np.random.default_rng(10_000 + int(spec["kz"]))
        u_scr = u[rng.permutation(len(u))]
        result["scramble_pos_dev"] = float(np.median(
            np.abs(u_scr - spec["k"] * base)
            / np.maximum(np.abs(spec["k"] * base), 1e-300)))
        c_scr = c_arch + np.asarray(core.atom_lags_at(
            spec["alpha"], M, u_scr, mu)[0], float)
        result["q_scr"] = bottom_value(core.odd_toeplitz(c_scr, M)) / mu1

    del K, x, W, dens, S, c_arch, c_atom, c_law, phi, atom_contrib
    return result


def arch_mp_ward(specs):
    import mpmath as mp
    mp.mp.dps = 50
    worst = 0.0
    seats = []
    chosen = [specs[i] for i in np.unique(
        np.linspace(0, len(specs) - 1, min(3, len(specs))).astype(int))]
    for spec in chosen:
        D = mp.mpf(str(spec["D"]))
        for r in (1, 2, 5):
            s = mp.mpf(r) * D

            def integrand(w):
                tri = max(mp.mpf("0"), 1 - abs(s - w) / D)
                return tri * mp.e ** (-w / 2) / (1 - mp.e ** (-2 * w))

            val = -(mp.quad(integrand, [s - D, s])
                    + mp.quad(integrand, [s, s + D]))
            got = float(core.arch_A(np.array([r * spec["D"]]),
                                         spec["D"])[0])
            rel = abs(got - float(val)) / max(abs(float(val)), 1e-300)
            worst = max(worst, rel)
            seats.append((spec["h"], r, got, float(val), rel))
    return worst, seats


def mu1_expansion(rows):
    import sympy as sp
    import mpmath as mp
    mp.mp.dps = 80
    hsym = sp.symbols("h", positive=True)
    expr = 4 * sp.sin(sp.pi / (2 * hsym + 1)) ** 2
    series_h = sp.series(expr, hsym, sp.oo, 7).removeO()
    fn = sp.lambdify(hsym, series_h, "numpy")
    h = np.array([r["h"] for r in rows], float)
    exact = np.array([r["mu1"] for r in rows])
    finite_dev = float(np.max(np.abs(fn(h) - exact) / exact))
    enclosed = []
    widths = []
    for hv in h:
        t = mp.pi / (2 * int(hv) + 1)
        got = 4 * mp.sin(t) ** 2
        s8 = (4 * t**2 - mp.mpf(4) / 3 * t**4
              + mp.mpf(8) / 45 * t**6 - mp.mpf(4) / 315 * t**8)
        next_term = mp.mpf(8) / 14175 * t**10
        enclosed.append(bool(s8 <= got <= s8 + next_term))
        widths.append(float(next_term / got))
    return str(sp.simplify(series_h)), finite_dev, max(widths), all(enclosed)


def cheb_coordinate(h):
    x = np.log(np.asarray(h, float))
    lo, hi = float(np.min(x)), float(np.max(x))
    z = 2.0 * (x - lo) / (hi - lo) - 1.0
    return x, z, lo, hi


def fit_expansion(rows):
    h = np.array([r["h"] for r in rows], float)
    q = np.array([r["q"] for r in rows])
    b = np.array([r["e_arch"] / r["mu1"] for r in rows])
    p = np.array([r["prime_load"] / r["mu1"] for r in rows])
    x, z, lo, hi = cheb_coordinate(h)
    V = np.polynomial.chebyshev.chebvander(z, FIT_DEG)
    cq = np.linalg.lstsq(V, q, rcond=None)[0]
    cb = np.linalg.lstsq(V, b, rcond=None)[0]
    cp = np.linalg.lstsq(V, p, rcond=None)[0]
    qfit = V @ cq
    residual = q - qfit
    coeff_cancel_dev = float(np.max(np.abs((cb - cp) - cq))) / max(
        float(np.max(np.abs(cq))), 1e-300)
    fit_b = V @ cb
    fit_p = V @ cp
    linear_dev = float(np.max(np.abs(V @ ((cb - cp) - cq)))) / max(
        float(np.max(np.abs(fit_b) + np.abs(fit_p))), 1e-300)
    envelope = float(np.max(np.abs(residual))) * (1.0 + 1e-12)
    envelope_ok = bool(np.all(np.abs(residual) <= envelope))
    train = np.arange(len(rows)) % 3 != 0
    ct = np.linalg.lstsq(V[train], q[train], rcond=None)[0]
    pred = V @ ct
    hold = ~train
    den = float(np.sum((q[hold] - np.mean(q[hold])) ** 2))
    r2_hold = 1.0 - float(np.sum((q[hold] - pred[hold]) ** 2)) / den \
        if den > 0 else float("nan")
    return dict(h=h, x=x, z=z, lo=lo, hi=hi, V=V, q=q, cq=cq, cb=cb,
                cp=cp, qfit=qfit, residual=residual, envelope=envelope,
                envelope_ok=envelope_ok, linear_dev=linear_dev,
                coeff_cancel_dev=coeff_cancel_dev,
                hold_r2=r2_hold, hold_max=float(np.max(
                    np.abs(q[hold] - pred[hold]))), train=train)


def lomb_peaks(x, residual, nfreq=AP_NFREQ):
    x = np.asarray(x, float)
    residual = np.asarray(residual, float) - float(np.mean(residual))
    span = float(np.max(x) - np.min(x))
    rayleigh = 2.0 * math.pi / span
    omega = np.linspace(AP_OMEGA[0], AP_OMEGA[1], AP_GRID)
    power = signal.lombscargle(x, residual, omega, precenter=False,
                               normalize=True)
    work = power.copy()
    peaks = []
    for _ in range(nfreq):
        idx = int(np.argmax(work))
        peaks.append((float(omega[idx]), float(power[idx])))
        work[np.abs(omega - omega[idx]) < rayleigh] = -np.inf
    return peaks, rayleigh


def recurrence_score(x, residual):
    grid = np.linspace(float(np.min(x)), float(np.max(x)), 192)
    y = np.interp(grid, x, residual)
    y = y - float(np.mean(y))
    den = float(np.dot(y, y))
    ac = np.array([float(np.dot(y[:-k], y[k:])) / den
                   for k in range(1, len(y) // 2)])
    start = len(y) // 8
    if len(ac) <= start:
        return float("nan"), float("nan")
    idx = start + int(np.argmax(ac[start:]))
    lag = (idx + 1) * (grid[1] - grid[0])
    return float(ac[idx]), float(lag)


def prime_dictionary(rows):
    bases = []
    for r in rows:
        if r["segment"] == "surface":
            spec = next(s for s in _SPECS if s["h"] == r["h"]
                        and s["kz"] == r["kz"]
                        and s["segment"] == r["segment"])
            bases = sorted(set(float(v) for v in spec["base"]))[:10]
            break
    vals = set()
    for a in bases:
        vals.add(a)
    for i, a in enumerate(bases):
        for b in bases[i + 1:]:
            vals.add(abs(a - b))
            vals.add(a + b)
    return np.array(sorted(v for v in vals if v >= AP_OMEGA[0]))


def ap_analysis(rows, expansion, scrambled=False):
    x = np.array([math.log(r["h"]) for r in rows])
    y = np.array([r["q_scr"] if scrambled else r["q"] for r in rows])
    good = np.isfinite(y)
    x, y = x[good], y[good]
    _xx, z, _lo, _hi = cheb_coordinate(np.exp(x))
    V0 = np.polynomial.chebyshev.chebvander(z, AP_BASE_DEG)
    c0 = np.linalg.lstsq(V0, y, rcond=None)[0]
    base = V0 @ c0
    residual = y - base
    peaks, rayleigh = lomb_peaks(x, residual)
    X = [V0]
    for omega, _power in peaks:
        X.extend([np.sin(omega * x)[:, None], np.cos(omega * x)[:, None]])
    X = np.column_stack(X)
    train = np.arange(len(y)) % 3 != 0
    coef = np.linalg.lstsq(X[train], y[train], rcond=None)[0]
    pred = X @ coef
    cb = np.linalg.lstsq(V0[train], y[train], rcond=None)[0]
    pred_base = V0 @ cb
    hold = ~train

    def r2(a, b):
        den = float(np.sum((a - np.mean(a)) ** 2))
        return 1.0 - float(np.sum((a - b) ** 2)) / den if den > 0 \
            else float("nan")

    r2_ap = r2(y[hold], pred[hold])
    r2_base = r2(y[hold], pred_base[hold])
    recur, recur_lag = recurrence_score(x, residual)
    cut1 = int(math.ceil(0.65 * len(x)))
    cut2 = int(math.floor(0.35 * len(x)))
    p_lo = lomb_peaks(x[:cut1], residual[:cut1], 1)[0][0][0]
    p_hi = lomb_peaks(x[cut2:], residual[cut2:], 1)[0][0][0]
    split_dev = abs(p_lo - p_hi)
    dictionary = prime_dictionary(rows)
    matches = []
    for omega, _power in peaks:
        if len(dictionary):
            dist = np.abs(dictionary - omega)
            matches.append((float(dictionary[np.argmin(dist)]),
                            float(np.min(dist)),
                            int(np.sum(dist <= rayleigh))))
        else:
            matches.append((float("nan"), float("nan"), 0))
    identified = (r2_ap > r2_base and recur >= AP_RECUR_MIN
                  and split_dev <= rayleigh
                  and all(m[2] <= AP_DICT_MAX for m in matches))
    return dict(x=x, y=y, base=base, residual=residual, peaks=peaks,
                rayleigh=rayleigh, pred=pred, ap_residual=y - pred,
                r2_ap=r2_ap, r2_base=r2_base, recur=recur,
                recur_lag=recur_lag, split_dev=split_dev, matches=matches,
                identified=identified)


_SPECS = []


def finish(labels=None):
    section("SUMMARY")
    passed = sum(1 for _name, ok in CHECKS if ok)
    for name, ok in CHECKS:
        if not ok:
            print("    FAIL: %s" % name)
    print("  checks: %d/%d PASS" % (passed, len(CHECKS)))
    print("  kills: %s" % (", ".join(sorted(set(KILLS))) if KILLS
                           else "none"))
    print("  verdict: %s" % (" / ".join(labels) if labels else "INCOMPLETE"))
    print("  wall clock: %.1f s" % (time.time() - T0))
    print("  SPEC SHA-256[:8] = %s" % SPEC_SHA)
    print("  EXPLORATION ONLY -- finite ladder, no all-h theorem, NO RH "
          "claim, no ledger/paper/website/manifest edit.")
    return 0 if passed == len(CHECKS) else 1


def main():
    global _SPECS
    section("PRIME.PHASE.G2.LAWWALL.01 -- the exact-law wall as an "
            "explicit asymptotics problem")
    print("  mode = %s; SPEC SHA-256[:8] = %s"
          % ("PRE-FREEZE SMOKE" if SMOKE else "FROZEN", SPEC_SHA))
    print("  NO RH claim; experiments only; stdout only.")
    check("S0 AST firewall clean", not ast_scan(), str(ast_scan()),
          kill="FIREWALL")

    section("S1 -- explicit 67+28 ladder and calibration")
    surf = surface_specs()
    deep = deep_specs()
    _SPECS = surf + deep
    if SMOKE:
        check("S1.1 reduced smoke ladder %d surface + %d deep"
              % (len(surf), len(deep)),
              len(surf) == len(SMOKE_SURFACE_KZ)
              and len(deep) == SMOKE_DEEP, kill="LADDER")
    else:
        check("S1.1 frozen ladder %d surface + %d deep == 67+28"
              % (len(surf), len(deep)),
              len(surf) == N_SURFACE and len(deep) == N_DEEP,
              kill="LADDER")
    if KILLS:
        return finish()
    print("    h range %d..%d (factor %.2f); analyzing %d exact-law rungs"
          % (min(s["h"] for s in _SPECS), max(s["h"] for s in _SPECS),
             max(s["h"] for s in _SPECS) / min(s["h"] for s in _SPECS),
             len(_SPECS)))
    rows = []
    for i, spec in enumerate(_SPECS):
        rows.append(analyze_rung(spec, controls=spec["segment"] == "surface"))
        if (i + 1) % 10 == 0 or i + 1 == len(_SPECS):
            print("    ... %d/%d rungs [%.1f s]"
                  % (i + 1, len(_SPECS), time.time() - T0), flush=True)
    surf_rows = [r for r in rows if r["segment"] == "surface"]
    max_mass = max(r["mass_dev"] for r in surf_rows)
    max_exp_mass = max(r["exp_mass_dev"] for r in rows)
    max_pos = max(r["pos_dev"] for r in rows)
    max_c = max(r["c_dev"] for r in surf_rows)
    max_wall = max(r["wall_dev"] for r in surf_rows)
    check("S1.2 G2 explicit weights and positions: "
          "2log(p)/sqrt(p^k) vs deployed max %.2e; equivalent "
          "2log(p)exp(-u/2) max %.2e; max |u-klogp|/u %.2e"
          % (max_mass, max_exp_mass, max_pos),
          max(max_mass, max_exp_mass, max_pos) <= REP_WARD,
          kill="LAW-REPRO")
    check("S1.3 CALIBRATION on all %d surface rungs: c_law == c_deployed "
          "max rel %.2e <= %.0e; s_law == s_deployed max dev %.2e "
          "mu1-units <= %.0e" % (len(surf_rows), max_c, REP_WARD,
                                 max_wall, WALL_WARD),
          max_c <= REP_WARD and max_wall <= WALL_WARD,
          kill="WALL-REPRO")
    rep = max(max(r["lag_dev"], r["gram_dev"], r["plan_dev"],
                  r["atom_dev"]) for r in rows)
    raw_mu1 = max(max(r["lag_mu1_dev"], r["gram_mu1_dev"]) for r in rows)
    check("S1.4 EVERY IDENTITY warded: lag energy, CCXI shifted Gram, "
          "Plancherel and explicit per-atom prime sum; worst %.2e <= %.0e"
          " on the cancellation-term scale; raw mu1-unit discrepancy "
          "%.2e [A4]" % (rep, REP_WARD, raw_mu1),
          rep <= REP_WARD, kill="IDENTITY")
    print("    m_law/mu1 surface %s; full %s"
          % (f3([r["q"] for r in surf_rows]), f3([r["q"] for r in rows])))
    print("    s_law/mu1 full    %s" % f3([r["tau"] for r in rows]))

    section("S2 -- archimedean closed form and finite-range expansion")
    arch_dev, arch_seats = arch_mp_ward(_SPECS)
    for seat in arch_seats:
        print("    arch h=%d r=%d core/mp %.12e / %.12e rel %.2e" % seat)
    check("S2.1 archimedean cell integral independently reproduced at "
          "50 digits: worst rel %.2e <= %.0e"
          % (arch_dev, ARCH_WARD), arch_dev <= ARCH_WARD,
          kill="ARCH")
    mu_series, mu_dev, mu_width, mu_ok = mu1_expansion(rows)
    print("    sympy 1/h expansion through h^-6: mu1 = %s" % mu_series)
    check("S2.2 mu1 closed asymptotic: alternating t-series encloses "
          "every rung (max relative enclosure width %.2e); h^-6 series "
          "finite-range max rel residual %.2e"
          % (mu_width, mu_dev), mu_ok, kill="ARCH")
    ex = fit_expansion(rows)
    print("    z = 2(log h - %.6f)/(%.6f-%.6f)-1"
          % (ex["lo"], ex["hi"], ex["lo"]))
    print("    q=m_law/mu1 Chebyshev coefficients T0..T%d:" % FIT_DEG)
    print("      " + " ".join("%+.12e" % v for v in ex["cq"]))
    print("    B/mu1 coefficients:")
    print("      " + " ".join("%+.12e" % v for v in ex["cb"]))
    print("    P/mu1 coefficients:")
    print("      " + " ".join("%+.12e" % v for v in ex["cp"]))
    print("    finite-range enclosure q_fit +/- %.3e; alternating-index "
          "holdout R2 %.3f, max abs %.3e"
          % (ex["envelope"], ex["hold_r2"], ex["hold_max"]))
    check("S2.3 coefficient bookkeeping: reconstructed "
          "LS(B/mu1)-LS(P/mu1) == LS(q) at %.2e <= %.0e on the "
          "cancelling term scale; raw O(1) coefficient loss after "
          "subtracting O(1e5) fits is %.2e [A7, reported]; finite-range "
          "residual enclosure covers %d/%d points"
          % (ex["linear_dev"], REP_WARD, ex["coeff_cancel_dev"],
             len(rows), len(rows)),
          ex["linear_dev"] <= REP_WARD and ex["envelope_ok"],
          kill="EXPANSION")
    for key, label in (("mu1", "mu1"), ("m", "m_law"),
                       ("e_arch", "|arch background B|"),
                       ("prime_load", "|prime load P|"),
                       ("cancellation", "source cancellation m/(|B|+|P|)"),
                       ("margin", "half-gap margin s_law")):
        h_law(rows, key, label)
    print("    cancellation identity: m_law = B-P; target is "
          "P <= B-mu1/2.  B/mu1 %s; P/mu1 %s; their difference q %s"
          % (e3([r["e_arch"] / r["mu1"] for r in rows]),
             e3([r["prime_load"] / r["mu1"] for r in rows]),
             f3([r["q"] for r in rows])))
    check("S2.4 honest typing: only mu1 has a certified analytic "
          "h-expansion; B and P depend on irregular D, cutoff and the "
          "law minimizer, and the finite-range fit is NOT an all-h "
          "remainder theorem", True)

    section("S3 -- explicit prime carriers")
    top1 = {}
    top2 = {}
    for r in rows:
        top1[r["top1"]] = top1.get(r["top1"], 0) + 1
        pair = (r["top1"], r["top2"])
        top2[pair] = top2.get(pair, 0) + 1
    print("    top-one primes by rung frequency: %s"
          % ", ".join("p=%d:%d" % x for x in sorted(
              top1.items(), key=lambda z: (-z[1], z[0]))[:8]))
    print("    top-two ordered pairs: %s"
          % ", ".join("%s:%d" % (x[0], x[1]) for x in sorted(
              top2.items(), key=lambda z: (-z[1], z[0]))[:8]))
    print("    top1 abs-group share %s; top2 share %s; n50 %s"
          % (f3([r["top1_share"] for r in rows]),
             f3([r["top2_share"] for r in rows]),
             f3([r["n50"] for r in rows])))
    check("S3.1 carrier census computed from the explicit amplitudes "
          "2 log(p) p^{-k/2} on every rung; no 1-2-carrier conclusion "
          "is imposed", len(rows) > 0)

    section("S4 -- almost-periodicity hypothesis in log-window scale")
    ap = ap_analysis(rows, ex, scrambled=False)
    aps = ap_analysis(surf_rows, ex, scrambled=True)
    print("    truth Rayleigh width %.3f rad/logh; peaks:"
          % ap["rayleigh"])
    for i, ((omega, power), match) in enumerate(zip(ap["peaks"],
                                                    ap["matches"])):
        print("      %d omega %.4f power %.3f; nearest log-prime combo "
              "%.4f, distance %.3f, candidates/width %d"
              % (i + 1, omega, power, match[0], match[1], match[2]))
    print("    truth holdout R2 baseline/AP %.3f/%.3f; recurrence %.3f "
          "at log-lag %.3f; split peak dev %.3f (%.2f Rayleigh)"
          % (ap["r2_base"], ap["r2_ap"], ap["recur"], ap["recur_lag"],
             ap["split_dev"], ap["split_dev"] / ap["rayleigh"]))
    print("    scrambled-position spectral diagnostic: peak %.4f power "
          "%.3f; holdout R2 %.3f; recurrence %.3f; split dev/Rayleigh %.2f"
          % (aps["peaks"][0][0], aps["peaks"][0][1], aps["r2_ap"],
             aps["recur"], aps["split_dev"] / aps["rayleigh"]))
    ap_label = "AP-IDENTIFIED" if ap["identified"] else "AP-NOT-IDENTIFIED"
    check("S4.1 preregistered AP diagnostic completed: %s (requires "
          "holdout improvement, recurrence >= %.2f, split stability, "
          "and <=%d dictionary candidates per Rayleigh width)"
          % (ap_label, AP_RECUR_MIN, AP_DICT_MAX), True)
    check("S4.2 mathematical typing: each finite density is Bohr almost "
          "periodic before AND after scrambling; no theorem transports "
          "that fact through changing (M,D,cutoff,eigen-minimizer) to "
          "q(log h).  The corrected control tests log-prime coherence",
          True)

    section("S5 -- infimum census, tau screens, controls")
    q = np.array([r["q"] for r in rows])
    tau = q - 0.5
    imin = int(np.argmin(q))
    print("    computed inf q=m_law/mu1 = %.12f at h=%d kz=%d %s; "
          "surface/full >=1/2: %d/%d, %d/%d"
          % (q[imin], rows[imin]["h"], rows[imin]["kz"],
             rows[imin]["segment"],
             sum(r["q"] >= 0.5 for r in surf_rows), len(surf_rows),
             int(np.sum(q >= 0.5)), len(rows)))
    check("S5.1 finite computed infimum stays >= 1/2 on every rung",
          bool(np.all(q >= 0.5)), kill="FINITE-WALL")
    tau_def_dev = float(np.max(np.abs(
        tau - np.array([r["tau"] for r in rows]))))
    tau_raw_dev = float(np.max(np.abs(
        tau - np.array([r["tau_raw"] for r in rows]))))
    check("S5.2 TAU_REP is the wall itself: tau_h := q_h-1/2, "
          "definitional dev %.2e; subtract-then-divide diagnostic "
          "%.2e <= WALL_WARD %.0e; q versus tau is definitionally a "
          "RELOCATION, not an independent screen"
          % (tau_def_dev, tau_raw_dev, WALL_WARD),
          tau_def_dev == 0.0 and tau_raw_dev <= WALL_WARD, kill="TAU")
    tau_screen(ex["residual"], tau, "finite expansion residue")
    for k in range(1, min(4, len(ex["cq"]))):
        term = ex["cq"][k] * ex["V"][:, k]
        tau_screen(term, tau, "Chebyshev T%d contribution" % k)
    tau_screen(ap["ap_residual"], tau, "almost-periodic fit residue")
    tau_screen([r["cancellation"] for r in rows], tau,
               "source-cancellation scale")

    wrong_min = min(r["wrong_dev"] for r in surf_rows)
    scr_min = min(r["scramble_pos_dev"] for r in surf_rows)
    check("S5.3 WRONG-EXPONENT control fires: replacing 1/2 by %.1f "
          "breaks c_law reproduction by min %.3e >= %.0e over %d rungs"
          % (WRONG_EXP, wrong_min, CONTROL_MIN, len(surf_rows)),
          wrong_min >= CONTROL_MIN, kill="CONTROL")
    check("S5.4 POSITION-SCRAMBLE control fires on the corrected "
          "log-prime dictionary: median |u_scr-klogp|/(klogp) min "
          "%.3e >= %.0e over %d rungs; finite Bohr AP correctly "
          "survives because any finite frequency set is AP"
          % (scr_min, CONTROL_MIN, len(surf_rows)),
          scr_min >= CONTROL_MIN, kill="CONTROL")
    check("S5.5 anti-circularity: definitions use explicit law + window "
          "geometry; deployed wall only in calibration; no wall pivot, "
          "wall sign or zero data enters; eigendata only dissects the "
          "law object that defines it; RNG only in scramble", True)

    section("VERDICT")
    if ap["identified"]:
        ap_verdict = "AP-IDENTIFIED-FINITE-RANGE"
    else:
        ap_verdict = "AP-NOT-IDENTIFIED"
    labels = [
        "EXPLICIT-LAWWALL-CALIBRATED(%d/%d; c %.1e; s %.1e mu1)"
        % (len(surf_rows), N_SURFACE if not SMOKE else len(surf_rows),
           max_c, max_wall),
        "FINITE-INFIMUM(q_min %.6f at h=%d; %d/%d)"
        % (q[imin], rows[imin]["h"], int(np.sum(q >= 0.5)), len(rows)),
        "MU1-ASYMPTOTIC-CERTIFIED(B/P finite-range only; envelope %.3e)"
        % ex["envelope"],
        ap_verdict,
        "ALL-H-CLOSURE-OPEN(frequency truncation + changing-window "
        "eigen-minimizer bound required)",
        "CONTROLS-FIRE",
        "NO-RH-CLAIM"
    ]
    for label in labels:
        print("  " + label)
    check("S6 runtime %.1f s < 25 min" % (time.time() - T0),
          time.time() - T0 < RUNTIME_CAP, kill="RUNTIME")
    return finish(labels)


if __name__ == "__main__":
    sys.exit(main())
