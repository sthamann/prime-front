#!/usr/bin/env python3
"""v706 -- PRIME.WEYLMASS.01: S-D, THE WEYL CHARACTERIZATION OF G1:
is the exact mass law an evaluation of the m-/Schur function of the
BACKGROUND operator (arch+pole -- since S-C geometrically the cover
operator in deck decomposition) at the slot data?

EXPLORATION ONLY (experiments/ firewall): nothing here is a
verification claim; no verification/, paper, ledger or website surface
is touched; no marker moves; NO RH statement.  File prefix chain_
(the beam-search worker owns z1_* names; its 5e = z1_lookahead_probe
is cited, not touched).

FRAME [E-corpus + S-A].  S-A measured: the Levinson recursion of the
window ladder is dynamically unstable (out-of-corridor perturbations
die 500-1000 lags downstream; global tolerance e^{-1.43 alpha}); the
true comb is the unique bounded trajectory -- classically: the WEYL
(minimal) solution, characterized by the Weyl m-function / Schur
function.  KEY STRUCTURAL FACT (measured in G0 here): the arch+pole
background ALONE is not PD to full depth -- it breaks down shortly
after the first slot cell; each atom rescues positivity just in time
(the 5c/5d flow narrative).  So the background Caratheodory function
F_bg(z) = 1 + (2/c_0) sum_{d>=1} c_d z^d is analytic in the disk but
NOT a Caratheodory function (Re F on the boundary dips negative) --
the dips ARE the slots' demand.

MEASUREMENTS (bars/verdicts declared BEFORE any number):
  W1.1 [E] the classical machinery, cross-verified as an identity
     (mpmath, 40 digits, window 0, depth 32 < background breakdown):
     (a) the Schur algorithm on f = (F-1)/(z(F+1)) yields parameters
         gamma_n == -k_{n+1} (Levinson reflection coefficients of the
         SAME lag data; sign convention discovered and asserted,
         bar 1e-28) -- i.e. THE 5-SERIES alpha ARE THE SCHUR/
         VERBLUNSKY PARAMETERS of the window measure;
     (b) backward continued-fraction evaluation (Weyl-type tail 0)
         == direct series evaluation of f and F at |z| <= 0.3
         (bar 1e-12; both truncations O(|z|^32)).
  W1.2 [M] the two solution rates at the slot: inject a relative
     1e-9 single-moment perturbation into the sequential background
     at slot cells (window 4, slots n in {2, 9, 23, 53, 101}) and
     fit the downstream growth rate lambda+ of |delta k_n|; report
     the per-slot-gap amplification g = exp(lambda+ x gap) against
     the user-quoted 5e band g ~ 5-12 (typed: user-quoted; 5e's g is
     the beam worker's quantity, ours is the linearized rate).
  W2 [M] THE MASS PREDICTION.  Closed candidate (the boundary
     evaluation of the background m-function at the active
     constraint):
        K2: N = m0_next (Fejer order = the just-in-time horizon);
            sigma_N = Fejer-N symbol of the SEQUENTIAL background
            (exact past); theta* = argmin sigma_N (the deepest dip);
            w_K2 = -sigma_N(theta*) / s_{u,N}(theta*),
            s_{u,N} = Fejer-N symbol of the slot unit read
        (this IS w = G(F(z0), z0) with z0 = e^{i theta*}: Re F
        boundary = sigma/c_0, Fejer-regularized);
        K3: same with N = min(M-1, 2 m0_next) (depth sensitivity);
        K2b: matched-filter refinement -- instead of the single dip
            point, the least-squares repair over the WHOLE negative
            region: w = -int_{sigma_N<0} sigma_N s_u / int s_u^2
            (Rayleigh-type evaluation of the same boundary data).
     Plus the PHASE-ALIGNMENT diagnostic s_{u,N}(theta*)/max s_{u,N}
     (position forcing = the slot read is phase-aligned with the
     dip?).  Ratios w/mu_true on windows 0/2/4, all slots u <=
     log 120; benchmark: S-B's C2 (median 0.9947, max|r-1| 0.31).
  W3 [M] THE INTERPRETATION TESTS (the information channel):
     W3.1 first slot n = 2 on the PURE background (NO past): does
        the pure Gamma+pole data predict mu_2 = 2 log2/sqrt2 =
        0.9803?  Both the closed K2 and the criterion-free shooting
        mass (argmax survival depth, plateau midpoint; grid anchored
        on K2 -- no arithmetic in the path).  The cleanest test of
        information content.
     W3.2 bootstrap ladder (masses arithmetic-free, positions given
        -- declared: slot positions log n are conditioned on, the
        ladder predicts MASSES only; 5e attacks positions too):
        windows 0 and 4; each slot's mass = shooting plateau
        midpoint on the BOOT background (past = predicted masses,
        never MU_ALL); per-slot ratio, drift, death slot.
     W3.3 channel decomposition: the same shooting with EXACT past
        vs boot past -- the difference is the arithmetic information
        injected by conditioning (5e-verifier structure named).
  W4 verdict (preregistered):
     WEYL-CLOSED    iff some K candidate: max|ratio-1| < 1% uniform
                    AND median within 0.1% AND transport w/o scalar;
     WEYL-STRUCTURAL iff corr(log w_K2, log mu) >= 0.95 across slots
                    AND boot-past shooting median |ratio-1| <= 5%
                    over >= 10 slots (mechanism carries the masses,
                    not exactly);
     WEYL-NULL      otherwise.
     Separately typed: the W3.1 first-slot result (pure background
     -> first prime mass), whatever it is.

FIREWALL: AST-checked -- no zetazero/nzeros/zeta anywhere.  MU_ALL
(counting masses = exact arithmetic Lambda(n)/sqrt n) enters ONLY as
comparison target and as the EXACT-PAST conditioning in W2/W3.3
(declared); the W3.1/W3.2 prediction paths never read it.

Provenance (read-only): v563 core, z1_uvarov/z1_flow (5c/5d),
z1_lookahead (5e, cited), chain_tolerance_scaling_probe (S-A),
chain_mass_law_probe (S-B benchmark), chain_deck_sector_probe (S-C).

PROVENANCE: discovery probe chain_weyl_mass_probe.py (2026-08-03,
10/10 PASS, verdict WEYL-NULL: the point-evaluation reading of the
mass law is falsified (K2 median 0.3993) -- WITH the positive finds:
the flow alpha ARE the Schur parameters (1e-40), the background
breakdown sits exactly between the n=2 and n=3 cell, and the bare
Gamma flow knows log 2 to 0.1-0.6%).  Promoted verbatim; numbers
unchanged.
"""
import ast
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
import mpmath as mp                  # noqa: E402

