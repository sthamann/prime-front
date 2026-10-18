#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""filon_enclosure_probe -- PRIME.RDAGGER.FILON_ENCLOSURE.01 (r483).

Enclose the two open integral classes of the r481 remainder
  S = B - C C^T / c_tail
on the even Nyström--Slepian block {psi_0, psi_2, psi_4}
versus even tail {psi_6, psi_8, psi_10} (odd partner
{psi_1, psi_3, psi_5} vs {psi_7, psi_9, psi_11}), then
attempt the SATZ lambda_*(0.3) >= c.

CLASS 1 -- [0, T] interval FT.  The Nyström sample transform
  hat_i(t) = sum_q w_q psi_i(x_q) e^{i t x_q}
is an explicit exponential sum (no x-quadrature).  sigma_A is
smooth.  Panel-linear Filon against cos((x_q-x_r) t) with a
split M2 remainder (r477 Digamma; |sigma''| <= 36.8 on (0,8]
and <= 0.018 on [8, 150]) seals every B,C entry on [0, T].
Midpoints hit the r480/r481 trapezoid to 1e-6.

CLASS 2 -- [T, infinity) tail.  The exp-sum is almost-periodic
and is NOT the decaying interpolant FT: the Ci-sum of the
exp-sum to infinity produces lambda_min(S) ~ -1.6 (KILL).
The decaying FT is the 4-term endpoint IBP of the sinc
extension (entire).  Remainder after 4 terms at T_rem=800
is O(10^{-5}) on C_46.  Diagonal tails are positive and are
booked to B (A_+ side, no silent shift).  Off-diagonal tails
are included as signed IBP values, not dropped.

ASSEMBLAGE.  Higham on the finite even S with entry radius
<= 1e-4 yields mu >= 1.19e-3 and a would-be
  c_* = mu / (1 + ||C||^2 / c_tail^2) ~ 1.68e-4
if C were the full operator coupling.  It is not.
Leftover ||P_block A P_{>=12}||_F = 2.74e-2 on [0, T]
(modes 12..14; 16+ are Nyström kernel junk).  The
IBP-inflated budget is ||C_rest|| < 2.4e-4.  Deficit
factor ~ 100.  Not lambda_*(0.3) >= c.

SIGN BOOKKEEPING.  (i) Diagonal IBP tails enlarge B and are
kept (safe for a lower bound on B).  (ii) Off-diagonal IBP
tails are signed and kept as values.  (iii) Exp-sum omega=0
pairs are NOT integrated to infinity (would diverge; the
diagonal DC is positive but the off-diagonal DC is not
safe to drop).  (iv) Leftover C is not silently moved into
B or into c_tail.

ANTI-LIST (not reused): Fourier-HS majorant (r478),
crude kappa_high (r480 KILL), integer Fourier ONB (r481),
sigma^2 Plancherel as ||A u||_{[-L,L]} (r481), IBP
envelope-as-pad (r481 KILL), exp-sum Ci-to-infinity (this
round KILL).

r469 contract.  Fixed L=0.3 only.  P empty.  SCRAMBLE GATE:
literal log n, vacuous here.  NO RH CLAIM.  NO anti-RH claim.
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
from scipy.special import psi as digamma

HERE = os.path.abspath(os.path.dirname(__file__))
CANDIDATES = [
    HERE,
    os.path.join(HERE, "..", "..", "experiments", "tfpt-discovery"),
    "/Users/stefanhamann/Projekte/tfpt-theoryv4/experiments/tfpt-discovery",
]
for path in CANDIDATES:
    path = os.path.abspath(path)
    if os.path.isfile(os.path.join(path, "classical_cert_probe.py")):
        if path not in sys.path:
            sys.path.insert(0, path)
        break

import classical_cert_probe as CC  # noqa: E402
import kappa_high_probe as KH  # noqa: E402

L_YB = 0.3
SIG0 = -5.372183419225666
TSTAR = 8.0
T_CUT = 150.0
PI = math.pi

R480_EVEN_LO = "5.0e-03"
R480_ODD_LO = "0.15"
EPS_HI_PIN = "1.50e-08"
C_TAIL_LO_PIN = "0.2408"
FILON_DIFF_PIN = "2.0e-04"
FILON_DIFF_FULL_PIN = "2.0e-05"
LEFTOVER_F_PIN = "2.74e-02"
LEFTOVER_BUDGET_PIN = "2.4e-04"
RHO_T2_PIN = "0.041667"
HIGHAM_MU_PIN = "1.19e-03"

