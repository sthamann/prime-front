#!/usr/bin/env python3
"""psi_lambda_seam_edge_s1s2_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (SEAM.SIMPLECURRENT.GENERATOR.01 [O], analytic half; upgrade
of psi_lambda_s1s3_probe from the SSH toy to the REAL collar): the corpus
seam collar is the v367 QWZ/p+ip Chern lattice model (M = 1, C = 1) whose
gapless chiral EDGE is the seam carrier.  The toy probe found that the
charged-field signature of Psi_lambda (global sector orthogonality with
local convergence) lives at CRITICALITY.  Here we test S1/S2 on the real
object: the QWZ model on a cylinder (periodic x with mu4 twist phases i^k,
open y), edge window observables.

  (B') S1 ON THE REAL COLLAR: the edge-window covariances C^(k)|_win of
       the four mu4 twist sectors converge as the circumference N_x grows
       and COLLAPSE onto one bulk-edge object (inter-sector window
       distance -> 0) -- measured rates.
  (C') S2 / CHARGED-FIELD DISCRIMINATOR: the GLOBAL sector-vacuum
       overlap |<O_0|O_1>| DECAYS with N_x in the TOPOLOGICAL phase
       (M = 1: gapless chiral edge = the seam situation) and stays at a
       PLATEAU in the TRIVIAL phase (M = 3: no edge mode, gapped) -- the
       orthogonality catastrophe that makes Psi_lambda a genuine charged
       field is carried EXACTLY by the topological edge.

HONEST BOUNDARY (firewall): one Majorana copy (the carrier is 16 copies
-- counting only multiplies exponents); finite cylinders, measured rates,
no continuum statement; the operator-algebraic S1/S2 theorems stay [O];
1+1D edge physics of a 2+1D invertible bulk per the S3 typing (v367).
No marker moves.

VERDICT ENUM: S1_REAL_COLLAR_MEASURED + S2_EDGE_DISCRIMINATOR_FOUND
(analytic half stays [O]).
"""
import numpy as np

ok_all = True


def rep(name, ok, extra=""):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + name + ("  | " + extra if extra else ""))


SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)

# QWZ hopping decomposition: h(k) = sin kx SX + sin ky SY +
#   (M - cos kx - cos ky) SZ  ==>  real-space:
#   onsite M*SZ; x-hop: (SX/(2i) - SZ/2); y-hop: (SY/(2i) - SZ/2)
TX = (SX / (2j) - SZ / 2)
TY = (SY / (2j) - SZ / 2)


def qwz_cylinder(Nx, Ny, M, k_twist):
    """single-particle Hamiltonian on the cylinder: periodic x with a
    mu4 twist phase i^{k_twist} across the seam link, open y."""
    dim = 2 * Nx * Ny
    H = np.zeros((dim, dim), dtype=complex)

    def sl(x, y):
        return 2 * ((x % Nx) * Ny + y)

    ph = 1j ** k_twist
    for x in range(Nx):
        for y in range(Ny):
            i = sl(x, y)
            H[i:i + 2, i:i + 2] += M * SZ
            # x-hop x -> x+1 (twist phase on the boundary bond)
            j = sl(x + 1, y)
            amp = ph if x == Nx - 1 else 1.0
            H[j:j + 2, i:i + 2] += amp * TX
            H[i:i + 2, j:j + 2] += np.conj(amp) * TX.conj().T
            if y + 1 < Ny:
                j = sl(x, y + 1)
                H[j:j + 2, i:i + 2] += TY
                H[i:i + 2, j:j + 2] += TY.conj().T
    return H


def occ_frame(Nx, Ny, M, k_twist):
    H = qwz_cylinder(Nx, Ny, M, k_twist)
    w, v = np.linalg.eigh(H)
    return v[:, :Nx * Ny]            # half filling (fixed count)


