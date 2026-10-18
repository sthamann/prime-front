#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zeroframe_unification_probe -- PRIME.WALL.ZEROFRAME.UNIFICATION.01
(EXPLORATION ONLY, experiments/; 2026-08-11.  THE STRUCTURAL QUESTION:
are W1 and W2 two minors of ONE small spectral frame operator?)

THE CONJECTURE UNDER TEST (ZEROFRAME).  The wall split of the deployed
ladder is M_h > 0 <=> B_h > 0 and W1_h and W2_h (port_tangent_schur /
CLXX-CLXXVIII; the B-half certified via the P_G chain).  W1 (the
Christoffel floor, CLXXXIV: FLOOR/mu1 from classical supply) and W2
(the background cancellation, CLXXXV: m = n - q along the measured
critical direction) both close from FEW stable sub-gamma_1 frequency
carriers (omega <= 5.25) read through the SAME verified-zero /
classical-tail currency (CLXXXIX supply, CXCIII consumption).  IF a
common small matrix F_h exists with W1_h = principal minor and W2_h =
complementary Schur complement and M_h > 0 <=> F_h > 0, the entire
zero supply collapses into ONE frame-operator statement and the all-h
question becomes a uniform lower frame bound on a FIXED small
subspace.  This probe BUILDS the natural candidate and MEASURES the
conjecture; every branch of the outcome (unified / half / refuted /
dimension grows) is a first-class typed finding.

THE CANDIDATE (frozen).  Per rung h (the CLXXXV wall operator
K_h = odd_toeplitz(c_ar + c_at, M), lam_min(K_h) = m_h = W2_h along
the eigen-direction v_h -- the trivial-but-exact Schur collapse
n - q = m at the eigenvector seat, CXLIII/CLI ward):
  V_h  = span{ v_h,  p_1, ..., p_K },
  p_j[i] = cos(omega_j (i + 1/2) D) / ||.||,   omega_j = pi j / Lu,
where Lu = uL - u0 is the deployed deep window of the per-rung
B-covering cut n_c = cB (round-62 rule, CLXXXV verbatim) -- the SAME
frame frequencies whose carriers hold share ~1.0 of PARITH (CLXXXV)
and which the W1 fold supply reads (alias band omega <= 5.25).  The
candidate frame operator and its basis Gram are
  F_h[a, b] = <x_a, K_h x_b>,     N_h[a, b] = <x_a, x_b>,
with EVERY entry computed from SOURCE-SIDE READS (archimedean lag
read e_ar(ab) = c_ar . W_ab plus per-atom reads mu_k w_ab(u_k) of the
polarized pair weight W_ab = [lw(x_a + x_b) - lw(x_a) - lw(x_b)]/2,
lw = the T163 correlation weights), never from eigendata of F or of
any target matrix; and each entry is INDEPENDENTLY re-read in
ZERO-READ COORDINATES via the explicit formula on the verified cache
(CLXXXIX input class, CXCIII machinery verbatim):
  F_zero[a, b] = e_ar(ab) + HEAD_ab(n_c) + TCONT_ab + PARITH_hat_ab,
  PARITH_hat_ab = -4 Sum_{gamma <= T_c} Re phihat_ab(gamma) - TRIV
                  - RampAtoms + RampCont + ExtCont - ExtAtoms,
  |F_prime[a, b] - F_zero[a, b]| = |PARITH_ab - PARITH_hat_ab|
                <= TAILB_ab   (Abel/N(T) Rosser corridor T_c -> T0,
                               beyond-T0 pad, dps pad -- CXCIII
                               direct_read formula verbatim),
warded per rung x entry (kill).  The v_h seat is MEASURED direction
data (DIRECTION-CONDITIONAL, disclosed exactly as CLXXXV/CXCIII
declare it); the carriers are a-priori window geometry; W1_h and
W2_h are computed by the CLXXXIV and CLXXXV machinery INDEPENDENTLY
of F_h (anti-circularity: the minor test compares, never defines).

WHAT IS MEASURED (typed; kills only where marked WARD).
 (a) F-CONSTRUCTION: F_h, N_h at K = KMAX = 6 on the surface (the
     39-step parent surface joined rung-exactly by kz to the CLXXXV
     ladder + the remaining CLXXXV surface rungs, 67 total) and the
     DEEP block (8 rungs of the 4e6 table, CXCIII selection verbatim,
     FLOAT-LEVEL declared).  Wards: POL (reads == x^T K y),
     ATOM-ID (c_at . W_ab == sum of atom reads), RECON (CXCIII
     bookkeeping, no zeros), HEART per entry (|PARITH - hat| <=
     TAILB), SPOT (one entry per rung re-read through CXCIII
     direct_read verbatim, bit-consistency), N-pencil PD census.
 (b) THE MINOR TEST.
     W2 side: with f0 = F[1:, 0], C_K = F[1:, 1:] (the carrier
     principal minor), q_K = f0^T C_K^{-1} f0, the EXACT identities
       Schur_K = F00 - q_K = 1/(F^{-1})_{00},
       det F = Schur_K det C_K,     F00 = m
     are warded (identity bars 1e-6, conditioned linear algebra; the
     <= 1e-8 census is REPORTED per rung).  The typed content: the
     Schur complement reproduces W2 as Schur_K = m (1 - rho_K) with
     the EXPLICIT measured positive factor 1 - rho_K, rho_K = q_K/m
     = the v <-> carrier overlap fraction; positivity of the factor
     on every rung is the W2-AS-SCHUR statement, the factor ladder is
     printed.  W1 side: W1_h = FLOOR/mu1 (CLXXXIV rung_band +
     rung_assembly verbatim; certified rungs), plus the everywhere-
     defined tiers b_sup/mu1 and truth = lam_min(G_core)/mu1, against
     the normalized principal minor lampen(C_K)/mu1 (pencil with the
     carrier Gram).  Frozen match rules: W1-MINOR-MATCHED iff
     |log10 ratio| <= W1_TOL_DEX = 0.5 on >= 0.8 of joined rungs
     (vs the truth tier); W1-MINOR-CALIBRATED iff the ratio's
     jackknife slope vs log h has |b| <= 0.30 (one h-stable positive
     normalization); else W1-MINOR-DIVERGES(med dex, slope).
 (c) EQUIVALENCE: lampen(F_h | N_h) == m_h warded (COMPRESS,
     1e-6 rel; v in V_h pins the compression EXACTLY, so
     M_h > 0 <=> F_h > 0 holds STRUCTURALLY through the v-seat --
     both directions, warded not assumed); the honest census of what
     the FIXED carrier space detects without the v-seat:
     lampen(C_K | N_C)/m per rung (>= 1 by compression), and the
     controls: does F go indefinite / does the carrier block go
     indefinite when the world breaks (smooth per rung lam_sm < 0
     KILL; Epstein + scramble at kz 9 lam_min < 0 KILL; their
     zero-read HEART must BREAK: scramble >= SCR_MIN = 1 entries
     KILL, Epstein census typed; off-line impostor gamma_1 -> beta =
     0.75 FE-quadruple shifts the (0,0) zero read by >= 10 x the
     genuine residual KILL -- CLXXXIX/CXCIII controls verbatim).
 (d) DIMENSION LAW: K*_rho(h) = min{K <= KMAX: rho_K >= RHO_BAR =
     0.90} (the overlap saturation seat) and K*_cap(h) = min{K:
     lampen(C_K|N_C)/m <= CAP_BAR = 2.0} (the carrier block prices
     the wall floor to a factor 2), both censored at KMAX + 1;
     jackknife slopes vs log h; typed DIM-FIXED(K* med, slope
     consistent with 0) / DIM-GROWS(slope, law).  The omega <= 5.25
     in-band census of the K frozen carriers is printed per rung.
 (e) FRAME-BOUND CURVE (the deliverable): c_h = lampen(F_h)/mu1(h)
     (== shat_h = m/mu1 by the warded compression -- printed as
     such, no new content) and the DECISIVE carrier-only curve
     c_carr_K(h) = lampen(C_K | N_C)/mu1(h) at K = 2 (the CLXXXV
     n90 seat) and K = KMAX, across surface + deep; jackknife trend
     vs alpha typed FRAME-FLAT(|slope| <= 0.05 dex/alpha) /
     FRAME-RISES / FRAME-FALLS(slope) -- this curve decides between
     the frame route and the Riccati route as the all-h contract.
     If DIM-FIXED and FRAME-FLAT/RISES the reduced contract
     PRIME.WALL.ZEROFRAME.UNIFORM.01 is stated verbatim; else the
     measured growth law is stated instead (the honest RH-hard
     reading).
 (f) GATES: tau-screens (jackknife log-log vs log m, bands PASS
     |s| <= 0.30 / RELOC >= 0.70) on 1 - rho_KMAX, c_carr_2,
     c_carr_KMAX, and the W1 ratio; SIGN-RESOLUTION census: the
     zero-read determines sign(lam_min F) iff the entry-wise TAILB
     perturbation bound ||dF||_2 / lammin(N) < lampen(F);
     zeros-needed anatomy (CXCIII declared main-term approximation)
     on unresolved rungs.

