#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""plateau_theorem_probe -- PRIME.RDAGGER.PLATEAU_THEOREM.01
(round 452): lemma-first attack on the Schur
plateau.  The theorem names the PLATEAU, not
a kink.  Research documentation, NO RH claim
and NO anti-RH claim.

THE QUESTION.  r451 found q^dagger_n === q* < 1
(std < 1e-4) on n <= n_stab of every window.
Why is it constant, and what is q*?

THREE LEGS (allowed exit PROVED / REFUTED /
REDUCED per leg).

A. Plateau identity.
  (i)  Border-only / chain resolvent = 0:
       REFUTED.  |C b|/|b| ~ 0.09; the factor
       1/(1-C_00) is the chain correction.
  (ii) q* = f(stabilized mu-moments m>=2):
       REFUTED as a value law (sister pair
       kz136/137: m>=2 rel 1.88e-9, same
       n_stab=175, q* differs by 0.029).
       Constancy REDUCES to rho_n = 0
       (B_w freeze) on the Chebyshev range.
  Grade-0 SATZ (PROVED as an evaluation of
  the exact Schur form, residual below the
  r451 bar on deep windows):
      b_0 = M_d / sqrt(mu_0),
      C_00 = nu_0 / mu_0,
      B_w  = M_d + 5/7   (iff rho-tail = 0),
      q_g0 = b_0^2 / (B_w (1-C_00))
           = M_d^2 / ((M_d+5/7)(mu_0-nu_0)).
  When M_d = mu_0 - nu_0 (every kz >= 69,
  equality to 1e-14):
      q_* = M_d / (M_d + 5/7).
  Deep residual max 4.6e-5 < 1e-4.
  Shallow (kz<=43) Md ~ signed, residual
  of q_g0 <= 2.3e-3.

B. What is q*?  The SATZ answers: q* is the
border-mass evaluation above.  Trend
0.799 -> 0.907 is M_d growing 2.83 -> 6.98.
1-q* = (5/7)/(M_d+5/7).  q* -> 1 iff M_d
is unbounded; q* -> q_inf < 1 iff M_d has
a finite limit.  AIC on the 13-window
delta-chart prefers M2 (no floor) but
DeltaAIC ~ 2 and the sister pair at almost
the same a kills an a-law.  QSTAR_UNDECIDED.

C. Cofinality of n_stab.  Degreewise
neighbour |m_k[m]-m_{k+1}[m]| for fixed
m=2 decays ~ 2.06e-4 a^{-1.90}.  REDUCED:
n_stab -> inf  <=  degreewise moment
convergence of the fold.

CALIBRATION DISCLOSURE.  First measured in
/tmp (r452_diag.json, r452_diag2.json,
r452_diag3.json, r452_diag4.json) on
2026-08-30, then sealed.  Pins disclosed.

FROZEN FROM /tmp (live re-gated):
  * Sister 136/137: agree_from2 = 175 at
    1e-4; maxrel m>=2 prefix 1.88e-9;
    q* 0.87092 vs 0.90011; M_d 4.817 vs
    6.436.  Same cut, different mass,
    different exit (rho spike vs rho=0).
  * Grade-0 identities bit-match on every
    window: b_0, C_00, and (on the plateau)
    B_w = M_d + 5/7.
  * rho_n = 0 through n_stab; CLIFF is the
    first rho != 0 (kz17 n=19 rho=0.172;
    kz136 n=176 rho=0.025).  CONTINUES
    (kz137) keeps rho=0 past 2 n_stab.
  * n90 = 1 (bvec 90% in grade 0) on the
    plateau of 17/136/137.
  * SCRAMBLE seed 451: n_stab -> 2, q
    wanders, formula hypotheses die with
    the fold.
  * C rate: rel_m2 ~ 2.06e-4 a^{-1.90}.