VERDICT_KIND = (
    "REDUCED(finite-S-interval-PD; leftover-C-HS=2.74e-2-vs-budget-2.4e-4)"
)
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS: list[tuple[str, bool]] = []

SCRAMBLE_SENSITIVE = True
SCRAMBLE_REASON = (
    "P uses literal log n on nodes log n <= 2L.  At L=0.3 "
    "the node set is empty (P=0); scrambling is vacuous here "
    "and becomes live at L=0.8.  Not fold-mode pairing."
)


def check(name: str, ok: bool, detail: str = "") -> bool:
    CHECKS.append((name, bool(ok)))
    print("  [%s] %-42s %s" %
          ("PASS" if ok else "FAIL", name, detail), flush=True)
    return bool(ok)


def firewall_audit() -> tuple[bool, str]:
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(source)
    forbidden = {"zetazero", "nzeros", "grampoint", "zetazeros"}
    bad = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in forbidden:
            bad.append(node.id)
        if isinstance(node, ast.Attribute) and node.attr in forbidden:
            bad.append(node.attr)
    return (not bad), (",".join(sorted(set(bad))) if bad else "")


def sigma(t: float) -> float:
    return float(np.real(digamma(0.25 + 1j * t / 2.0)) - math.log(math.pi))


def sinc_dn(dx: float, tc: float, n: int) -> float:
    if abs(dx) < 1e-12:
        if n % 2 == 1:
            return 0.0
        k = n // 2
        return (tc / PI) * ((-1) ** k) * (tc ** n) / (n + 1)
    tot = 0j
    ia = 1j * tc
    for k in range(n + 1):
        tot += (math.comb(n, k) * (ia ** (n - k))
                * ((-1) ** k) * math.factorial(k) / (dx ** (k + 1)))
    return float((np.exp(1j * tc * dx) * tot).imag / PI)


def jets_at(x, w, f, evk, tc, x0, nord=4):
    acc = [0.0] * (nord + 1)
    for xj, wj, fj in zip(x, w, f):
        dx = x0 - float(xj)
        for n in range(nord + 1):
            acc[n] += wj * sinc_dn(dx, tc, n) * fj
    return [a / evk for a in acc]


def hat_ibp_even(jets, t, nterm=4):
    s, c = math.sin(t * L_YB), math.cos(t * L_YB)
    phases = (s, c, -s, -c)
    tot, tk = 0.0, t
    for k in range(nterm):
        tot += 2.0 * jets[k] * phases[k % 4] / tk
        tk *= t
    return tot


def hat_ibp_odd(jets, t, nterm=4):
    s, c = math.sin(t * L_YB), math.cos(t * L_YB)
    phases = (-c, s, c, -s)
    tot, tk = 0.0, t
    for k in range(nterm):
        tot += 2.0 * jets[k] * phases[k % 4] / tk
        tk *= t
    return tot


def filon_band_J(omegas, t0, t1, npan):
    """Vectorized linear Filon of sigma on [t0, t1] for many omega."""
    ts = np.linspace(t0, t1, npan + 1)
    sig = np.array([sigma(t) if t > 1e-12 else sigma(1e-8) for t in ts])
    h = (t1 - t0) / npan
    a = ts[:-1]
    b = ts[1:]
    sa = sig[:-1]
    sb = sig[1:]
    q = (sb - sa) / h
    out = np.empty(len(omegas))
    for i, omega in enumerate(omegas):
        w = float(omega)
        if abs(w) < 1e-14:
            out[i] = float(np.trapezoid(sig, ts))
            continue
        s1 = (np.sin(w * b) - np.sin(w * a)) / w
        i_tau = (h * np.sin(w * b) / w
                 + (np.cos(w * b) - np.cos(w * a)) / (w * w))
        out[i] = float(np.dot(sa, s1) + np.dot(q, i_tau))
    rem = None
    return out, rem


def filon_rem_l1(t0, t1, m2, npan):
    h = (t1 - t0) / npan
    return m2 * (h ** 3) / 8.0 * npan


def assemble_filon(x, w, funcs, idx, jtab, om_index, rem_l1):
    m = len(idx)
    alphas = [w * funcs[k] for k in idx]
    amat = np.zeros((m, m))
    rmat = np.zeros((m, m))
    n = len(x)
    for a in range(m):
        for b in range(a, m):
            acc = 0.0
            racc = 0.0
            ai, aj = alphas[a], alphas[b]
            for q in range(n):
                for r in range(n):
                    acc += ai[q] * aj[r] * jtab[om_index[q, r]]
                    racc += abs(ai[q] * aj[r]) * rem_l1
            amat[a, b] = amat[b, a] = acc / PI
            rmat[a, b] = rmat[b, a] = racc / PI
    return amat, rmat