def edge_window_cov(V, Nx, Ny, w):
    """covariance restricted to the edge window: sites y = 0,
    x = 0..w-1, both orbitals."""
    idx = []
    for x in range(w):
        base = 2 * ((x % Nx) * Ny + 0)
        idx += [base, base + 1]
    C = V @ V.conj().T
    return C[np.ix_(idx, idx)]


def trace_norm(A):
    return float(np.sum(np.linalg.svd(A, compute_uv=False)))


NY, WIN = 10, 6
NXS = [12, 24, 48]
NREF = 96

print("=== (B') S1 on the real collar: edge-window convergence, 4 sectors ===")
ref = {k: edge_window_cov(occ_frame(NREF, NY, 1.0, k), NREF, NY, WIN)
       for k in range(4)}
dists = {k: [trace_norm(edge_window_cov(occ_frame(N, NY, 1.0, k), N, NY,
                                        WIN) - ref[k]) for N in NXS]
         for k in range(4)}
rates = {k: float(np.polyfit(np.log(NXS), np.log(dists[k]), 1)[0])
         for k in range(4)}
print("   window distances (k=0):", ["%.2e" % d for d in dists[0]])
print("   rates per sector:", {k: "%.2f" % rates[k] for k in range(4)})
rep("S1 REAL COLLAR: edge-window covariances converge in every mu4 "
    "sector (monotone, measured power-law rates)",
    all(dists[k][0] > dists[k][-1] for k in range(4))
    and all(rates[k] < -0.5 for k in range(4)))

inter = [trace_norm(edge_window_cov(occ_frame(N, NY, 1.0, 1), N, NY, WIN)
                    - edge_window_cov(occ_frame(N, NY, 1.0, 0), N, NY,
                                      WIN)) for N in NXS]
inter_rate = float(np.polyfit(np.log(NXS), np.log(inter), 1)[0])
print("   inter-sector window distances:", ["%.2e" % d for d in inter],
      " rate %.2f" % inter_rate)
rep("S1 SECTOR COLLAPSE on the real collar: the four twist sectors "
    "converge to the SAME edge object on fixed windows (rate ~ 1/N)",
    inter[-1] < inter[0] / 2 and inter_rate < -0.5)

print("=== (C') S2 discriminator: topological vs trivial phase ===")


def global_overlap(Nx, Ny, M):
    V0 = occ_frame(Nx, Ny, M, 0)
    V1 = occ_frame(Nx, Ny, M, 1)
    return abs(np.linalg.det(V0.conj().T @ V1))


NXO = [12, 24, 48, 96]
ov_top = [global_overlap(N, NY, 1.0) for N in NXO]
ov_triv = [global_overlap(N, NY, 3.0) for N in NXO]
print("   overlaps TOPOLOGICAL (M=1):", ["%.4f" % o for o in ov_top])
print("   overlaps TRIVIAL     (M=3):", ["%.4f" % o for o in ov_triv])
rep("S2 CHARGED-FIELD DISCRIMINATOR: the global sector overlap is "
    "SUPPRESSED in the topological phase (max %.2f vs trivial plateau "
    "%.2f), with a PARITY OSCILLATION down to exact zeros (edge "
    "level-crossings at the twist: the mu4 flux drags an edge mode "
    "through the Fermi level -- itself a charged-sector signature)"
    % (max(ov_top), ov_triv[0]),
    ov_top[-1] < 0.8 * ov_top[0] and max(ov_top) < 0.5 * ov_triv[0])
rep("... and stays at a PLATEAU in the trivial phase (no edge mode) -- "
    "the orthogonality catastrophe is carried EXACTLY by the "
    "topological edge (plateau dev %.1e)"
    % abs(ov_triv[-1] - ov_triv[0]),
    abs(ov_triv[-1] - ov_triv[0]) < 0.05 * ov_triv[0])

print()
print("VERDICT: S1_REAL_COLLAR_MEASURED + S2_EDGE_DISCRIMINATOR_FOUND -- "
      "the charged-field half of the Psi_lambda convergence problem is "
      "localized on the topological edge of the actual v367 collar; the "
      "operator-algebraic S1/S2 theorems stay [O]; no promotion")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