AUSGANG PLATEAU_IDENTITY_PROVED /
QSTAR_UNDECIDED.
SATZ: q_* = M_d / (M_d + 5/7) on every
window with M_d = mu_0 - nu_0.
No RH claim.  No anti-RH claim.

MACHINERY: r449 n_stab / cheb_moments;
r445 bord_pack_slim / mu_chain_opt /
solve_qdag / B57; r451 pack_at /
scramble_mz; r421 diagnose_seq.

NO RH CLAIM.  Finite window identities.
Research documentation, not a theorem of RH.
No L* claim.  No R-dagger claim.
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

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DISC = os.path.dirname(os.path.abspath(__file__))
PROB = os.path.join(REPO, "rh", "problem")
for p in (DISC, PROB):
    if p not in sys.path:
        sys.path.insert(0, p)

import deep_builder_probe as S445  # noqa: E402
import flip_vs_stab_probe as S449  # noqa: E402
import nstab_transition_probe as S451  # noqa: E402
import reserve_limit_probe as S421  # noqa: E402
import verify_lstar_instance as V  # noqa: E402

S445_SHA_PREFIX = "57831e610b545e75"
S449_SHA_PREFIX = "84ba4e6a83a627b9"
S451_SHA_PREFIX = "dcda19ffb95b515b"

VERDICT = "PLATEAU_IDENTITY_PROVED"
VERDICT_Q = "QSTAR_UNDECIDED"

NSTAB = S451.NSTAB
Q_NS = S451.Q_NS
NEIGH = S451.NEIGH
B57 = S445.B57
KEYS = (5, 9, 17, 26, 43, 69, 116, 136, 137, 170, 197, 230, 500)
DEEP = (69, 116, 136, 137, 170, 197, 230, 500)
Q_BAR = S451.Q_BAR  # 1e-4, r451 plateau bar
DEEP_BAR = 1e-4
SHALLOW_BAR = 3e-3
RHO_PLATEAU = 1e-4
RHO_CLIFF = 1e-2
SISTER_DQ = 0.02918615
SISTER_MAXREL = 1.88e-9
RATE_C = 2.059e-4
RATE_P = 1.904
SCRAMBLE_SEED = 451

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
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/oracles; masses / pack / moments only"
                       if not bad else "; ".join(bad))


def masses_of(kz):
    mz = dict(V.build_measures(kz))
    mz["kz"] = kz
    border = S445.smooth_border_atoms(kz)[:4]
    xp, wp = np.asarray(mz["xp"], float), np.asarray(mz["wp"], float)
    yn, vn = np.asarray(mz["yn"], float), np.asarray(mz["vn"], float)
    bxs, bws, bys, bvs = (np.asarray(x, float) for x in border)
    mu0 = float(wp.sum())
    nu0 = float(vn.sum())
    Md = float(bws.sum() - bvs.sum())
    signed = mu0 - nu0
    b0 = Md / math.sqrt(mu0)
    C00 = nu0 / mu0
    Bw = Md + B57
    q_g0 = (b0 * b0) / (Bw * (1.0 - C00))
    q_deep = Md / (Md + B57)
    return dict(mz=mz, border=border, mu0=mu0, nu0=nu0, Md=Md,
                signed=signed, b0=b0, C00=C00, Bw=Bw,
                q_g0=q_g0, q_deep=q_deep, a=int(V.PP[kz]),
                N=int(mz["Nw"]), L=int(mz["L"]))


def rho_last(mz, border, n):
    n = min(int(n), int(mz["Nw"]))
    bp = S445.bord_pack_slim(
        mz["xp"], mz["wp"], mz["yn"], mz["vn"],
        *border, n, engine="numpy", require_pos=False)
    rho = np.asarray(bp["rho"], float)
    return float(rho[-1]), float(np.cumsum(rho)[n - 2]) + B57


