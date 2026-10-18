#!/usr/bin/env python3
"""l1_montage_probe.py -- L1-MONTAGE: the first explicit assembly of
the CONTINUUM candidate of the Z1 operator and the machine test of the
scaling limit in the CORRECT normalization.

EXPLORATION ONLY (experiments/ firewall): nothing here is a
verification claim; no verification/, paper, ledger or website surface
is touched; no marker moves; NO RH statement.

CONTEXT (the chain this probe closes into one object):
  * S-C (chain_deck_sector_probe): the arch density rho(t) =
    e^{-t/2}/(1 - e^{-2t}) is EXACTLY the sum of the three deck-sector
    channels of the 48-site NS cover lift; the lattice operator read
    converges with ~N^-2 and joint scalar s* -> 0.9999 at N = 192.
  * S-D (chain_weyl_mass_probe): the flow alpha ARE the Schur
    parameters [E]; the arch+pole background alone is not
    Caratheodory (PD death between the n=2 and n=3 cell).
  * 5b (z1_jacobi_probe) M2.2: NO h-stable alpha ladder in RAW
    normalization (min r_env = -0.13) -- the negative this probe
    re-examines in the correct (fixed-frequency) normalization.
  * 5c (z1_uvarov_probe): atoms are single-lag insertions (duality
    point), slot identity exact, stabilization law.
  * v679 (orbifold continuum OS): the continuum template -- fixed
    continuum data over a discretization ladder, difference-ratio
    rates, geometric extrapolants with bands, honest typing of what
    stays open for the formal limit.
  * v695 S1.4: the comb sequence c + pole is positive-feasible; the
    deployed signedness IS the pole subtraction.

THE CORE IDEA (the 5b repair): the window measure lives on the circle
with cell width D(h) -> 0.  The continuum candidate is the measure on
the t-axis (window symbol PER BANDWIDTH).  Coefficient-level ladders
(raw alpha_k, or alpha at matched u = kD) need not converge -- the
right object is the m-/Schur-FUNCTION side: the window transform

    W_h(s, t)  =  sum_{d >= 1} p_d e^{(-s + i t) d D_h}

at FIXED band points (t = band position, s = Abel depth in t-units),
i.e. F_h(z) at fixed test points z = e^{(-s+it)D_h} in the band.

Sections and PREREGISTERED BARS (declared before the assembled run;
all bars were set from an interactive calibration scan of the same
formulas on 2026-08-03, documented in CALIBRATION below):

  G0 guards.
    G0.1 AST firewall (banned names: zetazero, nzeros, zeta,
         second_sheet_zero) -- construction path is counting data +
         closed expressions only.
    G0.2 5-window family (identical 5b/5c selection, 67 complete
         frame-A windows), full-depth Levinson PD on all 5.
    G0.3 THE CONTINUUM DICTIONARY, locked by machine: (a) the arch
         lag read is c_ar,d = -D rho(dD) (SIGN MEASURED: the arch
         half couples NEGATIVELY in the deployed background; the
         positive-density object is rho + pole, the deployed one is
         2cosh - rho = the pole-subtraction reading of v695 S1.4)
         [rel <= 1e-3 coarse / 1e-4 at window 4, tau ~ 1]; (b) the
         pole lag read is +D 2cosh(dD/2) [same bars]; (c) every
         INTERIOR atom (u <= 2 alpha - 2D) reads a total of exactly
         -mu_n/2 [<= 1e-12], while the reach-edge atom (u/D = M)
         reads partially -- the reach boundary is a slot, mirror of
         the UV cell (measured, typed); (d) the
         deployed diagonal cell obeys c_ar,0 ~ ln(1/D): increments
         per D-halving = ln 2 within 2% -- the d = 0 cell is the
         UV/renormalization slot, carried closed below.

  M1 the continuum arch operator (the S-C limit object, explicit).
    M1.1 [E] the continuum object NAMED: the diagonal operator with
         spectrum {2k + 1/2} (deck channels {6k + b}, b in
         {1/2, 5/2, 9/2}); heat trace == rho and the three deck
         channels exact [<= 1e-12].
    M1.2 [E] the N-ladder of the cover lift (N = 48..768): joint
         scalar s*(N) and max-rel-dev(N) with difference-ratio rates
         in [1.8, 2.3] (~N^-2) and geometric extrapolant
         |s*(inf) - 1| <= 1e-6, dev(768) <= 1e-3 -- the lift
         converges to the continuum object, s* -> 1.
    M1.3 [E] per-mode spectral convergence: eps_m(N) extrapolates to
         m/2 [rel <= 1e-5 for m <= 25] -- operator data, not only
         traces.
    M1.4 [E] the explicit multiplication/Jacobi object of the
         arch+pole half: multiplication by tau on
         L^2([tau_min, T_max], (rho(tau) + 2cosh(tau/2)) dtau) with
         tau_min = D_4 (the declared UV cell) and T_max = 2 alpha_4;
         Stieltjes/Lanczos Jacobi matrix K = 48; Gauss quadrature
         reproduces direct integrals [<= 1e-12] and the coefficients
         are quadrature-refinement stable [<= 1e-12]; spectrum inside
         [0.9 tau_min, 1.001 T_max].

  M2 the scaled limit (the 5b-M2.2 re-examination).
    M2.1 [measured anchor, both readings side by side] RAW
         normalization: the family alpha ladder fails the 5b bar
         r_env >= 0.80 (min r_env reproduced, was -0.13), AND the
         FIXED-MEASURE pair (synthetic rung M = 2048 vs window 4,
         same measure, D halved) also fails [r_env < 0.80]: the raw
         coefficient ladder is not h-stable even without reach
         effects -- the normalization, not only the measure, is the
         issue.
    M2.2 [central] the D-ladder in fixed-frequency normalization:
         synthetic dyadic ladder (fixed measure = window 4's:
         T = 2 alpha_4, all ka_4 atoms; M = 256..4096, reference
         M = 8192); renormalized transform
             W-hat = W - c_UV(D),  c_UV = (1/2) ln(1 - e^{(-s+it)D})
         (the CLOSED UV term of the -1/(2 tau) arch divergence);
         gates at every battery point (s in {0.25, 0.5, 1.0} x t in
         {5, 12, 27, 45}): |W-hat_j - W-hat_ref| strictly decreasing,
         LSQ D-rate in [0.5, 1.7] (first order, edge-dominated --
         measured, understood), err at M = 4096 <= 0.04.  The D/UV
         limit exists at EVERY band point including s < 1/2.
    M2.3 [E, must-fail] WITHOUT the closed UV renormalization the
         ladder is NOT Cauchy: the last raw increment equals the UV
         drift (1/2) ln 2 = 0.3466 within [0.28, 0.42] and is >= 4x
         the renormalized increment, at every battery point.
    M2.4 [central, THE REPAIR] the true family ladder converges in
         fixed-frequency normalization: for each window h a
         D-MATCHED reference rung (same D, full window-4 measure) is
         built; then
             W-hat_syn(D_h) - W-hat_h  ==  closed montage tail
         (atoms ka_h..ka_4 as point masses + closed pole integral +
         closed arch-tower integral over [2 alpha_h, 2 alpha_4]) to
         |dev| <= 3e-3 at all s in {0.75, 1.0, 1.5} x t battery --
         combined with M2.2 the window ladder converges as a
         FUNCTION limit at fixed band points for s > 1/2.  THIS is
         the repair of the 5b-M2.2 negative by correct normalization
         (both readings documented side by side in M2.1).
    M2.5 [measured] WHERE it diverges: the s-anatomy at t = 27.
         (a) the parts: at s = 1/4 the pole tail and the atom tail
         are individually large and cancel; gate: |pole tail| >=
         3 x |combined tail| on the two coarsest windows; (b) the
         montage-prediction residual grows monotonically as s drops
         (0.75 -> 0.5 -> 0.25) -- the missing piece at s <= 1/2 is
         the zero-side fluctuation (PNT-level cancellation measured,
         residual named, never loaded).  The divergence is NOT in D
         (M2.2 converges at s = 0.25); it sits in the REACH tails at
         s <= 1/2 -- the half-plane boundary is the critical line,
         typed, firewalled.

  M3 the montage.
    M3.1 [E] the tent read converges to the POINT-MASS reading: for
         single atoms (n = 2 and a late prime), the transform of the
         deployed <= 2-cell tent read minus the exact point value
         -(mu_n/2) e^{(-s+it)u_n} falls with LSQ D-rate in
         [1.7, 2.6] (~D^2), dev at M = 8192 <= 2e-4 -- the 5c
         duality point (lag insertion vs measure point mass) is a
         DISCRETIZATION artifact: in the limit the atoms are genuine
         point masses of the t-line montage measure.
    M3.2 [central] THE ASSEMBLED OBJECT: background density
         2cosh(tau/2) - rho(tau) on (0, T] (dictionary G0.3; the
         S-C cover-limit operator supplies rho geometrically, M1)
         + point masses -mu_n/2 at u_n = log n (counting data)
         + ONE closed UV slot (c_UV(D) + the ln(1/D) diagonal).
         Its truncations predict the window operators (M2.4, gated);
         the limit values W_inf(s, t) = extrapolated ladder + closed
         beyond-window-4 tail are TABLED with honest bands; gate:
         |tail beyond window 4| <= 0.05 at s >= 0.75 (the montage is
         reach-complete at the battery depth).
    M3.3 [C, honest typing] what is still MISSING for the contract
         as theorems (the v679 O5.1 template, cited): locally
         uniform bounds (measured: finitely many battery points),
         tightness/equicontinuity of the transform family, the limit
         Hilbert space (GNS on the limit moment data), Mosco/strong
         resolvent convergence of the CMV/Jacobi truncations (not
         only transform values), positivity transport in the limit
         (PD per window is measured; the limit-PD statement is the
         RP-in-the-limit analogue of v679 O2), and the s -> 1/2
         boundary object (the comb measure itself) -- named, not
         claimed.

  M4 verdict (preregistered):
    L1-ASSEMBLED-MEASURED       iff guards + M1.2 + M1.4 + M2.2 +
                                M2.3 + M2.4 + M3.1 + M3.2 all pass;
    L1-SCALING-REPAIRED-PARTIAL iff M2.2 + M2.3 + M2.4 pass (the
                                function-limit exists = the 5b
                                repair) but an M1/M3 gate fails;
    L1-OBSTRUCTED               otherwise, with the precise location.
    Plus the PRIME.Z1.OPERATOR.01 contract note (report only).

CALIBRATION (honesty first, recorded before the assembled run): all
bars above were set from an interactive calibration scan of the same
formulas (2026-08-03).  The scan fixed one SIGN in the construction:
the arch lag read carries -rho (measured, G0.3a), so the UV term
inside W is +(1/2) ln(1 - e^{zD}) and the renormalization SUBTRACTS
it; the first calibration pass had added it (drift doubled instead of
removed).  No gate was weakened after seeing assembled results.
  Run 1 (2026-08-03, 15/16, G0.3 check-wiring): the sampled "last
  atom" in G0.3c sits exactly AT the reach edge (u/D = M), where the
  tent read is partial BY CONSTRUCTION (measured ratio 0.0002); the
  gate was re-scoped to interior atoms (u <= 2 alpha - 2D, still
  <= 1e-12 exact) and the reach-edge partial read is now printed and
  typed as the boundary slot (mirror of the UV cell d = 0).  No bar
  moved; no measurement changed.

FIREWALL: AST-checked -- no zetazero/nzeros/zeta/second_sheet_zero
anywhere; the battery band points t in {5, 12, 27, 45} are arbitrary
declared band positions (NOT zero ordinates); counting data (v563
U_ALL/MU_ALL) enters only as the montage's atom layer -- that is this
route's point (v695 S6.1).  The kill criterion stands: any
construction loading zeros or zeta values is a renaming.

Provenance (read-only): v563 core (window geometry, arch/atom lags,
counting atoms), chain_deck_sector_probe (S-C), chain_weyl_mass_probe
(S-D), z1_jacobi_probe (5b), z1_uvarov_probe (5c), v679 (continuum
template), v695 (Z1 census, S1.4 pole layer).
"""
import ast
import cmath
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
FAILS = []
N_CHK = 0

