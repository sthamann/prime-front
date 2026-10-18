#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""read_decay_mechanism_probe -- PRIME.PORT.READDECAY.01
(EXPLORATION ONLY, experiments/; 2026-08-12.)

MISSION.  Resolve the supply/demand paradox at the registered half-gap
level without assuming that the premise is true.  The measured wall obeys

    m_h >= (1/2) mu1(h),   mu1(h) = 4 sin^2(pi/(2h+1)) ~ pi^2/h^2

on the 67-rung registered surface and the 28-rung deep blind holdout, while
the known absolute/isotropic supplies are h-flat or grow.  This probe asks
whether the TRUE phase-sensitive read decays like h^-2, and if so where.

THE EXACT CCXI READ.  For a rung with lag vector c, periodic density D_j,
L = 2M-2, and the PRIME-FREE smooth critical direction x_sm,

    S_j(x) = sum_p x_p sin(theta_j(p-(M-1)/2)),
    rho*_j = (2/L)(D_j - mu1/2),
    K - (mu1/2)I = Gram_{rho*}(S).

Split c = c_win + c_osc, c_win = c_ar + c_sm and
c_osc = c_at - c_sm.  Then

    rho* = rho*_win + rho*_osc,
    E_osc = sum_j rho*_osc,j S_j(x_sm)^2,
    E_win = sum_j rho*_win,j S_j(x_sm)^2,
    E_level = E_win + E_osc
            = x_sm^T(K-(mu1/2)I)x_sm.

The frequency channel is physical omega_j =
2 pi min(j,L-j)/(L D).  CARRIER means omega <= OMEGA_C = 5.25, the
CLV/CLXXXV inherited sub-gamma_1 band (the rung-dependent folded-channel
census is printed; N_BIN=21 below is a fixed comparison grid, not a claim
about that census).  Every channel contribution is an exact DFT read of
the directly assembled prime comb.  The aggregate is independently read
by the CLXXXIX verified-zero explicit formula.

THE CLXXXIX HEART, GENERALIZED ONLY IN ITS TEST FUNCTION.  Put W =
lag_weights_from_v(x_sm,h), so phi(u) = q_read(W,u) and

    E_osc = sum_n 2 Lambda(n)/sqrt(n) phi(log n)
            - 2 int e^(u/2) phi(u) du.

Extend phi linearly from zero at U0 = log(2)/2 to phi(log 2), retain the
deployed pw-linear test through u_end = M D where it vanishes, and write J
for its slope jumps.  Because the deployed smooth comb starts at u=0,
the exact correction LOW_CONT = 2 int_0^log2 e^(u/2) phi(u) du must also
be subtracted (the pre-freeze smoke omission and repair are disclosed
below).  Exactly as in CLXXXIX/CXCIII,

    E_osc_hat = -4 sum_{gamma <= T_c} Re phihat(gamma)
                - TRIV_exact + EXT_CONT - LOW_CONT,
    phihat(gamma) = -gamma^-2 sum_r J_r exp(i gamma v_r),
    |E_osc - E_osc_hat| <= TAILB.

The first 7000 verified ordinates are the finite CLXXXIX input class;
the tail consumes Rosser's N(T) corridor up to T0 = 3e12 and an
unconditional beta in [0,1] bound beyond T0.  The exact prime-side read
wards the zero-side read on every rung.  A finite zero sum is not an
all-h theorem.

THE DECAY-SEAT DECOMPOSITION.  For a channel set C define

    A = sum_C |rho_j|,                         (weight amplitude)
    O = sum_C |rho_j| S_j^2 / A,              (geometric overlap)
    X = |sum_C rho_j S_j^2| /
        sum_C |rho_j| S_j^2.                  (signed cancellation)

Thus |READ_C| = A O X exactly and its log-h slope is the sum of the
three component slopes.  The frozen labels are:

  DECAY-IN-OVERLAP  if E_osc has h-slope in TARGET_SLOPE and O supplies
                    the largest negative component;
  DECAY-IN-READS    if E_osc has h-slope in TARGET_SLOPE and A supplies
                    the largest negative component;
  DECAY-CROSSCHANNEL if E_osc has h-slope in TARGET_SLOPE and X supplies
                    the largest negative component;
  NO-READ-DECAY     otherwise; the level's source-cancellation factor
                    |E_level|/(|E_win|+|E_osc|) is then measured.

TARGET_SLOPE = [-2.5,-1.5], FLAT_SLOPE = [-0.5,+0.5].  These wide
exponent classes are frozen before smoke; no enum depends on a fitted
constant.  A fixed 21-bin carrier matrix records median normalized pair
products b_i b_j, its negative off-diagonal mass, top six bins and
Frobenius stability.

PROVABILITY TYPING.  The smooth direction is built without prime or zero
input.  Its overlap with the measured true direction is a DIAGNOSTIC ward
only; the true direction never enters a bound.  The measured true
direction gets a separate TRUTH-ANATOMY read (including its own CLXXXIX
heart) so a deep loss of smooth/true overlap cannot masquerade as a read
law; every certificate remains on x_sm.  Smooth quadrature is refined
6000 -> 12000 on the inherited subset.  Verdict classes:

  CLASSICAL-GEOMETRIC-CANDIDATE only for DECAY-IN-OVERLAP reproduced by
    the smooth profile; the remaining theorem demands are (G1) a uniform
    smooth overlap asymptotic and (G2) a perturbation theorem transferring
    it to the true bottom direction.
  OPEN-ARITHMETIC for read/cross-channel/source cancellation.  Fixed-h
    reads are finite and exact; standard mean-square/average prime results
    do not supply the required pointwise h^-2 law.  The restricted
    one-parameter family is NOT asserted RH-equivalent.  The uniform
    all-test-direction upgrade is the Weil-positivity face and is
    RH-equivalent; this distinction is printed explicitly.

CERTIFICATE SHAPE + CENSUS.  The sharp cheap phase-sensitive ray bound is

    E_level >= E_win + E_osc_hat - TAILB.

It is tested on the 75-rung CLXXXV census (67 surface + 8 evenly-spaced
deep rungs), against (i) the phase-blind channel triangle bound and
(ii) the cited CCI isotropic/absolute baseline 0/67.  IMPORTANT: positivity
on x_sm is a RAY certificate, not a lower bound on lambda_min.  A full
wall certificate additionally needs a source-only lower bound beta_h for
lambda_2(K_h) and a phase-sensitive residual-vector bound epsilon_h for
||(K_h-RQ_h)x_sm||, so Kato-Temple gives

    lambda_min(K_h) >= RQ_h - epsilon_h^2/(beta_h-RQ_h),
    beta_h > RQ_h.

The same expression with the MEASURED lambda_2 is printed as ORACLE
ANATOMY only.  It never enters the non-circular census.

