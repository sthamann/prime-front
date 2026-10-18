#!/usr/bin/env python3
"""prime_family_depth_probe -- does the certified pole x alias FAMILY
hold its floor share at the new deep rungs where the single pair dies?

EXPLORATION ONLY (experiments/): no verification claim, no ledger row,
no paper edit.  NO RH claim anywhere.  Frozen before running.

CONTEXT.  floor_envelope_depth_probe (ENVELOPE-HOLDS-DEEP) typed the
S5.HLAW miss: the single certified pair (pole, gamma_1) collapses at
depth -- gap rho/rho_cert widens 40x -> 673x across X = 18.375..25.5.
But prime_floor_theorem_probe's Piece 3 certified the pole x gamma_k
FAMILY (top-K = 100, per-rung psd chain) at 0.93..0.97 of the floor --
measured only on the old 15-window ladder (alpha <= 6.146).  This probe
re-runs the family certification on the six deep tower rungs.

TASK / FROZEN DESIGN
S1  RECONSTRUCT + REPRODUCTION WARD: the old 15-window Piece-3 numbers
    rerun verbatim (pp.components_of on lg.lock_block windows; family
    x_pz = a_z b_pole - b_z a_pole; cert100 = top-100 sum; per-rung
    chain lambda_min(A2 - M2) >= 0 with float budget
    bud = 100 eps (|A2|_F^2 + |M2|_F^2); cert_frac =
    (cert100 - bud)/det A2).  Ward: min/max cert_frac reproduce the
    cited 0.93 / 0.97 within +-0.01; pole-family/pair-total >= 0.999;
    lambda_min(R) >= 0 on all rungs.
S2  DEEP INSTRUMENT: the banded segmented sieve of the depth probe
    (imported READ-ONLY), same predeclared cap rule t_proj <= 1500 s
    (PREDECLARATION: X = 25.5 is included iff its projection passes,
    as in the parent run where it projected ~1130 s); the certified
    lambda_min anchors re-checked (rel <= 2e-2).
S3  THE DEPTH TEST per deep rung (D = 1/64 tower frames):
      A2 = lag-route lock block; det A2 = lambda tau (floor);
      (a, b) = zero components (RS-scan zeros <= T_SCAN = 2e4) + pole;
      M2 = 2x2 gram, det M2; the EXACT decomposition of the floor:
        det A2 = cert100 + fam_ranks(101..K2) + fam_tail + zz + resid
        (top-100 family / next-100 family / remaining pole x zero /
         zero x zero pairs / the > 2e4 remainder's det share);
      IDENTITY WARD: pair-scan SOS total == det M2 with the
        conditioning-aware bar max(1e-8, 64 eps (|M11 M22| + M12^2)
        / |det M2|) -- declared: at depth the 2x2 det is a ~1e10-
        conditioned difference (v818 FACT_COND_FAC convention); the
        SOS side is a sum of non-negatives (stable);
      PSD CHAIN AT DEPTH: lambda_min(A2 - M2) >= 0 per rung (the
        decision-(c) gate), resolvability vs the float budget typed;
      ALPHA-COVERAGE TYPING: the citation-grade sharpened chain of
        prime_tail_envelope_probe evaluated verbatim per deep rung
        (env_c = (4/D) num_sup(delta <= 1/2) sh_sum(T_ver = 3e12)
        + eps_f; pert = env s1n + 2 env^2; family gate
        pert < cert100, pair gate pert < X^2(gamma_1)) against the
        cited horizon alpha* ~ 11: deep alphas 9.19..12.75 straddle
        it -- which rungs carry citation grade vs per-rung verified
        grade is TYPED, with the eps_arch (GL-48->96 x 10) and
        eps_f terms printed so the binding term is named honestly.
S4  DECISION (frozen order): (c) any lambda_min(A2 - M2) < 0 ->
    CHAIN-BREAKS (depth limit typed); else (a) cert_frac >= 0.90 at
    ALL deep rungs -> FAMILY-SCALES; else (b) FAMILY-DECAYS with the
    loss localized by the exact decomposition above (K doubled:
    ranks 101..200 gain; family tail; zero x zero; residue) and the
    Lagrange pair census (top-10 carriers labeled, alias identity
    gamma D / 2 pi) at the deepest affordable rung.
S5  SYNTHESIS: per deep rung rho_cert_fam = (cert100 - bud)/(lambda
    tau_pnt) vs measured rho; gap_fam = rho/rho_cert_fam = 1/cert_frac
    vs the single-pair gap (the parent's 40x -> 673x trend).
CONTROLS: C1 [must-fire] scramble at M = 1176 (uniform positions,
    same masses, seed 7): lambda_min(A2_scr - M2) < 0 (the psd chain
    refuses the scrambled comb) and the family share collapses
    (typed); C2 budget ward: the top-3 family carriers at the deepest
    rung recomputed in mpmath (dps 40), rel dev <= 1e-8 (the float
    certified values contain the high-precision evaluation); C3 the
    two independent pair implementations agree (pair_brick vs
    x_pz[0]^2, rel <= 1e-9).
VERDICT (frozen): FAMILY-SCALES / FAMILY-DECAYS / CHAIN-BREAKS.

FIREWALL: v563 / v684 / v692 / parent probes READ-ONLY; zero values
used openly (on-line by computation <= 2e4 via the parent's RS scan,
citation horizon 3e12 [Platt-Trudgian] in the tail chain); RNG only
in the declared C1 scramble (seed 7).  Report only, nothing written.
"""