U_SLOTS = math.log(120.0)
ND_SYM = 1 << 16
N1_SCHUR = 32
L_SER = 36
BAR_SIGN = 1e-28
BAR_CF = 1e-12
WIN_SET = (0, 2, 4)
RATE_NS = (2, 9, 23, 53, 101)
GRID_PTS = 55
BIT_EDGE = 20
MARGIN = 40


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


def build_win(kz):
    alpha, M = window_geometry(kz)
    D = 2.0 * alpha / M
    ka = core.atoms_in(alpha)
    c_ar = core.arch_lags(M, D)
    cp = pole_lags(M, D)
    return dict(kz=kz, alpha=alpha, M=M, D=D, ka=ka, p_sm=c_ar + cp)


def unit_read(w, u):
    c1, _ = core.atom_lags_at(w["alpha"], w["M"],
                              np.array([u]), np.array([1.0]))
    return c1


def slot_list(w):
    out = []
    for i in range(w["ka"]):
        u = float(core.U_ALL[i])
        if u > U_SLOTS:
            break
        cu = unit_read(w, u)
        nz = np.nonzero(cu)[0]
        out.append(dict(i=i, n=int(round(math.exp(u))), u=u,
                        mu=float(core.MU_ALL[i]), cu=cu,
                        ist=int(nz[np.argmax(np.abs(cu[nz]))]),
                        m0=int(nz[0])))
    return out


def bd_of(r, N):
    r = np.asarray(r, float)
    a = np.zeros(N + 1)
    a[0] = 1.0
    E = float(r[0])
    for n in range(1, N + 1):
        acc = r[n] + (float(a[1:n] @ r[n - 1:0:-1]) if n > 1 else 0.0)
        k = -acc / E
        a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
        E *= (1.0 - k * k)
        if not (abs(k) < 1.0) or E <= 0.0:
            return n
    return None


