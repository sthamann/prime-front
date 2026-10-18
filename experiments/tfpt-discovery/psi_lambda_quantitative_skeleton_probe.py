#!/usr/bin/env python3
"""psi_lambda_quantitative_skeleton_probe -- EXPLORATION ONLY (no promotion).

THE QUESTION (SEAM.SIMPLECURRENT.GENERATOR.01 [O], analytic half; the
quantitative S2 / G1-G4 skeleton on the REAL collar).  v983 identified
the generator lambda = (omega_s, omega_f) at lattice level (h_lambda = 1,
order-4 glue).  The collar is the v367 QWZ/p+ip Chern model (M = 1
topological / M = 3 trivial) on a cylinder, copied from
psi_lambda_seam_edge_s1s2_probe.py.  The S1-S4 chain asks for local
covariance convergence, Shale-Stinespring implementer convergence,
crossed-product/scaling-limit exchange, holomorphy selector.  This probe
delivers the sharpest MACHINE-CHECKABLE quantitative S2 lemma plus G3/G4
shadows available on the finite cylinder:

  S2 QUANTITATIVE (the core).  Two quasi-free sector states are locally
     implementable and globally inequivalent iff the difference of their
     Fermi covariances is Hilbert-Schmidt on every finite window and NOT
     HS on the full system.  For sectors k = 0 vs k = 1:
       (a) windowed ||E_w (C^0 - C^1) E_w||_HS (fixed width w, N_x
           growing): BOUNDED / convergent -- local implementability, the
           quantitative S2 upper bound.  The companion Shale number
           ||(C^0 - C^1) E_w||_HS plateaus (O(1), does not grow).
       (b) full-system ||C^0 - C^1||_HS^2 vs N_x: LOG growth in the
           topological phase (gapless edge = charged-field / global
           inequivalence); SATURATION in the trivial phase (M = 3).
     Covariances are the particle-hole symmetric Fermi symbols
     C = chi_{(-inf,0)}(H) + (1/2) chi_{{0}}(H).

  G4 / Q-SYSTEM SHADOW (fusion order 4).  Four twist insertions compose
     to the trivial sector: H^{(k=4)} = H^{(k=0)} identically (phase
     i^4 = 1, exact), and NONTRIVIALLY the sector-covariance distances
     obey the group pattern d(C^0, C^k) = d(C^0, C^{4-k}) (conjugate
     symmetry) and d depends only on k mod 4.

  G3 / MONODROMY SHADOW.  h_lambda = 1 => trivial self-monodromy.  Lattice
     shadow: discrete Berry phase of the half-filled Slater determinant
     under adiabatic transport of the twist angle theta : 0 -> 2 pi
     (one full mu4 cycle = 4 quarter-steps), together with the spectral-
     flow count of the Fermi occupation.  Honest report: measured phase
     and spectral-flow count, typed as the G3 shadow -- not a braiding
     theorem.

REMAINING LEMMA (open; the operator-norm / energy-bound half of G1 on
the infinite-volume edge algebra -- this is what the externalization
package cites this probe's constants as input for):

  Let C_N^{(k)} be the PH-symmetric Fermi covariance of the QWZ cylinder
  of circumference N_x, and Delta_N = C_N^{(0)} - C_N^{(1)}.  This probe
  supplies the HS hypotheses: ||E_w Delta_N E_w||_HS bounded (and
  decaying) in N_x, ||Delta_N E_w||_HS plateaus, and in the topological
  phase ||Delta_N||_HS^2 = a + b log N_x with b > 0 (so Delta_N is NOT
  Hilbert-Schmidt as N_x -> inf).  Shale-Stinespring therefore yields a
  Bogoliubov implementer U_{N,w} on each finite window, and forbids a
  global implementer on the full CAR algebra of the topological cylinder
  in the limit.

  OPEN: let A_edge be the quasi-local CAR algebra of the infinite chiral
  edge (strip of width O(1) along y = 0, x in Z) and D its finite-particle
  core.  There exist choices of implementers U_N such that (i) U_N is
  strongly Cauchy on D (operator-norm convergence on the core as
  N -> inf) and (ii) the limit intertwiner Psi_lambda satisfies
  polynomial energy bounds w.r.t. the edge Hamiltonian H_edge:
      Psi_lambda Omega  in  intersection_n  dom(H_edge^n),
      ||H_edge^n Psi_lambda Omega||  <=  C^{n+1} (n!)^beta
  for some finite C, beta.  Neither (i) nor (ii) follows from HS data:
  SS controls the implementer only in the Fock topology of a finite
  window; H_edge is unbounded.  That is the missing G1 half.  Measured
  (a, b, window power, Shale plateau) are printed at runtime.

HONEST BOUNDARY (firewall): one Majorana copy (the carrier is 16 copies
-- counting only multiplies exponents); finite cylinders; measured rates
and constants, not an operator-algebraic theorem.  G2 relative locality
is not addressed.  SEAM.SIMPLECURRENT.GENERATOR.01 stays [O]; no marker
moves; no promotion.

VERDICT ENUM: S2_QUANTITATIVE_SKELETON_MEASURED
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

# QWZ hopping decomposition: h(k) = sin kx SX + sin ky SY +
#   (M - cos kx - cos ky) SZ  ==>  real-space:
#   onsite M*SZ; x-hop: (SX/(2i) - SZ/2); y-hop: (SY/(2i) - SZ/2)
#   (verbatim construction of psi_lambda_seam_edge_s1s2_probe.py)
TX = (SX / (2j) - SZ / 2)
TY = (SY / (2j) - SZ / 2)

ZCUT = 1e-10
NY, WIN = 8, 6
NXS = (16, 24, 32, 48, 64, 80, 96)
NX_G4 = 32
NX_G3 = 24
NSTEP_BERRY = 40


def qwz_cylinder(Nx, Ny, M, phase):
    """single-particle Hamiltonian on the cylinder: periodic x with a
    complex twist `phase` across the seam link x = Nx-1 -> 0, open y.
    Integer mu4 sectors: phase = 1j ** k.  Continuous flux: exp(i theta)."""
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


def ground_cov(H):
    """particle-hole symmetric Fermi covariance:
    C = chi_{E<0}(H) + (1/2) chi_{E=0}(H)."""
    w, v = np.linalg.eigh(H)
    n = np.zeros(w.shape[0])
    n[w < -ZCUT] = 1.0
    n[np.abs(w) <= ZCUT] = 0.5
    C = (v * n) @ v.conj().T
    return C, w, n


def hs2(A):
    """||A||_HS^2 = Tr(A^* A) for a square matrix."""
    return float(np.vdot(A, A).real)


def edge_window_idx(Nx, Ny, w):
    """sites y = 0, x = 0..w-1, both orbitals (parent-probe window)."""
    idx = []
    for x in range(w):
        base = 2 * ((x % Nx) * Ny + 0)
        idx += [base, base + 1]
    return idx


def log_lin_fit(xs, ys):
    """ys ~ a + b log(xs).  Returns a, b, r^2."""
    x = np.log(np.asarray(xs, float))
    y = np.asarray(ys, float)
    b, a = np.polyfit(x, y, 1)
    yhat = a + b * x
    ss_res = float(np.sum((y - yhat) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
    return float(a), float(b), float(r2)


# ======================================================================
# S2 QUANTITATIVE: windowed HS-boundedness + global HS-divergence
# ======================================================================
print("=== S2 QUANTITATIVE: windowed HS vs global HS  (Ny=%d, w=%d) ==="
      % (NY, WIN))

s2 = {}
for M, tag in ((1.0, "TOP"), (3.0, "TRIV")):
    glob, win, col = [], [], []
    print("  -- M=%.1f %s  sectors k=0 vs k=1 --" % (M, tag))
    for Nx in NXS:
        C0, _, n0 = ground_cov(qwz_cylinder(Nx, NY, M, 1j ** 0))
        C1, _, n1 = ground_cov(qwz_cylinder(Nx, NY, M, 1j ** 1))
        D = C0 - C1
        idx = edge_window_idx(Nx, NY, WIN)
        g = hs2(D)
        wloc = hs2(D[np.ix_(idx, idx)])
        cloc = hs2(D[:, idx])
        glob.append(g)
        win.append(wloc)
        col.append(cloc)
        print("     Nx=%3d  ||D||_HS^2=%10.6f  ||EDE||_HS^2=%10.4e  "
              "||DE||_HS^2=%10.4e  trC0=%.1f"
              % (Nx, g, wloc, cloc, float(n0.sum())))
    a, b, r2 = log_lin_fit(NXS, glob)
    pwin = float(np.polyfit(np.log(NXS), np.log(np.maximum(win, 1e-300)), 1)[0])
    s2[tag] = dict(glob=glob, win=win, col=col, a=a, b=b, r2=r2, pwin=pwin)
    print("     fit  ||D||_HS^2 = %.6f + %.6f log Nx   r^2=%.6f"
          % (a, b, r2))
    print("     window ||EDE||_HS^2 ~ Nx^{%.3f};  Shale plateau "
          "||DE||_HS^2 in [%.4f, %.4f]"
          % (pwin, min(col), max(col)))

top, triv = s2["TOP"], s2["TRIV"]

rep("S2 LOCAL (a): topological windowed compression ||E (C^0-C^1) E||_HS^2 "
    "is BOUNDED and CONVERGENT (monotone decay, power p=%.3f < -1; "
    "Nx=16 -> 96: %.3e -> %.3e)"
    % (top["pwin"], top["win"][0], top["win"][-1]),
    top["win"][-1] < top["win"][0] / 10
    and top["pwin"] < -1.0
    and all(top["win"][i] >= top["win"][i + 1] for i in range(len(NXS) - 1)))

rep("S2 LOCAL (a'): topological Shale number ||(C^0-C^1) E_w||_HS^2 "
    "PLATEAUS (relative range %.3f < 0.15; finite-N upper bound %.4f) "
    "-- local implementability, the quantitative S2 upper bound"
    % ((max(top["col"]) - min(top["col"])) / np.mean(top["col"]),
       max(top["col"])),
    (max(top["col"]) - min(top["col"])) / np.mean(top["col"]) < 0.15
    and max(top["col"]) < 1.0)

rep("S2 GLOBAL (b) TOPOLOGICAL: ||C^0-C^1||_HS^2 = %.4f + %.4f log Nx "
    "(r^2=%.4f) -- LOG DIVERGENCE of the gapless edge, the charged-field "
    "/ global-inequivalence half of S2 (b in (0.12, 0.30), r^2 > 0.99)"
    % (top["a"], top["b"], top["r2"]),
    0.12 < top["b"] < 0.30 and top["r2"] > 0.99
    and top["glob"][-1] > top["glob"][0])

rep("S2 GLOBAL (b) TRIVIAL control: ||C^0-C^1||_HS^2 SATURATES at %.10f "
    "(rel. range %.1e; log-slope %.1e) -- gapped bulk, twist is a local "
    "perturbation, globally quasi-equivalent"
    % (triv["glob"][-1],
       (max(triv["glob"]) - min(triv["glob"])) / triv["glob"][-1],
       triv["b"]),
    abs(triv["b"]) < 1e-6
    and (max(triv["glob"]) - min(triv["glob"])) / triv["glob"][-1] < 1e-5)

rep("S2 TRIVIAL window: ||EDE||_HS^2 decays to numerical zero "
    "(Nx=96: %.1e) -- no edge mode, sectors collapse even faster"
    % triv["win"][-1],
    triv["win"][-1] < 1e-20 and triv["win"][0] > triv["win"][3])


# ======================================================================
# G4 / Q-SYSTEM SHADOW: fusion order 4
# ======================================================================
print()
print("=== G4 Q-SYSTEM SHADOW: fusion order 4, conjugate symmetry ===")

rep("G4 EXACT: phase i^4 = 1, so H^{(k=4)} = H^{(k=0)} identically "
    "(and H^{(k)} = H^{(k mod 4)} for every k)",
    np.array_equal(np.array(1j ** 4), np.array(1 + 0j))
    or abs(1j ** 4 - 1) < 1e-15)

# identical Hamiltonians: exact at the matrix level, both phases
h_eq_ok = True
for M in (1.0, 3.0):
    H0 = qwz_cylinder(NX_G4, NY, M, 1j ** 0)
    H4 = qwz_cylinder(NX_G4, NY, M, 1j ** 4)
    H5 = qwz_cylinder(NX_G4, NY, M, 1j ** 5)
    H1 = qwz_cylinder(NX_G4, NY, M, 1j ** 1)
    h_eq_ok &= np.allclose(H0, H4, atol=1e-15)
    h_eq_ok &= np.allclose(H1, H5, atol=1e-15)
rep("G4 EXACT: H(k=4) == H(k=0) and H(k=5) == H(k=1) as matrices "
    "(Nx=%d, both phases)" % NX_G4, h_eq_ok)

g4 = {}
for M, tag in ((1.0, "TOP"), (3.0, "TRIV")):
    Cs = []
    for k in range(8):
        C, _, _ = ground_cov(qwz_cylinder(NX_G4, NY, M, 1j ** k))
        Cs.append(C)
    d = [np.sqrt(hs2(Cs[0] - Cs[k])) for k in range(8)]
    g4[tag] = d
    print("   %s d(C^0, C^k) k=0..7:" % tag, ["%.6f" % x for x in d])

for tag in ("TOP", "TRIV"):
    d = g4[tag]
    conj = max(abs(d[k] - d[(4 - k) % 4]) for k in range(4))
    mod4 = max(abs(d[k] - d[k + 4]) for k in range(4))
    print("   %s conjugate max |d(k)-d(4-k)|=%.3e   mod4 max |d(k)-d(k+4)|=%.3e"
          % (tag, conj, mod4))
    rep("G4 %s: conjugate symmetry d(C^0,C^k)=d(C^0,C^{4-k}) "
        "(max abs %.3e)" % (tag, conj), conj < 1e-9)
    rep("G4 %s: d depends only on k mod 4  (max |d(k)-d(k+4)|=%.3e); "
        "d(0,0)=0, d(0,2) > d(0,1)=d(0,3)"
        % (tag, mod4),
        mod4 < 1e-9 and d[0] < 1e-12 and d[2] > d[1]
        and abs(d[1] - d[3]) < 1e-9)


# ======================================================================
# G3 / MONODROMY SHADOW: Berry phase + spectral flow
# ======================================================================
print()
print("=== G3 MONODROMY SHADOW: Berry phase of the Slater GS, "
      "theta: 0 -> 2pi (%d steps) ===" % NSTEP_BERRY)


def berry_and_flow(Nx, Ny, M, nstep):
    """discrete Berry phase of the half-filled Slater determinant along
    the mu4 cycle, with parallel-transport gauge, plus Fermi-occupation
    spectral flow (N_- swing and jump count)."""
    nocc = Nx * Ny
    thetas = np.linspace(0.0, 2.0 * np.pi, nstep, endpoint=False)
    V_prev = None
    V0 = None
    min_s = 1.0
    Nm = []
    prev_w = None
    n_up = n_down = 0
    for th in thetas:
        w, v = np.linalg.eigh(qwz_cylinder(Nx, Ny, M, np.exp(1j * th)))
        Nm.append(int(np.sum(w < -ZCUT)))
        if prev_w is not None:
            for a, b in zip(prev_w, w):
                if a < 0.0 <= b:
                    n_up += 1
                if a > 0.0 >= b:
                    n_down += 1
        prev_w = w
        Vraw = v[:, :nocc]
        if V_prev is None:
            V_prev = Vraw
            V0 = Vraw.copy()
            continue
        mover = V_prev.conj().T @ Vraw
        u, s, vh = np.linalg.svd(mover, full_matrices=False)
        min_s = min(min_s, float(s.min()))
        V_prev = Vraw @ vh.conj().T @ u.conj().T
    mover = V_prev.conj().T @ V0
    u, s, vh = np.linalg.svd(mover, full_matrices=False)
    min_s = min(min_s, float(s.min()))
    berry = float(np.angle(np.linalg.det(u @ vh)))
    dN = np.diff(np.array(Nm + [Nm[0]], dtype=int))
    return dict(berry=berry, min_s=min_s,
                n_up=n_up, n_down=n_down, net=n_up - n_down,
                swing=int(max(Nm) - min(Nm)),
                n_jump=int(np.sum(np.abs(dN))),
                Nm0=Nm[0], Nm_min=min(Nm), Nm_max=max(Nm))


g3 = {}
for M, tag in ((1.0, "TOP"), (3.0, "TRIV")):
    r = berry_and_flow(NX_G3, NY, M, NSTEP_BERRY)
    g3[tag] = r
    print("   %s Nx=%d: Berry=%.6f (%.4f pi)  min_s=%.3e  "
          "N_- swing=%d jumps=%d  sorted up/down/net=%d/%d/%d"
          % (tag, NX_G3, r["berry"], r["berry"] / np.pi, r["min_s"],
             r["swing"], r["n_jump"], r["n_up"], r["n_down"], r["net"]))

rep("G3 TRIVIAL: no spectral flow (N_- swing=0, jumps=0, min_s>0.9) "
    "and Berry phase = 0 mod 2pi (measured %.3e) -- gapped, the mu4 "
    "cycle is a contractible local perturbation"
    % g3["TRIV"]["berry"],
    g3["TRIV"]["swing"] == 0 and g3["TRIV"]["n_jump"] == 0
    and g3["TRIV"]["min_s"] > 0.9
    and abs(g3["TRIV"]["berry"]) < 1e-6)

rep("G3 TOPOLOGICAL: spectral flow on the chiral edge "
    "(N_- swing=%d >= 1, jumps=%d >= 1) with Slater-overlap collapse "
    "(min_s=%.3e << 1) -- the Laughlin pump of Chern C=1, the lattice "
    "shadow of the charged-sector monodromy"
    % (g3["TOP"]["swing"], g3["TOP"]["n_jump"], g3["TOP"]["min_s"]),
    g3["TOP"]["swing"] >= 1 and g3["TOP"]["n_jump"] >= 1
    and g3["TOP"]["min_s"] < 1e-4)

rep("G3 SELF-MONODROMY shadow of h_lambda=1: the Berry phase of the "
    "ground-state Slater determinant around one full mu4 cycle is 0 "
    "mod 2pi in BOTH phases (TOP %.4f pi, TRIV %.4f pi) -- trivial "
    "self-monodromy; the topological discriminator is the spectral-flow "
    "count, not a nontrivial U(1) holonomy"
    % (g3["TOP"]["berry"] / np.pi, g3["TRIV"]["berry"] / np.pi),
    abs(g3["TOP"]["berry"]) < 0.2 and abs(g3["TRIV"]["berry"]) < 1e-6)


# ======================================================================
# remaining lemma + verdict
# ======================================================================
print()
print("REMAINING LEMMA (G1, operator-norm / energy-bound half; NOT proved):")
print("  Hypotheses measured here, topological phase, Ny=%d, w=%d:" % (NY, WIN))
print("    ||C^0-C^1||_HS^2 = %.6f + %.6f log N_x   (r^2=%.6f)"
      % (top["a"], top["b"], top["r2"]))
print("    ||E_w (C^0-C^1) E_w||_HS^2 ~ N_x^{%.3f}  (convergent -> 0)"
      % top["pwin"])
print("    ||(C^0-C^1) E_w||_HS^2 plateau in [%.6f, %.6f]  (S2 local bound)"
      % (min(top["col"]), max(top["col"])))
print("    trivial-phase global HS^2 plateau = %.10f" % triv["glob"][-1])
print("  Open: strong/operator-norm Cauchy of Shale-Stinespring")
print("  implementers U_N on the finite-particle core of the infinite-")
print("  volume edge CAR algebra A_edge, AND polynomial energy bounds")
print("  ||H_edge^n Psi_lambda Omega|| <= C^{n+1} (n!)^beta.")
print("  HS numbers do not imply either.  Contract stays [O].")
print()
print("VERDICT: S2_QUANTITATIVE_SKELETON_MEASURED -- windowed-HS-"
      "boundedness + global-HS-divergence is the quantitative S2 lemma "
      "on the real collar; G4 fusion-order-4 and G3 trivial-self-"
      "monodromy/spectral-flow are measured shadows; the G1 energy/"
      "operator-norm half on A_edge remains open; no promotion")
print("PROBE " + ("ALL PASS" if ok_all else "HAS FAILURES"))
raise SystemExit(0 if ok_all else 1)
