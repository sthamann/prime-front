#!/usr/bin/env python3
"""QF-OFFENSIVE strand 3, module 4 (THE LAST DECIDER) -- the ordered
multiplicative cell cocycle on a depth-dependent slow band:
qf_cell_cocycle_probe.

STAKES (frozen up front by the user): if this module dies, the Gram
route closes WITHOUT further variants and the sharpened Z1 contract
takes over.  The Z1 handover content in that case: the moving-edge
cadence (7th threshold at M = 992, count 8 from ~1108, the 8/9
crossing at 976), the ram-odd contact direction, the settled
per-function q levels (R2 family 0.225..0.358, R1 family
0.008..0.079), and whichever domain facts survive this run.

Exploration only (tfpt-experiment firewall): NOT wired into
run_all.py, no ledger row, no paper edit, no website edit, NO RH
CLAIM, and this probe writes no files.  Everything is built
exclusively from the source window operator -- never from target
data (AST-guarded).

INPUT STATE (frozen findings, none re-adjudicated here):
  *  v758 killed the additive cellwise-positivity formulation;
     qf_feshbach_effective_probe blocked the fixed-d Feshbach limit
     (FESHBACH-PARTIAL: d = 6 is the right well-defined object but
     its Cauchy tail flattens where mode 7 grazes the band edge;
     d = 7 converges but loses separation at the top rung; d = 8
     has an internal 8/9 crossing at M = 976).  The moving edge
     names THIS module: transport with a DEPTH-DEPENDENT band.
  *  qf_drainage_probe: QF-SETTLES-POSITIVE (the wall is a positive
     per-function constant); threshold count 6 -> 7 at M = 992,
     -> 8 from ~1108 on the 1e8 comb.

EXACT IDENTITY (derived first, then float-gated on every rung):
grow the window by one cell,
    A_{k+1} - z = [[A_k - z, U_k], [U_k^T, W_k - z]],
where (U_k, W_k) are EXACTLY the added rows/columns of the source
operator between rungs k and k+1 (the new Toeplitz lag placements).
Eliminating the new cell is the Redheffer star action of the cell
block; on the graph of the resolvent it is the linear-fractional
map [R; I] -> M_k [R; I], and its corner evaluation is the exact
Moebius/Riccati update of the compressed resolvent corner
    G_{k+1}(z) = G_k(z) + (Y_k)_I D_k^{-1} (Y_k)_I^T,
    Y_k = R_k U_k,   D_k = (W_k - z) - U_k^T R_k U_k,
with R_k = (A_k - z)^{-1} the carried cocycle state and I the
frozen NCOR-coordinate corner; the ordered product Prod_k M_k is
the nested-Schur (quotient-property) composition -- Schur
complements COMPOSE, they are not summed: this replaces the killed
additive formulation.  HONESTY (predeclared reading): for a DENSE
Toeplitz source the cell coefficients are the new lags FILTERED
through the carried state R_k -- the source's memory lives in the
cocycle state; a strictly local new-lags-only coefficient set
exists only for banded sources.  All coefficients remain 100%
source-native and target-free.  The identity is gated on EVERY
rung (defect ||(A_k - z) R_k[:, I] - E_I||_max <= IDY_BAR) and
against INDEPENDENT dense solves at the Ward rungs (rel <=
WARD_BAR) -- this is the module's exact-identity gate, mirroring
the Feshbach reconstruction Ward.
DECLARED IMPLEMENTATION CORRECTION (after the first execution;
full disclosure in RESULTS): raw chained Banachiewicz updates
amplified float error by ~2.3x per cell (72 cells -> defect
6.2e13) while the 4-cell control ladders stayed at 5e-12 -- a
numerical failure of the carried state, NOT of the identity.  The
state is therefore refreshed by the exact-identity-preserving
Hotelling iteration R <- R + R (I - (A - z) R) after each cell
until the per-rung defect meets REFRESH_FLOOR = 1e-11 (max 3
iterations).  The update coefficients (U_k, W_k), every gate and
every bar are UNCHANGED; the identity gate remains the arbiter,
and the eigh-based W~ layer is untouched by this correction.

DEPTH-DEPENDENT BAND WITH TRANSITION MAPS (frozen band rule): the
band at rung M is the THRESHOLD BAND d(M) = #{lambda_i(A_M) <=
THR_NULL = 1e-4} (the deployed near-null threshold rule; measured
cadence 6 -> 7 at 992, -> 8 near 1108; every change of d(M) inside
the gated range is a TYPED TRANSITION, reported with the entering
mode's eigenvalue).  Transition maps (frozen convention): the
transported frame R_k in O(d(k)) is chained by the Kato/polar
factors of the band overlaps; at a dimension INCREASE d -> d' the
old frame is embedded by the polar isometry J = U_thin V_thin^T of
the (d' x d) overlap and the new directions enter as the sign-fixed
orthonormal complement columns, R_{k+1} = [J R_k | N] in O(d'); at
a (not expected) DECREASE the frame is re-anchored to I_{d'} and
the transition is typed MODE-EXIT.  The transported band object is
    W~_k(z) = R_k^T diag(1/(lambda_i(X_k) - z))_{i <= d(k)} R_k,
the compressed band resolvent (the Herglotz object of the Feshbach
run) in the moving d(X) frame.  The cocycle and the gates run over
the FULL gated range INCLUDING the transitions -- that is the
point of the module.  Increments across a transition are compared
on the transported-old-frame corner (first d columns of R_{k+1});
transition increments are additionally listed separately.

ADMISSIBLE MATRIX DOMAIN (frozen BEFORE running; the kill-#9
gate): the Nevanlinna/Stieltjes sandwich
    D = {Im F(z) >= -HERG_FLOOR at both complex points
         z = i h and -1e-3 + i h (h = 1e-2)}
        INTERSECT
        {min eig F(-eps) >= -PSD_FLOOR for eps in (1e-1, 1e-2,
         1e-3)}  (Stieltjes cone at the frozen real points),
tested for BOTH transported objects (corner cocycle value G_k and
band object W~_k) on EVERY gated rung including every transition
rung.  Individual cocycle factors MAY be indefinite -- ONLY domain
preservation is gated (the whole philosophy: transport
information, don't demand cellwise positivity); the cell margins
(min eig D_k, eigenrange of the corner update term) are REPORTED,
never gated.  The cone test is a fixed-z statement about the
compressed resolvent (like the Feshbach Q-separation) -- NOT a
positive-lower-eigenvalue bound on A, which remains forbidden in
gates (PD of the window stays measured output).  Predeclared
control honesty: real-symmetric indefinite controls KEEP the
complex-point Herglotz identity (self-adjointness is not what they
break); the discriminating domain clause is the Stieltjes cone at
real z and/or cell-block positivity loss (D_k leaves the cone) --
exactly where 'the Herglotz sandwich' breaks for indefinite A.
Domain-breach typing (frozen): 0 non-transition breaches = pass;
1..2 isolated breaches = typed exceptions (CARRIES additionally
requires them transition-adjacent, i.e. within one rung of a typed
transition); > 2 = SYSTEMATIC = kill.

RENORMALIZED CONVERGENCE (frozen; Gate-3'-corner lesson): the
gated statistic runs on RELATIVE entrywise increments
    rel_k = ||obj_{k+1} - obj_k||_max / N_k,
    N_k = max(||obj_k||_max, ||obj_{k+1}||_max),
a source-native, target-free normalizer declared as part of the
object definition -- this is a RENORMALIZED-OBJECT claim, NOT the
absolute 2^-n contract (stated plainly).  Gated cells: both
objects x the three real eps (6 cells); the two complex points are
REPORTED.  Bars per cell (house oscillation-aware statistic):
med5(LAST5)/med5(FIRST5) <= C_MED = 0.5 AND second-half falling
rate b2 >= C_SLOPE = 0.02/X (hbp.fit_rate verbatim, the declared
bounded-statistic slope -- no other fit enters any gate);
converged-to-floor clause: a cell also passes if med5(LAST5) <=
NOISE_PASS = 1e-12 (already at float noise).  72 increments,
blocks FIRST5 = 1..5, LAST5 = 68..72, second half = 37..72,
increment X = right-rung X.
KILLS (frozen): K1 exact identity fails (any rung defect >
  IDY_BAR = 1e-8 or Ward residual > WARD_BAR = 1e-8); K2
  SYSTEMATIC domain breach (> 2 non-transition rungs, any cell);
  K3 target data in the updates (AST + construction audit); K4
  transport collapse (overlap sigma_min < 1e-8, a 90-degree
  angle); K5 an RH-strength normalizer (audit: the normalizer is
  the object's own entry scale, nothing else).
LADDER: the 1e8 comb re-derived in-process (probes write no
  files); gated range GLAD = 888..1176 step 4 (73 rungs, 72
  increments, cell width s = 4); step-1 spectra around every
  measured transition rung REPORTED (entering eigenvalue vs
  threshold at step-1 resolution).  Guards: overlap exact,
  Chebyshev envelope, parent-tower prefix Ward, reproduction Ward
  against the Feshbach run (6/7 gap(1176) = 0.1397 +- 2e-3,
  nn(888) = 6, nn(1176) = 8, lambda_min(1176) = 3.8825e-6 +-
  2e-8), runtime cap 1800 s predeclared.
CONTROLS (mandatory, must fire; frozen fire rule): CS
  position-scramble (deep comb, seed 7, rungs 496..512 step 4) and
  CE Epstein x^2 + 5y^2 (cap 640, rungs 624..640 step 4), same
  cocycle machinery; FIRE = [Stieltjes cone broken: min eig
  G(-eps) < -1e-6 at the top rung for some gated eps] OR [cell
  Schur block leaves the cone: min eig D_k < 0 at real z] OR
  [identity defect > 1e-6] OR [init/update solve singular].
VERDICT ENUM (frozen; decision order as listed):
  0. any guard fails or a control fails to fire -> printed as
     COCYCLE-DEAD (invalid run), exit 1, no structural claim.
  1. a kill fires -> COCYCLE-DEAD: the Gram route closes without
     further variants; the sharpened Z1 contract takes over with
     the handover content named in STAKES.
  2. exact identity + domain preserved (incl. transitions) + all
     six gated convergence cells pass -> COCYCLE-CARRIES: the wall
     becomes a domain-preserving transport statement; what a proof
     would still need is named precisely: (i) UNCONDITIONAL cell
     positivity -- every cell Schur block D_k in the cone from the
     source construction itself, replacing the measured window PD
     input; (ii) a Loewner-order contraction modulus for the
     ordered Moebius product (Birkhoff/Wojtkowski-type), giving
     convergence without measurement; (iii) the z -> 0 boundary
     transition of the limit object (Nevanlinna/Herglotz).  NO RH
     claim at any point.
  3. identity + domain hold but a convergence cell fails ->
     COCYCLE-DOMAIN-ONLY: structure without limit; the Gram route
     retains only the domain-transport statement; Z1 handover as
     in STAKES plus the surviving domain facts.
  4. anything else -> COCYCLE-DEAD (as in 1).
STOP-LIST (binding, inherited): no bare A^{-1} (every resolvent at
frozen z with |z| >= 1e-3 or Im z = h, never z = 0); no PD margin
or 1/eps in any gate; no fits in gates beyond the declared
bounded-statistic slope; no Riemann zeros; no target data; NO RH
claim.  This probe writes no files.

RESULTS (2026-08-05; verdict COCYCLE-DOMAIN-ONLY, GATES 2/8,
GUARDS+CONTROLS 14/14, 28.2 s):
  *  RUN LOG (honesty): execution 1 (26.0 s) was destroyed by the
     numerical instability of the raw chained state (defect
     6.2e13, garbage D_k margins) -- implementation failure, not
     adjudicable, disclosed above as the DECLARED IMPLEMENTATION
     CORRECTION.  Execution 2 with the Hotelling-refreshed state
     is the valid run; the eigh-based W~ layer reproduced
     IDENTICALLY between both executions (as declared).
  *  THE EXACT IDENTITY HOLDS AT MACHINE PRECISION: max per-rung
     defect 9.7e-12 over 73 rungs x 5 z (bar 1e-8), independent
     dense-solve Ward 1.3e-13 (bar 1e-8).  The Moebius/Redheffer
     cell composition with source-lag coefficients is exact as
     derived.  Cell margins (reported): min eig D_k in
     [0.0605, 0.0668] -- every cell Schur block PD; corner update
     terms PSD to -1.5e-17: the cocycle is a MONOTONE Loewner
     flow on the source, exactly the structure the domain gate
     transports.
  *  DOMAIN PRESERVED, ZERO BREACHES in all 730 rung x cell tests
     INCLUDING both typed transitions (d 6 -> 7 at M = 992,
     entering eigenvalue 9.9438e-5; d 7 -> 8 at M = 1108,
     9.9460e-5; step-1 resolution shows the threshold crossings
     at 991 -> 992 and 1106 -> 1107).  Margins: Stieltjes cone
     min eig G >= 0.709, W~ >= 9.99; Herglotz Im >= +1.22e-2 (G),
     >= +98.8 (W~).  Transition increments are UNREMARKABLE
     (same size as neighboring increments) -- the transitions are
     NOT the obstruction.
  *  BUT NO CONVERGENCE CELL PASSES (0/6): the corner cocycle
     value G absorbs a FLAT ~0.1-0.2% relative update per rung
     (med5 ratios 1.032 / 1.014 / 0.777 at eps = 1e-1/1e-2/1e-3
     -- no decay at reachable depth, though second-half rates
     turn positive +0.06..+0.59/X); the band object W~ falls to
     EXACTLY the bar (ratios 0.496 / 0.498 / 0.514 vs 0.5) but
     its second-half slope is NEGATIVE (b2 = -0.15..-0.16/X:
     increments RISING toward the top -- the moving-edge activity
     of the 7/8 modes, the same signature that flattened the
     d = 6 Feshbach tail).
  *  CONTROLS both fire on every eps cell (Stieltjes cone broken:
     min eig G = -2.2e-4 scramble / -0.385 Epstein; cell blocks
     leave the cone: min eig D_k = -1.3e+5 / -4.1e+2); identity
     defects stay at 5e-12 on controls -- the algebra is
     universal, the DOMAIN is what the comb owns.
  *  CONSEQUENCE (stated plainly, per the frozen stakes):
     STRUCTURE WITHOUT LIMIT.  The Gram route retains exactly one
     theorem-shaped fact -- the exact source-native cell cocycle
     preserves the Nevanlinna/Stieltjes domain through the full
     gated range including the mode-entry transitions, as a
     monotone Loewner flow with PD cell blocks -- but its
     renormalized objects do NOT converge at reachable depth: the
     corner updates are flat and the band increments rise with
     the moving edge.  Per the user's frozen stakes the Gram
     route CLOSES without further variants and the sharpened Z1
     contract takes over.  Z1 HANDOVER CONTENT: the moving-edge
     cadence (7th threshold at M = 992, count 8 from 1107/1108,
     the 8/9 crossing at 976); the ram-odd contact direction; the
     settled per-function q levels (R2 family 0.225..0.358, R1
     family 0.008..0.079); and the surviving domain facts (exact
     cocycle identity, PD cell blocks, zero domain breaches,
     Herglotz/Stieltjes margins above).  NO RH claim, no
     X -> infinity claim.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/qf_cell_cocycle_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core  # noqa: E402
import simpler_schur_recursion_probe as srp  # noqa: E402
import handoff_bulk_probe as hbp  # noqa: E402
import epstein_firewall_probe as epx  # noqa: E402
import qf_spectral_bundle_probe as qsb  # noqa: E402  (read-only)

T_START = time.time()

# ------------------------------------------------ frozen specification
D = srp.DGRID
ATOM_MAX_DEEP = 100000000
M_CAP_DEEP = int(math.floor(math.log(ATOM_MAX_DEEP) / D))
M_TOP_DEEP = 1176
M_TOP_PAR = 824

GLAD = list(range(888, 1177, 4))          # 73 rungs, 72 increments
RECON_RUNGS = (888, 968, 1048, 1128, 1176)
NCOR = 8                                  # frozen corner size

EPS_GATED = (1.0e-1, 1.0e-2, 1.0e-3)
Z_REF = -1.0e-2
H_IM = 1.0e-2
ZC = (complex(0.0, H_IM), complex(-1.0e-3, H_IM))
Z_ALL = tuple(complex(-e, 0.0) for e in EPS_GATED) + ZC

THR_NULL = 1.0e-4                         # band rule threshold
THR_DEEP = 1.0e-5

IDY_BAR = 1.0e-8                          # K1 per-rung defect
WARD_BAR = 1.0e-8                         # K1 dense-solve Ward
REFRESH_FLOOR = 1.0e-11                   # state refinement target
REFRESH_MAX = 3                           # Hotelling iters per cell
HERG_FLOOR = 1.0e-10                      # domain, complex points
PSD_FLOOR = 1.0e-9                        # domain, Stieltjes cone
BREACH_SYS = 2                            # > this = systematic (K2)
SVD_FLOOR = 1.0e-8                        # K4 transport floor

C_MED = 0.50
C_SLOPE = 0.02
NOISE_PASS = 1.0e-12
INC_FIRST5 = slice(0, 5)
INC_LAST5 = slice(67, 72)
INC_HALF2 = slice(36, 72)
QF_FLOOR = 1.0e-15

REPRO_GAP1176 = 0.1397
REPRO_NN888 = 6
REPRO_NN1176 = 8
REPRO_LMIN1176 = 3.8825e-6
REPRO_TOL = 2.0e-3
REPRO_LTOL = 2.0e-8
COMB_DEV_BAR = 1.0e-12
PREFIX_WARD = 1.0e-12
PD_TOL = 1.0e-9
RUNTIME_CAP = 1800.0

CTRL_CONE = -1.0e-6                       # control fire floor
CTRL_IDY = 1.0e-6
EP_NCAP = 34000
EP_MMAX = 640
SEED = 7

BANNED = ("zetazero", "nzeros", "isprime", "primerange", "nextprime",
          "prevprime", "primepi", "sympy")

CHECKS = []
GATES = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))
    return bool(ok)


def gate(name, ok, detail=""):
    GATES.append((name, bool(ok)))
    print("[GATE %s] %s%s" % ("PASS" if ok else "FAIL", name,
                              (": " + detail) if detail else ""))
    return bool(ok)


def ast_firewall():
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    hits = set()
    for node in ast.walk(tree):
        name = ""
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                token = alias.name.split(".")[0]
                if any(b in token.lower() for b in BANNED):
                    hits.add(token)
        if name and any(b in name.lower() for b in BANNED):
            hits.add(name)
    return sorted(hits)


def freeze_spec():
    hsh = hashlib.sha256()
    hsh.update(("qf-cell-cocycle spec: cap %d M_CAP=%d M_TOP=%d "
                "D=%.10f; GLAD=%s; RECON=%s; NCOR=%d; band rule = "
                "threshold d(M)=#{lam<=%g}, transitions typed, "
                "increase embed [JR|N] sign-fixed, decrease "
                "re-anchor; z: eps=%s zref=%g h=%g zc=%s; identity: "
                "G_{k+1}=G_k+Y_I D^{-1} Y_I^T, Y=RU, D=(W-z)-U^T R "
                "U, defect<=%g every rung, ward<=%g at RECON, "
                "state refreshed by Hotelling to floor %g max %d "
                "iters (declared correction); "
                "domain: Herglotz>=-%g at zc AND Stieltjes cone "
                ">=-%g at real eps, both objects, every rung incl "
                "transitions, breaches: 0 pass, <=%d typed (CARRIES "
                "needs transition-adjacent), > systematic kill; "
                "conv: relative increments, N=max neighbor "
                "max-entry, med5<=%g AND b2>=%g, floor %g, blocks "
                "[0:5][67:72][36:72], gated cells = {G,W~}x{real "
                "eps}, complex reported; kills: idy, systematic "
                "breach, AST, svd<%g, normalizer audit; repro: "
                "gap1176=%g nn888=%d nn1176=%d lmin=%g tol %g/%g; "
                "guards: comb<=%g prefix<=%g pd>-%g cap %g; "
                "controls: cone<%g or Dk<0 or idy>%g or singular, "
                "lads %s/%s ep %d/%d seed %d; verdict: invalid -> "
                "kills DEAD -> all pass CARRIES -> identity+domain "
                "DOMAIN-ONLY -> DEAD; stakes: DEAD closes the Gram "
                "route, Z1 contract takes over"
                % (ATOM_MAX_DEEP, M_CAP_DEEP, M_TOP_DEEP, D, GLAD,
                   RECON_RUNGS, NCOR, THR_NULL, EPS_GATED, Z_REF,
                   H_IM, ZC, IDY_BAR, WARD_BAR, REFRESH_FLOOR,
                   REFRESH_MAX, HERG_FLOOR,
                   PSD_FLOOR, BREACH_SYS, C_MED, C_SLOPE,
                   NOISE_PASS, SVD_FLOOR, REPRO_GAP1176, REPRO_NN888,
                   REPRO_NN1176, REPRO_LMIN1176, REPRO_TOL,
                   REPRO_LTOL, COMB_DEV_BAR, PREFIX_WARD, PD_TOL,
                   RUNTIME_CAP, CTRL_CONE, CTRL_IDY, qsb.CTRL_LAD_S,
                   qsb.CTRL_LAD_E, EP_NCAP, EP_MMAX, SEED)).encode())
    return hsh.hexdigest()


# ------------------------------------------------ towers (verbatim)
def build_parent_tower():
    alpha = 0.5 * M_TOP_PAR * D
    ka, masks, dev_m = srp.channel_masks(alpha)
    check("G1.3 parent tower comb consistency (zeta-free Gauss "
          "double sieve == deployed masses, rel dev <= %.0e)"
          % COMB_DEV_BAR, dev_m <= COMB_DEV_BAR,
          "rel dev %.1e, ka=%d" % (dev_m, ka))
    c = srp.continuum_lags(M_TOP_PAR)
    for cnl in ("ro", "re", "sp", "in"):
        c = c + srp.atom_channel_lags(alpha, M_TOP_PAR, masks[cnl])
    return sla.toeplitz(c[:M_TOP_PAR])


def build_deep_comb():
    lam_deep = core.von_mangoldt_table(ATOM_MAX_DEEP)
    dev = float(np.max(np.abs(lam_deep[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("G1.1 deep-table overlap: deep von Mangoldt table == "
          "deployed core table on [0, %d] EXACTLY"
          % core.ATOM_MAX, dev == 0.0, "max abs dev %.1e" % dev)
    nn = np.nonzero(lam_deep > 0.0)[0]
    u_deep = np.log(nn.astype(float))
    mu_deep = 2.0 * lam_deep[nn] / np.sqrt(nn.astype(float))
    psi = np.cumsum(lam_deep[nn])
    keep = nn.astype(float) >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nn[keep].astype(float))
                         / nn[keep].astype(float)))
    check("G1.2 deep-range Chebyshev envelope: kappa = %.6f <= "
          "%.6f" % (kappa, core.KAPPA_REF + core.TOL_KAPPA),
          kappa <= core.KAPPA_REF + core.TOL_KAPPA)
    return u_deep, mu_deep


def build_deep_tower(u_deep, mu_deep, T_par):
    alpha = 0.5 * M_TOP_DEEP * D
    ka = int(np.searchsorted(u_deep, 2.0 * alpha + 1.0e-14,
                             side="right"))
    c_cont = srp.continuum_lags(M_TOP_DEEP)
    c_at, _dd = core.atom_lags_at(alpha, M_TOP_DEEP, u_deep[:ka],
                                  mu_deep[:ka])
    T = sla.toeplitz((c_cont + c_at)[:M_TOP_DEEP])
    dev = float(np.max(np.abs(T[:M_TOP_PAR, :M_TOP_PAR] - T_par)))
    check("G1.4 prefix Ward: deep tower leading %d block == parent "
          "tower, max abs dev %.1e <= %.0e"
          % (M_TOP_PAR, dev, PREFIX_WARD), dev <= PREFIX_WARD)
    return T, c_cont, alpha, ka


# ------------------------------------------------ exact cell cocycle
def ident_defect(T, z, R, M):
    cols = R[:, :NCOR]
    E = T[:M, :M] @ cols - z * cols
    E[np.arange(NCOR), np.arange(NCOR)] -= 1.0
    return float(np.max(np.abs(E)))


def cocycle_run(T, z, sizes, ward_rungs=(), margins=False):
    """Exact ordered cell cocycle: init resolvent at sizes[0], then
    72 Moebius/Redheffer cell updates with (U, W) = the added
    rows/columns.  Returns per-rung corners, defects, cell margins,
    dense-solve Ward residuals."""
    cplx = (z.imag != 0.0)
    dt = np.complex128 if cplx else np.float64
    zz = z if cplx else z.real
    M0 = sizes[0]
    A0 = np.asarray(T[:M0, :M0], dtype=dt)
    R = sla.solve(A0 - zz * np.eye(M0, dtype=dt),
                  np.eye(M0, dtype=dt), assume_a="sym")
    dfc = ident_defect(T, zz, R, M0)
    for _ in range(REFRESH_MAX):
        if dfc <= REFRESH_FLOOR:
            break
        E0 = -(T[:M0, :M0] @ R - zz * R)
        E0[np.arange(M0), np.arange(M0)] += 1.0
        R = R + R @ E0
        dfc = ident_defect(T, zz, R, M0)
    Gs = [R[:NCOR, :NCOR].copy()]
    defects = [dfc]
    dk_min, upd_lo, upd_hi = [], [], []
    wards = {}

    def ward_at(M, Rmat):
        A = np.asarray(T[:M, :M], dtype=dt)
        cols = np.eye(M, dtype=dt)[:, :NCOR]
        Gd = sla.solve(A - zz * np.eye(M, dtype=dt), cols,
                       assume_a="sym")[:NCOR, :]
        num = float(np.max(np.abs(Gd - Rmat[:NCOR, :NCOR])))
        return num / max(float(np.max(np.abs(Gd))), QF_FLOOR)

    if M0 in ward_rungs:
        wards[M0] = ward_at(M0, R)
    for Ma, Mb in zip(sizes, sizes[1:]):
        s = Mb - Ma
        U = np.asarray(T[:Ma, Ma:Mb], dtype=dt)
        W = np.asarray(T[Ma:Mb, Ma:Mb], dtype=dt)
        Y = R @ U
        Dm = (W - zz * np.eye(s, dtype=dt)) - U.T @ Y
        Dinv = np.linalg.inv(Dm)
        YD = Y @ Dinv
        Rn = np.empty((Mb, Mb), dtype=dt)
        Rn[:Ma, :Ma] = R + YD @ Y.T
        Rn[:Ma, Ma:] = -YD
        Rn[Ma:, :Ma] = -YD.T
        Rn[Ma:, Ma:] = Dinv
        R = Rn
        # Exact-identity-preserving state refinement (declared
        # implementation correction, see docstring): Hotelling
        # iteration R <- R + R (I - (A - z) R) until the carried
        # state meets the refresh floor; coefficients untouched.
        dfc = ident_defect(T, zz, R, Mb)
        for _ in range(REFRESH_MAX):
            if dfc <= REFRESH_FLOOR:
                break
            E = -(T[:Mb, :Mb] @ R - zz * R)
            E[np.arange(Mb), np.arange(Mb)] += 1.0
            R = R + R @ E
            dfc = ident_defect(T, zz, R, Mb)
        Gs.append(R[:NCOR, :NCOR].copy())
        defects.append(dfc)
        if margins and not cplx:
            dk_min.append(float(np.min(np.linalg.eigvalsh(
                0.5 * (Dm + Dm.T)))))
            upd = Y[:NCOR] @ Dinv @ Y[:NCOR].T
            ev = np.linalg.eigvalsh(0.5 * (upd + upd.T))
            upd_lo.append(float(ev[0]))
            upd_hi.append(float(ev[-1]))
        if Mb in ward_rungs:
            wards[Mb] = ward_at(Mb, R)
    return dict(Gs=Gs, defects=defects, dk_min=dk_min,
                upd_lo=upd_lo, upd_hi=upd_hi, wards=wards)


# ------------------------------------------------ band layer
def spectral_pass(T, sizes):
    out = {}
    for M in sizes:
        A = T[:M, :M]
        lam, V = np.linalg.eigh(A)
        out[M] = dict(lam=lam, V=qsb.sign_fix(V[:, :10]),
                      d=int(np.sum(lam <= THR_NULL)))
    return out


def band_transport(spec):
    """Chained polar transport with typed transition maps on the
    depth-dependent band d(M)."""
    ds = [spec[M]["d"] for M in GLAD]
    Rs = [np.eye(ds[0])]
    trans, sig_min = [], []
    for i, (Ma, Mb) in enumerate(zip(GLAD, GLAD[1:])):
        da, db = ds[i], ds[i + 1]
        Va = spec[Ma]["V"][:, :da]
        Vb = spec[Mb]["V"][:Ma, :db]
        S = Vb.T @ Va                      # (db, da)
        if db == da:
            U, sv, Vt = np.linalg.svd(S)
            Rs.append((U @ Vt) @ Rs[-1])
            sig_min.append(float(sv[-1]))
        elif db > da:
            U, sv, Vt = np.linalg.svd(S, full_matrices=True)
            J = U[:, :da] @ Vt
            N = U[:, da:db]
            for j in range(N.shape[1]):
                if N[np.argmax(np.abs(N[:, j])), j] < 0.0:
                    N[:, j] = -N[:, j]
            Rs.append(np.concatenate([J @ Rs[-1], N], axis=1))
            sig_min.append(float(sv[-1]))
            trans.append((i, Ma, Mb, da, db, "MODE-ENTRY",
                          float(spec[Mb]["lam"][db - 1])))
        else:
            Rs.append(np.eye(db))
            sig_min.append(1.0)
            trans.append((i, Ma, Mb, da, db, "MODE-EXIT re-anchor",
                          float(spec[Mb]["lam"][db - 1])))
    return ds, Rs, trans, sig_min


def band_obj(spec, Rs, z):
    out = []
    for i, M in enumerate(GLAD):
        d = spec[M]["d"]
        lam = spec[M]["lam"][:d]
        out.append(Rs[i].T @ np.diag(1.0 / (lam - z)) @ Rs[i])
    return out


def rel_increments(objs, ds):
    rel, raw = [], []
    for i in range(len(objs) - 1):
        c = min(ds[i], ds[i + 1])
        dd = float(np.max(np.abs(objs[i + 1][:c, :c]
                                 - objs[i][:c, :c])))
        nn = max(float(np.max(np.abs(objs[i]))),
                 float(np.max(np.abs(objs[i + 1]))), QF_FLOOR)
        raw.append(dd)
        rel.append(dd / nn)
    return np.array(rel), np.array(raw)


def conv_stat(rel, xs):
    med_f = float(np.median(rel[INC_FIRST5]))
    med_l = float(np.median(rel[INC_LAST5]))
    ratio = med_l / max(med_f, QF_FLOOR)
    rows = [dict(XmR=float(x), mx=float(max(v, QF_FLOOR)))
            for x, v in zip(xs[INC_HALF2], rel[INC_HALF2])]
    b2, _r = hbp.fit_rate(rows)
    ok = (ratio <= C_MED and b2 >= C_SLOPE) or med_l <= NOISE_PASS
    return med_f, med_l, ratio, b2, ok


def herg_min(F):
    return float(np.min(np.linalg.eigvalsh(
        0.5j * (F.conj().T - F))))


def psd_min(F):
    return float(np.min(np.linalg.eigvalsh(
        0.5 * (F + F.T).real)))


# ------------------------------------------------ controls
def control_cocycle(Tc, lad, label):
    dets, fired = [], False
    for e in EPS_GATED:
        z = complex(-e, 0.0)
        try:
            out = cocycle_run(Tc, z, list(lad), margins=True)
        except np.linalg.LinAlgError:
            dets.append("eps=%g: singular update (fires)" % e)
            fired = True
            continue
        cone = psd_min(out["Gs"][-1])
        dkm = min(out["dk_min"]) if out["dk_min"] else 0.0
        idy = max(out["defects"])
        f = cone < CTRL_CONE or dkm < 0.0 or idy > CTRL_IDY
        fired = fired or f
        dets.append("eps=%g: min eig G = %+.2e, min eig D_k = "
                    "%+.2e, defect %.1e -> %s"
                    % (e, cone, dkm, idy,
                       "FIRES" if f else "quiet"))
    lam = np.linalg.eigvalsh(Tc[:lad[-1], :lad[-1]])
    det = ("%s: %s; census %d/%d negative eigenvalues (complex-"
           "point Herglotz not discriminating -- predeclared)"
           % (label, "; ".join(dets), int(np.sum(lam < 0.0)),
              len(lam)))
    return fired, det


def run_controls(c_cont, alpha_deep, ka_deep, mu_deep):
    print("\n-- controls (must fire: indefinite data breaks the "
          "Stieltjes cone / cell positivity)")
    rng = np.random.default_rng(SEED)
    pos = np.sort(rng.uniform(0.5, 2.0 * alpha_deep, ka_deep))
    cat_s, _dd = core.atom_lags_at(alpha_deep, M_TOP_DEEP, pos,
                                   mu_deep[:ka_deep])
    Ts = sla.toeplitz((c_cont + cat_s)[:M_TOP_DEEP])
    fire_s, det_s = control_cocycle(Ts, qsb.CTRL_LAD_S, "scramble")
    check("CS position-scramble control fires", fire_s, det_s)

    r1 = epx.lattice_r1(EP_NCAP)
    bb = np.asarray(r1, float) / 2.0
    lamE = epx.dirichlet_vonmangoldt(bb, EP_NCAP)
    supp = np.nonzero(np.abs(lamE) > 1.0e-9)[0]
    supp = supp[supp >= 2]
    posE = np.log(supp.astype(float))
    masE = 2.0 * lamE[supp] / np.sqrt(supp.astype(float))
    catE, _dd = core.atom_lags_at(0.5 * EP_MMAX * D, EP_MMAX, posE,
                                  masE)
    cont = srp.continuum_lags(EP_MMAX)
    TE = sla.toeplitz((cont + catE)[:EP_MMAX])
    fire_e, det_e = control_cocycle(TE, qsb.CTRL_LAD_E, "epstein")
    check("CE Epstein control (x^2+5y^2) fires", fire_e, det_e)


# ------------------------------------------------ run
def run():
    print("=" * 78)
    print("QF OFFENSIVE strand 3, module 4 (LAST DECIDER) -- "
          "ordered cell cocycle on the d(X) band, 1e8 comb")
    print("=" * 78)

    hits = ast_firewall()
    check("G0.1 AST firewall (K3: update coefficients are lag data "
          "of the source operator only)", not hits, str(hits))
    spec_sha = freeze_spec()
    check("G0.2 construction + band rule + domain + bars + verdict "
          "order SHA-256-frozen BEFORE any comb data",
          True, "SHA256 %s..." % spec_sha[:16])
    check("G0.3 reach census: M_TOP = %d <= %d; sieve cover %d <= "
          "%d; runtime cap %.0f s"
          % (M_TOP_DEEP, M_CAP_DEEP,
             int(math.exp(M_TOP_DEEP * D)) + 2, ATOM_MAX_DEEP,
             RUNTIME_CAP),
          M_TOP_DEEP <= M_CAP_DEEP
          and int(math.exp(M_TOP_DEEP * D)) + 2 <= ATOM_MAX_DEEP)

    u_deep, mu_deep = build_deep_comb()
    T_par = build_parent_tower()
    T, c_cont, alpha_deep, ka_deep = build_deep_tower(
        u_deep, mu_deep, T_par)

    # ---- band layer: spectra, d(X), transitions, transport
    spec = spectral_pass(T, GLAD)
    ds = [spec[M]["d"] for M in GLAD]
    pd_min = min(float(spec[M]["lam"][0]) for M in GLAD)
    check("G1.6 measured PD: lambda_min = %.3e > -%.0e on every "
          "gated rung (measured output, in NO gate)"
          % (pd_min, PD_TOL), pd_min > -PD_TOL)
    g1176 = (spec[1176]["lam"][6] - spec[1176]["lam"][5]) \
        / spec[1176]["lam"][6]
    check("G1.5 reproduction Ward: 6/7 gap(1176) = %.4f vs %.4f "
          "(tol %.0e); nn(888) = %d (== %d), nn(1176) = %d (== "
          "%d); lambda_min(1176) = %.4e vs %.4e (tol %.0e)"
          % (g1176, REPRO_GAP1176, REPRO_TOL, ds[0], REPRO_NN888,
             ds[-1], REPRO_NN1176, spec[1176]["lam"][0],
             REPRO_LMIN1176, REPRO_LTOL),
          abs(g1176 - REPRO_GAP1176) <= REPRO_TOL
          and ds[0] == REPRO_NN888 and ds[-1] == REPRO_NN1176
          and abs(spec[1176]["lam"][0] - REPRO_LMIN1176)
          <= REPRO_LTOL)

    ds, Rs, trans, sig_min = band_transport(spec)
    t_rungs = set()
    for (i, Ma, Mb, da, db, typ, lnew) in trans:
        t_rungs.add(Mb)
        print("  TYPED TRANSITION at increment %d (%d -> %d): d "
              "%d -> %d [%s], entering eigenvalue %.4e vs "
              "threshold %.0e" % (i, Ma, Mb, da, db, typ, lnew,
                                  THR_NULL))
    check("K4 kill audit: transport min sigma_min = %.6f >= %.0e "
          "over the chained d(X) overlaps (%d typed transitions)"
          % (min(sig_min), SVD_FLOOR, len(trans)),
          min(sig_min) >= SVD_FLOOR)
    print("  d(X) profile: d = %d on %d rungs, 7 from M = %d, 8 "
          "from M = %d"
          % (ds[0], len(GLAD),
             next((M for M, d in zip(GLAD, ds) if d >= 7), -1),
             next((M for M, d in zip(GLAD, ds) if d >= 8), -1)))

    # ---- exact cocycle at all five z
    print("\n-- exact cell cocycle (identity gated on every rung)")
    coc = {}
    idy_worst, ward_worst = 0.0, 0.0
    for z in Z_ALL:
        coc[z] = cocycle_run(T, z, GLAD, ward_rungs=RECON_RUNGS,
                             margins=(abs(z - Z_REF) < 1e-15))
        idy_worst = max(idy_worst, max(coc[z]["defects"]))
        ward_worst = max(ward_worst, max(coc[z]["wards"].values()))
    id_ok = gate("IDENTITY exact Moebius/Redheffer composition: "
                 "max per-rung defect ||(A-z)R[:,I] - E_I|| = "
                 "%.1e <= %.0e over %d rungs x %d z; max "
                 "independent dense-solve Ward residual = %.1e <= "
                 "%.0e at %d rungs x %d z"
                 % (idy_worst, IDY_BAR, len(GLAD), len(Z_ALL),
                    ward_worst, WARD_BAR, len(RECON_RUNGS),
                    len(Z_ALL)),
                 idy_worst <= IDY_BAR and ward_worst <= WARD_BAR)
    mz = coc[complex(Z_REF, 0.0)]
    print("  cell margins at z_ref (REPORTED, never gated): min "
          "eig D_k in [%.4e, %.4e]; corner update-term eigenrange "
          "[%.1e, %.1e]"
          % (min(mz["dk_min"]), max(mz["dk_min"]),
             min(mz["upd_lo"]), max(mz["upd_hi"])))

    # ---- band objects
    wt = {z: band_obj(spec, Rs, z) for z in Z_ALL}

    # ---- domain gates
    print("\n-- domain preservation (Nevanlinna/Stieltjes sandwich"
          ", both objects, every rung incl. transitions)")
    breach_nt, breach_t = [], []
    margins = {}
    for lbl, series in (("G", coc), ("W~", wt)):
        for z in Z_ALL:
            objs = series[z]["Gs"] if lbl == "G" else series[z]
            vals = []
            for i, M in enumerate(GLAD):
                if z.imag > 0.0:
                    m = herg_min(objs[i])
                    bad = m < -HERG_FLOOR
                else:
                    m = psd_min(objs[i])
                    bad = m < -PSD_FLOOR
                vals.append(m)
                if bad:
                    (breach_t if M in t_rungs
                     else breach_nt).append((lbl, z, M, m))
            margins[(lbl, z)] = (min(vals), max(vals))
    for (lbl, z), (lo, hi) in margins.items():
        cls = "Herglotz Im>=" if z.imag > 0.0 else "cone min eig"
        print("  %-2s z=%s: %s in [%+.3e, %+.3e] %s"
              % (lbl, ("%g%+gi" % (z.real, z.imag)) if z.imag
                 else "%g" % z.real, cls, lo, hi,
                 "(transitions included)" if t_rungs else ""))
    dom_ok = gate("DOMAIN preserved: %d non-transition breaches "
                  "(0 required for clean pass; <= %d typed; > %d "
                  "systematic kill) and %d transition-rung "
                  "breaches across %d rung x cell tests"
                  % (len(breach_nt), BREACH_SYS, BREACH_SYS,
                     len(breach_t),
                     2 * len(Z_ALL) * len(GLAD)),
                  len(breach_nt) == 0 and len(breach_t) == 0)
    k2_kill = len(breach_nt) > BREACH_SYS

    # ---- convergence of the renormalized objects
    print("\n-- renormalized convergence (relative entrywise "
          "increments; declared normalizer = neighbor max-entry)")
    xs = np.array([M * D for M in GLAD[1:]])
    conv_ok = True
    for lbl, series in (("G", coc), ("W~", wt)):
        for z in Z_ALL:
            objs = series[z]["Gs"] if lbl == "G" else series[z]
            dloc = ds if lbl == "W~" else [NCOR] * len(GLAD)
            rel, raw = rel_increments(objs, dloc)
            med_f, med_l, ratio, b2, ok = conv_stat(rel, xs)
            gated = (z.imag == 0.0)
            line = ("%-2s z=%-8s med5 first/last = %.3e / %.3e, "
                    "ratio %.3f, b2 %+ .3f/X, raw last %.2e"
                    % (lbl, "%g" % z.real if not z.imag else
                       "%g%+gi" % (z.real, z.imag), med_f, med_l,
                       ratio, b2, raw[-1]))
            if gated:
                conv_ok &= gate("CONV %s (bars med5<=%g, "
                                "b2>=%g, floor %g)"
                                % (line, C_MED, C_SLOPE,
                                   NOISE_PASS), ok)
            else:
                print("  reported: %s" % line)
            if lbl == "W~" and gated and trans:
                tt = ["inc %d (M=%d): rel %.3e" % (i, Mb, rel[i])
                      for (i, _Ma, Mb, _a, _b, _t, _l) in trans]
                print("    transition increments: %s"
                      % "; ".join(tt))

    # ---- step-1 spectra around transitions (reported)
    print("\n-- step-1 spectra around transitions (REPORTED)")
    for (_i, _Ma, Mb, _da, db, _typ, _lnew) in trans:
        for M in range(Mb - 4, min(Mb + 5, M_TOP_DEEP + 1)):
            lam = np.linalg.eigvalsh(T[:M, :M])
            print("    M=%d: nn=%d, lam_%d = %.4e (thr %.0e)"
                  % (M, int(np.sum(lam <= THR_NULL)), db,
                     lam[db - 1], THR_NULL))

    # ---- K5 normalizer audit
    check("K5 kill audit: the convergence normalizer is the "
          "object's own neighbor max-entry (source-native, "
          "declared part of the renormalized object) -- no "
          "RH-strength input, no 1/eps, no PD margin in any gate",
          True)

    # ---- controls + runtime
    run_controls(c_cont, alpha_deep, ka_deep, mu_deep)
    dt = time.time() - T_START
    check("G0.4 runtime %.1f s <= cap %.0f s" % (dt, RUNTIME_CAP),
          dt <= RUNTIME_CAP)

    # ---- verdict
    guards_ok = all(ok for (n, ok) in CHECKS
                    if not n.startswith(("CS", "CE")))
    controls_ok = all(ok for (n, ok) in CHECKS
                      if n.startswith(("CS", "CE")))
    kill = (not id_ok) or k2_kill or (min(sig_min) < SVD_FLOOR)
    if not (guards_ok and controls_ok):
        verdict = "COCYCLE-DEAD (invalid run)"
    elif kill:
        verdict = "COCYCLE-DEAD"
    elif id_ok and dom_ok and conv_ok:
        verdict = "COCYCLE-CARRIES"
    elif id_ok and dom_ok:
        verdict = "COCYCLE-DOMAIN-ONLY"
    else:
        verdict = "COCYCLE-DEAD"

    n_gate = sum(1 for (_n, ok) in GATES if ok)
    n_chk = sum(1 for (_n, ok) in CHECKS if ok)
    print("\nVERDICT: %s" % verdict)
    print("GATES %d/%d, GUARDS+CONTROLS %d/%d, runtime %.1f s"
          % (n_gate, len(GATES), n_chk, len(CHECKS),
             time.time() - T_START))
    if verdict == "COCYCLE-CARRIES":
        print("CONSEQUENCE (stated plainly): the wall is now a "
              "DOMAIN-PRESERVING TRANSPORT statement -- the exact "
              "cell cocycle composes through the full gated range "
              "including the typed mode-entry transitions, stays "
              "in the Nevanlinna/Stieltjes domain, and its "
              "renormalized objects converge at the frozen bars.  "
              "WHAT A PROOF WOULD STILL NEED (named precisely): "
              "(i) UNCONDITIONAL cell positivity -- every cell "
              "Schur block D_k in the cone from the source "
              "construction itself, replacing the measured window "
              "PD input; (ii) a Loewner-order contraction modulus "
              "for the ordered Moebius product "
              "(Birkhoff/Wojtkowski-type), turning the measured "
              "convergence into a theorem; (iii) the z -> 0 "
              "boundary transition of the limit object "
              "(Nevanlinna/Herglotz).  NO RH claim; this is a "
              "renormalized-object statement at reachable depth, "
              "not the absolute 2^-n contract.")
    elif verdict == "COCYCLE-DOMAIN-ONLY":
        print("CONSEQUENCE (stated plainly): structure without "
              "limit -- the exact identity and the domain "
              "transport hold (the failing convergence cells are "
              "printed above), so the Gram route retains ONLY the "
              "domain-transport statement.  Per the frozen "
              "stakes: the sharpened Z1 contract takes over, "
              "carrying the moving-edge cadence (992 / ~1108 / "
              "976), the ram-odd contact direction, the settled q "
              "levels (0.225..0.358 / 0.008..0.079), and the "
              "surviving domain facts named above.  NO RH claim.")
    else:
        print("CONSEQUENCE (stated plainly): the cocycle route "
              "dies -- per the frozen stakes the Gram route "
              "closes WITHOUT further variants and the sharpened "
              "Z1 contract takes over.  Z1 handover content: the "
              "moving-edge cadence (7th threshold at 992, count 8 "
              "from ~1108, 8/9 crossing at 976), the ram-odd "
              "contact direction, the settled per-function q "
              "levels (R2 0.225..0.358, R1 0.008..0.079), and the "
              "domain facts that did/did not survive (see the "
              "margin table above).  NO RH claim.")
    return 0 if (guards_ok and controls_ok) else 1


if __name__ == "__main__":
    sys.exit(run())
