#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""source_weyl_energy_probe -- PRIME.SOURCE.WEYL_ENERGY.THEOREM.01
(round 399): the source-pure Weyl energy of the centered
mass difference, after DCCLXII 5.2/5.3 and the r398 KILL_FAIL.

Coexistence: r389 Chebyshev energy + grid Parseval; r390
Bernstein-Szego Fejer background; r392 Uvarov tau; r393
rank-1 Delta^2 log tau (coupling 31 pct); r394 Dirichlet
zones.  r398: a macroscopic cluster of R_{N-3} sits at 1/2
from above -- the cheap high-moment kill is dead, the route
runs through this energy.

THE FROZEN QUESTION.  After subtracting the explicit
Bernstein-Szego / arch background and splitting three
source-defined edge modes, does
  E_k^bulk = Sum_{r not edge} omega_{k,r} |dhat_k(r)|^2
tend to 0 in the CD-transfer norm that is supposed to
control the bulk operator and the 3x3 edge block?
Forbidden inputs: lambda_min(R^dagger), det M^dagger, q_N,
any measured margin.

LEGS (lemma-first; exits PROVED / REFUTED / REDUZIERT /
ZIRKULAER):
  A  Exact Fourier-Dirichlet representation of dhat on the
     prime side: tent interpolant + even-circulant + Fejer
     Laplacian, plus explicit arch/Gamma/pole as d^ref.
     Transfer weights omega from r389 CD (which weighted
     dhat-energy controls Delta^2 log tau / mu-OP Gram?).
  B  Source-pure edge split (mass r=0, fold r=1, cap
     Nyquist); E^bulk on a_k=2^k (as far as the Lambda
     table) and core-42: does it fall?
  C  Analytic attack: dyadic / Montgomery-Vaughan MVT /
     Gallagher on the grid t_{k,r}; prime powers >=2
     absolute.  Honesty gate: every block typed
     unconditional / PNT / RH-near.
  D  Kills: scramble, two-period comb, mutant omega=1 /
     no edge split, dead chi.

CALIBRATION DISCLOSURE.  Identities, w9 / kz18 / kz52
Dirichlet residuals, CD energies, selected a_k=2^k,
core-42 slopes, assist correlation, scramble / two-period
/ chi, MVT ratios were first measured in /tmp (r399_cal.py,
r399_cal2.py) on the same constructors, 2026-08-29.  Frozen
floors below are that measurement, sealed as gates -- not a
search over 1/2.  No two-commit pre-blind freeze: pins
disclosed.  Builder fallback NOT taken: full census wall
< 3 s (bar 120 s) on core-42 + selected k=2..9 + chi.

FROZEN FROM /tmp (live re-gated, not fitted):
  * dcent = Fejer odot d^P on the folded grid, w9 maxdev
    2.8e-17.  Dirichlet interpolant
    dP[j] = -Sum_n Lambda(n) n^{-1/2} K_j(log n) matches
    spectral_density at maxdev 7e-15 (w9 j=1), 2.5e-13
    (j=183); kz18 5.7e-14; kz52 2.8e-13.
  * IFFT(Fejer odot dP) = Delta_circ(cP_ext)/L, w9 maxdev
    8.7e-19.  Stencil over Q: h_0=2/L, h_{pm 1}=-1/L.
  * Folded C_m = (1/2) unfolded cosine transform, maxdev
    2.1e-14.  C_0=C_1=0 at machine zero (Fejer kills mass
    and the fold fundamental); Nyquist lies outside the
    CD band k=N_w-3, so E^bulk = E already.
  * Transfer omega_m = 1/pi (m=0), 2/pi (1<=m<N_w-3):
    the r389 Chebyshev-CD energy of centered d.
    w9 E=1.80686, mean C^2/qm=0.619, qm=0.02547,
    Cmax=0.583 at m=129.  corr(E/Nw, assist)=0.18
    (does NOT dominate); corr(E, assist)=-0.78 is the
    N-confound.
  * Core-42: E^bulk in [1.178, 5.983], slope d log E /
    d log N_w = +0.542 (GROWS); E/Nw slope -0.458;
    mean C^2/qm in [0.427, 0.848] -- quadratic-mean,
    same class as r389 nu-angles.
  * Selected a_k=2^k (Lean r397: m_k=k 2^{floor sqrt k}-1,
    n<=a^2, table cap k<=9): E^bulk 0.033, 0.191, 0.384,
    0.402, 0.508, 0.536, 0.869 for k=3..9 -- not monotone
    to 0.  k=2 is all-edge (E^bulk=0).
  * MVT (Montgomery-Vaughan quality (T+X) Sum a_n^2):
    w9 X/T=1.23, crude/E ~ 10^3 -- 10^4; kz82 X/T=345,
    crude/E ~ 10^6.  Unconditional large sieve does not
    close.  Sub-QM decay would be RH-near AND contradicts
    the QM census.
  * Scramble seed=1: E^bulk=3.40 > MAIN 1.81 (separates:
    centered d sees the log-n cancellation, scramble
    does not).  Two-period S=21 cosine grid: HHI=0.629,
    comb at m=S -- concentrating adversary.  Dead chi3-15
    E=1.69 vs living chi3-9 E=1.47 vs MAIN 1.81: not a
    world separator.  Mutant omega=1 (no 2/pi, no CD
    cutoff) is a different scale; drop-edge does not
    change CD energy (edge already out).
  * Prime-power k>=2 lag L2 ratio vs primes 0.23 on w9
    (finite-window); the series Sum_{k>=2} p^{-k/2} log p
    is absolutely convergent.

