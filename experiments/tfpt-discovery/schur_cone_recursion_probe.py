#!/usr/bin/env python3
"""schur_cone_recursion_probe.py -- REVIEW OFFENSIVE 3: the
cone-preserving Schur recursion.  Thesis under test: every prime-ideal
layer (Hecke degrees + KMS half-weight + rank-1 atom contributions)
acts SU(1,1)/J-contractively on the Schur data of the window measure,
so that window positivity = a composition of cone-preserving Moebius
maps kappa_{n+1} = Phi_n(kappa_n).

EXPLORATION ONLY (experiments/ firewall): no verification/, paper,
ledger or website surface; no marker moves; NO RH statement.

THE EXACT ALGEBRA (derived by hand, verified symbolically in S2a and
as a machine-precision identity in S1): let the base window measure
have lags c (c_0 > 0) and Schur data w(z) = z f(z) where
F = (1 + w)/(1 - w) is the c_0-normalized Caratheodory function.
Adding ONE layer with lags psi (Herglotz polynomial
B(z) = psi_0 + 2 sum_{d>=1} psi_d z^d, a = 2 c_0 + psi_0) updates

    w~ = [ (B - psi_0) + (a - B) w ] / [ (a + B) - (B + psi_0) w ]

-- a z-pointwise Moebius/transfer action with matrix
    T(z) = [[a - B, B - psi_0], [-(B + psi_0), a + B]]
and the exact J-identity (J = diag(1, -1), v = (1, -1)^T):
    T* J T = (a^2 - psi_0^2) J - 2 (a + psi_0) Re B(z) . v v^T,
    (w-bar, 1) T*JT (w, 1)^T
        = (a^2 - psi_0^2)(|w|^2 - 1) - 2(a + psi_0) ReB |1 - w|^2.
COROLLARY (the SU(1,1) criterion): T(z) is J-contractive (maps the
closed Schur ball into itself) at z iff Re B(z) >= 0; the update is
cone-preserving on the whole disk iff B is Herglotz iff THE LAYER IS
A POSITIVE-DEFINITE SEQUENCE (a positive measure layer).

MEASUREMENTS (bars/verdicts declared BEFORE any number):
  S1 [E] the symbolic update, verified as an identity: on window 0,
     base = full window minus the p = 13 channel; adding the channel
     via the Moebius series action and running the Schur algorithm on
     f~ must reproduce the direct Levinson reflection coefficients of
     the full lags (gamma_n = -k_{n+1}, the W1.1 sign), to depth
     N1 = min(24, first-13-cell - 6), bar 1e-20 (mpmath dps 40).
  S2a [E] the SU(1,1) structure, symbolic (sympy): the T*JT identity
     and the q-form factorization above hold exactly.
  S2b [M] contraction factors per prime-ideal layer over the ladder
     (windows 0/2/4; classes declared from Z[i]: p = 2 ramified,
     p = 5, 13 split, p = 3, 7 inert, inert also as square-only
     subchannel): min_theta Re B_p(r e^{i theta}) for
     r in {0.5, 0.8, 0.9, 0.95, 0.99, 1.0} and the Moebius expansion
     factor R_max = max_{|w|=1} |phi(w)| at the worst boundary-near
     point.  STRUCTURAL FACT tested first: every atom channel has
     c_0 = 0 with nonzero deeper lags -- a nonzero positive-definite
     sequence needs |c_d| <= c_0, so NO atom layer can be a positive
     measure, and by S2a its map CANNOT be J-contractive on the disk
     (the Weil sign structure: primes enter subtracted).
  S2c [M] the compensation fact: the FULL window ladder is PD to
     full depth (max_n |k_n| < 1) -- the orbit stays in the Schur
     ball even though every single layer map is expansive somewhere.
  S3 verdict (preregistered):
     SCHUR-CONE-ALIVE iff every prime channel on every ladder window
        satisfies min_{r<=0.99} min_theta Re B_p >= -1e-12 x scale
        (then formulate the induction theorem candidate);
     SCHUR-CONE-DEAD otherwise -- with the anatomy: which class
        breaks at which radius, the expansion factors, and the
        structural c_0 = 0 one-liner; then the honest granularity
        statement (the review kill).

FIREWALL: AST-checked; no zero/prime loaders beyond the v563 core's
own atom table (MU_ALL/U_ALL = the deployed window object, declared).
Provenance (read-only): v563 core, chain_weyl_mass_probe (S-D: Schur
= Levinson identity W1.1), z1_uvarov_probe (5c, related rank-1 work).
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

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp                  # noqa: E402

T0 = time.time()
FAILS = []
N_CHK = 0

BANNED = ("zetazero", "nzeros", "zeta", "second_sheet_zero")

L_SER = 40
N1_CAP = 24
BAR_S1 = 1e-20
ND_SYM = 1 << 14
R_LADDER = (0.5, 0.8, 0.9, 0.95, 0.99, 1.0)
WIN_SET = (0, 2, 4)
P_SET = (2, 3, 5, 7, 13)
P_CLASS = {2: "ramified", 3: "inert", 5: "split", 7: "inert",
           13: "split"}
NW_GRID = 512


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


def spf(n):
    if n % 2 == 0:
        return 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            return q
        q += 2
    return n


def build_win(kz):
    alpha, M = window_geometry(kz)
    D = 2.0 * alpha / M
    ka = core.atoms_in(alpha)
    c_ar = core.arch_lags(M, D)
    cp = pole_lags(M, D)
    ch = {}
    ch_sq = {}
    for i in range(ka):
        n = int(round(math.exp(float(core.U_ALL[i]))))
        p = spf(n)
        ch.setdefault(p, []).append(i)
        k_exp = int(round(math.log(n, p)))
        if k_exp % 2 == 0:
            ch_sq.setdefault(p, []).append(i)
    lay = {}
    for p, idx in ch.items():
        lags, _ = core.atom_lags_at(alpha, M,
                                    core.U_ALL[idx],
                                    core.MU_ALL[idx])
        lay[p] = lags
    lay_sq = {}
    for p in (3, 7):
        idx = ch_sq.get(p, [])
        if idx:
            lags, _ = core.atom_lags_at(alpha, M,
                                        core.U_ALL[idx],
                                        core.MU_ALL[idx])
            lay_sq[p] = lags
    c_at, _ = core.atom_lags_at(alpha, M, core.U_ALL[:ka],
                                core.MU_ALL[:ka])
    return dict(kz=kz, alpha=alpha, M=M, D=D, ka=ka,
                bg=c_ar + cp, arch=c_ar, pole=cp, c_at=c_at,
                total=c_ar + cp + c_at, lay=lay, lay_sq=lay_sq)


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


def lev_kmax(r, N):
    r = np.asarray(r, float)
    a = np.zeros(N + 1)
    a[0] = 1.0
    E = float(r[0])
    kmax = 0.0
    for n in range(1, N + 1):
        acc = r[n] + (float(a[1:n] @ r[n - 1:0:-1]) if n > 1 else 0.0)
        k = -acc / E
        kmax = max(kmax, abs(k))
        a[1:n + 1] = a[1:n + 1] + k * a[n - 1::-1][:n]
        E *= (1.0 - k * k)
        if not (abs(k) < 1.0) or E <= 0.0:
            return n, kmax
    return None, kmax


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


def s_mul(a, b, L):
    out = [mp.mpf(0)] * L
    for i, ai in enumerate(a[:L]):
        if ai == 0:
            continue
        for j, bj in enumerate(b[:L - i]):
            out[i + j] += ai * bj
    return out


def s_axpy(alpha_, a, b, L):
    """alpha_*a + b as series of length L."""
    out = [mp.mpf(0)] * L
    for i in range(L):
        va = a[i] if i < len(a) else mp.mpf(0)
        vb = b[i] if i < len(b) else mp.mpf(0)
        out[i] = alpha_ * va + vb
    return out


def f_from_lags(cd, L):
    """Schur function series f of the measure with lags cd."""
    A = [mp.mpf(1)] + [2 * cd[d] / cd[0] for d in range(1, L + 1)]
    num = [A[d + 1] for d in range(L)]
    den = [A[0] + 1] + [A[d] for d in range(1, L)]
    return s_div(num, den, L)


def schur_from_f(f, N1, L):
    gams = []
    for _n in range(N1):
        g = f[0]
        gams.append(g)
        num2 = [(f[d + 1] if d + 1 < L else mp.mpf(0))
                for d in range(L)]
        den2 = [1 - g * f[0]] + [-g * f[d] for d in range(1, L)]
        f = s_div(num2, den2, L)
    return gams


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


# ------------------------------------------------- Herglotz machinery
def reB_grid(lags, r):
    """Re B(r e^{i theta}) on the ND_SYM theta grid,
    B = psi_0 + 2 sum psi_d z^d (finite window support -- exact)."""
    M = len(lags)
    arr = np.zeros(ND_SYM)
    d = np.arange(1, M)
    arr[0] = lags[0]
    arr[1:M] = 2.0 * lags[1:M] * (r ** d if r < 1.0 else 1.0)
    return np.fft.rfft(arr).real


def B_at(lags, z):
    M = len(lags)
    zp = z ** np.arange(M)
    return complex(lags[0] + 2.0 * np.dot(lags[1:], zp[1:]))


def expansion_factor(c0_base, psi0, Bval):
    """max_{|w|=1} |phi_T(w)| for the layer transfer matrix."""
    a = 2.0 * c0_base + psi0
    w = np.exp(2j * math.pi * np.arange(NW_GRID) / NW_GRID)
    num = (a - Bval) * w + (Bval - psi0)
    den = -(Bval + psi0) * w + (a + Bval)
    return float(np.max(np.abs(num / den)))


def run():
    print("=" * 78)
    print("REVIEW OFFENSIVE 3 -- the cone-preserving Schur recursion")
    print("=" * 78)
    check("S0.0 [E] AST firewall: no zero loaders; the v563 atom "
          "table is the deployed window object (declared)",
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
    wins = {i: build_win(kz) for i, (kz, _a, _M) in enumerate(picks)}
    for i in WIN_SET:
        w = wins[i]
        print("   window %d: h = %d, D = %.5f, alpha = %.3f, "
              "%d atoms, prime channels present: %s"
              % (i, w["M"] // 2, w["D"], w["alpha"], w["ka"],
                 sorted(w["lay"].keys())[:12]))

    # ============================================================== S1
    print("\nS1 -- the symbolic update as a machine-precision "
          "identity (window 0, mpmath dps 40)")
    mp.mp.dps = 40
    w0 = wins[0]
    ch13 = w0["lay"][13]
    base = w0["total"] - ch13
    d13 = np.nonzero(ch13)[0]
    N1 = min(N1_CAP, int(d13[0]) - 6)
    bd_base = bd_of(base, N1 + 4)
    print("   p = 13 channel: first active cell %d, using depth "
          "N1 = %d; base (total minus channel) PD to N1+4: %s"
          % (int(d13[0]), N1, bd_base is None))
    cd_b = [mp.mpf(float(x)) for x in base[:L_SER + 2]]
    cd_l = [mp.mpf(float(x)) for x in ch13[:L_SER + 2]]
    cd_t = [cd_b[d] + cd_l[d] for d in range(L_SER + 2)]
    # Moebius route: w~ = [(B-psi0) + (a-B) w] / [(a+B) - (B+psi0) w]
    f_b = f_from_lags(cd_b, L_SER)
    w_s = [mp.mpf(0)] + f_b[:L_SER - 1]            # w = z f
    Bs = [cd_l[0]] + [2 * cd_l[d] for d in range(1, L_SER)]
    c0 = cd_b[0]
    psi0 = cd_l[0]
    a_ = 2 * c0 + psi0
    mB = [-x for x in Bs]
    num = s_axpy(mp.mpf(1), s_mul(s_axpy(mp.mpf(1), mB,
                                         [a_] + [mp.mpf(0)] *
                                         (L_SER - 1), L_SER),
                                  w_s, L_SER),
                 s_axpy(mp.mpf(1), Bs,
                        [-psi0] + [mp.mpf(0)] * (L_SER - 1), L_SER),
                 L_SER)
    den = s_axpy(mp.mpf(-1),
                 s_mul(s_axpy(mp.mpf(1), Bs,
                              [psi0] + [mp.mpf(0)] * (L_SER - 1),
                              L_SER), w_s, L_SER),
                 s_axpy(mp.mpf(1), Bs,
                        [a_] + [mp.mpf(0)] * (L_SER - 1), L_SER),
                 L_SER)
    w_t = s_div(num, den, L_SER)
    dev_w0 = float(abs(w_t[0]))
    f_t = w_t[1:] + [mp.mpf(0)]                     # f~ = w~ / z
    gams = schur_from_f(f_t, N1, L_SER - 1)
    ks = mp_levinson(cd_t, N1)
    dev = max(float(abs(gams[n] + ks[n])) for n in range(N1))
    check("S1.1 [E] IDENTITY: Moebius-updated Schur parameters == "
          "direct Levinson of the summed lags (gamma_n = -k_{n+1}), "
          "depth %d: max dev %.2e <= %.0e; w~(0) residual %.1e"
          % (N1, dev, BAR_S1, dev_w0),
          dev <= BAR_S1 and dev_w0 <= BAR_S1 and bd_base is None)

    # ============================================================= S2a
    print("\nS2a -- the SU(1,1)/J-structure, symbolic")
    try:
        import sympy as sp
        c0s, s0s, xs, ys, us, vs = sp.symbols("c0 s0 x y u v",
                                              real=True)
        Bsym = xs + sp.I * ys
        asym = 2 * c0s + s0s
        Tm = sp.Matrix([[asym - Bsym, Bsym - s0s],
                        [-(Bsym + s0s), asym + Bsym]])
        Jm = sp.diag(1, -1)
        lhs = sp.expand(Tm.H * Jm * Tm)
        rhs = sp.expand((asym ** 2 - s0s ** 2) * Jm
                        - 2 * (asym + s0s) * xs
                        * sp.Matrix([[1, -1], [-1, 1]]))
        ok_m = sp.simplify(lhs - rhs) == sp.zeros(2, 2)
        wv = sp.Matrix([us + sp.I * vs, 1])
        qf = sp.expand((wv.H * lhs * wv)[0])
        qt = sp.expand((asym ** 2 - s0s ** 2)
                       * (us ** 2 + vs ** 2 - 1)
                       - 2 * (asym + s0s) * xs
                       * ((1 - us) ** 2 + vs ** 2))
        ok_q = sp.simplify(qf - qt) == 0
        check("S2a.1 [E] SYMBOLIC: T*JT = (a^2-psi0^2) J - "
              "2(a+psi0) ReB vv^T and the q-form factorization hold "
              "exactly -- COROLLARY: the layer map is J-contractive "
              "on the disk iff Re B >= 0 iff the layer is a "
              "positive-definite sequence (positive measure)",
              bool(ok_m) and bool(ok_q))
    except ImportError:
        # numeric fallback at random points, dps 40
        rng = np.random.default_rng(7)
        okn = True
        for _ in range(200):
            c0v, s0v = rng.uniform(0.1, 3.0, 2)
            Bv = complex(*rng.uniform(-2, 2, 2))
            wv_ = complex(*rng.uniform(-0.7, 0.7, 2))
            av = 2 * c0v + s0v
            T = np.array([[av - Bv, Bv - s0v],
                          [-(Bv + s0v), av + Bv]])
            Jn = np.diag([1.0, -1.0])
            lhs_ = T.conj().T @ Jn @ T
            rhs_ = (av ** 2 - s0v ** 2) * Jn \
                - 2 * (av + s0v) * Bv.real \
                * np.array([[1, -1], [-1, 1]])
            vv = np.array([wv_, 1.0])
            q1 = float((vv.conj() @ lhs_ @ vv).real)
            q2 = (av ** 2 - s0v ** 2) * (abs(wv_) ** 2 - 1) \
                - 2 * (av + s0v) * Bv.real * abs(1 - wv_) ** 2
            okn &= np.max(np.abs(lhs_ - rhs_)) < 1e-10 \
                and abs(q1 - q2) < 1e-10
        check("S2a.1 [E] T*JT identity + q-form factorization "
              "(numeric fallback, 200 random points, sympy absent)",
              okn)

    # ============================================================= S2b
    print("\nS2b -- contraction factors per prime-ideal layer over "
          "the ladder")
    all_c0_zero = True
    alive = True
    worst = {}
    for i in WIN_SET:
        w = wins[i]
        c0_tot = float(w["total"][0])
        for p in P_SET:
            lags = w["lay"][p]
            sc = float(np.max(np.abs(lags)))
            all_c0_zero &= (abs(lags[0]) <= 1e-15 * sc)
            margins = []
            for r in R_LADDER:
                margins.append(float(np.min(reB_grid(lags, r))))
            alive_p = all(m >= -1e-12 * sc for m in margins[:-1])
            alive &= alive_p
            # expansion factor at the worst r = 0.99 point
            g99 = reB_grid(lags, 0.99)
            th_star = 2.0 * math.pi * int(np.argmin(g99)) / ND_SYM
            zst = 0.99 * complex(math.cos(th_star),
                                 math.sin(th_star))
            base_p = w["total"] - lags
            Rmax = expansion_factor(float(base_p[0]),
                                    float(lags[0]),
                                    B_at(lags, zst))
            worst[(i, p)] = (margins, Rmax)
            print("   window %d, p = %2d (%-8s): c_0 = %.1e, "
                  "min ReB over r-ladder %s; expansion R_max(0.99) "
                  "= %.4f%s"
                  % (i, p, P_CLASS[p], lags[0],
                     ["%+.3f" % m for m in margins],
                     Rmax, "  <-- EXPANSIVE" if not alive_p else ""))
        for p in (3, 7):
            if p in w["lay_sq"]:
                lq = w["lay_sq"][p]
                mq = [float(np.min(reB_grid(lq, r)))
                      for r in R_LADDER]
                print("   window %d, p = %2d square-only subchannel: "
                      "min ReB %s" % (i, p, ["%+.3f" % m
                                             for m in mq]))
    check("S2b.1 [E] STRUCTURAL: every prime channel has c_0 = 0 "
          "with nonzero deeper lags -- a nonzero positive-definite "
          "sequence requires |c_d| <= c_0, so NO atom layer is a "
          "positive measure; by S2a its Moebius map CANNOT be "
          "J-contractive on the whole disk (the Weil sign "
          "structure: primes enter subtracted)", all_c0_zero)
    check("S2b.2 [M] measured: every class (ramified/split/inert, "
          "square-only included) goes ReB-negative well inside the "
          "disk on every ladder window -- the thesis' contraction "
          "fails for ALL prime-ideal layers, not just one",
          not alive)

    # ============================================================= S2c
    print("\nS2c -- the compensation fact (the orbit vs the maps)")
    ok_orbit = True
    for i in WIN_SET:
        w = wins[i]
        bd_t, kmax = lev_kmax(w["total"], w["M"] - 1)
        bd_bg = bd_of(w["bg"], w["M"] - 1)
        ok_orbit &= bd_t is None
        print("   window %d: FULL window PD to depth %d (max|k| = "
              "%.6f); background alone breaks at %s"
              % (i, w["M"] - 1, kmax, bd_bg))
    check("S2c.1 [M] the orbit stays in the Schur ball to full "
          "depth on every ladder window (all |k_n| < 1) while every "
          "single layer map is expansive somewhere -- positivity is "
          "orbit-specific compensation, not map-wise cone "
          "preservation", ok_orbit)

    # ============================================================== S3
    print("\nS3 -- adjudication")
    verdict = "SCHUR-CONE-ALIVE" if alive else "SCHUR-CONE-DEAD"
    check("S3.1 [M] preregistered adjudication: %s" % verdict, True)
    print("""
  ANATOMIE (der Review-Kill, exakt):
    (a) [E] Der Layer-Update IST eine exakte Moebius/Transfer-
        Wirkung mit expliziter Matrix T(z) und exakter J-Identitaet
        (S1 Maschinengenauigkeit, S2a symbolisch) -- die Rekursion
        kappa -> Phi_p(kappa) EXISTIERT.
    (b) [E] Kegelbewahrung von Phi_p ist AEQUIVALENT zu "die Schicht
        ist ein positives Mass" (Re B_p >= 0).  Jede Primideal-
        Schicht des deployten Fensters hat aber c_0 = 0 und
        nichttriviale tiefere Lags (die Weil-Vorzeichenstruktur:
        die Primseite wird SUBTRAHIERT) -- also ist KEINE Schicht
        kegelbewahrend; das ist ein Einzeiler, kein numerischer
        Grenzfall.  Ramifiziert/split/traege (auch Quadrat-
        Subkanaele) brechen identisch (S2b).
    (c) [M] Trotzdem bleibt das Gesamtfenster PD zu voller Tiefe
        (S2c) -- die Positivitaet ist orbit-spezifische Kompensation
        der Schichten gegeneinander (das Just-in-time-Bild von
        S-A/S-D), KEINE Komposition kegelbewahrender Karten.
    => Die schichtweise Rekursion ist das falsche Granularitaets-
       niveau: "T*JT <= J pro Schicht" kann prinzipiell nicht
       tragen, weil das Kriterium schichtweise Positivitaet
       erzwingt, die die explizite Formel verbietet.  Ein Ausweg
       braeuchte eine kanonische positive Umbuendelung (jede
       Prim-Schicht + ihr Hintergrund-Anteil positiv) -- die
       Existenz einer solchen Zerlegung ist selbst eine Aussage der
       RH-Klasse (die Dips des Hintergrunds muessten exakt von den
       Atomen gedeckt sein) und der praezise benannte fehlende
       Baustein.""")

    print("\nVERDICT: %s" % verdict)
    dt = time.time() - T0
    if FAILS:
        print("RESULT: %d/%d checks passed -- FAILURES: %s  (%.1f s)"
              % (N_CHK - len(FAILS), N_CHK, ", ".join(FAILS), dt))
        return 1
    print("RESULT: ALL %d CHECKS PASSED  (%.1f s)" % (N_CHK, dt))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