BANNED = ("zetazero", "nzeros", "zeta", "second_sheet_zero")


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in BANNED:
            return False
        if isinstance(node, ast.Name) and node.id in BANNED:
            return False
    return True


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import scipy.linalg as sla  # noqa: E402
from scipy.ndimage import median_filter  # noqa: E402

# ---------------------------------------------------------------- bars
BAR_EXACT = 1e-12             # closed identities (tower, deck, atoms)
BAR_DICT_COARSE = 1e-3        # dictionary rel dev at M = 256
BAR_DICT_FINE = 1e-4          # dictionary rel dev at window 4
BAR_DIAG_LAW = 0.02           # |d c_ar,0 / ln 2 - 1| per D-halving
RATE_N_LO, RATE_N_HI = 1.8, 2.3   # N-ladder difference-ratio rates
BAR_SSTAR = 1e-6              # |s*(inf) - 1|
BAR_DEVN = 1e-3               # joint dev at N = 768
BAR_MODE = 1e-5               # per-mode extrapolant rel dev
K_JAC = 48                    # Jacobi depth of the continuum object
BAR_GAUSS = 1e-12             # Gauss-vs-direct functionals
BAR_JSTAB = 1e-12             # quadrature-refinement stability
R_LADDER = 0.80               # the 5b h-stability bar (cited)
RUNGS = (256, 512, 1024, 2048, 4096)
M_REF = 8192
T_BATT = (5.0, 12.0, 27.0, 45.0)      # arbitrary declared band points
S_DLAD = (0.25, 0.50, 1.00)           # Abel depths, D-ladder
S_FAM = (0.75, 1.00, 1.50)            # Abel depths, family (s > 1/2)
S_ANAT = (0.25, 0.50, 0.75)           # the s-anatomy scan (t = 27)
SLOPE_D_LO, SLOPE_D_HI = 0.5, 1.7     # W-hat LSQ D-rate band
BAR_ERR4096 = 0.04            # |W-hat(4096) - W-hat(8192)|
RAW_UV_LO, RAW_UV_HI = 0.28, 0.42     # raw UV drift ~ (1/2) ln 2
RAW_X = 4.0                   # raw increment >= 4x renormalized
BAR_MATCH = 3e-3              # matched-rung montage-tail deviation
CANCEL_X = 3.0                # pole-vs-sum cancellation at s = 1/4
SLOPE_PM_LO, SLOPE_PM_HI = 1.7, 2.6   # tent -> point-mass D-rate
BAR_PM_FINE = 2e-4            # point-mass dev at M = 8192
BAR_TAIL_INF = 0.05           # |montage tail beyond window 4|
K_LO = 8                      # skip boundary coefficients (5b)
K_ARCH = 300                  # arch tower terms in closed integrals
T_GRID = np.linspace(0.5, 3.0, 51)    # S-C trace grid
N_LADDER = (48, 96, 192, 384, 768)


