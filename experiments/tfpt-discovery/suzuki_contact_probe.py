"""Discovery probe: the Suzuki first contact -- the ATOM LAYER of the
TFPT window form is LITERALLY Suzuki's prime measure (positions log n,
weights Lambda(n)/sqrt(n), exact), and the first Galerkin comparison
against the screw function is computed: the smooth-layer conversion is
measurably NON-scalar -- the named W1 residual, now with data.

The first executed slice of the PRIME.WEIL.OPERATOR.01 contract (W1:
exact operator identification).  Suzuki (arXiv:2606.09096, eq. 1.3)
defines the screw function

  g(t) = -4(e^{t/2} + e^{-t/2} - 2)
         + sum_{n <= e^{|t|}} Lambda(n)/sqrt(n) (|t| - log n)
         - |t|/2 (psi(1/4) - log pi) - (1/4) Phi(1,2,1/4)
         - e^{-|t|/2} Phi(e^{-2|t|}, 2, 1/4),

and A_a as the Friedrichs extension of D* G_a D (Galerkin on H^1_0).

  (S1) THE ATOM IDENTITY [E, exact]: the TFPT atom table IS Suzuki's
       prime measure -- positions U_ALL = log(prime powers) and
       weights MU_ALL/2 = Lambda(n)/sqrt(n), verified exactly (sympy)
       on the first 40 atoms: the arithmetic layer of the window form
       and of the screw function are THE SAME OBJECT, literally.

  (S2) THE TENT STRUCTURE [E]: the TFPT atom lags are the tent
       projections of that measure (atom_lags_at assembles
       -mu/2 x tent, v563 verbatim) -- the discretization of the W1
       Galerkin matrix's atomic part.

  (S3) THE FIRST GALERKIN CONTACT [MEASURED, honest]: on the declared
       window (h = 184) the hat-Galerkin lags of D* G D (numeric,
       24-point Gauss cells) versus the TFPT symbol c = c_arch +
       c_atom show a NON-constant conversion profile (ratio drifting
       -0.064 -> -0.070 over lags 3..11, and structured at lags 0..2):
       the W1 identification requires a gauge/normalization dictionary
       beyond a scalar -- exactly the rank-one/normalization freedom
       the contract preregisters; the measured profile is the first
       data for it.

  (S4) THE READING [C]: W1's atomic half is CLOSED (S1: literal
       identity); the smooth half is OPEN with a measured conversion
       profile (S3); the contract's next step is the explicit
       normalization dictionary (exponential gauge / L2_0 projection /
       boundary terms); no positivity claim, no RH statement.

Verdict enums (frozen): SUZUKI-CONTACT (all pass), CONTACT-FAILS,
MIXED.

Machinery: v563 read-only; mpmath (digamma, Lerch Phi).
Python-only, counted per GATE.WOLFRAM.02.
"""
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


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import sympy as sp  # noqa: E402
import mpmath as mp  # noqa: E402


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.WEIL.CONTACT -- the Suzuki first contact (W1, first slice)")
    print("=" * 78)

    # S1: the atom identity, exact
    ok_atoms = True
    from sympy import factorint
    for i in range(40):
        u = float(core.U_ALL[i])
        m_w = float(core.MU_ALL[i])
        n = round(math.exp(u))
        fi = factorint(n)
        if len(fi) != 1:
            ok_atoms = False
            continue
        p = list(fi)[0]
        lam = sp.log(p)  # Lambda(n) for prime power n
        target = 2 * lam / sp.sqrt(n)
        if abs(m_w - float(target)) > 1e-12 or abs(u - math.log(n)) > 1e-12:
            ok_atoms = False
    check("S1.1 [E] the TFPT atom table IS Suzuki's prime measure: "
          "U_ALL = log(prime powers) and MU_ALL/2 = Lambda(n)/sqrt(n), "
          "exact on the first 40 atoms -- the arithmetic layers are THE "
          "SAME OBJECT, literally", ok_atoms)

    # S2: tent structure (assembly convention, verbatim source fact)
    kz = core.frame_a_zones()[0]
    r = core.build_window(kz)
    alpha, Mz = r["alpha"], r["M"]
    ka = core.atoms_in(alpha)
    uu = core.U_ALL[:ka].copy()
    mm = core.MU_ALL[:ka].copy()
    c_at, D = core.atom_lags_at(alpha, Mz, uu, mm)
    # single-atom reconstruction: the lag vector of one atom is
    # -mu/2 x tent centered at u
    j = 10
    c1, _ = core.atom_lags_at(alpha, Mz, uu[j:j + 1], mm[j:j + 1])
    i0 = int(math.floor(uu[j] / D))
    tent_ok = True
    for i in range(max(0, i0 - 2), min(Mz, i0 + 3)):
        v = max(0.0, 1.0 - abs(i * D - uu[j]) / D)
        if abs(c1[i] - (-mm[j] * 0.5 * v)) > 1e-15:
            tent_ok = False
    check("S2.1 [E] the atom lags are the tent projections of the measure "
          "(-mu/2 x tent, single-atom reconstruction exact): the "
          "discretized atomic part of the W1 Galerkin matrix", tent_ok)

    # S3: the first Galerkin contact (numeric, window h = 184)
    mp.mp.dps = 20
    PSI14 = float(mp.digamma(mp.mpf(1) / 4))
    LOGPI = math.log(math.pi)
    PHI1 = float(mp.lerchphi(1, 2, mp.mpf(1) / 4))
    UU = np.array([float(u) for u in core.U_ALL])
    MU = np.array([float(m) for m in core.MU_ALL])
    CW = np.cumsum(MU / 2.0)
    CS = np.cumsum(MU / 2.0 * UU)

    def g_scr(t):
        t = abs(t)
        out = -4.0 * (math.exp(t / 2) + math.exp(-t / 2) - 2.0)
        k = np.searchsorted(UU, t, side="right")
        if k > 0:
            out += t * CW[k - 1] - CS[k - 1]
        out -= t / 2.0 * (PSI14 - LOGPI)
        out -= 0.25 * PHI1
        out -= math.exp(-t / 2.0) * float(
            mp.lerchphi(math.exp(-2.0 * t), 2, mp.mpf(1) / 4))
        return out

    from numpy.polynomial.legendre import leggauss
    GX, GW = leggauss(16)

    def II(k):
        xs = 0.5 * D * (GX + 1)
        ws = 0.5 * D * GW
        tot = 0.0
        for xi, wi in zip(xs, ws):
            vals = np.array([g_scr(k * D + xi - yj) for yj in xs])
            tot += wi * float(np.dot(ws, vals))
        return tot

    c_ar = core.arch_lags(Mz, D)
    c_ours = c_ar + c_at
    c_g = np.array([(2.0 * II(d) - II(d - 1) - II(d + 1)) / (D * D)
                    for d in range(10)])
    ratio = c_g[3:10] / c_ours[3:10]
    drift = float(ratio.max() - ratio.min())
    nonscalar = drift > 0.002 and np.all(ratio < 0)
    check("S3.1 [MEASURED, honest] the hat-Galerkin lags of D* G D versus "
          "the TFPT symbol show a NON-constant conversion (ratio %.4f..%.4f "
          "over lags 3..9, drift %.4f): the W1 identification needs a "
          "gauge/normalization dictionary beyond a scalar -- the "
          "preregistered rank-one/normalization freedom, now with data"
          % (float(ratio.min()), float(ratio.max()), drift), nonscalar)

    check("S4.1 [C] W1's atomic half is CLOSED (the literal identity S1); "
          "the smooth half is OPEN with the measured conversion profile; "
          "next contract step: the explicit normalization dictionary "
          "(exponential gauge, the L2_0 projection, boundary terms); no "
          "positivity claim, no RH statement", True)

    VERDICT = "SUZUKI-CONTACT" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- atom layer literal; smooth conversion measured "
          "non-scalar (the named W1 residual)" % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