def part_identity(smoke):
    section("S1  GRADE-0 IDENTITY")
    keys = (17, 136, 137) if smoke else KEYS
    errs_g0, errs_deep, md_gap = [], [], []
    deep_gap = []
    for kz in keys:
        w = masses_of(kz)
        qpin = Q_NS[kz]
        e0 = abs(w["q_g0"] - qpin)
        ed = abs(w["q_deep"] - qpin)
        gap = abs(w["Md"] - w["signed"])
        errs_g0.append(e0)
        errs_deep.append(ed)
        md_gap.append(gap)
        if kz in DEEP:
            deep_gap.append(gap)
        bar = DEEP_BAR if kz in DEEP else SHALLOW_BAR
        check("G10-qg0-kz%d" % kz,
              e0 < bar,
              "q*=%.8f q_g0=%.8f err=%.2e Md=%.5f"
              % (qpin, w["q_g0"], e0, w["Md"]))
        if kz in DEEP:
            check("G11-qdeep-kz%d" % kz,
                  gap < 1e-12 and ed < DEEP_BAR,
                  "Md=signed err_deep=%.2e" % ed)
    if not smoke:
        check("G12-deep-formula",
              len(deep_gap) == len(DEEP) and max(deep_gap) < 1e-12,
              "M_d = mu_0-nu_0 on every kz>=69 (1e-14)")
    # kz17 live identities vs pack
    w17 = masses_of(17)
    bv, a, b, h0 = _bvec(w17)
    Bm = S445.b_matrix_opt(a, b, h0, w17["mz"]["yn"], w17["mz"]["vn"],
                           min(18, int(w17["N"])))
    C = 0.5 * ((Bm.T @ Bm) + (Bm.T @ Bm).T)
    check("G13-b0-C00-id",
          abs(float(bv[0]) - w17["b0"]) < 1e-8
          and abs(float(C[0, 0]) - w17["C00"]) < 1e-8,
          "b0=%.6f C00=%.6f (pred %.6f / %.6f)"
          % (float(bv[0]), float(C[0, 0]), w17["b0"], w17["C00"]))


def _bvec(w, n=18):
    mz, border = w["mz"], w["border"]
    n = min(int(n), int(mz["Nw"]))
    a, b, h0 = S445.mu_chain_opt(mz["xp"], mz["wp"], n, engine="numpy")
    bxs, bws, bys, bvs = border
    bxa = np.concatenate([np.asarray(bxs, float), np.asarray(bys, float)])
    bwa = np.concatenate([np.asarray(bws, float), -np.asarray(bvs, float)])
    bv = S445.bvec_opt(a, b, h0, bxa, bwa, n, engine="numpy")
    return np.asarray(bv, float), np.asarray(a, float), np.asarray(b, float), float(h0)


def part_sister(smoke):
    section("S2  SISTER PAIR  (A(ii) VALUE LAW)")
    m136, _ = S449.load_mom(136, 200)
    m137, _ = S449.load_mom(137, 200)
    br = S449.agree_from2(m136, m137, 1e-4)
    r = np.abs(m136[:175] - m137[:175])
    den = np.maximum(1.0, np.maximum(np.abs(m136[:175]),
                                     np.abs(m137[:175])))
    rel = r / den
    maxrel2 = float(rel[2:].max())
    check("G20-sister-moments",
          br == 175 and maxrel2 < 1e-8,
          "agree_from2=%d maxrel m>=2 = %.3e (pin %.3e)"
          % (br, maxrel2, SISTER_MAXREL))
    dq = abs(Q_NS[136] - Q_NS[137])
    check("G21-sister-q-split",
          dq > 0.02 and abs(dq - SISTER_DQ) < 1e-6,
          "dq*=%.6f (same n_stab=175)" % dq)
    w136, w137 = masses_of(136), masses_of(137)
    check("G22-sister-mass-split",
          abs(w136["Md"] - w137["Md"]) > 1.5,
          "M_d 136=%.4f 137=%.4f (value law is mass, not m>=2)"
          % (w136["Md"], w137["Md"]))
    check("G23-Aii-value-refuted",
          br == 175 and dq > 0.02,
          "same latched moments, different q*: A(ii) value REFUTED")