import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break
sys.path.insert(0, _here)

import v563_paper2_readouts as core          # noqa: E402 (READ-ONLY)
import v692_rank3_lockgram as lg             # noqa: E402 (READ-ONLY)
import prime_lagrange_pair_probe as pp       # noqa: E402 (READ-ONLY)
import prime_floor_theorem_probe as ft       # noqa: E402 (READ-ONLY)
import prime_tail_envelope_probe as tp       # noqa: E402 (READ-ONLY)
import floor_envelope_depth_probe as fdp     # noqa: E402 (READ-ONLY)
from mpmath import mp, mpf, mpc, sin as msin, sinh as msinh, \
    exp as mexp, sqrt as msqrt, re as mre  # noqa: E402 (VALUES only)

T0 = time.time()
FAILS = []
N_CHK = 0

# ------------------------------------------------- frozen bars / constants
K_FAM = ft.K_FAM              # certified family size (100, frozen)
K_DBL = 2 * K_FAM             # the decision-(b) K-doubling diagnostic
FAM_BAR = 0.90                # decision-(a) per-rung certified share bar
REPRO_MM = (0.93, 0.97)       # cited old-ladder cert_frac min/max
REPRO_TOL = 0.01              # printed-precision reproduction tolerance
FAM_PAIR_TOT = ft.FAM_PAIR_TOT   # pole family / pair total (0.999)
WARD_REL = pp.WARD_REL        # identity ward base bar (1e-8)
COND_FAC = 64.0               # v818 FACT_COND_FAC conditioning convention
IMAG_BAR_DEEP = 1.0e-8        # phase residual bar at depth (declared:
#   arguments (M-1) D gamma / 2 reach ~2.5e5 rad; float argument
#   reduction scales the parent's 1e-9 bar by ~one decade)
CHAIN_FAC = ft.CHAIN_FAC      # float chain budget factor (100)
T_VER = tp.T_VER              # citation horizon 3e12 (Platt-Trudgian)
ALPHA_STAR_CITED = 11.0       # tail-probe fitted alpha-horizon (cited)
MP_DPS = 40                   # budget-ward working precision
BW_TOP = 3                    # carriers recomputed in mpmath
BW_REL = 1.0e-8               # budget-ward bar
PB_REL = 1.0e-9               # C3 cross-implementation bar
EPSM = float(np.finfo(float).eps)
DGRID = fdp.DGRID
TARGET_MS = fdp.TARGET_MS
ANCHOR_MS = fdp.ANCHOR_MS
LAM_CITED = fdp.LAM_CITED
SEED_SCRAMBLE = fdp.SEED_SCRAMBLE


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def fam_numbers(w, gam, A2, det_a2):
    """The Piece-3 family certification numbers on one window dict
    (needs f1, f2, D, M).  Returns the full exact decomposition."""
    a, b, meta = pp.components_of(w, gam)
    M2 = np.array([[float(a @ a), float(a @ b)],
                   [float(a @ b), float(b @ b)]])
    det_m2 = float(np.linalg.det(M2))
    x_pz = a[:-1] * b[-1] - b[:-1] * a[-1]
    x2 = x_pz ** 2
    order = np.argsort(x2)[::-1]
    top = x2[order]
    fam_tot = float(np.sum(x2))
    cert1 = float(np.sum(top[:K_FAM]))
    cert2 = float(np.sum(top[:K_DBL]))
    bud = CHAIN_FAC * EPSM * (float(np.linalg.norm(A2)) ** 2
                              + float(np.linalg.norm(M2)) ** 2)
    lam_r = ft.eig2_min(A2 - M2)
    return dict(a=a, b=b, meta=meta, M2=M2, det_m2=det_m2,
                x_pz=x_pz, order=order,
                fam_tot=fam_tot, cert1=cert1, cert2=cert2, bud=bud,
                lam_r=lam_r,
                fam_pt=fam_tot / det_m2,
                cert_frac=(cert1 - bud) / det_a2,
                cert_frac2=(cert2 - bud) / det_a2,
                residue=1.0 - det_m2 / det_a2,
                x2_g1=float(x2[0]))


