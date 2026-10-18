#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""gauss_node_unitary_probe -- PRIME.CONTRACTOR.GAUSSNODE.01
(EXPLORATION ONLY, experiments/; round 33 evening, probe 3
follow-up, after CHRISTOFFEL-PARTIAL, 2026-08-08).

THE QUESTION: rebuild C = D_- U D_+ at the Gauss nodes of the
source Jacobi chain, where the grid's 2x-oversampling (the
sqrt2 over-normalization) disappears -- is the transition now
genuinely (partially) unitary, are the diagonals still
contractive, and does the pole-port share sharpen?

THE ALGEBRA, DERIVED BEFORE RUNNING (frozen predictions):
with the polynomial bridge S = phase . sin(th/2) .
P_{h-1}(cos th) (verified 2e-13 in the Christoffel probe) and
nu~_{+-} the sin^2-modified arm measures:

  (P1) GAUSS TIGHTNESS: the h-point Gauss rule of nu~_+ is
       exact to degree 2h-1 >= 2h-2 = deg(S . S~), so
       B_+^G := diag(sqrt(w^S)) F(th^G) satisfies
       (B_+^G)^H B_+^G = G_+ EXACTLY -- an exact square tight
       frame; consequently the Gauss-Christoffel identity
       w_g^S K_+(th_g, th_g) = 1 holds and D_+^G = I EXACTLY.
  (P2) MINUS-ARM RANK: the negative arm is rank-deficient
       (grid census: rank 104 at kz 9 = #negative fold pairs
       < h) -- the minus Gauss system terminates at the folded
       support itself (an N-point Gauss rule of an N-point
       measure IS the measure).  U^G is r_- x h.  Fold
       aggregation DOUBLES the interior masses:
       (D_-^G)^2 = 2 mu K at interior pairs -- the grid's
       0.70 becomes ~0.98: the domination is razor-thin in
       the clean frame; the honest decisive measurement.
  (P3) ROWS: lam_g^- K_+(th_g, th_g) = 1 gives EXACTLY unit
       rows of U^G and ||U^G||_F^2 = r_-.  U^G (U^G)^H has
       unit diagonal; its off-diagonal is the Christoffel-
       normalized PLUS kernel between MINUS nodes.  Exact
       co-isometry (the certificate) would require the minus
       nodes to lie in the plus measure's quasi-orthogonal
       (Gauss-tight) node family -- a cross-measure
       alignment that is NOT automatic: the sharpened
       premise.  The probe measures the deviation.
  (P4) BRIDGE LOSSLESS BY THEOREM: (B_-^G)^H B_-^G = G_-
       exactly, so sigma(C^G) = sigma(C_grid) (both =
       sqrt eig(G_+^{-1} G_-)) and tau is preserved.
  (P5) FRAME INVARIANCE OF THE PORT: u^G = B_+^G G_+^{-1/2}
       e_soft with B_+^G G_+^{-1/2} UNITARY, hence
       |<u^G, p^G>| = beta EXACTLY: the pole share can
       neither sharpen nor delocalize under a frame change --
       the 84-86% is frame-independent; the remainder is the
       bulk admittance of the kappa law.