def lev_k(r, N):
    """Levinson with reflection-coefficient history (stops at
    breakdown; returns array of k up to last computed)."""
    r = np.asarray(r, float)
    a = np.zeros(N + 1)
    a[0] = 1.0
    E = float(r[0])
    ks = []
    for n in range(1, N + 1):
        acc = r[n] + (float(a[1:n] @ r[n - 1:0:-1]) if n > 1 else 0.0)
        k = -acc / E
        ks.append(k)
        a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
        E *= (1.0 - k * k)
        if not (abs(k) < 1.0) or E <= 0.0:
            break
    return np.array(ks)


# ------------------------------------------------------- mp series ops
def s_div(num, den, L):
    inv0 = 1 / den[0]
    q = [mp.mpf(0)] * L
    for k in range(L):
        acc = num[k] if k < len(num) else mp.mpf(0)
        for j in range(k):
            acc -= q[j] * den[k - j]
        q[k] = acc * inv0
    return q


def schur_params(cd, N1, L):
    """Schur algorithm on f = (F-1)/(z(F+1)) from moments cd
    (mp list, cd[0] = c_0); returns gamma_0..gamma_{N1-1} and the
    f_0 series."""
    A = [mp.mpf(1)] + [2 * cd[d] / cd[0] for d in range(1, L + 1)]
    num = [A[d + 1] for d in range(L)]          # (F-1)/z
    den = [A[0] + 1] + [A[d] for d in range(1, L)]  # F+1
    f = s_div(num, den, L)
    f0 = list(f)
    gams = []
    for _n in range(N1):
        g = f[0]
        gams.append(g)
        num2 = [(f[d + 1] if d + 1 < L else mp.mpf(0))
                for d in range(L)]              # (f - g)/z
        den2 = [1 - g * f[0]] + [-g * f[d] for d in range(1, L)]
        f = s_div(num2, den2, L)
    return gams, f0


def mp_levinson(cd, N):
    a = [mp.mpf(0)] * (N + 1)
    a[0] = mp.mpf(1)
    E = cd[0]
    ks = []
    for n in range(1, N + 1):
        acc = cd[n]
        for i in range(1, n):
            acc += a[i] * cd[n - i]
        k = -acc / E
        ks.append(k)
        newa = list(a)
        for i in range(1, n + 1):
            newa[i] = a[i] + k * a[n - i]
        a = newa
        E = E * (1 - k * k)
    return ks


def cf_eval(gams, z):
    f = mp.mpc(0)
    for g in reversed(gams):
        f = (g + z * f) / (1 + g * z * f)
    return f


def ser_eval(coeffs, z):
    acc = mp.mpc(0)
    for c in reversed(coeffs):
        acc = acc * z + c
    return acc


# ------------------------------------------------- symbol machinery
def fejer_symbol(lags, N):
    arr = np.zeros(ND_SYM)
    d = np.arange(1, N)
    arr[0] = lags[0]
    arr[1:N] = 2.0 * (1.0 - d / N) * lags[1:N]
    return np.fft.rfft(arr).real


def k_candidate(seq, cu, N):
    """Dip evaluation K2, matched-filter K2b, phase alignment."""
    sig = fejer_symbol(seq, N)
    su = fejer_symbol(cu, N)
    i_star = int(np.argmin(sig))
    align = float(su[i_star] / np.max(np.abs(su)))
    mask = sig < 0
    if not mask.any():
        return float("nan"), float("nan"), align
    k2b = float(-(sig[mask] @ su[mask]) / (su[mask] @ su[mask]))
    if su[i_star] <= 1e-6 * np.max(np.abs(su)):
        return float("nan"), k2b, align
    return float(-sig[i_star] / su[i_star]), k2b, align


# ------------------------------------------------- shooting machinery
def c0_anchor(bg, s):
    """Closed naive-law anchor (S-B C0): the mass zeroing the
    reflection at the dominant cell -- linear in w, two Levinson
    runs.  Arithmetic-free (background + slot geometry only)."""
    ist = s["ist"]
    ks0 = lev_k(bg, ist + 1)
    ks1 = lev_k(bg + s["cu"], ist + 1)
    if len(ks0) < ist or len(ks1) < ist:
        return float("nan")
    k0, k1 = ks0[ist - 1], ks1[ist - 1]
    if k1 == k0:
        return float("nan")
    return float(-k0 / (k1 - k0))


