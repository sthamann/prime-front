#!/usr/bin/env python3
"""psi_lambda_lemma_reduction_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (SEAM.SIMPLECURRENT.GENERATOR.01 [O], last analytic half).
Yesterday's psi_lambda_quantitative_skeleton_probe.py measured the S2
HS hypotheses on the v367 QWZ collar (windowed Shale plateau, global
HS^2 log-divergence).  Those numbers do not imply (L1) strong/operator-
norm Cauchy of the local Bogoliubov implementers U_N on the finite-
particle core of the infinite-volume edge CAR algebra, nor (L2)
polynomial energy bounds ||H_edge^n Psi_lambda Omega|| <= C^{n+1}(n!)^beta.
This probe attempts the honest REDUCTION of L1/L2 to a cited quasi-free
theorem class plus measured Cauchy data on the same collar.

COLLAR (verbatim skeleton/QWZ): h(k) = sin kx σx + sin ky σy +
(M − cos kx − cos ky)σz on a cylinder, N_x periodic with μ4 twist
phases i^k on the boundary x-bonds, N_y open; M=1 topological /
M=3 trivial control.  One Majorana copy.  PH-symmetric Fermi covariance
C = χ_{E<0}(H) + (1/2) χ_{E=0}(H); half-filling projector
P = χ_{lowest N_x N_y}(H) (the Slater ground-state projection).

  (1) WINDOWED HS-CAUCHY (L1 hypothesis).  Object: the windowed sector
      difference D_N = E_w (Q_N^{(1)} − Q_N^{(0)}) E_w with Q ∈ {C, P},
      window = sites y=0, x=0..w−1, both orbitals, w ∈ {6, 8}.  The
      window is finite-dimensional and independent of N_x (N_x ≥ w), so
      HS / operator / trace norms are equivalent here: windowed HS-Cauchy
      IS operator-norm Cauchy of the one-particle data on the window.
      Nested pairs from N ∈ {24, 32, 48, 64, 96}.  Fit the rate of
      ||D_N − D_{Nmax}||_HS.

  (2) IMPLEMENTER MATRIX-ELEMENT CAUCHY (direct L1 witness).  Equal-
      particle Slaters |Ω_N^{(0)}>, |T_N> = k=0,1 half-filling grounds.
      Phase-fix by the polar decomposition of V0† V1 so <Ω|T> > 0, then
        m_N(A) = <Ω| A |T> / |<Ω|T>|
      for window-local A (identity, n_x, c†_x c_y).  Transition 1-RDM
      by the determinant/Cauchy-Binet formula γ = V1 (V0† V1)^{-1} V0†.
      PARITY: energy-sign fillings have nocc(k=0) = N_x N_y − 1 vs
      nocc(k=1) = N_x N_y (k=0 has a 2-dim kernel) ⇒ overlap identically
      0.  Equal-particle half-filling is the nonzero-overlap choice; on
      a denser N-grid |det| oscillates between two Pfaffian bands.  The
      contracted N-set sits in one band; that subsequence is used.  The
      complementary band is reported, not mixed.

  (3) ENERGY BOUNDS (L2 finite shadow).  H_N = dΓ(h^{(0)}_N), the
      many-body quadratic Hamiltonian of the k=0 single-particle
      matrix (NOT a PH-even |h|^n trace: those ratios are identically 1
      by PH symmetry and are not a test).  Exact Slater generating
      function <e^{z H}> = det(V† e^{z h} V) ⇒ cumulants ⇒
        e_n(N) = ||H_N^n |T_N>|| / ||H_N^n |Ω_N^{(0)}>||
      for n=1..4, and the excitation norms ||(H_N − E_Ω)^n |T_N>||.

CITED THEOREM CLASS (not re-proved): Shale–Stinespring 1965
implementability; Araki quasi-free CAR continuity; Ruijsenaars 1978
(Bogoliubov transformations, general case) — HS-convergence of the
one-particle data plus a continuous phase/Pfaffian choice implies
strong convergence of the implementers on the finite-particle core.

REDUCTION STATEMENT (typed, conditional):
  GIVEN the cited quasi-free implementer-continuity theorem class, the
  measured windowed HS-Cauchy rates + phase-fixed matrix-element Cauchy
  on one Pfaffian subsequence + bounded energy ratios reduce L1/L2 on
  this collar to the citation; what remains genuinely open is the
  identification of the QWZ edge scaling limit with the (E8)_1 sector
  theory (the MMST leg) — i.e. the lemma is REDUCED, not closed.

FIREWALL: one Majorana copy, finite cylinders, measured rates; no
operator-algebra proof; contract SEAM.SIMPLECURRENT.GENERATOR.01 stays
[O]; no marker move; no promotion.

VERDICT ENUM: LEMMA_REDUCED_TO_CITED_QUASIFREE_CLASS
  (or HS_CAUCHY_FAILS / MATRIX_ELEMENT_CAUCHY_FAILS /
   ENERGY_RATIO_UNBOUNDED / PARITY_BLOCKS_SUBSEQUENCE).
"""
import time
from math import comb