GATES.
  W1  ladder census 67 surface + 28 deep (full), mu1 identity, deep-table
      prefix byte-exact.
  W2  CCXI DFT/Plancherel/source-split identities on every rung.
  W3  CLXXXIX cache wards (census, monotonicity, gamma_1, Rosser corridor,
      independent zeta spots, T_c < T0), transform/trivial-zero wards and
      |E_osc-E_osc_hat| <= TAILB on every rung.
  W4  inherited classical-direction overlap >= 0.80 on the inherited
      surface subset; 6000/12000 smooth directions overlap >= 0.99 there.
      Full 95-rung overlap is measured, not silently promoted.
  T   tau screens: the h^-2-normalized level and normalized
      source-cancellation law are regressed against measured m_h; a real
      independent law should be PASS, |slope| <= 0.30 (RELOC >= 0.70).
  C   controls MUST FIRE: smooth has no oscillatory read and fails the
      level; scramble seed 1 breaks the level/decay cancellation; Epstein
      x^2+5y^2 at kz=9 fails; cosh injection A=.01, delta=.05, gamma0=10
      breaks the level on at least one surface rung.  The exact identity
      remains world-blind and is not counted as discrimination.
  A   anti-circularity: x_sm only in every bound; measured x_true,
      lambda_2 and Kato-Temple oracle are diagnostics only.  No M-eigendata
      enters a certificate.  Verified zeros enter only the finite supply
      side and are tested against the independent prime-side assembly.

EXTERNAL-CITED PEDIGREE: Platt--Trudgian (Bull. LMS 53, 2021), RH true
through 3e12 (on-line status of every summed ordinate); Rosser (AJM 63,
1941, Thm. 19), explicit N(T) corridor; Davenport, Multiplicative Number
Theory, Ch. 17, compact-test explicit-formula class; Kato--Temple
inequality (Temple 1928 / Kato, Perturbation Theory for Linear Operators).
No unproved statement from these sources is consumed.

FROZEN NUMERICAL BARS (pre-smoke): OMEGA_C=5.25; N_BIN=21; N_Z=7000;
NG_SMOOTH=6000, NG_REFINE=12000; TARGET_SLOPE=(-2.5,-1.5);
FLAT_SLOPE=(-.5,.5); OVERLAP_WARD=.80 inherited on SUBSET =
(9,13,26,40,60,90,121); SMOOTH_REFINE_WARD=.99; ID_WARD=1e-9;
TRANS_WARD=1e-9; HEART_TOL=1e-9 scaled; ZETA_TOL=1e-6 at 24 spots;
TAU_PASS=.30, TAU_RELOC=.70; deep table 4e6, H_HOLD=(128,2900);
certificate ladder 67+8; runtime cap 25 min.  Smoke mode
READDECAY_SMOKE=1 uses six inherited surface rungs + two shallow deep
rungs, defers full census wards, and runs the same identities and
controls on that reduced set.

SMOKE DISCLOSURE (pre-freeze, fail-first; READDECAY_SMOKE=1, six inherited
surface rungs + two shallow deep rungs).  SMOKE-1 used pre-freeze SPEC SHA
dc3a5e00, exit 1, 17/21 checks in 15.7 s.  Four failures:
  A1  I1 reported 2.26e3 because the diagnostic compared sum S_j^2 to 1;
      CCXI Plancherel is (2/L) sum S_j^2 = 1.  The representation energies
      themselves were correctly normalized.  Mechanical repair: restore
      the exact 2/L factor; ID_WARD unchanged.
  A2  I4 heart excess was +1.23.  The deployed c_sm integrates q_read from
      u=0, while the explicit compact test begins at U0 and the v0
      translation corrected only its artificial U0->log2 ramp.  The
      omitted exact term is LOW_CONT = 2 int_0^log2 e^(u/2)q_read du.
      It is now computed in the existing piecewise-linear closed form and
      subtracted.  No tail bar or zero sum changed.
  A3  The two shallow deep rungs exposed smooth/true overlaps down to
      1.33e-6 (surface inherited ward still passed at 0.8775).  Therefore
      the v0 combined x_sm law (+1.333 for shifted level, E_osc +0.733)
      mixed mechanism truth with failure of the classical proxy.
      Pre-freeze correction: add a separately labelled measured-true
      direction anatomy, with its own DFT and CLXXXIX wards; the certificate
      continues to use x_sm only.  No eigendata enters a bound.
  A4  Epstein had x_sm shifted ray +2.470 and cosh failed 0/6 ON THAT RAY,
      although predecessor controls are wall-eigenvalue controls.  The
      result locates where they die: outside the smooth ray.  The controls
      now print both the x_sm ray and measured wall minimum and fire only
      on the inherited wall criterion; no discrimination threshold moved.
All cache/Rosser/transform/trivial-zero/surface-overlap/refinement/smooth/
scramble checks passed.  Smoke truth ray passed 8/8; the phase-blind and
7000-zero smooth-ray bounds both closed 0/8.  No success bar, slope band,
enum, OMEGA_C, tau band or census target moved after smoke.

SMOKE-2 (post-amendment freeze candidate, SPEC SHA 8b4d6c61): exit 0,
21/21 in 17.4 s.  CCXI identities max 1.72e-14; both smooth and measured-
true CLXXXIX hearts passed, worst scaled excess -4.39e-3; inherited
surface overlap 0.8775 and smooth-refinement 1.000000 passed.  The reduced
truth laws were E_osc h^+0.105, shifted level h^-1.785, source cancellation
h^-1.889; E_osc components A/O/X = h^-0.572/h^+0.677/h^-0.001, hence
NO-READ-DECAY / LEVEL-DECAY-IN-SOURCE-CANCELLATION.  Normalized level and
source-cancellation tau screens PASS at -0.079/-0.020; overlap AMBIG
-0.351.  Truth and smooth rays pass 8/8; absolute and signed-7000-zero
ray bounds close 0/8; Kato-Temple oracle 0/8.  Controls: smooth 8/8,
scramble wall 6/6, Epstein wall -1.006e1 while its smooth ray is +2.470,
cosh wall 5/6 while its smooth ray is 0/6 -- the latter two die outside
the smooth ray.  No further amendment; this disclosure freezes the
full-run specification.

HONEST SCOPE.  This is an experiment-only mechanism diagnosis.  It
neither proves the registered inequality for all h nor makes an RH claim.
No marker, ledger, paper, website, manifest or verification file moves.
Stdout only.
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import exterior_square_factorization_probe as extq  # noqa: E402 READ-ONLY
import subgamma_fourier_bound_probe as subg  # noqa: E402  READ-ONLY
import w2_pairing_structure_probe as w2  # noqa: E402  READ-ONLY
import w2_verified_supply_consumption_probe as vz  # noqa: E402 READ-ONLY


SMOKE = os.environ.get("READDECAY_SMOKE", "") == "1"
ZC_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
N_Z = 7000
OMEGA_C = 5.25
N_BIN = 21
NG_SMOOTH = 6000
NG_REFINE = 12000
TARGET_SLOPE = (-2.5, -1.5)
FLAT_SLOPE = (-0.5, 0.5)
SUBSET = (9, 13, 26, 40, 60, 90, 121)
OVERLAP_WARD = 0.80
SMOOTH_REFINE_WARD = 0.99
ID_WARD = 1e-9
TRANS_WARD = 1e-9
HEART_TOL = 1e-9
ZETA_TOL = 1e-6
NS_ZETA = 24
CORR_EPS = 1e-6
DPS_ERR = 1e-9
TAU_PASS = 0.30
TAU_RELOC = 0.70
TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
KZ_SURF = 150
KZ_DEEP = 400
N_SURF = 67
N_DEEP = 28
N_CERT_DEEP = 8
SCR_SEED = 1
CTRL_KZ = 9
INJ_A = 0.01
INJ_DELTA = 0.05
INJ_GAMMA = 10.0
LN2 = math.log(2.0)
BANNED_IDS = ("primerange", "isprime", "primepi", "nextprime", "prevprime")
SMOKE_SURF = (9, 13, 26, 60, 90, 121)

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78, flush=True)