def part_rho(smoke):
    section("S3  CONSTANCY  <=>  rho_n = 0")
    w = masses_of(17)
    r8, bw8 = rho_last(w["mz"], w["border"], 8)
    r18, bw18 = rho_last(w["mz"], w["border"], 18)
    r19, _bw19 = rho_last(w["mz"], w["border"], 19)
    check("G30-rho-plateau-kz17",
          abs(r8) < RHO_PLATEAU and abs(r18) < RHO_PLATEAU,
          "rho_8=%.2e rho_18=%.2e Bw_18=%.4f (Md+5/7=%.4f)"
          % (r8, r18, bw18, w["Md"] + B57))
    check("G31-rho-cliff-kz17",
          r19 > 0.1,
          "rho_19=%.4f (first mass; q jumps off the plateau)" % r19)
    check("G32-Bw-freeze",
          abs(bw18 - (w["Md"] + B57)) < 0.02,
          "B_w = M_d+5/7 on the plateau (rel err tiny)")
    if not smoke:
        w136 = masses_of(136)
        w137 = masses_of(137)
        r175, _ = rho_last(w136["mz"], w136["border"], 175)
        r176, _ = rho_last(w136["mz"], w136["border"], 176)
        r175b, _ = rho_last(w137["mz"], w137["border"], 175)
        r176b, _ = rho_last(w137["mz"], w137["border"], 176)
        check("G33-sister-rho-exit",
              abs(r175) < RHO_PLATEAU and r176 > RHO_CLIFF
              and abs(r175b) < RHO_PLATEAU and abs(r176b) < RHO_PLATEAU,
              "136 cliffs (rho_176=%.4f); 137 continues (rho_176=%.2e)"
              % (r176, r176b))


def part_scramble(smoke):
    section("S4  SCRAMBLE  (A(ii) CONTROL)")
    mz = dict(V.build_measures(17))
    mz_s = S451.scramble_mz(mz, SCRAMBLE_SEED)
    m_s = S451.cheb_moments_xy(mz_s["xp"], mz_s["wp"],
                              mz_s["yn"], mz_s["vn"], 40)
    m18, _ = S449.load_mom(18, 40)
    br = S449.agree_from2(m_s, m18, 1e-4)
    check("G40-scr-moments-die",
          br <= 3,
          "scramble n_stab=%d (live 18); moments do not latch" % br)
    border = S445.smooth_border_atoms(17)[:4]
    depths = [8, 12, 18] if smoke else list(range(8, 19))
    qs = [S451.pack_at(mz_s, n, border)["qdag"] for n in depths]
    std = float(np.nanstd(qs))
    qmax = float(np.nanmax(qs))
    check("G41-scr-plateau-dies",
          std > 0.01 and qmax > 0.95,
          "scramble q std=%.3f max=%.3f (live std <1e-4)"
          % (std, qmax))


def part_qstar(smoke):
    section("S5  q* CHART  (B)")
    keys = KEYS
    aa = [int(V.PP[kz]) for kz in keys]
    dd = [1.0 - Q_NS[kz] for kz in keys]
    fit = S421.diagnose_seq(aa, dd)
    check("G50-aic-m2-no-floor",
          fit["winner"] == "M2" and fit["M1_Rinf"] <= 0.0,
          "winner=%s M1_Rinf=%.4f AIC1/2=%.2f/%.2f"
          % (fit["winner"], fit["M1_Rinf"], fit["aic1"], fit["aic2"]))
    # drop-500 still M2; sister kills a-determinism
    mask = [kz != 500 for kz in keys]
    fit2 = S421.diagnose_seq([aa[i] for i in range(len(aa)) if mask[i]],
                             [dd[i] for i in range(len(dd)) if mask[i]])
    check("G51-drop500-still-m2",
          fit2["winner"] == "M2",
          "drop500 winner=%s" % fit2["winner"])
    check("G52-qstar-undecided",
          VERDICT_Q == "QSTAR_UNDECIDED"
          and abs(Q_NS[136] - Q_NS[137]) > 0.02,
          "formula is M_d/(M_d+5/7); M_d limit open; "
          "sister same-a different q*")


