#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""calib_scratch_wi -- PRE-FREEZE calibration for PRIME.WINDOW.INSTRUMENT.01
(window_instrument_probe.py).  INSTRUMENT-ONLY.  Deleted after freeze;
logs kept (calib_wi_pass*.log).

BARS DECLARED BEFORE THIS SCRATCH RAN (frozen intent, r160 discipline):
  identity bars: farform/theta-c1/budget-moment devs <= 1e-40 core;
  trial Courant HARD; theta_cap >= theta HARD; GW closure two-sided
  0 <= tau - S_cache <= env(gtop) at x = 5/8; zone share <= 1e-2;
  s*-theorem: sign flip at s*(1 +/- 1e-6); tau-price s* <= tau/(lamP w0^2)
  HARD; dA0 closed form vs central FD rel <= 1e-6 at h = 1e-3 s*;
  symmetric-derivative rel <= 1e-6; ghost replica vs r160 strings rel
  <= 0.15; plant sandwich tau <= tau_plant <= lam1 (1+1e-9) HARD;
  plateau vs deflation rel <= 1e-3 (to be calibrated); multi-plant b5:
  tau_W > 0 AND NOT in-window (value witness); b8 multi in-window.
This scratch MEASURES the values to quote verbatim in the frozen spec.
"""
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4          # noqa: E402
import anchor_epslock_probe as AEP     # noqa: E402
import rootladder_probe as RL          # noqa: E402
import j2_primeforce_probe as JP       # noqa: E402
import fullgap_growthlaw_probe as FGL  # noqa: E402

T0 = time.time()
gam = np.asarray(np.load(os.path.join(HERE, "verified_zeros_n7000.npy")),
                 float)
gtop = float(gam[-1])


def say(m):
    print(m, flush=True)


def E_of(cs, aa, oms, t):
    Rv = 2 * cs[0] / t
    for k in range(1, len(cs)):
        Rv += 2 * cs[k] * (-1) ** k * t / (t * t - oms[k] ** 2)
    return mp.sin(aa * t) * Rv


# ===================================================================
# RUNG LAYER (R4 cells)
# ===================================================================
def rung(x, dps):
    say("\n===== RUNG x=%d (dps %d) =====" % (x, dps))
    ce = R4.build_cell(x, 1.25, "MAIN", dps, want_mp=True)
    K = ce["K"]
    E = ce["mpE"]
    V = ce["mpV"]
    say("built K=%d in %.1f s  tau=%s" % (K, ce["build_s"], ce["tau_str"]))
    with mp.workdps(dps):
        aa = mp.log(x) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        b = [o * o for o in oms]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        A0p = sum(((-1) ** k) * cs[k] for k in range(K))
        A2p = sum(((-1) ** k) * cs[k] * b[k] for k in range(K))
        A4p = sum(((-1) ** k) * cs[k] * b[k] ** 2 for k in range(K))
        yt = abs(A2p / A0p)
        J2 = (A4p / A0p) / (A2p / A0p) ** 2
        tau = E[0]
        lam1 = E[1]
        lammax = E[K - 1]
        FG = (lam1 - tau) / tau
        Tz = 2 * math.pi * x
        Tz2 = mp.mpf(repr(Tz)) ** 2
        Gz = mp.mpf(repr(FGL.hsw_G(Tz)))
        tlaw0 = tau / (8 * A0p * A0p * Gz)
        cs1 = [V[i, 1] / nrm[i] for i in range(K)]
        A01 = sum(((-1) ** k) * cs1[k] for k in range(K))
        J = (A01 / A0p) ** 2
        theta = J / Tz2 ** 2
        c1v = abs(A01 / A0p) / Tz2
        t_r = (lam1 * A0p * A0p) / (tau * A01 * A01)
        say("FG %.6e  theta %.6f  c1 %.6f  t_r %.4f  tlaw0 %.4f  "
            "J2 %.6f  yt %.4e  theta-c1^2 dev %.1e"
            % (float(FG), float(theta), float(c1v), float(t_r),
               float(tlaw0), float(J2), float(yt),
               float(abs(theta - c1v ** 2))))
        # ---------------- slots
        nc = sum(1 for i in range(K) if E[i] < mp.mpf("0.1") * lammax)
        A_prev = A0p
        slots = []
        for i in range(1, min(nc, 8)):
            csi = [V[k2, i] / nrm[k2] for k2 in range(K)]
            A0i = sum(((-1) ** k2) * csi[k2] for k2 in range(K))
            ci = abs(A0i / A_prev) / Tz2
            tli = E[i] / (8 * A0i * A0i * Gz)
            slots.append((i, float(ci), float(tli / tlaw0)))
            A_prev = A0i
        say("nc=%d slots (i, c_i, tlaw_i/tlaw0): %s"
            % (nc, "  ".join("%d:%.4f/%.3f" % s for s in slots)))
        # kernel battery quick look
        if slots:
            c1s = slots[0][1]
            geo = ["%.4f" % (c1s / 2 ** (i - 1))
                   for i, _c, _t in slots]
            wal = []
            wv = 1.0
            for i, _c, _t in slots:
                wv = wv * (2 * i - 1) / (2 * i)
                wal.append("%.4f" % wv)
            fej = []
            for i, _c, _t in slots:
                fej.append("%.4f" % (2.0 / ((2 * i + 1) * (2 * i + 2))
                                     * 6.0 * c1s))
            say("kernels: geo-half %s | wallis %s | fejer-scaled %s"
                % ("/".join(geo), "/".join(wal), "/".join(fej)))
        # band-edge offset for c1 law hunt
        m_zone = int(np.sum(gam <= Tz))
        g_lo = float(gam[m_zone - 1])
        g_hi = float(gam[m_zone])
        ufrac = (Tz - g_lo) / (g_hi - g_lo)
        say("edge offset: m=%d gamma_m=%.3f gamma_m+1=%.3f ufrac=%.4f"
            % (m_zone, g_lo, g_hi, ufrac))
        # ---------------- trial cap
        cvec = [V[i, 0] for i in range(K)]
        mu_b = sum(cvec[k] * cvec[k] * b[k] for k in range(K))
        vfr = [cvec[k] * (b[k] - mu_b) for k in range(K)]
        n2 = sum(vfr[k] * vfr[k] for k in range(K))
        Mq = ce["mpM"]
        Mv = [sum(Mq[i, k] * vfr[k] for k in range(K)) for i in range(K)]
        ray = sum(vfr[k] * Mv[k] for k in range(K)) / n2
        r_trial = (ray - tau) / tau
        th_cap = (1 + r_trial) / (t_r * Tz2 ** 2)
        say("trial r %.6e  theta_cap %.4f  cap/theta %.3f  "
            "courant %.1e" % (float(r_trial), float(th_cap),
                              float(th_cap / theta),
                              float(r_trial / FG - 1)))
        # ---------------- far-form identity at 3 sample points
        om_max = float(mp.sqrt(b[K - 1]))
        for fac in (1.1, 1.7, 3.0):
            t = mp.mpf(repr(fac * om_max))
            Ev = E_of(cs, aa, oms, t)
            y = t * t
            S = sum(((-1) ** k) * cs[k] * b[k] / (y - b[k])
                    for k in range(1, K)) / A0p
            pred = (2 * A0p / t) * mp.sin(aa * t) * (1 + S)
            say("farform t=%.1f om_max: dev %.1e"
                % (fac, float(abs(Ev - pred) / abs(Ev))))
        # budget-moment dictionary at one above-band zero
        gsel = float(gam[np.searchsorted(gam, om_max * 1.3)])
        t = mp.mpf(repr(gsel))
        y = t * t
        Ev = E_of(cs, aa, oms, t)
        Tf = sum(((-1) ** k) * cs[k] * b[k] * b[k] / (y - b[k])
                 for k in range(1, K)) / A0p
        z = y / yt
        # a2 = A2/A0 (signed); Phi via L1 with signed a2: use
        # 1 + S = (a2 + T)/y + 1 ... direct: F/A0 = 1 + S
        Phi_dir = (y / yt) * (1 + sum(((-1) ** k) * cs[k] * b[k]
                                      / (y - b[k])
                                      for k in range(1, K)) / A0p)
        lhs = 2 * Ev * Ev
        rhs = 8 * A0p * A0p * mp.sin(aa * t) ** 2 * yt * yt \
            * Phi_dir ** 2 / y ** 3
        say("budget-moment at gamma=%.2f: z=%.3f  dev %.1e"
            % (gsel, float(z), float(abs(lhs - rhs) / abs(lhs))))
        # ---------------- GW budget over the cache
        eta_g = sum(abs(cs[k]) * b[k] for k in range(1, K)) \
            / (abs(A0p) * (mp.mpf(repr(gtop)) ** 2 - b[K - 1]))
        for tag, csv, lamv, A0v in (("phi", cs, tau, A0p),
                                    ("psi1", cs1, lam1, A01)):
            Sz = Sb = Ss = Sf = mp.mpf(0)
            for g in gam:
                t = mp.mpf(repr(float(g)))
                Ev = E_of(csv, aa, oms, t)
                w2 = 2 * Ev * Ev
                gf = float(g)
                if gf <= Tz:
                    Sz += w2
                elif gf <= om_max:
                    Sb += w2
                elif gf * gf <= float(yt):
                    Ss += w2
                else:
                    Sf += w2
            Stot = Sz + Sb + Ss + Sf
            env = 8 * (abs(A0v) * (1 + eta_g)) ** 2 \
                * mp.mpf(repr(FGL.hsw_G(gtop)))
            rem = lamv - Stot
            say("budget %s: shares z/b/s/f = %.2e/%.4f/%.4f/%.4f  "
                "rem/lam %.2e  rem/env %.3f  closure(S/lam) %.6f"
                % (tag, float(Sz / lamv), float(Sb / lamv),
                   float(Ss / lamv), float(Sf / lamv),
                   float(rem / lamv), float(rem / env),
                   float(Stot / lamv)))
        # equidistribution
        s2 = mp.mpf(0)
        g2 = mp.mpf(0)
        for g in gam[gam > Tz]:
            t = mp.mpf(repr(float(g)))
            s2 += mp.sin(aa * t) ** 2 / (t * t)
            g2 += 1 / (t * t)
        say("equidistribution: <sin^2>_(gamma>Tz) = %.4f  "
            "sum 1/g^2 / G(Tz) = %.4f  tlaw0 = %.4f"
            % (float(s2 / g2), float(g2 / Gz), float(tlaw0)))
    return dict(x=x)


# ===================================================================
# W2 LAYER (AEP blocks)
# ===================================================================
def w2block(tag, x_nom, dps, do_multi=True):
    say("\n===== W2 BLOCK b%d (dps %d) =====" % (tag, dps))
    u0, _lo, _hi = AEP.anchor_select(x_nom)
    x0 = math.exp(u0)
    icap = int(math.floor(x0))
    with mp.workdps(dps):
        u = mp.mpf(repr(u0))
        aa = u / 2
        K = int(math.ceil(AEP.kfun_f(float(mp.exp(u)))))
    MA, _n = AEP.cell_matrix(aa, K, icap, dps)
    atoms = JP.prime_atoms(icap, dps)
    NpT = JP.nprime_block(aa, K, dps, [("atoms", atoms)])
    rT = JP.world_measure(MA, K, aa, dps)
    with mp.workdps(dps):
        tau = rT["tau"]
        E = rT["E"]
        order = rT["order"]
        Vm = rT["V"]
        phi = rT["phi"]
        nrm = rT["nrm"]
        d1 = E[1] - E[0]
        alp = [((-1) ** k) / nrm[k] for k in range(K)]
        A0t = sum(alp[k] * phi[k] for k in range(K))
        say("b%d: x0 %.6f K %d tau %.3e d1 %.3e J2 %.6f A0 %.3e"
            % (tag, x0, K, float(tau), float(d1), rT["J2"],
               float(A0t)))
        # eigenvectors sorted
        psis = []
        for c in range(K):
            ie = order[c]
            psis.append([Vm[i, ie] for i in range(K)])
        gam_list = (2.0, 5.0, 9.0, 12.0, 14.5, 20.0, 30.0)
        for g in gam_list:
            Np = JP.nprime_block(aa, K, dps, [("cos", g, 1.0)])
            P = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    P[i, j] = -Np[i, j]
            Ep, Vp = mp.eigsy(P)
            imax = max(range(K), key=lambda i: Ep[i])
            lamP = Ep[imax]
            vP = [Vp[i, imax] for i in range(K)]
            w0 = sum(vP[i] * phi[i] for i in range(K))
            # rank-1 closed form s* = 1/(lamP v'M^-1 v)
            zsol = mp.lu_solve(MA, mp.matrix(vP))
            quad = sum(vP[i] * zsol[i] for i in range(K))
            resid = mp.norm(MA * zsol - mp.matrix(vP))
            s_star = 1 / (lamP * quad)
            price = tau / (lamP * w0 * w0)
            # verify sign flip
            flips = []
            for sgn, eps in ((1, -1e-6), (1, +1e-6)):
                s = float(s_star) * (1 + eps)
                Mw = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Mw[i, j] = MA[i, j] - s * P[i, j]
                Ew, _ = mp.eigsy(Mw)
                flips.append(float(min(Ew[i] for i in range(K))))
            # dA0/ds closed form (ghost dir: M - sP)
            Pphi = [sum(P[i, j] * phi[j] for j in range(K))
                    for i in range(K)]
            D = mp.mpf(0)
            for c in range(1, K):
                av = sum(alp[k] * psis[c][k] for k in range(K))
                pv = sum(psis[c][k] * Pphi[k] for k in range(K))
                D += av * pv / (E[c] - E[0])
            # FD at h = 1e-3 s*
            h = float(s_star) * 1e-3
            fd = []
            for sgn in (-1, 1):
                Mw = mp.zeros(K, K)
                for i in range(K):
                    for j in range(K):
                        Mw[i, j] = MA[i, j] + sgn * h * P[i, j]
                Ew, Vw = mp.eigsy(Mw)
                i0 = min(range(K), key=lambda i: Ew[i])
                ph = [Vw[i, i0] for i in range(K)]
                ov = sum(ph[i] * phi[i] for i in range(K))
                if ov < 0:
                    ph = [-v for v in ph]
                nn = mp.sqrt(sum(v * v for v in ph))
                fd.append(sum(alp[k] * ph[k] / nn for k in range(K)))
            fd_d = (fd[0] - fd[1]) / (2 * h)
            say("  g=%4.1f lamP %.3e w0^2 %.3e s* %.3e price %.3e "
                "s*/price %.3f lamin(-) %.2e lamin(+) %.2e "
                "lures %.1e dA0 D %.3e FD %.3e rel %.1e "
                "dA0/A0/s* %.2e"
                % (g, float(lamP), float(w0 * w0), float(s_star),
                   float(price), float(s_star / price), flips[0],
                   flips[1], float(resid), float(D), float(fd_d),
                   float(abs(fd_d / D - 1)) if D != 0 else -1,
                   float(abs(D) * s_star / abs(A0t))))
        # plant sandwich + plateau at g = 5
        g = 5.0
        Np = JP.nprime_block(aa, K, dps, [("cos", g, 1.0)])
        P = mp.zeros(K, K)
        for i in range(K):
            for j in range(K):
                P[i, j] = -Np[i, j]
        Ep, Vp = mp.eigsy(P)
        imax = max(range(K), key=lambda i: Ep[i])
        vP = [Vp[i, imax] / mp.sqrt(sum(Vp[i2, imax] ** 2
                                        for i2 in range(K)))
              for i in range(K)]
        # deflation: Householder basis of vP-perp
        Q = []
        e0 = [mp.mpf(1) if i == 0 else mp.mpf(0) for i in range(K)]
        wv = [vP[i] - e0[i] for i in range(K)]
        nw = mp.sqrt(sum(v * v for v in wv))
        if nw > mp.mpf("1e-30"):
            wv = [v / nw for v in wv]
        else:
            wv = None
        # columns of Householder H = I - 2ww' except first (maps e0->vP)
        cols = []
        for j in range(1, K):
            col = [mp.mpf(0)] * K
            col[j] = mp.mpf(1)
            if wv is not None:
                dot = wv[j]
                for i in range(K):
                    col[i] -= 2 * dot * wv[i]
            cols.append(col)
        Mc = mp.zeros(K - 1, K - 1)
        for a2 in range(K - 1):
            Ma = [sum(MA[i, j] * cols[a2][j] for j in range(K))
                  for i in range(K)]
            for b2 in range(a2 + 1):
                val = sum(cols[b2][i] * Ma[i] for i in range(K))
                Mc[a2, b2] = Mc[b2, a2] = val
        Ec, Vc = mp.eigsy(Mc)
        i0c = min(range(K - 1), key=lambda i: Ec[i])
        tau_defl = Ec[i0c]
        phc = [Vc[i, i0c] for i in range(K - 1)]
        ph_full = [sum(cols[j][i] * phc[j] for j in range(K - 1))
                   for i in range(K)]
        nn = mp.sqrt(sum(v * v for v in ph_full))
        A0_defl = sum(alp[k] * ph_full[k] / nn for k in range(K))
        say("  deflation g=5: tau_defl %.6e  in [tau, lam1]? %s  "
            "A0_defl %.3e (A0 %.3e)"
            % (float(tau_defl), tau <= tau_defl <= E[1],
               float(A0_defl), float(A0t)))
        for s in (1.0, 1e3):
            Mw = mp.zeros(K, K)
            for i in range(K):
                for j in range(K):
                    Mw[i, j] = MA[i, j] + s * Ep[imax] * vP[i] * vP[j]
            Ew, Vw = mp.eigsy(Mw)
            i0 = min(range(K), key=lambda i: Ew[i])
            tw = Ew[i0]
            ph = [Vw[i, i0] for i in range(K)]
            ov = sum(ph[i] * ph_full[i] / nn for i in range(K))
            if ov < 0:
                ph = [-v for v in ph]
            nn2 = mp.sqrt(sum(v * v for v in ph))
            A0w = sum(alp[k] * ph[k] / nn2 for k in range(K))
            say("  plant s=%g (rank-1 lamP): tau_w %.6e sandwich %s "
                "tau_w/tau_defl-1 %.2e  A0_w/A0_defl-1 %.2e"
                % (s, float(tw), tau <= tw <= E[1] * (1 + 1e-9),
                   float(tw / tau_defl - 1),
                   float(A0w / A0_defl - 1)))
        # ghost break replica (JP-exact path)
        d1f = float(d1)
        ghosts = {}
        for g in (2.0, 5.0, 9.0, 14.5, 20.0, 30.0):
            lo = max(d1f * 1e-3, 1e-40)
            r_hi = JP.build_world(MA, NpT, [("atoms", atoms),
                                            ("cos", g, -1.0)],
                                  K, aa, dps, census=False)
            if JP.in_window(r_hi, lite=True):
                ghosts[g] = float("inf")
                continue
            a2, b2 = math.log10(lo), 0.0
            for _ in range(JP.THETA_BIS_STEPS):
                m = 0.5 * (a2 + b2)
                r = JP.build_world(MA, NpT, [("atoms", atoms),
                                             ("cos", g,
                                              -(10.0 ** m))],
                                   K, aa, dps, census=False)
                if not JP.in_window(r, lite=True):
                    b2 = m
                else:
                    a2 = m
            ghosts[g] = 10.0 ** b2
        say("  ghost replica s*: %s"
            % "  ".join("%g:%.2e" % (g, ghosts[g]) for g in ghosts))
        if do_multi:
            r = JP.build_world(MA, NpT, [("atoms", atoms)]
                               + [("cos", g, 1.0)
                                  for g in (2.0, 5.0, 9.0, 12.0)],
                               K, aa, dps)
            say("  multi-plant: tau %.3e J2 %.6f ytb %.2f n_esc %d "
                "in_window %s"
                % (r["tau_f"], r["J2"], r["ytb"], r["n_esc"],
                   JP.in_window(r)))
            for g in (2.0, 9.0):
                r = JP.build_world(MA, NpT, [("atoms", atoms),
                                             ("cos", g, 1.0)],
                                   K, aa, dps)
                say("  single plant g=%g: tau %.3e J2 %.6f in %s"
                    % (g, r["tau_f"], r["J2"], JP.in_window(r)))


if __name__ == "__main__":
    args = sys.argv[1:]
    if "rung5" in args or not args:
        rung(5, 60)
    if "rung8" in args:
        rung(8, 80)
    if "b5" in args or not args:
        w2block(5, 5.44, 60)
    if "b8" in args:
        w2block(8, 8.50, 80)
    say("\nTOTAL %.1f s" % (time.time() - T0))