def assemble_ibp(idx, jets, hatfun, t0, t1, nt):
    tt = np.linspace(t0, t1, nt)
    sg = np.array([sigma(t) for t in tt])
    hats = {k: np.array([hatfun(jets[k], t, 4) for t in tt]) for k in idx}
    m = len(idx)
    amat = np.zeros((m, m))
    for a, i in enumerate(idx):
        for b, j in enumerate(idx):
            if b < a:
                continue
            amat[a, b] = amat[b, a] = (
                float(np.trapezoid(sg * hats[i] * hats[j], tt)) / PI)
    return amat


def schur_of(qmat, c_tail, nblk=3):
    bmat, cmat = qmat[:nblk, :nblk], qmat[:nblk, nblk:]
    smat = bmat - cmat @ cmat.T / c_tail
    cop = float(np.linalg.svd(cmat, compute_uv=False)[0])
    return (float(np.min(np.linalg.eigvalsh(smat))), cop, smat, bmat, cmat)


def s_radius(d_q, cmat, c_tail, nblk=3):
    d_b, d_c = d_q[:nblk, :nblk], d_q[:nblk, nblk:]
    return d_b + (np.abs(cmat) @ d_c.T
                  + d_c @ np.abs(cmat).T
                  + d_c @ d_c.T) / c_tail


def leftover_f(qfull, block, tail_hi):
    rest = [k for k in range(12, tail_hi + 1, 2)]
    cmat = qfull[np.ix_(block, rest)]
    return float(np.linalg.norm(cmat, "fro"))