def ast_scan():
    tree = ast.parse(open(os.path.abspath(__file__), encoding="utf-8").read())
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return sorted(set(bad))


def band(values):
    values = np.asarray(values, float)
    return float(np.min(values)), float(np.median(values)), float(np.max(values))


def bfmt(values):
    return "%.3e/%.3e/%.3e" % band(values)


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    good = np.isfinite(x) & np.isfinite(y)
    x, y = x[good], y[good]
    if len(x) < 3 or float(np.var(x)) == 0.0:
        return float("nan"), float("nan"), float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / np.var(x))
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, 1.0 - ss / st if st > 0 else float("nan")


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    good = np.isfinite(x) & np.isfinite(y)
    x, y = x[good], y[good]
    _a, b, r2 = ols_line(x, y)
    if len(x) < 4:
        return b, float("nan"), r2, len(x)
    bb = []
    for i in range(len(x)):
        keep = np.ones(len(x), bool)
        keep[i] = False
        bb.append(ols_line(x[keep], y[keep])[1])
    bb = np.asarray(bb, float)
    se = math.sqrt((len(x) - 1) / len(x)
                   * float(np.sum((bb - np.mean(bb)) ** 2)))
    return b, se, r2, len(x)


def law(rows, key, label, positive=False):
    x = np.array([r["h"] for r in rows], float)
    y = np.array([r[key] for r in rows], float)
    if not positive:
        y = np.abs(y)
    good = y > 1e-300
    b, se, r2, n = jack_slope(np.log10(x[good]), np.log10(y[good]))
    print("    %-27s h^%+.3f  (2SE %.3f, R2 %.3f, n=%d, excl=%d)"
          % (label, b, 2 * se, r2, n, len(y) - n))
    return b, se, r2


def tau_screen(rows, values, label):
    vals = np.asarray(values, float)
    tau = np.array([r["m"] for r in rows], float)
    good = (vals > 1e-300) & (tau > 1e-300)
    b, se, r2, n = jack_slope(np.log(tau[good]), np.log(vals[good]))
    if np.isfinite(b) and abs(b) <= TAU_PASS:
        typ = "PASS"
    elif np.isfinite(b) and b >= TAU_RELOC:
        typ = "RELOC"
    else:
        typ = "AMBIG"
    print("    %-31s %s slope %+.3f (2SE %.3f, R2 %.3f, n=%d)"
          % (label, typ, b, 2 * se, r2, n))
    return typ, b


def smooth_comb(alpha, ng=NG_SMOOTH):
    u = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mu = 2.0 * np.exp(u / 2.0) * (2.0 * alpha / ng)
    return u, mu


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def frame_of(alpha, M, h, kz, uu, mu, lam_tab, segment):
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0], float)
    D = 2.0 * alpha / M
    c_ar = np.asarray(core.arch_lags(M, D), float)
    return dict(alpha=float(alpha), M=int(M), h=int(h), kz=int(kz),
                D=float(D), L=2 * int(M) - 2, uu=np.asarray(uu, float),
                mu=np.asarray(mu, float), lam_tab=lam_tab,
                c_at=c_at, c_ar=c_ar, mu1=mu1_of(h), segment=segment)


def surface_specs():
    out = []
    for kz in range(2, KZ_SURF + 1):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        out.append(frame_of(rr["alpha"], rr["M"], rr["h"], kz,
                            rr["uu"], 2.0 * np.asarray(rr["lam"], float),
                            core.LAM_TAB, "surface"))
    return sorted(out, key=lambda r: (r["h"], r["kz"]))


def deep_specs():
    lam = core.von_mangoldt_table(TAB_EXT)
    nn = np.nonzero(lam > 0.0)[0]
    u = np.log(nn.astype(float))
    mu = 2.0 * lam[nn] / np.sqrt(nn.astype(float))
    gaps = np.diff(u)
    ext = dict(lam=lam, nn=nn, u=u, mu=mu, gaps=gaps)
    out = []
    for kz in range(2, min(KZ_DEEP + 1, len(u) - 1)):
        alpha = float(u[kz])
        Dk = 0.5 * float(gaps[kz]) / float(core.NU_MAIN)
        M = int(math.ceil(alpha / Dk - 1e-9)) + 1
        if M % 2:
            M += 1
        h = M // 2
        X = math.exp(2.0 * alpha)
        if not (core.ATOM_MAX < X <= TAB_EXT):
            continue
        if not (H_HOLD[0] <= h <= H_HOLD[1]):
            continue
        ka = int(np.searchsorted(u, 2.0 * alpha + 1e-14,
                                 side="right"))
        out.append(frame_of(alpha, M, h, kz, u[:ka], mu[:ka], lam,
                            "deep"))
    return sorted(out, key=lambda r: (r["h"], r["kz"])), ext


def int_exp_linear(a, b, fa, fb):
    slope = (fb - fa) / (b - a)
    return 2.0 * (math.exp(b / 2.0) * (2.0 * fb - 4.0 * slope)
                  - math.exp(a / 2.0) * (2.0 * fa - 4.0 * slope))


def full_phi(W, D, M):
    """Compact pw-linear explicit-formula test for the complete oscillatory
    energy, including the no-prime left extension."""
    u_end = M * D
    knots = D * np.arange(1, M, dtype=float)
    knots = knots[(knots > LN2 + 1e-12) & (knots < u_end - 1e-12)]
    edges = np.concatenate([[subg.U0, LN2], knots, [u_end]])
    fvals = np.zeros(len(edges))
    fvals[1:] = w2.q_read(W, edges[1:], D, M)
    fvals[-1] = 0.0
    slopes = np.diff(fvals) / np.diff(edges)
    J = np.empty(len(edges))
    J[0] = slopes[0]
    J[1:-1] = slopes[1:] - slopes[:-1]
    J[-1] = -slopes[-1]
    keep = np.abs(J) > 1e-15
    low_pieces = w2.weight_pieces(W, 0.0, LN2, D, M)
    return dict(edges=edges, fvals=fvals, slopes=slopes,
                v=edges[keep], J=J[keep],
                sd=float(np.sum(np.abs(J[keep]))),
                vmax=float(edges[-1]),
                ext_cont=int_exp_linear(subg.U0, LN2, 0.0,
                                        float(fvals[1])),
                low_cont=w2.tcont_of(low_pieces),
                triv=vz.triv_pl(edges, fvals, slopes),
                fmax=float(np.max(np.abs(fvals))))