VERDICT (frozen): GAUSS-UNITARY-ASSEMBLES /
GAUSS-UNITARY-BRIDGE-LOSSY / GAUSS-STILL-DEFECTIVE.
NO RH claim; writes nothing; v563 READ-ONLY.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/gauss_node_unitary_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.CONTRACTOR.GAUSSNODE.01 spec v1 (2026-08-08, frozen
before run).  Machinery = christoffel_transition build_rung
verbatim; ladder = ALL frame_a_zones with h <= 900; heavy
rungs {9, 12, 13, 26, 40}; anchors {9, 12, 13}.  ARM GAUSS
SYSTEMS per rung: fold-aggregate each arm's sin^2-modified
measure nu~_{+-} on x = cos th; if #support(nu~) > h: h-step
Lanczos chain (full reorth twice) -> Gauss nodes/weights
(typed FAIL if breakdown < h); else: nodes = support, weights
= masses (measure-tight, typed).  Frame: w^S = w_gauss /
(4 sin^2(th/2)); B^G = diag(sqrt(w^S)) F(th); zero-weight
folds dropped.  Objects: Zp/Zm = F(th^{+-}) G_+^{-1/2},
Kdiag, lam = 1/Kdiag, U^G = Lam_-^{1/2} Zm Zp^H Lam_+^{1/2},
D_-^G = sqrt(w^S_- Kdiag_-), D_+^G = sqrt(w^S_+ Kdiag_+),
C^G = diag(sqrt(w^S_-)) Zm Zp^H diag(sqrt(w^S_+)) (the
SourceContractor formula transported).  GATE WARDS: W1
tightness ||(B^G)^H B^G - G||_F/||G||_F <= 1e-8 both arms,
every rung; W2 Gauss-Christoffel max|w^S_+ Kdiag_+ - 1| <=
1e-8 (== D_+^G = I) every rung; W3 rows max|row(U^G)-1| <=
1e-8 and ||U^G||_F^2 = r_- rel <= 1e-10 every rung; W4 at
heavy rungs: Douglas cross ||C^G - B_-^G pinv(B_+^G)||_F/
||C^G||_F <= 1e-8 AND sigma-spectrum match vs grid Cres (all
sigma > 1e-8 sigma_max, rel <= 1e-6); W5 bridge/tau every
rung: |sigma_max(C^G)^2 - (1 - lam1(Delta))| <= max(1e-10,
lam1/10) (kill bar = BRIDGE-LOSSY); W6 port frame invariance
| |<u^G, p^G>| - beta | <= 1e-6 every rung (P5; delocalize
kill if breached).  MEASUREMENTS: unitarity certificate
cert = max_g |sigma_g(U^G)^2 - 1| = ||U^G(U^G)^H - I||_2 per
rung (full SVD, values); heavy: sigma census, off-diagonal
structure of U^G(U^G)^H (max |offdiag|, nearest-neighbor
profile vs node separation); D_-^G profile (max, argmax tau,
margin) per rung; payoff product max(D_-^G) sigma_max(U^G)
max(D_+^G) vs ||C|| vs 1 census; soft-mode localization: IPR
of u^G vs grid u_C (descriptive).  REGRESSIONS (gate):
beta(kz9) in [0.59, 0.63], ladder max beta in [0.80, 0.88];
grid ||C|| = sqrt(1 - lam1) reproduced.  S5 controls at kz 9:
Epstein (x^2+5y^2, N = floor(e^{2 alpha9})+1) and scramble
seed 1 through the same Gauss pipeline; bars: lam1 < 0
(||C^G|| > 1) AND the triple (max D_-^G, sigma_max(U^G),
cert) differs from truth by >= 5 percent in >= 1 component.
VERDICT: GAUSS-STILL-DEFECTIVE iff any gate ward fails OR
(cert > 1e-6 anywhere or max D_-^G > 1 + 1e-9 anywhere; the
breaching factor typed with magnitude and location);
GAUSS-UNITARY-ASSEMBLES iff gates pass AND cert <= 1e-6 all
rungs AND max D_-^G <= 1 + 1e-9 all rungs AND W5 holds;
GAUSS-UNITARY-BRIDGE-LOSSY iff cert + D bars pass but W5
fails.  The payoff/hypothesis statement printed either way
with each piece's measured status.  Float64; budget ~15 min.
NO RH claim; writes nothing.
"""

HEAVY = (9, 12, 13, 26, 40)
ANCHORS = (9, 12, 13)
BETA_KZ9 = (0.59, 0.63)
BETA_MAX = (0.80, 0.88)
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan(banned):
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


# ------------------------------------------------ Krein machinery (verbatim)
def odd_extend_mat(h):
    E = np.zeros((2 * h, h))
    E[:h] = np.eye(h)
    E[h:] = -np.eye(h)[::-1]
    return E


def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps(N):
    r = np.zeros(N + 1)
    s = int(math.isqrt(N)) + 1
    for x in range(-s, s + 1):
        for y in range(-s, s + 1):
            v = x * x + 5 * y * y
            if 1 <= v <= N:
                r[v] += 1.0
    a = r / 2.0
    lam = np.zeros(N + 1)
    for n in range(2, N + 1):
        acc = a[n] * math.log(n)
        for dd in range(2, n):
            if n % dd == 0:
                acc -= lam[dd] * a[n // dd]
        lam[n] = acc
    return lam


def build_rung(kz, scramble_seed=None, comb=None):
    """Grid-frame source data (christoffel probe verbatim)."""
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    Ktoe = core.odd_toeplitz(c_ar + c_at, M)
    L = 2 * (2 * h) - 2
    E = odd_extend_mat(h)
    F = np.fft.fft(np.vstack([E, np.zeros((L - M, h))]), axis=0)
    dp = np.sqrt(np.maximum(d, 0.0) / (2.0 * L))
    dm = np.sqrt(np.maximum(-d, 0.0) / (2.0 * L))
    Bp = dp[:, None] * F
    Bm = dm[:, None] * F
    U, s, Vh = np.linalg.svd(Bp, full_matrices=False)
    rk = int(np.sum(s > 1e-12 * s[0]))
    Cf = (Bm @ (Vh[:rk].conj().T / s[:rk])) @ U[:, :rk].conj().T
    pos, neg = d > 0.0, d < 0.0
    Cres = Cf[np.ix_(neg, pos)]
    Gp = np.real(Bp.conj().T @ Bp)
    Gm = np.real(Bm.conj().T @ Bm)
    ev, Vp = np.linalg.eigh(Gp)
    Rm = Vp @ np.diag(ev ** -0.5) @ Vp.T
    Rp = Vp @ np.diag(ev ** 0.5) @ Vp.T
    Delta = Rm @ Ktoe @ Rm
    Delta = 0.5 * (Delta + Delta.T)
    jj = np.arange(L)
    tau = np.where(jj <= L // 2, jj, L - jj) * (
        2.0 * math.pi / L) / D
    return dict(rr=rr, d=d, L=L, h=h, D=D, alpha=alpha, F=F,
                Bp=Bp, Bm=Bm, tau=tau, pos=pos, neg=neg,
                Cres=Cres, Gp=Gp, Gm=Gm, Rm=Rm, Rp=Rp,
                Delta=Delta)


# ------------------------------------------------ Gauss-node machinery
def folded_arm_measure(b, arm):
    """The sin^2-modified arm measure nu~ on x = cos th,
    folded pairs aggregated.  arm in {+1, -1}."""
    L = b["L"]
    mask = b["pos"] if arm > 0 else b["neg"]
    jj = np.arange(L)[mask]
    th = 2.0 * math.pi * jj / L
    mu = np.abs(b["d"][mask]) / (2.0 * L)
    wt = mu * 4.0 * np.sin(th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    thu = 2.0 * math.pi * uf / L
    keep = wagg > 0.0
    return np.cos(thu[keep]), wagg[keep], thu[keep]


def lanczos_chain(x, w, n):
    """Lanczos chain (full reorth, twice) of sum w_i
    delta_{x_i}; returns (al, be, m0, steps)."""
    m0 = float(np.sum(w))
    m = len(x)
    Q = np.zeros((m, n))
    Q[:, 0] = np.sqrt(w) / math.sqrt(m0)
    al = np.zeros(n)
    be = np.zeros(max(n - 1, 0))
    steps = n
    for k in range(n):
        z = x * Q[:, k]
        al[k] = float(Q[:, k] @ z)
        z = z - al[k] * Q[:, k]
        if k > 0:
            z = z - be[k - 1] * Q[:, k - 1]
        for _ in range(2):
            z = z - Q[:, :k + 1] @ (Q[:, :k + 1].T @ z)
        if k == n - 1:
            break
        bnorm = float(np.linalg.norm(z))
        if bnorm <= 1e-13 * max(1.0, float(np.max(np.abs(x)))):
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def arm_gauss_system(b, arm):
    """Gauss nodes th^G and frame weights w^S of one arm.
    Returns (th, wS, mode) with mode in {'gauss',
    'measure-tight', 'breakdown'}."""
    xs, ws, thu = folded_arm_measure(b, arm)
    h = b["h"]
    if len(xs) > h:
        al, be, m0, steps = lanczos_chain(xs, ws, h)
        if steps < h:
            return None, None, "breakdown@%d" % steps
        T = np.diag(al)
        if h > 1:
            T += np.diag(be, 1) + np.diag(be, -1)
        evs, V = np.linalg.eigh(T)
        xg = np.clip(evs, -1.0, 1.0)
        wg = m0 * V[0] ** 2
        th = np.arccos(xg)
        wS = wg / (4.0 * np.sin(th / 2.0) ** 2)
        return th, wS, "gauss"
    # measure-tight: the N-point Gauss rule IS the measure
    th = thu
    wS = ws / (4.0 * np.sin(th / 2.0) ** 2)
    return th, wS, "measure-tight"


def eval_frame(th, h):
    """F(th)[g, k] = e^{-i th k} - e^{-i th (2h-1-k)}."""
    k = np.arange(h)
    ph = np.exp(-1j * np.outer(th, k))
    ph2 = np.exp(-1j * np.outer(th, 2 * h - 1 - k))
    return ph - ph2


def gauss_objects(b):
    """The full Gauss-frame factorization of one rung."""
    h = b["h"]
    thp, wSp, modep = arm_gauss_system(b, +1)
    thm, wSm, modem = arm_gauss_system(b, -1)
    if thp is None or thm is None:
        return dict(mode=(modep, modem), fail=True)
    Fp = eval_frame(thp, h)
    Fm = eval_frame(thm, h)
    BpG = np.sqrt(wSp)[:, None] * Fp
    BmG = np.sqrt(wSm)[:, None] * Fm
    Zp = Fp @ b["Rm"]
    Zm = Fm @ b["Rm"]
    Kp = np.sum(np.abs(Zp) ** 2, axis=1)
    Km = np.sum(np.abs(Zm) ** 2, axis=1)
    Knp = Zm @ Zp.conj().T
    U = (1.0 / np.sqrt(Km))[:, None] * Knp \
        * (1.0 / np.sqrt(Kp))[None, :]
    Dp = np.sqrt(wSp * Kp)
    Dm = np.sqrt(wSm * Km)
    CG = np.sqrt(wSm)[:, None] * Knp * np.sqrt(wSp)[None, :]
    # gate quantities
    w1p = float(np.linalg.norm(np.real(BpG.conj().T @ BpG)
                               - b["Gp"]) / np.linalg.norm(
                                   b["Gp"]))
    w1m = float(np.linalg.norm(np.real(BmG.conj().T @ BmG)
                               - b["Gm"]) / max(
                                   np.linalg.norm(b["Gm"]),
                                   1e-300))
    w2 = float(np.max(np.abs(wSp * Kp - 1.0)))
    rown = np.sqrt(np.sum(np.abs(U) ** 2, axis=1))
    w3row = float(np.max(np.abs(rown - 1.0)))
    w3fro = abs(float(np.sum(np.abs(U) ** 2)) - len(thm)) \
        / len(thm)
    return dict(mode=(modep, modem), fail=False, thp=thp,
                thm=thm, wSp=wSp, wSm=wSm, BpG=BpG, BmG=BmG,
                Zp=Zp, Zm=Zm, Kp=Kp, Km=Km, U=U, Dp=Dp, Dm=Dm,
                CG=CG, w1p=w1p, w1m=w1m, w2=w2, w3row=w3row,
                w3fro=w3fro, rminus=len(thm))


def softport(b):
    """Pole-port quantities (kappa-probe conventions)."""
    h = b["h"]
    v = np.exp(0.5 * np.arange(h) * b["D"])
    v = v / np.linalg.norm(v)
    w = b["Rp"] @ v
    w = w / np.linalg.norm(w)
    lam, W = np.linalg.eigh(b["Delta"])
    esoft = W[:, 0]
    beta = float(abs(w @ esoft))
    return dict(v=v, beta=beta, lam1=float(lam[0]),
                lam2=float(lam[1]), esoft=esoft,
                normC=math.sqrt(max(0.0, 1.0 - float(lam[0]))))


def ipr(u):
    a = np.abs(u) ** 2
    a = a / np.sum(a)
    return float(1.0 / np.sum(a ** 2))


# ================================================================= main
def main():
    section("PRIME.CONTRACTOR.GAUSSNODE.01 (EXPLORATION ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean (no zero/prime oracles)",
          not ast_scan(BANNED_IDS))

    zones = list(core.frame_a_zones())

    section("S1-S4 ladder pass (all frame_a_zones, h <= 900)")
    rows = []
    heavy_data = {}
    skipped = []
    modes = set()
    print("    kz    h    r-   ||C||   maxD-G  sigmax  cert"
          "      tauerr    beta   shr-beta  prod")
    for kz in zones:
        b = build_rung(kz)
        if b["h"] > 900:
            skipped.append(kz)
            continue
        go = gauss_objects(b)
        if go["fail"]:
            check("S1.x kz %d Gauss system FAILED (%s)"
                  % (kz, go["mode"]), False)
            continue
        modes.add(go["mode"])
        sp = softport(b)
        sv = np.linalg.svd(go["U"], compute_uv=False)
        cert = float(np.max(np.abs(sv ** 2 - 1.0)))
        svC = np.linalg.svd(go["CG"], compute_uv=False)
        tauerr = abs(float(svC[0]) ** 2
                     - (1.0 - sp["lam1"]))
        # port frame invariance
        uG = go["BpG"] @ (b["Rm"] @ sp["esoft"])
        pG = go["BpG"] @ sp["v"]
        share = float(abs(np.vdot(uG, pG))
                      / (np.linalg.norm(uG)
                         * np.linalg.norm(pG)))
        r = dict(kz=kz, h=b["h"], rminus=go["rminus"],
                 normC=sp["normC"], normCG=float(svC[0]),
                 maxDm=float(np.max(go["Dm"])),
                 maxDp=float(np.max(go["Dp"])),
                 sig=float(sv[0]), sigmin=float(sv[-1]),
                 cert=cert, tauerr=tauerr, lam1=sp["lam1"],
                 beta=sp["beta"], share=share,
                 sharedev=abs(share - sp["beta"]),
                 w1=max(go["w1p"], go["w1m"]), w2=go["w2"],
                 w3=max(go["w3row"], go["w3fro"]),
                 uG=None,
                 prod=float(np.max(go["Dm"])) * float(sv[0])
                 * float(np.max(go["Dp"])))
        rows.append(r)
        if kz in HEAVY:
            heavy_data[kz] = (b, go, sp, sv, uG)
        print("    %-5d %-4d %-4d %.4f  %.4f  %.4f  %.2e"
              "  %.2e  %.3f  %.1e   %.4f"
              % (kz, r["h"], r["rminus"], r["normC"],
                 r["maxDm"], r["sig"], cert, tauerr,
                 r["beta"], r["sharedev"], r["prod"]),
              flush=True)
    if skipped:
        print("    skipped (h > 900): %s" % skipped)
    print("    arm modes seen: %s" % sorted(modes))

    # ---------------- S1 frame wards
    section("S1 -- the Gauss-node frame: gate wards")
    w1max = max(r["w1"] for r in rows)
    check("S1.1 [W1 TIGHTNESS] (B^G)^H B^G == G both arms, "
          "every rung (max rel %.2e; P1/P2 quadrature "
          "exactness)" % w1max, w1max <= 1e-8)
    w2max = max(r["w2"] for r in rows)
    check("S1.2 [W2 GAUSS-CHRISTOFFEL] w^S K = 1 at the plus "
          "Gauss nodes, every rung (max dev %.2e; == D_+^G = "
          "I)" % w2max, w2max <= 1e-8)
    w3max = max(r["w3"] for r in rows)
    check("S1.3 [W3 ROWS] unit rows of U^G and ||U^G||_F^2 = "
          "r_- (max dev %.2e; P3)" % w3max, w3max <= 1e-8)
    rm_frac = [r["rminus"] / r["h"] for r in rows]
    print("    minus-arm rank r_-/h over ladder: [%.3f, %.3f] "
          "(P2: the negative arm is a strict compression)"
          % (min(rm_frac), max(rm_frac)))

    # ---------------- S2 the U^G spectrum
    section("S2 -- the transition U^G: unitarity")
    cert_all = max(r["cert"] for r in rows)
    cert_ok = cert_all <= 1e-6
    print("    unitarity certificate max_g |sigma_g^2 - 1| "
          "over ladder: [%.3e, %.3e]; bar 1e-6: %s"
          % (min(r["cert"] for r in rows), cert_all,
             "MET" if cert_ok else "BREACHED"))
    for kz in HEAVY:
        b, go, sp, sv, uG = heavy_data[kz]
        n1m3 = int(np.sum(np.abs(sv - 1.0) <= 1e-3))
        n1m6 = int(np.sum(np.abs(sv - 1.0) <= 1e-6))
        gram = go["U"] @ go["U"].conj().T
        off = gram - np.diag(np.diag(gram))
        offmax = float(np.max(np.abs(off)))
        gi, gj = np.unravel_index(int(np.argmax(np.abs(off))),
                                  off.shape)
        sep = abs(go["thm"][gi] - go["thm"][gj]) / b["D"]
        # nearest-neighbour coherence profile
        nnv = [abs(off[i, i + 1]) for i
               in range(len(go["thm"]) - 1)]
        print("    kz %-3d: sigma in [%.6f, %.6f], #|s-1|<="
              "1e-3: %d/%d, <=1e-6: %d; max|offdiag "
              "UU^H| = %.2e at dtau %.3f; NN coherence "
              "med/max = %.2e/%.2e"
              % (kz, sv[-1], sv[0], n1m3, len(sv), n1m6,
                 offmax, sep, float(np.median(nnv)),
                 float(np.max(nnv))))

    # ---------------- S3 the diagonals + payoff product
    section("S3 -- the diagonals D_+-^G and the payoff product")
    dp_all = max(r["maxDp"] for r in rows)
    dm_all = max(r["maxDm"] for r in rows)
    dminus_ok = dm_all <= 1.0 + 1e-9
    print("    max D_+^G over ladder: %.12f (theorem: = 1 "
          "exactly)" % dp_all)
    print("    max D_-^G over ladder: %.6f -- %s"
          % (dm_all, "CONTRACTIVE, min margin %.2e"
             % (1.0 - dm_all) if dminus_ok else
             "EXCEEDS 1 by %.2e (the domination breaks in "
             "the clean frame)" % (dm_all - 1.0)))
    for kz in HEAVY:
        b, go, sp, sv, uG = heavy_data[kz]
        im = int(np.argmax(go["Dm"]))
        print("    kz %-3d: max D_-^G = %.6f at tau = %.3f "
              "(grid maxD- was ~%.3f; fold doubling P2); "
              "D_-^G quantiles q50/q90 = %.4f/%.4f"
              % (kz, go["Dm"][im], go["thm"][im] / b["D"],
                 go["Dm"][im] / math.sqrt(2.0),
                 float(np.quantile(go["Dm"], 0.5)),
                 float(np.quantile(go["Dm"], 0.9))))
    ncert = sum(1 for r in rows if r["prod"] <= 1.0)
    worst = max(rows, key=lambda r: r["prod"])
    print("    payoff product max(D_-^G) sigmax(U^G) "
          "max(D_+^G) <= 1 on %d/%d rungs (max %.6f at kz %d;"
          " ||C|| there %.6f, excess %.2e)"
          % (ncert, len(rows), worst["prod"], worst["kz"],
             worst["normC"], worst["prod"] - 1.0))

    # ---------------- S4 bridge + soft mode
    section("S4 -- bridge consistency and the soft mode")
    tau_ok = all(r["tauerr"] <= max(1e-10, r["lam1"] / 10.0)
                 for r in rows)
    tau_worst = max(rows, key=lambda r: r["tauerr"])
    check("S4.1 [W5 BRIDGE/TAU] |sigmax(C^G)^2 - (1-lam1)| "
          "<= max(1e-10, tau/10) every rung (worst %.2e at "
          "kz %d, tau there %.2e)"
          % (tau_worst["tauerr"], tau_worst["kz"],
             tau_worst["lam1"]), tau_ok)
    w4_ok = True
    for kz in HEAVY:
        b, go, sp, sv, uG = heavy_data[kz]
        Cd = go["BmG"] @ np.linalg.pinv(go["BpG"])
        relD = float(np.linalg.norm(Cd - go["CG"])
                     / np.linalg.norm(go["CG"]))
        svG = np.linalg.svd(go["CG"], compute_uv=False)
        svg = np.linalg.svd(b["Cres"], compute_uv=False)
        nsig = int(np.sum(svg > 1e-8 * svg[0]))
        nsig = min(nsig, len(svG))
        smrel = float(np.max(np.abs(svG[:nsig] - svg[:nsig])
                             / svg[:nsig]))
        w4_ok &= relD <= 1e-8 and smrel <= 1e-6
        print("    kz %-3d: Douglas cross %.2e; sigma-spectrum"
              " match vs grid Cres over %d values: max rel "
              "%.2e" % (kz, relD, nsig, smrel))
    check("S4.2 [W4 DEPLOYED-C REPRODUCTION] C^G = Douglas "
          "form and sigma(C^G) == sigma(C_grid) at heavy "
          "rungs", w4_ok)
    shr_max = max(r["sharedev"] for r in rows)
    check("S4.3 [W6 PORT FRAME-INVARIANCE] |share - beta| <= "
          "1e-6 every rung (max dev %.2e; P5: the pole share "
          "neither sharpens nor delocalizes)" % shr_max,
          shr_max <= 1e-6)
    b9 = next(r for r in rows if r["kz"] == 9)
    bmax = max(rows, key=lambda r: r["beta"])
    beta_ok = (BETA_KZ9[0] <= b9["beta"] <= BETA_KZ9[1]
               and BETA_MAX[0] <= bmax["beta"] <= BETA_MAX[1])
    check("S4.4 [SOFTPORT REGRESSION] beta(kz9) = %.4f, "
          "ladder max = %.4f at kz %d"
          % (b9["beta"], bmax["beta"], bmax["kz"]), beta_ok)
    for kz in ANCHORS:
        b, go, sp, sv, uG = heavy_data[kz]
        uCgrid = b["Bp"][b["pos"]] @ (b["Rm"] @ sp["esoft"])
        print("    kz %-3d: soft-mode IPR: grid %d bins -> "
              "%.1f eff; Gauss %d nodes -> %.1f eff (share = "
              "beta = %.4f in both frames)"
              % (kz, int(np.sum(b["pos"])), ipr(uCgrid),
                 len(go["thp"]), ipr(uG), sp["beta"]))

    # ---------------- S5 controls
    section("S5 -- controls at kz 9 (Epstein x^2+5y^2, "
            "scramble seed 1)")
    rt = next(r for r in rows if r["kz"] == 9)
    triple_t = np.array([rt["maxDm"], rt["sig"], rt["cert"]])
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        bc = build_rung(9, **kw)
        gc = gauss_objects(bc)
        sc = softport(bc)
        if gc["fail"]:
            print("    %-8s: Gauss system failed (%s) -- "
                  "typed as maximal discrimination"
                  % (nmc, gc["mode"]))
            ctrl_ok &= sc["lam1"] < 0.0
            continue
        svc = np.linalg.svd(gc["U"], compute_uv=False)
        certc = float(np.max(np.abs(svc ** 2 - 1.0)))
        triple_c = np.array([float(np.max(gc["Dm"])),
                             float(svc[0]), certc])
        reldiff = np.abs(triple_c - triple_t) \
            / np.maximum(triple_t, 1e-12)
        ctrl_ok &= (sc["lam1"] < 0.0
                    and bool(np.max(reldiff) >= 0.05))
        print("    %-8s: lam1 = %+.4e (||C|| = %.4f); "
              "(maxD-G, sigmax, cert) = (%.4f, %.4f, %.2e) "
              "vs truth (%.4f, %.4f, %.2e); max rel diff "
              "%.1f%%"
              % (nmc, sc["lam1"],
                 math.sqrt(max(0.0, 1.0 - sc["lam1"])),
                 *triple_c, *triple_t,
                 100.0 * float(np.max(reldiff))))
    check("S5.1 [DISCRIMINATOR CARRY-OVER] both controls "
          "break the sign AND the Gauss-frame triple differs "
          "by >= 5%", ctrl_ok)

    # ---------------- verdict
    section("V -- FROZEN VERDICT + the payoff statement")
    gates_ok = (w1max <= 1e-8 and w2max <= 1e-8
                and w3max <= 1e-8 and w4_ok
                and shr_max <= 1e-6 and beta_ok and ctrl_ok)
    if gates_ok and cert_ok and dminus_ok and tau_ok:
        verdict = "GAUSS-UNITARY-ASSEMBLES"
        typed = ("unitary core certified + contractive "
                 "diagonals + scalar port")
    elif gates_ok and cert_ok and dminus_ok and not tau_ok:
        verdict = "GAUSS-UNITARY-BRIDGE-LOSSY"
        typed = "tau error %.2e at kz %d" % (
            tau_worst["tauerr"], tau_worst["kz"])
    else:
        verdict = "GAUSS-STILL-DEFECTIVE"
        bad = []
        if not gates_ok:
            bad.append("gate wards: %s" % sorted(set(FAILS)))
        if not cert_ok:
            wc = max(rows, key=lambda r: r["cert"])
            bad.append("U^G co-isometry defect %.3e (kz %d; "
                       "sigma in [%.4f, %.4f] there) -- the "
                       "cross-measure node alignment (P3) "
                       "does not hold"
                       % (wc["cert"], wc["kz"], wc["sigmin"],
                          wc["sig"]))
        if not dminus_ok:
            wd = max(rows, key=lambda r: r["maxDm"])
            bad.append("D_-^G max %.6f > 1 at kz %d (fold-"
                       "doubled domination breaks)"
                       % (wd["maxDm"], wd["kz"]))
        typed = "; ".join(bad)
    print("\n  VERDICT: %s" % verdict)
    print("  typed: %s" % typed)

    print("\n  THE PAYOFF STATEMENT (each piece's measured "
          "status):")
    print("    ||C|| <= max(D_-^G) . sigma_max(U^G) . "
          "max(D_+^G)")
    print("    - D_+^G = I: EXACT (Gauss-Christoffel, ward "
          "%.1e)" % w2max)
    print("    - max D_-^G: %.6f (%s)"
          % (dm_all, "<= 1: measured, discriminating"
             if dminus_ok else "> 1: NOT certified"))
    print("    - sigma_max(U^G): %.6f, co-isometry defect "
          "%.3e (%s)"
          % (max(r["sig"] for r in rows), cert_all,
             "certificate grade" if cert_ok else
             "NOT unitary -- typed above"))
    print("    - product census: <= 1 on %d/%d rungs"
          % (ncert, len(rows)))
    print("    - port scalar: beta in [%.3f, %.3f] "
          "(frame-invariant, ward %.1e); remainder = bulk "
          "admittance (kappa law)"
          % (min(r["beta"] for r in rows),
             max(r["beta"] for r in rows), shr_max))
    print("    NAMED HYPOTHESES a theorem would need:")
    print("    (H-D) uniform sup_kz max_g w^S_g "
          "K_+(th_g,th_g) <= 1 - delta on the minus nodes "
          "[measured: sup = %.6f]" % dm_all)
    print("    (H-U) uniform sigma_max(U^G) <= 1 + eps with "
          "(1-delta)(1+eps) <= 1 [measured: sup = %.6f]"
          % max(r["sig"] for r in rows))
    print("    (H-PORT) the kappa scalar s > 0 uniformly "
          "(pole-port Feshbach premise) [beta series above]")

    npass = sum(1 for _, ok in CHECKS if ok)
    print("\n  checks: %d/%d passed; elapsed %.1f s"
          % (npass, len(CHECKS), time.time() - T0))
    print("""
HONEST CONSEQUENCE (no RH claim):
  the Gauss frame removes the sqrt2 over-normalization by
  construction (D_+^G = I exact, unit rows exact) and
  preserves the full Krein content (sigma spectra match, tau
  lossless by quadrature exactness).  What it cannot do by
  algebra: sharpen the pole share (frame invariance P5) or
  decide the cross-measure alignment (P3) -- the latter is
  the measured content of this run.  EXPLORATION ONLY;
  nothing here enters verification/ or the papers.""")
    return verdict


if __name__ == "__main__":
    main()