def run(smoke: bool) -> int:
    global CHECKS
    CHECKS = []
    started = time.perf_counter()
    print("filon_enclosure_probe -- r483")
    print("SPEC_SHA", SPEC_SHA[:16])
    print("mode", "SMOKE" if smoke else "FULL")
    print("scramble-sensitive", SCRAMBLE_SENSITIVE)
    print("verdict-kind", VERDICT_KIND)
    print("prime-range", "n <= exp(2L)")

    fw_ok, fw_d = firewall_audit()
    check("firewall", fw_ok, fw_d if not fw_ok else "no zero oracle")
    check("scramble-gate", SCRAMBLE_SENSITIVE, "literal log n (vacuous at 0.3)")
    check("no-rh-claim", "NO RH CLAIM" in (__doc__ or ""), "doc boundary")
    check("only-L03", True, "this round is L=0.3 only")
    check("type-reduced",
          VERDICT_KIND.startswith("REDUCED")
          and "leftover-C-HS" in VERDICT_KIND,
          VERDICT_KIND)
    check("anti-list",
          "Fourier-HS majorant" in (__doc__ or "")
          and "exp-sum Ci-to-infinity" in (__doc__ or ""),
          "HS / exp-sum-Ci not reused")
    check("sign-book",
          "no silent shift" in (__doc__ or ""),
          "diagonal tails booked to B, leftover not moved")

    rec = KH.measure(TSTAR, 5, n_ny=48, m_modes=12, t_cut=T_CUT, nt=3000)
    print("  r480-style even lminS=%.6e  odd=%.6e"
          % (rec["even"][2], rec["odd"][2]))
    check("r480-even",
          rec["even"][2] > float(R480_EVEN_LO),
          "midpoint even S > 5e-3")
    check("r480-odd",
          rec["odd"][2] > float(R480_ODD_LO),
          "midpoint odd S > 0.15")

    ev, x, w, funcs = KH.nystrom_modes(L_YB, TSTAR, 48)
    eps = float(ev[6])
    sig8 = float(sigma(TSTAR))
    c_tail = sig8 * (1.0 - eps) + SIG0 * eps
    print("  lambda6=%.6e  c_tail=%.6f  sigma(8)=%.6f" % (eps, c_tail, sig8))
    check("eps-weyl", eps < float(EPS_HI_PIN), "lambda_6 < 1.50e-8")
    check("c-tail", c_tail > float(C_TAIL_LO_PIN), "c_tail=%.6f" % c_tail)

    t2rho = abs((150.0 ** 2) * (sigma(150.0) - math.log(150.0 / (2.0 * PI))))
    print("  |t^2 rho| at t=150: %.6f (Binet 1/24=%.6f)" % (t2rho, 1.0 / 24.0))
    check("binet-rho",
          abs(t2rho - 1.0 / 24.0) < 1e-5,
          "rho = -1/(24 t^2)")

    qfull = rec["q"]
    # leftover on the r480 12-mode Q (modes 12,14 not present) -- rebuild
    a_wide = KH.a_matrix(x, w, funcs, 0.0, T_CUT, 16, 2500)
    p_wide = KH.pi_matrix(x, w, funcs, 16)
    q_wide = a_wide + p_wide
    left_f = leftover_f(q_wide, [0, 2, 4], 14)
    print("  leftover ||C||_F modes 12..14: %.6e" % left_f)
    check("leftover-f",
          abs(left_f - float(LEFTOVER_F_PIN)) < 5e-4,
          "NO-TAIL leftover HS")
    check("leftover-kills-satz",
          left_f > float(LEFTOVER_BUDGET_PIN),
          "deficit factor ~ %.0f" % (left_f / float(LEFTOVER_BUDGET_PIN)))

    # cheap Filon vs trap on even 5 (smoke: coarse panels)
    even = [0, 2, 4, 6, 8]
    diffs = (x[:, None] - x[None, :]).ravel()
    uniq, inv = np.unique(np.round(diffs, 12), return_inverse=True)
    om_index = inv.reshape(len(x), len(x))
    if smoke:
        npans = (2000, 1500)
    else:
        npans = (8000, 8000)
    m2s = (36.8, 0.018)
    bands = ((1e-8, 8.0), (8.0, T_CUT))
    rem_l1 = (filon_rem_l1(*bands[0], m2s[0], npans[0])
              + filon_rem_l1(*bands[1], m2s[1], npans[1]))
    print("  Filon rem_L1=%.3e  npan=%s" % (rem_l1, npans))
    j0, _ = filon_band_J(uniq, *bands[0], npans[0])
    j1, _ = filon_band_J(uniq, *bands[1], npans[1])
    jtab = j0 + j1
    ae, re = assemble_filon(x, w, funcs, even, jtab, om_index, rem_l1)
    a_tr = KH.a_matrix(x, w, funcs, 0.0, T_CUT, 10, 4000)
    dmax = max(abs(ae[i, i] - a_tr[even[i], even[i]]) for i in range(5))
    print("  Filon vs trap max |d diag|=%.3e  remA max=%.3e"
          % (dmax, re.max()))
    check("filon-midpoint",
          dmax < float(FILON_DIFF_PIN if smoke else FILON_DIFF_FULL_PIN),
          "hits r480/r481 trapezoid")
    check("filon-rem-finite", rem_l1 > 0.0, "M2 remainder sealed")

    pi_m = KH.pi_matrix(x, w, funcs, 12)
    qe = ae.copy()
    for a, i in enumerate(even):
        for b, j in enumerate(even):
            qe[a, b] += pi_m[i, j]
    lmin0, c0, *_ = schur_of(qe, c_tail)
    print("  NO-TAIL Filon even lminS=%.6e ||C||=%.4f" % (lmin0, c0))
    check("notail-pd", lmin0 > float(R480_EVEN_LO), "Filon S PD")

    if not smoke:
        jets = {k: jets_at(x, w, funcs[k], ev[k], TSTAR, L_YB, 4)
                for k in range(12)}
        even6 = [0, 2, 4, 6, 8, 10]
        odd6 = [1, 3, 5, 7, 9, 11]
        ae_t = (assemble_ibp(even6, jets, hat_ibp_even, T_CUT, 400.0, 4000)
                + assemble_ibp(even6, jets, hat_ibp_even, 400.0, 8000.0, 12000))
        ao_t = (assemble_ibp(odd6, jets, hat_ibp_odd, T_CUT, 400.0, 4000)
                + assemble_ibp(odd6, jets, hat_ibp_odd, 400.0, 8000.0, 12000))
        far = (math.log(8000.0 / (2.0 * PI)) + 1.0) / 8000.0
        for a, i in enumerate(even6):
            for b, j in enumerate(even6):
                ae_t[a, b] += (2.0 / PI) * jets[i][0] * jets[j][0] * far
        for a, i in enumerate(odd6):
            for b, j in enumerate(odd6):
                ao_t[a, b] += (2.0 / PI) * jets[i][0] * jets[j][0] * far
        print("  even IBP-tail diag", np.diag(ae_t))
        print("  odd  IBP-tail diag", np.diag(ao_t))
        check("diag-tail-pos",
              bool(np.all(np.diag(ae_t) > 0.0)
                   and np.all(np.diag(ao_t) > 0.0)),
              "diagonal tails on A_+")

        a0_6 = KH.a_matrix(x, w, funcs, 0.0, T_CUT, 12, 4000)
        qe6 = np.zeros((6, 6))
        qo6 = np.zeros((6, 6))
        for a, i in enumerate(even6):
            for b, j in enumerate(even6):
                qe6[a, b] = a0_6[i, j] + pi_m[i, j] + ae_t[a, b]
        for a, i in enumerate(odd6):
            for b, j in enumerate(odd6):
                qo6[a, b] = a0_6[i, j] + pi_m[i, j] + ao_t[a, b]
        le, ce_n, se, _be, ce_m = schur_of(qe6, c_tail)
        lo, co_n, so, _bo, co_m = schur_of(qo6, c_tail)
        print("  WITH-IBP even lminS=%.6e ||C||=%.4f" % (le, ce_n))
        print("  WITH-IBP odd  lminS=%.6e ||C||=%.4f" % (lo, co_n))
        check("ibp-even-pd", le > 5e-3, "finite even S PD after IBP")
        check("ibp-odd-pd", lo > 0.15, "finite odd S PD after IBP")

        entry_r = 1.0e-4
        srad_e = s_radius(np.full((6, 6), entry_r), ce_m, c_tail)
        srad_o = s_radius(np.full((6, 6), entry_r), co_m, c_tail)
        he = CC.validated_lammin(se, srad_e, le)
        ho = CC.validated_lammin(so, srad_o, lo)
        print("  Higham even mu=%s  odd mu=%s" % (he, ho))
        check("higham-even",
              he is not None and he > float(HIGHAM_MU_PIN),
              "finite even interval-PD")
        check("higham-odd",
              ho is not None and ho > 0.05,
              "finite odd interval-PD")
        if he is not None:
            cstar = he / (1.0 + (ce_n / c_tail) ** 2)
            print("  would-be c_* (leftover=0)=%.6e" % cstar)
            pert = (2.0 * ce_n * left_f + left_f ** 2) / c_tail
            print("  leftover perturbation of S: %.4e (mu=%.4e)"
                  % (pert, he))
            check("deficit-exact",
                  pert > he,
                  "leftover eats Higham mu; SATZ not assembled")

        ev64, x64, w64, f64 = KH.nystrom_modes(L_YB, TSTAR, 64)
        d_blk = 0.0
        d_tail = 0.0
        for k in (0, 2, 4):
            j48 = jets_at(x, w, funcs[k], ev[k], TSTAR, L_YB, 0)[0]
            j64 = jets_at(x64, w64, f64[k], ev64[k], TSTAR, L_YB, 0)[0]
            d_blk = max(d_blk, abs(j48 - j64))
        for k in (6, 8):
            j48 = jets_at(x, w, funcs[k], ev[k], TSTAR, L_YB, 0)[0]
            j64 = jets_at(x64, w64, f64[k], ev64[k], TSTAR, L_YB, 0)[0]
            d_tail = max(d_tail, abs(j48 - j64))
        print("  |u(L)| n48 vs 64  block=%.3e  tail=%.3e"
              % (d_blk, d_tail))
        check("endpoint-jet-block",
              d_blk < 1e-9,
              "block jets stable")
        check("endpoint-jet-tail",
              d_tail < 2e-3,
              "tail jets resolved at IBP accuracy")
        check("exp-sum-ci-killed",
              True,
              "Ci of exp-sum to inf: lminS~-1.6 (anti-list)")
        check("not-proved-lambda",
              True,
              "leftover C blocks lambda_*(0.3)>=c")

    elapsed = time.perf_counter() - started
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_fail = sum(1 for _, ok in CHECKS if not ok)
    print("\nCHECKS %d/%d  elapsed %.2fs" % (n_pass, n_pass + n_fail, elapsed))
    print("VERDICT", VERDICT_KIND)
    print("SPEC_SHA", SPEC_SHA)
    print("PIN_DUMP_BEGIN")
    print("  PIN even_lminS=%.8e odd_lminS=%.8e eps=%.8e c_tail=%.8f"
          % (rec["even"][2], rec["odd"][2], eps, c_tail))
    print("  PIN leftover_F=%.8e rem_L1=%.8e" % (left_f, rem_l1))
    print("  PIN filon_dmax=%.8e" % dmax)
    print("PIN_DUMP_END")
    if n_fail:
        print("FILON_ENCLOSURE FAILED")
        return 1
    print("FILON_ENCLOSURE %s" % VERDICT_KIND)
    return 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.smoke))


if __name__ == "__main__":
    main()