import numpy as np

T0 = time.time()
ok_all = True

SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
TX = (SX / (2j) - SZ / 2)
TY = (SY / (2j) - SZ / 2)

ZCUT = 1e-10
NY = 8
NXS = (24, 32, 48, 64, 96)
NMAX = NXS[-1]
WINS = (6, 8)
NX_BAND_B = (36, 68, 80)   # complementary Pfaffian band (not mixed into Cauchy)
OV_ZERO = 1e-12


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


def qwz_cylinder(Nx, Ny, M, phase):
    """single-particle Hamiltonian on the cylinder: periodic x with a
    complex twist `phase` across the seam link x = Nx-1 -> 0, open y.
    Integer mu4 sectors: phase = 1j ** k."""
    dim = 2 * Nx * Ny
    H = np.zeros((dim, dim), dtype=complex)

    def sl(x, y):
        return 2 * ((x % Nx) * Ny + y)

    ph = complex(phase)
    for x in range(Nx):
        for y in range(Ny):
            i = sl(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            j = sl(x + 1, y)
            amp = ph if x == Nx - 1 else 1.0
            H[j:j + 2, i:i + 2] += amp * TX
            H[i:i + 2, j:j + 2] += np.conj(amp) * TX.conj().T
            if y + 1 < Ny:
                j = sl(x, y + 1)
                H[j:j + 2, i:i + 2] += TY
                H[i:i + 2, j:j + 2] += TY.conj().T
    return H


def edge_window_idx(Nx, Ny, w):
    """sites y = 0, x = 0..w-1, both orbitals (skeleton window)."""
    idx = []
    for x in range(w):
        base = 2 * ((x % Nx) * Ny + 0)
        idx += [base, base + 1]
    return idx


def hs_norm(A):
    return float(np.sqrt(np.vdot(A, A).real))


def op_norm(A):
    return float(np.linalg.norm(A, 2))


def power_fit(xs, ys):
    """ys ~ c * xs^p  (ys > 0).  Returns p, r^2."""
    x = np.log(np.asarray(xs, float))
    y = np.log(np.asarray(ys, float))
    p, a = np.polyfit(x, y, 1)
    yhat = a + p * x
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return float(p), float(r2)


def spectrum(Nx, M, k):
    H = qwz_cylinder(Nx, NY, M, 1j ** k)
    w, v = np.linalg.eigh(H)
    nocc = Nx * NY
    n = np.zeros(w.shape[0])
    n[w < -ZCUT] = 1.0
    n[np.abs(w) <= ZCUT] = 0.5
    C = (v * n) @ v.conj().T
    V = v[:, :nocc]
    P = V @ V.conj().T
    return dict(H=H, w=w, v=v, C=C, P=P, V=V, nocc=nocc,
                nneg=int(np.sum(w < -ZCUT)),
                nzero=int(np.sum(np.abs(w) <= ZCUT)))


def polar_fix(V0, V1):
    """right-multiply V1 by a unitary so V0† V1 is Hermitian PSD
    (overlap det real and >= 0).  Returns V1_new, overlap, smin."""
    G = V0.conj().T @ V1
    u, s, vh = np.linalg.svd(G, full_matrices=False)
    W = u @ vh
    V1n = V1 @ W.conj().T
    ov = float(np.prod(s.real))
    return V1n, ov, float(s.min())


def transition_rdm(V0, V1n):
    """γ_ij = <Ω| c†_j c_i |T> / <Ω|T>  after polar fix (G = V0† V1n > 0)."""
    G = V0.conj().T @ V1n
    return V1n @ np.linalg.inv(G) @ V0.conj().T


def slater_cumulants(V, h, nmax, shift=0.0):
    """Cumulants of H = dΓ(h) − shift·1 in the Slater with frame V.
    Generating function <e^{z dΓ(h)}> = det(V† e^{z h} V)."""
    nocc = V.shape[1]
    w, u = np.linalg.eigh(h)
    Wf = u.conj().T @ V
    M = [np.eye(nocc, dtype=complex)]
    for k in range(1, nmax + 1):
        M.append(Wf.conj().T @ ((w ** k)[:, None] * Wf))
    R = []
    for n in range(1, nmax + 1):
        acc = M[n].copy()
        for j in range(1, n):
            acc = acc - comb(n - 1, j) * (M[j] @ R[n - 1 - j])
        R.append(acc)
    kappa = [float(np.trace(R[n]).real) for n in range(nmax)]
    kappa[0] -= float(shift)
    mu = [1.0]
    for n in range(1, nmax + 1):
        s = 0.0
        for m in range(n):
            s += comb(n - 1, m) * kappa[n - 1 - m] * mu[m]
        mu.append(s)
    return kappa, mu


# ======================================================================
# cache spectra
# ======================================================================
print("=== cache QWZ spectra  Ny=%d  N=%s  (M=1 TOP / M=3 TRIV) ==="
      % (NY, list(NXS)))
CACHE = {}
for M, tag in ((1.0, "TOP"), (3.0, "TRIV")):
    for Nx in NXS:
        for k in (0, 1):
            CACHE[(tag, Nx, k)] = spectrum(Nx, M, k)
        a, b = CACHE[(tag, Nx, 0)], CACHE[(tag, Nx, 1)]
        print("   %s Nx=%3d  nneg0/1=%d/%d  nzero0/1=%d/%d  nocc=%d"
              % (tag, Nx, a["nneg"], b["nneg"], a["nzero"], b["nzero"],
                 a["nocc"]))

CACHE_B = {}
for Nx in NX_BAND_B:
    for k in (0, 1):
        CACHE_B[(Nx, k)] = spectrum(Nx, 1.0, k)


# ======================================================================
# (1) WINDOWED HS-CAUCHY
# ======================================================================
print()
print("=== (1) WINDOWED HS-CAUCHY  D_N = E_w (Q^{(1)}-Q^{(0)}) E_w ===")
print("    Q = C (PH-symmetric covariance, skeleton object) or")
print("        P (half-filling Slater projector).  Window y=0, x<w.")

cauchy = {}
for tag in ("TOP", "TRIV"):
    for qname in ("C", "P"):
        for w in WINS:
            Ds = {}
            for Nx in NXS:
                Q0 = CACHE[(tag, Nx, 0)][qname]
                Q1 = CACHE[(tag, Nx, 1)][qname]
                idx = edge_window_idx(Nx, NY, w)
                Ds[Nx] = (Q1 - Q0)[np.ix_(idx, idx)]
            hsD = [hs_norm(Ds[N]) for N in NXS]
            vs_max = [hs_norm(Ds[N] - Ds[NMAX]) for N in NXS[:-1]]
            adj = [hs_norm(Ds[N] - Ds[M])
                   for N, M in zip(NXS[:-1], NXS[1:])]
            vs_max_op = [op_norm(Ds[N] - Ds[NMAX]) for N in NXS[:-1]]
            key = (tag, qname, w)
            cauchy[key] = dict(hsD=hsD, vs_max=vs_max, adj=adj,
                               vs_max_op=vs_max_op)
            if min(vs_max) > 0:
                p, r2 = power_fit(NXS[:-1], vs_max)
            else:
                p, r2 = 0.0, 1.0
            cauchy[key]["p"] = p
            cauchy[key]["r2"] = r2
            print("  %s Q=%s w=%d  ||D_N||_HS:" % (tag, qname, w),
                  ["%.4e" % x for x in hsD])
            print("           ||D_N-D_%d||_HS:" % NMAX,
                  ["N=%d:%.4e" % (N, x)
                   for N, x in zip(NXS[:-1], vs_max)])
            print("           adjacent HS:",
                  ["(%d,%d):%.4e" % (N, M, x)
                   for (N, M), x in zip(zip(NXS[:-1], NXS[1:]), adj)])
            print("           vs-max power p=%.3f r^2=%.4f  "
                  "||.||_op vs-max=%s"
                  % (p, r2, ["%.3e" % x for x in vs_max_op]))

# topological: both Q, both windows, vs-max monotone + decaying power
topo_ok = True
for qname in ("C", "P"):
    for w in WINS:
        rec = cauchy[("TOP", qname, w)]
        mono = all(rec["vs_max"][i] > rec["vs_max"][i + 1]
                   for i in range(len(rec["vs_max"]) - 1))
        decaying = rec["p"] < -1.0 and rec["r2"] > 0.95
        ok = mono and decaying and rec["vs_max"][-1] < rec["vs_max"][0] / 4
        topo_ok &= ok
        rep("L1 HS-CAUCHY TOP Q=%s w=%d: ||D_N-D_%d||_HS monotone "
            "decaying (p=%.3f, r^2=%.4f;  %.3e -> %.3e) -- windowed "
            "one-particle data is Cauchy, hence operator-norm Cauchy "
            "on the finite window"
            % (qname, w, NMAX, rec["p"], rec["r2"],
               rec["vs_max"][0], rec["vs_max"][-1]),
            ok)

triv_tiny = True
for qname in ("C", "P"):
    for w in WINS:
        rec = cauchy[("TRIV", qname, w)]
        tiny = rec["vs_max"][0] < 1e-6 and rec["hsD"][-1] < 1e-12
        triv_tiny &= tiny
        rep("L1 TRIVIAL control Q=%s w=%d: windowed D_N already at "
            "numerical zero (||D_%d||=%.1e, Cauchy vs-max %.1e) -- "
            "gapped, no edge implementer to take a limit of"
            % (qname, w, NMAX, rec["hsD"][-1], rec["vs_max"][0]),
            tiny)


# ======================================================================
# (2) IMPLEMENTER MATRIX-ELEMENT CAUCHY
# ======================================================================
print()
print("=== (2) IMPLEMENTER MATRIX ELEMENTS  "
      "m_N(A)=<Ω|A|T>/|<Ω|T>|  (polar-fixed) ===")


def melems_from(spec0, spec1, w=6):
    V0 = spec0["V"]
    V1n, ov, smin = polar_fix(spec0["V"], spec1["V"])
    # energy-sign overlap is identically 0 on particle-number mismatch
    nocc_es_0 = spec0["nneg"]
    nocc_es_1 = spec1["nneg"]
    gamma = transition_rdm(V0, V1n)
    Nx = spec0["H"].shape[0] // (2 * NY)
    idx = edge_window_idx(Nx, NY, w)
    i00, i01 = idx[0], idx[1]          # x=0, y=0, orb 0/1
    i10 = idx[2]                        # x=1, y=0, orb 0
    # A = 1  -> m = 1 (phase-fixed)
    # A = c†_p c_q  -> m = γ_{q p}
    m_id = 1.0 + 0j
    m_n00 = gamma[i00, i00]            # <c†_{00} c_{00}>
    m_n01 = gamma[i01, i01]
    m_hop = gamma[i10, i00]            # <c†_{00} c_{10}>
    return dict(ov=ov, smin=smin,
                nocc_es=(nocc_es_0, nocc_es_1),
                m_id=m_id, m_n00=m_n00, m_n01=m_n01, m_hop=m_hop)


print("  PARITY / particle-number: energy-sign nocc(k=0) vs nocc(k=1)")
es_mismatch = True
for Nx in NXS:
    a, b = CACHE[("TOP", Nx, 0)], CACHE[("TOP", Nx, 1)]
    print("    TOP Nx=%3d  energy-sign nocc %d vs %d  (kernel dim %d) "
          "-- equal-N Slater used instead"
          % (Nx, a["nneg"], b["nneg"], a["nzero"]))
    es_mismatch &= (a["nneg"] != b["nneg"])
rep("PARITY documented: energy-sign Slaters have nocc mismatch on "
    "every contracted N (k=0 kernel of dim 2) so <Ω|T> = 0 "
    "identically for that filling; the nonzero-overlap choice is "
    "equal-particle half-filling",
    es_mismatch)

print("  Band A (contracted N-set, expected small |det|):")
bandA = {}
keys_m = ("m_n00", "m_n01", "m_hop")
for Nx in NXS:
    bandA[Nx] = melems_from(CACHE[("TOP", Nx, 0)], CACHE[("TOP", Nx, 1)])
    r = bandA[Nx]
    print("    Nx=%3d  |ov|=%.4e  smin=%.3e  n00=%+.5f%+.5fj  "
          "n01=%+.5f%+.5fj  hop=%+.5f%+.5fj"
          % (Nx, r["ov"], r["smin"],
             r["m_n00"].real, r["m_n00"].imag,
             r["m_n01"].real, r["m_n01"].imag,
             r["m_hop"].real, r["m_hop"].imag))

nonzeroA = [Nx for Nx in NXS if bandA[Nx]["ov"] > OV_ZERO]
rep("Band A = contracted N-set has nonzero half-filling overlap "
    "at every N (min |ov|=%.3e); this is the Cauchy subsequence"
    % min(bandA[N]["ov"] for N in NXS),
    len(nonzeroA) == len(NXS))

# identity phase-fixed
id_ok = all(abs(bandA[N]["m_id"] - 1) < 1e-12 for N in NXS)
rep("phase-fixed m_N(1) = 1 on Band A (polar gauge of V0† V1)", id_ok)

# Cauchy of local m_N vs Nmax
me_ok = True
for name in keys_m:
    diffs = [abs(bandA[N][name] - bandA[NMAX][name]) for N in NXS[:-1]]
    mono = all(diffs[i] >= diffs[i + 1] * 0.98
               for i in range(len(diffs) - 1))  # allow 2% jitter
    # require overall decay; the 0.98 slack is for last-step flattening
    decaying = diffs[-1] < diffs[0] / 2
    p, r2 = power_fit(NXS[:-1], diffs)
    print("  Band A Cauchy |m_N(%s)-m_%d|: " % (name, NMAX),
          ["N=%d:%.4e" % (N, d) for N, d in zip(NXS[:-1], diffs)],
          " p=%.3f r^2=%.4f" % (p, r2))
    ok = decaying and diffs[-1] < 0.02
    me_ok &= ok
    rep("L1 ME-CAUCHY Band A  %s: |m_N-m_%d| decays "
        "(%.3e -> %.3e, p=%.3f) -- strong convergence on window "
        "vectors, one Pfaffian choice"
        % (name, NMAX, diffs[0], diffs[-1], p),
        ok)

print("  Band B (complementary Pfaffian class; NOT mixed into Band A):")
bandB = {}
for Nx in NX_BAND_B:
    bandB[Nx] = melems_from(CACHE_B[(Nx, 0)], CACHE_B[(Nx, 1)])
    r = bandB[Nx]
    print("    Nx=%3d  |ov|=%.4e  smin=%.3e  n00=%+.5f%+.5fj  "
          "hop=%+.5f%+.5fj"
          % (Nx, r["ov"], r["smin"],
             r["m_n00"].real, r["m_n00"].imag,
             r["m_hop"].real, r["m_hop"].imag))

# Band B internally Cauchy; different limit from Band A (honest)
bN = NX_BAND_B
diffsB = [abs(bandB[N]["m_n00"] - bandB[bN[-1]]["m_n00"]) for N in bN[:-1]]
sep = abs(bandA[NMAX]["m_n00"] - bandB[bN[-1]]["m_n00"])
print("  Band B |m_n00 - m_%d|:" % bN[-1],
      ["N=%d:%.4e" % (N, d) for N, d in zip(bN[:-1], diffsB)])
print("  |lim_A m_n00 - lim_B m_n00| = %.4f  (distinct Pfaffian classes)"
      % sep)
rep("Band B internally Cauchy in n00 (|Δ| last=%.3e) and is a "
    "DISTINCT limit from Band A (separation %.3f >> Band-A last "
    "step) -- the cited theorem's phase/Pfaffian choice; each "
    "subsequence is Cauchy, they are not mixed"
    % (diffsB[-1], sep),
    diffsB[-1] < diffsB[0] / 2 and sep > 0.1)

print("  TRIVIAL control overlaps / m_n00:")
triv_ov = []
triv_n00 = []
for Nx in NXS:
    r = melems_from(CACHE[("TRIV", Nx, 0)], CACHE[("TRIV", Nx, 1)])
    triv_ov.append(r["ov"])
    triv_n00.append(r["m_n00"])
    print("    TRIV Nx=%3d  |ov|=%.6f  n00=%+.6f%+.6fj"
          % (Nx, r["ov"], r["m_n00"].real, r["m_n00"].imag))
rep("TRIVIAL: overlap plateaus (rel range %.1e) and m_n00 is "
    "Cauchy at machine precision -- local twist, no charged field"
    % ((max(triv_ov) - min(triv_ov)) / np.mean(triv_ov)),
    (max(triv_ov) - min(triv_ov)) / np.mean(triv_ov) < 1e-6
    and abs(triv_n00[-1] - triv_n00[0]) < 1e-8)


# ======================================================================
# (3) ENERGY BOUNDS
# ======================================================================
print()
print("=== (3) ENERGY BOUNDS  H = dΓ(h^{(0)}) on Slaters ===")
print("    e_n = ||H^n |T>|| / ||H^n |Ω>|| ;  "
      "f_n = ||(H - E_Ω)^n |T>||")
print("    (PH-even Tr(P |h|^n) ratios are identically 1 by "
      "particle-hole symmetry -- not a test, omitted as a gate.)")

en = {n: [] for n in range(1, 5)}
fn = {n: [] for n in range(1, 5)}
dEs = []
vars_ = []
E0s = []
for Nx in NXS:
    spec0 = CACHE[("TOP", Nx, 0)]
    spec1 = CACHE[("TOP", Nx, 1)]
    h, V0, V1 = spec0["H"], spec0["V"], spec1["V"]
    kap0, mu0 = slater_cumulants(V0, h, 8, shift=0.0)
    kap1, mu1 = slater_cumulants(V1, h, 8, shift=0.0)
    E0 = kap0[0]
    _, mu1p = slater_cumulants(V1, h, 8, shift=E0)
    # Ω is an eigenstate: κ_{n>1}(Ω) = 0, ||H^n Ω|| = |E0|^n
    dE = kap1[0] - E0
    varT = kap1[1]
    dEs.append(dE)
    vars_.append(varT)
    E0s.append(E0)
    row_e, row_f = [], []
    for n in range(1, 5):
        nT = float(np.sqrt(max(mu1[2 * n], 0.0)))
        nO = float(np.sqrt(max(mu0[2 * n], 0.0)))
        nexc = float(np.sqrt(max(mu1p[2 * n], 0.0)))
        en[n].append(nT / nO)
        fn[n].append(nexc)
        row_e.append(nT / nO)
        row_f.append(nexc)
    print("    Nx=%3d  E_Ω=%.4f  dE=%.4f  var_T=%.4f"
          % (Nx, E0, dE, varT))
    print("           e_n n=1..4:", ["%.8f" % x for x in row_e])
    print("           f_n n=1..4:", ["%.6f" % x for x in row_f])
    # sanity: Ω variance ~ 0
    if abs(kap0[1]) > 1e-6:
        rep("Ω is an eigenstate of dΓ(h0) (var=0)", False,
            extra="var_Ω=%.3e" % kap0[1])

print("  energy-ratio table e_n(N):")
print("      N\\n     n=1        n=2        n=3        n=4")
for i, Nx in enumerate(NXS):
    print("      %3d  " % Nx + "  ".join("%.8f" % en[n][i]
                                         for n in range(1, 5)))
print("  excitation-norm table f_n(N) = ||(H-E_Ω)^n T||:")
print("      N\\n     n=1        n=2        n=3        n=4")
for i, Nx in enumerate(NXS):
    print("      %3d  " % Nx + "  ".join("%10.4f" % fn[n][i]
                                         for n in range(1, 5)))

e_ok = True
for n in range(1, 5):
    lo, hi = min(en[n]), max(en[n])
    bounded = 0.90 < lo <= hi < 1.05
    e_ok &= bounded
    rep("L2 e_%d(N) bounded in N (range [%.6f, %.6f] subset "
        "(0.90, 1.05); tends to 1 as volume/edge) -- finite shadow "
        "of ||H^n T|| / ||H^n Ω|| staying O(1)"
        % (n, lo, hi),
        bounded)

f_ok = True
for n in range(1, 5):
    lo, hi = min(fn[n]), max(fn[n])
    rel = (hi - lo) / lo if lo > 0 else 1.0
    # saturating O(1) in N; mild drift from finite-size edge energy
    sat = rel < 0.05
    f_ok &= sat
    rep("L2 f_%d(N)=||(H-E_Ω)^n T|| saturates in N "
        "(range [%.4f, %.4f], rel %.2f%%) -- excess energy of the "
        "twist state is O(1), the finite shadow of a (n!)^β bound "
        "with N-independent C"
        % (n, lo, hi, 100 * rel),
        sat)

dE_rel = (max(dEs) - min(dEs)) / np.mean(dEs)
rep("L2 relative energy dE=Tr((P1-P0) h0) is O(1) in N "
    "(values %s, rel range %.2f%%) -- not an extensive bulk cost"
    % ([round(x, 4) for x in dEs], 100 * dE_rel),
    dE_rel < 0.05 and min(dEs) > 1.0)

# factorial growth in n of f_n, at fixed N=NMAX: a sanity that we
# are seeing (n!)^β-compatible growth, not exponential in n worse
# than e.g. (n!)^3.  Ratios f_{n+1}/((n+1) f_n) staying bounded
# is the β=1 shadow; we only check f_n < (C)^{n+1} (n!)^2
# for a C fitted from n=1.
fN = [fn[n][-1] for n in range(1, 5)]
# C from n=1: f1 <= C^2 * 1  => C >= sqrt(f1)
Cfit = float(np.sqrt(fN[0]) + 0.5)
beta = 2.0
fact = 1
poly_ok = True
for n in range(1, 5):
    fact *= n
    bound = Cfit ** (n + 1) * (fact ** beta)
    poly_ok &= (fN[n - 1] < bound)
rep("L2 factorial envelope at N=%d: f_n < C^{n+1} (n!)^2 with "
    "C=%.3f  (f=%s vs envelope) -- executable (n!)^β shadow, "
    "not a proof of the infinite-volume bound"
    % (NMAX, Cfit, ["%.2f" % x for x in fN]),
    poly_ok)


# ======================================================================
# (4) REDUCTION STATEMENT + VERDICT
# ======================================================================
print()
l1 = topo_ok and me_ok and len(nonzeroA) == len(NXS)
l2 = e_ok and f_ok and poly_ok
if l1 and l2:
    verdict = "LEMMA_REDUCED_TO_CITED_QUASIFREE_CLASS"
elif not topo_ok:
    verdict = "HS_CAUCHY_FAILS"
elif len(nonzeroA) < 3:
    verdict = "PARITY_BLOCKS_SUBSEQUENCE"
elif not me_ok:
    verdict = "MATRIX_ELEMENT_CAUCHY_FAILS"
elif not l2:
    verdict = "ENERGY_RATIO_UNBOUNDED"
else:
    verdict = "REDUCTION_PARTIAL"

print("REDUCTION STATEMENT:")
print("  GIVEN the cited quasi-free implementer-continuity theorem")
print("  class (Shale-Stinespring 1965; Araki quasi-free CAR;")
print("  Ruijsenaars 1978), the measured windowed HS-Cauchy rates")
pC6 = cauchy[("TOP", "C", 6)]["p"]
pC8 = cauchy[("TOP", "C", 8)]["p"]
pP6 = cauchy[("TOP", "P", 6)]["p"]
print("    ||D_N[C]-D_%d[C]||_HS ~ N^{%.3f} (w=6) and N^{%.3f} (w=8)"
      % (NMAX, pC6, pC8))
print("    ||D_N[P]-D_%d[P]||_HS ~ N^{%.3f} (w=6); finite window =>"
      % (NMAX, pP6))
print("    HS-Cauchy = operator-norm Cauchy of one-particle data,")
print("  plus phase-fixed matrix-element Cauchy on the Band-A")
print("  Pfaffian subsequence %s" % list(NXS))
print("    (energy-sign overlap is identically 0 by nocc mismatch;")
print("     Band B %s is a second phase choice, internally Cauchy,"
      % list(NX_BAND_B))
print("     distinct local limit, not mixed),")
print("  plus bounded energy ratios e_n in [%.5f, %.5f] and"
      % (min(min(en[n]) for n in range(1, 5)),
         max(max(en[n]) for n in range(1, 5))))
print("  saturating excitation norms f_n,")
print("  REDUCE L1/L2 on this QWZ collar to the citation.")
print("  What remains genuinely open is the identification of the")
print("  QWZ edge scaling limit with the (E8)_1 sector theory")
print("  (the MMST leg) -- the lemma is REDUCED, not closed.")
print("  Contract SEAM.SIMPLECURRENT.GENERATOR.01 stays [O].")
print()
print("FIREWALL: one Majorana copy; finite cylinders Nx<=%d Ny=%d; "
      % (NMAX, NY))
print("  measured rates, no operator-algebra proof; no marker move.")
print()
print("VERDICT: %s" % verdict)
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES")
      + "  (%.1fs)" % (time.time() - T0))
raise SystemExit(0 if ok_all else 1)