REPRODUCTION WARDS (kill; [full] = frozen run only): parent census
42/41/39 + v901 minB/gap (MINB_REF 0.679 rtol 2e-2, GAP_REF
0.052/0.888 rtol 5e-2); CLXXXV ladder 67 rungs [full], m > 0 all +
pivot collapse <= 1e-9 on SUBSET, shat band (0.502, 1.027, 2.185)
tol 1.5e-3 [full], cB coverage N/N; zero-cache wards Z1-Z4 (census
7000, corridor both sides per index, |zeta| spot <= 1e-6 at 24
geomspaced ordinates, T_c < T0) CLXXXIX verbatim; Abel base in
[1e-4, 4e-4]; Buethe table soundness; deep-table prefix byte-exact;
CLXXXIV per-rung kill wards on the W1 chain (fold soundness <= 0,
domination <= 1e-12, Loewner >= -1e-9, L5 <= 1e-9, grid <= 1e-9,
v_lo recon + soundness, FLOOR <= truth, surface cert census == 7
[full]); s_P >= mu1 39/39.

VERDICT (frozen enums, decided by these rules and nothing else):
  V0 headline: ZEROFRAME-UNIFIED iff (W2-AS-SCHUR exact-with-factor
     AND W1-MINOR-MATCHED AND COMPRESS ward green AND DIM-FIXED both
     laws); ZEROFRAME-HALF(W2) iff W2 side exact-with-positive-factor
     and COMPRESS green but W1-MINOR not MATCHED; ZEROFRAME-REFUTED
     iff an exact W2/compression identity ward fails structurally
     (not numerically) or the Schur factor goes non-positive on a
     truth rung.
  V1 W2-AS-SCHUR-EXACT-WITH-FACTOR(factor band; 1e-8 census n/N) /
     W2-SCHUR-BROKEN.
  V2 W1-MINOR-MATCHED(frac) / W1-MINOR-CALIBRATED(slope) /
     W1-MINOR-DIVERGES(med dex, slope).
  V3 EQUIV-SEAT-CARRIED(N/N; controls wall k/2 + heart counts;
     carrier-only detection n/2) -- the equivalence is exact and
     carried by the v-seat; the carrier-only detection census is the
     honest content.
  V4 DIM-FIXED(K*_rho med, K*_cap med) / DIM-GROWS(slopes) /
     DIM-CENSORED(counts at KMAX).
  V5 FRAME-FLAT/RISES/FALLS(slope dex/alpha, c_carr bands) +
     ZEROREAD(entries, worst heart slack dex, SIGN-RESOLVED n/N) +
     SCREENS(...) + DISCRIMINATION(scramble entries, impostor ratio).
DEAD overrides: kill wards -> PIPELINE-BROKEN / WARD-BROKEN /
ALGEBRA-BROKEN as tagged.

FROZEN BARS: KMAX = 6; K_SMALL = 2 (CLXXXV n90 med, cited); OMEGA_C
= 5.25 (inherited CLV/CLXXXV); RHO_BAR = 0.90; CAP_BAR = 2.0;
W1_TOL_DEX = 0.5; MATCH_FRAC = 0.8; POL_WARD = 1e-10; ATOM_ID_WARD
= 1e-9; RECON_TOL = 1e-9 (CXCIII); SPOT_WARD = 1e-9; F00_WARD =
1e-10 on the CLXXXV W3 energy scale max(1, |E_at(0,0)|) (amendment
A1; the raw relative deviation is reported); ID_WARD_NUM = 1e-6
(det/pivot/Schur identity, conditioned linear algebra; the 1e-8
census reported); COMPRESS_WARD = 1e-6; MREL_WARD = 1e-10 (eigh m
vs build_rung m); SCR_MIN = 1 at the declared control cut = truth
kz-9 covering cut, fallback NB_MED = 17 (amendment A2); IMP_BETA =
0.75; IMP_RATIO_MIN = 10; TREND_FLAT = 0.05; SLOPE_PASS/RELOC =
0.30/0.70 (w2 verbatim); N_Z = 7000; ZETA_TOL = 1e-6; NS_ZETA = 24;
CORR_EPS = 1e-6; DPS_ERR = 1e-9; ABEL_BAND = (1e-4, 4e-4); N_DEEP =
8 (smoke 2); CTRL_KZ = 9; scramble seed 1; runtime cap declared:
25 min.  Smoke mode ZFRAME_SMOKE=1: CLXXXV ladder kz <= 30, joined
surface first 8 rows by h, deep 2, full-only wards deferred
(disclosed prints).

ANTI-CIRCULARITY (frozen): F_h entries are source-side lag reads
(archimedean geometry + prime-power atoms) cross-warded against the
zero side of the explicit formula on the EXTERNAL-CITED verified
cache (mpmath.zetazero dps 15 builder, disclosed CLXXXIX; corridor +
independent |zeta| spot wards here); no eigendata of F_h, M_h or any
target matrix enters any entry, bound or supply; v_h is a declared
MEASURED direction (DIRECTION-CONDITIONAL, CLXXXV pedigree); W1_h /
W2_h enter the minor test only as independently computed comparison
columns.  PEDIGREE: gamma_1, Platt-Trudgian T0 = 3e12, Rosser 1941
N(T), Buethe 2018, B_PSI -- cited constants exactly as in
CLXXXIV/CLXXXIX/CXCIII.  RNG: none except the declared scramble
control (seed 1).

PRE-FREEZE SIZING DISCLOSURE (2026-08-11, before freezing): the
construction was sized on THREE joined rungs (kz 23/16/52) with one
throwaway scratch script (deleted), and the following numbers were
SEEN before this spec was frozen: ladder join 39/39; polarization
identity <= 2.8e-16; split identity <= 1.7e-16; zero-read heart
passes with ~2 dex slack (e.g. 2.3e-05 <= 2.3e-03); rho at K = 6 =
0.900/0.996/0.906 (the v <-> carrier overlap is LARGE -- the Schur
factor 1 - rho is small-positive, NOT ~1); lampen(F)/mu1 = shat to
3 digits (0.598/1.620/1.437 -- the v-seat pins the compression);
basis Gram cond 2.5e3..2.8e4; and the W1 raw scale gap: truth
s_P/mu1 = 2.3e3/1.9e4/7.8e4 vs lampen(C)/mu1 = O(1) -- a 3.3..4.9
dex offset, i.e. the strict W1-minor identity is EXPECTED to fail
and the probe will type how (MATCHED is near-excluded, the honest
question is CALIBRATED vs DIVERGES).  RHO_BAR = 0.90 and CAP_BAR =
2.0 were frozen AFTER seeing the three rho values (0.90 is the
smallest seen at K = 6); W1_TOL_DEX/MATCH_FRAC are generic dex
bars; ID_WARD_NUM = 1e-6 was set from the conditioning estimate
(cond(F) ~ 1e7 x eps), with the mission's 1e-8 target kept as a
reported census.  No enum or success rule was tuned to make any
branch pass: every branch is a typed finding.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): THREE smoke
runs (ZFRAME_SMOKE=1: 19-rung reduced CLXXXV ladder, 8 joined
surface rows, 2 deep), full fail-first history, nothing omitted.
SMOKE-1 (v0, exit 1, 12.8 s, 43/44 checks): ONE fail plus ONE
vacuously-passing control, both repaired by scale/bookkeeping
amendments, no structural bar or enum moved:
 (i) B1 F00 == m read 3.90e-07 > 1e-8 on the RAW relative scale.
     DIAGNOSIS: F00 = e_ar + E_at(0,0) is a six-digit cancellation
     down to m ~ 1e-4 while the float-eigh reference m carries
     eps x ||K_h|| ~ 1e-10 absolute noise -- the raw relative
     measure divides that noise by the cancelled m, not by the
     energy scale the identity lives on.  AMENDMENT A1: B1 measures
     |F00 - m| / max(1, |E_at(0,0)|) <= 1e-10 -- exactly the
     CLXXXV W3 energy-bookkeeping convention and a TIGHTER absolute
     bar; the raw relative worst stays printed as a reported
     number.  SMOKE-1 value on the A1 scale: 2.09e-13.
 (ii) G2/G3: both kz-9 control combs (Epstein, scramble) have NO
     covering cut of their own (cert_B never goes positive -- the
     control's certificate machinery already fails, which is
     itself part of the firing), so v0's heart read was skipped
     and G2 passed VACUOUSLY.  AMENDMENT A2: the control heart is
     read at the DECLARED control cut = the truth kz-9 covering
     cut (fallback NB_MED = 17); an invalid control cut now FAILS
     G2 instead of escaping it.