def zero_read(pc, gam, abel, s2tail, inv2, inv3):
    zsum = vz.zsum4re(pc["v"], pc["J"], gam)
    center = (-zsum - pc["triv"] + pc["ext_cont"]
              - pc["low_cont"])
    dps = 4.0 * pc["sd"] * (pc["vmax"] * inv2 + 2.0 * inv3) \
        * DPS_ERR
    tail = (4.0 * pc["sd"] * abel
            + 4.0 * math.exp(pc["vmax"] / 2.0) * pc["sd"] * s2tail
            + dps + 1e-12 * (1.0 + abs(pc["triv"])))
    return center, tail


def decomp(rho, overlap, mask=None):
    if mask is None:
        mask = np.ones(len(rho), bool)
    rr = rho[mask]
    oo = overlap[mask]
    amp = float(np.sum(np.abs(rr)))
    absread = float(np.sum(np.abs(rr) * oo))
    signed = abs(float(np.sum(rr * oo)))
    return dict(amp=amp, overlap=absread / max(amp, 1e-300),
                cancel=signed / max(absread, 1e-300),
                signed=signed, absread=absread)


def bin_channels(omega, contrib):
    out = np.zeros(N_BIN)
    keep = omega <= OMEGA_C + 1e-12
    idx = np.minimum((omega[keep] / OMEGA_C * N_BIN).astype(int),
                     N_BIN - 1)
    np.add.at(out, idx, contrib[keep])
    return out