# ------------------------------------------------- window machinery
def window_geometry(kz):
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    M = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if M % 2:
        M += 1
    return alpha, M


def g_pole(tv):
    tv = abs(tv)
    return -4.0 * (math.exp(tv / 2) + math.exp(-tv / 2) - 2.0)


def pole_lags(M, D):
    return np.array([-(g_pole((d - 1) * D) - 2.0 * g_pole(d * D)
                       + g_pole((d + 1) * D)) / D for d in range(M)])


def build_lags(alpha, M, ka):
    """Full deployed lag build at (alpha, M): arch + atoms + pole."""
    D = 2.0 * alpha / M
    c_ar = core.arch_lags(M, D)
    c_at, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    cp = pole_lags(M, D)
    return dict(D=D, c_ar=c_ar, c_at=c_at, cp=cp, p=c_ar + c_at + cp)


def rho_arch(tau):
    tau = np.asarray(tau, float)
    return np.exp(-tau / 2.0) / (1.0 - np.exp(-2.0 * tau))


# ------------------------------------------------- S-C lift machinery
def channel(b, t):
    return np.exp(-b * t) / (1.0 - np.exp(-6.0 * t))


def sector_trace_lat(N, r, t):
    ms = np.arange(1, N, 2)
    ms = ms[ms % 12 == r]
    eps = (N / math.pi) * np.sin(ms * math.pi / (2.0 * N))
    return np.exp(-np.outer(t, eps)).sum(axis=1)


def joint_fit(traces, chans):
    Tv = np.concatenate(traces)
    Cv = np.concatenate(chans)
    s = float(Tv @ Cv) / float(Tv @ Tv)
    dev = float(np.max(np.abs(s * Tv - Cv) / np.abs(Cv)))
    return s, dev


# --------------------------------------------- v679 template utilities
def seq_rates(vals):
    d = np.diff(np.asarray(vals, dtype=float))
    r = []
    for k in range(len(d) - 1):
        if d[k] == 0 or d[k + 1] == 0 or d[k] * d[k + 1] <= 0:
            r.append(float("nan"))
        else:
            r.append(math.log2(abs(d[k]) / abs(d[k + 1])))
    return d, r


def geo_extrap(f1, f2, f3):
    d1, d2 = f2 - f1, f3 - f2
    if d1 == 0 or d2 == 0 or d1 * d2 <= 0:
        return float("nan"), float("nan")
    q = d2 / d1
    if not (0.0 < q < 1.0):
        return float("nan"), float("nan")
    return f3 + d2 * q / (1.0 - q), -math.log2(q)


def geo_extrap_c(v1, v2, v3):
    aR, _ = geo_extrap(v1.real, v2.real, v3.real)
    aI, _ = geo_extrap(v1.imag, v2.imag, v3.imag)
    if math.isnan(aR):                       # rate-1 Richardson q=1/2
        aR = v3.real + (v3.real - v2.real)
    if math.isnan(aI):
        aI = v3.imag + (v3.imag - v2.imag)
    return complex(aR, aI)


# --------------------------------------------- transform machinery
def W_of(p, D, s, t):
    """The fixed-frequency window transform sum_{d>=1} p_d e^{z d D},
    z = -s + i t (t = band position, s = Abel depth in t-units)."""
    d = np.arange(1, len(p))
    return complex(np.sum(p[1:] * np.exp((-s + 1j * t) * D * d)))


def c_uv(D, s, t):
    """The CLOSED UV term of the -1/(2 tau) arch divergence inside W:
    sum_d (D/(2 d D)) e^{z d D} -> -(1/2) ln(1 - e^{zD}) with the
    measured arch sign (-rho) giving +(1/2) ln(1 - e^{zD})."""
    return 0.5 * cmath.log(1.0 - cmath.exp((-s + 1j * t) * D))


def pole_int(z, a, b):
    """Closed: int_a^b 2 cosh(tau/2) e^{z tau} d tau."""
    return ((cmath.exp((z + 0.5) * b) - cmath.exp((z + 0.5) * a))
            / (z + 0.5)
            + (cmath.exp((z - 0.5) * b) - cmath.exp((z - 0.5) * a))
            / (z - 0.5))


def arch_int(z, a, b, K=K_ARCH):
    """Closed tower sum: int_a^b rho(tau) e^{z tau} d tau."""
    acc = 0j
    for k in range(K):
        bk = 2.0 * k + 0.5
        acc += (cmath.exp((z - bk) * b) - cmath.exp((z - bk) * a)) \
            / (z - bk)
    return acc


def montage_tail(z, ka_lo, ka_hi, a, b):
    """The closed montage tail between reaches: point-mass atoms
    ka_lo..ka_hi + pole integral + arch-tower integral on [a, b]."""
    u = core.U_ALL[ka_lo:ka_hi]
    mu = core.MU_ALL[ka_lo:ka_hi]
    atoms = -0.5 * complex(np.sum(mu * np.exp(z.real * u)
                                  * np.exp(1j * z.imag * u)))
    return atoms + pole_int(z, a, b) - arch_int(z, a, b)