SMOKE-2 (v0 + A1/A2, exit 0, 12.8 s, 44/44): all green; exposed
ONE counting defect: the control heart census printed 49/28
(full symmetric matrix instead of the 28 upper-triangle entries).
AMENDMENT A3: the census counts upper-triangle entries; the
SCR_MIN = 1 bar is unaffected.
SMOKE-3 (v0 + A1/A2/A3, expected 44/44): the confirmation pass.
SMOKE-2 measured content the frozen run must be consistent with
(reduced ladder -- the frozen run decides all full-surface
numbers): structural wards green (POL 8.3e-13, ATOM-ID 7.5e-13,
RECON 1.3e-14, HEART all 280 entries with slack med +2.60 dex,
SPOT 0.0, m-rel 0.0, F00(A1) 2.1e-13, Schur pivot 5.0e-08 /
det 2.5e-08 <= 1e-6 with 1e-8 census 8/10, COMPRESS 3.9e-07);
rho(K=6) med 0.832, factor band 2.3e-03..2.7e-01 positive 10/10;
W1-MINOR-DIVERGES med -3.43 dex (matched 0/8; the sizing
disclosure anticipated this); DIM-CENSORED (K*_rho censored 7/10
at KMAX = 6, K*_cap 4/4/5); c_carr(2) band 26..4386 falling,
c_carr(6) band 0.57..2.02 FLAT (+0.049 dex/alpha); scramble +
Epstein wall-level fire and break the zero-read heart at the A2
control cut (worst 1.7e+03 / 6.0e+02 x TAILB); impostor 6.8e+03 x
genuine residual; SIGN-RESOLVED 0/10 at N_Z = 7000 (TAILB-priced,
consistent with CXCIII); smoke verdict pinned by the frozen rules:
ZEROFRAME-HALF(W2).  No bar, band, count, rule or enum moved after
SMOKE-3 beyond A1/A2/A3 above.

HONEST SCOPE + NO-GO (stated once, repeated in the verdict): every
statement is per-rung; the v-seat is a MEASURED direction; the deep
block is FLOAT-LEVEL; W1 columns exist only on the joined 39-step
surface (deep W1 not recomputed here -- CLXXXIV's deep census is
cited, not consumed); a finite verified-zero sum can never prove RH;
the equivalence M_h > 0 <=> F_h > 0 through the v-seat is exact but
NOT a reduction of the wall (the seat is per-rung data); only the
carrier-only curve at FIXED K could carry an all-h contract, and its
trend is measured, not asserted.  NO RH claim.  No marker moves, no
promotion, no ledger row, stdout only, no edits outside
experiments/.

FIREWALL: AST scan (banned ids zetazero / nzeros / primerange /
isprime / primepi / nextprime / prevprime -- the cache builder is a
separate disclosed script, CLXXXIX); v563 READ-ONLY; RNG only in the
declared scramble control; the verified cache enters ONLY the zero
side of the explicit-formula ward and the impostor control, never
any construction.

Sources (read-only, SPEC-SHA prefix-warded): exterior_pg_schur_probe
(parent, 084c9689 full), w2_pairing_structure_probe (CLXXXV,
8db29e6e), w1_assembly_certificate_probe (CLXXXIV, 37a5e259),
w2_verified_supply_consumption_probe (CXCIII, 921140fa),
j16_verified_zero_supply_probe (CLXXXIX, machinery pattern),
subgamma_fourier_bound_probe (c7d8810c), monotone_composition_probe
(bed53f23), vfloor_headroom_probe (9ffe771d),
lowfreq_discrepancy_gain_probe (be867853), deep_blind_holdout_probe
(ext tables), v563_paper2_readouts (core).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/zeroframe_unification_probe.py
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

import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY)
import bfloor_pg_dominance_probe as base  # noqa: E402  (READ-ONLY)
import exterior_pg_schur_probe as parent  # noqa: E402  (READ-ONLY)
import w2_pairing_structure_probe as w2  # noqa: E402  (READ-ONLY)
import subgamma_fourier_bound_probe as subg  # noqa: E402 (READ-ONLY)
import lowfreq_discrepancy_gain_probe as lf  # noqa: E402 (READ-ONLY)
import deep_blind_holdout_probe as deep  # noqa: E402  (READ-ONLY)
import w1_assembly_certificate_probe as asm  # noqa: E402 (READ-ONLY)
import w2_verified_supply_consumption_probe as cxc  # noqa: E402

SMOKE = os.environ.get("ZFRAME_SMOKE", "") == "1"

PARENT_SHA = ("084c968964f0ab6e0e852b29c75c210e324bcf63106d6858"
              "3048910992d92da4")
PREFIXES = dict(w2="8db29e6e", asm="37a5e259", cxc="921140fa",
                subgamma="c7d8810c")

ZC_NPY = os.path.join(_HERE, "verified_zeros_n7000.npy")
N_Z = 7000
ZETA_TOL = 1.0e-6
NS_ZETA = 24
CORR_EPS = 1.0e-6
ABEL_BAND = (1.0e-4, 4.0e-4)

KMAX = 6
K_SMALL = 2
OMEGA_C = w2.OMEGA_C
RHO_BAR = 0.90
CAP_BAR = 2.0
W1_TOL_DEX = 0.5
MATCH_FRAC = 0.8
POL_WARD = 1.0e-10
ATOM_ID_WARD = 1.0e-9
RECON_TOL = 1.0e-9
SPOT_WARD = 1.0e-9
F00_WARD = 1.0e-10
ID_WARD_NUM = 1.0e-6
ID_CENSUS = 1.0e-8
COMPRESS_WARD = 1.0e-6
MREL_WARD = 1.0e-10
SCR_MIN = 1
IMP_BETA = 0.75
IMP_RATIO_MIN = 10.0
TREND_FLAT = 0.05
N_DEEP = 2 if SMOKE else 8
N_SURF_JOIN = 8 if SMOKE else 39
KZ_TOP = 30 if SMOKE else w2.KZMAX
CTRL_KZ = 9
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

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
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def band(v):
    v = np.asarray(v, float)
    return float(np.min(v)), float(np.median(v)), float(np.max(v))


def lampen(F, N):
    """lam_min of the pencil (F, N): min eig of N^{-1/2} F N^{-1/2};
    None if N is not PD (counted by the caller)."""
    try:
        L = np.linalg.cholesky(0.5 * (N + N.T))
    except np.linalg.LinAlgError:
        return None
    Li = np.linalg.inv(L)
    Fh = Li @ F @ Li.T
    return float(np.linalg.eigvalsh(0.5 * (Fh + Fh.T))[0])