def analyze_rung(row, gam, s2tail, inv2, inv3, refine=False):
    alpha, M, h, D, L = (row["alpha"], row["M"], row["h"],
                          row["D"], row["L"])
    us, ms = smooth_comb(alpha)
    c_sm = np.asarray(core.atom_lags_at(alpha, M, us, ms)[0], float)
    c_win = row["c_ar"] + c_sm
    c_true = row["c_ar"] + row["c_at"]
    Ksm = core.odd_toeplitz(c_win, M)
    K = core.odd_toeplitz(c_true, M)
    esm, Vsm = np.linalg.eigh(Ksm)
    et, Vt = np.linalg.eigh(K)
    xsm = Vsm[:, 0]
    xt = Vt[:, 0]
    if float(xsm @ xt) < 0.0:
        xt = -xt
    W = core.lag_weights_from_v(xsm, h)
    Wt = core.lag_weights_from_v(xt, h)
    e_win_raw = float(c_win @ W)
    e_osc = float((row["c_at"] - c_sm) @ W)
    rq = float(c_true @ W)
    e_level = rq - 0.5 * row["mu1"]
    source_cancel = abs(e_level) / max(abs(e_win_raw - 0.5 * row["mu1"])
                                       + abs(e_osc), 1e-300)
    true_e_win_raw = float(c_win @ Wt)
    true_e_osc = float((row["c_at"] - c_sm) @ Wt)
    true_e_level = float(et[0]) - 0.5 * row["mu1"]
    true_source_cancel = abs(true_e_level) / max(
        abs(true_e_win_raw - 0.5 * row["mu1"]) + abs(true_e_osc), 1e-300)

    Dtrue = extq.grid_density(c_true)
    Dosc = extq.grid_density(row["c_at"] - c_sm)
    rho_osc = 2.0 * Dosc / L
    rho_star = 2.0 * Dtrue / L - row["mu1"] / L
    rho_win = rho_star - rho_osc
    S = extq.sine_reads(np.column_stack([xsm, xt]), M)
    osm = S[:, 0] ** 2
    otr = S[:, 1] ** 2
    jj = np.arange(L)
    omega = 2.0 * math.pi * np.minimum(jj, L - jj) / (L * D)
    carrier = omega <= OMEGA_C + 1e-12
    do_car = decomp(rho_osc, osm, carrier)
    do_all = decomp(rho_osc, osm)
    dt_all = decomp(rho_star, osm)
    true_do_car = decomp(rho_osc, otr, carrier)
    true_do_all = decomp(rho_osc, otr)
    true_dt_all = decomp(rho_star, otr)
    t_osc = rho_osc * osm
    t_win = rho_win * osm
    t_total = rho_star * osm
    true_t_osc = rho_osc * otr
    true_t_win = rho_win * otr
    true_t_total = rho_star * otr
    source_cos = float(np.dot(t_win, t_osc) / max(
        float(np.linalg.norm(t_win) * np.linalg.norm(t_osc)), 1e-300))
    true_source_cos = float(np.dot(true_t_win, true_t_osc) / max(
        float(np.linalg.norm(true_t_win) * np.linalg.norm(true_t_osc)),
        1e-300))
    bins = bin_channels(omega, t_total)
    true_bins = bin_channels(omega, true_t_total)

    pc = full_phi(W, D, M)
    true_pc = full_phi(Wt, D, M)
    tg = vz.tail_grid(D, float(gam[-1]))
    abel = subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                           n_start=float(N_Z))
    osc_hat, tailb = zero_read(pc, gam, abel, s2tail, inv2, inv3)
    true_osc_hat, true_tailb = zero_read(
        true_pc, gam, abel, s2tail, inv2, inv3)
    e_win_shift = e_win_raw - 0.5 * row["mu1"]
    ray_lb = e_win_shift + osc_hat - tailb
    abs_lb = e_win_shift - do_all["absread"]

    resid_vec = K @ xsm - rq * xsm
    resid = float(np.linalg.norm(resid_vec))
    beta_oracle = float(et[1])
    kt_oracle = float("nan")
    if beta_oracle > rq:
        kt_oracle = rq - resid * resid / (beta_oracle - rq)

    rep_level = abs(float(np.sum(t_total)) - e_level)
    rep_osc = abs(float(np.sum(t_osc)) - e_osc)
    rep_true_level = abs(float(np.sum(true_t_total)) - true_e_level)
    rep_true_osc = abs(float(np.sum(true_t_osc)) - true_e_osc)
    rep_plan = max(abs(2.0 * float(np.sum(osm)) / L - 1.0),
                   abs(2.0 * float(np.sum(otr)) / L - 1.0))
    rep_scale = max(1.0, abs(e_win_raw), abs(e_osc))
    trans = complex(-np.sum(pc["J"] * np.exp(25j * pc["v"]))
                    / 25.0 ** 2)
    trans_seg = vz.hat_seg_c(pc["edges"], pc["fvals"],
                             pc["slopes"], 25j)
    true_trans = complex(-np.sum(
        true_pc["J"] * np.exp(25j * true_pc["v"])) / 25.0 ** 2)
    true_trans_seg = vz.hat_seg_c(
        true_pc["edges"], true_pc["fvals"], true_pc["slopes"], 25j)
    trans_dev = max(abs(trans - trans_seg) / max(1.0, abs(trans)),
                    abs(true_trans - true_trans_seg)
                    / max(1.0, abs(true_trans)))
    triv_env = vz.triv_env_pl(pc["edges"], pc["fvals"])
    heart_excess = (abs(e_osc - osc_hat) - tailb
                    - HEART_TOL * rep_scale) / rep_scale
    true_rep_scale = max(1.0, abs(true_e_win_raw), abs(true_e_osc))
    true_heart_excess = (abs(true_e_osc - true_osc_hat) - true_tailb
                         - HEART_TOL * true_rep_scale) / true_rep_scale

    refine_overlap = float("nan")
    if refine:
        ur, mr = smooth_comb(alpha, NG_REFINE)
        c_ref = row["c_ar"] + np.asarray(
            core.atom_lags_at(alpha, M, ur, mr)[0], float)
        _er, Vr = np.linalg.eigh(core.odd_toeplitz(c_ref, M))
        refine_overlap = abs(float(xsm @ Vr[:, 0]))

    row.update(c_sm=c_sm, W=W, xsm=xsm, m=float(et[0]),
               lambda2=float(et[1]), lam_sm=float(esm[0]),
               overlap_true=abs(float(xsm @ xt)),
               profile_overlap=float(np.dot(osm, otr) / max(
                   float(np.linalg.norm(osm) * np.linalg.norm(otr)),
                   1e-300)),
               refine_overlap=refine_overlap, rq=rq,
               e_win=e_win_shift, e_osc=e_osc, e_level=e_level,
               source_cancel=source_cancel, source_cos=source_cos,
               true_e_win=true_e_win_raw - 0.5 * row["mu1"],
               true_e_osc=true_e_osc, true_e_level=true_e_level,
               true_source_cancel=true_source_cancel,
               true_source_cos=true_source_cos,
               osc_amp_car=do_car["amp"],
               osc_overlap_car=do_car["overlap"],
               osc_cancel_car=do_car["cancel"],
               osc_signed_car=do_car["signed"],
               osc_abs_car=do_car["absread"],
               osc_amp_all=do_all["amp"],
               osc_overlap_all=do_all["overlap"],
               osc_cancel_all=do_all["cancel"],
               osc_abs_all=do_all["absread"],
               total_amp=dt_all["amp"],
               total_overlap=dt_all["overlap"],
               total_cancel=dt_all["cancel"],
               total_abs=dt_all["absread"],
               true_osc_amp_car=true_do_car["amp"],
               true_osc_overlap_car=true_do_car["overlap"],
               true_osc_cancel_car=true_do_car["cancel"],
               true_osc_signed_car=true_do_car["signed"],
               true_osc_abs_car=true_do_car["absread"],
               true_osc_abs_all=true_do_all["absread"],
               true_total_amp=true_dt_all["amp"],
               true_total_overlap=true_dt_all["overlap"],
               true_total_cancel=true_dt_all["cancel"],
               true_total_abs=true_dt_all["absread"],
               carrier_count=int(np.sum(
                   np.arange(L // 2 + 1) * 2.0 * math.pi / (L * D)
                   <= OMEGA_C + 1e-12)),
               carrier_share=float(np.sum(t_osc[carrier])
                                   / (e_osc if abs(e_osc) > 1e-300
                                      else 1e-300)),
               true_carrier_share=float(np.sum(true_t_osc[carrier])
                                        / (true_e_osc
                                           if abs(true_e_osc) > 1e-300
                                           else 1e-300)),
               bins=bins, true_bins=true_bins,
               osc_hat=osc_hat, tailb=tailb,
               true_osc_hat=true_osc_hat, true_tailb=true_tailb,
               ray_lb=ray_lb, abs_lb=abs_lb, resid=resid,
               kt_oracle=kt_oracle, beta_oracle=beta_oracle,
               rep_dev=max(rep_level, rep_osc, rep_true_level,
                           rep_true_osc, rep_plan) / max(rep_scale,
                                                        true_rep_scale),
               trans_dev=trans_dev,
               triv_ok=abs(pc["triv"]) <= triv_env * (1 + 1e-9) + 1e-15,
               true_triv_ok=abs(true_pc["triv"]) <= vz.triv_env_pl(
                   true_pc["edges"], true_pc["fvals"]) * (1 + 1e-9) + 1e-15,
               heart_excess=heart_excess,
               true_heart_excess=true_heart_excess,
               abel=abel, sd=pc["sd"], true_sd=true_pc["sd"])
    del K, Ksm, Vsm, Vt, S, Dtrue, Dosc
    return row


def source_control_energy(row, c_at):
    return float((row["c_ar"] + c_at) @ row["W"]
                 - 0.5 * row["mu1"])


def control_wall_and_seat(row, c_at):
    K = core.odd_toeplitz(row["c_ar"] + c_at, row["M"])
    wall = float(np.linalg.eigvalsh(K)[0] - 0.5 * row["mu1"])
    Tb = core.parity_basis(row["h"], 2).T
    seat = Tb.T @ (K @ Tb) - 0.5 * row["mu1"] * np.eye(2)
    det = float(seat[0, 0] * seat[1, 1] - seat[0, 1] ** 2)
    return wall, det


def controls(rows, surface_rows):
    smooth_fail = sum(r["lam_sm"] - 0.5 * r["mu1"] < 0.0 for r in rows)
    scramble_vals = []
    scramble_wall = []
    scramble_det = []
    cosh_vals = []
    cosh_wall = []
    cosh_det = []
    for r in surface_rows:
        rr = core.build_window(r["kz"], scramble_seed=SCR_SEED)
        cs = np.asarray(core.atom_lags_at(
            r["alpha"], r["M"], rr["uu"],
            2.0 * np.asarray(rr["lam"], float))[0], float)
        scramble_vals.append(source_control_energy(r, cs))
        cw, cd = control_wall_and_seat(r, cs)
        scramble_wall.append(cw)
        scramble_det.append(cd)
        tt = np.arange(r["M"]) * r["D"]
        cinj = INJ_A * np.cos(INJ_GAMMA * tt) \
            * (np.cosh(INJ_DELTA * tt) - 1.0)
        cosh_vals.append(r["e_level"] + float(cinj @ r["W"]))
        cw, cd = control_wall_and_seat(r, r["c_at"] + cinj)
        cosh_wall.append(cw)
        cosh_det.append(cd)
    scramble_vals = np.asarray(scramble_vals)
    scramble_wall = np.asarray(scramble_wall)
    scramble_det = np.asarray(scramble_det)
    cosh_vals = np.asarray(cosh_vals)
    cosh_wall = np.asarray(cosh_wall)
    cosh_det = np.asarray(cosh_det)
    ctrl = next(r for r in surface_rows if r["kz"] == CTRL_KZ)
    N = int(math.floor(math.exp(2.0 * ctrl["alpha"]))) + 1
    lamE = w2.lambda_eps(N)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    cE = np.asarray(core.atom_lags_at(
        ctrl["alpha"], ctrl["M"], np.log(nn.astype(float)),
        2.0 * lamE[nn] / np.sqrt(nn.astype(float)))[0], float)
    epstein_ray = source_control_energy(ctrl, cE)
    epstein_wall, epstein_det = control_wall_and_seat(ctrl, cE)
    if len(surface_rows) >= 4:
        hs = np.array([r["h"] for r in surface_rows], float)
        b_scr, se_scr, r2_scr, _n = jack_slope(
            np.log10(hs), np.log10(np.maximum(np.abs(scramble_vals), 1e-300)))
    else:
        b_scr = se_scr = r2_scr = float("nan")
    return dict(smooth_fail=smooth_fail,
                scramble_ray_fail=int(np.sum(scramble_vals < 0.0)),
                scramble_wall_fail=int(np.sum(scramble_wall < 0.0)),
                scramble_det_fail=int(np.sum(scramble_det < 0.0)),
                scramble_kz9=float(scramble_vals[
                    [r["kz"] for r in surface_rows].index(CTRL_KZ)]),
                scramble_wall_kz9=float(scramble_wall[
                    [r["kz"] for r in surface_rows].index(CTRL_KZ)]),
                scramble_slope=b_scr, scramble_se=se_scr,
                scramble_r2=r2_scr,
                cosh_ray_fail=int(np.sum(cosh_vals < 0.0)),
                cosh_wall_fail=int(np.sum(cosh_wall < 0.0)),
                cosh_det_fail=int(np.sum(cosh_det < 0.0)),
                epstein_ray=epstein_ray, epstein_wall=epstein_wall,
                epstein_det=epstein_det)


def cancellation_matrix(rows):
    B = np.array([r["true_bins"] for r in rows], float)
    den = np.sum(np.abs(B), axis=1)
    good = den > 1e-300
    BN = B[good] / den[good, None]
    mats = np.einsum("ni,nj->nij", BN, BN)
    C = np.median(mats, axis=0)
    stability = np.median(np.linalg.norm(
        mats - C[None, :, :], axis=(1, 2)))
    diag = float(np.trace(C))
    off = C - np.diag(np.diag(C))
    neg = float(-np.sum(np.minimum(off, 0.0)))
    pos = float(np.sum(np.maximum(off, 0.0)))
    medabs = np.median(np.abs(BN), axis=0)
    top = np.argsort(-medabs)[:6]
    sign_stab = np.maximum(np.mean(BN[:, top] >= 0.0, axis=0),
                           np.mean(BN[:, top] <= 0.0, axis=0))
    return C, top, stability, diag, neg, pos, sign_stab


def finish(labels=None):
    section("VERDICT")
    passed = sum(1 for _name, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}.get(KILLS[0], KILLS[0])
    else:
        verdict = " / ".join(labels or ["READDECAY-MEASURED"])
    print("    %s" % verdict)
    print("""
    HONEST SCOPE: fixed-rung reads are exact finite computations and the
    verified-zero centers are finite EXTERNAL-CITED supply data.  A ray
    bound along the prime-free smooth direction is not a lower bound on
    lambda_min.  The missing source-only beta_h + residual-vector bounds
    are not supplied or hidden.  The restricted smooth-direction family
    is not asserted RH-equivalent; the all-direction Weil-positivity
    upgrade is RH-equivalent.  NO RH claim; no marker move; experiment
    only.""")
    print("    KILLS: %s" % (", ".join(KILLS) if KILLS else "none"))
    print("    checks %d/%d passed  [%.1f s]"
          % (passed, len(CHECKS), time.time() - T0))
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.PORT.READDECAY.01 -- true read h-laws and their seat")
    spec_sha = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % spec_sha)
    print("    mode = %s; NO RH claim; experiments only"
          % ("SMOKE (pre-freeze)" if SMOKE else "FROZEN"))
    check("S0 AST firewall clean", not ast_scan(), str(ast_scan()),
          kill="K2")

    section("Z -- CLXXXIX finite verified-zero input")
    check("Z0 cache present", os.path.exists(ZC_NPY), kill="K1")
    if KILLS:
        return finish()
    gam = np.load(ZC_NPY)
    check("Z1 7000 strictly increasing ordinates; gamma1 dev %.2e"
          % abs(float(gam[0]) - subg.GAMMA1),
          len(gam) == N_Z and bool(np.all(np.diff(gam) > 0.0))
          and abs(float(gam[0]) - subg.GAMMA1) <= 2e-6, kill="K2")
    kk = np.arange(1, N_Z + 1, dtype=float)
    ok_corr = ((kk <= subg.n_up(gam + CORR_EPS))
               & (kk >= subg.n_lo(gam + CORR_EPS))
               & (kk - 1 <= subg.n_up(np.maximum(gam - CORR_EPS, 2.0)))
               & (kk - 1 >= subg.n_lo(np.maximum(gam - CORR_EPS, 2.0))))
    check("Z2 Rosser corridor both sides %d/%d"
          % (int(np.sum(ok_corr)), N_Z), bool(np.all(ok_corr)), kill="K2")
    from mpmath import mp as _mp, mpc as _mpc
    from mpmath import zeta as _zeta
    _mp.dps = 20
    zi = np.unique(np.geomspace(1, N_Z, NS_ZETA).astype(int)) - 1
    zworst = max(float(abs(_zeta(_mpc(0.5, float(gam[i]))))) for i in zi)
    check("Z3 independent zeta spots worst %.2e <= %.0e"
          % (zworst, ZETA_TOL), zworst <= ZETA_TOL, kill="K2")
    check("Z4 T_c %.4f < T0 %.1e"
          % (float(gam[-1]), subg.T0_RH),
          float(gam[-1]) < subg.T0_RH, kill="K2")
    inv2 = float(np.sum(1.0 / gam ** 2))
    inv3 = float(np.sum(1.0 / gam ** 3))
    s2tail = subg.s2_tail()

    section("W -- 67 surface + 28 deep frames")
    surf_all = surface_specs()
    deep_all, dext = deep_specs()
    prefix = bool(np.array_equal(
        dext["lam"][:core.ATOM_MAX + 1], core.LAM_TAB))
    check("W0 deep table prefix byte-exact", prefix, kill="K2")
    if SMOKE:
        surf = [r for r in surf_all if r["kz"] in SMOKE_SURF]
        deep = deep_all[:2]
        check("W1 smoke ladder %d surface + %d deep; full census deferred"
              % (len(surf), len(deep)), len(surf) == 6 and len(deep) == 2,
              kill="K1")
    else:
        surf, deep = surf_all, deep_all
        check("W1 ladder census %d surface + %d deep == 67 + 28"
              % (len(surf), len(deep)),
              len(surf) == N_SURF and len(deep) == N_DEEP, kill="K1")
    if KILLS:
        return finish()
    rows = surf + deep
    print("    h range %d..%d; analyzing %d exact read functionals"
          % (min(r["h"] for r in rows), max(r["h"] for r in rows),
             len(rows)))
    for i, r in enumerate(rows):
        analyze_rung(r, gam, s2tail, inv2, inv3,
                     refine=(r["segment"] == "surface"
                             and r["kz"] in SUBSET))
        if (i + 1) % 10 == 0 or i + 1 == len(rows):
            print("    ... %d/%d rungs [%.1f s]"
                  % (i + 1, len(rows), time.time() - T0), flush=True)

    section("I -- identity wards and smooth-direction ward")
    rep = max(r["rep_dev"] for r in rows)
    trans = max(r["trans_dev"] for r in rows)
    heart = max(max(r["heart_excess"], r["true_heart_excess"])
                for r in rows)
    check("I1 CCXI DFT/Plancherel/source split max scaled dev %.2e"
          % rep, rep <= ID_WARD, kill="K3")
    check("I2 CLXXXIX jump/segment transform max dev %.2e"
          % trans, trans <= TRANS_WARD, kill="K3")
    check("I3 trivial-zero envelope on %d/%d"
          % (sum(r["triv_ok"] and r["true_triv_ok"] for r in rows),
             len(rows)),
          all(r["triv_ok"] and r["true_triv_ok"] for r in rows),
          kill="K2")
    check("I4 HEART |Eosc-Ehat| <= TAILB on smooth + measured-true "
          "reads every rung; worst scaled excess %.2e"
          % heart, heart <= 0.0, kill="K2")
    subrows = [r for r in rows if r["segment"] == "surface"
               and r["kz"] in SUBSET]
    omin = min(r["overlap_true"] for r in subrows)
    rmin = min(r["refine_overlap"] for r in subrows)
    check("I5 inherited classical-direction overlap ward min %.4f >= %.2f"
          % (omin, OVERLAP_WARD), omin >= OVERLAP_WARD, kill="K2")
    check("I6 smooth 6000/12000 refinement overlap min %.6f >= %.2f"
          % (rmin, SMOOTH_REFINE_WARD), rmin >= SMOOTH_REFINE_WARD,
          kill="K2")
    print("    full true/smooth vector overlap %s" %
          bfmt([r["overlap_true"] for r in rows]))
    print("    full S^2 channel-profile overlap %s" %
          bfmt([r["profile_overlap"] for r in rows]))
    print("    smooth zero-heart slack log10(TAILB/|resid|) %s dex" % bfmt(
        [math.log10(r["tailb"] / max(abs(r["e_osc"] - r["osc_hat"]),
                                            1e-300)) for r in rows]))
    print("    true zero-heart slack log10(TAILB/|resid|) %s dex" % bfmt(
        [math.log10(r["true_tailb"] / max(
            abs(r["true_e_osc"] - r["true_osc_hat"]), 1e-300))
         for r in rows]))

    section("L -- true h-laws and the decay seat")
    print("    MEASURED-TRUE direction laws (diagnostic truth; never a bound):")
    slopes = {}
    for key, label, pos in (
            ("mu1", "mu1", True),
            ("m", "true m", True),
            ("true_e_level", "true shifted level", True),
            ("true_e_win", "|true smooth shifted E|", False),
            ("true_e_osc", "|true arithmetic Eosc|", False),
            ("true_source_cancel", "true source cancellation", True),
            ("true_osc_amp_car", "true osc carrier weight A", True),
            ("true_osc_overlap_car", "true osc carrier overlap O", True),
            ("true_osc_cancel_car", "true osc carrier cancel X", True),
            ("true_osc_signed_car", "|true osc carrier read|", True),
            ("true_total_amp", "true total weight A", True),
            ("true_total_overlap", "true total overlap O", True),
            ("true_total_cancel", "true total cancellation X", True)):
        slopes[key] = law(rows, key, label, positive=pos)
    add_dev = abs(slopes["true_osc_signed_car"][0]
                  - slopes["true_osc_amp_car"][0]
                  - slopes["true_osc_overlap_car"][0]
                  - slopes["true_osc_cancel_car"][0])
    check("L1 exact log-slope decomposition signed = A+O+X "
          "(dev %.2e)" % add_dev, add_dev <= 1e-8, kill="K3")
    p_osc = slopes["true_e_osc"][0]
    comps = {"READS(weight)": slopes["true_osc_amp_car"][0],
             "OVERLAP": slopes["true_osc_overlap_car"][0],
             "CROSSCHANNEL": slopes["true_osc_cancel_car"][0]}
    if TARGET_SLOPE[0] <= p_osc <= TARGET_SLOPE[1]:
        seat_name = min(comps, key=comps.get)
        if seat_name == "OVERLAP":
            seat = "DECAY-IN-OVERLAP"
        elif seat_name.startswith("READS"):
            seat = "DECAY-IN-READS"
        else:
            seat = "DECAY-CROSSCHANNEL"
    else:
        seat = "NO-READ-DECAY"
    p_level = slopes["true_e_level"][0]
    p_source = slopes["true_source_cancel"][0]
    if (TARGET_SLOPE[0] <= p_level <= TARGET_SLOPE[1]
            and TARGET_SLOPE[0] <= p_source <= TARGET_SLOPE[1]):
        level_seat = "LEVEL-DECAY-IN-SOURCE-CANCELLATION"
    elif TARGET_SLOPE[0] <= p_level <= TARGET_SLOPE[1]:
        level_comps = {
            "WEIGHT": slopes["true_total_amp"][0],
            "OVERLAP": slopes["true_total_overlap"][0],
            "CROSSCHANNEL": slopes["true_total_cancel"][0]}
        level_seat = "LEVEL-DECAY-IN-%s" % min(level_comps,
                                               key=level_comps.get)
    else:
        level_seat = "LEVEL-NO-H2-LAW"
    print("    DECAY-SEAT = %s; E_osc exponent %+.3f; components %s"
          % (seat, p_osc, ", ".join("%s %+.3f" % x
                                    for x in comps.items())))
    print("    LEVEL-SEAT = %s; Elevel exponent %+.3f; source-cancel "
          "exponent %+.3f" % (level_seat, p_level, p_source))
    print("    source cancellation |Elevel|/(|Ewin|+|Eosc|) %s"
          % bfmt([r["true_source_cancel"] for r in rows]))
    print("    carrier count min/med/max %s; carrier share of Eosc %s"
          % (str(band([r["carrier_count"] for r in rows])),
             bfmt([r["true_carrier_share"] for r in rows])))
    print("    source-vector cosine(win,osc) %s (minus one = antiparallel)"
          % bfmt([r["true_source_cos"] for r in rows]))
    print("    SMOOTH-PROXY laws (certificate direction; deep overlap may die):")
    sm_slopes = {}
    for key, label, pos in (
            ("e_level", "proxy shifted level", True),
            ("e_osc", "|proxy arithmetic Eosc|", False),
            ("osc_overlap_car", "proxy carrier overlap O", True),
            ("source_cancel", "proxy source cancellation", True)):
        sm_slopes[key] = law(rows, key, label, positive=pos)
    for seg in ("surface", "deep"):
        segrows = [r for r in rows if r["segment"] == seg]
        if len(segrows) >= 4:
            print("    %s-only cross-check (%d rungs):" % (seg, len(segrows)))
            law(segrows, "true_e_level", "true shifted level", positive=True)
            law(segrows, "true_e_osc", "|true arithmetic Eosc|",
                positive=False)
            law(segrows, "true_source_cancel", "true source cancellation",
                positive=True)
            law(segrows, "true_osc_overlap_car", "true carrier overlap O",
                positive=True)

    C, top, cstab, cdiag, cneg, cpos, sstab = cancellation_matrix(rows)
    print("    21-bin cancellation matrix: diag %.3e, negative offdiag "
          "mass %.3e, positive offdiag mass %.3e, median Frobenius "
          "instability %.3e" % (cdiag, cneg, cpos, cstab))
    print("    top bins (omega intervals) + sign stability: %s"
          % ", ".join("%d:[%.2f,%.2f]/%.2f"
                     % (j, j * OMEGA_C / N_BIN,
                        (j + 1) * OMEGA_C / N_BIN, s)
                     for j, s in zip(top, sstab)))
    print("    top-six median normalized pair-product matrix:")
    for i in top:
        print("      " + " ".join("%+8.2e" % C[i, j] for j in top))

    section("P -- provability class and smooth-model ward")
    smooth_reproduces_shape = min(r["profile_overlap"] for r in rows) >= 0.80
    if seat == "DECAY-IN-OVERLAP" and smooth_reproduces_shape:
        prov = "CLASSICAL-GEOMETRIC-CANDIDATE"
        print("    G1 needed: uniform asymptotic O_h for the smooth channel "
              "profile; G2 needed: source-only beta_h and residual-vector "
              "perturbation bound.")
    else:
        prov = "OPEN-ARITHMETIC-PHASE-CANCELLATION"
        print("    Fixed h: finite exact.  Pointwise all-h cancellation: "
              "not delivered by known average/mean-square prime results.")
        print("    Restricted x_sm(h) family: NOT proved RH-equivalent here.  "
              "Uniform all-direction upgrade: Weil positivity, "
              "RH-equivalent.")
    print("    PROVABILITY = %s; smooth geometry reproduces channel profile "
          "%s but smooth value fails on %d/%d"
          % (prov, "YES" if smooth_reproduces_shape else "NO",
             sum(r["lam_sm"] - 0.5 * r["mu1"] < 0 for r in rows),
             len(rows)))

    section("C -- mechanism-aware 75-rung certificate census")
    if SMOKE:
        cert_rows = rows
        print("    smoke census only (%d rungs); frozen 75-rung census deferred"
              % len(cert_rows))
    else:
        didx = np.unique(np.linspace(0, len(deep) - 1,
                                     N_CERT_DEEP).astype(int))
        cert_rows = surf + [deep[i] for i in didx]
    n_truth = sum(r["true_e_level"] >= -1e-12 for r in cert_rows)
    n_proxy_truth = sum(r["e_level"] >= -1e-12 for r in cert_rows)
    n_phase = sum(r["ray_lb"] > 0.0 for r in cert_rows)
    n_abs = sum(r["abs_lb"] > 0.0 for r in cert_rows)
    n_kt = sum(np.isfinite(r["kt_oracle"])
               and r["kt_oracle"] > 0.5 * r["mu1"] for r in cert_rows)
    ns = sum(r["segment"] == "surface" and r["ray_lb"] > 0
             for r in cert_rows)
    nd = sum(r["segment"] == "deep" and r["ray_lb"] > 0
             for r in cert_rows)
    print("    measured true-direction halfgap           %d/%d"
          % (n_truth, len(cert_rows)))
    print("    smooth-proxy ray halfgap                  %d/%d"
          % (n_proxy_truth, len(cert_rows)))
    print("    phase-blind channel triangle ray bound   %d/%d"
          % (n_abs, len(cert_rows)))
    print("    verified-zero signed ray bound            %d/%d "
          "(surface %d, deep %d)" % (n_phase, len(cert_rows), ns, nd))
    print("    Kato-Temple with MEASURED lambda2 ORACLE %d/%d "
          "(diagnostic, forbidden in certificate)" % (n_kt, len(cert_rows)))
    print("    full non-circular wall certificate        0/%d "
          "(source-only beta_h + vector residual supply missing)"
          % len(cert_rows))
    print("    cited isotropic/absolute wall baseline     0/67 (CCI)")
    print("    TAILB/mu1 %s; ray lower-margin/mu1 on closers %s"
          % (bfmt([r["tailb"] / r["mu1"] for r in cert_rows]),
             bfmt([r["ray_lb"] / r["mu1"] for r in cert_rows
                   if r["ray_lb"] > 0]) if n_phase else "none"))
    law(cert_rows, "tailb", "verified-zero tail price", positive=True)

    section("T -- tau screens")
    tau1 = tau_screen(rows, [r["true_e_level"] / r["mu1"] for r in rows],
                      "true Elevel/mu1")
    tau2 = tau_screen(
        rows, [r["true_source_cancel"] / r["mu1"] for r in rows],
        "true source-cancel/mu1")
    tau3 = tau_screen(rows, [r["true_osc_overlap_car"] for r in rows],
                      "true carrier overlap O")

    section("K -- controls MUST FIRE")
    surf_rows = [r for r in rows if r["segment"] == "surface"]
    ctl = controls(rows, surf_rows)
    check("K1 smooth has zero oscillatory read and fails level %d/%d"
          % (ctl["smooth_fail"], len(rows)),
          ctl["smooth_fail"] == len(rows), kill="K2")
    check("K2 scramble fires: kz9 shifted wall/ray %.3e/%.3e; "
          "wall/ray/seat fail %d/%d, %d/%d, %d/%d; "
          "ray abs-law h^%+.3f +- %.3f"
          % (ctl["scramble_wall_kz9"], ctl["scramble_kz9"],
             ctl["scramble_wall_fail"], len(surf_rows),
             ctl["scramble_ray_fail"], len(surf_rows),
             ctl["scramble_det_fail"], len(surf_rows),
             ctl["scramble_slope"], 2 * ctl["scramble_se"]),
          ctl["scramble_wall_kz9"] < 0.0 or ctl["scramble_det_fail"] >= 1,
          kill="K2")
    check("K3 Epstein fires at kz9: shifted wall/ray %.3e/%.3e, "
          "seat det %.3e (positive ray locates death outside x_sm)"
          % (ctl["epstein_wall"], ctl["epstein_ray"],
             ctl["epstein_det"]),
          ctl["epstein_wall"] < 0.0 or ctl["epstein_det"] < 0.0,
          kill="K2")
    check("K4 cosh fires on wall/seat %d/%d, %d/%d surface rungs "
          "(smooth ray sees %d/%d: death seat reported)"
          % (ctl["cosh_wall_fail"], len(surf_rows),
             ctl["cosh_det_fail"], len(surf_rows),
             ctl["cosh_ray_fail"], len(surf_rows)),
          ctl["cosh_wall_fail"] >= 1 or ctl["cosh_det_fail"] >= 1,
          kill="K2")
    check("K5 anti-circularity: every bound uses x_sm only; x_true, "
          "lambda2 and Kato-Temple are diagnostics", True)

    if SMOKE:
        check("F full 67+28 and 75-rung census deferred in disclosed smoke",
              True)
    else:
        check("F frozen census sizes 95 read laws and 75 certificate rungs",
              len(rows) == 95 and len(cert_rows) == 75, kill="K1")

    labels = [
        "READ-LAW(Eosc h^%+.3f; level h^%+.3f)" %
        (slopes["true_e_osc"][0], slopes["true_e_level"][0]),
        seat,
        level_seat,
        prov,
        "PHASE-RAY-CLOSES(%d/%d; absolute %d/%d; wall 0/%d)" %
        (n_phase, len(cert_rows), n_abs, len(cert_rows), len(cert_rows)),
        "TAU(%s/%s/%s)" % (tau1[0], tau2[0], tau3[0]),
        "CONTROLS-FIRE"
    ]
    return finish(labels)


if __name__ == "__main__":
    sys.exit(main())