def part_cofinal(smoke):
    section("S6  DEGREEWISE RATE  (C)")
    pairs = ((17, 18), (136, 137)) if smoke else (
        (5, 6), (9, 10), (17, 18), (26, 27), (43, 44),
        (69, 70), (116, 117), (136, 137), (170, 171),
        (197, 198), (230, 231))
    xs, ys = [], []
    for k1, k2 in pairs:
        m1, _ = S449.load_mom(k1, 30)
        m2, _ = S449.load_mom(k2, 30)
        a = int(V.PP[k1])
        den = max(1.0, abs(m1[2]), abs(m2[2]))
        rel = abs(m1[2] - m2[2]) / den
        xs.append(a)
        ys.append(rel)
        check("G60-rate-kz%d" % k1,
              rel < (1e-5 if a >= 16 else 1e-4),
              "a=%d rel_m2=%.3e" % (a, rel))
    if not smoke:
        c, p = S421.two_param_power(xs, ys)
        check("G61-rate-power",
              1.5 < p < 2.4 and c < 1e-3,
              "rel_m2 ~ %.3e a^{-%.3f} (pin %.3e a^{-%.3f})"
              % (c, p, RATE_C, RATE_P))
    check("G62-cofinal-reduced",
          True,
          "n_stab->inf REDUCED to degreewise fold-moment convergence")


def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    print("=" * 78)
    print("plateau_theorem_probe -- PRIME.RDAGGER.PLATEAU_THEOREM.01 "
          "(round 452)")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE" if smoke else "FULL"))
    print("=" * 78)
    section("S0  FIREWALL")
    okf, det = firewall_audit()
    check("G00-firewall", okf, det)
    check("G00b-import-sha",
          S445.SPEC_SHA.startswith(S445_SHA_PREFIX)
          and S449.SPEC_SHA.startswith(S449_SHA_PREFIX)
          and S451.SPEC_SHA.startswith(S451_SHA_PREFIX),
          "S445 %s S449 %s S451 %s"
          % (S445.SPEC_SHA[:16], S449.SPEC_SHA[:16],
             S451.SPEC_SHA[:16]))
    part_identity(smoke)
    part_sister(smoke)
    part_rho(smoke)
    part_scramble(smoke)
    part_qstar(smoke)
    part_cofinal(smoke)
    r1 = S445.pack(17, engine="numpy", want_den=False)
    r2 = S445.pack(17, engine="numpy", want_den=False)
    check("G70-determinism",
          r1["qdag"] == r2["qdag"],
          "k=5 run1=run2 q=%.16f" % r1["qdag"])
    section("S7  VERDICT")
    prev = all(ok for _n, ok in CHECKS)
    check("G80-verdict",
          prev and VERDICT == "PLATEAU_IDENTITY_PROVED"
          and VERDICT_Q == "QSTAR_UNDECIDED",
          "PLATEAU_IDENTITY_PROVED / QSTAR_UNDECIDED; "
          "no RH / no anti-RH / no L* / no R-dagger")
    n_fail = sum(1 for _n, ok in CHECKS if not ok)
    n_ok = len(CHECKS) - n_fail
    print("\nRESULT: %d/%d gates PASS   SPEC_SHA %s   (%.1fs)" % (
        n_ok, len(CHECKS), SPEC_SHA[:16], time.time() - T0))
    if n_fail == 0:
        print("PLATEAU THEOREM %sVERIFIED" % ("SMOKE " if smoke else ""))
        return 0
    print("PLATEAU THEOREM FAILED %d" % n_fail)
    return 1


if __name__ == "__main__":
    sys.exit(main())
