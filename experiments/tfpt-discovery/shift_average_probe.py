#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""shift_average_probe -- PRIME.COFINAL.SHIFT.AVERAGE.01: the
grid-phase averaging route (EXPLORATION ONLY, experiments/, NO RH
CLAIM, 2026-08-13).

THE ROUTE.  The formal extraction chain (H_cof, CCCIX / CofinalWeil)
needs only a PREDEFINED cofinal sequence of positive windows -- not
positivity for every grid.  The deployed wall grid has a natural
third parameter: the offset theta in [0,1).  Cells at (k+theta)D give
a one-parameter family of equally faithful discretizations
M_{a,D,theta} with Schur margin s(a,D,theta).  If the AVERAGE
int_0^1 s dtheta > 0 (with B(theta) PD for all theta), then at least
one offset gives a positive window, and the smallest dyadic offset
with a positive certificate is a deterministic choice.

THE FAMILY (this probe's frozen definition, derived from the
instrument of record).  The deployed arbiter wall (PATH-3, CCCXXIII/
CCCXXIX verbatim) is Omega[m,m'] = (G_{m+m'} + G_{|m-m'|})/2 with
G_r = c_r - (c_{r+1} + c_{|r-1|})/2 and c_r the lag profile: the
continuous even function c(x) = arch_A(xD, D)
- (1/2) sum_n mu_n [tau_D(xD - u_n) + tau_D(xD + u_n)] sampled at
integer x (tent reads of the prime comb + the archimedean Weil
kernel paired with one tent; mu_n = 2 Lambda(n)/sqrt(n),
u_n = log n <= 2 alpha).  Moving the cells to (k+theta)D leaves all
pairwise DIFFERENCES of cell positions unchanged and shifts all
reflected-pair distances by 2 theta.  The family is therefore

    Omega_theta[m,m'] = (G(m+m'+2 theta) + G(|m-m'|)) / 2,

with G(x) = c(x) - (c(x+1) + c(|x-1|))/2 read at CONTINUOUS
positions.  theta = 0 is the deployed wall bit for bit; theta = 1
gives Omega_1[m,m'] = Omega_0[m+1,m'+1] (the same family with cells
relabelled by one) -- the STRUCTURAL faithfulness identity.  The
Schur scalar is s(theta) = n - b^T B^{-1} b at the (0,0) pivot of
Omega_theta (n = Omega[0,0], b = Omega[1:,0], B = Omega[1:,1:]).
ANTI-CIRCULARITY: the family is pure grid geometry + prime comb +
archimedean kernel; no tau, no zero data, no eigensolver anywhere in
this file (AST-warded); signs are decided by Cholesky certificates
only.

THE RIGOR DEVICE (the CCCXXIII lesson).  On every theta-interval on
which all entries are AFFINE in theta (the atom tent reads are
piecewise linear; breakpoints are frac(u_n/(2D)) and
frac(u_n/(2D) + 1/2) per atom, plus theta = 1/2 for the
archimedean |x-1| fold), the Schur scalar
s(theta) = min_{v_0 = 1} v^T Omega_theta v is a minimum of affine
functions of theta, hence CONCAVE, and Hermite-Hadamard gives
rigorous two-sided bounds per piece:
(s(a)+s(b))/2 <= piece mean <= s(midpoint) -- NO Lipschitz constant,
NO eigensolver.  Summing pieces gives a certified enclosure of
int_0^1 s dtheta (TIER 2), modulo three DECLARED and printed slacks:
(i) the certified per-evaluation enclosure of s (approximate
Cholesky solve + residual + certified floor lambda_min(B) >= c_lo
via shifted Cholesky with a Higham-type rounding certificate;
r^T B^{-1} r in [0, |r|^2/c_lo]), (ii) the float64 entry envelope,
measured by 40-digit mpmath spot re-assembly of c(x) from source
(independent quadrature of the same archimedean integrand + exact
mp logs) times a safety factor, entering as
2 h eps V^2_unif, and (iii) the archimedean curvature model (the
arch part of an entry is smooth, not affine, on a piece; the
deviation from its chord is <= len^2/8 max|d^2 entry/dtheta^2|,
with max|G_arch''| measured by finite differences times a safety
factor -- O(len^2), negligible and printed).  The lambda_min(B)
floor is extended from piece endpoints to the whole piece by
CONCAVITY of lambda_min over affine families.  TIER 2 runs on every
picked cell whose projected cost (2.2 x pieces x measured
per-evaluation time) fits the frozen budget; deeper cells get
TIER 1: the same certified per-sample enclosures on a frozen
midpoint theta-grid (mean typed MEASURED -- quadrature modulus not
closed) PLUS the rigorous KILL-SIDE test via Jensen: the Schur
complement is concave in the matrix, so
int_0^1 s(Omega_theta) dtheta <= s(Omega_bar) with Omega_bar the
EXACTLY theta-averaged wall (atom part integrated in closed form
piecewise; arch part by warded Gauss-Legendre) -- a certified
s(Omega_bar) < 0 kills the route at that depth.

FROZEN PROTOCOL.
 S0 freeze + AST firewall (no zetazero/nzeros/eigh/eigvalsh/eig/
    eigvals/eigs/eigsh calls; RNG only with the declared literal
    seed).
 T  independent sieve to TAB = 1.6e7, BITWISE ward against the
    deployed core.LAM_TAB prefix (4e5); the deep-frame census
    (deployed formula verbatim, NU = 4); cell picks: for each target
    h in {184, 405, 838, 1393, 2854} the census cell with nearest h
    (tie -> smaller kz).
 W  W1 theta = 0 reproduces the deployed lag profile and G sequence
    at every picked cell (arch generator shared, atom reads
    independent; rel <= 1e-9); W2 the shift identity
    Omega_1[m,m'] == Omega_0[m+1,m'+1] numerically at the smallest
    cell (structural, must be exact to roundoff); W3 identity (B):
    int_0^1 sum_k tau_{D,theta,k}(u) tau_{D,theta,k}(v) dtheta =
    (1/D)(tau_D * tau_D)(u-v), verified EXACTLY in Fraction
    arithmetic on rational tuples (piecewise Simpson, exact for the
    piecewise-quadratic integrand) and to >= 40 digits in mpmath on
    irrational tuples (u, v = logs of primes).
 A  TIER 1 per cell: certified s(theta) on the frozen midpoint grid
    (N by target: 256/256/128/64/32) + theta = 0 + the dyadic ladder
    (denominators 2..2^5, deep cells 2^3); PD census of B(theta),
    with EVERY refusal diagnosed by float LDL block inertia (n_neg,
    min pivot) -- a refusal with n_neg = 0 would be a certificate
    artifact and fails the instrument check A1; genuine
    indefiniteness is a MEASUREMENT (the premise of the route
    breaks at that offset), reported, and the mean becomes
    CONDITIONAL on the PD subset; smallest dyadic offset with
    certified positive s (the H_cof choice rule, typed: the RULE is
    frozen here before any measurement).  Atom truncation: the comb
    is capped at u <= 2 alpha + D (the SUPPORT of the family: the
    topmost reflected reads touch (2 alpha, 2 alpha + D] for
    theta > 1/2; at theta = 0 the extra atoms are never read, so
    the deployed ward W1 is unaffected).
 J  the exact theta-averaged wall Omega_bar per cell; certified
    s(Omega_bar); Jensen kill test (concavity of the Schur
    complement in the matrix: E-cited, Horn & Johnson 2nd ed.
    Sec. 7.7 + Boyd-Vandenberghe Ex. 3.58; warded numerically:
    measured mean <= s(Omega_bar) + tolerance).
 H  TIER 2 (piece-exact Hermite-Hadamard) on every cell within the
    frozen cost guard (per cell 420 s projected, 700 s total,
    measured per-evaluation time from A -- machine-dependent, typed
    honestly): certified two-sided enclosure of int_0^1 s dtheta;
    per-piece concavity ward (midpoint >= chord within enclosures);
    cross-ward against the TIER-1 grid mean.
 C  the decomposition attempt (identity (C)) at the smallest cell:
    P_bar = int_0^1 b(theta) b(theta)^T dtheta EXACTLY (piecewise
    Simpson on the union breakpoints; exact for the
    piecewise-quadratic products; arch model slack typed), split
    arch x arch / cross / comb x comb; the comb x comb block is a
    second moment, hence PSD (warded by shifted Cholesky); with
    B0 = the co-block of Omega_bar the mean decomposes as
    mean s = n_bar - tr(B0^{-1} P_bar) - delta_B,
    delta_B := q_bar - tr(B0^{-1} P_bar) the measured B-variation
    remainder; the PSD comb energy E+ = tr(B0^{-1} P_bar_cc) >= 0
    and its SIGN OF ENTRY into the mean is the decisive structural
    read (the mission's target (C) wants a positive energy CARRYING
    the mean; on a wall LINEAR in the comb the quadratic comb energy
    can only enter through -b^T B^{-1} b, i.e. with sign -E+ --
    measured and typed either way; compare CCCXXXI amendment A1).
 X  controls, identical pipeline, frozen: SCRAMBLE (atom positions
    uniform on (0, 2 alpha), masses preserved, seed 20260813) and
    EPSTEIN (Lambda_E of the x^2+5y^2 Epstein zeta by Dirichlet
    division from exact lattice counts, epstein_firewall_probe
    read-only, cap min(X, 1e5)) at the target-184 and target-838
    cells, N = 32; report their theta-averages / PD failures.
 V  verdict (frozen enum + precedence ILLDEFINED > DEAD > MIXED >
    POSITIVE):
    SHIFTAVG-ILLDEFINED  iff a faithfulness ward (W1/W2/W3) fails --
                         the family fails to BE the deployed
                         architecture or the averaging identity is
                         wrong;
    SHIFTAVG-DEAD        iff a certified enclosure (TIER 2 upper
                         bound, or Jensen s(Omega_bar) upper bound
                         incl. the entry envelope) puts
                         int_0^1 s dtheta < 0 on a genuine FULL-PD
                         cell whose wards are green (THE FROZEN
                         KILL; on a premise-broken cell the mean of
                         s is not the defined object and the kill
                         cannot bind);
    SHIFTAVG-MIXED       iff some cell has a PD-premise failure at
                         some theta (B(theta) genuinely indefinite,
                         LDL-diagnosed -- cells + failure measure +
                         n_neg listed) or a nonpositive
                         (conditional) mean;
    SHIFTAVG-POSITIVE    iff all five cells are full-PD with
                         positive means (certified where TIER 2
                         ran, measured elsewhere -- tier typed per
                         cell); margins printed.
    A positive read is "no witness found" -- positivity of the
    route is NOT certified by this probe; NO all-h statement; the
    dyadic choice rule is reported as the H_cof instantiation
    CANDIDATE only (the CCCXXXVII Q-3 tension -- certificate-
    conditioned selection -- is typed in the log).

EXTERNAL-CITED (consumed, warded, never proved here):
 E1 Schur/Sylvester: M = [[n, b^T],[b, B]] symmetric with B PD is PD
    iff s = n - b^T B^{-1} b > 0.  [Horn & Johnson, Matrix Analysis,
    2nd ed., Sec. 7.2.]
 E2 Concavity: the Schur complement s(M) is concave on PD matrices,
    and lambda_min is concave; both are infima of linear functionals
    (min_{v_0=1} v^T M v resp. min_{|v|=1} v^T M v).  [Horn &
    Johnson op. cit.; Boyd & Vandenberghe, Convex Optimization,
    Ex. 3.58.]
 E3 Rounding certificates: a successful floating Cholesky of
    B - beta I certifies lambda_min(B) >= beta - slack with the
    Higham-type slack used verbatim from the deployed pattern
    (comb_window_verification_probe.chol_cert_lower).  [Higham, ASNA
    2nd ed., Ch. 10; Rump, Acta Numerica 19 (2010).]

FIREWALL: verification/v563 + epstein_firewall_probe READ-ONLY
(deployed generators only, never cached assemblies -- every wall
here is assembled from source in THIS file); no zeta-zero data
anywhere; RNG only in the declared scramble control.
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import scipy.linalg as sla

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (os.path.join(_here, "..", "..", "verification"), _here):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break
sys.path.insert(0, _here)

import mpmath as mp                              # noqa: E402
import v563_paper2_readouts as core              # noqa: E402 (READ-ONLY)
import epstein_firewall_probe as epx             # noqa: E402 (READ-ONLY)

T0 = time.time()
FAILS = []
KILLS = []
N_CHK = 0
SMOKE = os.environ.get("TFPT_SMOKE", "") == "1"

# ------------------------------------------------------------ frozen spec
FROZEN_SPEC = """\
shift_average_probe spec v4 (2026-08-13, frozen before the run of
record; v1 -> v2 -> v3 -> v4 after five disclosed smokes plus one
disclosed full pre-freeze run: (v2) atom cap widened to the family
support, refusal diagnosis by LDL inertia, conditional-on-PD means,
GL 48/96, verdict semantics ILLDEFINED = wards only; (v3) cap
corrected to 2 alpha + 2D, TIER2 slacks made per-piece with the
antidiagonal transfer model and forced subdivision L_SUB = 2048,
CERT tier claimed only when the certified lower bound is positive,
concavity-ward firings repaired into the enclosure x4; (v4, after
the pre-freeze full run showed ALL deep evaluations refusing with
LDL n_neg = 0 and healthy pivots, i.e. certificate artifacts, not
indefiniteness: inverse-iteration hint 12 iterations, 14 beta
quarterings, certificate-refused-but-factorized evaluations keep
the plain float64 s as an UNCERTIFIED tier, refusals split
GENUINE-INDEFINITE (n_neg >= 1, premise broken) vs
RESOLUTION-LIMITED (n_neg = 0, B-floor below the float64 Higham
slack -- measured lambda_min(B) ~ 4e-12 at h 2854 vs slack ~ 8e-12,
typed); no gate loosened).  Family:
Omega_theta[m,m'] = (G(m+m'+2theta)+G(|m-m'|))/2, G(x) = c(x) -
(c(x+1)+c(|x-1|))/2, c(x) = arch_A(xD,D) - tent reads of the prime
comb (atoms n <= e^{2 alpha + 2D}, masses 2 Lambda(n)/sqrt(n), even
reflection), deployed arbiter wall at theta=0.  Schur scalar
s = n - b^T B^-1 b at pivot (0,0).  TAB = 16000000; NU = 4; targets
h = 184/405/838/1393/2854, pick = nearest census h, tie -> smaller
kz.  TIER1 midpoint grids N = 256/256/128/64/32 by target + theta=0
+ dyadics den 2..32 (deep targets 1393/2854: den 2..8); every PD
refusal LDL-diagnosed (n_neg >= 1 required, else instrument FAIL).
TIER2 Hermite-Hadamard on exact affine pieces (breakpoints
frac(u/(2D)), frac(u/(2D)+1/2) per atom + {0, 1/2, 1}, subdivided
to max length 1/2048), cost guard 420 s/cell + 700 s total
projected from measured TIER1 eval time; PD-refused pieces excluded
-> enclosure typed CONDITIONAL with the excluded measure.
Enclosures: shifted-Cholesky Higham floor (BETA_FRAC 0.5, <= 8
quarterings), q-bracket r^T B^-1 r in [0,|r|^2/c_lo], gamma_n dot
envelopes; per-piece slacks with the declared measured-vhat model
(vhat = (1,-y) of the piece evals, transfer factor 2, warded by the
concavity ward): arch curvature (len^2/4) sum_r S2[r] conv_r(|vhat|)
with S2 = 8 x FD-measured |G_arch''| profile (step 1e-3, three
off-kink offsets; conv = FFT autocorrelation of |vhat|), entry
envelope 2 eps ||vhat||_1^2 with eps = 8 x max mpmath-40dps spot
deviation (6 spots/cell).  Jensen kill test
on the exact averaged wall (atom part closed-form, arch part GL-48
per unit interval, warded vs GL-96), binding only on full-PD cells.
Identity (B): exact Fraction Simpson on 7 rational tuples + mpmath
dps 60 on 2 irrational tuples, bar 1e-40 abs.  Decomposition (C) at
target 184: P_bar exact piecewise Simpson, split aa/cross/cc, PSD
ward on cc, B0 = co-block of Omega_bar, delta_B = q_bar,cond -
tr(B0^-1 P_bar) (absorbs the B(theta) variation AND any PD-subset
mismatch, typed).  Controls at targets 184/838, N = 32: scramble
seed 20260813 (positions uniform (0,2alpha), masses kept), Epstein
Lambda_E cap min(X,1e5) via epstein_firewall_probe.  Verdict:
ILLDEFINED (wards) > DEAD (certified mean < 0 on a full-PD genuine
cell) > MIXED (premise broken somewhere or nonpositive conditional
mean) > POSITIVE (tier per cell: CERT-POS only when the certified
lower bound is > 0, else MEAS).  No eigensolvers, no zero data, no
tau; RNG only seed 20260813.  NO RH CLAIM."""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()

TAB = 16000000
NU = 4
TARGETS = (184, 405, 838, 1393, 2854)
N_THETA = {184: 256, 405: 256, 838: 128, 1393: 64, 2854: 32}
DY_TMAX = {184: 5, 405: 5, 838: 5, 1393: 3, 2854: 3}
TIER2_CAP_S = 420.0
TIER2_TOTAL_S = 700.0
L_SUB = 2048
MODEL_FAC = 2.0
VIOL_FAC = 4.0
VIOL_CAP = 8
BETA_FRAC = 0.5
BETA_TRIES = 14
LAM_ITERS = 12
ENV_SAFE = 8.0
FD_STEP = 1.0e-3
WARD_DEP_REL = 1.0e-9
WARD_SHIFT_REL = 1.0e-12
IDB_BAR = mp.mpf("1e-40")
MP_DPS = 60
SPOT_DPS = 40
N_SPOTS = 6
GL_UNIT = 48
GL_UNIT_REF = 96
CTRL_TARGETS = (184, 838)
CTRL_N = 32
SEED_SCR = 20260813
EP_CAP = 100000
JENSEN_TOL_REL = 1.0e-6
U_RND = 0.5 * np.finfo(float).eps
CERT_INFL = 1.01

if SMOKE:
    N_THETA = {k: max(8, v // 8) for k, v in N_THETA.items()}
    CTRL_N = 8

_GLX24, _GLW24 = np.polynomial.legendre.leggauss(GL_UNIT)
_GLX48, _GLW48 = np.polynomial.legendre.leggauss(GL_UNIT_REF)


def check(name, ok, detail="", kill=None):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
        if kill:
            KILLS.append(kill)
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def section(title):
    print("\n" + "-" * 78)
    print(title)
    print("-" * 78)


def gamma_n(k):
    t = k * U_RND * 2.0
    return t / (1.0 - t)


def ast_firewall():
    banned = {"zetazero", "zetazeros", "nzeros", "find_zeros",
              "eigh", "eigvalsh", "eig", "eigvals", "eigs", "eigsh"}
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits, rng_bad = [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f = node.func
            nm = f.attr if isinstance(f, ast.Attribute) else (
                f.id if isinstance(f, ast.Name) else "")
            if nm in banned:
                hits.append(nm)
            if nm == "default_rng":
                for a in node.args:
                    if not isinstance(a, (ast.Constant, ast.Name)):
                        rng_bad.append(ast.dump(a))
    return hits, rng_bad


# ================================================================ tables
DEEP = {}


def build_tables():
    lam = core.von_mangoldt_table(TAB)
    nn = np.nonzero(lam > 0.0)[0]
    DEEP["NN"] = nn
    DEEP["U"] = np.log(nn.astype(float))
    DEEP["MU"] = 2.0 * lam[nn] / np.sqrt(nn.astype(float))
    DEEP["G"] = np.diff(DEEP["U"])
    pref = core.ATOM_MAX
    ok = bool(np.array_equal(lam[:pref + 1], core.LAM_TAB))
    del lam
    return ok


def census():
    u, g = DEEP["U"], DEEP["G"]
    out = []
    for kz in range(2, len(u) - 1):
        alpha = float(u[kz])
        dk = 0.5 * float(g[kz]) / float(NU)
        if dk <= 0.0:
            continue
        mz = int(math.ceil(alpha / dk - 1.0e-9)) + 1
        if mz % 2:
            mz += 1
        x_val = math.exp(2.0 * alpha)
        if x_val <= TAB:
            out.append(dict(h=mz // 2, kz=kz, alpha=alpha, M=mz,
                            X=x_val))
    out.sort(key=lambda c: (c["h"], c["kz"]))
    return out


def pick_cells(cen):
    picks = {}
    for tgt in TARGETS:
        best = min(cen, key=lambda c: (abs(c["h"] - tgt), c["kz"]))
        picks[tgt] = best
    return picks


def cell_atoms(cell, world=None, seed=None):
    """The cell's comb from source.  Cap u <= 2 alpha + 2D: the
    offset family's topmost reflected reads touch
    (2 alpha, 2 alpha + 2 theta D] for theta > 1/2 (max read
    position x = 2h-1+2theta, tent support < (2h+2theta)D), so the
    FAITHFUL truncation is the support of the family, not the
    deployed 2 alpha (at theta = 0 the extra atoms are never read --
    W1 stays bit-compatible; typed.  Smoke 1 measured exactly this:
    with the deployed cap the co-block B(theta) read FALSE
    indefiniteness at fractional offsets -- a truncation artifact,
    not physics)."""
    alpha = cell["alpha"]
    d_cell = 2.0 * alpha / cell["M"]
    ka = int(np.searchsorted(DEEP["U"],
                             2.0 * alpha + 2.0 * d_cell + 1.0e-14,
                             side="right"))
    uu = DEEP["U"][:ka].copy()
    mm = DEEP["MU"][:ka].copy()
    if world == "scramble":
        rng = np.random.default_rng(seed)
        uu = np.sort(rng.uniform(0.0, 2.0 * alpha, size=ka))
    elif world == "epstein":
        cap = int(min(cell["X"], EP_CAP))
        r1 = np.asarray(epx.lattice_r1(cap), float)
        lam_e = epx.dirichlet_vonmangoldt(r1 / 2.0, cap)
        supp = np.nonzero(np.abs(lam_e) > 1.0e-9)[0]
        supp = supp[supp >= 2]
        uu = np.log(supp.astype(float))
        mm = 2.0 * lam_e[supp] / np.sqrt(supp.astype(float))
    return uu, mm


# ==================================================== continuous readers
class Wall:
    """Assembles c(x), G, Omega_theta for one cell + one comb, from
    source, independently of any cached assembly."""

    def __init__(self, cell, uu, mm):
        self.h = cell["M"] // 2
        self.D = 2.0 * cell["alpha"] / cell["M"]
        self.alpha = cell["alpha"]
        self.uu = np.asarray(uu, float)
        self.mm = np.asarray(mm, float)
        self.uh = self.uu / self.D            # atom positions, grid units
        self.n_atom = int(len(uu))
        h = self.h
        # Toeplitz part (theta-free): c at integers -1..h+1
        ci = self.c_scalar_vec(np.arange(-1.0, h + 2.0))
        self.G_t = ci[1:h + 1] - 0.5 * (ci[2:h + 2] + ci[0:h])
        self.ci_full = None                   # integer c cache (wards)

    # ---- atom tent reads at a unit-spaced ladder x_r = r + shift
    def _atom_ladder(self, shift, nread):
        """c_at at x = (r + shift), r = 0..nread-1, x >= 0 assumed."""
        out = np.zeros(nread)
        t = self.uh - shift
        r0 = np.floor(t).astype(np.int64)
        fr = t - r0
        for off, wgt in ((0, 1.0 - fr), (1, fr)):
            idx = r0 + off
            ok = (idx >= 0) & (idx < nread) & (wgt > 0.0)
            if ok.any():
                np.subtract.at(out, idx[ok], self.mm[ok] * 0.5 * wgt[ok])
        # even reflection (deployed): atoms with u < D add tents at -u
        refl = self.uh < 1.0
        if refl.any():
            for j in np.nonzero(refl)[0]:
                v = 1.0 - (shift + self.uh[j])
                r = 0
                while v > 0.0 and r < nread:
                    out[r] -= self.mm[j] * 0.5 * v
                    r += 1
                    v = 1.0 - (r + shift + self.uh[j])
        return out

    def _atom_scalar(self, x):
        """c_at at one arbitrary position x >= 0 (grid units)."""
        lo = np.searchsorted(self.uh, x - 1.0)
        hi = np.searchsorted(self.uh, x + 1.0)
        v = 1.0 - np.abs(x - self.uh[lo:hi])
        s = -0.5 * float(np.dot(self.mm[lo:hi], np.maximum(v, 0.0)))
        refl = self.uh < 1.0 - x
        if refl.any():
            s -= 0.5 * float(np.dot(self.mm[refl],
                                    1.0 - (x + self.uh[refl])))
        return s

    def c_scalar_vec(self, xs):
        xs = np.abs(np.asarray(xs, float))
        c_ar = core.arch_A(xs * self.D, self.D)
        c_at = np.array([self._atom_scalar(float(x)) for x in xs])
        return c_ar + c_at

    def c_ladder(self, theta, split=False):
        """c at x = (r + 2 theta), r = -1..2h-1 (length 2h+1).
        Negative x uses evenness; split returns (arch, atom)."""
        h = self.h
        nn = 2 * h + 1
        xs = np.arange(-1.0, 2.0 * h) + 2.0 * theta
        axs = np.abs(xs)
        c_ar = core.arch_A(axs * self.D, self.D)
        c_at = self._atom_ladder(2.0 * theta - 1.0, nn)
        neg = xs < 0.0
        for i in np.nonzero(neg)[0]:
            c_at[i] = self._atom_scalar(float(axs[i]))
        return (c_ar, c_at) if split else c_ar + c_at

    def G_hankel(self, theta, split=False):
        """G(r + 2 theta) for r = 0..2h-2."""
        if split:
            car, cat = self.c_ladder(theta, split=True)
            ga = car[1:-1] - 0.5 * (car[2:] + car[:-2])
            gc = cat[1:-1] - 0.5 * (cat[2:] + cat[:-2])
            return ga, gc
        cl = self.c_ladder(theta)
        return cl[1:-1] - 0.5 * (cl[2:] + cl[:-2])

    def omega(self, theta):
        h = self.h
        gh = self.G_hankel(theta)
        H = sla.hankel(gh[:h], gh[h - 1:2 * h - 1])
        T = sla.toeplitz(self.G_t[:h])
        return 0.5 * (H + T)

    def omega_from_gh(self, gh):
        h = self.h
        H = sla.hankel(gh[:h], gh[h - 1:2 * h - 1])
        T = sla.toeplitz(self.G_t[:h])
        return 0.5 * (H + T)

    # ---- exact atom-part unit integrals F(r) = int_r^{r+1} c_at dx
    def atom_unit_integrals(self, r_lo, r_hi):
        """F[j] = int_{r_lo+j}^{r_lo+j+1} c_at(x) dx, exact closed
        form (x >= 0 range assumed; reflection handled for u < D)."""
        nun = r_hi - r_lo
        F = np.zeros(nun)

        def i_tau(t):
            t = np.asarray(t, float)
            out = np.where(t <= -1.0, 0.0,
                           np.where(t <= 0.0, 0.5 * (t + 1.0) ** 2,
                                    np.where(t <= 1.0,
                                             1.0 - 0.5 * (1.0 - t) ** 2,
                                             1.0)))
            return out

        # each atom contributes int tau(x - uh) over unit intervals
        t0 = self.uh - r_lo
        j_lo = np.maximum(np.floor(t0 - 1.0).astype(np.int64), 0)
        for off in range(0, 4):
            j = j_lo + off
            ok = j < nun
            if not ok.any():
                continue
            a = j[ok] - t0[ok]
            contrib = i_tau(a + 1.0) - i_tau(a)
            np.subtract.at(F, j[ok], self.mm[ok] * 0.5 * contrib)
        refl = self.uh < 1.0
        if refl.any() and r_lo <= 0:
            for jj in np.nonzero(refl)[0]:
                # int max(0, 1 - (x + u)) dx over [k, k+1], x >= 0
                for k in range(0, 2):
                    col = k - r_lo
                    if not (0 <= col < nun):
                        continue
                    a, b = float(k), float(k + 1)
                    ub = min(b, 1.0 - self.uh[jj])
                    if ub > a:
                        val = (1.0 - self.uh[jj]) * (ub - a) \
                            - 0.5 * (ub * ub - a * a)
                        F[col] -= self.mm[jj] * 0.5 * val
        return F

    def arch_unit_integral(self, r, glx, glw):
        """int_r^{r+1} arch_A(xD, D) dx by GL (x may be negative:
        evenness is applied pointwise)."""
        mid, half = r + 0.5, 0.5
        xs = mid + half * glx
        vals = core.arch_A(np.abs(xs) * self.D, self.D)
        return half * float(np.dot(glw, vals))


# ======================================================= certified Schur
def ldl_inertia_of(B):
    """Float LDL block inertia (diagnosis of PD refusals; scipy.ldl
    is a factorization, not an eigensolver).  Returns (n_neg,
    min_1x1_pivot)."""
    try:
        _l, d, _p = sla.ldl(B, lower=True)
    except Exception as exc:                          # noqa: BLE001
        return -1, float("nan"), type(exc).__name__
    n = d.shape[0]
    n_neg = 0
    min_piv = float("inf")
    i = 0
    while i < n:
        if i + 1 < n and abs(d[i, i + 1]) > 0.0:
            a, bq, c = d[i, i], d[i, i + 1], d[i + 1, i + 1]
            det = a * c - bq * bq
            tr = a + c
            if det < 0.0:
                n_neg += 1
            elif det > 0.0 and tr < 0.0:
                n_neg += 2
            i += 2
        else:
            if d[i, i] < 0.0:
                n_neg += 1
            min_piv = min(min_piv, d[i, i])
            i += 1
    return n_neg, min_piv, None


def chol_cert_lower(B, lam_hat):
    """Certified lambda_min(B) >= returned value (or None), the
    deployed Higham pattern (comb_window_verification verbatim)."""
    M = B.shape[0]
    beta = BETA_FRAC * lam_hat
    for _ in range(BETA_TRIES):
        A = B.copy()
        A[np.diag_indices(M)] -= beta
        try:
            L = np.linalg.cholesky(A)
        except np.linalg.LinAlgError:
            beta *= 0.25
            continue
        aL = np.abs(L)
        w = float(np.max(aL @ aL.sum(axis=0))) * CERT_INFL
        slack = gamma_n(M + 1) * w
        e_diag = U_RND * float(np.max(np.abs(np.diag(A)))) \
            + U_RND * abs(beta)
        cert = beta - slack - e_diag
        if cert > 0.0:
            return cert
        beta *= 0.25
    return None


def lam_hint(B, cf):
    """Cheap lambda_min hint by inverse iteration on an existing
    Cholesky factor (solves only; the CERTIFICATE is the shifted
    Cholesky, never this hint)."""
    n = B.shape[0]
    v = np.ones(n) / math.sqrt(n)
    for _ in range(LAM_ITERS):
        v = sla.cho_solve(cf, v, check_finite=False)
        v /= float(np.linalg.norm(v))
    return float(v @ (B @ v))


def cert_schur(omega, floor_hint=None, want_y=False, diagnose=False):
    """Certified enclosure of s = n - b^T B^{-1} b.  Returns dict; on
    PD refusal returns a refusal dict (optionally with LDL inertia
    diagnosis) instead."""
    n0 = float(omega[0, 0])
    b = np.ascontiguousarray(omega[1:, 0])
    B = np.ascontiguousarray(omega[1:, 1:])
    hb = B.shape[0]

    def refusal(kind):
        out = dict(refused=kind)
        if diagnose:
            nneg, minp, err = ldl_inertia_of(B)
            out.update(n_neg=nneg, min_piv=minp, ldl_err=err)
        return out

    try:
        cf = sla.cho_factor(B, lower=True, check_finite=False)
    except np.linalg.LinAlgError:
        return refusal("CHOL-FAIL")
    y = sla.cho_solve(cf, b, check_finite=False)
    lam0 = floor_hint if floor_hint else lam_hint(B, cf)
    c_lo = chol_cert_lower(B, lam0)
    if c_lo is None and floor_hint:
        c_lo = chol_cert_lower(B, lam_hint(B, cf))
    if c_lo is None:
        # the B-floor is below the float64 Higham certification
        # resolution: refuse the CERTIFICATE but keep the plain
        # float64 measurement of s, typed UNCERTIFIED
        out = refusal("CERT-WEAK")
        out["uncert_s"] = n0 - float(math.fsum((b * y).tolist()))
        return out
    absB_absy = np.abs(B) @ np.abs(y)
    r = b - B @ y
    env_r = gamma_n(hb + 1) * (absB_absy + np.abs(b))
    t1 = math.fsum((b * y).tolist())
    t2 = math.fsum((r * y).tolist())
    e_dot = gamma_n(hb + 1) * (
        math.fsum(np.abs(b * y).tolist())
        + math.fsum(np.abs(r * y).tolist())) \
        + math.fsum((env_r * np.abs(y)).tolist())
    r_up = math.sqrt(math.fsum(((np.abs(r) + env_r) ** 2).tolist())) \
        * (1.0 + gamma_n(hb + 1))
    t3_hi = r_up * r_up / c_lo
    q_lo = t1 + t2 - e_dot
    q_hi = t1 + t2 + e_dot + t3_hi
    out = dict(n=n0, s_lo=n0 - q_hi, s_hi=n0 - q_lo,
               s=(2.0 * n0 - q_lo - q_hi) * 0.5,
               c_lo=c_lo, v2=1.0 + float(y @ y),
               bnorm=float(np.linalg.norm(b)))
    if want_y:
        out["y"] = y
    return out


# ================================================== identity (B) checks
def tau_frac(x, D):
    a = abs(x)
    return Fraction(0) if a >= D else 1 - Fraction(a, 1) / D


def bspline_frac(w, D):
    t = abs(Fraction(w) / D)
    if t >= 2:
        return Fraction(0)
    if t <= 1:
        return D * (Fraction(2, 3) - t * t + t * t * t / 2)
    return D * (2 - t) ** 3 / 6


def identity_b_exact(u, v, D):
    """int_0^1 sum_k tau(u-(k+theta)D) tau(v-(k+theta)D) dtheta,
    EXACT Fractions via piecewise Simpson (integrand pw-quadratic)."""
    lo = min(u, v) - D
    hi = max(u, v) + D
    k_lo = int(math.floor(float(lo / D))) - 1
    k_hi = int(math.ceil(float(hi / D))) + 1

    def s_of(th):
        tot = Fraction(0)
        for k in range(k_lo, k_hi + 1):
            p = (k + th) * D
            tot += tau_frac(u - p, D) * tau_frac(v - p, D)
        return tot

    bps = {Fraction(0), Fraction(1)}
    for k in range(k_lo, k_hi + 1):
        for w in (u, v):
            for off in (-1, 0, 1):
                th = Fraction(w) / D - k + off
                if 0 < th < 1:
                    bps.add(th)
    bps = sorted(bps)
    total = Fraction(0)
    for a, b in zip(bps[:-1], bps[1:]):
        m = (a + b) / 2
        total += (b - a) * (s_of(a) + 4 * s_of(m) + s_of(b)) / 6
    return total


def identity_b_mp(u, v, D):
    lo, hi = min(u, v) - D, max(u, v) + D
    k_lo = int(mp.floor(lo / D)) - 1
    k_hi = int(mp.ceil(hi / D)) + 1

    def tau_m(x):
        a = abs(x)
        return mp.mpf(0) if a >= D else 1 - a / D

    def s_of(th):
        return mp.fsum(tau_m(u - (k + th) * D) * tau_m(v - (k + th) * D)
                       for k in range(k_lo, k_hi + 1))

    bps = {mp.mpf(0), mp.mpf(1)}
    for k in range(k_lo, k_hi + 1):
        for w in (u, v):
            for off in (-1, 0, 1):
                th = w / D - k + off
                if 0 < th < 1:
                    bps.add(th)
    bps = sorted(bps)
    tot = mp.mpf(0)
    for a, b in zip(bps[:-1], bps[1:]):
        m = (a + b) / 2
        tot += (b - a) * (s_of(a) + 4 * s_of(m) + s_of(b)) / 6
    t = abs(u - v) / D
    rhs = mp.mpf(0) if t >= 2 else (
        D * (mp.mpf(2) / 3 - t * t + t ** 3 / 2) if t <= 1
        else D * (2 - t) ** 3 / 6)
    return tot, rhs / D


# =========================================== mpmath spot entry re-audit
def mp_arch_A(s, D):
    """arch_A(s, D) re-derived in mpmath from the same integrand
    formulas (independent quadrature)."""
    s = abs(mp.mpf(s))
    D = mp.mpf(D)

    def tau_m(x):
        a = abs(x)
        return mp.mpf(0) if a >= D else 1 - a / D

    if s >= D:
        f = lambda w: (tau_m(s - w) * mp.e ** (-w / 2)
                       / (1 - mp.e ** (-2 * w)))
        return -(mp.quad(f, [s - D, s, s + D]))
    tri = tau_m(s)
    W = s + D
    euler = mp.euler
    logpi = mp.log(mp.pi)

    def g(w):
        Sv = (tau_m(s - w) + tau_m(s + w)) / 2
        return ((tri * mp.e ** (-2 * w) - Sv * mp.e ** (-w / 2))
                / (1 - mp.e ** (-2 * w)))

    pts = sorted({mp.mpf(0), s, D - s, W})
    pts = [p for p in pts if 0 <= p <= W]
    tot = mp.quad(g, pts)
    return (-(euler + logpi) * tri + 2 * tot
            + tri * (-mp.log(1 - mp.e ** (-2 * W))))


def spot_entry_dev(wall, cell):
    """max |float64 c(x) - mpmath c(x)| over N_SPOTS declared spots."""
    h = wall.h
    xs = [0.37, 0.9, 1.73, 0.5 * h + 0.29, 2.0 * h - 1.42,
          1.0 * h + 0.11][:N_SPOTS]
    dev = 0.0
    with mp.workdps(SPOT_DPS):
        Dm = mp.mpf(2) * mp.mpf(cell["alpha"]) / cell["M"]
        for x in xs:
            f64 = float(wall.c_scalar_vec(np.array([x]))[0])
            v_ar = mp_arch_A(mp.mpf(x) * Dm, Dm)
            lo = np.searchsorted(wall.uh, x - 1.0)
            hi = np.searchsorted(wall.uh, x + 1.0)
            acc = mp.mpf(0)
            for j in range(lo, hi):
                nnj = int(round(math.exp(float(wall.uu[j]))))
                uj = (mp.log(nnj)
                      if abs(math.log(nnj) - float(wall.uu[j]))
                      < 1.0e-9 else mp.mpf(float(wall.uu[j])))
                t = mp.mpf(x) - uj / Dm
                v = 1 - abs(t)
                if v > 0:
                    acc -= mp.mpf(float(wall.mm[j])) * v / 2
            dev = max(dev, abs(f64 - float(v_ar + acc)))
    return dev


# ================================================================ tiers
def dyadic_list(tmax):
    out = [(0, Fraction(0))]
    for t in range(1, tmax + 1):
        den = 2 ** t
        for k in range(1, den, 2):
            out.append((t, Fraction(k, den)))
    return out


def ok_res(r):
    return r is not None and "refused" not in r


def tier1_cell(tag, wall, n_grid, dy_tmax, floor_hint=None):
    """Certified s(theta) on the midpoint grid + theta=0 + dyadics;
    every PD refusal is DIAGNOSED (LDL inertia)."""
    rows = {}
    t_ev = []
    hint = floor_hint

    def ev(th):
        key = float(th)
        if key in rows:
            return rows[key]
        t_a = time.time()
        res = cert_schur(wall.omega(key), floor_hint=hint,
                         diagnose=True)
        t_ev.append(time.time() - t_a)
        rows[key] = res
        return res

    r0 = ev(0.0)
    if ok_res(r0):
        hint = r0["c_lo"] * 2.0
    grid = [(2 * i + 1) / (2.0 * n_grid) for i in range(n_grid)]
    for th in grid:
        ev(th)
    dyads = dyadic_list(dy_tmax)
    for _t, fr in dyads:
        ev(float(fr))
    ok_rows = {k: v for k, v in rows.items() if ok_res(v)}
    pd_fail = sorted(k for k, v in rows.items() if not ok_res(v))
    svals = np.array([rows[th]["s"] for th in grid
                      if ok_res(rows[th])])
    slo = np.array([rows[th]["s_lo"] for th in grid
                    if ok_res(rows[th])])
    shi = np.array([rows[th]["s_hi"] for th in grid
                    if ok_res(rows[th])])
    # the UNCERTIFIED tier (float64 measurement, no enclosure):
    # certificate-refused evaluations whose factorization succeeded
    avals = np.array([(rows[th]["s"] if ok_res(rows[th])
                       else rows[th].get("uncert_s", np.nan))
                      for th in grid])
    n_grid_pd = len(svals)
    mean = float(np.mean(svals)) if len(svals) else float("nan")
    out = dict(tag=tag, rows=rows, grid=grid, pd_fail=pd_fail,
               mean=mean, frac_fail=1.0 - n_grid_pd / float(n_grid),
               mean_all=(float(np.nanmean(avals))
                         if not np.isnan(avals).all()
                         else float("nan")),
               n_uncert=int(np.sum([not ok_res(rows[th])
                                    and "uncert_s" in rows[th]
                                    for th in grid])),
               mean_lo=float(np.mean(slo)) if len(slo) else float("nan"),
               mean_hi=float(np.mean(shi)) if len(shi) else float("nan"),
               s_min=float(np.min(svals)) if len(svals) else float("nan"),
               s_max=float(np.max(svals)) if len(svals) else float("nan"),
               s0=r0 if ok_res(r0) else None,
               s0_uncert=(r0.get("uncert_s") if not ok_res(r0)
                          else None),
               t_eval=float(np.median(t_ev)) if t_ev else 0.0,
               n_pd=len(ok_rows), n_all=len(rows))
    # refusal diagnosis census
    diag = [(k, rows[k].get("n_neg"), rows[k].get("min_piv"),
             rows[k]["refused"]) for k in pd_fail]
    out["diag"] = diag
    out["n_ldl_err"] = sum(1 for k in pd_fail
                           if rows[k].get("ldl_err"))
    out["genuine_neg"] = [d for d in diag
                          if d[1] is not None and d[1] >= 1]
    out["res_limited"] = [d for d in diag
                          if d[1] is not None and d[1] == 0]
    nnegs = [d[1] for d in diag if d[1] is not None and d[1] >= 0]
    out["nneg_range"] = ((min(nnegs), max(nnegs)) if nnegs else None)
    # the frozen H_cof dyadic choice rule (typed: candidate only)
    theta_star = None
    for t, fr in dyads:
        r = rows.get(float(fr))
        if ok_res(r) and r["s_lo"] > 0.0:
            theta_star = (t, fr)
            break
    out["theta_star"] = theta_star
    v2s = [v["v2"] for v in ok_rows.values()]
    cls = [v["c_lo"] for v in ok_rows.values()]
    bns = [v["bnorm"] for v in ok_rows.values()]
    out["v2_max"] = max(v2s) if v2s else float("nan")
    out["c_lo_min"] = min(cls) if cls else float("nan")
    out["b_max"] = max(bns) if bns else float("nan")
    return out


def jensen_cell(wall):
    """The exact theta-averaged wall Omega_bar + certified
    s(Omega_bar) (>= true mean by Schur concavity, E2)."""
    h = wall.h
    # atom part: unit integrals of c_at on [-1, 2h+2]
    F = wall.atom_unit_integrals(-1, 2 * h + 3)   # F[j]=int over [j-1,j)

    def int_c_at(a, b):                            # a,b integers
        return float(np.sum(F[a + 1:b + 1]))

    # arch part per unit interval, warded GL
    A24 = np.array([wall.arch_unit_integral(r, _GLX24, _GLW24)
                    for r in range(-1, 2 * h + 2)])
    ridx = [0, 2 * h // 2, 2 * h]
    dev = max(abs(A24[r + 1] - wall.arch_unit_integral(r, _GLX48,
                                                       _GLW48))
              for r in ridx)

    def int_c(a, b):
        return int_c_at(a, b) + float(np.sum(A24[a + 1:b + 1]))

    # Gbar(r) = 1/2 int_r^{r+2} G(x) dx
    gbar = np.empty(2 * h - 1)
    for r in range(0, 2 * h - 1):
        v = int_c(r, r + 2) - 0.5 * int_c(r + 1, r + 3)
        if r >= 1:
            v -= 0.5 * int_c(r - 1, r + 1)
        else:
            v -= 0.5 * 2.0 * int_c(0, 1)          # int_{-1}^{1} c(|t|)
        gbar[r] = 0.5 * v
    om_bar = wall.omega_from_gh(gbar)
    res = cert_schur(om_bar, want_y=True, diagnose=True)
    return res, om_bar, gbar, dev


def arch_curvature(wall):
    """The declared arch model constant S2 = sum_r max_theta0
    |d^2 G_arch(r + 2 theta)/dx^2| (FD at three off-kink theta0,
    times ENV_SAFE).  The antidiagonal SUM bounds the spectral norm
    of the arch curvature Hankel perturbation (each row meets each
    antidiagonal once), so no extra factor h enters."""
    h = wall.h
    th0s = (0.13, 0.37, 0.71)
    rr = np.arange(0, 2 * h - 1, dtype=float)
    s2 = np.zeros(2 * h - 1)
    for th0 in th0s:
        x0 = rr + 2.0 * th0
        # G_arch(x) = A(x) - (A(x+1) + A(|x-1|))/2 at x0 +- 2 fd
        vals = []
        for off in (-2.0 * FD_STEP, 0.0, 2.0 * FD_STEP):
            x = x0 + off
            pts = np.concatenate([np.abs(x), x + 1.0,
                                  np.abs(x - 1.0)])
            a = core.arch_A(pts * wall.D, wall.D)
            n = len(x)
            vals.append(a[:n] - 0.5 * (a[n:2 * n] + a[2 * n:]))
        d2 = np.abs(vals[0] - 2.0 * vals[1] + vals[2]) \
            / (2.0 * FD_STEP) ** 2
        s2 = np.maximum(s2, d2)
    return ENV_SAFE * s2, ENV_SAFE * float(np.sum(s2))


def tier2_cell(tag, wall, t1, s2_arch, eps_entry):
    """Piece-exact Hermite-Hadamard enclosure of int_0^1 s dtheta.
    Pieces = atom breakpoints + {0, 1/2, 1}, subdivided to max
    length 1/L_SUB (HH holds on any subinterval of an affine piece).
    Per-piece slacks through the DECLARED measured-vhat model
    (vhat = (1, -y) of the piece evaluations, transfer factor
    MODEL_FAC = 2, warded by the concavity ward): arch curvature
    |Delta s| <= (len^2/4) sum_r S2[r] conv_r(|vhat|) (the exact
    antidiagonal transfer -- conv is the autocorrelation of |vhat|;
    S2 the FD-measured curvature profile x 8), entry envelope
    2 eps ||vhat||_1^2."""
    h = wall.h
    bset = {0.0, 0.5, 1.0}
    half = np.mod(wall.uh / 2.0, 1.0)
    for v in half:
        bset.add(float(v))
        bset.add(float(math.fmod(v + 0.5, 1.0)))
    raw = np.array(sorted(x for x in bset if 0.0 <= x <= 1.0))
    if raw[0] > 0.0:
        raw = np.concatenate([[0.0], raw])
    if raw[-1] < 1.0:
        raw = np.concatenate([raw, [1.0]])
    keep = np.concatenate([[True], np.diff(raw) > 1.0e-14])
    raw = raw[keep]
    # forced subdivision to max piece length 1/L_SUB
    fine = [raw[0]]
    for a, b in zip(raw[:-1], raw[1:]):
        nsub = max(1, int(math.ceil((b - a) * L_SUB)))
        for j in range(1, nsub + 1):
            fine.append(a + (b - a) * j / nsub)
    bps = np.array(fine)
    n_piece = len(bps) - 1
    n_eval = 2 * n_piece + 1
    proj = n_eval * max(t1["t_eval"], 1.0e-4)
    print("    pieces %d (%d atom breakpoints), projected %.0f s "
          "(eval %.4f s)" % (n_piece, len(raw) - 1, proj,
                             t1["t_eval"]))
    if proj > TIER2_CAP_S:
        return dict(tag=tag, status="TIER2-UNAFFORDABLE",
                    n_piece=n_piece, proj=proj)
    hint = t1["s0"]["c_lo"] * 2.0 if t1["s0"] else None
    s2_prof, _s2_sum = s2_arch
    cache = {}

    def ev(th):
        key = round(float(th), 15)
        if key not in cache:
            res = cert_schur(wall.omega(float(th)), floor_hint=hint,
                             want_y=True)
            if ok_res(res):
                av = np.concatenate([[1.0], np.abs(res.pop("y"))])
                n2 = 1 << int(math.ceil(math.log2(2 * len(av))))
                fa = np.fft.rfft(av, n2)
                conv = np.abs(np.fft.irfft(fa * fa, n2)[:len(s2_prof)])
                res["e_conv"] = float(np.dot(s2_prof, conv))
                res["l1sq"] = float(np.sum(av)) ** 2
            cache[key] = res
        return cache[key]

    lo_sum, hi_sum = 0.0, 0.0
    pd_fail_pieces = 0
    fail_measure = 0.0
    v2max, c_lo_min = 0.0, float("inf")
    pd_len = 0.0
    slack_arch, slack_entry, slack_viol = 0.0, 0.0, 0.0
    viols = []
    for i in range(n_piece):
        a, b = float(bps[i]), float(bps[i + 1])
        ln = b - a
        ra, rb = ev(a), ev(b)
        rm = ev(0.5 * (a + b))
        if not (ok_res(ra) and ok_res(rb) and ok_res(rm)):
            pd_fail_pieces += 1
            fail_measure += ln
            continue
        pd_len += ln
        lo_sum += ln * 0.5 * (ra["s_lo"] + rb["s_lo"])
        hi_sum += ln * rm["s_hi"]
        econv = max(ra["e_conv"], rb["e_conv"], rm["e_conv"])
        l1sq = max(ra["l1sq"], rb["l1sq"], rm["l1sq"])
        arch_p = 0.25 * ln * ln * econv * MODEL_FAC
        ent_p = 2.0 * eps_entry * l1sq * MODEL_FAC
        chord = 0.5 * (ra["s"] + rb["s"])
        hw = 0.5 * (ra["s_hi"] - ra["s_lo"] + rb["s_hi"] - rb["s_lo"]) \
            + 0.5 * (rm["s_hi"] - rm["s_lo"])
        defect = chord - hw - arch_p - rm["s"]
        if defect > 1.0e-13 * (abs(chord) + 1.0):
            # the concavity ward FIRED: the declared model
            # under-priced this piece; repair by widening the
            # enclosure by the measured defect x VIOL_FAC (typed)
            viols.append((a, b, defect))
            slack_viol += ln * defect * VIOL_FAC
        slack_arch += ln * arch_p
        slack_entry += ln * ent_p
        v2max = max(v2max, ra["v2"], rb["v2"], rm["v2"])
        c_lo_min = min(c_lo_min, ra["c_lo"], rb["c_lo"], rm["c_lo"])
    slack_bp = 2.0 * n_piece * 1.0e-12 * max(abs(t1["s_max"]),
                                             abs(t1["s_min"]))
    slack = slack_arch + slack_entry + slack_bp + slack_viol
    status = "OK" if pd_fail_pieces == 0 else "OK-CONDITIONAL"
    for a, b, d in viols[:4]:
        print("      WARD-FIRED piece [%.6f, %.6f]: defect %.2e "
              "(repaired x%.0f)" % (a, b, d, VIOL_FAC))
    return dict(tag=tag, status=status, n_piece=n_piece,
                pd_fail_pieces=pd_fail_pieces,
                fail_measure=fail_measure, pd_measure=pd_len,
                mean_lo=lo_sum - slack, mean_hi=hi_sum + slack,
                conc_viol=len(viols), slack_arch=slack_arch,
                slack_entry=slack_entry, slack_bp=slack_bp,
                slack_viol=slack_viol,
                v2max=v2max, c_lo_min=c_lo_min, n_eval=len(cache))


# =============================================== decomposition (C) probe
def decompose_c(wall, om_bar):
    """Exact P_bar = int_0^1 b b^T dtheta (piecewise Simpson, exact
    for the pw-quadratic atom products; arch part enters through the
    same nodes -- model slack typed), split and energies."""
    h = wall.h
    bset = {0.0, 0.5, 1.0}
    half = np.mod(wall.uh / 2.0, 1.0)
    for v in half:
        bset.add(float(v))
        bset.add(float(math.fmod(v + 0.5, 1.0)))
    bps = np.array(sorted(bset))
    keep = np.concatenate([[True], np.diff(bps) > 1.0e-14])
    bps = bps[keep]
    n_piece = len(bps) - 1
    # Simpson nodes + weights
    nodes, wgt = [], []
    for i in range(n_piece):
        a, b = float(bps[i]), float(bps[i + 1])
        ln = b - a
        nodes += [a, 0.5 * (a + b), b]
        wgt += [ln / 6.0, 4.0 * ln / 6.0, ln / 6.0]
    nodes = np.array(nodes)
    wgt = np.array(wgt)
    # columns: hankel reads split (m = 1..h-1 of g = G(m+2theta))
    E_aa = np.zeros((h - 1, h - 1))
    E_ac = np.zeros((h - 1, h - 1))
    E_cc = np.zeros((h - 1, h - 1))
    Ea = np.zeros(h - 1)
    Ec = np.zeros(h - 1)
    # constant Toeplitz split
    ci_a = core.arch_A(np.abs(np.arange(-1.0, h + 2.0)) * wall.D,
                       wall.D)
    ci_c = np.array([wall._atom_scalar(abs(float(x)))
                     for x in np.arange(-1.0, h + 2.0)])
    gt_a = ci_a[1:h + 1] - 0.5 * (ci_a[2:h + 2] + ci_a[0:h])
    gt_c = ci_c[1:h + 1] - 0.5 * (ci_c[2:h + 2] + ci_c[0:h])
    tvec_a, tvec_c = gt_a[1:h], gt_c[1:h]
    for th, w in zip(nodes, wgt):
        ga, gc = wall.G_hankel(float(th), split=True)
        va, vc = ga[1:h], gc[1:h]
        E_aa += w * np.outer(va, va)
        E_ac += w * np.outer(va, vc)
        E_cc += w * np.outer(vc, vc)
        Ea += w * va
        Ec += w * vc
    P_aa = 0.25 * (E_aa + np.outer(Ea, tvec_a) + np.outer(tvec_a, Ea)
                   + np.outer(tvec_a, tvec_a))
    P_cc = 0.25 * (E_cc + np.outer(Ec, tvec_c) + np.outer(tvec_c, Ec)
                   + np.outer(tvec_c, tvec_c))
    P_ac = 0.25 * (E_ac + np.outer(Ea, tvec_c) + np.outer(tvec_a, Ec)
                   + np.outer(tvec_a, tvec_c))
    P_cross = P_ac + P_ac.T
    P_all = P_aa + P_cross + P_cc
    B0 = np.ascontiguousarray(om_bar[1:, 1:])
    cf = sla.cho_factor(B0, lower=True, check_finite=False)

    def tr_term(P):
        return float(np.trace(sla.cho_solve(cf, P, check_finite=False)))

    # PSD ward on P_cc (second moment -> PSD up to roundoff)
    shift = 1.0e-14 * float(np.max(np.abs(P_cc))) + 1.0e-300
    try:
        np.linalg.cholesky(P_cc + shift * np.eye(h - 1))
        psd_ok = True
    except np.linalg.LinAlgError:
        psd_ok = False
    return dict(n_piece=n_piece, psd_ok=psd_ok,
                t_aa=tr_term(P_aa), t_cross=tr_term(P_cross),
                e_plus=tr_term(P_cc), t_all=tr_term(P_all))


# ================================================================= main
def main():
    print("=" * 78)
    print("PRIME.COFINAL.SHIFT.AVERAGE.01 -- grid-phase averaging "
          "(shift_average_probe)%s" % ("  ** SMOKE **" if SMOKE else ""))
    print("=" * 78)
    print("SPEC SHA-256: %s" % SPEC_SHA)
    with open(os.path.abspath(__file__), "rb") as fh:
        print("CODE SHA-256: %s"
              % hashlib.sha256(fh.read()).hexdigest())

    # ------------------------------------------------------------- S0
    section("S0 -- freeze + firewall")
    hits, rng_bad = ast_firewall()
    check("S0.AST no zero-generator and NO EIGENSOLVER call in this "
          "file; RNG seeds literal", not hits and not rng_bad,
          "hits=%s rng=%s" % (hits, rng_bad), kill="K0")
    check("S0.NU deployed frame constant NU == core.NU_MAIN == 4",
          NU == int(core.NU_MAIN) == 4, kill="K0")

    # -------------------------------------------------------------- T
    section("T -- tables + census + picks (source, independent)")
    t_a = time.time()
    ok_tab = build_tables()
    check("T1 sieve to %.1e BITWISE == deployed prefix (%.1f s)"
          % (TAB, time.time() - t_a), ok_tab, kill="K1")
    cen = census()
    picks = pick_cells(cen)
    print("    census: %d cells, h in [%d, %d]"
          % (len(cen), cen[0]["h"], cen[-1]["h"]))
    for tgt in TARGETS:
        c = picks[tgt]
        print("    target %4d -> h %4d kz %3d alpha %.4f M %5d "
              "X %.3e" % (tgt, c["h"], c["kz"], c["alpha"], c["M"],
                          c["X"]))
    check("T2 all five targets resolved to census cells "
          "(nearest-h rule, frozen)", len(picks) == 5, kill="K1")

    run_targets = TARGETS if not SMOKE else (184, 838)

    # -------------------------------------------------------------- W
    section("W -- faithfulness wards")
    walls = {}
    dep_ok = True
    for tgt in run_targets:
        cell = picks[tgt]
        uu, mm = cell_atoms(cell)
        w = Wall(cell, uu, mm)
        walls[tgt] = w
        # deployed route (verdicta window_data verbatim)
        c_ar = np.asarray(core.arch_lags(cell["M"], w.D), float)
        c_at = np.asarray(core.atom_lags_at(cell["alpha"], cell["M"],
                                            uu, mm)[0], float)
        lag = c_ar + c_at
        mine = w.c_ladder(0.0)[1:]            # r = 0..2h-1
        scale = float(np.max(np.abs(lag))) + 1e-300
        dev = float(np.max(np.abs(mine - lag))) / scale
        M2 = cell["M"]
        aext = np.concatenate([lag, [lag[M2 - 2]]])
        rr = np.arange(2 * w.h)
        gseq = aext[rr] - 0.5 * (aext[rr + 1] + aext[np.abs(rr - 1)])
        gh0 = w.G_hankel(0.0)
        devg = float(np.max(np.abs(gh0 - gseq[:2 * w.h - 1]))) \
            / (float(np.max(np.abs(gseq))) + 1e-300)
        ok = dev <= WARD_DEP_REL and devg <= WARD_DEP_REL
        dep_ok = dep_ok and ok
        print("    h %4d: |c - deployed lag| rel %.2e, |G - gseq| "
              "rel %.2e" % (w.h, dev, devg))
    check("W1 theta = 0 reproduces the DEPLOYED lag profile and G "
          "sequence at every picked cell (rel <= %.0e)"
          % WARD_DEP_REL, dep_ok, kill="K3")
    w0 = walls[run_targets[0]]
    om0 = w0.omega(0.0)
    om1 = w0.omega(1.0)
    dev_sh = float(np.max(np.abs(om1[:-1, :-1] - om0[1:, 1:]))) \
        / (float(np.max(np.abs(om0))) + 1e-300)
    check("W2 shift identity Omega_1[m,m'] == Omega_0[m+1,m'+1] "
          "(rel %.2e <= %.0e)" % (dev_sh, WARD_SHIFT_REL),
          dev_sh <= WARD_SHIFT_REL, kill="K3")

    # identity (B) -- item (4)
    d_r = Fraction(3, 200)
    u_r = Fraction(7, 5)
    exact_ok = True
    for wnum, wden in ((0, 1), (1, 3), (1, 2), (1, 1), (3, 2),
                       (2, 1), (5, 2)):
        wq = Fraction(wnum, wden) * d_r
        lhs = identity_b_exact(u_r, u_r - wq, d_r)
        rhs = bspline_frac(wq, d_r) / d_r
        exact_ok = exact_ok and (lhs == rhs)
    check("W3a identity (B) EXACT (Fraction Simpson == closed-form "
          "B-spline) on 7 rational separations", exact_ok, kill="K3")
    with mp.workdps(MP_DPS):
        dd = mp.mpf(2) * mp.mpf(picks[184]["alpha"]) / picks[184]["M"]
        devs = []
        for (uu_, vv_) in ((mp.log(5), mp.log(3)),
                           (mp.log(7), mp.log(7) - mp.mpf("1.7") * dd)):
            lhs, rhs = identity_b_mp(uu_, vv_, dd)
            devs.append(abs(lhs - rhs))
        dmax = max(devs)
    check("W3b identity (B) mpmath dps %d on irrational tuples: "
          "max |dev| %s <= 1e-40 (>= 40 digits)"
          % (MP_DPS, mp.nstr(dmax, 3)), dmax <= IDB_BAR, kill="K3")

    # -------------------------------------------------------------- A
    section("A -- TIER 1: certified s(theta) on the frozen grids")
    t1res, spot_eps, m2arch = {}, {}, {}
    for tgt in run_targets:
        w = walls[tgt]
        t_a = time.time()
        eps = spot_entry_dev(w, picks[tgt]) if not SMOKE else 1e-13
        spot_eps[tgt] = ENV_SAFE * eps
        m2arch[tgt] = arch_curvature(w)
        r = tier1_cell("h%d" % w.h, w, N_THETA[tgt], DY_TMAX[tgt])
        t1res[tgt] = r
        se0 = (2.0 * w.h * spot_eps[tgt] * r["s0"]["v2"]
               if r["s0"] else float("nan"))
        ths = ("den 2^%d, theta = %s" % (r["theta_star"][0],
                                         r["theta_star"][1])
               if r["theta_star"] else "NONE")
        s0txt = (("%.6e" % r["s0"]["s"]) if r["s0"]
                 else ("%.6e UNCERT" % r["s0_uncert"])
                 if r["s0_uncert"] is not None else "REFUSED")
        print("    h %4d (N %3d): CERT %d/%d, UNCERT %d (refusal "
              "measure ~%.3f) | s(0) %s (entry-slack %.1e) | CERT "
              "mean %.6e [%.6e, %.6e] | ALL-TIER mean %.6e | "
              "min/max %.3e / %.3e | c_lo,min %.3e V2max %.2e | "
              "theta* (dyadic) %s | %.1f s"
              % (w.h, N_THETA[tgt], r["n_pd"], r["n_all"],
                 r["n_uncert"], r["frac_fail"], s0txt, se0,
                 r["mean"], r["mean_lo"], r["mean_hi"],
                 r["mean_all"], r["s_min"], r["s_max"],
                 r["c_lo_min"], r["v2_max"], ths,
                 time.time() - t_a))
        if r["pd_fail"]:
            head = ", ".join("%.4f(%s, n_neg %s, minpiv %.1e)"
                             % (th, kd, nn, mp_)
                             for th, nn, mp_, kd in r["diag"][:4])
            print("      refusals (%d; genuine-indefinite %d, "
                  "resolution-limited %d), first 4: %s"
                  % (len(r["pd_fail"]), len(r["genuine_neg"]),
                     len(r["res_limited"]), head))
    check("A1 instrument coherent: every certificate refusal "
          "carries an LDL diagnosis (0 LDL errors, 0 unexplained "
          "CHOL-FAIL-with-n_neg-0)",
          all(t1res[t]["n_ldl_err"] == 0
              and not any(d[3] == "CHOL-FAIL" and d[1] == 0
                          for d in t1res[t]["diag"])
              for t in run_targets),
          "; ".join("h%d: %d refusals (%d genuine, %d "
                    "resolution-limited)"
                    % (walls[t].h, len(t1res[t]["pd_fail"]),
                       len(t1res[t]["genuine_neg"]),
                       len(t1res[t]["res_limited"]))
                    for t in run_targets))
    s0_neg = [walls[t].h for t in run_targets
              if t1res[t]["s0"] is not None
              and t1res[t]["s0"]["s_hi"] < 0.0]
    s0_res = [walls[t].h for t in run_targets
              if t1res[t]["s0"] is not None
              and t1res[t]["s0"]["s_lo"] > 0.0]
    check("A2 theta = 0 anchor: no certified-NEGATIVE s(0) "
          "anywhere; enclosure-positive at %s (cells beyond the "
          "float64 enclosure resolution typed UNCERT)" % s0_res,
          not s0_neg and len(s0_res) >= min(3, len(run_targets)))

    # -------------------------------------------------------------- J
    section("J -- exact averaged wall + Jensen kill test (E2)")
    jres = {}
    for tgt in run_targets:
        w = walls[tgt]
        t_a = time.time()
        res, om_bar, gbar, gl_dev = jensen_cell(w)
        if not ok_res(res):
            un = res.get("uncert_s") if res else None
            print("    h %4d: s(Omega_bar) certificate REFUSED "
                  "(%s)%s" % (w.h, res.get("refused") if res
                              else "?",
                              " -- UNCERT value %.6e" % un
                              if un is not None else ""))
            jres[tgt] = (None, om_bar, un)
            continue
        jres[tgt] = (res, om_bar, None)
        print("    h %4d: s(Omega_bar) %.6e [%.6e, %.6e] | GL ward "
              "%.1e | mean(T1) %.6e <= upper %s | %.1f s"
              % (w.h, res["s"], res["s_lo"], res["s_hi"], gl_dev,
                 t1res[tgt]["mean"],
                 "OK" if not np.isfinite(t1res[tgt]["mean"])
                 or t1res[tgt]["mean"] <= res["s_hi"]
                 + JENSEN_TOL_REL * abs(res["s"]) else "VIOLATED",
                 time.time() - t_a))
    j_cells = [t for t in run_targets
               if jres[t][0] is not None
               and np.isfinite(t1res[t]["mean"])]
    jensen_ok = all(t1res[t]["mean"] <= jres[t][0]["s_hi"]
                    + JENSEN_TOL_REL * (abs(jres[t][0]["s"]) + 1e-30)
                    for t in j_cells)
    check("J1 Jensen ward: certified mean <= certified "
          "s(Omega_bar) on every resolvable cell (Schur concavity, "
          "E2; cells: %s)" % [walls[t].h for t in j_cells],
          jensen_ok and len(j_cells) >= min(3, len(run_targets)))
    # the kill test binds only where the PD premise holds for all
    # sampled theta (else the mean of s is not the defined object)
    jensen_kill = [t for t in run_targets
                   if not t1res[t]["pd_fail"]
                   and jres[t][0] is not None
                   and jres[t][0]["s_hi"]
                   + 2.0 * walls[t].h * spot_eps[t]
                   * jres[t][0]["v2"] < 0.0]
    check("J2 Jensen KILL test: no full-PD cell has certified "
          "s(Omega_bar) < 0 (which would certify mean < 0)",
          not jensen_kill, "killed at %s" % jensen_kill,
          kill="K4" if jensen_kill else None)

    # -------------------------------------------------------------- H
    section("H -- TIER 2: piece-exact Hermite-Hadamard enclosures")
    t2res = {}
    budget = TIER2_TOTAL_S
    for tgt in run_targets:
        w = walls[tgt]
        t_a = time.time()
        if budget <= 0.0:
            t2res[tgt] = dict(status="TIER2-UNAFFORDABLE",
                              n_piece=-1, proj=-1.0)
            print("    h %4d: total budget exhausted -- TIER 1 only"
                  % w.h)
            continue
        print("    h %4d:" % w.h)
        r2 = tier2_cell("h%d" % w.h, w, t1res[tgt], m2arch[tgt],
                        spot_eps[tgt])
        t2res[tgt] = r2
        el = time.time() - t_a
        budget -= el
        if r2["status"].startswith("OK"):
            cond = ("" if r2["status"] == "OK"
                    else " CONDITIONAL on the PD subset (measure "
                    "%.4f; %d/%d pieces refused)"
                    % (r2["pd_measure"], r2["pd_fail_pieces"],
                       r2["n_piece"]))
            print("      CERT%s: int s over PD-subset in [%.6e, "
                  "%.6e] | %d pieces, %d evals | ward-fired %d "
                  "(repaired, slack %.1e) | slacks arch %.1e entry "
                  "%.1e bp %.1e | %.1f s"
                  % (cond, r2["mean_lo"], r2["mean_hi"],
                     r2["n_piece"], r2["n_eval"], r2["conc_viol"],
                     r2["slack_viol"], r2["slack_arch"],
                     r2["slack_entry"], r2["slack_bp"], el))
        else:
            print("      %s" % r2["status"])
    cert_cells = [t for t in run_targets
                  if t2res[t]["status"].startswith("OK")]
    full_cert = [t for t in cert_cells if t2res[t]["status"] == "OK"]
    conc_ok = all(t2res[t]["conc_viol"] <= VIOL_CAP
                  for t in cert_cells)
    check("H1 concavity ward coherent on every TIER-2 cell "
          "(<= %d model under-pricings, each repaired into the "
          "enclosure and printed)" % VIOL_CAP,
          conc_ok and len(cert_cells) >= 1,
          "cert cells: %s (unconditional: %s), ward-fired: %s"
          % ([walls[t].h for t in cert_cells],
             [walls[t].h for t in full_cert],
             [t2res[t]["conc_viol"] for t in cert_cells]))
    cross_ok = True
    for t in cert_cells:
        r2 = t2res[t]
        # compare against the conditional T1 mean scaled by measure
        est = t1res[t]["mean"] * r2["pd_measure"]
        tol = 0.15 * (abs(est) + abs(r2["mean_hi"]) + 1e-30)
        cross_ok = cross_ok and (r2["mean_lo"] - tol <= est
                                 <= r2["mean_hi"] + tol)
    check("H2 cross-ward: the TIER-1 conditional grid mean (scaled "
          "by the PD measure) is consistent with every TIER-2 "
          "enclosure", cross_ok)
    t2_kill = [t for t in full_cert if t2res[t]["mean_hi"] < 0.0]
    check("H3 TIER-2 KILL test: no unconditional certified "
          "enclosure puts the mean below zero", not t2_kill,
          "killed at %s" % t2_kill, kill="K4" if t2_kill else None)

    # -------------------------------------------------------------- C
    section("C -- decomposition attempt (identity (C)) at the "
            "smallest cell")
    tgt_c = run_targets[0]
    w = walls[tgt_c]
    res_j, om_bar = jres[tgt_c][0], jres[tgt_c][1]
    dec = decompose_c(w, om_bar)
    mean_c = t1res[tgt_c]["mean"]        # conditional-on-PD, typed
    n_bar = res_j["n"] if res_j else float("nan")
    q_bar = n_bar - mean_c
    delta_b = q_bar - dec["t_all"]
    print("    (means CONDITIONAL on the PD subset where the "
          "premise broke)")
    print("    n_bar %.6e | q_bar %.6e | tr(B0^-1 P_aa) %.6e | "
          "tr(B0^-1 P_cross) %.6e | E+ = tr(B0^-1 P_cc) %.6e | "
          "delta_B %.6e" % (n_bar, q_bar, dec["t_aa"],
                            dec["t_cross"], dec["e_plus"], delta_b))
    print("    mean s = n_bar - tr(B0^-1 P_aa) - tr(B0^-1 P_cross) "
          "- E+ - delta_B = %.6e (recomposed %.6e)"
          % (mean_c, n_bar - dec["t_all"] - delta_b))
    check("C1 the comb x comb block P_cc of the theta-averaged pair "
          "kernel is PSD (second moment; the identity-(B) energy)",
          dec["psd_ok"] and dec["e_plus"] >= -1e-15)
    struct = ("C-STRUCTURE-INVERTED" if dec["e_plus"] > 0.0
              else "C-ENERGY-VACUOUS")
    print("    TYPED READING: the PSD comb energy enters the mean "
          "through -b^T B^-1 b, i.e. with sign -E+ = %.3e -- %s: "
          "the mission's target (C) (positive prime energy CARRYING "
          "the mean) does NOT materialize on this wall, which is "
          "LINEAR in the comb (the CCCXXXI-A1 analogue, measured); "
          "the mean is carried by n_bar - arch/cross terms."
          % (-dec["e_plus"], struct))
    check("C2 decomposition ledger closes: mean == n_bar - "
          "tr(B0^-1 P_bar) - delta_B by construction (delta_B "
          "measured %.2e, the B(theta)-variation term)" % delta_b,
          np.isfinite(delta_b))

    # -------------------------------------------------------------- X
    section("X -- controls (identical pipeline, frozen)")
    ctrl_rows = []
    for tgt in (CTRL_TARGETS if not SMOKE else (184,)):
        if tgt not in walls:
            continue
        cell = picks[tgt]
        for world in ("scramble", "epstein"):
            uu, mm = cell_atoms(cell, world=world, seed=SEED_SCR)
            wc = Wall(cell, uu, mm)
            r = tier1_cell("%s-h%d" % (world, wc.h), wc, CTRL_N, 2)
            ctrl_rows.append((world, wc.h, r))
            ms = ("mean %.3e" % r["mean"]) if r["n_pd"] else "no mean"
            print("    %s h %4d: PD %d/%d | %s | s range [%.3e, "
                  "%.3e]" % (world.upper(), wc.h, r["n_pd"],
                             r["n_all"], ms,
                             r["s_min"] if r["n_pd"] else float("nan"),
                             r["s_max"] if r["n_pd"] else float("nan")))
    fired = sum(1 for _wl, _h, r in ctrl_rows
                if r["pd_fail"] or (np.isfinite(r["mean"])
                                    and r["mean"] < 0.0)
                or r["s_min"] < 0.0)
    check("X1 controls fire: %d/%d control runs break PD or read a "
          "negative s somewhere (genuine cells do neither)"
          % (fired, len(ctrl_rows)), fired >= 1,
          "silent controls are typed, not hidden")

    # -------------------------------------------------------------- V
    section("V -- verdict")
    ill = "W1" in FAILS or "W2" in FAILS or "W3a" in FAILS \
        or "W3b" in FAILS
    dead = bool(jensen_kill or t2_kill)
    broken = [t for t in run_targets if t1res[t]["genuine_neg"]]
    reslim = [t for t in run_targets
              if t1res[t]["res_limited"] and not
              t1res[t]["genuine_neg"]]
    neg_cells = [walls[t].h for t in run_targets
                 if (not np.isfinite(t1res[t]["mean_all"]))
                 or t1res[t]["mean_all"] <= 0.0]
    cell_lines = []
    for t in run_targets:
        r1, r2 = t1res[t], t2res.get(t, {})
        if t in broken:
            stat = ("PREMISE-BROKEN(B(theta) indefinite at %d "
                    "offsets, n_neg %s; refusal measure ~%.3f)"
                    % (len(r1["genuine_neg"]), r1["nneg_range"],
                       r1["frac_fail"]))
        elif r2.get("status") == "OK" and r2["mean_lo"] > 0.0:
            stat = "CERT-POS-MEAN [%.3e, %.3e]" % (r2["mean_lo"],
                                                   r2["mean_hi"])
        elif t in reslim:
            stat = ("RESOLUTION-LIMITED(B-floor below the float64 "
                    "Higham slack at %d/%d offsets, n_neg = 0 "
                    "everywhere; UNCERT mean %.3e)"
                    % (len(r1["res_limited"]), r1["n_all"],
                       r1["mean_all"]))
        elif r2.get("status") == "OK":
            stat = ("MEAS-MEAN %.3e (CERT enclosure [%.3e, %.3e] "
                    "inconclusive)" % (r1["mean"], r2["mean_lo"],
                                       r2["mean_hi"]))
        else:
            stat = "MEAS-MEAN %.3e" % r1["mean"]
        cell_lines.append("h%d: %s" % (walls[t].h, stat))
    print("  per cell: " + " | ".join(cell_lines))
    if ill:
        verdict = "SHIFTAVG-ILLDEFINED(faithfulness wards failed)"
    elif dead:
        verdict = "SHIFTAVG-DEAD(certified negative mean at %s)" \
            % ([walls[t].h for t in (jensen_kill + t2_kill)])
    elif broken or neg_cells:
        verdict = ("SHIFTAVG-MIXED(%s%s)"
                   % ("premise B(theta)>0 BROKEN at %s"
                      % [walls[t].h for t in broken] if broken
                      else "",
                      "%snonpositive/undefined means at %s"
                      % ("; " if broken else "", neg_cells)
                      if neg_cells else ""))
    else:
        verdict = "SHIFTAVG-POSITIVE(%s)" % "; ".join(cell_lines)
    print("\n  VERDICT: %s" % verdict)
    print("  theta* dyadic picks (H_cof candidate rule, typed "
          "certificate-conditioned -- the CCCXXXVII Q-3 tension "
          "applies): %s"
          % "; ".join("h%d: %s" % (walls[t].h,
                                   t1res[t]["theta_star"][1]
                                   if t1res[t]["theta_star"]
                                   else "NONE")
                      for t in run_targets))
    print("  A positive read is 'no witness found' -- route "
          "positivity is NOT certified; NO all-h statement; "
          "NO RH claim.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed%s   "
          "[KILLS] %s"
          % (time.time() - T0, N_CHK, len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else "",
             ",".join(KILLS) if KILLS else "none"))
    return 0 if not FAILS else 1


if __name__ == "__main__":
    raise SystemExit(main())