AUSGANG REFUTED (the decay E^bulk -> 0 at the CD-transfer
norm).  SATZ: the Fourier-Dirichlet representation, the
Fejer Laplacian, C_0=C_1=0, the r389 transfer weights as
the named CD energy of centered d.  The energy sits at
quadratic-mean and GROWS like N_w^{0.54} on core-42.
Honesty gate: every block that could force ->0 is RH-near
(ZIRKULAER as a closing strategy for R^dagger > 1/2 I);
the unconditional MVT is 10^3-10^6 short; the census
refutes decay independently of that circularity.
No RH claim.  No L* claim.  No R-dagger claim.

MACHINERY: r226/r283 V.build_measures / prime_lags /
arch_lags / spectral_density, r357 DMF chi lags, r389
Chebyshev-CD energy, r390 Fejer Bernstein-Szego, r397
selected sequence a_k=2^k.

NO RH CLAIM.  Finite identities, a named refutation of
the decay, a named honesty-gate.  Research documentation,
not a theorem of RH.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import verify_lstar_instance as V  # noqa: E402
import dirichlet_matched_frame_probe as DMF  # noqa: E402

PI = math.pi
SCR_SEED = 1
MAIN_KZ = 9
CORE_N = 42
DEAD_CHI3 = 15
ID_BAR = 1.0e-12
DIR_BAR = 1.0e-10
LAP_BAR = 1.0e-12

W9_E_LO, W9_E_HI = 1.70, 1.92
W9_QM_LO, W9_QM_HI = 0.50, 0.75
CORE_E_LO, CORE_E_HI = 1.00, 7.00
CORE_SLOPE_LO = 0.30
SEL_K9_E_LO, SEL_K9_E_HI = 0.50, 1.50
SCR_RATIO = 1.20
TP_HHI_FLOOR = 0.50
MVT_RATIO_FLOOR = 100.0
CORR_ABS_HI = 0.45
PP_RATIO_HI = 0.50
CHI_E_LO, CHI_E_HI = 0.80, 3.00

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-44s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return bool(ok)


def section(t):
    print("\n" + "=" * 78)
    print(t)
    print("=" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "gram" + "point",
            "prime" + "range"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero oracles; von Mangoldt sieve / "
                       "tent / Fejer / CD energy only"
                       if not bad else "; ".join(bad))