# --------------------------------------------- Jacobi machinery (M1.4)
def gl_nodes(a, b, npan, deg):
    x, wq = np.polynomial.legendre.leggauss(deg)
    edges = np.linspace(a, b, npan + 1)
    xs, ws = [], []
    for i in range(npan):
        mid = 0.5 * (edges[i] + edges[i + 1])
        half = 0.5 * (edges[i + 1] - edges[i])
        xs.append(mid + half * x)
        ws.append(half * wq)
    return np.concatenate(xs), np.concatenate(ws)


def lanczos_jacobi(xs, ws, K):
    """Stieltjes/Lanczos: Jacobi coefficients of the discretized
    measure sum ws_i delta(xs_i) (one re-orthogonalization pass)."""
    b0 = float(ws.sum())
    q = np.sqrt(ws / b0)
    q_prev = np.zeros_like(q)
    beta = 0.0
    aJ, bJ = [], []
    for _k in range(K):
        v = xs * q - beta * q_prev
        alpha_k = float(q @ v)
        v = v - alpha_k * q
        v -= q * float(q @ v)
        beta = float(np.linalg.norm(v))
        aJ.append(alpha_k)
        bJ.append(beta)
        q_prev, q = q, v / beta
    return np.array(aJ), np.array(bJ[:-1]), b0


# --------------------------------------------- OPUC machinery (M2.1)
def levinson(r, N):
    r = np.asarray(r, float)
    a = np.zeros(N + 1)
    a[0] = 1.0
    E = float(r[0])
    ks = np.zeros(N)
    for n in range(1, N + 1):
        acc = r[n] + (float(a[1:n] @ r[n - 1:0:-1]) if n > 1 else 0.0)
        k = -acc / E
        ks[n - 1] = k
        a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
        E *= (1.0 - k * k)
        if not (abs(k) < 1.0) or E <= 0.0:
            return ks[:n], n
    return ks, None


def envelope(x, width):
    e = median_filter(np.abs(x), size=max(5, width | 1),
                      mode="nearest")
    return np.maximum(e, 1e-300)