def frame_of(r, gam, s2t, inv2, inv3, do_spot=False,
             nc_override=None):
    """The candidate frame operator of one rung: exact source-side
    F/N + the zero-read of every entry with per-entry TAILB.
    Returns None if the rung has no covering cut (unless a control
    cut is forced via nc_override, amendment A2)."""
    if nc_override is None and r["ncB"] <= 0:
        return None
    h, M, D = r["h"], r["M"], r["D"]
    alpha, uu, mu = r["alpha"], r["uu"], r["mu"]
    nc = int(nc_override) if nc_override is not None \
        else int(r["ncB"])
    Ng = r["Ng"]
    if nc < 2 or nc >= Ng - 1:
        return None
    u0 = math.log(nc + 1.0)
    uL = math.log(float(Ng))
    Lu = uL - u0
    # the wall operator (CLXXXV verbatim ingredients)
    c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0], float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    Kt = core.odd_toeplitz(c_ar + c_at, M)
    ev, V = np.linalg.eigh(Kt)
    m = float(ev[0])
    v = V[:, 0].copy()
    if v[int(np.argmax(np.abs(v)))] < 0.0:
        v = -v
    m_rel = abs(m - r["m"]) / max(abs(r["m"]), 1e-300)
    # basis: v-seat + K frozen frame-cosine carrier directions
    ii = (np.arange(h) + 0.5) * D
    oms = np.array([math.pi * j / Lu for j in range(1, KMAX + 1)])
    P = np.empty((h, KMAX + 1))
    P[:, 0] = v
    for j in range(1, KMAX + 1):
        p = np.cos(oms[j - 1] * ii)
        P[:, j] = p / float(np.linalg.norm(p))
    N = P.T @ P
    N = 0.5 * (N + N.T)
    # entries: source-side reads + split + zero read
    nn = r["nn"]
    i_cut = int(np.searchsorted(nn, nc, side="right")) - 1
    tg = cxc.tail_grid(D, float(gam[-1]))
    abel = subg.abel_upper(tg, 1.0 / tg[:-1] ** 2,
                           n_start=float(N_Z))
    lw = [core.lag_weights_from_v(P[:, a], h)
          for a in range(KMAX + 1)]
    n_b = KMAX + 1
    Fp = np.zeros((n_b, n_b))
    Fz = np.zeros((n_b, n_b))
    TB = np.zeros((n_b, n_b))
    pol_dev = atom_dev = recon_dev = 0.0
    heart_ex = -1e18
    heart_slack = []
    spot_dev = 0.0
    pcs = []
    metas = []
    for a in range(n_b):
        for bb in range(a, n_b):
            Wab = 0.5 * (core.lag_weights_from_v(
                P[:, a] + P[:, bb], h) - lw[a] - lw[bb])
            e_ar = float(c_ar @ Wab)
            qa = mu * w2.q_read(Wab, uu, D, M)
            e_at = float(qa.sum())
            f_pr = e_ar + e_at
            # POL ward: reads == x^T Kt y
            f_mat = float(P[:, a] @ (Kt @ P[:, bb]))
            pol_dev = max(pol_dev, abs(f_pr - f_mat)
                          / max(1.0, abs(f_pr)))
            # ATOM-ID ward: tent-lag contraction == atom reads
            atom_dev = max(atom_dev, abs(float(c_at @ Wab) - e_at)
                           / max(1.0, abs(e_at)))
            head_at = float(qa[:i_cut + 1].sum()) if i_cut >= 0 \
                else 0.0
            t_int = e_at - head_at
            pc0 = w2.weight_pieces(Wab, u0, uL, D, M)
            tcont = w2.tcont_of(pc0)
            par = t_int - tcont
            sp = dict(nc=nc, u0=u0, uL=uL, tcont=tcont, par=par,
                      t_int=t_int)
            row_ab = dict(r)
            row_ab["Wv"] = Wab
            pc = cxc.phi_cont_of(row_ab, sp)
            recon_dev = max(recon_dev,
                            cxc.recon_of(row_ab, sp, pc))
            pcs.append(pc)
            metas.append((a, bb, e_ar, head_at, tcont, par, f_pr,
                          sp, row_ab))
    # ONE chunked pass over the ordinates for all entries
    v_all = np.unique(np.concatenate([pc["v"] for pc in pcs]))
    Jm = np.zeros((len(v_all), len(pcs)))
    for c_i, pc in enumerate(pcs):
        idx = np.searchsorted(v_all, pc["v"])
        Jm[idx, c_i] += pc["J"]
    zs = np.zeros(len(pcs))
    for i0 in range(0, len(gam), 1000):
        g = gam[i0:i0 + 1000]
        E = np.exp(1j * np.outer(g, v_all))
        zs += 4.0 * np.sum(
            (-(E @ Jm) / (g ** 2)[:, None]).real, axis=0)
    for c_i, (pc, meta) in enumerate(zip(pcs, metas)):
        a, bb, e_ar, head_at, tcont, par, f_pr, sp, row_ab = meta
        par_hat = (-zs[c_i] - pc["triv"] - pc["ramp_at"]
                   + pc["ramp_cont"] + pc["ext_cont"]
                   - pc["ext_at"])
        dps = 4.0 * pc["sd"] * (pc["vmax"] * inv2 + 2.0 * inv3) \
            * cxc.DPS_ERR
        tailb = (4.0 * pc["sd"] * abel
                 + 4.0 * math.exp(0.5 * pc["vmax"]) * pc["sd"]
                 * s2t + dps
                 + 1e-12 * (1.0 + abs(pc["triv"])))
        heart = abs(par - par_hat)
        heart_ex = max(heart_ex, heart - tailb)
        heart_slack.append(math.log10(max(tailb, 1e-300)
                                      / max(heart, 1e-300)))
        Fp[a, bb] = Fp[bb, a] = f_pr
        Fz[a, bb] = Fz[bb, a] = e_ar + head_at + tcont + par_hat
        TB[a, bb] = TB[bb, a] = tailb
        if do_spot and a == 0 and bb == 0:
            ph_v, tb_v = cxc.direct_read(row_ab, sp, pc, gam,
                                         abel, s2t, inv2, inv3)
            spot_dev = max(abs(par_hat - ph_v)
                           / max(1.0, abs(ph_v)),
                           abs(tailb - tb_v)
                           / max(tailb, 1e-300))
    pc00 = pcs[0]
    # amendment A1: the F00 cancellation scale is the CLXXXV W3
    # energy-bookkeeping scale max(1, |E_at(0,0)|)
    eat00 = metas[0][6] - metas[0][2]
    return dict(kz=r["kz"], h=h, alpha=alpha, m=m, mu1=r["mu1"],
                v=v, P=P, N=N, F=Fp, Fz=Fz, TB=TB, oms=oms,
                Lu=Lu, nc=nc, m_rel=m_rel, pol=pol_dev,
                atom=atom_dev, recon=recon_dev, heart_ex=heart_ex,
                heart_slack=heart_slack, spot=spot_dev,
                pc00=pc00, par00=metas[0][5], zs00=float(zs[0]),
                f00_scale=max(1.0, abs(eat00)),
                lam_sm=r.get("lam_sm"),
                n_inband=int(np.sum(oms <= OMEGA_C)))


def minors_of(fr):
    """Minor/Schur/pencil measurements of one frame operator, for
    every K = 1..KMAX.  Exact-identity deviations at KMAX."""
    F, N, m = fr["F"], fr["N"], fr["m"]
    out = dict(rho={}, schur={}, cpen={}, npd={})
    for K in range(1, KMAX + 1):
        sel = list(range(1, K + 1))
        C = F[np.ix_(sel, sel)]
        NC = N[np.ix_(sel, sel)]
        f0 = F[sel, 0]
        lc = lampen(C, NC)
        out["cpen"][K] = lc
        out["npd"][K] = lc is not None
        evC = np.linalg.eigvalsh(0.5 * (C + C.T))
        if float(evC[0]) > 0.0:
            q = float(f0 @ np.linalg.solve(C, f0))
            out["rho"][K] = q / m
            out["schur"][K] = F[0, 0] - q
        else:
            out["rho"][K] = None
            out["schur"][K] = None
    # exact identities at KMAX
    sel = list(range(1, KMAX + 1))
    C = F[np.ix_(sel, sel)]
    f0 = F[sel, 0]
    # amendment A1: cancellation-aware scale (CLXXXV W3 convention);
    # the raw relative deviation is kept for the reported census
    dev = dict(f00=abs(F[0, 0] - m) / fr["f00_scale"],
               f00_rel=abs(F[0, 0] - m) / max(abs(m), 1e-300))
    sch = out["schur"][KMAX]
    if sch is not None:
        Finv = np.linalg.inv(F)
        dev["piv"] = abs(sch - 1.0 / Finv[0, 0]) \
            / max(abs(sch), 1e-300)
        sF, ldF = np.linalg.slogdet(F)
        sC, ldC = np.linalg.slogdet(C)
        if sF > 0 and sC > 0 and sch > 0:
            dev["det"] = abs(ldF - (math.log(sch) + ldC))
        else:
            dev["det"] = float("nan")
    lf_pen = lampen(F, fr["N"])
    dev["compress"] = (abs(lf_pen - m) / max(abs(m), 1e-300)
                       if lf_pen is not None else float("inf"))
    out["dev"] = dev
    out["lf_pen"] = lf_pen
    return out


def finish(labels):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _n, ok in CHECKS if ok)
    if KILLS:
        verdict = {"K1": "PIPELINE-BROKEN", "K2": "WARD-BROKEN",
                   "K3": "ALGEBRA-BROKEN"}[KILLS[0]]
    else:
        verdict = " / ".join(labels.get(k, "-")
                             for k in ("v0", "v1", "v2", "v3",
                                       "v4", "v5"))
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST SCOPE: every statement is per-rung; the v-seat is a
  MEASURED direction (DIRECTION-CONDITIONAL); the deep block is
  FLOAT-LEVEL; W1 columns exist only on the joined surface; the
  equivalence through the v-seat is exact but NOT a wall reduction
  (the seat is per-rung data); only the carrier-only curve at fixed
  K could carry an all-h contract and its trend is a measurement.
  A finite verified-zero sum can never prove RH.  NO RH claim; no
  marker moves; no promotion.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, len(CHECKS), len(CHECKS) - passed))
    if any(not ok for _n, ok in CHECKS):
        print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
    return 0 if passed == len(CHECKS) else 1