def energy_fn_audit():
    """E_bulk must not consume lambda_min(R), det M, q_N, margins."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    target = None
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "cd_energy_of":
            target = node
            break
    if target is None:
        return False, "cd_energy_of missing"
    names = set()
    for n in ast.walk(target):
        if isinstance(n, ast.Name):
            names.add(n.id.lower())
        if isinstance(n, ast.Attribute):
            names.add(n.attr.lower())
    banned = {"eigvalsh", "eigh", "det", "q_n", "qn", "margin",
              "lambda_min", "lmin"}
    hit = sorted(names & banned)
    return (not hit), ("energy path source-pure"
                       if not hit else "banned: " + ",".join(hit))


# ---- exact constructors -------------------------------------------------

def even_extend(c):
    c = np.asarray(c, float)
    return np.concatenate([c, c[-2:0:-1]])


def circ_tent_symbol(j, u, D, M, L):
    """DFT at bin j of the even-circulant tent (incl. reflection)."""
    c = np.zeros(M)
    i0 = int(math.floor(u / D))
    for i in range(max(0, i0 - 2), min(M, i0 + 3)):
        v = 1.0 - abs(i * D - u) / D
        if v > 0.0:
            c[i] += v
    if u < D:
        for i in range(0, min(M, int(math.floor((D - u) / D)) + 2)):
            v = 1.0 - (i * D + u) / D
            if v > 0.0:
                c[i] += v
    a = even_extend(c)
    n = np.arange(L)
    z = np.dot(a, np.exp(-2j * PI * j * n / L))
    return float(z.real), float(z.imag)


def dirichlet_dP(j, D, M, L, ka):
    acc = 0j
    for n_idx in range(ka):
        n = int(V.PP[n_idx])
        u = float(V.U[n_idx])
        lam_over = float(V.LAM[n]) / math.sqrt(float(n))
        kr, ki = circ_tent_symbol(j, u, D, M, L)
        acc += -lam_over * (kr + 1j * ki)
    return acc


def C_cos(th, v, mmax):
    m = np.arange(mmax + 1)[:, None]
    return (np.asarray(v, float)[None, :]
            * np.cos(m * np.asarray(th, float)[None, :])).sum(1)


def energy_from_C(C, k):
    C = np.asarray(C, float)
    s = float(C[0] * C[0])
    if k > 1:
        s += 2.0 * float(np.dot(C[1:k], C[1:k]))
    return s / PI


def cd_energy_of(th, dcent, k):
    """r389 Chebyshev-CD energy of a signed mass on the cosine
    grid.  Transfer weights: omega_0=1/pi, omega_m=2/pi for
    1 <= m < k.  No spectral peeking, no R^dagger inputs."""
    C = C_cos(th, dcent, k + 2)
    E = energy_from_C(C, k)
    Cb = C.copy()
    Cb[0] = 0.0
    if k > 1:
        Cb[1] = 0.0
    E_bulk = energy_from_C(Cb, k)
    qm = 0.5 * float(np.dot(dcent, dcent))
    tail = C[1:k] ** 2 if k > 1 else np.array([0.0])
    mean_c2 = float(np.mean(tail)) if len(tail) else 0.0
    return dict(
        C=C, E=E, E_bulk=E_bulk, k=int(k),
        C0=float(C[0]), C1=float(C[1]) if k > 1 else 0.0,
        Cmax=float(np.max(np.abs(tail ** 0.5))) if k > 1 else 0.0,
        argmax=(int(np.argmax(tail)) + 1) if k > 1 else 0,
        qm=qm,
        mean_over_qm=mean_c2 / max(qm, 1e-30),
        hhi=float(np.sum((tail / max(float(np.sum(tail)), 1e-30)) ** 2)),
    )


def pack_kz(kz):
    alpha, M, L, Nw, D = V.window_shape(kz)
    cP, ka = V.prime_lags(alpha, M, D)
    cA = V.arch_lags(M, D)
    dP = V.spectral_density(cP)
    dA = V.spectral_density(cA)
    jj = np.arange(1, L // 2 + 1)
    th = 2.0 * PI * jj / L
    fej = (2.0 / L) * (1.0 - np.cos(th))
    fej = fej.copy()
    fej[-1] *= 0.5
    dcent = fej * dP[jj]
    dref = fej * dA[jj]
    k = max(1, Nw - 3)
    en = cd_energy_of(th, dcent, k)
    a = even_extend(cP)
    fej_full = (2.0 / L) * (1.0 - np.cos(2.0 * PI * np.arange(L) / L))
    dcent_u = fej_full * dP
    lap = 2.0 * a - np.roll(a, 1) - np.roll(a, -1)
    rec = np.fft.ifft(dcent_u).real
    return dict(
        kz=kz, alpha=alpha, M=M, L=L, Nw=Nw, D=D, ka=ka,
        cP=cP, dP=dP, dA=dA, jj=jj, th=th, fej=fej,
        dcent=dcent, dref=dref, a=a, dcent_u=dcent_u,
        lap_dev=float(np.max(np.abs(rec - lap / L))),
        dcent_dev=float(np.max(np.abs(dcent - fej * dP[jj]))),
        **en,
    )


def dirichlet_maxdev(P, js=None):
    L, M, D, ka = P["L"], P["M"], P["D"], P["ka"]
    if js is None:
        js = [1, 2, 3, min(8, L // 4), L // 4, L // 2]
    js = [j for j in js if 0 < j < L]
    mx = 0.0
    for j in js:
        pred = dirichlet_dP(j, D, M, L, ka)
        mx = max(mx, abs(float(P["dP"][j]) - pred.real))
    return mx


def selected_shape(k):
    a = 2 ** k
    rk = int(math.isqrt(k))
    m = k * (2 ** rk) - 1
    alpha = math.log(a)
    D = alpha / (m + 1)
    M = m + 1
    L = 2 * M
    return dict(k=k, a=a, rk=rk, m=m, alpha=alpha, D=D, M=M, L=L,
                X=a * a, Nw=M // 2)


def selected_cP(shp):
    alpha, D, M = shp["alpha"], shp["D"], shp["M"]
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1.0e-14, side="right"))
    c = np.zeros(M)
    for u_j, m_j in zip(V.U[:ka], V.W_VM[:ka]):
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                c[i] -= m_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= m_j * 0.5 * v
    return c, ka


def pack_selected(k):
    shp = selected_shape(k)
    cP, ka = selected_cP(shp)
    M, L = shp["M"], shp["L"]
    a = np.concatenate([cP, [0.0], cP[-1:0:-1]])
    dP = np.fft.fft(a).real
    jj = np.arange(1, L // 2 + 1)
    th = 2.0 * PI * jj / L
    fej = (2.0 / L) * (1.0 - np.cos(th))
    fej = fej.copy()
    fej[-1] *= 0.5
    dcent = fej * dP[jj]
    Nw = shp["Nw"]
    kk = max(1, Nw - 3) if Nw > 3 else max(1, Nw)
    en = cd_energy_of(th, dcent, kk)
    return dict(shp=shp, ka=ka, dP=dP, dcent=dcent, th=th, **en)


def lags_from_atoms(uu, ww, M, D):
    return DMF.chi_prime_lags(M, D, uu, ww)


def pack_lags(cP, M, L, Nw):
    dP = V.spectral_density(cP) if len(cP) == M and L == 2 * M - 2 else None
    if dP is None:
        a = np.concatenate([cP, [0.0], cP[-1:0:-1]]) if L == 2 * len(cP) \
            else even_extend(cP)
        dP = np.fft.fft(a).real
        if len(dP) != L:
            raise ValueError("lag FFT length")
    jj = np.arange(1, L // 2 + 1)
    th = 2.0 * PI * jj / L
    fej = (2.0 / L) * (1.0 - np.cos(th))
    fej = fej.copy()
    fej[-1] *= 0.5
    dcent = fej * dP[jj]
    k = max(1, Nw - 3) if Nw > 3 else max(1, Nw)
    return cd_energy_of(th, dcent, k)


def scramble_energy():
    alpha, M, L, Nw, D = V.window_shape(MAIN_KZ)
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1.0e-14, side="right"))
    rng = np.random.default_rng(SCR_SEED)
    u_s = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    cP = lags_from_atoms(u_s, V.W_VM[:ka], M, D)
    return pack_lags(cP, M, L, Nw)


def two_period_hhi(S=21, c=2.0 / 3.0):
    j = np.arange(1, S + 1)
    x = np.cos(PI * j / S)
    mesh = (1.0 - x) * (PI / S)
    w = np.where(j % 2 == 0, mesh, -c * mesh)
    th = PI * j / S
    fej = np.maximum(1.0 - x, 0.0)
    dref = fej * (float(np.sum(w)) / max(float(np.sum(fej)), 1e-30))
    dcent = w - dref
    C = C_cos(th, dcent, S)
    tail = C[1:] ** 2
    hhi = float(np.sum((tail / max(float(np.sum(tail)), 1e-30)) ** 2))
    arg = int(np.argmax(np.abs(C[1:]))) + 1
    return dict(hhi=hhi, arg=arg, C0=float(C[0]),
                E=energy_from_C(C, S // 2 + 1))


def chi_energy(kz, q, lpq):
    uu, ww, _nn, _ch = DMF.chi_window_comb(kz, q)
    alpha, M, L, Nw, D = V.window_shape(kz)
    cP = DMF.chi_prime_lags(M, D, uu, ww)
    return pack_lags(cP, M, L, Nw)


def assist_of(kz):
    """Correlation witness only -- NOT an input of E_bulk."""
    mz = V.build_measures(kz)
    k = int(mz["Nw"])
    a, b, h0 = V.mu_chain(mz["xp"], mz["wp"], k)
    B = V.b_matrix(a, b, h0, mz["yn"], mz["vn"], k)
    E = 0.5 * ((B @ B.T) + (B @ B.T).T)
    maxd = float(np.max(np.diag(E)))
    lam = float(np.linalg.eigvalsh(E)[-1])
    return lam / maxd - 1.0 if maxd > 0 else 0.0


def mvt_ratio(P):
    alpha, D, L, ka, k = P["alpha"], P["D"], P["L"], P["ka"], P["k"]
    X = math.exp(2.0 * alpha)
    T = PI / max(D, 1e-15)
    s2 = 0.0
    for n_idx in range(ka):
        n = int(V.PP[n_idx])
        lam = float(V.LAM[n])
        s2 += (lam * lam) / float(n)
    crude = (1.0 + X / T) * s2 * max(k, 1)
    return crude / max(P["E_bulk"], 1e-30), X / T, s2


def ppow_lag_ratio(kz=MAIN_KZ):
    alpha, M, L, Nw, D = V.window_shape(kz)
    ka = int(np.searchsorted(V.U, 2.0 * alpha + 1.0e-14, side="right"))
    c_pr = np.zeros(M)
    c_pp = np.zeros(M)

    def is_prime(n):
        if n < 2:
            return False
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True

    for n_idx in range(ka):
        n = int(V.PP[n_idx])
        tgt = c_pr if is_prime(n) else c_pp
        u_j = float(V.U[n_idx])
        m_j = float(V.W_VM[n_idx])
        i0 = int(math.floor(u_j / D))
        for i in range(max(0, i0 - 2), min(M, i0 + 3)):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                tgt[i] -= m_j * 0.5 * v
        if u_j < D:
            for i in range(0, min(M, int(math.floor((D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    tgt[i] -= m_j * 0.5 * v
    npr = float(np.linalg.norm(c_pr))
    npp = float(np.linalg.norm(c_pp))
    return npp / max(npr, 1e-30), npr, npp


# ---- legs ---------------------------------------------------------------

def part_a_toy():
    section("S1  LEG A -- FRACTIONS STENCIL, CD ENERGY TOY")
    L = 6
    h0, h1 = Fr(2, L), Fr(-1, L)
    check("G01-stencil-Q",
          h0 == Fr(1, 3) and h1 == Fr(-1, 6) and h0 + 2 * h1 == 0,
          "h0=2/L=%s h1=-1/L=%s; mass of stencil = 0" % (h0, h1))
    # circulant convolution over Q: (h * a)_i = lap(a)_i / L
    a = [Fr(2), Fr(1), Fr(0), Fr(3), Fr(0), Fr(1)]
    conv = []
    for i in range(L):
        s = h0 * a[i] + h1 * a[(i - 1) % L] + h1 * a[(i + 1) % L]
        lap = 2 * a[i] - a[(i - 1) % L] - a[(i + 1) % L]
        conv.append(s - lap / L)
    check("G02-laplacian-conv-Q",
          all(x == 0 for x in conv),
          "IFFT(Fejer) * a = Delta a / L over Q on a 6-cycle")
    nodes = [Fr(-2, 3), Fr(-1, 3), Fr(0), Fr(1, 3), Fr(2, 3)]
    wts = [Fr(1), Fr(-1), Fr(2), Fr(-2), Fr(1)]
    # C0 = sum w, C1 toy skip -- r389 identity scale-stripped
    C0 = sum(wts)
    check("G03-centered-mass-not-forced",
          C0 == Fr(1),
          "toy signed mass %s (arch subtraction is what zeros C0 "
          "on MAIN, not the CD weights)" % C0)
    okf, det = energy_fn_audit()
    check("G04-energy-no-forbidden", okf, det)


def part_b_w9():
    section("S2  LEG A -- w9 REPRESENTATION + TRANSFER NORM")
    P = pack_kz(MAIN_KZ)
    check("G10-w9-dcent-is-fej-dP",
          P["dcent_dev"] < ID_BAR,
          "maxdev=%.3e (centered d = Fejer odot prime density)"
          % P["dcent_dev"])
    ddev = dirichlet_maxdev(P)
    check("G11-w9-Dirichlet-interpolant",
          ddev < DIR_BAR,
          "maxdev=%.3e  dP[j] = -Sum Lambda n^{-1/2} K_j(log n)"
          % ddev)
    check("G12-w9-Fejer-Laplacian",
          P["lap_dev"] < LAP_BAR,
          "maxdev=%.3e  IFFT(Fejer odot dP) = Delta cP_ext / L"
          % P["lap_dev"])
    check("G13-w9-edge-C0-C1-zero",
          abs(P["C0"]) < 1e-12 and abs(P["C1"]) < 1e-12
          and abs(P["E_bulk"] - P["E"]) <= 1e-12,
          "C0=%.3e C1=%.3e E=E_bulk=%.6g (mass+fold killed; "
          "cap outside CD band)" % (P["C0"], P["C1"], P["E_bulk"]))
    check("G14-w9-E-bulk-pin",
          W9_E_LO <= P["E_bulk"] <= W9_E_HI,
          "E_bulk=%.6g (CD-transfer of centered d)" % P["E_bulk"])
    check("G15-w9-quadratic-mean",
          W9_QM_LO <= P["mean_over_qm"] <= W9_QM_HI,
          "mean C^2/qm=%.4f -- Parseval class, not a valley"
          % P["mean_over_qm"])
    ratio, xt, s2 = mvt_ratio(P)
    check("G16-w9-MVT-does-not-close",
          ratio >= MVT_RATIO_FLOOR,
          "crude/E=%.4g  X/T=%.3g  s2=%.4g  (unconditional MVT "
          "is %d x too large)" % (ratio, xt, s2, int(ratio)))
    return P


def part_a_two_windows():
    section("S3  LEG A -- TWO FURTHER WINDOWS (kz=18, 52)")
    devs = []
    Es = []
    for kz in (18, 52):
        P = pack_kz(kz)
        ddev = dirichlet_maxdev(P, js=[1, 2, 5, P["L"] // 4])
        devs.append(ddev)
        Es.append(P["E_bulk"])
        print("    kz=%d L=%d Nw=%d Dirichlet maxdev=%.3e E_bulk=%.6g"
              % (kz, P["L"], P["Nw"], ddev, P["E_bulk"]), flush=True)
    check("G20-kz18-kz52-Dirichlet",
          max(devs) < 1e-10,
          "maxdev=%.3e / %.3e" % (devs[0], devs[1]))
    check("G21-kz18-kz52-E-not-tiny",
          min(Es) >= 1.0,
          "E_bulk %.6g, %.6g (no decay vs w9=1.81)" % (Es[0], Es[1]))


def part_b_selected(smoke):
    section("S4  LEG B -- SELECTED SEQUENCE a_k=2^k")
    ks = (4, 6) if smoke else tuple(range(2, 10))
    rows = []
    for k in ks:
        shp = selected_shape(k)
        if shp["X"] > V.TABLE_CAP:
            continue
        R = pack_selected(k)
        rows.append(R)
        print("    k=%d a=%d L=%d Nw=%d E_bulk=%.6g E/Nw=%.6g"
              % (k, shp["a"], shp["L"], shp["Nw"], R["E_bulk"],
                 R["E_bulk"] / max(shp["Nw"], 1)), flush=True)
    e4 = next(r["E_bulk"] for r in rows if r["shp"]["k"] == 4)
    e6 = next(r["E_bulk"] for r in rows if r["shp"]["k"] == 6)
    check("G30-selected-not-falling-small",
          e6 > e4 > 0.05,
          "k=4 E=%.4g < k=6 E=%.4g (grows on the Lean ladder)"
          % (e4, e6))
    if not smoke:
        e9 = next(r["E_bulk"] for r in rows if r["shp"]["k"] == 9)
        check("G31-selected-k9",
              SEL_K9_E_LO <= e9 <= SEL_K9_E_HI,
              "k=9 E_bulk=%.6g -- not ~0" % e9)
        bulk = [r["E_bulk"] for r in rows if r["shp"]["k"] >= 4]
        check("G32-selected-no-monotone-decay",
              max(bulk) >= 0.5 and bulk[-1] >= bulk[0],
              "k=4..9 E_bulk ends at %.4g >= start %.4g"
              % (bulk[-1], bulk[0]))
    return rows


def part_d_kills():
    section("S5  LEG D -- KILLS")
    P = pack_kz(MAIN_KZ)
    scr = scramble_energy()
    check("G40-scramble-not-small",
          scr["E_bulk"] >= SCR_RATIO * P["E_bulk"],
          "SCR E=%.4g > %.2f x MAIN %.4g -- centered d SEES "
          "log-n cancellation (r389 nu-QM did not)"
          % (scr["E_bulk"], SCR_RATIO, P["E_bulk"]))
    tp = two_period_hhi(21)
    check("G41-two-period-comb",
          tp["hhi"] >= TP_HHI_FLOOR and tp["arg"] == 21,
          "HHI=%.3f comb at m=%d (cosine-grid AP)"
          % (tp["hhi"], tp["arg"]))
    # mutant: omega=1, no 2/pi and no CD cutoff -- Parseval of C
    C = P["C"]
    mut = float(np.dot(C, C))
    check("G42-mutant-omega-1",
          mut / max(P["E"], 1e-30) >= 1.5,
          "Sigma C_m^2 = %.4g vs CD-E %.4g -- transfer weights "
          "are load-bearing as a SCALE, not as a decay"
          % (mut, P["E"]))
    check("G43-mutant-no-split-noop",
          abs(P["E_bulk"] - P["E"]) <= 1e-12,
          "dropping r=0,1 does not change CD-E (already zero): "
          "the 'energy must not fall without split' mutant is "
          "vacuous at this norm -- named honestly")
    dchi = chi_energy(DEAD_CHI3, DMF.Q_CHI3, DMF.LPQ3)
    lchi = chi_energy(MAIN_KZ, DMF.Q_CHI3, DMF.LPQ3)
    check("G44-dead-chi-not-separator",
          CHI_E_LO <= dchi["E_bulk"] <= CHI_E_HI
          and CHI_E_LO <= lchi["E_bulk"] <= CHI_E_HI,
          "dead chi3-15 E=%.4g living chi3-9 E=%.4g MAIN=%.4g "
          "(two-sided: both O(1))"
          % (dchi["E_bulk"], lchi["E_bulk"], P["E_bulk"]))
    ratio, npr, npp = ppow_lag_ratio()
    check("G45-prime-powers-absolute",
          ratio <= PP_RATIO_HI,
          "||c_{p^k, k>=2}|| / ||c_p|| = %.4f (w9); series "
          "Sum p^{-k/2} log p converges unconditionally"
          % ratio)
    return P, scr, tp


def part_full_census():
    section("S6  LEG B/C -- CORE-42 CENSUS + BRIDGE + MVT")
    core = list(V.admissible_indices())
    rows = []
    assists = []
    for kz in core:
        P = pack_kz(kz)
        rows.append(P)
        assists.append(assist_of(kz))
    Ebs = np.array([r["E_bulk"] for r in rows], float)
    Nws = np.array([r["Nw"] for r in rows], float)
    qms = np.array([r["mean_over_qm"] for r in rows], float)
    As = np.array(assists, float)
    En = Ebs / Nws
    sl = float(np.polyfit(np.log(Nws), np.log(np.maximum(Ebs, 1e-30)), 1)[0])
    sln = float(np.polyfit(np.log(Nws), np.log(np.maximum(En, 1e-30)), 1)[0])
    corr = float(np.corrcoef(En, As)[0, 1])
    check("G50-core42-count",
          len(rows) == CORE_N, "n=%d" % len(rows))
    check("G51-core42-E-grows",
          CORE_E_LO <= float(Ebs.min()) and float(Ebs.max()) <= CORE_E_HI
          and sl >= CORE_SLOPE_LO,
          "E in [%.4g, %.4g] slope=%.3f -- GROWS, not ->0"
          % (float(Ebs.min()), float(Ebs.max()), sl))
    check("G52-core42-quadratic-mean",
          0.35 <= float(qms.min()) and float(qms.max()) <= 0.95,
          "mean C^2/qm in [%.3f, %.3f] -- Parseval class"
          % (float(qms.min()), float(qms.max())))
    check("G53-bridge-assist-weak",
          abs(corr) <= CORR_ABS_HI,
          "corr(E/Nw, assist)=%.3f -- the CD energy of centered "
          "d does NOT dominate Assist (5.4 bridge is a named "
          "norm, not a closing majorant)" % corr)
    Pdeep = rows[int(np.argmax(Nws))]
    ratio, xt, s2 = mvt_ratio(Pdeep)
    check("G54-deep-MVT-worse",
          ratio >= MVT_RATIO_FLOOR and xt >= 10.0,
          "deep Nw=%d crude/E=%.4g X/T=%.4g (unconditional "
          "large sieve farther from closing)"
          % (Pdeep["Nw"], ratio, xt))
    print("    slope E ~ Nw^{%.3f}; E/Nw ~ Nw^{%.3f}; "
          "corr(E/Nw,assist)=%.3f"
          % (sl, sln, corr), flush=True)
    return rows, sl, corr


def verdict_of(w9, core_rows):
    if core_rows is None:
        if w9["E_bulk"] > 1.0 and w9["mean_over_qm"] > 0.4:
            return "REFUTED"
        return "PARTIAL"
    Ebs = [r["E_bulk"] for r in core_rows]
    Nws = [r["Nw"] for r in core_rows]
    sl = float(np.polyfit(np.log(Nws),
                          np.log(np.maximum(Ebs, 1e-30)), 1)[0])
    qms = [r["mean_over_qm"] for r in core_rows]
    if sl > 0.2 and min(qms) > 0.3 and max(Ebs) > 2.0:
        return "REFUTED"
    return "PARTIAL"


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("source_weyl_energy_probe -- "
          "PRIME.SOURCE.WEYL_ENERGY.THEOREM.01 (round 399)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else
                         "FULL (core-42 + selected k=2..9 + chi)"))
    print("=" * 78)

    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)

    part_a_toy()
    pw9 = part_b_w9()
    part_a_two_windows()
    part_b_selected(smoke)
    part_d_kills()
    core_rows = None
    if not smoke:
        core_rows, _sl, _c = part_full_census()
    else:
        section("S6  FULL CENSUS skipped (--smoke)")

    verd = verdict_of(pw9, core_rows)
    section("S7  VERDICT")
    check("G60-verdict-REFUTED",
          verd == "REFUTED",
          "E^bulk sits at quadratic-mean and grows; decay "
          "theorem REFUTED.  Representation SATZ.  MVT/large "
          "sieve unconditional-fails; a closing bound would "
          "be RH-near (ZIRKULAER as a strategy).  %s" % verd)

    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)  %s" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0, verd))
    if n_fail == 0:
        print("SOURCE WEYL ENERGY %sVERIFIED" % (
            "SMOKE " if smoke else ""))
        return 0
    print("SOURCE WEYL ENERGY FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