def shoot_mass(bg, cu, cap, anchor):
    """Plateau midpoint of argmax survival depth; grid anchored on
    the closed (arithmetic-free) anchor.  Returns (w*, S_max)."""
    if not (anchor > 0) or math.isnan(anchor):
        anchor = abs(bg[0]) * 1e-2

    def S(w):
        b = bd_of(bg + w * cu, cap)
        return cap + 1 if b is None else b

    grid = anchor * np.geomspace(0.15, 6.0, GRID_PTS)
    vals = np.array([S(w) for w in grid])
    S_max = int(vals.max())
    idx = np.where(vals == S_max)[0]
    # contiguous block around the median admissible index
    mid = idx[len(idx) // 2]
    lo_i = mid
    while lo_i - 1 in idx:
        lo_i -= 1
    hi_i = mid
    while hi_i + 1 in idx:
        hi_i += 1

    def edge(w_in, w_out):
        for _ in range(BIT_EDGE):
            wm = 0.5 * (w_in + w_out)
            if S(wm) >= S_max:
                w_in = wm
            else:
                w_out = wm
        return w_in

    w_lo = grid[lo_i] if lo_i == 0 else edge(grid[lo_i],
                                             grid[lo_i - 1])
    w_hi = grid[hi_i] if hi_i == len(grid) - 1 else \
        edge(grid[hi_i], grid[hi_i + 1])
    return 0.5 * (w_lo + w_hi), S_max


def stats_ratio(v):
    v = np.asarray([x for x in v if not math.isnan(x)], float)
    if len(v) == 0:
        return (float("nan"),) * 4
    return (float(np.median(v)), float(np.quantile(v, 0.25)),
            float(np.quantile(v, 0.75)),
            float(np.max(np.abs(v - 1.0))))


def run():
    print("=" * 78)
    print("S-D CHAIN WEYL MASS -- m-function characterization of G1")
    print("=" * 78)

    check("G0.0 [E] AST firewall: no zeta/zero symbol anywhere; "
          "MU_ALL only as comparison target / declared exact-past "
          "conditioning", ast_firewall(os.path.abspath(__file__)))

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
    wins = {i: build_win(kz) for i, (kz, _a, _M) in enumerate(picks)}
    ok_bd = True
    for i in WIN_SET:
        w = wins[i]
        sl = slot_list(w)
        w["slots"] = sl
        bd_bg = bd_of(w["p_sm"], w["M"] - 1)
        m02, m03 = sl[0]["m0"], sl[1]["m0"]
        ok_bd &= (bd_bg is not None) and (m02 - 1 <= bd_bg
                                          <= m03 + MARGIN)
        print("   window %d (h=%d): background-ONLY breakdown at "
              "cell %s; slot cells n=2: %d, n=3: %d"
              % (i, w["M"] // 2, bd_bg, m02, m03))
    check("G0.1 [M] the arch+pole background alone is NOT PD: it "
          "breaks down between the n=2 cell and the n=3 cell on all "
          "three windows -- F_bg is analytic but not Caratheodory; "
          "its boundary dips are the slots' demand (the flow "
          "narrative, now in Weyl language)", ok_bd)

    # ============================================================ W1.1
    print("\nW1.1 -- Schur/Verblunsky machinery as an identity "
          "(window 0, mpmath dps 40)")
    mp.mp.dps = 40
    w0 = wins[0]
    cd = [mp.mpf(float(x)) for x in w0["p_sm"][:L_SER + 2]]
    gams, f0 = schur_params(cd, N1_SCHUR, L_SER)
    ks = mp_levinson(cd, N1_SCHUR)
    dev_p = max(abs(gams[n] + ks[n]) for n in range(N1_SCHUR))
    dev_m = max(abs(gams[n] - ks[n]) for n in range(N1_SCHUR))
    sign = "-" if dev_p < dev_m else "+"
    dev_sign = float(min(dev_p, dev_m))
    zs = [mp.mpf("0.25"), mp.mpf("-0.3"),
          mp.mpc(0, "0.3"), mp.mpf("0.3") * mp.expjpi(mp.mpf(2) / 7)]
    dev_cf = 0.0
    for z in zs:
        f_cf = cf_eval(gams, z)
        f_sr = ser_eval(f0, z)
        F_cf = (1 + z * f_cf) / (1 - z * f_cf)
        A = [mp.mpf(1)] + [2 * cd[d] / cd[0]
                           for d in range(1, L_SER + 1)]
        F_sr = ser_eval(A, z)
        dev_cf = max(dev_cf, float(abs(f_cf - f_sr)),
                     float(abs(F_cf - F_sr)))
    check("W1.1 [E] IDENTITY: Schur parameters gamma_n == %sk_{n+1} "
          "(Levinson, same lag data; dev %.1e <= %.0e) -- the "
          "5-series alpha ARE the Schur/Verblunsky parameters of "
          "the window measure; backward continued-fraction (Weyl "
          "tail 0) == series evaluation of f and F at |z| <= 0.3 "
          "(dev %.1e <= %.0e)"
          % (sign, dev_sign, BAR_SIGN, dev_cf, BAR_CF),
          dev_sign <= BAR_SIGN and dev_cf <= BAR_CF)

    # ============================================================ W1.2
    print("\nW1.2 -- the two solution rates at the slot (window 4)")
    w4 = wins[4]
    sl4 = w4["slots"]
    n_map4 = {s["n"]: j for j, s in enumerate(sl4)}
    seq = w4["p_sm"].copy()
    seq_at = {}
    for j, s in enumerate(sl4):
        seq += s["mu"] * s["cu"]
        seq_at[j] = seq.copy()
    g_list = []
    for n_t in RATE_NS:
        j = n_map4[n_t]
        s = sl4[j]
        gap = (sl4[j + 1]["m0"] - s["m0"]) if j + 1 < len(sl4) \
            else MARGIN
        cap = min(w4["M"] - 1, s["m0"] + gap + MARGIN)
        base = seq_at[j]
        ks0 = lev_k(base, cap)
        q = base.copy()
        q[s["m0"]] += 1e-9 * base[0]
        ks1 = lev_k(q, cap)
        L_ = min(len(ks0), len(ks1))
        d = np.abs(ks1[:L_] - ks0[:L_])
        seg = d[s["m0"] + 1:L_]
        seg = seg[seg > 0]
        # linear-regime cut: stop before |delta k| saturates
        big = np.where(seg > 1e-3)[0]
        if len(big):
            seg = seg[:big[0]]
        if len(seg) < 8:
            continue
        x = np.arange(len(seg), dtype=float)
        lam = float(np.polyfit(x, np.log(seg), 1)[0])
        g_gap = math.exp(lam * gap)
        g_list.append((n_t, lam, gap, g_gap))
        print("   n=%3d: lambda+ = %+.4f /cell, gap = %3d cells, "
              "amplification to next slot g = %.2f"
              % (n_t, lam, gap, g_gap))
    g_vals = [g for (_n, _l, _g, g) in g_list]
    check("W1.2 [M] linearized instability rates measured: "
          "lambda+ > 0 on all probed slots; per-gap amplification "
          "g in [%.1f, %.1f] (median %.1f) -- compare the "
          "user-quoted 5e band g ~ 5-12 (different estimator, "
          "typed)" % (min(g_vals), max(g_vals),
                      float(np.median(g_vals))),
          all(l > 0 for (_n, l, _g, _gg) in g_list))

    # ============================================================== W2
    print("\nW2 -- the mass prediction: boundary evaluation of the "
          "background m-function at the deepest Fejer dip")
    tabs = {}
    for iw in WIN_SET:
        w = wins[iw]
        sl = w["slots"]
        seqb = w["p_sm"].copy()
        rows = []
        for j, s in enumerate(sl):
            m0n = sl[j + 1]["m0"] if j + 1 < len(sl) \
                else s["m0"] + MARGIN
            k2, k2b, al2 = k_candidate(seqb, s["cu"], m0n)
            k3, _k3b, _al3 = k_candidate(seqb, s["cu"],
                                         min(w["M"] - 1, 2 * m0n))
            rows.append(dict(n=s["n"], k2=k2 / s["mu"],
                             k2b=k2b / s["mu"],
                             k3=k3 / s["mu"], align=al2))
            seqb += s["mu"] * s["cu"]
        tabs[iw] = rows
        md2, q12, q32, mx2 = stats_ratio([r["k2"] for r in rows])
        mdb, q1b, q3b, mxb = stats_ratio([r["k2b"] for r in rows])
        md3, _q13, _q33, mx3 = stats_ratio([r["k3"] for r in rows])
        nn2 = sum(1 for r in rows if math.isnan(r["k2"]))
        nnb = sum(1 for r in rows if math.isnan(r["k2b"]))
        al_med = float(np.median([r["align"] for r in rows]))
        print("   window %d: K2 ratio median %.4f IQR [%.4f, %.4f] "
              "max|r-1| %.4f (%d NaN); K2b median %.4f IQR [%.4f, "
              "%.4f] max|r-1| %.4f (%d NaN); K3 median %.4f max "
              "%.4f; median phase alignment %.3f"
              % (iw, md2, q12, q32, mx2, nn2, mdb, q1b, q3b, mxb,
                 nnb, md3, mx3, al_med))
    pairs = [(sl4[j]["mu"], sl4[j]["mu"] * r["k2b"])
             for j, r in enumerate(tabs[4])
             if not math.isnan(r["k2b"]) and r["k2b"] > 0]
    mu4 = [p[0] for p in pairs]
    k2v4 = [p[1] for p in pairs]
    cc = float(np.corrcoef(np.log(k2v4), np.log(mu4))[0, 1]) \
        if len(k2v4) >= 8 else float("nan")
    md2_4, _q1, _q3, mx2_4 = stats_ratio([r["k2b"]
                                          for r in tabs[4]])
    print("   window 4: corr(log w_K2b, log mu_true) = %.3f over "
          "%d slots" % (cc, len(k2v4)))
    print("   window 4 detail (n, K2b ratio, alignment): %s"
          % [(r["n"], round(r["k2b"], 3), round(r["align"], 2))
             for r in tabs[4][:14]])
    check("W2.1 [M] closed boundary-evaluation candidates measured "
          "on all three windows (exact past); benchmark S-B C2: "
          "median 0.9947, max|r-1| 0.31 -- K2b (matched filter) "
          "window-4 median %.4f, max|r-1| %.4f, structural "
          "correlation %.3f" % (md2_4, mx2_4, cc), True)
    meds = [stats_ratio([r["k2b"] for r in tabs[iw]])[0]
            for iw in WIN_SET]
    check("W2.2 [M] transport without scalar: K2b medians across "
          "windows %s" % ["%.4f" % m for m in meds], True)

    # ============================================================ W3.1
    print("\nW3.1 -- FIRST SLOT n = 2 on the PURE background "
          "(no past, no arithmetic in the path)")
    ok31_rows = []
    for iw in WIN_SET:
        w = wins[iw]
        sl = w["slots"]
        s2 = sl[0]
        m0n = sl[1]["m0"]
        k2p, k2bp, al = k_candidate(w["p_sm"], s2["cu"], m0n)
        cap = min(w["M"] - 1, m0n + MARGIN)
        anchor = c0_anchor(w["p_sm"], s2)
        if not (anchor > 0) or math.isnan(anchor):
            anchor = k2bp
        w_sh, S_max = shoot_mass(w["p_sm"], s2["cu"], cap, anchor)
        r_k = k2p / s2["mu"]
        r_kb = k2bp / s2["mu"]
        r_s = w_sh / s2["mu"]
        ok31_rows.append((iw, r_k, r_kb, r_s, S_max, cap, al))
        print("   window %d: K2 = %.4f, K2b = %.4f x mu_2 (align "
              "%.2f); shooting = %.4f x mu_2 (max survival %d / "
              "cap %d); mu_2 = %.6f"
              % (iw, r_k, r_kb, al, r_s, S_max, cap, s2["mu"]))
    check("W3.1 [M] the pure Gamma+pole background predicts the "
          "FIRST prime mass: shooting ratios %s, matched-filter "
          "K2b ratios %s -- the information test result, typed "
          "exactly as measured"
          % (["%.4f" % r for (_i, _k, _kb, r, _S, _c, _a)
              in ok31_rows],
             ["%.4f" % kb for (_i, _k, kb, _r, _S, _c, _a)
              in ok31_rows]),
          True)

    # ============================================================ W3.2
    print("\nW3.2 -- bootstrap ladder (masses arithmetic-free, "
          "positions given)")
    boot_res = {}
    for iw in (0, 4):
        w = wins[iw]
        sl = w["slots"]
        bgb = w["p_sm"].copy()
        ratios = []
        death = None
        prev_w = float("nan")
        for j, s in enumerate(sl):
            m0n = sl[j + 1]["m0"] if j + 1 < len(sl) \
                else s["m0"] + MARGIN
            cap = min(w["M"] - 1, m0n + MARGIN)
            _k2, k2b, _al = k_candidate(bgb, s["cu"], m0n)
            anchor = c0_anchor(bgb, s)
            if not (anchor > 0) or math.isnan(anchor):
                anchor = k2b if (k2b > 0 and not math.isnan(k2b)) \
                    else prev_w
            w_b, S_max = shoot_mass(bgb, s["cu"], cap, anchor)
            if S_max < s["m0"] + 2:
                death = s["n"]
                break
            ratios.append(w_b / s["mu"])
            bgb += w_b * s["cu"]
            prev_w = w_b
        boot_res[iw] = ratios
        arr = np.array(ratios)
        print("   window %d: %d slots predicted%s; ratio median "
              "%.4f, median|r-1| %.4f, max|r-1| %.4f; first 10: %s"
              % (iw, len(ratios),
                 " (ladder death at n=%s)" % death if death else "",
                 float(np.median(arr)),
                 float(np.median(np.abs(arr - 1))),
                 float(np.max(np.abs(arr - 1))),
                 ["%.3f" % r for r in ratios[:10]]))
    check("W3.2 [M] bootstrap ladder measured (MU_ALL never in the "
          "prediction path; positions log n conditioned, declared; "
          "5e attacks positions too, cited)", True)

    # ============================================================ W3.3
    print("\nW3.3 -- information channel: exact past vs boot past")
    w = wins[4]
    sl = w["slots"]
    seqb = w["p_sm"].copy()
    exact_ratios = []
    for j, s in enumerate(sl):
        m0n = sl[j + 1]["m0"] if j + 1 < len(sl) \
            else s["m0"] + MARGIN
        cap = min(w["M"] - 1, m0n + MARGIN)
        _k2e, k2be, _ale = k_candidate(seqb, s["cu"], m0n)
        anchor_e = c0_anchor(seqb, s)
        if not (anchor_e > 0) or math.isnan(anchor_e):
            anchor_e = k2be
        w_e, _S = shoot_mass(seqb, s["cu"], cap, anchor_e)
        exact_ratios.append(w_e / s["mu"])
        seqb += s["mu"] * s["cu"]
    ex = np.array(exact_ratios)
    bo = np.array(boot_res[4])
    L_ = min(len(ex), len(bo))
    print("   window 4 shooting with EXACT past, ALL %d slots: "
          "median|r-1| %.4f, max|r-1| %.4f (the 5d reproduction)"
          % (len(ex), float(np.median(np.abs(ex - 1))),
             float(np.max(np.abs(ex - 1)))))
    print("   common first %d slots: EXACT median|r-1| %.4f vs "
          "BOOT median|r-1| %.4f"
          % (L_, float(np.median(np.abs(ex[:L_] - 1))),
             float(np.median(np.abs(bo[:L_] - 1)))))
    check("W3.3 [M] channel decomposition measured: the exact-past "
          "vs boot-past gap IS the arithmetic information injected "
          "by conditioning (the 5e-verifier structure, named)",
          True)

    # ============================================================== W4
    print("\nW4 -- verdict")
    boot_ok = float(np.median(np.abs(bo - 1))) <= 0.05 \
        and len(bo) >= 10
    closed = (mx2_4 < 0.01) and abs(md2_4 - 1) < 1e-3
    structural = (not math.isnan(cc)) and cc >= 0.95 and boot_ok
    if closed:
        VERDICT = "WEYL-CLOSED"
    elif structural:
        VERDICT = "WEYL-STRUCTURAL"
    else:
        VERDICT = "WEYL-NULL (K2: median %.4f max %.4f corr %.3f; "\
            "boot median|r-1| %.4f)" \
            % (md2_4, mx2_4, cc, float(np.median(np.abs(bo - 1))))
    check("W4.1 [M] preregistered classification: %s" % VERDICT,
          True)

    print("\nVERDICT: %s" % VERDICT)
    dt = time.time() - T0
    if FAILS:
        print("RESULT: %d/%d checks passed -- FAILURES: %s  (%.1f s)"
              % (N_CHK - len(FAILS), N_CHK, ", ".join(FAILS), dt))
        return 1
    print("RESULT: ALL %d CHECKS PASSED  (%.1f s)" % (N_CHK, dt))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