def main():
    section("PRIME.WALL.ZEROFRAME.UNIFICATION.01 -- are W1 and W2 "
            "two minors of ONE small frame operator? "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    shas = dict(
        parent=hashlib.sha256(
            parent.__doc__.encode("utf-8")).hexdigest(),
        w2=hashlib.sha256(w2.__doc__.encode("utf-8")).hexdigest(),
        asm=hashlib.sha256(asm.__doc__.encode("utf-8")).hexdigest(),
        cxc=hashlib.sha256(cxc.__doc__.encode("utf-8")).hexdigest(),
        subgamma=hashlib.sha256(
            subg.__doc__.encode("utf-8")).hexdigest())
    for tag in sorted(shas):
        print("    %-8s SPEC SHA-256 = %s" % (tag, shas[tag]))
    print("    PEDIGREE (EXTERNAL-CITED): gamma_1 = %.6f; T0 = "
          "%.1e (Platt-Trudgian 2021); Rosser 1941 N(T) corridor "
          "(%.3f, %.3f, %.3f); Buethe 2018; B_PSI = %.5f; verified "
          "ordinates: local cache, builder disclosed (CLXXXIX)."
          % (subg.GAMMA1, subg.T0_RH, subg.ROSSER_A, subg.ROSSER_B,
             subg.ROSSER_C, core.B_PSI))
    if SMOKE:
        print("    *** SMOKE MODE: ladder kz <= %d, %d joined "
              "rows, %d deep, full-only wards deferred ***"
              % (KZ_TOP, N_SURF_JOIN, N_DEEP))
    check("S0 AST firewall clean", not ast_scan(), kill="K2")
    check("S0b parent SPEC reproduced", shas["parent"] == PARENT_SHA,
          kill="K2")
    ok_pref = all(shas[k][:8] == v for k, v in PREFIXES.items())
    check("S0c predecessor SPEC prefixes reproduced (%s)"
          % "/".join(PREFIXES[k] for k in sorted(PREFIXES)),
          ok_pref, kill="K2")

    # ------------------------------------------------------------ Z
    section("Z -- the verified-zero cache (CLXXXIX wards verbatim)")
    check("Z0 cache present", os.path.exists(ZC_NPY), kill="K1")
    if KILLS:
        return finish({})
    gam = np.load(ZC_NPY)
    t_c = float(gam[-1])
    check("Z1 census %d == %d, increasing, first == gamma_1 "
          "(dev %.1e)" % (len(gam), N_Z, abs(gam[0] - subg.GAMMA1)),
          len(gam) == N_Z and bool(np.all(np.diff(gam) > 0.0))
          and abs(gam[0] - subg.GAMMA1) <= 2.0e-6, kill="K2")
    kk = np.arange(1, N_Z + 1, dtype=float)
    up_r = subg.n_up(gam + CORR_EPS)
    lo_r = subg.n_lo(gam + CORR_EPS)
    up_l = subg.n_up(np.maximum(gam - CORR_EPS, 2.0))
    lo_l = subg.n_lo(np.maximum(gam - CORR_EPS, 2.0))
    n_ok = int(np.sum((kk <= up_r) & (kk >= lo_r)
                      & (kk - 1.0 <= up_l) & (kk - 1.0 >= lo_l)))
    check("Z2 Rosser-corridor consistency per index (%d/%d both "
          "sides)" % (n_ok, N_Z), n_ok == N_Z, kill="K2")
    from mpmath import mp as _mp, mpc as _mpc
    from mpmath import zeta as _zf
    _mp.dps = 20
    idx = np.unique(np.geomspace(1, N_Z, NS_ZETA).astype(int)) - 1
    worst_z = max(float(abs(_zf(_mpc(0.5, float(gam[i])))))
                  for i in idx)
    check("Z3 independent zeta spot check <= %.0e at %d ordinates "
          "(worst %.1e)" % (ZETA_TOL, len(idx), worst_z),
          worst_z <= ZETA_TOL, kill="K2")
    check("Z4 T_c = %.4f below T0" % t_c, t_c < subg.T0_RH,
          kill="K2")
    inv2 = float(np.sum(1.0 / gam ** 2))
    inv3 = float(np.sum(1.0 / gam ** 3))
    s2t = subg.s2_tail()

    # ------------------------------------------------------------ W
    section("W -- the two ladders + their reproduction wards")
    zones, truth, full, rows = parent.build_truth_rows()
    check("W1 parent census 42/41/39",
          len(zones) == 42 and len(full) == 41 and len(rows) == 39,
          "%d/%d/%d" % (len(zones), len(full), len(rows)),
          kill="K1")
    if KILLS:
        return finish({})
    minb = min(float(np.linalg.eigvalsh(w["B"])[0]) for w in rows)
    gaps = np.array([w["gap"] for w in rows])
    check("W2 v901 reproduction (minB %.4f, gap %.4f/%.4f)"
          % (minb, float(np.min(gaps)), float(np.median(gaps))),
          abs(minb / parent.MINB_REF - 1.0) <= parent.MINB_RTOL
          and abs(float(np.min(gaps)) / parent.GAPMIN_REF - 1.0)
          <= parent.GAP_RTOL
          and abs(float(np.median(gaps)) / parent.GAPMED_REF - 1.0)
          <= parent.GAP_RTOL, kill="K2")
    n_sp = sum(w["sP"] >= w["mu1"] for w in rows)
    check("W3 CLXXIV reproduction s_P >= mu1 %d/%d"
          % (n_sp, len(rows)), n_sp == len(rows), kill="K2")
    for w in rows:
        Gc = w["H"] @ w["H"].T
        w["Gc"] = 0.5 * (Gc + Gc.T)
    rungs = []
    for kz in range(2, KZ_TOP + 1):
        r = w2.build_rung(kz)
        if r is not None:
            rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    NL = len(rungs)
    check("W4 CLXXXV ladder census %d %s  [%.1f s]"
          % (NL, "== 67" if not SMOKE else ">= 8 (smoke)",
             time.time() - T0),
          (NL == 67) if not SMOKE else (NL >= 8), kill="K1")
    if KILLS:
        return finish({})
    sub = [r for r in rungs if r["kz"] in w2.SUBSET]
    pres = max(r["pivres"] for r in sub) if sub else 0.0
    check("W5 WARD m > 0 on %d/%d + pivot collapse %.1e <= %.0e "
          "=> n - q = m along v"
          % (sum(1 for r in rungs if r["m"] > 0), NL, pres,
             w2.RES_WARD),
          all(r["m"] > 0 for r in rungs) and pres <= w2.RES_WARD,
          kill="K2")
    mm_l = np.array([r["m"] for r in rungs])
    shat = mm_l / np.array([r["mu1"] for r in rungs])
    s3 = band(shat)
    if not SMOKE:
        check("W6 CXLIII band shat %.4f/%.4f/%.4f ~ %s"
              % (s3 + (w2.SHAT_REF,)),
              all(abs(s3[i] - w2.SHAT_REF[i]) <= w2.SHAT_TOL
                  for i in range(3)), kill="K2")
    else:
        print("    (smoke: shat band %.4f/%.4f/%.4f -- full ward "
              "deferred)" % s3)
        check("W6 deferred in smoke (disclosed)", True)
    check("W7 cB coverage %d/%d"
          % (sum(1 for r in rungs if r["ncB"] > 0), NL),
          all(r["ncB"] > 0 for r in rungs), kill="K2")
    by_kz = {r["kz"]: r for r in rungs}
    joined = [(w, by_kz[w["r2"]["kz"]]) for w in rows
              if w["r2"]["kz"] in by_kz]
    joined = sorted(joined, key=lambda t: t[1]["h"])[:N_SURF_JOIN]
    if not SMOKE:
        check("W8 rung-exact join surface %d/39" % len(joined),
              len(joined) == 39, kill="K1")
    else:
        check("W8 join %d rows (smoke)" % len(joined),
              len(joined) >= 4, kill="K1")

    # ------------------------------------------------------------ E
    section("E -- classical inputs on the extended table")
    lam_ext = deep.build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("E0 deep-table fidelity (overlap dev %.1e; TAB %d == %d)"
          % (dev, deep.TAB_EXT, w2.TAB_EXT),
          dev == 0.0 and deep.TAB_EXT == w2.TAB_EXT, kill="K2")
    NN_e = deep.EXT["NN"]
    psi_e = np.cumsum(lam_ext[NN_e])
    lf.ENV.update(lf.table_sups(NN_e, psi_e, deep.TAB_EXT))
    check("E1 Buethe envelope warded on the table (sup %.4f <= "
          "%.2f)" % (lf.ENV["BUETHE_SUP"], lf.BUETHE),
          lf.ENV["BUETHE_SUP"] <= lf.BUETHE, kill="K2")
    tg0 = cxc.tail_grid(rungs[0]["D"], t_c)
    abel0 = subg.abel_upper(tg0, 1.0 / tg0[:-1] ** 2,
                            n_start=float(N_Z))
    check("E2 Abel tail base %.4e in [%.0e, %.0e]"
          % ((abel0,) + ABEL_BAND),
          ABEL_BAND[0] <= abel0 <= ABEL_BAND[1], kill="K2")

    # ------------------------------------------------------------ A
    section("A -- the independent W1 chain (CLXXXIV verbatim) on "
            "the joined surface")
    s2t_w1 = s2t
    w1col = {}
    sound_worst = -1e18
    n_dom = n_loew = n_l5 = n_grid = n_vlo = n_fs = 0
    n_cert = 0
    for w, _r in joined:
        r2 = w["r2"]
        rr = base.window_of(r2["kz"])
        rb = asm.rung_band(rr["alpha"], rr["M"], rr["uu"],
                           2.0 * rr["lam"], rr["c_ar"], s2t_w1)
        pa = asm.rung_assembly(rb, r2["y_core"], r2["v_core"],
                               r2["h"], w["Gc"], w["mu1"])
        if pa is None:
            continue
        sound_worst = max(sound_worst, asm.fold_sound(rb))
        n_dom += int(pa["dom_sup"] <= asm.DOM_TOL)
        n_loew += int(pa["loewner"] >= -asm.L2_TOL)
        n_l5 += int(pa["l5_id"] <= asm.L5_TOL)
        n_grid += int(pa["grid_dev"] <= asm.GRID_TOL)
        n_vlo += int(pa["vlo_excess"] <= 0.0)
        n_fs += int(pa["floor"] <= pa["truth"]
                    * (1.0 + asm.FLOOR_TOL) + 1e-15)
        n_cert += int(pa["cert"])
        w1col[r2["kz"]] = pa
    nA = len(w1col)
    check("A1 W1 chain built on %d/%d joined rungs"
          % (nA, len(joined)), nA == len(joined), kill="K1")
    check("A2 fold soundness worst excess %.2e <= 0"
          % sound_worst, sound_worst <= 0.0, kill="K2")
    check("A3 domination / Loewner / L5 / grid / v_lo / "
          "FLOOR <= truth: %d/%d each"
          % (min(n_dom, n_loew, n_l5, n_grid, n_vlo, n_fs), nA),
          min(n_dom, n_loew, n_l5, n_grid, n_vlo, n_fs) == nA,
          kill="K3")
    if not SMOKE:
        check("A4 CLXXXIV surface cert census %d == 7" % n_cert,
              n_cert == 7, kill="K2")
    else:
        print("    (smoke: cert census %d on %d shallowest rows "
              "-- full ward deferred)" % (n_cert, nA))
        check("A4 deferred in smoke (disclosed)", True)

    # ------------------------------------------------------------ F
    section("F -- THE FRAME OPERATOR: F_h on surface + deep, "
            "zero-read warded")
    surf_r = [r for r in rungs] if not SMOKE \
        else [r for _w, r in joined]
    frames = []
    pol_w = atom_w = recon_w = spot_w = m_w = 0.0
    heart_w = -1e18
    slack_all = []
    for i, r in enumerate(surf_r):
        fr = frame_of(r, gam, s2t, inv2, inv3, do_spot=True)
        if fr is None:
            continue
        fr["deep"] = False
        frames.append(fr)
        pol_w = max(pol_w, fr["pol"])
        atom_w = max(atom_w, fr["atom"])
        recon_w = max(recon_w, fr["recon"])
        spot_w = max(spot_w, fr["spot"])
        m_w = max(m_w, fr["m_rel"])
        heart_w = max(heart_w, fr["heart_ex"])
        slack_all.extend(fr["heart_slack"])
        if (i + 1) % 10 == 0:
            print("    ... %d surface frames  [%.1f s]"
                  % (i + 1, time.time() - T0), flush=True)
    n_surf_fr = len(frames)
    # deep block (CXCIII selection verbatim)
    EXT = dict(lam=lam_ext, NN=NN_e,
               U=np.log(NN_e.astype(float)),
               MU=2.0 * lam_ext[NN_e] / np.sqrt(NN_e.astype(float)))
    EXT["G"] = np.diff(EXT["U"])
    new_kz = []
    for kz in range(2, min(w2.KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        a_ = float(EXT["U"][kz])
        Xk = math.exp(2.0 * a_)
        if Xk > w2.TAB_EXT:
            break
        if Xk <= core.ATOM_MAX:
            continue
        D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
        Mk = int(math.ceil(a_ / D_k - 1.0e-9)) + 1
        if Mk % 2:
            Mk += 1
        if not (w2.H_HOLD[0] <= Mk // 2 <= w2.H_HOLD[1]):
            continue
        new_kz.append(kz)
    deep_rows = []
    if new_kz:
        order = sorted(new_kz)
        pick = sorted(set(int(round(t)) for t in
                          np.linspace(0, len(order) - 1,
                                      min(N_DEEP, len(order)))))
        for ii in pick:
            r = w2.build_rung(order[ii], ext=EXT)
            if r is not None:
                deep_rows.append(r)
        deep_rows.sort(key=lambda r: r["h"])
    n_deep_fr = 0
    for r in deep_rows:
        fr = frame_of(r, gam, s2t, inv2, inv3, do_spot=True)
        if fr is None:
            continue
        fr["deep"] = True
        frames.append(fr)
        n_deep_fr += 1
        pol_w = max(pol_w, fr["pol"])
        atom_w = max(atom_w, fr["atom"])
        recon_w = max(recon_w, fr["recon"])
        spot_w = max(spot_w, fr["spot"])
        m_w = max(m_w, fr["m_rel"])
        heart_w = max(heart_w, fr["heart_ex"])
        slack_all.extend(fr["heart_slack"])
    NE = (KMAX + 1) * (KMAX + 2) // 2
    print("    %d surface + %d deep frames, %d zero-read entries "
          "each  [%.1f s]"
          % (n_surf_fr, n_deep_fr, NE, time.time() - T0))
    check("F0 frame census surface %d + deep %d"
          % (n_surf_fr, n_deep_fr),
          n_surf_fr >= (4 if SMOKE else 60)
          and n_deep_fr == len(deep_rows), kill="K1")
    check("F1 WARD polarization reads == x^T K y: worst %.2e <= "
          "%.0e" % (pol_w, POL_WARD), pol_w <= POL_WARD, kill="K2")
    check("F2 WARD atom identity c_at . W_ab == atom reads: worst "
          "%.2e <= %.0e" % (atom_w, ATOM_ID_WARD),
          atom_w <= ATOM_ID_WARD, kill="K2")
    check("F3 WARD CXCIII bookkeeping recon (no zeros): worst "
          "%.2e <= %.0e" % (recon_w, RECON_TOL),
          recon_w <= RECON_TOL, kill="K2")
    check("F4 WARD zero-read HEART |PARITH - hat| <= TAILB on "
          "every rung x entry (worst excess %.2e; slack med "
          "%+.2f dex)" % (heart_w,
                          float(np.median(slack_all))),
          heart_w <= 0.0, kill="K2")
    check("F5 WARD m consistency eigh vs ladder: worst %.2e <= "
          "%.0e" % (m_w, MREL_WARD), m_w <= MREL_WARD, kill="K2")
    check("F6 WARD SPOT bit-consistency vs CXCIII direct_read: "
          "worst %.2e <= %.0e" % (spot_w, SPOT_WARD),
          spot_w <= SPOT_WARD, kill="K2")
    inband = [fr["n_inband"] for fr in frames]
    print("    omega <= %.2f in-band census of the %d carriers: "
          "min/med/max %d/%d/%d"
          % (OMEGA_C, KMAX, int(np.min(inband)),
             int(np.median(inband)), int(np.max(inband))))

    # ------------------------------------------------------------ B
    section("B -- THE MINOR TEST: W2 as Schur complement, W1 as "
            "principal minor")
    dev_f00 = dev_piv = dev_det = dev_cmp = 0.0
    f00_rel_w = 0.0
    n_c8 = 0
    n_pos_fac = 0
    n_npd = 0
    minors = []
    for fr in frames:
        mo = minors_of(fr)
        minors.append(mo)
        d = mo["dev"]
        dev_f00 = max(dev_f00, d["f00"])
        f00_rel_w = max(f00_rel_w, d["f00_rel"])
        if "piv" in d:
            dev_piv = max(dev_piv, d["piv"])
            if np.isfinite(d.get("det", float("nan"))):
                dev_det = max(dev_det, d["det"])
            if max(d["f00"], d["piv"], d.get("det", 0.0)) \
                    <= ID_CENSUS:
                n_c8 += 1
        dev_cmp = max(dev_cmp, d["compress"])
        rho = mo["rho"][KMAX]
        if rho is not None and rho < 1.0:
            n_pos_fac += 1
        if mo["lf_pen"] is None:
            n_npd += 1
    NF = len(frames)
    check("B1 WARD F00 == m (W2 at the seat, CLXXXV W3 scale, "
          "A1): worst %.2e <= %.0e (raw relative worst %.2e, "
          "reported)" % (dev_f00, F00_WARD, f00_rel_w),
          dev_f00 <= F00_WARD, kill="K2")
    check("B2 WARD Schur identities (pivot %.2e, det %.2e) <= "
          "%.0e; <= 1e-8 census %d/%d (reported)"
          % (dev_piv, dev_det, ID_WARD_NUM, n_c8, NF),
          max(dev_piv, dev_det) <= ID_WARD_NUM, kill="K2")
    check("B3 WARD COMPRESS lampen(F|N) == m: worst %.2e <= %.0e "
          "(N not PD on %d rungs, counted)"
          % (dev_cmp, COMPRESS_WARD, n_npd),
          dev_cmp <= COMPRESS_WARD and n_npd == 0, kill="K2")
    rhoK = np.array([mo["rho"][KMAX] for mo in minors
                     if mo["rho"][KMAX] is not None])
    fac = 1.0 - rhoK
    check("B4 typed: W2-AS-SCHUR factor 1 - rho positive on "
          "%d/%d; factor band %.3e/%.3e/%.3e (rho med %.4f)"
          % (n_pos_fac, NF, band(fac)[0], band(fac)[1],
             band(fac)[2], float(np.median(rhoK))),
          n_pos_fac == NF, kill=None)
    # W1 comparison on the joined surface
    ratio_dex = []
    hs_j = []
    n_match = 0
    fl_rows = []
    fr_by_kz = {fr["kz"]: fr for fr in frames if not fr["deep"]}
    mo_by_kz = {fr["kz"]: mo for fr, mo in zip(frames, minors)
                if not fr["deep"]}
    print("\n    the W1 columns vs the carrier principal minor "
          "(joined surface):")
    print("    kz    h    truth/mu1   bsup/mu1  FLOOR/mu1  "
          "lamC_pen/mu1(K=%d)  ratio dex" % KMAX)
    for w, r in joined:
        kz = w["r2"]["kz"]
        if kz not in w1col or kz not in fr_by_kz:
            continue
        pa = w1col[kz]
        fr = fr_by_kz[kz]
        mo = mo_by_kz[kz]
        lc = mo["cpen"][KMAX]
        if lc is None:
            continue
        w1_truth = pa["truth"] / pa["mu1"]
        w1_bsup = pa["b_sup"] / pa["mu1"]
        w1_floor = (pa["floor"] / pa["mu1"]) if pa["cert"] \
            else float("nan")
        cmin = lc / fr["mu1"]
        rdx = math.log10(max(cmin, 1e-300)) \
            - math.log10(max(w1_truth, 1e-300))
        ratio_dex.append(rdx)
        hs_j.append(math.log10(fr["h"]))
        if abs(rdx) <= W1_TOL_DEX:
            n_match += 1
        fl_rows.append((kz, fr["h"], w1_truth, w1_bsup, w1_floor,
                        cmin, rdx))
        print("    %-4d %4d  %9.3e  %9.3e  %9s  %13.4f  %+8.3f"
              % (kz, fr["h"], w1_truth, w1_bsup,
                 ("%9.3e" % w1_floor) if np.isfinite(w1_floor)
                 else "   (open)", cmin, rdx), flush=True)
    nJ = len(ratio_dex)
    b_w1, se_w1, r2_w1 = w2.jack_slope(hs_j, ratio_dex)
    med_dex = float(np.median(ratio_dex)) if ratio_dex else \
        float("nan")
    if nJ and n_match / nJ >= MATCH_FRAC:
        v2lab = "W1-MINOR-MATCHED(%d/%d)" % (n_match, nJ)
    elif np.isfinite(b_w1) and abs(b_w1) <= w2.SLOPE_PASS:
        v2lab = ("W1-MINOR-CALIBRATED(offset %+.2f dex, slope "
                 "%+.3f)" % (med_dex, b_w1))
    else:
        v2lab = ("W1-MINOR-DIVERGES(med %+.2f dex, slope %+.3f "
                 "/log h, 2SE %.3f, R^2 %.3f)"
                 % (med_dex, b_w1, 2 * se_w1, r2_w1))
    check("B5 typed: %s (matched %d/%d at %.1f dex)"
          % (v2lab, n_match, nJ, W1_TOL_DEX), True)

    # ------------------------------------------------------------ G
    section("G -- EQUIVALENCE + CONTROLS (the world must break "
            "the frame)")
    check("G0 WARD smooth world lam_sm < 0 on %d/%d rungs"
          % (sum(1 for r in rungs if r["lam_sm"] < 0.0), NL),
          all(r["lam_sm"] < 0.0 for r in rungs), kill="K2")
    ctrl_fire = {}
    ctrl_heart = {}
    r9 = by_kz.get(CTRL_KZ)
    if r9 is None:
        r9 = w2.build_rung(CTRL_KZ)
    NE9 = int(math.floor(math.exp(2.0 * r9["alpha"]))) + 1 \
        if r9 is not None else 0
    ctrls = {}
    if r9 is not None:
        lamE = w2.lambda_eps(NE9)
        nnE = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ctrls["Epstein"] = w2.build_rung(
            CTRL_KZ, comb=(np.log(nnE.astype(float)),
                           2.0 * lamE[nnE]
                           / np.sqrt(nnE.astype(float))))
        ctrls["scramble"] = w2.build_rung(CTRL_KZ, scramble_seed=1)
    # amendment A2: the control worlds have no covering cut (their
    # certificate machinery already fails there -- printed); the
    # zero-read heart is exercised at the DECLARED control cut =
    # the truth kz-9 covering cut, fallback NB_MED = 17.
    nc_ctrl = int(r9["ncB"]) if (r9 is not None
                                 and r9["ncB"] > 0) else w2.NB_MED
    for name, rc in ctrls.items():
        if rc is None:
            ctrl_fire[name] = True
            ctrl_heart[name] = -1
            print("    %-9s: chain dead -> fires" % name)
            continue
        ctrl_fire[name] = rc["m"] < 0.0
        if rc["ncB"] <= 0:
            print("    %-9s: no covering cut of its own "
                  "(certificate machinery fails there, part of "
                  "the firing); heart read at control cut %d (A2)"
                  % (name, nc_ctrl))
        frc = frame_of(rc, gam, s2t, inv2, inv3,
                       nc_override=nc_ctrl)
        if frc is None:
            ctrl_heart[name] = 0
            print("    %-9s: m %+.3e (%s); control cut invalid -> "
                  "heart NOT read" % (name, rc["m"],
                                      "fires" if ctrl_fire[name]
                                      else "SILENT"))
            continue
        iu = np.triu_indices(KMAX + 1)
        n_break = int(np.sum((np.abs(frc["F"] - frc["Fz"])
                              > frc["TB"])[iu]))
        worst = float(np.max((np.abs(frc["F"] - frc["Fz"])
                              / np.maximum(frc["TB"],
                                           1e-300))[iu]))
        ctrl_heart[name] = n_break
        moc = minors_of(frc)
        lcp = moc["cpen"][KMAX]
        print("    %-9s: m %+.3e (%s); zero-read heart breaks "
              "%d/%d entries (worst %.1e x TAILB); carrier-only "
              "lampen(C)/|m| %+.2f"
              % (name, rc["m"], "fires" if ctrl_fire[name]
                 else "SILENT", n_break, NE, worst,
                 (lcp / abs(rc["m"])) if lcp is not None
                 else float("nan")), flush=True)
    check("G1 WARD Epstein + scramble fire at kz %d (wall level)"
          % CTRL_KZ, all(ctrl_fire.get(k, False)
                         for k in ("Epstein", "scramble")),
          kill="K2")
    check("G2 WARD scramble breaks the zero-read heart on >= %d "
          "entries (%d/%d)" % (SCR_MIN,
                               max(ctrl_heart.get("scramble", 0),
                                   0), NE),
          ctrl_heart.get("scramble", 0) >= SCR_MIN
          or ctrl_heart.get("scramble") == -1, kill="K2")
    check("G3 typed: Epstein heart census %d/%d entries"
          % (max(ctrl_heart.get("Epstein", 0), 0), NE), True)
    # impostor on the truth kz-9 frame, (0,0) entry (CXCIII M4)
    fr9 = frame_of(r9, gam, s2t, inv2, inv3) if r9 is not None \
        else None
    if fr9 is not None:
        pc9 = fr9["pc00"]
        g1 = float(gam[0])
        on_pair = 4.0 * float((-(np.exp(1j * g1 * pc9["v"])
                                 @ pc9["J"]) / g1 ** 2).real)
        dlt = IMP_BETA - 0.5
        quad = 2.0 * (cxc.hat_seg_c(pc9["edges"], pc9["fvals"],
                                    pc9["slopes"],
                                    dlt + 1j * g1).real
                      + cxc.hat_seg_c(pc9["edges"], pc9["fvals"],
                                      pc9["slopes"],
                                      -dlt + 1j * g1).real)
        shift = abs(on_pair - quad)
        res9 = abs(fr9["F"][0, 0] - fr9["Fz"][0, 0])
        ratio = shift / max(res9, 1e-300)
        check("G4 CONTROL off-line impostor (gamma_1 -> beta = "
              "%.2f) shifts the (0,0) zero read by %.3e = %.1e x "
              "the genuine residual (>= %.0f)"
              % (IMP_BETA, shift, ratio, IMP_RATIO_MIN),
              ratio >= IMP_RATIO_MIN, kill="K2")
    else:
        check("G4 impostor seat unavailable (kz %d)" % CTRL_KZ,
              False, kill="K2")
    print("    EQUIVALENCE reading: lampen(F|N) == m is warded "
          "(B3), so M_h > 0 <=> F_h > 0 holds EXACTLY through the "
          "v-seat on every rung and every control -- both "
          "directions; the seat is per-rung data, so this is a "
          "representation, not a reduction.")

    # ------------------------------------------------------------ H
    section("H -- DIMENSION LAW + FRAME-BOUND CURVES + SCREENS")
    ks_rho, ks_cap = [], []
    hs_all, al_all = [], []
    c2_all, cK_all, m_all = [], [], []
    cens_rho = cens_cap = 0
    for fr, mo in zip(frames, minors):
        kr = next((K for K in range(1, KMAX + 1)
                   if mo["rho"][K] is not None
                   and mo["rho"][K] >= RHO_BAR), KMAX + 1)
        kc = next((K for K in range(1, KMAX + 1)
                   if mo["cpen"][K] is not None
                   and mo["cpen"][K] / fr["m"] <= CAP_BAR),
                  KMAX + 1)
        cens_rho += int(kr == KMAX + 1)
        cens_cap += int(kc == KMAX + 1)
        ks_rho.append(kr)
        ks_cap.append(kc)
        hs_all.append(math.log10(fr["h"]))
        al_all.append(fr["alpha"])
        c2 = mo["cpen"][K_SMALL]
        cK = mo["cpen"][KMAX]
        c2_all.append(c2 / fr["mu1"] if c2 is not None
                      else float("nan"))
        cK_all.append(cK / fr["mu1"] if cK is not None
                      else float("nan"))
        m_all.append(fr["m"])
    b_r, se_r, r2_r = w2.jack_slope(hs_all, ks_rho)
    b_c, se_c, r2_c = w2.jack_slope(hs_all, ks_cap)
    kr3 = band(ks_rho)
    kc3 = band(ks_cap)
    fixed_rho = abs(b_r) <= 2.0 * se_r if np.isfinite(b_r) \
        else False
    fixed_cap = abs(b_c) <= 2.0 * se_c if np.isfinite(b_c) \
        else False
    v4lab = ("DIM-FIXED(K*_rho med %d, K*_cap med %d)"
             % (int(kr3[1]), int(kc3[1]))) \
        if (fixed_rho and fixed_cap
            and cens_rho + cens_cap == 0) else \
        ("DIM-CENSORED(rho %d, cap %d at KMAX)"
         % (cens_rho, cens_cap)) \
        if cens_rho + cens_cap > 0 else \
        ("DIM-GROWS(rho slope %+.2f 2SE %.2f, cap slope %+.2f "
         "2SE %.2f /log h)" % (b_r, 2 * se_r, b_c, 2 * se_c))
    check("H1 typed: %s (K*_rho %d/%d/%d, K*_cap %d/%d/%d; "
          "rho-slope %+.3f R^2 %.2f, cap-slope %+.3f R^2 %.2f)"
          % (v4lab, int(kr3[0]), int(kr3[1]), int(kr3[2]),
             int(kc3[0]), int(kc3[1]), int(kc3[2]),
             b_r, r2_r, b_c, r2_c), True)
    c2a = np.array(c2_all)
    cKa = np.array(cK_all)
    lg_c2 = np.log10(np.maximum(c2a, 1e-300))
    lg_cK = np.log10(np.maximum(cKa, 1e-300))
    b2, se2, r22 = w2.jack_slope(al_all, lg_c2)
    bK, seK, r2K = w2.jack_slope(al_all, lg_cK)
    print("\n    THE FRAME CURVES (c = lampen/mu1):")
    print("    c_h == shat (warded B3): band %.4f/%.4f/%.4f "
          "(nothing new -- the v-seat pins it)" % band(shat))
    print("    c_carr(K=%d): band %.3f/%.3f/%.3f | trend "
          "%+.4f dex/alpha (2SE %.4f, R^2 %.3f)"
          % ((K_SMALL,) + band(c2a[np.isfinite(c2a)])
             + (b2, 2 * se2, r22)))
    print("    c_carr(K=%d): band %.3f/%.3f/%.3f | trend "
          "%+.4f dex/alpha (2SE %.4f, R^2 %.3f)"
          % ((KMAX,) + band(cKa[np.isfinite(cKa)])
             + (bK, 2 * seK, r2K)))
    thr = np.argsort(shat)[:3]
    print("    near-threshold rungs (smallest shat): %s"
          % ", ".join("kz %d shat %.3f" % (rungs[i]["kz"],
                                           shat[i]) for i in thr))
    if abs(bK) <= TREND_FLAT:
        v5curve = "FRAME-FLAT(%+.4f dex/alpha)" % bK
    elif bK > 0:
        v5curve = "FRAME-RISES(%+.4f dex/alpha)" % bK
    else:
        v5curve = "FRAME-FALLS(%+.4f dex/alpha)" % bK
    check("H2 typed: %s at K = %d (the deliverable curve)"
          % (v5curve, KMAX), True)
    # sign resolution census
    n_res = 0
    zn_list = []
    for fr in frames:
        lminN = float(np.linalg.eigvalsh(fr["N"])[0])
        if lminN <= 0.0:
            continue
        dF = float(np.linalg.norm(fr["TB"], 2))
        lfp = lampen(fr["F"], fr["N"])
        if lfp is not None and dF / lminN < lfp:
            n_res += 1
        else:
            _t_at, n_at = cxc.zeros_needed(fr["m"],
                                           fr["pc00"]["sd"])
            zn_list.append(n_at)
    check("H3 typed: SIGN-RESOLVED %d/%d at N_Z = %d "
          "(perturbation bound ||TAILB||_2/lammin(N) < "
          "lampen(F)); zeros-needed med %.1e on unresolved "
          "(main-term N(T), declared)"
          % (n_res, NF, N_Z,
             float(np.median(zn_list)) if zn_list
             else float("nan")), True)
    lg_m = np.log10(np.maximum(np.array(m_all), 1e-300))
    scr = []
    s1, _l1 = w2.screen_label("1-rho(KMAX)",
                              lg_m, np.log10(np.maximum(
                                  1.0 - np.array(
                                      [mo["rho"][KMAX]
                                       if mo["rho"][KMAX]
                                       is not None else np.nan
                                       for mo in minors]),
                                  1e-300)))
    scr.append(s1)
    s2_, _l2 = w2.screen_label("c_carr(2)", lg_m, lg_c2)
    scr.append(s2_)
    s3_, _l3 = w2.screen_label("c_carr(KMAX)", lg_m, lg_cK)
    scr.append(s3_)
    if ratio_dex:
        mj = [math.log10(max(fr_by_kz[kz]["m"], 1e-300))
              for kz, *_rest in fl_rows]
        s4_, _l4 = w2.screen_label("W1-ratio", mj, ratio_dex)
        scr.append(s4_)
    for s in scr:
        print("    screen %s" % s)
    check("H4 tau-screens recorded (%d)" % len(scr), True)

    # ------------------------------------------------------- verdict
    v1lab = ("W2-AS-SCHUR-EXACT-WITH-FACTOR(factor %0.3e..%0.3e, "
             "1e-8 census %d/%d)"
             % (band(fac)[0], band(fac)[2], n_c8, NF)) \
        if (n_pos_fac == NF and not KILLS) else "W2-SCHUR-BROKEN"
    v3lab = ("EQUIV-SEAT-CARRIED(%d/%d; controls wall 2/2, "
             "scramble heart %d, Epstein heart %d)"
             % (NF, NF, max(ctrl_heart.get("scramble", 0), 0),
                max(ctrl_heart.get("Epstein", 0), 0)))
    v5lab = ("%s + ZEROREAD(%d entries, slack med %+.2f dex, "
             "SIGN-RESOLVED %d/%d)"
             % (v5curve, NF * NE,
                float(np.median(slack_all)), n_res, NF))
    if not KILLS and v1lab.startswith("W2-AS-SCHUR") \
            and v2lab.startswith("W1-MINOR-MATCHED") \
            and v4lab.startswith("DIM-FIXED"):
        v0lab = "ZEROFRAME-UNIFIED"
    elif not KILLS and v1lab.startswith("W2-AS-SCHUR"):
        v0lab = "ZEROFRAME-HALF(W2)"
    else:
        v0lab = "ZEROFRAME-REFUTED"
    print("\n    reduced-contract statement:")
    if v4lab.startswith("DIM-FIXED") and not v5curve.startswith(
            "FRAME-FALLS"):
        print("      PRIME.WALL.ZEROFRAME.UNIFORM.01 (candidate "
              "contract): there exist K = %d and c0 > 0 such that "
              "for every deployed rung h, the carrier-only frame "
              "operator C_K(h) (frame cosines omega_j = pi j/Lu_h "
              "at the covering cut) satisfies lampen(C_K | N_C) "
              ">= c0 mu1(h); measured c0 candidate = %.3f (the "
              "min of the c_carr(K=%d) curve).  The v-seat then "
              "pins lam_min(F_h) = m_h exactly and W2 follows "
              "with the measured positive factor."
              % (KMAX, float(np.nanmin(cKa)), KMAX))
    else:
        print("      the unification at FIXED dimension is NOT "
              "supported by the measured laws (%s, %s): the "
              "carrier space that prices the wall floor grows or "
              "its bound falls -- the honest reading is that "
              "ZEROFRAME at fixed K is another representation of "
              "the all-h wall (RH-hard), with the measured law "
              "printed above." % (v4lab, v5curve))
    return finish(dict(v0=v0lab, v1=v1lab, v2=v2lab, v3=v3lab,
                       v4=v4lab, v5=v5lab))


if __name__ == "__main__":
    raise SystemExit(main())