def mp_family_term(f1, f2, D, Mz, g):
    """One family term x_pz(gamma)^2 in mpmath (budget ward C2)."""
    mp.dps = MP_DPS
    Dm, gm = mpf(D), mpf(repr(float(g)))
    jj = range(Mz)
    # zero legs: F = sum f_j e^{i j D g}; S = Re(0.5i e^{-i(M-1)Dg/2} F)
    ph = [mexp(mpc(0, 1) * Dm * gm * j) for j in jj]
    F1 = sum(mpf(repr(float(f1[j]))) * ph[j] for j in jj)
    F2 = sum(mpf(repr(float(f2[j]))) * ph[j] for j in jj)
    rot = mexp(-mpc(0, 1) * (Mz - 1) * Dm * gm / 2) * mpc(0, "0.5")
    hw = Dm * gm / 2
    wg = Dm * (msin(hw) / hw) ** 2
    a_z = 2 * msqrt(wg) * mre(rot * F1)
    b_z = 2 * msqrt(wg) * mre(rot * F2)
    # pole layer via T at +-i/2 (real arithmetic in mp)
    dec = [mexp(-Dm * j / 2) for j in jj]
    grw = [mexp(Dm * j / 2) for j in jj]
    Fm = {}
    for tag, f in (("1", f1), ("2", f2)):
        Fm["p" + tag] = sum(mpf(repr(float(f[j]))) * dec[j] for j in jj)
        Fm["m" + tag] = sum(mpf(repr(float(f[j]))) * grw[j] for j in jj)
    cs = msinh(Dm / 4) / (Dm / 4)
    pref = cs * cs * Dm / 2
    P = {}
    for (i, j), (fa, fb) in {(0, 0): ("1", "1"), (1, 1): ("2", "2"),
                             (0, 1): ("1", "2")}.items():
        # sum over z = +i/2 and -i/2 doubles the symmetric product
        tsum = pref * (Fm["p" + fa] * Fm["m" + fb]
                       + Fm["p" + fb] * Fm["m" + fa])
        P[(i, j)] = P[(j, i)] = -tsum          # -0.5 * (2 tsum) * ... 
    # 2x2 eigen (closed form)
    mid = (P[(0, 0)] + P[(1, 1)]) / 2
    rad = msqrt(((P[(0, 0)] - P[(1, 1)]) / 2) ** 2 + P[(0, 1)] ** 2)
    lmax = mid + rad
    v0, v1 = P[(0, 1)], lmax - P[(0, 0)]
    nrm = msqrt(v0 * v0 + v1 * v1)
    sq = msqrt(lmax if lmax > 0 else mpf(0))
    vp0, vp1 = sq * v0 / nrm, sq * v1 / nrm
    x = a_z * vp1 - b_z * vp0
    return float(x * x)


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("THE FAMILY AT DEPTH -- does the certified pole x alias "
          "family scale?")
    print("(prime_family_depth_probe, exploration only, no RH claim)")
    print("=" * 78)

    # ============================================================== S1
    print("\nS1 -- RECONSTRUCT + reproduction ward (old 15-window "
          "ladder, Piece-3 rerun)")
    gam, n_rvm = pp.zero_list()
    check("S1.Z zero list: %d zeros to T = 2e4 (RvM dev %.2f <= 3)"
          % (len(gam), abs(len(gam) - n_rvm)),
          abs(len(gam) - n_rvm) <= 3.0)
    g1 = float(gam[0])
    KZ = core.frame_a_zones()
    L15 = len(KZ)
    fam5 = [0, (L15 - 1) // 4, L15 // 2, (3 * (L15 - 1)) // 4, L15 - 1]
    inter = []
    for (lo_i, hi_i), n_in in zip(zip(fam5[:-1], fam5[1:]), (2, 3, 3, 2)):
        for j in range(1, n_in + 1):
            inter.append(lo_i + j * (hi_i - lo_i) // (n_in + 1))
    idx15 = sorted(set(fam5 + inter))
    wins = [lg.lock_block(KZ[i]) for i in idx15]
    wins = [w for w in wins if w["complete"]]
    wins.sort(key=lambda w: w["alpha"])
    print("    %5s %6s | %8s %8s | %10s | %8s"
          % ("h", "alpha", "fam/pt", "cert/fl", "lam_min(R)", "residue"))
    for w in wins:
        det_a2 = float(np.linalg.det(w["A2"]))
        fn = fam_numbers(w, gam, w["A2"], det_a2)
        w.update(fn, det_a2=det_a2)
        print("    %5d %6.3f | %8.5f %8.4f | %10.2e | %8.4f"
              % (w["h"], w["alpha"], fn["fam_pt"], fn["cert_frac"],
                 fn["lam_r"], fn["residue"]))
    cf = [w["cert_frac"] for w in wins]
    lam_r_min_old = min(w["lam_r"] for w in wins)
    rep_ok = (abs(min(cf) - REPRO_MM[0]) <= REPRO_TOL
              and abs(max(cf) - REPRO_MM[1]) <= REPRO_TOL)
    check("S1.REPRO the old-ladder certified family shares reproduce: "
          "cert_frac %.4f..%.4f vs cited %.2f..%.2f (tol %.2f)"
          % (min(cf), max(cf), REPRO_MM[0], REPRO_MM[1], REPRO_TOL),
          rep_ok)
    check("S1.CHAIN old ladder: pole family >= %.3f of the pair total "
          "on every rung (min %.5f) and lambda_min(A2 - M2) = %.1e "
          ">= 0 on all 15" % (FAM_PAIR_TOT,
                              min(w["fam_pt"] for w in wins),
                              lam_r_min_old),
          min(w["fam_pt"] for w in wins) >= FAM_PAIR_TOT
          and lam_r_min_old >= 0.0)

    # ============================================================== S2
    print("\nS2 -- the deep instrument (banded sieve, predeclared cap "
          "rule t_proj <= %.0f s)" % fdp.T_CAP)
    ms_all = sorted(set(TARGET_MS) | set(ANCHOR_MS))
    caps_all = [fdp.nmax_of_M(M) for M in ms_all]
    Mpad = max(ms_all) + 3
    acc = {b: np.zeros(Mpad) for b in range(len(ms_all))}
    cnt = {b: 0 for b in range(len(ms_all))}
    n_1176 = fdp.nmax_of_M(1176)
    t0 = time.time()
    masses_scr = fdp.seg_sieve_bands(caps_all, 0, n_1176, acc, Mpad,
                                     cnt, collect_mass_cap=n_1176)
    t_bench = time.time() - t0
    proj = {M: t_bench * (fdp.nmax_of_M(M) / n_1176) * fdp.PROJ_SAFETY
            for M in ms_all}
    deep_ms = [M for M in TARGET_MS if proj[M] <= fdp.T_CAP]
    print("    benchmark: %d atoms to n = %d in %.1f s; cap rule "
          "keeps %s" % (cnt[0], n_1176, t_bench,
                        ", ".join("M=%d" % M for M in deep_ms)))
    for M in TARGET_MS:
        if M not in deep_ms:
            print("    DROPPED by the predeclared rule: M = %d "
                  "(t_proj = %.0f s)" % (M, proj[M]))
    n_deep = fdp.nmax_of_M(max(deep_ms))
    t0 = time.time()
    fdp.seg_sieve_bands(caps_all, n_1176, n_deep, acc, Mpad, cnt)
    print("    deep sieve to n = %d: %.1f s (projected %.0f s)"
          % (n_deep, time.time() - t0, proj[max(deep_ms)]))

    def c_of(M):
        nm = fdp.nmax_of_M(M)
        c = np.zeros(M)
        for b, cap in enumerate(caps_all):
            if cap <= nm:
                c += acc[b][:M]
        return c

    import v755_simpler_schur_recursion as srp   # READ-ONLY
    anch_ok = True
    for M in [M for M in ANCHOR_MS
              if fdp.nmax_of_M(M) <= n_deep]:
        cT = srp.continuum_lags(M)[:M] + c_of(M)[:M]
        lamM = float(sla.eigvalsh(sla.toeplitz(cT),
                                  subset_by_index=[0, 0])[0])
        rel = abs(lamM - LAM_CITED[M]) / LAM_CITED[M]
        anch_ok = anch_ok and rel <= fdp.ANCH_REL
    check("S2.ANCH the certified-rung lambda_min anchors reproduce "
          "(rel <= %.2f) on every built certified rung" % fdp.ANCH_REL,
          anch_ok)

    # ============================================================== S3
    print("\nS3 -- THE DEPTH TEST (family certification per deep rung)")
    deep = []
    for M in deep_ms:
        dw = fdp.deep_window(M, c_of(M))
        ev = fdp.floor_eval(dw["t1"], dw["t2"], dw["W11"], dw["W22"],
                            dw["W12"], dw["c_ar"], dw["c_at"], DGRID,
                            M, full_geo=False)
        cc = dw["c_ar"] + dw["c_at"]
        A2 = np.array([[cc @ dw["W11"], cc @ dw["W12"]],
                       [cc @ dw["W12"], cc @ dw["W22"]]])
        det_a2 = ev["lam"] * ev["tau"]
        wd = dict(f1=fdp.odd_ext(dw["t1"], M), f2=fdp.odd_ext(dw["t2"], M),
                  D=DGRID, M=M, h=M // 2)
        t0 = time.time()
        fn = fam_numbers(wd, gam, A2, det_a2)
        ev.update(fn, M=M, X=M * DGRID, alpha=dw["alpha"], dw=dw,
                  wd=wd, A2=A2, det_a2=det_a2, t_fam=time.time() - t0)
        deep.append(ev)
    print("    %5s %7s %6s | %8s %8s %8s | %10s %9s | %8s"
          % ("M", "X", "alpha", "fam/pt", "cert/fl", "c2/fl",
             "lam_min(R)", "bud", "residue"))
    for ev in deep:
        print("    %5d %7.3f %6.2f | %8.5f %8.4f %8.4f | %10.2e "
              "%9.1e | %8.4f"
              % (ev["M"], ev["X"], ev["alpha"], ev["fam_pt"],
                 ev["cert_frac"], ev["cert_frac2"], ev["lam_r"],
                 ev["bud"], ev["residue"]))
    # meta wards at depth
    im_max = max(ev["meta"]["imag_res"] for ev in deep)
    pd_max = max(ev["meta"]["pole_dev"] for ev in deep)
    check("S3.META phase extraction + pole rank-one at depth: "
          "imag_res <= %.1e (bar %.0e, declared for the deep phase "
          "scale), pole_dev <= %.1e"
          % (im_max, IMAG_BAR_DEEP, pd_max),
          im_max <= IMAG_BAR_DEEP and pd_max <= 1.0e-8)
    # identity ward (SOS == det, conditioning-aware bar)
    id_ok = True
    print("    identity ward (Lagrange SOS == det M2):")
    for ev in deep:
        tot, top_pairs = pp.pair_scan(ev["a"], ev["b"], pp.K_TOP)
        M2 = ev["M2"]
        cond = (abs(M2[0, 0] * M2[1, 1]) + M2[0, 1] ** 2) \
            / max(abs(ev["det_m2"]), 1e-300)
        bar = max(WARD_REL, COND_FAC * EPSM * cond)
        rel = abs(tot - ev["det_m2"]) / max(abs(ev["det_m2"]), 1e-300)
        ev.update(sos_rel=rel, sos_bar=bar, top_pairs=top_pairs)
        id_ok = id_ok and rel <= bar
        print("      M = %4d: rel dev %.2e <= bar %.2e (det cond "
              "%.1e) %s" % (ev["M"], rel, bar, cond,
                            "ok" if rel <= bar else "MISS"))
    check("S3.ID the identity ward holds at every deep rung "
          "(conditioning-aware machine-precision bar, declared)",
          id_ok)
    chain_ok = all(ev["lam_r"] >= 0.0 for ev in deep)
    n_res = sum(1 for ev in deep if ev["lam_r"] >= ev["bud"])
    check("S3.PSD the per-rung psd-remainder chain holds at depth: "
          "lambda_min(A2 - M2) = %.2e..%.2e >= 0 on %d/%d rungs; "
          "resolvable above the float budget on %d/%d (typed)"
          % (min(ev["lam_r"] for ev in deep),
             max(ev["lam_r"] for ev in deep),
             sum(1 for ev in deep if ev["lam_r"] >= 0.0), len(deep),
             n_res, len(deep)), chain_ok)

    # alpha-coverage typing: the citation-grade sharpened chain
    print("\n    alpha-coverage (tail-probe sharpened chain at T_ver "
          "= %.0e; cited alpha* ~ %.0f):" % (T_VER, ALPHA_STAR_CITED))
    print("    %5s %6s | %9s %9s %9s | %9s %9s | %5s %5s"
          % ("M", "alpha", "tailterm", "eps_arch", "eps_f", "pert",
             "cert100", "c.fam", "c.pr"))
    sh = tp.sh_sum(T_VER)
    for ev in deep:
        Mz, D = ev["M"], DGRID
        s1n = (abs(ev["A2"][0, 0]) + abs(ev["A2"][1, 1])
               + 2.0 * abs(ev["A2"][0, 1]))
        eps_f = CHAIN_FAC * EPSM * float(np.linalg.norm(ev["A2"])) ** 2
        num_c = tp.num_sup({"h": Mz // 2, "D": D}, 0.5)
        tail_term = (4.0 / D) * num_c * sh
        # eps_arch diagnostic (floor-theorem P1 convention)
        dc = ft.arch_A_fine(np.arange(Mz) * D, D) \
            - np.asarray(core.arch_lags(Mz, D), float)
        dw = ev["dw"]
        eps_arch = ft.ARCH_SLACK * max(
            abs(float(dc @ dw["W11"])), abs(float(dc @ dw["W22"])),
            abs(float(dc @ dw["W12"])))
        env_c = tail_term + eps_f              # tail-probe frozen form
        pert = tp.pert_of(env_c, s1n)
        pert_wa = tp.pert_of(env_c + eps_arch, s1n)
        cfam = pert < ev["cert1"]
        cpr = pert < ev["x2_g1"]
        ev.update(pert_c=pert, pert_wa=pert_wa, cit_fam=cfam,
                  cit_pair=cpr, eps_arch=eps_arch, eps_f=eps_f)
        print("    %5d %6.2f | %9.2e %9.2e %9.2e | %9.2e %9.2e | "
              "%5s %5s"
              % (Mz, ev["alpha"], tail_term, eps_arch, eps_f, pert,
                 ev["cert1"], "yes" if cfam else "NO",
                 "yes" if cpr else "NO"))
    n_cit = sum(1 for ev in deep if ev["cit_fam"])
    al_cov = [ev["alpha"] for ev in deep if ev["cit_fam"]]
    al_unc = [ev["alpha"] for ev in deep if not ev["cit_fam"]]
    arch_flip = any(ev["cit_fam"] != (ev["pert_wa"] < ev["cert1"])
                    for ev in deep)
    print("    TYPED: citation grade covers alpha in {%s}; alpha in "
          "{%s} stands on the PER-RUNG VERIFIED chain only (deep "
          "alphas straddle the cited alpha* ~ %.0f); eps_arch "
          "inclusion %s closure on any rung"
          % (", ".join("%.2f" % a for a in al_cov) or "none",
             ", ".join("%.2f" % a for a in al_unc) or "none",
             ALPHA_STAR_CITED,
             "FLIPS" if arch_flip else "does not flip"))
    check("S3.ALPHA alpha-coverage typed: %d/%d deep rungs close at "
          "citation grade (family gate); the rest are per-rung "
          "verified (lambda_min >= 0, no citation horizon)"
          % (n_cit, len(deep)), True)

    # ============================================================== S4
    print("\nS4 -- THE DECISION (frozen)")
    min_cf = min(ev["cert_frac"] for ev in deep)
    if not chain_ok:
        decision = "CHAIN-BREAKS"
    elif min_cf >= FAM_BAR:
        decision = "FAMILY-SCALES"
    else:
        decision = "FAMILY-DECAYS"
    print("    min deep cert_frac = %.4f vs bar %.2f; psd chain %s"
          % (min_cf, FAM_BAR, "holds" if chain_ok else "BREAKS"))
    if decision == "FAMILY-DECAYS":
        print("\n    WHERE THE LOSS GOES (exact decomposition of "
              "det A2, per deep rung):")
        print("    %5s %7s | %8s %8s %8s %8s %8s | sum"
              % ("M", "X", "top100", "101-200", "famtail", "zxz",
                 "residue"))
        for ev in deep:
            f_top = ev["cert1"] / ev["det_a2"]
            f_dbl = (ev["cert2"] - ev["cert1"]) / ev["det_a2"]
            f_tail = (ev["fam_tot"] - ev["cert2"]) / ev["det_a2"]
            f_zz = (ev["det_m2"] - ev["fam_tot"]) / ev["det_a2"]
            f_res = ev["residue"]
            ev.update(f_top=f_top, f_dbl=f_dbl, f_tail=f_tail,
                      f_zz=f_zz)
            print("    %5d %7.3f | %8.4f %8.4f %8.4f %8.4f %8.4f | "
                  "%6.4f" % (ev["M"], ev["X"], f_top, f_dbl, f_tail,
                             f_zz, f_res,
                             f_top + f_dbl + f_tail + f_zz + f_res))
        # census at the deepest rung
        evd = deep[-1]
        n_z = len(gam)
        print("\n    CENSUS at the deepest rung (M = %d, X = %.3f): "
              "top-10 rank-one pairs of the full SOS:" % (evd["M"],
                                                          evd["X"]))
        dsum = evd["det_m2"]
        for r, (val, i, j) in enumerate(evd["top_pairs"][:10]):
            print("      #%2d %-24s x %-24s %10.3e (%6.4f of det M2)"
                  % (r + 1, pp.lab(int(i), n_z, gam),
                     pp.lab(int(j), n_z, gam), val, val / dsum))
        # alias identity of the top family carriers
        idx10 = evd["order"][:10]
        rfrac = gam[idx10] * DGRID / (2.0 * math.pi)
        med_alias = float(np.median(np.abs(rfrac - np.round(rfrac))))
        print("    top-10 FAMILY carriers: gamma = %s"
              % ", ".join("%.1f" % gam[i] for i in idx10))
        print("    alias offsets |gamma D/2pi - round| median %.4f "
              "(alias period 2 pi / D = %.1f)"
              % (med_alias, 2.0 * math.pi / DGRID))

    # ============================================================== S5
    print("\nS5 -- THE SYNTHESIS TABLE (certified family vs measured "
          "rho; single-pair gap for contrast)")
    print("    %5s %7s | %10s %10s %8s | %10s %8s"
          % ("M", "X", "rho_certF", "rho", "gap_fam", "rho_certP",
             "gap_pair"))
    for ev in deep:
        rho_cf = (ev["cert1"] - ev["bud"]) / (ev["lam"] * ev["tau_pnt"])
        rho_cp = ev["x2_g1"] / (ev["lam"] * ev["tau_pnt"])
        ev.update(rho_cf=rho_cf, rho_cp=rho_cp,
                  gap_f=ev["rho"] / max(rho_cf, 1e-300),
                  gap_p=ev["rho"] / max(rho_cp, 1e-300))
        print("    %5d %7.3f | %10.3e %10.3e %8.2f | %10.3e %8.1f"
              % (ev["M"], ev["X"], rho_cf, ev["rho"], ev["gap_f"],
                 rho_cp, ev["gap_p"]))
    below = all(ev["rho_cf"] <= ev["rho"] * (1.0 + 1e-9) for ev in deep)
    check("S5.SYN the certified family lower bound sits below the "
          "measured rho at every deep rung; gap_fam %.2f..%.2fx vs "
          "the single-pair gap %.0f..%.0fx (the parent's 40->673x "
          "trend)"
          % (min(ev["gap_f"] for ev in deep),
             max(ev["gap_f"] for ev in deep),
             min(ev["gap_p"] for ev in deep),
             max(ev["gap_p"] for ev in deep)), below)

    # ============================================================== C
    print("\nC -- controls")
    ev0 = next(ev for ev in deep if ev["M"] == 1176)
    rng = np.random.default_rng(SEED_SCRAMBLE)
    u_scr = rng.uniform(0.0, 1176 * DGRID, size=masses_scr.size)
    c_scr = np.zeros(1176)
    fdp.tent_accumulate_D(c_scr, 1176, DGRID, u_scr, masses_scr)
    dw0 = ev0["dw"]
    ccs = dw0["c_ar"] + c_scr
    A2s = np.array([[ccs @ dw0["W11"], ccs @ dw0["W12"]],
                    [ccs @ dw0["W12"], ccs @ dw0["W22"]]])
    lam_r_scr = ft.eig2_min(A2s - ev0["M2"])
    det_s = float(np.linalg.det(A2s))
    share_scr = ev0["cert1"] / det_s if det_s != 0.0 else float("inf")
    check("C1 [must-fire] scramble at M = 1176 (same %d masses, seed "
          "%d): the psd chain refuses the scrambled comb, "
          "lambda_min(A2_scr - M2) = %.3e < 0 (was %.2e); det %.3e "
          "-> %.3e, the certified share loses meaning (%.2f)"
          % (masses_scr.size, SEED_SCRAMBLE, lam_r_scr, ev0["lam_r"],
             ev0["det_a2"], det_s, share_scr), lam_r_scr < 0.0)
    evd = deep[-1]
    bw_dev = 0.0
    for i in evd["order"][:BW_TOP]:
        x2mp = mp_family_term(evd["wd"]["f1"], evd["wd"]["f2"], DGRID,
                              evd["M"], gam[int(i)])
        bw_dev = max(bw_dev, abs(x2mp - float(evd["x_pz"][int(i)] ** 2))
                     / max(x2mp, 1e-300))
    check("C2 budget ward: the top-%d family carriers at the deepest "
          "rung recomputed in mpmath (dps %d) match the float chain "
          "to rel %.1e <= %.0e (the certified values contain the "
          "high-precision evaluation)"
          % (BW_TOP, MP_DPS, bw_dev, BW_REL), bw_dev <= BW_REL)
    pb_dev = 0.0
    for ev in deep:
        pb = fdp.pair_brick(ev["dw"]["t1"], ev["dw"]["t2"], DGRID,
                            ev["M"], g1)
        pb_dev = max(pb_dev, abs(pb - ev["x2_g1"])
                     / max(ev["x2_g1"], 1e-300))
    check("C3 cross-implementation: pair_brick == x_pz(gamma_1)^2 on "
          "every deep rung (max rel dev %.1e <= %.0e)"
          % (pb_dev, PB_REL), pb_dev <= PB_REL)

    # ============================================================== V
    print("\n" + "=" * 78)
    print("V -- VERDICT: %s" % decision)
    print("=" * 78)
    if decision == "FAMILY-SCALES":
        print("""
  THE CERTIFIED SKELETON SCALES.  The pole x alias family (top-%d,
  per-rung psd chain) carries %.3f..%.3f of the floor at every deep
  rung X = %.3f..%.3f -- where the single pair holds only 1/%.0f..
  1/%.0f.  ALPHA-COVERAGE CAVEAT: citation grade (fixed T_ver = 3e12)
  covers only alpha <= ~%.0f; the deeper rungs stand on the per-rung
  verified chain."""
              % (K_FAM, min_cf, max(ev["cert_frac"] for ev in deep),
                 deep[0]["X"], deep[-1]["X"],
                 min(ev["gap_p"] for ev in deep),
                 max(ev["gap_p"] for ev in deep), ALPHA_STAR_CITED))
    elif decision == "FAMILY-DECAYS":
        print("""
  THE FAMILY SHARE DECAYS AT DEPTH (min cert_frac %.4f < %.2f).
  The loss is localized by the exact decomposition (top100 / ranks
  101-200 / family tail / zero x zero / >2e4 residue) and the census
  above names the deep carriers."""
              % (min_cf, FAM_BAR))
    else:
        print("""
  THE PSD CHAIN BREAKS AT DEPTH (lambda_min(A2 - M2) < 0 at some
  rung): the certification method's depth reach is bounded; typed
  above.""")
    dt = time.time() - T0
    print("-" * 78)
    print("checks: %d run, %d failed%s | runtime %.1f min"
          % (N_CHK, len(FAILS),
             (" [" + ", ".join(FAILS) + "]") if FAILS else "",
             dt / 60.0))
    print("NO RH claim; exploration only; nothing outside "
          "experiments/ touched.")


if __name__ == "__main__":
    run()