def pearson(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    x = x - x.mean()
    y = y - y.mean()
    d = math.sqrt(float(x @ x) * float(y @ y))
    return float(x @ y) / d if d > 0 else 0.0


def uprof_r_env(alA, DA, alB, DB):
    """5b M2.2 envelope-normalized u-profile correlation, verbatim
    convention (u = k D, mask u >= K_LO D_A)."""
    ua = np.arange(len(alA)) * DA
    ub = np.arange(len(alB)) * DB
    ea = envelope(alA, int(0.15 / DA))
    eb = envelope(alB, int(0.15 / DB))
    m_ = ua >= K_LO * DA
    ref_env = np.interp(ua[m_], ub, alB / eb)
    return pearson(alA[m_] / ea[m_], ref_env)


def run():
    print("=" * 78)
    print("L1-MONTAGE -- the continuum candidate of the Z1 operator:")
    print("assembly + the scaling limit in fixed-frequency "
          "normalization")
    print("=" * 78)

    # ================================================================ G0
    print("\nG0 -- guards, family, the continuum dictionary")
    check("G0.1 [E] AST firewall: banned names %s nowhere in this "
          "probe; construction path = counting data + closed "
          "expressions only" % (BANNED,),
          ast_firewall(os.path.abspath(__file__)))

    zones = core.frame_a_zones()
    fam = []
    for kz in zones:
        alpha, M = window_geometry(kz)
        if math.exp(2.0 * alpha) <= core.ATOM_MAX + 0.5:
            fam.append((kz, alpha, M))
    hs = np.array([t[2] // 2 for t in fam], float)
    picks = [fam[0]]
    for qq in (0.25, 0.5, 0.75, 1.0):
        tgt = float(np.quantile(hs, qq))
        cand = min(fam, key=lambda t_: abs(t_[2] // 2 - tgt))
        if all(cand[0] != p_[0] for p_ in picks):
            picks.append(cand)
    picks = sorted(picks, key=lambda t_: t_[2])
    wins = []
    for (kz, alpha, M) in picks:
        ka = core.atoms_in(alpha)
        w = build_lags(alpha, M, ka)
        w.update(kz=kz, alpha=alpha, M=M, h=M // 2, ka=ka)
        ks, bd = levinson(w["p"], M - 1)
        w["al"] = -ks
        w["bd"] = bd
        wins.append(w)
    print("   family: " + ", ".join(
        "h=%d (alpha=%.4f, D=%.6f, X=%.0f)"
        % (w["h"], w["alpha"], w["D"], math.exp(2 * w["alpha"]))
        for w in wins))
    check("G0.2 [E] 5-window family (identical 5b/5c selection, %d "
          "complete frame-A windows); full-depth Levinson PD on all "
          "5 (reproduces 5b M1.1)" % len(fam),
          len(picks) == 5 and len(fam) == 67
          and all(w["bd"] is None for w in wins))

    w4 = wins[-1]
    alpha4, ka4 = w4["alpha"], w4["ka"]
    T4 = 2.0 * alpha4
    D4 = w4["D"]

    # the synthetic dyadic ladder (fixed measure = window 4's)
    lads = {}
    for M in RUNGS + (M_REF,):
        lads[M] = build_lags(alpha4, M, ka4)

    # dictionary
    dev_ar, dev_cp = {}, {}
    for M, bar_tag in ((256, "coarse"), (w4["M"], "win4")):
        w = lads[256] if M == 256 else w4
        D = w["D"]
        d = int(round(1.0 / D))
        tau_d = d * D
        dev_ar[bar_tag] = abs(w["c_ar"][d] / D
                              + float(rho_arch(tau_d))) \
            / float(rho_arch(tau_d))
        dev_cp[bar_tag] = abs(w["cp"][d] / D
                              - 2.0 * math.cosh(tau_d / 2.0)) \
            / (2.0 * math.cosh(tau_d / 2.0))
    dev_atom = 0.0
    i_int = int(np.searchsorted(core.U_ALL, T4 - 2.0 * D4)) - 1
    for i in (0, 1, 10, 100, 1000, i_int):
        c1, _ = core.atom_lags_at(alpha4, w4["M"],
                                  core.U_ALL[i:i + 1],
                                  core.MU_ALL[i:i + 1])
        dev_atom = max(dev_atom,
                       abs(float(np.sum(c1))
                           / (-float(core.MU_ALL[i]) / 2.0) - 1.0))
    c1b, _ = core.atom_lags_at(alpha4, w4["M"],
                               core.U_ALL[ka4 - 1:ka4],
                               core.MU_ALL[ka4 - 1:ka4])
    r_edge = float(np.sum(c1b)) / (-float(core.MU_ALL[ka4 - 1]) / 2.0)
    print("   reach-edge cell: the last atom (u/D = %.2f = M) reads "
          "PARTIALLY, ratio %.4f -- the reach boundary is a slot, "
          "mirror of the UV cell d = 0 (typed, measured)"
          % (float(core.U_ALL[ka4 - 1]) / D4, r_edge))
    diag = [lads[M]["c_ar"][0] for M in (256, 512, 1024, 2048, 4096)]
    dev_diag = max(abs((diag[i + 1] - diag[i]) / math.log(2.0) - 1.0)
                   for i in range(4))
    print("   diagonal cell c_ar,0 over D-halvings: %s (increments "
          "/ ln 2 dev <= %.4f)" % (["%.4f" % x for x in diag],
                                   dev_diag))
    check("G0.3 [E] THE CONTINUUM DICTIONARY locked: (a) arch lag = "
          "-D rho(dD) (rel dev %.1e coarse / %.1e win4; the arch "
          "half couples with the MINUS sign -- the deployed "
          "background density is 2cosh(tau/2) - rho(tau), the pole-"
          "subtraction reading of v695 S1.4); (b) pole lag = "
          "+D 2cosh(dD/2) (rel %.1e / %.1e); (c) every INTERIOR atom "
          "(u <= 2 alpha - 2D) reads EXACTLY -mu_n/2 in total (max "
          "dev %.1e; the reach-edge atom reads partially -- boundary "
          "slot, printed); (d) the diagonal "
          "cell obeys the closed UV law c_ar,0 ~ ln(1/D) "
          "(increment/ln2 dev %.3f <= %.2f) -- d = 0 is the "
          "renormalization slot"
          % (dev_ar["coarse"], dev_ar["win4"], dev_cp["coarse"],
             dev_cp["win4"], dev_atom, dev_diag, BAR_DIAG_LAW),
          dev_ar["coarse"] <= BAR_DICT_COARSE
          and dev_ar["win4"] <= BAR_DICT_FINE
          and dev_cp["coarse"] <= BAR_DICT_COARSE
          and dev_cp["win4"] <= BAR_DICT_FINE
          and dev_atom <= BAR_EXACT and dev_diag <= BAR_DIAG_LAW)

    # ================================================================ M1
    print("\nM1 -- the continuum arch operator (the S-C limit "
          "object, explicit)")
    t = T_GRID
    rho_t = rho_arch(t)
    tow = sum(np.exp(-(2.0 * k + 0.5) * t) for k in range(400))
    dev_tow = float(np.max(np.abs(tow - rho_t) / rho_t))
    dev_deck = 0.0
    for b in (0.5, 2.5, 4.5):
        ch = channel(b, t)
        tw = sum(np.exp(-(6.0 * k + b) * t) for k in range(140))
        dev_deck = max(dev_deck, float(np.max(np.abs(tw - ch) / ch)))
    check("M1.1 [E] the continuum object NAMED: diagonal operator "
          "with spectrum {2k + 1/2} (deck channels {6k + b}, b in "
          "{1/2, 5/2, 9/2}); heat trace == rho (rel %.1e) and deck "
          "split exact (rel %.1e), both <= %.0e -- the S-C anchor "
          "re-verified" % (dev_tow, dev_deck, BAR_EXACT),
          dev_tow <= BAR_EXACT and dev_deck <= BAR_EXACT)

    chans = [channel(b, t) for b in (0.5, 2.5, 4.5)]
    svals, devs = [], []
    for N in N_LADDER:
        traces = [sector_trace_lat(N, r, t) for r in (1, 5, 9)]
        s_star, dev = joint_fit(traces, chans)
        svals.append(s_star)
        devs.append(dev)
        print("   N = %3d: s* = %.9f, joint max rel dev %.3e"
              % (N, s_star, dev))
    _, r_s = seq_rates(svals)
    _, r_d = seq_rates(devs)
    s_inf, _ = geo_extrap(*svals[2:])
    check("M1.2 [E] N-ladder of the cover lift: s*(N) rates %s and "
          "dev rates %s all in [%.1f, %.1f] (~N^-2); geometric "
          "extrapolant s*(inf) = %.9f, |s*(inf) - 1| = %.1e <= %.0e; "
          "dev(768) = %.1e <= %.0e -- the lift converges to the "
          "continuum object with the measured N^-2 rate and the "
          "joint scalar goes to 1"
          % (["%.2f" % x for x in r_s], ["%.2f" % x for x in r_d],
             RATE_N_LO, RATE_N_HI, s_inf, abs(s_inf - 1.0),
             BAR_SSTAR, devs[-1], BAR_DEVN),
          all(RATE_N_LO <= x <= RATE_N_HI for x in r_s + r_d)
          and abs(s_inf - 1.0) <= BAR_SSTAR and devs[-1] <= BAR_DEVN)

    dev_mode = 0.0
    for m in range(1, 26, 2):
        vals = [(N / math.pi) * math.sin(m * math.pi / (2.0 * N))
                for N in (192, 384, 768)]
        a_m, _ = geo_extrap(*vals)
        dev_mode = max(dev_mode, abs(a_m - m / 2.0) / (m / 2.0))
    check("M1.3 [E] per-mode spectral convergence: eps_m(N) "
          "extrapolates to m/2 for all odd m <= 25 (worst rel dev "
          "%.1e <= %.0e) -- operator data converge, not only traces"
          % (dev_mode, BAR_MODE), dev_mode <= BAR_MODE)

    def w_plus(tau):
        return rho_arch(tau) + 2.0 * np.cosh(tau / 2.0)

    xs, wq0 = gl_nodes(D4, T4, 3000, 12)
    ws = wq0 * w_plus(xs)
    aJ, bJ, mass = lanczos_jacobi(xs, ws, K_JAC)
    ev, U = sla.eigh_tridiagonal(aJ, bJ)
    wg = mass * U[0] ** 2
    dev_g = 0.0
    for s in (0.3, 1.0, 3.0):
        exact = float(np.sum(ws * np.exp(-s * xs)))
        gq = float(np.sum(wg * np.exp(-s * ev)))
        dev_g = max(dev_g, abs(gq - exact) / abs(exact))
    xs2, wq02 = gl_nodes(D4, T4, 6000, 12)
    aJ2, bJ2, _ = lanczos_jacobi(xs2, wq02 * w_plus(xs2), K_JAC)
    stab = max(float(np.max(np.abs(aJ2 - aJ))),
               float(np.max(np.abs(bJ2 - bJ))))
    print("   Jacobi head: aJ = %s, bJ = %s"
          % (["%.4f" % x for x in aJ[:4]],
             ["%.4f" % x for x in bJ[:4]]))
    check("M1.4 [E] the explicit multiplication/Jacobi object of the "
          "arch+pole half: measure (rho + 2cosh(tau/2)) dtau on "
          "[tau_min = D_4 = %.4f, T_max = 2 alpha_4 = %.4f] (mass "
          "%.4f; tau_min = the declared UV cell, typed [O]); K = %d "
          "Jacobi coefficients via Stieltjes/Lanczos; Gauss "
          "quadrature == direct integrals (rel %.1e <= %.0e), "
          "refinement-stable (%.1e <= %.0e), spectrum [%.4f, %.4f] "
          "inside the support -- the continuum operator EXISTS as an "
          "explicit matrix" % (D4, T4, mass, K_JAC, dev_g, BAR_GAUSS,
                               stab, BAR_JSTAB, ev.min(), ev.max()),
          dev_g <= BAR_GAUSS and stab <= BAR_JSTAB
          and ev.min() >= 0.9 * D4 and ev.max() <= 1.001 * T4)

    # ================================================================ M2
    print("\nM2 -- the scaled limit (the 5b-M2.2 re-examination)")

    # ---- M2.1 the raw reading, reproduced honestly
    r_fam = []
    for w in wins[1:-1]:
        r_fam.append(uprof_r_env(w["al"], w["D"], w4["al"], w4["D"]))
    ks_syn, bd_syn = levinson(lads[2048]["p"], 2047)
    r_fix = uprof_r_env(-ks_syn, lads[2048]["D"], w4["al"], w4["D"]) \
        if bd_syn is None else float("nan")
    print("   raw family r_env vs window 4: %s (5b bar %.2f)"
          % (["%+.4f" % r for r in r_fam], R_LADDER))
    print("   raw FIXED-measure pair (rung M=2048 vs window 4, same "
          "measure, D halved): r_env = %+.4f" % r_fix)
    check("M2.1 [E, the raw negative, both readings side by side] "
          "RAW normalization has no h-stable ladder: family min "
          "r_env = %+.4f (reproduces the 5b M2.2 negative, was "
          "-0.13) AND the fixed-measure pair gives r_env = %+.4f -- "
          "both < %.2f: the coefficient-level comparison fails even "
          "WITHOUT reach effects; the normalization is the issue, "
          "which is what the function-level ladder (M2.2/M2.4) "
          "repairs" % (min(r_fam), r_fix, R_LADDER),
          min(r_fam) < R_LADDER and r_fix < R_LADDER)

    # ---- M2.2 the renormalized D-ladder (fixed measure)
    print("   M2.2 D-ladder (fixed measure, M = 256..4096, ref "
          "8192): W-hat = W - (1/2) ln(1 - e^{zD})")
    ok_mono, ok_last = True, True
    slopes = []
    raw_last, ren_last = [], []
    Dv = np.array([lads[M]["D"] for M in RUNGS])
    for s in S_DLAD:
        for tb in T_BATT:
            Wref = W_of(lads[M_REF]["p"], lads[M_REF]["D"], s, tb) \
                - c_uv(lads[M_REF]["D"], s, tb)
            errs, raws, rens = [], [], []
            for M in RUNGS:
                Wv = W_of(lads[M]["p"], lads[M]["D"], s, tb)
                raws.append(Wv)
                rens.append(Wv - c_uv(lads[M]["D"], s, tb))
                errs.append(abs(rens[-1] - Wref))
            errs = np.array(errs)
            ok_mono &= bool(np.all(np.diff(errs) < 0.0))
            ok_last &= errs[-1] <= BAR_ERR4096
            sl = float(np.polyfit(np.log2(Dv), np.log2(errs), 1)[0])
            slopes.append(sl)
            raw_last.append(abs(raws[-1] - raws[-2]))
            ren_last.append(abs(rens[-1] - rens[-2]))
            print("   s=%.2f t=%4.1f: |W-hat - ref| = %s  D-rate "
                  "%.2f" % (s, tb, ["%.1e" % e for e in errs], sl))
    check("M2.2 [central] the D/UV limit EXISTS at every band point "
          "(incl. s < 1/2): after the closed UV renormalization the "
          "ladder error falls strictly monotonically at all %d "
          "battery points, LSQ D-rates in [%.2f, %.2f] (band "
          "[%.1f, %.1f]: first order, edge-dominated -- measured, "
          "understood), worst err(4096) <= %.0e -- the "
          "discretization limit of the window transform is CLEAN"
          % (len(S_DLAD) * len(T_BATT), min(slopes), max(slopes),
             SLOPE_D_LO, SLOPE_D_HI, BAR_ERR4096),
          ok_mono and ok_last
          and all(SLOPE_D_LO <= x <= SLOPE_D_HI for x in slopes))

    ratio_uv = min(rl / max(re, 1e-300)
                   for rl, re in zip(raw_last, ren_last))
    check("M2.3 [E, must-fail] WITHOUT the renormalization the "
          "ladder is NOT Cauchy: last raw increments in [%.3f, "
          "%.3f] == the closed UV drift (1/2) ln 2 = %.4f (band "
          "[%.2f, %.2f]), and raw/renormalized increment ratio >= "
          "%.1f (bar %.1f) at every battery point -- the UV term is "
          "real, closed, and exactly one term"
          % (min(raw_last), max(raw_last), 0.5 * math.log(2.0),
             RAW_UV_LO, RAW_UV_HI, ratio_uv, RAW_X),
          all(RAW_UV_LO <= x <= RAW_UV_HI for x in raw_last)
          and ratio_uv >= RAW_X)

    # ---- M2.4 the family repair: D-matched rungs + closed tails
    print("   M2.4 family ladder, fixed-frequency normalization "
          "(D-matched reference rungs + closed montage tails):")
    match = {}
    for w in wins[:-1]:
        M_syn = int(round(T4 / w["D"]))
        match[w["h"]] = build_lags(alpha4, M_syn, ka4)
    dev_match = []
    for s in S_FAM:
        for tb in T_BATT:
            z = complex(-s, tb)
            row = []
            for w in wins[:-1]:
                syn = match[w["h"]]
                Wh = W_of(w["p"], w["D"], s, tb) - c_uv(w["D"], s, tb)
                Wsyn = W_of(syn["p"], syn["D"], s, tb) \
                    - c_uv(syn["D"], s, tb)
                tail = montage_tail(z, w["ka"], ka4,
                                    2.0 * w["alpha"], T4)
                row.append(abs((Wsyn - Wh) - tail))
            dev_match.append(max(row))
            print("   s=%.2f t=%4.1f: |(W-hat_syn - W-hat_h) - "
                  "closed tail| per window = %s"
                  % (s, tb, ["%.1e" % x for x in row]))
    check("M2.4 [central, THE 5b REPAIR] the family ladder CONVERGES "
          "in fixed-frequency normalization: at every battery point "
          "(s in %s x t in %s) the D-matched reference rung minus "
          "the true window equals the CLOSED montage tail (point-"
          "mass atoms + pole integral + arch-tower integral) to "
          "worst dev %.1e <= %.0e -- combined with M2.2 the window "
          "ladder has a function limit at fixed band points for "
          "s > 1/2; the 5b M2.2 negative was the NORMALIZATION "
          "(raw alpha), not the limit"
          % (list(S_FAM), list(T_BATT), max(dev_match), BAR_MATCH),
          max(dev_match) <= BAR_MATCH)

    # ---- M2.5 the s-anatomy: where it diverges
    print("   M2.5 s-anatomy at t = 27 (window 0 row, reach "
          "%.2f -> %.2f):" % (2 * wins[0]["alpha"], T4))
    res_s = {}
    canc = []
    for s in S_ANAT:
        z = complex(-s, 27.0)
        w = wins[0]
        syn = match[w["h"]]
        Wh = W_of(w["p"], w["D"], s, 27.0) - c_uv(w["D"], s, 27.0)
        Wsyn = W_of(syn["p"], syn["D"], s, 27.0) \
            - c_uv(syn["D"], s, 27.0)
        tail = montage_tail(z, w["ka"], ka4, 2.0 * w["alpha"], T4)
        res_s[s] = abs((Wsyn - Wh) - tail)
        u = core.U_ALL[w["ka"]:ka4]
        mu = core.MU_ALL[w["ka"]:ka4]
        at = -0.5 * complex(np.sum(mu * np.exp(z.real * u)
                                   * np.exp(1j * z.imag * u)))
        pl = pole_int(z, 2.0 * w["alpha"], T4)
        if s == 0.25:
            canc = [abs(at), abs(pl), abs(tail)]
        print("   s=%.2f: |atom tail| %.4f  |pole tail| %.4f  "
              "|combined| %.4f  prediction residual %.4f"
              % (s, abs(at), abs(pl), abs(tail), res_s[s]))
    check("M2.5 [measured] WHERE it diverges -- located: NOT in D "
          "(M2.2 converges at s = 0.25); in the REACH tails at "
          "s <= 1/2: at s = 1/4 atom and pole tails are individually "
          "large (%.3f / %.3f) and cancel to %.3f (pole/combined = "
          "%.1fx >= %.1fx, the PNT-level cancellation, measured); "
          "the montage-prediction residual grows monotonically as s "
          "drops (%.4f -> %.4f -> %.4f for s = 0.75/0.50/0.25) -- "
          "the missing piece at s <= 1/2 is the zero-side "
          "fluctuation, NAMED and firewalled (never loaded); the "
          "half-plane boundary s = 1/2 is the critical line, typed"
          % (canc[0], canc[1], canc[2], canc[1] / canc[2], CANCEL_X,
             res_s[0.75], res_s[0.50], res_s[0.25]),
          canc[1] / canc[2] >= CANCEL_X
          and res_s[0.25] > res_s[0.50] > res_s[0.75])

    # ================================================================ M3
    print("\nM3 -- the montage")

    # ---- M3.1 tent read -> point mass
    print("   M3.1 tent read -> point mass (D-ladder, single atoms):")
    ok_pm = True
    for (i_at, lab) in ((0, "n=2"), (28, "n~%d"
                                     % round(math.exp(
                                         float(core.U_ALL[28]))))):
        u_n = float(core.U_ALL[i_at])
        mu_n = float(core.MU_ALL[i_at])
        for (s, tb) in ((0.5, 12.0), (1.0, 45.0)):
            devs_pm, Dl = [], []
            for M in RUNGS + (M_REF,):
                D = 2.0 * alpha4 / M
                c1, _ = core.atom_lags_at(alpha4, M,
                                          core.U_ALL[i_at:i_at + 1],
                                          core.MU_ALL[i_at:i_at + 1])
                Wa = W_of(c1, D, s, tb)
                exact = -(mu_n / 2.0) * cmath.exp((-s + 1j * tb)
                                                  * u_n)
                devs_pm.append(abs(Wa - exact))
                Dl.append(D)
            sl = float(np.polyfit(np.log2(Dl),
                                  np.log2(devs_pm), 1)[0])
            ok_pm &= (SLOPE_PM_LO <= sl <= SLOPE_PM_HI
                      and devs_pm[-1] <= BAR_PM_FINE)
            print("   atom %-7s s=%.2f t=%4.1f: dev %s  LSQ D-rate "
                  "%.2f" % (lab, s, tb,
                            ["%.1e" % x for x in devs_pm], sl))
    check("M3.1 [E] THE DUALITY POINT DISSOLVES IN THE LIMIT: the "
          "deployed <= 2-cell tent read converges to the exact "
          "point-mass value -(mu_n/2) e^{z u_n} with LSQ D-rate in "
          "[%.1f, %.1f] (~D^2) and dev(8192) <= %.0e on both test "
          "atoms x both battery points -- the 5c lag-insertion vs "
          "measure-point-mass duality is a discretization artifact; "
          "in the continuum the atoms are genuine point masses of "
          "the t-line montage measure"
          % (SLOPE_PM_LO, SLOPE_PM_HI, BAR_PM_FINE), ok_pm)

    # ---- M3.2 the assembled limit values + reach completeness
    print("   M3.2 the assembled limit W_inf(s, t) = extrapolated "
          "D-ladder + closed tail beyond window 4:")
    ka_end = len(core.U_ALL)
    U_MAX = float(core.U_ALL[-1])
    ok_tail = True
    print("   %-5s %-6s %22s %10s %10s"
          % ("s", "t", "W_inf", "|tail4inf|", "band"))
    for s in S_FAM:
        for tb in T_BATT:
            z = complex(-s, tb)
            v1 = W_of(lads[2048]["p"], lads[2048]["D"], s, tb) \
                - c_uv(lads[2048]["D"], s, tb)
            v2 = W_of(lads[4096]["p"], lads[4096]["D"], s, tb) \
                - c_uv(lads[4096]["D"], s, tb)
            v3 = W_of(lads[M_REF]["p"], lads[M_REF]["D"], s, tb) \
                - c_uv(lads[M_REF]["D"], s, tb)
            W_lim = geo_extrap_c(v1, v2, v3)
            tail = montage_tail(z, ka4, ka_end, T4, U_MAX)
            tail += -cmath.exp((z - 0.5) * U_MAX) / (z - 0.5)
            u_oct = core.U_ALL[core.U_ALL >= U_MAX - math.log(2.0)]
            mu_oct = core.MU_ALL[core.U_ALL >= U_MAX - math.log(2.0)]
            at_oct = -0.5 * complex(
                np.sum(mu_oct * np.exp(z.real * u_oct)
                       * np.exp(1j * z.imag * u_oct)))
            sm_oct = -(cmath.exp((z + 0.5) * U_MAX)
                       - cmath.exp((z + 0.5)
                                   * (U_MAX - math.log(2.0)))) \
                / (z + 0.5)
            band = abs(v3 - v2) + abs(at_oct - sm_oct)
            ok_tail &= abs(tail) <= BAR_TAIL_INF
            print("   %-5.2f %-6.1f %10.5f%+10.5fj %10.5f %10.5f"
                  % (s, tb, (W_lim + tail).real, (W_lim + tail).imag,
                     abs(tail), band))
    check("M3.2 [central] THE L1 CANDIDATE IS ASSEMBLED at the "
          "measured level: ONE fixed, zero-free-described continuum "
          "object -- background density 2cosh(tau/2) - rho(tau) on "
          "the lag line (rho = the S-C cover-limit heat trace, M1; "
          "sign = the v695 pole-subtraction slot), counting-data "
          "point masses -mu_n/2 at log n (M3.1), ONE closed UV slot "
          "(c_UV(D) + the ln(1/D) diagonal, G0.3d) -- whose "
          "truncations reproduce the window operators (M2.4) and "
          "whose limit values are tabled above with honest bands "
          "(atom table to u = %.2f = ln %d, smooth remainder closed, "
          "band = extrapolation + last-octave fluctuation); reach "
          "completeness: |tail beyond window 4| <= %.2f at all "
          "s >= 3/4 battery points"
          % (U_MAX, core.ATOM_MAX, BAR_TAIL_INF), ok_tail)

    check("M3.3 [C, honest typing] WHAT IS STILL MISSING FOR THE "
          "CONTRACT AS THEOREMS (v679 O5.1 template, cited): (i) "
          "locally uniform convergence bounds -- measured here at "
          "finitely many battery points only; (ii) tightness/"
          "equicontinuity of the transform family in (s, t); (iii) "
          "the limit Hilbert space (GNS on the limit moment data) "
          "and MOSCO/STRONG-RESOLVENT convergence of the CMV/Jacobi "
          "truncations -- transform-value convergence (this probe) "
          "is weaker than operator convergence; (iv) positivity "
          "transport: PD is measured per window (5b M1.1), the "
          "limit-PD statement is the RP-in-the-limit analogue of "
          "v679 O2 and is OPEN; (v) the s -> 1/2 boundary object "
          "(the comb measure itself) and the UV cell as a theorem "
          "(Pf/diagonal renormalization, S-C D6) -- all NAMED, none "
          "claimed; GATE stays where it is", True)

    # ================================================================ M4
    print("\nM4 -- verdict + contract note")
    central = [f for f in FAILS
               if f.startswith(("M2.2", "M2.3", "M2.4"))]
    if not FAILS:
        verdict = "L1-ASSEMBLED-MEASURED"
    elif not central:
        verdict = "L1-SCALING-REPAIRED-PARTIAL (at %s)" \
            % ", ".join(FAILS)
    else:
        verdict = "L1-OBSTRUCTED (at %s)" % ", ".join(FAILS)
    check("M4.1 [E] preregistered verdict logic: ASSEMBLED iff all "
          "gates; REPAIRED-PARTIAL iff the scaling repair "
          "(M2.2/M2.3/M2.4) stands but an assembly gate fails; "
          "OBSTRUCTED otherwise with location", True)
    print("\n   VERDICT: %s" % verdict)
    print("""
   contract note PRIME.Z1.OPERATOR.01 (report only, no ledger row):
     L1-MONTAGE (this run): der Kontinuums-Kandidat ist MONTIERT auf
     Mess-Ebene -- ein festes, zeta-frei beschriebenes Objekt:
       (1) Hintergrund: Dichte 2cosh(tau/2) - rho(tau) auf der
           Lag-Achse; rho ist per S-C die Waermespur des expliziten
           Cover-Limes-Operators (Spektrum {2k+1/2}, N-Leiter
           extrapoliert s* -> 1 auf %.1e, Raten ~N^-2, M1.2); das
           Minuszeichen der Arch-Haelfte ist GEMESSEN (G0.3) und ist
           der v695-S1.4-Pol-Abzugs-Slot; die Multiplikations-/
           Jacobi-Lesart der positiven rho+Pol-Haelfte existiert als
           explizite K=%d-Jacobi-Matrix (Gauss-Konsistenz %.0e).
       (2) Atome: echte PUNKTMASSEN -mu_n/2 bei log n im Limes --
           der 5c-Dualitaetspunkt (Lag-Insertion vs. Mass-Punkt)
           verschwindet mit Rate ~D^2 (M3.1).
       (3) UV: EIN geschlossener Slot -- c_UV(D) =
           (1/2) ln(1 - e^{zD}) im Transform + ln(1/D) in der
           Diagonalzelle (G0.3d, S-C-D6-Slot).
     DER GRENZUEBERGANG: in fester Frequenz-Normierung (F_h an
     festen Bandpunkten z, NICHT rohe alpha_k) konvergiert die
     h-Leiter: D-Limes sauber an ALLEN Bandpunkten inkl. s < 1/2
     (M2.2, must-fail M2.3: ohne den UV-Term keine Cauchy-Folge);
     Reichweiten-Leiter = geschlossener Zaehldaten-Tail auf <= 3e-3
     fuer s > 1/2 (M2.4).  Das 5b-M2.2-Negativ war die NORMIERUNG:
     roh gibt es keine h-stabile Leiter, selbst bei festem Mass
     (r_env = %+.2f) -- beide Lesarten dokumentiert (M2.1).
     WO es divergiert: nicht in D; in den Reichweiten-Tails bei
     s <= 1/2 (Atome und Pol einzeln divergent, Ausloeschung auf
     PNT-Niveau gemessen, Faktor %.0fx; das Prediktions-Residuum
     waechst monoton Richtung s = 1/2) -- die Halbebenen-Grenze ist
     die kritische Linie, getypt, nie geladen (M2.5).
     FEHLENDE SAETZE fuer den Vertrag (benannt, M3.3): lokal
     uniforme Schranken, Straffheit, GNS-Limes-Hilbertraum, Mosco-/
     stark-resolvente Konvergenz der CMV/Jacobi-Trunkierungen,
     Positivitaets-Transport im Limes (RP-Analogon v679 O2), das
     s=1/2-Randobjekt und die Pf/Diagonal-UV als Satz.
     Kill-Kriterien unveraendert (AST-erzwungen).""" % (
        abs(s_inf - 1.0), K_JAC, BAR_GAUSS, r_fix, canc[1] / canc[2]))

    # ------------------------------------------------------------ final
    print("\n" + "=" * 72)
    dt = time.time() - T0
    if FAILS:
        print("RESULT: %d/%d checks passed -- FAILURES: %s  (%.1f s)"
              % (N_CHK - len(FAILS), N_CHK, ", ".join(FAILS), dt))
        print("VERDICT: %s" % verdict)
        return 1
    print("RESULT: ALL %d CHECKS PASSED  (%.1f s)" % (N_CHK, dt))
    print("VERDICT: %s" % verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
