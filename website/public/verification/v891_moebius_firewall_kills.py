#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v891 -- PRIME.PORT.MOEBIUS.CRFIREWALL.01 + PRIME.PORT.MOEBIUS.GAUGEFW.01 + PRIME.PORT.MOEBIUS.CENSUS.01: THE HONEST KILL BATTERY OF THE MOEBIUS/CARRIER-INVARIANCE ROUTE, ONE module from three probes (10/10 + 13/13 + 7/7 checks, zero fails, verdicts CRFIREWALL-MEASURED (CR-DEAD / ANCHOR-FRAGILE / COCYCLE-BROKEN / SMOOTH-CR-DEAD) + GAUGEFW-MEASURED (GAUGE-MADE (W:DEGENERATE, A:DEGENERATE, D:MOVING) / LAMBDA-FLAT / JACOBI-DEAD) + MOEBIUSCENSUS-MEASURED (all five discriminators UNDECIDED); discovery probes mobius_crossratio_firewall_probe.py (SPEC v2), iiks_gauge_firewall_probe.py (SPEC v3), mobius_control_census_probe.py (SPEC v2), round 48, 2026-08-09, re-run identically at promotion, embedded BYTE-EXACT and executed verbatim, ~1.5 min).  THE VERDICTS ARE KILLS AND ARE RECORDED AS SUCH -- this module preserves the negative results that close the route.  (1) THE FIT-FREE CROSS-RATIO FIREWALL (reviewer probes 1 + 6): with NO per-rung normalization anywhere -- cross-ratios are Moebius-invariant, so a true Moebius step needs no gauge -- the full-coverage quadruple battery types CR-DEAD, the exact three-anchor step maps are ANCHOR-FRAGILE (the map depends on the anchor choice), and the composition test is COCYCLE-BROKEN (41 independent local fits, not a cocycle); the predecessor's celebrated 0.0015 normalized residual was MANUFACTURED by the three-point PSL(2,R) pinning (the F4 settling line types RAW-NEITHER, the reviewer's worry CONFIRMED: in the raw coordinate the identity is as good as the fit but BOTH are poor -- raw-id median 0.139 vs fit median 0.092, neither captures the step).  THE SURVIVING ARITHMETIC REMNANT (report-only, localized by the probe itself): the DEEP-CORE sub-battery on the 8 deepest common nodes keeps cr-coherence at 4.3e-4 on truth vs 2.7e-2 on the smooth-mass world -- whatever Moebius structure is real lives in the deep core and is arithmetic, the named residue for any future route.  (2) THE GAUGE FIREWALL (reviewer probes 2 + 3): three SOURCE-FROZEN gauges satisfying the reviewer's five validity conditions (Wronskian interpolation frame at frozen reference indices, window-edge asymptotic frame, determinant-phase frame) -- NONE is raw-invariant: the Wronskian and asymptotic frames expose a COLLAPSED near-constant carrier (RAW-DEGENERATE, caught by the v3 degeneracy guard: invariance of a collapsed carrier is vacuous) and the determinant-phase frame shows REAL rung-to-rung motion (RAW-MOVING) -- GAUGE-MADE: the baseline per-rung-normalized invariance (median id-res 0.0011) holds while no frozen gauge is raw-invariant and the cross-gauge conjugations disagree; the discarded scalar cocycle lambda_h does NOT track the wall (LAMBDA-FLAT: corr(cumsum log lambda, log tau) = 0.13 vs the 0.90/0.60 bars), and the Jacobi-transfer projectivization candidate is JACOBI-DEAD (median d_P 0.997 even under the v3 robust joint-Sylvester global conjugation) -- the Moebius step is neither gauge-real nor source-derived.  (3) THE SIX-WORLD CONTROL CENSUS (reviewer probe 4, no post-hoc selection): the identical pipeline on truth / Epstein / scramble / lattice-smooth / edge-smoothed / interior-smoothed types ALL FIVE discriminators (cross-ratio, step map, J-contractivity, raw identity, tau sign census) UNDECIDED -- four via no-frame-alive-controls and the raw identity via truth-fails -- because the arithmetic separates AT THE FRAME: every control world INCLUDING the smooth-mass worlds loses window subcriticality (win-ALIVE 0/28, 0/33, 0/42, 0/42, 0/42 vs truth 41/41), so no frame-alive control exists to discriminate against, and on the bare cross-ratio and step-map bars the frame-dead SCRAMBLE world even scores BETTER than truth (0.0060/0.0011 vs 0.0218/0.0446) -- the Moebius/cross-ratio structure is rank-2 window KINEMATICS, not arithmetic dynamics.  NET (the route decision recorded): the carrier-invariance/Moebius-cocycle route to positivity inheritance is CLOSED by its own preregistered firewall battery; the arithmetic lives in the FRAME (window subcriticality) and in the multi-factor determinant anatomy (v890), with the deep-core cross-ratio coherence as the sole named remnant.  NO RH claim; no marker moves; honest negatives are findings -- nothing here is upgraded, nothing softened.  Float64 on the deployed v563 machinery (READ-ONLY); no zeros, no prime oracles (AST firewalls inside the probes); RNG only in the declared scramble world (seed 1).  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes mobius_crossratio_firewall_probe.py
(10/10, CRFIREWALL-MEASURED, SPEC v2: chordal conditioning,
deterministic even-coverage battery replacing the depth-biased
first draft -- strictly harder, fail-first preserved; absolute
smallness bar added to the F4 positive settlement; deep-core
sub-battery kept report-only), iiks_gauge_firewall_probe.py
(13/13, GAUGEFW-MEASURED, SPEC v2 pre-run: shear-killing Wronskian
frame, frozen z_ref, anchor-step exclusions; SPEC v3 post-run with
every first-run outcome quoted: degeneracy guard on collapsed
carriers, robust joint-Sylvester global conjugation, the
smooth-mass world typed SMOOTH-FRAME-DEAD -- lam(E) >= 1 on all 42
smooth rungs under this probe's Gram frame), mobius_control_
census_probe.py (7/7, MOEBIUSCENSUS-MEASURED, SPEC v2: sieve-
accelerated Epstein recursion warded against the O(N^2) recursion,
frozen quadruple battery, 1e-6 carrier bar for all worlds with the
1e-10 truth ward kept, frame-alive rule quantified; post-run-1
reporting-only additions disclosed), all 2026-08-09, re-run
identically at promotion.  ROUND-31 EMBEDDING CONVENTION: frozen
sources embedded BYTE-EXACT, executed verbatim in isolated
namespaces; printed spec SHAs reproduce; byte-equality ward vs
experiments/tfpt-discovery/ inside the pattern gates.  All probes
consume the READ-ONLY deployed core v563_paper2_readouts.py.

FIREWALL: no zeros, no prime-table oracles; all fail-first spec
amendments preserved; kill verdicts recorded verbatim, never
softened; the deep-core remnant stays report-only.  NO RH claim.
"""

import contextlib
import io
import os
import re
import sys
import time
import types

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

# ------------- frozen probe source mobius_crossratio_firewall_probe (embedded BYTE-EXACT, raw string)
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mobius_crossratio_firewall_probe -- PRIME.PORT.MOEBIUS.
CRFIREWALL.01 (EXPLORATION ONLY, experiments/; round 48, reviewer
probes 1 + 6: is the Moebius structure of the port carrier ladder
REAL -- cross-ratio invariance, three-anchor holdout
determination, cocycle composition -- or a least-squares
artifact?, 2026-08-09).

THE QUESTION (frozen): port_schur_cocycle_probe fitted one
Moebius map per rung to the PSL(2,R)-NORMALIZED carrier (median
residual 0.0015); moebius_source_step_probe then typed the
normalized carrier CARRIER-INVARIANT.  The reviewer's worry: the
per-rung three-point normalization pins 3 of ~11 nodes and can
MANUFACTURE identity; the TLS fit can absorb noise.  This probe
uses NO per-rung normalization anywhere.  THE PRINCIPLE:
cross-ratios are Moebius-invariant, so if the step is truly
Moebius NO gauge is needed at all -- cr equality across rungs,
exact three-anchor determination with holdout prediction, and
cocycle composition are all decidable FIT-FREE in the raw
carrier coordinate.

THE RAW COORDINATE (honesty note, frozen): the carrier pairs
(g_j, f_j) carry ONLY the frozen SPEC v2 extraction gauge (the
SO(2) rotation pinning the deepest port node, lax2 verbatim --
machinery, not a per-step fit; the SVD basis of the degenerate
singular pair is otherwise arbitrary, so the gauge is what makes
the frame deterministic).  The gauge acts as a chordal ISOMETRY
of RP^1 and a Moebius map, hence F1 (cross-ratios), F2 (holdout
errors) and F3 (projective distances) are EXACTLY gauge-free;
only the F4 raw-identity readout is stated 'in the frozen
extraction gauge' and is flagged as such.

THE LADDER (frozen, port_schur_cocycle verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
rung pairs at ladder separation k with >= 8 common port alias
indices (typed skips counted); k in {1, 2, 4, 5, 8} (k = 1 is
the truth battery; k = 5 is the reviewer's mismatched-pair null;
the k-law distinguishes 'one global function' (flat in k) from
'smooth flow' (growing in k) fit-free).

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first
run; all bars frozen before the run):

 F1  CROSS-RATIO INVARIANCE: per rung pair, the frozen battery
     of well-conditioned quadruples of common nodes: if the pair
     carries more than 16 common nodes, subsample 16 node
     indices evenly across the sorted common list
     (round(linspace), deterministic -- full-range coverage, no
     depth bias); enumerate ALL quadruples of the selected
     nodes; CONDITIONING (frozen, applied on BOTH rungs): reject
     if the min pairwise chordal separation within the quadruple
     < 1e-3 x the within-quadruple chordal spread, or if |cr|
     lies outside [1e-3, 1e3] on either rung; keep the 200
     BEST-CONDITIONED survivors (ranked by min pairwise chordal
     separation, min over both rungs; deterministic tie-break by
     lexicographic index order).  cr is the homogeneous
     cross-ratio cr(p_i, p_j; p_k, p_l) = (d_ik d_jl)/(d_il
     d_jk) with signed 2x2 determinants d_ab = det[p_a p_b].
     Invariance defect per quadruple: Dcr = |cr_{h'} - cr_h| /
     (1 + |cr_h|).  Report per-step (median, q90, max) and the
     POOLED ladder distribution at k = 1.  TYPED: CR-INVARIANT
     iff pooled median <= 1e-3 AND pooled q90 <= 1e-2
     (certificate level); CR-APPROX iff pooled median <= 0.02;
     CR-DEAD otherwise.  DEEP-CORE SUB-BATTERY (report-only,
     never typed): the same battery restricted to the 8 DEEPEST
     common nodes (smallest alias indices) -- prints WHERE any
     cr-coherence lives if the full-coverage battery dies.  THE k-LAW (reviewer null (b),
     concretized fit-free): the same battery at k = 2, 4, 5, 8;
     pooled median per k; printed ratio med(k=8)/med(k=1) with
     the frozen reading: <= 2 -> ladder-global (one function);
     > 2 -> grows with separation (smooth flow); k = 5 is the
     mismatch null quoted against k = 1.

 F2  THREE-ANCHOR HOLDOUT: per k = 1 step, anchor triples =
     combinations of common nodes, conditioned like F1 (min
     pairwise chordal >= 1e-3 x within-triple spread on both
     rungs, non-degenerate three-point normalizers); the PRIMARY
     triple is the one maximizing the min pairwise chordal
     separation (min over both rungs; deterministic tie-break by
     lexicographic index order).  The step map is determined
     EXACTLY (closed form, no fit): M = N_b^{-1} N_a where N_a,
     N_b send the anchor values to (0, 1, inf).  Holdout error =
     chordal(M p_a, p_b) on all NON-anchor common nodes; per-step
     median, ladder median over steps.  ANCHOR STABILITY: over
     the top-60 conditioned triples (by score, deterministic),
     the pairwise projective distance of the exact maps d_P(A, B)
     = min_lambda ||A - lambda B||_F / ||A||_F = |sin angle(A,
     B)|; per-step median, ladder median.  TYPED: ANCHOR-STABLE
     iff ladder median holdout <= 3e-3 AND ladder median d_P <=
     1e-2; ANCHOR-FRAGILE otherwise (the reviewer kill: the map
     depends on the anchor choice).

 F3  COCYCLE COMPOSITION (reviewer probe 6): the exact primary
     three-anchor maps must compose in the raw coordinate:
     d_P(M_{h->h+2}, M_{h+1->h+2} M_{h->h+1}) on all consecutive
     triples, and the k-step transfers d_P(M_{h->h+4}, product
     of the four unit steps); all direct maps use the SAME
     frozen primary-anchor rule on their own pair.  TYPED:
     COCYCLE-EXACT iff the pooled median d_P (k = 2 and k = 4
     comparisons together) <= 1e-2; COCYCLE-BROKEN otherwise
     (41 independent local fits, not a cocycle).

 F4  SIGNIFICANCE ANATOMY (reviewer section 4; report, no
     score): per k = 1 step print the chordal spread of the
     common-node carrier values (region size), the median
     pairwise chordal (are the points on a tiny arc?), the
     numerical precision floor of the carrier (the SVD rank-2
     defect s3/s1 of the commutator extraction, worse rung of
     the pair), the RAW identity residual median
     chordal(p_h, p_{h'}) (frozen extraction gauge, NO
     normalization), and the TLS fitted-map residual (fit on all
     common nodes, residual median over all -- reference only).
     THE SETTLING LINE (frozen reading, three-way): RAW-
     INVARIANT iff the ladder median raw identity <= 3 x the
     ladder median fit residual AND <= 0.02 absolute -- then the
     un-normalized carrier is ALREADY rung-invariant, stronger
     and gauge-free, settling the tautology worry in the
     POSITIVE direction; RAW-NEITHER iff raw identity <= 3 x fit
     residual but BOTH are poor (> 0.02 absolute) -- then in the
     raw coordinate neither identity nor any single Moebius map
     captures the step, and the predecessor's tiny normalized
     residual was manufactured by the three-point pinning (the
     reviewer's worry CONFIRMED); RAW-MOVES otherwise (the
     fitted step carries real content beyond identity).

 C   CONTROLS: (C1, kz 9, must fire) Epstein (lambda_eps
     recursion comb) + scramble (seed 1): frame death (window
     unavailable or I - E_out indefinite or lam(C_J) > 1),
     channel reported; silent -> CONTROL-DEAD.  (C2, the frame-
     SURVIVING control, decisive): the SMOOTH-MASS world --
     masses 2 e^{u/2} du on the TRUE prime-power lattice
     (lattice_parametrix B1 verbatim; the frame is geometry-
     driven, so its window/port machinery is expected to exist:
     VERIFIED and reported per rung).  Build the full smooth
     ladder, run F1 (k = 1 battery) and F2 (primary holdout) on
     it.  TYPED REPORT: SMOOTH-FRAME-DEAD (< 10 measured smooth
     steps -- no answer); SMOOTH-CARRIES-CR iff the smooth
     pooled k = 1 cr-defect median <= 0.02 (then the cr-
     invariance is GEOMETRIC -- the lattice + smooth masses
     already carry it); SMOOTH-CR-DEAD otherwise (then it is
     ARITHMETIC -- the actual Lambda masses are load-bearing).
     If the TRUTH full-coverage battery is itself CR-DEAD, the
     geometric-vs-arithmetic question devolves to the DEEP CORE:
     the truth vs smooth deep-core medians are printed side by
     side with the same 0.02 reading (report-only).  The smooth
     world is a physics answer, not a kill channel.

 W   PIPELINE WARDS: W1 >= 30 rungs built; W2 [Y, D_P] rank 2 on
     every truth rung (s3/s1 <= 1e-10); W3 >= 30 k = 1 steps
     with a non-empty quadruple battery.

KILLS: K1 pipeline ward breaks -> PIPELINE-BROKEN; K3 the C1
controls are silent -> CONTROL-DEAD.

VERDICT (frozen enum): CRFIREWALL-MEASURED with typed sublabels
CR-INVARIANT / CR-APPROX / CR-DEAD (F1), ANCHOR-STABLE /
ANCHOR-FRAGILE (F2), COCYCLE-EXACT / COCYCLE-BROKEN (F3), and
the C2 report label SMOOTH-CARRIES-CR / SMOOTH-CR-DEAD /
SMOOTH-FRAME-DEAD; else PIPELINE-BROKEN / CONTROL-DEAD.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) the conditioning rule is concretized in the
CHORDAL metric (min pairwise chordal < 1e-3 x within-tuple
spread rejected, applied on both rungs) -- the affine
|r_a - r_b| rule is chart-dependent and breaks at f ~ 0 nodes,
which are regular points of RP^1; (ii) the battery is frozen
deterministically: even-coverage node subsample (16 of n if
n > 16), full quadruple enumeration on the subsample, top 200
survivors by conditioning score -- REPLACES the first-draft
lexicographic accept order, which on deep rungs (up to 53
common nodes) tested almost only the deepest nodes and
FLATTERED the invariance; the coverage rule makes F1 strictly
harder (fail-first preserved); anchor triples capped at the top
60 by conditioning score; (iii) the reviewer's affine-only null
(b) is realized as the frozen k-separation law (the prompt's
own simplification), with k = 5 as the explicit mismatched-pair
null; (iv) the raw coordinate carries the frozen one-point
SO(2) extraction gauge (machinery verbatim, a chordal isometry
-- F1/F2/F3 are exactly gauge-free, F4's raw identity is
flagged); (v) the smooth-mass control reuses build_rung with
the B1 masses via a bookkeeping flag (physics verbatim from
lattice_parametrix_probe); (vi) the F4 positive settlement
carries an ABSOLUTE smallness bar (0.02) on top of the factor-3
comparison -- the first draft's relative-only rule would have
typed 'raw-invariant' when identity and fit are equally POOR,
which is the opposite of a positive settlement (bar added
before scoring; strictly harder, fail-first preserved); (vii)
the DEEP-CORE sub-battery (8 deepest common nodes) is printed
REPORT-ONLY on truth and smooth ladders -- it is exactly the
sub-region the first-draft bias accidentally tested, kept as
anatomy so the probe itself localizes any surviving coherence;
typing stays on the full-coverage battery.

NO RH claim -- cross-ratio invariance of a compressed-truncation
carrier is a numerical measurement, not a theorem about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; carrier extraction
verbatim from port_schur_cocycle_probe.py (PRIME.PORT.
SCHURSTEP.01, itself SPEC v2 of port_riemann_hilbert_setup);
normalization warning from moebius_source_step_probe.py
(PRIME.PORT.MOEBIUS.SOURCE.01); smooth-mass B1 world from
lattice_parametrix_probe.py (PRIME.PORT.LATTICE.PARAMETRIX.01).
IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mobius_crossratio_firewall_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
MIN_RUNGS = 30
MIN_STEPS = 30
MIN_COMMON_J = 8
RANK_BAR = 1e-10
CTRL_KZ = 9

K_SEPS = (1, 2, 4, 5, 8)          # k=1 truth; k=5 mismatch null
COND_SEP_FRAC = 1e-3              # within-tuple conditioning
CR_ABS_LO, CR_ABS_HI = 1e-3, 1e3  # |cr| window (both rungs)
QUAD_NODE_CAP = 16                # even-coverage node subsample
QUAD_ACCEPT_CAP = 200             # best-conditioned survivors
DEEP_CORE_N = 8                   # deep-core sub-battery (report)
MAX_TRIPLES = 60
CR_INV_MED = 1e-3
CR_INV_Q90 = 1e-2
CR_APPROX_MED = 0.02
K_FLAT_FACTOR = 2.0               # k-law reading (report-only)
HOLDOUT_BAR = 3e-3
DP_STAB_BAR = 1e-2
COCYCLE_BAR = 1e-2
RAWID_FACTOR = 3.0                # F4 settling line (report-only)
RAWID_ABS = 0.02                  # F4 absolute smallness bar
SMOOTH_MIN_STEPS = 10
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


# --------- pipeline, verbatim from port_schur_cocycle_probe
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


def cell_widths(uu):
    """Midpoint cells (lattice_parametrix verbatim; smooth world)."""
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def build_rung(kz, scramble_seed=None, comb=None, smooth=False):
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if smooth:
        # B1 world: smooth masses 2 e^{u/2} du on the TRUE lattice
        mm = 2.0 * np.exp(uu / 2.0) * cell_widths(uu)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h)


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
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
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN EXTRACTION GAUGE (lax2 verbatim): the SO(2) rotation
    pinning the deepest port node.  A chordal isometry and a
    Moebius map -- F1/F2/F3 are exactly gauge-free (see docstring
    honesty note)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, **kw):
    """One heavy build per rung (port_schur_cocycle verbatim): the
    negative-arm Gram E feeds the 12-index window compression (the
    controls' frame channel) and the dressed-port IIKS generators."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, alpha=b["alpha"],
               lamE=float(np.linalg.eigvalsh(E)[-1]))
    # ---- window compression (frame channel, verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    # ---- dressed port + IIKS generators (verbatim)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    """Raw carrier pairs p_j = (g_j, f_j), unit length; NO
    normalization anywhere in this probe."""
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 between unit pair rows."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def chord_mat(P):
    """Full pairwise chordal matrix (battery conditioning)."""
    return np.abs(P[:, None, 0] * P[None, :, 1]
                  - P[:, None, 1] * P[None, :, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (verbatim).  Used ONLY inside the exact
    three-anchor step map M = N_b^{-1} N_a -- never to normalize
    the carrier."""
    M = np.stack([p2, p0], axis=1)
    if abs(float(np.linalg.det(M))) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def apply_hom(T, P):
    Q = (T @ P.T).T
    n = np.linalg.norm(Q, axis=1)
    n[n < 1e-300] = 1.0
    return Q / n[:, None]


def moebius_fit(P, Q):
    """TLS Moebius fit (verbatim) -- F4 REFERENCE ONLY, never used
    to type F1/F2/F3."""
    rows = np.stack([P[:, 0] * Q[:, 1], P[:, 1] * Q[:, 1],
                     -P[:, 0] * Q[:, 0], -P[:, 1] * Q[:, 0]],
                    axis=1)
    _u, _s, Vh = np.linalg.svd(rows)
    a, b, c, d = Vh[-1]
    T = np.array([[a, b], [c, d]])
    return T, chordal(apply_hom(T, P), Q)


def sdet(p, q):
    """Signed 2x2 determinant det[p q] on homogeneous pairs."""
    return float(p[0] * q[1] - p[1] * q[0])


def cross_ratio(P, i, j, k, l):
    """Homogeneous cross-ratio cr(p_i, p_j; p_k, p_l)."""
    den = sdet(P[i], P[l]) * sdet(P[j], P[k])
    if abs(den) < 1e-300:
        return None
    return (sdet(P[i], P[k]) * sdet(P[j], P[l])) / den


def d_proj(A, B):
    """Projective distance d_P(A, B) = min_lambda ||A - lambda B||_F
    / ||A||_F = |sin angle(A, B)| (symmetric, scale-free)."""
    na = float(np.linalg.norm(A))
    nb = float(np.linalg.norm(B))
    if na < 1e-300 or nb < 1e-300:
        return 1.0
    c = float(np.sum(A * B)) / (na * nb)
    return math.sqrt(max(0.0, 1.0 - c * c))


def pair_pairs(ra, rb):
    """Raw unit pairs on the sorted common port alias indices of a
    rung pair; None if < MIN_COMMON_J common nodes."""
    com, ia, ib = np.intersect1d(ra.get("jp", []),
                                 rb.get("jp", []),
                                 return_indices=True)
    if len(com) < MIN_COMMON_J:
        return None
    Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
    Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
    return Pa, Pb, com


def quad_battery(Pa, Pb, deep_core=False):
    """F1 frozen battery: even-coverage node subsample (no depth
    bias), full quadruple enumeration on the subsample, top
    QUAD_ACCEPT_CAP survivors by conditioning score (min pairwise
    chordal, min over both rungs); returns the defect list and the
    reject count.  deep_core=True restricts to the DEEP_CORE_N
    deepest common nodes (report-only sub-battery)."""
    n = len(Pa)
    if deep_core:
        nodes = np.arange(min(DEEP_CORE_N, n))
    elif n > QUAD_NODE_CAP:
        nodes = np.unique(np.round(
            np.linspace(0, n - 1, QUAD_NODE_CAP)).astype(int))
    else:
        nodes = np.arange(n)
    Da, Db = chord_mat(Pa), chord_mat(Pb)
    cands, n_rej = [], 0
    for q in combinations(nodes.tolist(), 4):
        qi = list(q)
        score = 1.0
        ok = True
        for Dm in (Da, Db):
            sub = Dm[np.ix_(qi, qi)]
            vals = sub[np.triu_indices(4, 1)]
            spread = float(np.max(vals))
            if spread < 1e-300 or float(np.min(vals)) \
                    < COND_SEP_FRAC * spread:
                ok = False
                break
            score = min(score, float(np.min(vals)))
        if not ok:
            n_rej += 1
            continue
        cra = cross_ratio(Pa, *q)
        crb = cross_ratio(Pb, *q)
        if (cra is None or crb is None
                or not (CR_ABS_LO <= abs(cra) <= CR_ABS_HI)
                or not (CR_ABS_LO <= abs(crb) <= CR_ABS_HI)):
            n_rej += 1
            continue
        cands.append((score, q,
                      abs(crb - cra) / (1.0 + abs(cra))))
    cands.sort(key=lambda sqd: (-sqd[0], sqd[1]))
    return [d for _s, _q, d in cands[:QUAD_ACCEPT_CAP]], n_rej


def cond_triples(Pa, Pb):
    """F2 conditioned anchor triples, sorted by descending score =
    min pairwise chordal separation (min over both rungs);
    deterministic tie-break by lexicographic index order."""
    n = len(Pa)
    Da, Db = chord_mat(Pa), chord_mat(Pb)
    out = []
    for t in combinations(range(n), 3):
        ti = list(t)
        score = 1.0
        ok = True
        for Dm in (Da, Db):
            sub = Dm[np.ix_(ti, ti)]
            vals = sub[np.triu_indices(3, 1)]
            spread = float(np.max(vals))
            if spread < 1e-300 or float(np.min(vals)) \
                    < COND_SEP_FRAC * spread:
                ok = False
                break
            score = min(score, float(np.min(vals)))
        if ok:
            out.append((score, t))
    out.sort(key=lambda st: (-st[0], st[1]))
    return out


def anchor_map(Pa, Pb, t):
    """The EXACT (closed-form, fit-free) Moebius map determined by
    the three anchors t: M = N_b^{-1} N_a."""
    Na = norm_map(Pa[t[0]], Pa[t[1]], Pa[t[2]])
    Nb = norm_map(Pb[t[0]], Pb[t[1]], Pb[t[2]])
    if Na is None or Nb is None:
        return None
    M = np.linalg.solve(Nb, Na)
    return M / np.linalg.norm(M)


def primary_step(Pa, Pb):
    """The frozen primary three-anchor map of a pair; returns
    (M, triple, holdout_median, triples_list) or None."""
    tri = cond_triples(Pa, Pb)
    for score, t in tri:
        M = anchor_map(Pa, Pb, t)
        if M is None:
            continue
        keep = np.ones(len(Pa), dtype=bool)
        keep[list(t)] = False
        err = chordal(apply_hom(M, Pa), Pb)
        return M, t, float(np.median(err[keep])), tri
    return None


def q_stats(v):
    a = np.asarray(v, float)
    return (float(np.median(a)), float(np.percentile(a, 90)),
            float(np.max(a)))


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.2e  med %.2e  q75 %.2e" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


def build_ladder(smooth=False):
    rungs = []
    rk_max = 0.0
    for kz in core.frame_a_zones():
        r = rung_all(kz, smooth=smooth)
        if not isinstance(r, dict) or "f" not in r:
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    return rungs, rk_max


def k_battery(rungs, k, deep_core=False):
    """Pooled cr-defects for rung pairs at ladder separation k."""
    pooled, per_step, n_skip = [], [], 0
    for i in range(len(rungs) - k):
        pp = pair_pairs(rungs[i], rungs[i + k])
        if pp is None:
            n_skip += 1
            continue
        Pa, Pb, _com = pp
        dfs, _rej = quad_battery(Pa, Pb, deep_core=deep_core)
        if not dfs:
            n_skip += 1
            continue
        pooled.extend(dfs)
        per_step.append((rungs[i]["h"], rungs[i + k]["h"], dfs))
    return pooled, per_step, n_skip


def main():
    section("PRIME.PORT.MOEBIUS.CRFIREWALL.01 -- fit-free Moebius "
            "firewall on the raw port carrier (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; NO per-rung normalization anywhere; "
          "no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth ladder (all frame-A zones, "
            "h <= %d; machinery verbatim)" % H_DEEP_MAX)
    rungs, rk_max = build_ladder(smooth=False)
    print("    %d rungs, h %d .. %d; worst [Y,D_P] s3/s1 %.1e"
          % (len(rungs), rungs[0]["h"] if rungs else -1,
             rungs[-1]["h"] if rungs else -1, rk_max))
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")

    # ------------------------------------------------------------ F1
    section("F1 -- cross-ratio invariance, raw coordinate, frozen "
            "quadruple battery")
    print("    conditioning: min pairwise chordal >= %.0e x "
          "within-quadruple spread (both rungs);" % COND_SEP_FRAC)
    print("    |cr| in [%.0e, %.0e] on both rungs; accept cap %d "
          "per pair.  Dcr = |cr' - cr|/(1 + |cr|)."
          % (CR_ABS_LO, CR_ABS_HI, QUAD_ACCEPT_CAP))
    k_pooled = {}
    for k in K_SEPS:
        pooled, per_step, n_skip = k_battery(rungs, k)
        k_pooled[k] = pooled
        if k == 1:
            print("\n    per-step battery (k = 1; %d typed skips):"
                  % n_skip)
            for ha, hb, dfs in per_step:
                m, q90, mx = q_stats(dfs)
                print("    h %3d->%3d  n_quad %3d  med %.2e  "
                      "q90 %.2e  max %.2e"
                      % (ha, hb, len(dfs), m, q90, mx))
            n_steps_k1 = len(per_step)
    check("W3 >= %d k=1 steps with non-empty battery" % MIN_STEPS,
          n_steps_k1 >= MIN_STEPS, "%d steps" % n_steps_k1,
          kill="K1")
    m1, q901, mx1 = (q_stats(k_pooled[1]) if k_pooled[1]
                     else (1.0, 1.0, 1.0))
    print("\n    POOLED ladder distribution (k = 1, %d quadruples):"
          " med %.2e  q90 %.2e  max %.2e"
          % (len(k_pooled[1]), m1, q901, mx1))
    f1_type = ("CR-INVARIANT" if (m1 <= CR_INV_MED
                                  and q901 <= CR_INV_Q90) else
               "CR-APPROX" if m1 <= CR_APPROX_MED else "CR-DEAD")
    print("    TYPED: med %.2e vs %.0e (and q90 %.2e vs %.0e) / "
          "approx bar %.2f -> %s"
          % (m1, CR_INV_MED, q901, CR_INV_Q90, CR_APPROX_MED,
             f1_type))
    dc_pooled, _dc_steps, _dc_skip = k_battery(rungs, 1,
                                               deep_core=True)
    if dc_pooled:
        dc_med, dc_q90, dc_max = q_stats(dc_pooled)
        print("    DEEP-CORE sub-battery (%d deepest common "
              "nodes, %d quadruples, REPORT-ONLY): med %.2e  "
              "q90 %.2e  max %.2e"
              % (DEEP_CORE_N, len(dc_pooled), dc_med, dc_q90,
                 dc_max))
    else:
        dc_med = float("inf")
        print("    DEEP-CORE sub-battery: no measurable "
              "quadruples")
    check("F1.1 typed: %s (fit-free, gauge-free)" % f1_type, True)
    print("\n    THE k-LAW (reviewer null: neighbor property vs "
          "one global function):")
    meds_k = {}
    for k in K_SEPS:
        if k_pooled[k]:
            mk, qk, xk = q_stats(k_pooled[k])
            meds_k[k] = mk
            print("      k = %d : %5d quadruples  med %.2e  "
                  "q90 %.2e  max %.2e%s"
                  % (k, len(k_pooled[k]), mk, qk, xk,
                     "   <- mismatch null (h vs h+5)"
                     if k == 5 else ""))
        else:
            print("      k = %d : no measurable pairs" % k)
    if 1 in meds_k and 8 in meds_k and meds_k[1] > 0:
        ratio = meds_k[8] / meds_k[1]
        print("      med(k=8)/med(k=1) = %.2f -> %s (frozen "
              "reading, factor %.0f)"
              % (ratio, "LADDER-GLOBAL (one function)"
                 if ratio <= K_FLAT_FACTOR else
                 "GROWS WITH SEPARATION (smooth flow)",
                 K_FLAT_FACTOR))
    if 1 in meds_k and 5 in meds_k:
        print("      mismatch check: med(k=5) %.2e vs med(k=1) "
              "%.2e" % (meds_k[5], meds_k[1]))

    # ------------------------------------------------------------ F2
    section("F2 -- three-anchor holdout (exact maps, no fit) + "
            "anchor stability")
    print("    primary triple: max-min chordal separation (both "
          "rungs); stability over top-%d" % MAX_TRIPLES)
    print("    conditioned triples, pairwise d_P(A, B) = "
          "|sin angle|.")
    steps = []          # (i, Pa, Pb, com, M, t, holdout)
    hold_meds, dp_meds = [], []
    n_skip = 0
    for i in range(len(rungs) - 1):
        pp = pair_pairs(rungs[i], rungs[i + 1])
        if pp is None:
            n_skip += 1
            continue
        Pa, Pb, com = pp
        ps = primary_step(Pa, Pb)
        if ps is None:
            n_skip += 1
            continue
        M, t, hold, tri = ps
        maps = []
        for _sc, tt in tri[:MAX_TRIPLES]:
            Mt = anchor_map(Pa, Pb, tt)
            if Mt is not None:
                maps.append(Mt)
        dps = [d_proj(maps[a], maps[b])
               for a in range(len(maps))
               for b in range(a + 1, len(maps))]
        dpm = float(np.median(dps)) if dps else float("inf")
        hold_meds.append(hold)
        dp_meds.append(dpm)
        steps.append(dict(i=i, Pa=Pa, Pb=Pb, com=com, M=M, t=t,
                          hold=hold))
        print("    h %3d->%3d  n %2d  anchors %-12s  holdout med "
              "%.2e  n_tri %3d  d_P med %.2e"
              % (rungs[i]["h"], rungs[i + 1]["h"], len(com),
                 str(list(t)), hold, len(maps), dpm))
    med_hold = float(np.median(hold_meds)) if hold_meds else 1.0
    med_dp = float(np.median(dp_meds)) if dp_meds else 1.0
    print("    holdout ladder: %s" % quart(hold_meds))
    print("    d_P     ladder: %s" % quart(dp_meds))
    f2_type = ("ANCHOR-STABLE" if (med_hold <= HOLDOUT_BAR
                                   and med_dp <= DP_STAB_BAR)
               else "ANCHOR-FRAGILE")
    print("    TYPED: med holdout %.2e vs %.0e AND med d_P %.2e "
          "vs %.0e -> %s"
          % (med_hold, HOLDOUT_BAR, med_dp, DP_STAB_BAR, f2_type))
    check("F2.1 typed: %s (%d steps, %d typed skips)"
          % (f2_type, len(steps), n_skip), True)

    # ------------------------------------------------------------ F3
    section("F3 -- cocycle composition of the exact three-anchor "
            "maps (raw coordinate)")
    map_cache = {}
    for s in steps:
        map_cache[(s["i"], 1)] = s["M"]
    for k in (2, 4):
        for i in range(len(rungs) - k):
            pp = pair_pairs(rungs[i], rungs[i + k])
            if pp is None:
                continue
            ps = primary_step(pp[0], pp[1])
            if ps is None:
                continue
            map_cache[(i, k)] = ps[0]
    dp_coc = []
    for k in (2, 4):
        n_cmp = 0
        vals = []
        for i in range(len(rungs) - k):
            if (i, k) not in map_cache:
                continue
            prod = np.eye(2)
            ok = True
            for j in range(k):
                if (i + j, 1) not in map_cache:
                    ok = False
                    break
                prod = map_cache[(i + j, 1)] @ prod
            if not ok:
                continue
            d = d_proj(map_cache[(i, k)], prod)
            vals.append(d)
            n_cmp += 1
            print("    h %3d ->(+%d) %3d : d_P(direct, product) "
                  "%.2e"
                  % (rungs[i]["h"], k, rungs[i + k]["h"], d))
        if vals:
            print("    k = %d summary: %d comparisons, %s"
                  % (k, n_cmp, quart(vals)))
        dp_coc.extend(vals)
    med_coc = float(np.median(dp_coc)) if dp_coc else 1.0
    f3_type = ("COCYCLE-EXACT" if med_coc <= COCYCLE_BAR
               else "COCYCLE-BROKEN")
    print("    TYPED: pooled median d_P %.2e vs %.0e -> %s "
          "(%d comparisons)"
          % (med_coc, COCYCLE_BAR, f3_type, len(dp_coc)))
    check("F3.1 typed: %s" % f3_type, True)

    # ------------------------------------------------------------ F4
    section("F4 -- significance anatomy (report; raw = frozen "
            "extraction gauge, NO normalization)")
    print("    step        spread   med-arc  prec-floor  raw-id "
          "med  fit res med")
    raw_ids, fit_res = [], []
    for s in steps:
        i = s["i"]
        Pa, Pb = s["Pa"], s["Pb"]
        Da = chord_mat(Pa)
        vals = Da[np.triu_indices(len(Pa), 1)]
        spread = float(np.max(vals))
        arc = float(np.median(vals))
        floor = max(rungs[i].get("rk", 0.0),
                    rungs[i + 1].get("rk", 0.0))
        rid = float(np.median(chordal(Pa, Pb)))
        _T, res = moebius_fit(Pa, Pb)
        fr = float(np.median(res))
        raw_ids.append(rid)
        fit_res.append(fr)
        print("    h %3d->%3d  %.3f    %.3f    %.1e     %.2e"
              "     %.2e"
              % (rungs[i]["h"], rungs[i + 1]["h"], spread, arc,
                 floor, rid, fr))
    med_rid = float(np.median(raw_ids)) if raw_ids else 1.0
    med_fit = float(np.median(fit_res)) if fit_res else 1.0
    print("    ladder: raw-id med %.2e | fit res med %.2e "
          "(settling factor %.0f, abs bar %.2f)"
          % (med_rid, med_fit, RAWID_FACTOR, RAWID_ABS))
    if med_rid <= RAWID_FACTOR * med_fit and med_rid <= RAWID_ABS:
        f4_line = ("RAW-INVARIANT: the un-normalized carrier is "
                   "already rung-invariant -- stronger and "
                   "gauge-free; the tautology worry is settled "
                   "in the POSITIVE direction (no normalization "
                   "was applied anywhere in this probe).")
    elif med_rid <= RAWID_FACTOR * med_fit:
        f4_line = ("RAW-NEITHER: raw identity is as good as the "
                   "fit but BOTH are poor -- in the raw "
                   "coordinate neither identity nor any single "
                   "Moebius map captures the step; the "
                   "predecessor's tiny normalized residual was "
                   "manufactured by the three-point pinning "
                   "(reviewer's worry CONFIRMED).")
    else:
        f4_line = ("RAW-MOVES: the raw carrier moves between "
                   "rungs; the Moebius step carries real content "
                   "beyond identity (fit beats raw identity by "
                   "more than the settling factor).")
    print("    " + f4_line)
    check("F4.1 anatomy reported (raw-id med %.2e, fit med %.2e)"
          % (med_rid, med_fit), True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    print("  C1 frame-die controls (kz %d, must fire):" % CTRL_KZ)
    ok = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        rc = rung_all(CTRL_KZ, **kw)
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> FRAME DIES"
                  % (nmc, rc))
            continue
        if "lamC" not in rc:
            print("    %-8s: window unavailable -> FRAME DIES"
                  % nmc)
            continue
        fired = (rc["lamO"] > 1.0) or (rc["lamC"] > 1.0)
        ok &= fired
        print("    %-8s: lam(out) %.3e | lam(C_J) %.3e | lam(E) "
              "%.3e -> fires via %s"
              % (nmc, rc["lamO"], rc["lamC"], rc["lamE"],
                 "EXTERIOR" if rc["lamO"] > 1.0 else
                 "WINDOW" if rc["lamC"] > 1.0 else "NOTHING"))
    check("C1 CONTROLS FIRE (frame death on both)", ok, kill="K3")

    print("\n  C2 SMOOTH-MASS world (masses 2 e^{u/2} du on the "
          "true lattice, lattice_parametrix B1;")
    print("     frame-SURVIVING control -- geometric vs "
          "arithmetic; report-only):")
    sm_rungs, sm_rk = build_ladder(smooth=True)
    n_frame = sum(1 for r in sm_rungs if "lamC" in r)
    n_sub = sum(1 for r in sm_rungs
                if "lamC" in r and r["lamC"] <= 1.0
                and r.get("lamO", 2.0) <= 1.0)
    print("    smooth ladder: %d rungs with carrier (%d with "
          "window; %d subcritical); worst s3/s1 %.1e"
          % (len(sm_rungs), n_frame, n_sub, sm_rk))
    sm_pooled, sm_steps, sm_skip = k_battery(sm_rungs, 1)
    sm_holds = []
    for i in range(len(sm_rungs) - 1):
        pp = pair_pairs(sm_rungs[i], sm_rungs[i + 1])
        if pp is None:
            continue
        ps = primary_step(pp[0], pp[1])
        if ps is not None:
            sm_holds.append(ps[2])
    if len(sm_steps) < SMOOTH_MIN_STEPS:
        c2_label = "SMOOTH-FRAME-DEAD"
        print("    only %d measurable smooth steps (< %d) -> %s "
              "(no answer from this control)"
              % (len(sm_steps), SMOOTH_MIN_STEPS, c2_label))
    else:
        sm_med, sm_q90, sm_max = q_stats(sm_pooled)
        sm_hold_med = (float(np.median(sm_holds)) if sm_holds
                       else float("inf"))
        print("    smooth k=1 battery: %d steps, %d quadruples "
              "(%d typed skips): med %.2e  q90 %.2e  max %.2e"
              % (len(sm_steps), len(sm_pooled), sm_skip,
                 sm_med, sm_q90, sm_max))
        print("    smooth primary holdout median: %s"
              % (("%.2e" % sm_hold_med)
                 if sm_hold_med < float("inf") else "n/a"))
        c2_label = ("SMOOTH-CARRIES-CR"
                    if sm_med <= CR_APPROX_MED
                    else "SMOOTH-CR-DEAD")
        print("    TYPED REPORT: smooth cr med %.2e vs %.2f -> %s"
              % (sm_med, CR_APPROX_MED, c2_label))
        print("    reading: %s"
              % ("the cr-structure is GEOMETRIC -- the lattice "
                 "with smooth masses already carries it"
                 if c2_label == "SMOOTH-CARRIES-CR" else
                 "the cr-structure is ARITHMETIC -- the actual "
                 "Lambda masses are load-bearing"))
        if f1_type == "CR-DEAD":
            sm_dc, _s, _k = k_battery(sm_rungs, 1,
                                      deep_core=True)
            sm_dc_med = (q_stats(sm_dc)[0] if sm_dc
                         else float("inf"))
            print("    DEEP-CORE comparison (truth full battery "
                  "is CR-DEAD; report-only): truth %.2e vs "
                  "smooth %s (reading bar %.2f):"
                  % (dc_med, ("%.2e" % sm_dc_med)
                     if sm_dc_med < float("inf") else "n/a",
                     CR_APPROX_MED))
            print("      %s"
                  % ("BOTH deep cores coherent -> the surviving "
                     "deep-core cr-coherence is GEOMETRIC"
                     if (dc_med <= CR_APPROX_MED
                         and sm_dc_med <= CR_APPROX_MED) else
                     "truth deep core coherent, smooth one dead "
                     "-> the surviving deep-core cr-coherence "
                     "is ARITHMETIC"
                     if dc_med <= CR_APPROX_MED else
                     "no deep-core coherence on truth either -> "
                     "nothing survives to localize"))
    check("C2 smooth-mass control reported: %s" % c2_label, True)

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("CRFIREWALL-MEASURED / %s / %s / %s / %s"
                   % (f1_type, f2_type, f3_type, c2_label))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (F1 pooled med %.2e q90 %.2e; F2 holdout med "
              "%.2e d_P med %.2e; F3 med %.2e;"
              % (m1, q901, med_hold, med_dp, med_coc))
        print("   F4 raw-id med %.2e vs fit med %.2e)"
              % (med_rid, med_fit))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source iiks_gauge_firewall_probe (embedded BYTE-EXACT, raw string)
_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""iiks_gauge_firewall_probe -- PRIME.PORT.MOEBIUS.GAUGEFW.01
(EXPLORATION ONLY, experiments/; round 48, reviewer probes 2+3 of
the round-47 review: prove the carrier invariance is NOT
manufactured by the per-rung normalization, 2026-08-09).

THE QUESTION (frozen): moebius_source_step_probe measured
CARRIER-INVARIANT -- but under a PER-RUNG three-point PSL(2,R)
normalization.  The reviewer's tautology warning: a per-rung gauge
choice G_h is a free function of h; choosing G_{h+1} = G_h M_h^{-1}
forces every step to the identity.  THE FIVE GAUGE-VALIDITY
CONDITIONS (reviewer, quoted verbatim): a valid gauge must be
"(1) frozen before comparison, (2) source-only, (3) identically
defined on all rungs, (4) unchanged on truth and controls,
(5) using NO neighbor-rung information."  This probe re-derives
everything in three SOURCE-FROZEN gauges satisfying (1)-(5), asks
where the discarded scalar lambda went (reviewer probe 2), and
tests whether the Moebius step is the projectivization of the
source Jacobi transfer (reviewer probe 3).

THE LADDER (frozen, predecessor verbatim): all frame-A zones
(core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive rung pairs with >= 8 common port alias indices.

FROZEN PROTOCOL (2026-08-09, frozen + SHA-hashed before first run;
all bars frozen before the run):

 W   PIPELINE (predecessor verbatim): heavy build per rung, SPEC
     v2 IIKS extraction of the antisymmetric generators (f, g) of
     C = [Y, D_P] (NO gauge rotation applied at extraction; each
     gauge below fixes its own frame).  Wards: W1 >= 30 rungs;
     W2 [Y, D_P] rank 2 on every rung (s3/s1 <= 1e-10); W3 the
     frozen reference set exists.  FROZEN REFERENCES: J* = alias
     indices present on >= 0.90 of rungs (deterministic
     availability stepdown 0.90 -> 0.80 -> 0.70 if |J*| < 4,
     reported); reference PAIR = two smallest J* indices
     (jr1 < jr2); step ANCHORS = three smallest J* indices.  These
     are GRID indices, not rung-dependent choices -- conditions
     (1)-(5) hold: frozen rule, source-side index bookkeeping
     only, same rule on every rung and on the controls, no
     neighbor-rung data.

 G0  BASELINE (printed, not a claim): the predecessor's per-rung
     three-point normalization + TLS step fit, machinery verbatim
     -- reproduces the numbers the reviewer challenged (median fit
     residual, median identity-candidate residual).

 G1  SOURCE-FROZEN GAUGES (three candidates, all rung-local and
     source-only; each fully fixes the GL(2) frame of (f, g)):
     (i)  WRONSKIAN gauge "W": the unique generator basis with
          (f(jr1), f(jr2)) = (1, 0) and (g(jr1), g(jr2)) = (0, 1)
          -- then the antisymmetric pairing W(jr1, jr2) =
          f(jr1) g(jr2) - g(jr1) f(jr2) = 1 at the FIXED reference
          pair of grid indices, and g's component along the frozen
          reference direction e_{jr1} vanishes at the deepest
          reference node (g(jr1) = 0), as demanded.  PRECISE
          STATEMENT of the amendment: the prompt's two conditions
          (pairing = 1, g(jr1) = 0) leave a one-parameter shear
          f -> f + t g free (it preserves both); the interpolation
          frame above realizes both conditions AND kills the
          shear; it is the unique completion that stays rung-local
          and reference-pair-only.  Degenerate 2x2 node matrix
          (s2/s1 <= 1e-12) or missing reference index = typed
          rung skip.
     (ii) ASYMPTOTIC gauge "A": window-edge (y -> 1) frame.  Edge
          functionals from the rung's OWN two deepest port nodes
          (largest y): L1(v) = linear extrapolation of v to y = 1,
          L2(v) = (v(y_1) - v(y_0))/(y_0 - y_1) (the leading slope
          in 1 - y).  Frame: (L1, L2)(f) = (1, 0), (L1, L2)(g) =
          (0, 1) -- f carries the unit leading coefficient, g is
          purely subleading.  Source-computable from the
          extraction; same rule on every rung.
     (iii) DETERMINANT-PHASE gauge "D": det-normalize the
          extraction SVD convention itself: f = U[:, 0], g =
          U[:, 1] (unit vectors, det-scale s1 divided out), the
          orientation sign fixed by C = +s1 (f g^T - g f^T), the
          SO(2) rotation of the (degenerate) singular pair fixed
          by the frozen convention g = 0 with f > 0 at the rung's
          deepest port node (smallest alias index) -- a fixed
          sign/order convention, no per-rung choice.
     UNDER EACH GAUGE: the carrier r_h = g/f at the common nodes;
     the rung-to-rung RAW chordal deviation at matched nodes (NO
     further normalization of any kind); the step map M_h = the
     unique Moebius map through the carrier values at the three
     frozen anchors (exact three-point construction, no fitting).
     TYPED per gauge: RAW-INVARIANT iff median over steps of the
     per-step median raw chordal deviation <= 0.05, else
     RAW-MOVING.  CROSS-GAUGE: for each of the three gauge pairs,
     the single global conjugation S is solved from the FIRST
     common valid step (Sylvester nullspace; that anchor step is
     excluded from scoring) and the pairwise projective distance
     d_P(S M^a S^-1, M^b) is medianed over the remaining steps.
     TYPED: GAUGE-ROBUST iff all three pairwise medians <= 0.05
     AND the per-gauge RAW labels agree; GAUGE-MADE iff the
     baseline G0 invariance holds (median id-res <= 0.05) while NO
     frozen gauge is RAW-INVARIANT and the cross-gauge agreement
     fails at 0.20 (the reviewer kill -- reported plainly);
     GAUGE-PARTIAL otherwise.

 G2  THE SCALAR COCYCLE (reviewer probe 2, 'where did lambda
     go'): the quotient r = g/f is blind to (f, g) -> lambda_h
     (f, g).  In gauge (i) the frame is FULLY fixed, so the
     gauged generator values are data.  FROZEN: lambda_h =
     median_j |f_{h+1}(j)| / |f_h(j)| over the matched common
     nodes j (the two pinned reference nodes excluded -- f(jr1) =
     1 and f(jr2) = 0 identically by the gauge).  Printed: the
     lambda ladder, its cumulative log sum, and the tau ladder
     tau_h = 1 - lam_max(E_h) (the Krein wall margin).  SCORED:
     Pearson correlation and OLS slope of cumsum(log lambda)
     against log tau at the arriving rung, over steps with
     tau > 0.  TYPED: LAMBDA-IS-WALL iff |corr| >= 0.90 (the
     reviewer's boxed hypothesis: the projective carrier is
     universal, the arithmetic sits in the scalar cocycle);
     LAMBDA-PARTIAL iff |corr| >= 0.60; else LAMBDA-FLAT.
     (Unscored: the same correlation in gauges (ii) and (iii),
     printed.)

 G3  JACOBI TRANSFER IDENTIFICATION (reviewer probe 3): the
     SOURCE Jacobi one-step transfer of the tilde-measure chain
     (cd_pick_scalarization convention frozen: positive-arm
     folded tilde measure, Lanczos chain a_k = al[k], b_k =
     be[k]):
        T_k(z) = [[ (z - a_k)/b_k, -b_{k-1}/b_k ], [1, 0]]
     at the FROZEN spectral parameter z_ref = 1.0 (the window
     edge y -> 1 in the x = cos theta variable -- the port edge,
     rung-independent, source-only; matches the gauge (ii)
     anchor point).  CANDIDATE: the measured step M_h (gauge (i))
     ~ projectivization of the product of the Jacobi transfers
     entering between rung h and h+1: J_h = T_{h_b - 1} ... T_
     {h_a} from the DEEPER rung's chain (the chain that contains
     the entering levels); equal-h steps carry the empty product
     (identity).  COMPARISON: NO free parameters beyond the
     single global conjugation S solved from the first step with
     dh >= 5 (excluded from scoring); scored = median d_P(S J_h
     S^-1, M_h) over the remaining steps.  TYPED: JACOBI-DERIVED
     iff median <= 0.05 / JACOBI-PARTIAL iff <= 0.20 /
     JACOBI-DEAD.  Unscored diagnostic: corr(log lambda_h,
     accumulated log growth of the transfer product) -- the G2/G3
     bridge.  HONEST CAVEAT (frozen): the same identification is
     run on the SMOOTH-MASS world; if it holds there too, the
     Moebius motion is generic OPRL kinematics (universal
     geometry) and the arithmetic is confirmed to sit in G2's
     scalar / the measure itself -- reported as sublabel
     UNIVERSAL-KINEMATICS.

 SM  SMOOTH-MASS WORLD (the frame-surviving control throughout,
     christoffel_pnt_gamma W3 convention frozen: atoms at the
     ACTUAL positions u_n carrying the smooth PNT Voronoi cell
     masses m0_j = 4 (e^{b_j/2} - e^{b_{j-1}/2}), b_0 = 0, b_j =
     (u_j + u_{j+1})/2, b_ka = 2 alpha): the full ladder is
     rebuilt with the smooth comb and G1 raw deviations, the G2
     correlation and the G3 identification are re-measured with
     the SAME frozen gauges/references (condition (4)).  Frame
     survival census printed; if < 10 smooth steps are available
     the affected blocks are typed SMOOTH-UNAVAILABLE (reported,
     no kill -- the truth answer stands on its own).

 C   CONTROLS (kz 9, must fire): Epstein (lambda_eps recursion
     comb) + scramble (seed 1); frame death reported per control
     (window unavailable / lam(out) > 1 / lam(C_J) > 1 /
     extraction unavailable).  Silent on both -> CONTROL-DEAD.
     The smooth-mass world is the frame-SURVIVING control and is
     not required to fire.

KILLS: K1 pipeline ward breaks (rungs / rank-2 / references /
gauge-(i) step count / lambda ladder) -> PIPELINE-BROKEN; K3
Epstein+scramble silent -> CONTROL-DEAD.

VERDICT (frozen enum): GAUGEFW-MEASURED with typed sublabels
GAUGE-ROBUST / GAUGE-PARTIAL / GAUGE-MADE (G1, + per-gauge
RAW-INVARIANT / RAW-MOVING), LAMBDA-IS-WALL / LAMBDA-PARTIAL /
LAMBDA-FLAT (G2), JACOBI-DERIVED / JACOBI-PARTIAL / JACOBI-DEAD
(G3, + UNIVERSAL-KINEMATICS caveat where applicable); else
PIPELINE-BROKEN / CONTROL-DEAD.

SPEC v2 AMENDMENTS (documented before the first run; fail-first
preserved): (i) gauge (i) is concretized as the interpolation
frame at the frozen reference pair -- the prompt's two conditions
alone leave a one-parameter shear free (stated precisely in G1);
(ii) z_ref = 1.0 frozen (window edge; the only rung-independent
source-side spectral point); (iii) the lambda median excludes the
two gauge-pinned reference nodes (0/0 there by construction);
(iv) equal-h ladder steps carry the empty Jacobi product and the
entering levels are hosted by the deeper rung's chain; (v) the
global-conjugation anchor steps (first common step for G1 cross
pairs; first dh >= 5 step for G3) are excluded from the scored
medians; (vi) cumulative log lambda is accumulated over the
measured step sequence (typed skips break no bookkeeping).

SPEC v3 AMENDMENTS (documented after the first full run; every
first-run typed outcome is quoted so nothing is silently
upgraded): (vii) DEGENERACY GUARD: the first run printed gauge
(ii) raw deviation 0.0000 on every step -- invariance of a
COLLAPSED (near-constant) carrier is vacuous, so each gauge now
also reports the per-rung carrier SPREAD (median pairwise chordal
distance over the common nodes, the two gauge-pinned reference
nodes excluded) and types RAW-DEGENERATE iff the median spread
< 0.05; RAW-INVARIANT now additionally requires median spread >=
0.05.  (viii) ROBUST GLOBAL CONJUGATION: the first run solved S
from the single first common step; the Sylvester nullspace vector
came out singular on two of the three gauge pairs (cross d_P
printed as inf over 0 steps) because near-identity step families
make the one-step Sylvester problem ill-posed.  v3 scores the
better of TWO frozen global candidates: S = Id (the trivial
global conjugation) and S = the joint least-squares Sylvester
solve stacked over ALL common steps (still exactly ONE global
conjugation, 3 projective dof against ~40 steps); both medians
are printed.  The same robustification applies to G3 (first-run
G3 numbers under the one-step solve: truth med d_P 1.0000, smooth
med d_P 1.0000, kappa corr -0.14/-0.11).  (ix) SMOOTH-FRAME-DEAD:
the first run measured lam(E) >= 1 on ALL 42 smooth-mass rungs
(min tau -2.0e9) -- the smooth-mass world is NOT frame-surviving
under this probe's Gram frame; it is typed SMOOTH-FRAME-DEAD, its
measurements are still printed as the universality caveat (with
that caveat stated), and its G2 correlation uses log|tau| (tau <
0 throughout, disclosed).  (x) unscored diagnostic added: the
extraction scale ladder corr(log s1, log tau) over rungs (s1 =
the [Y, D_P] commutator scale) -- the scale channel the gauge-(i)
lambda (which pins f(jr1) = 1) cannot see.  (xi) G1.0 FRAME
SELF-TEST ward: every gauge frame is re-verified against its
defining linear conditions (gauge (i): interpolation values;
gauge (ii): edge functionals; gauge (iii): unit norms + rotation
zero + sign) at 1e-8 -- a broken frame is a pipeline kill (K1);
the per-gauge relative motion (median raw dev / median spread) is
printed alongside.  No frozen bar moved; first-run typed
outcomes: G1 GAUGE-PARTIAL (W:RAW-INVARIANT before the spread
guard, A:RAW-INVARIANT before the spread guard, D:RAW-MOVING;
cross d_P inf/inf/0.98 under the ill-posed one-step solve),
G2 LAMBDA-FLAT (corr 0.1292), G3 JACOBI-DEAD (med d_P 1.0000).

NO RH claim -- gauge-frozen invariance, a scalar cocycle tracking
a wall margin, or a Jacobi-transfer identification are numerical
measurements on compressed truncations, not theorems about zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; extraction + ladder
machinery verbatim from moebius_source_step_probe.py /
port_schur_cocycle_probe.py (PRIME.PORT.MOEBIUS.SOURCE.01 /
PRIME.PORT.SCHURSTEP.01); Jacobi chain convention from
cd_pick_scalarization_probe.py (PRIME.CD.PICKDEFECT.01);
smooth-mass cells from christoffel_pnt_gamma_probe.py.  IIKS =
Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/iiks_gauge_firewall_probe.py
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

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
MIN_RUNGS = 30
MIN_PAIRS = 30
MIN_COMMON_J = 8
MIN_JSTAR = 4
JSTAR_FRACS = (0.90, 0.80, 0.70)
RANK_BAR = 1e-10
REF_SEP_MIN = 1e-6
FRAME_COND = 1e-12          # min s2/s1 of the 2x2 frame solve
CTRL_KZ = 9

RAW_INV_BAR = 0.05          # G1: RAW-INVARIANT bar (median chordal)
DP_ROBUST_BAR = 0.05        # G1: cross-gauge d_P robust bar
DP_PART_BAR = 0.20          # G1: cross-gauge d_P partial bar
LAM_WALL_CORR = 0.90        # G2: LAMBDA-IS-WALL bar
LAM_PART_CORR = 0.60        # G2: LAMBDA-PARTIAL bar
JAC_DER_BAR = 0.05          # G3: JACOBI-DERIVED bar
JAC_PART_BAR = 0.20         # G3: JACOBI-PARTIAL bar
Z_REF = 1.0                 # G3: frozen spectral parameter
ANCHOR_MIN_DH = 5           # G3: conjugation anchor needs dh >= 5
MIN_SMOOTH_STEPS = 10
GAUGES = ("W", "A", "D")
GAUGE_NAMES = {"W": "(i) WRONSKIAN", "A": "(ii) ASYMPTOTIC",
               "D": "(iii) DET-PHASE"}
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


# --------- pipeline, verbatim from moebius_source_step_probe
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
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    return dict(d=d, L=2 * M - 2, D=D, alpha=alpha, h=h,
                uu=uu, mm=mm, M=M)


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
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
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim; sign/order convention fixed, NO rotation applied)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def rung_all(kz, **kw):
    """One heavy build per rung (predecessor verbatim) + Jacobi
    chain storage; generators stored WITHOUT any gauge rotation."""
    b = build_rung(kz, **kw)
    h, L, D = b["h"], b["L"], b["D"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    xs, ws, _ = folded_measure(b["d"], L, +1.0)
    ys, vs, uf_n = folded_measure(b["d"], L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    lamE = float(np.linalg.eigvalsh(E)[-1])
    out = dict(kz=kz, h=h, alpha=b["alpha"], M=b["M"], D=D,
               lamE=lamE, tau=1.0 - lamE, al=al, be=be)
    # ---- window compression (controls' frame channel, verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
    # ---- dressed port + IIKS generators (verbatim, no rotation)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        out["fS"], out["gS"] = f, g
        out["s1"] = float(sv[0])
        out["jp"], out["yp"] = uf_n[ip], ys[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    M = np.stack([p2, p0], axis=1)
    if abs(float(np.linalg.det(M))) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def apply_hom(T, P):
    Q = (T @ P.T).T
    n = np.linalg.norm(Q, axis=1)
    n[n < 1e-300] = 1.0
    return Q / n[:, None]


def moebius_fit(P, Q):
    rows = np.stack([P[:, 0] * Q[:, 1], P[:, 1] * Q[:, 1],
                     -P[:, 0] * Q[:, 0], -P[:, 1] * Q[:, 0]],
                    axis=1)
    _u, _s, Vh = np.linalg.svd(rows)
    a, b, c, d = Vh[-1]
    T = np.array([[a, b], [c, d]])
    return T, chordal(apply_hom(T, P), Q)


def quart(v):
    q = np.percentile(np.asarray(v, float), [25, 50, 75])
    return "q25 %.4f  med %.4f  q75 %.4f" % tuple(q)


def eps_comb(kz):
    rr = core.build_window(kz)
    N_E = int(math.floor(math.exp(2.0 * rr["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    return (np.log(nn.astype(float)),
            2.0 * lamE_[nn] / np.sqrt(nn.astype(float)))


def cells_of(uu, alpha):
    """FROZEN Voronoi cells on [0, 2 alpha] + exact rho^0 masses
    (christoffel_pnt_gamma verbatim)."""
    bb = np.concatenate([[0.0], 0.5 * (uu[1:] + uu[:-1]),
                         [2.0 * alpha]])
    m0c = 4.0 * (np.exp(0.5 * bb[1:]) - np.exp(0.5 * bb[:-1]))
    return bb, m0c


# ------------------------------------------- gauge + projective tools
def solve_frame(B, F, G):
    """Unique basis (fN, gN) of span(F, G) with the two linear
    functionals (rows of B) taking values (1,0) / (0,1); None if
    the functional matrix is degenerate."""
    sv = np.linalg.svd(B, compute_uv=False)
    if sv[0] <= 0 or sv[1] / sv[0] <= FRAME_COND:
        return None
    cf = np.linalg.solve(B, np.array([1.0, 0.0]))
    cg = np.linalg.solve(B, np.array([0.0, 1.0]))
    return cf[0] * F + cf[1] * G, cg[0] * F + cg[1] * G


def edge_functionals(r):
    """The two window-edge functionals of gauge (ii): linear
    extrapolation to y = 1 and the leading slope in 1 - y, built
    from the rung's own two deepest port nodes."""
    yp = np.asarray(r["yp"], float)
    o = np.argsort(-yp)
    e0, e1 = int(o[0]), int(o[1])
    y0, y1 = float(yp[e0]), float(yp[e1])
    if abs(y0 - y1) <= 1e-15:
        return None

    def L1(v):
        return v[e0] + (v[e1] - v[e0]) * (1.0 - y0) / (y1 - y0)

    def L2(v):
        return (v[e1] - v[e0]) / (y0 - y1)
    return L1, L2


def gauge_frames(r, refs):
    """The three source-frozen gauges on one rung; each entry is
    (f, g) arrays over the port nodes, or None (typed skip)."""
    out = {"W": None, "A": None, "D": None}
    if "fS" not in r:
        return out
    F, G = r["fS"], r["gS"]
    jp = [int(j) for j in r["jp"]]
    # (i) WRONSKIAN: interpolation frame at the frozen grid pair
    if refs[0] in jp and refs[1] in jp:
        k1, k2 = jp.index(refs[0]), jp.index(refs[1])
        B = np.array([[F[k1], G[k1]], [F[k2], G[k2]]])
        out["W"] = solve_frame(B, F, G)
    # (ii) ASYMPTOTIC: window-edge value/slope frame (own edge)
    Ls = edge_functionals(r)
    if Ls is not None:
        L1, L2 = Ls
        B = np.array([[L1(F), L1(G)], [L2(F), L2(G)]])
        out["A"] = solve_frame(B, F, G)
    # (iii) DET-PHASE: unit SVD basis + frozen rotation/sign
    s1 = r["s1"]
    f3 = F / math.sqrt(s1)
    g3 = G / math.sqrt(s1)
    m0 = int(np.argmin(r["jp"]))
    rr = math.hypot(f3[m0], g3[m0])
    if rr > 1e-300:
        c, s = f3[m0] / rr, g3[m0] / rr
        out["D"] = (c * f3 + s * g3, -s * f3 + c * g3)
    return out


def frame_selftest(rungs, refs):
    """G1.0 (v3 xi): re-verify every gauge frame against its
    defining conditions; returns max deviation per gauge."""
    dev = {g: 0.0 for g in GAUGES}
    for r in rungs:
        fr = gauge_frames(r, refs)
        jp = [int(j) for j in r.get("jp", [])]
        if fr["W"] is not None:
            k1, k2 = jp.index(refs[0]), jp.index(refs[1])
            fN, gN = fr["W"]
            dev["W"] = max(dev["W"], abs(fN[k1] - 1.0),
                           abs(fN[k2]), abs(gN[k1]),
                           abs(gN[k2] - 1.0))
        if fr["A"] is not None:
            L1, L2 = edge_functionals(r)
            fN, gN = fr["A"]
            dev["A"] = max(dev["A"], abs(L1(fN) - 1.0),
                           abs(L2(fN)), abs(L1(gN)),
                           abs(L2(gN) - 1.0))
        if fr["D"] is not None:
            f3, g3 = fr["D"]
            m0 = int(np.argmin(r["jp"]))
            dev["D"] = max(dev["D"],
                           abs(float(np.linalg.norm(f3)) - 1.0),
                           abs(float(np.linalg.norm(g3)) - 1.0),
                           abs(g3[m0]), max(0.0, -f3[m0]))
    return dev


def proj_dist(A, B):
    """Projective (sine) distance between real 2x2 matrices mod
    scale and sign."""
    na = float(np.linalg.norm(A))
    nb = float(np.linalg.norm(B))
    if na < 1e-300 or nb < 1e-300:
        return 1.0
    ipd = float(np.sum(A * B)) / (na * nb)
    return math.sqrt(max(0.0, 1.0 - ipd * ipd))


def conj_joint(As, Bs):
    """ONE global S with B_i ~ S A_i S^{-1} for all i: joint
    least-squares Sylvester solve (stacked nullspace of
    B_i S - S A_i); returns (S, s_min/s_max of the stack)."""
    rows = []
    for A, B in zip(As, Bs):
        L = np.zeros((4, 4))
        for j in range(4):
            E = np.zeros((2, 2))
            E[j // 2, j % 2] = 1.0
            L[:, j] = (B @ E - E @ A).ravel()
        rows.append(L)
    L = np.concatenate(rows, axis=0)
    _u, sv, Vh = np.linalg.svd(L)
    S = Vh[-1].reshape(2, 2)
    return S, float(sv[-1] / max(sv[0], 1e-300))


def conj_apply(S, A):
    dS = float(np.linalg.det(S))
    if abs(dS) < 1e-12 * float(np.linalg.norm(S)) ** 2:
        return None
    return S @ A @ np.linalg.inv(S)


def kappa(M):
    d = float(np.linalg.det(M))
    if abs(d) < 1e-300:
        return float("inf")
    return float(np.trace(M)) ** 2 / d


def pearson(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if len(x) < 3 or float(np.std(x)) < 1e-15 \
            or float(np.std(y)) < 1e-15:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def jacobi_product(al, be, ka, kb, z):
    """prod_{k=ka}^{kb-1} T_k(z), Frobenius-renormalized per
    factor; returns (J, accumulated log norm)."""
    J = np.eye(2)
    lognorm = 0.0
    for k in range(ka, kb):
        Tk = np.array([[(z - al[k]) / be[k], -be[k - 1] / be[k]],
                       [1.0, 0.0]])
        J = Tk @ J
        n = float(np.linalg.norm(J))
        lognorm += math.log(n)
        J /= n
    return J, lognorm


# ------------------------------------------- ladder-level machinery
def build_ladder(comb_of=None, tag="truth"):
    """Build all frame-A rungs; comb_of(kz, uu, alpha) -> comb or
    None for the truth comb."""
    rungs = []
    rk_max = 0.0
    n_incomplete = 0
    for kz in core.frame_a_zones():
        kw = {}
        if comb_of is not None:
            rr0 = core.build_window(kz)
            uu = np.asarray(rr0["uu"], float)
            kw["comb"] = comb_of(uu, rr0["alpha"])
        r = rung_all(kz, **kw)
        if r == "TOO-DEEP":
            continue
        if not isinstance(r, dict):
            n_incomplete += 1
            continue
        rk_max = max(rk_max, r.get("rk", 1.0))
        rungs.append(r)
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    print("    [%s] %d rungs (h %d .. %d), %d incomplete chains, "
          "worst rank s3/s1 %.1e   [t %.0f s]"
          % (tag, len(rungs), rungs[0]["h"] if rungs else -1,
             rungs[-1]["h"] if rungs else -1, n_incomplete,
             rk_max, time.time() - T0), flush=True)
    return rungs, rk_max


def ladder_pairs(rungs):
    pairs = []
    n_skip = 0
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        com, ia, ib = np.intersect1d(ra.get("jp", []),
                                     rb.get("jp", []),
                                     return_indices=True)
        if len(com) >= MIN_COMMON_J and "fS" in ra and "fS" in rb:
            pairs.append(dict(ra=ra, rb=rb, com=com, ia=ia, ib=ib))
        else:
            n_skip += 1
    return pairs, n_skip


def jstar_refs(rungs):
    all_jp = [set(int(j) for j in r.get("jp", [])) for r in rungs]
    for fr in JSTAR_FRACS:
        cand = sorted(j for j in set().union(*all_jp)
                      if sum(j in s for s in all_jp)
                      >= fr * len(rungs))
        if len(cand) >= MIN_JSTAR:
            return cand, fr
    return [], None


def pair_spread(P):
    """Median pairwise chordal distance among unit-pair rows (the
    carrier's own contrast on the rung)."""
    n = len(P)
    if n < 2:
        return 0.0
    D = np.abs(P[:, None, 0] * P[None, :, 1]
               - P[:, None, 1] * P[None, :, 0])
    iu = np.triu_indices(n, 1)
    return float(np.median(D[iu]))


def measure_gauges(rungs, pairs, refs):
    """Per gauge: raw deviations + carrier spread + anchor step
    maps per pair."""
    frames = [gauge_frames(r, refs) for r in rungs]
    idx_of = {id(r): i for i, r in enumerate(rungs)}
    out = {g: {} for g in GAUGES}
    anchors = refs[:3]
    for si, p in enumerate(pairs):
        ra, rb = p["ra"], p["rb"]
        fa_all = frames[idx_of[id(ra)]]
        fb_all = frames[idx_of[id(rb)]]
        jpa = [int(j) for j in ra["jp"]]
        jpb = [int(j) for j in rb["jp"]]
        nref = np.array([int(j) not in refs[:2] for j in p["com"]])
        for g in GAUGES:
            if fa_all[g] is None or fb_all[g] is None:
                continue
            fa, ga = fa_all[g]
            fb, gb = fb_all[g]
            Pa = unit_pairs(ga[p["ia"]], fa[p["ia"]])
            Pb = unit_pairs(gb[p["ib"]], fb[p["ib"]])
            raw = float(np.median(chordal(Pa, Pb)))
            spr = pair_spread(Pa[nref]) if int(np.sum(nref)) >= 2 \
                else 0.0
            rec = dict(raw=raw, spr=spr, M=None, kap=float("nan"),
                       fa=fa, fb=fb)
            if all(j in jpa and j in jpb for j in anchors):
                PA = unit_pairs(ga, fa)
                PB = unit_pairs(gb, fb)
                qa = [PA[jpa.index(j)] for j in anchors]
                qb = [PB[jpb.index(j)] for j in anchors]
                seps = [chordal(x[None, :], y[None, :])[0]
                        for xy in (qa, qb)
                        for x, y in ((xy[0], xy[1]),
                                     (xy[0], xy[2]),
                                     (xy[1], xy[2]))]
                Ta = norm_map(*qa)
                Tb = norm_map(*qb)
                if (min(seps) > REF_SEP_MIN and Ta is not None
                        and Tb is not None):
                    M = np.linalg.inv(Tb) @ Ta
                    rec["M"] = M / max(float(np.linalg.norm(M)),
                                       1e-300)
                    rec["kap"] = kappa(M)
            out[g][si] = rec
    return out


def family_dp(As, Bs, S):
    """Median d_P(S A S^-1, B) over the two matched families;
    inf if S is singular."""
    ds = []
    for A, B in zip(As, Bs):
        AC = conj_apply(S, A)
        if AC is None:
            return float("inf")
        ds.append(proj_dist(AC, B))
    return float(np.median(ds)) if ds else float("inf")


def robust_conj_score(As, Bs):
    """Score the agreement of two step families up to ONE global
    conjugation: the better of S = Id and the joint least-squares
    Sylvester solve (SPEC v3 amendment viii).  Returns (best med,
    med at Id, med at joint S, s_min/s_max, n)."""
    if len(As) < 2:
        return (float("inf"), float("inf"), float("inf"),
                float("nan"), len(As))
    d_id = family_dp(As, Bs, np.eye(2))
    S, smin = conj_joint(As, Bs)
    d_jt = family_dp(As, Bs, S)
    return min(d_id, d_jt), d_id, d_jt, smin, len(As)


def cross_gauge(meas, ga, gb):
    """Cross-gauge step-family comparison up to ONE global
    conjugation (robust, v3)."""
    common = sorted(si for si in meas[ga]
                    if si in meas[gb]
                    and meas[ga][si]["M"] is not None
                    and meas[gb][si]["M"] is not None)
    As = [meas[ga][si]["M"] for si in common]
    Bs = [meas[gb][si]["M"] for si in common]
    return robust_conj_score(As, Bs)


def lambda_ladder(meas_g, pairs, refs):
    """G2: gauge-(i) scalar cocycle over the measured steps."""
    rows = []
    for si, p in enumerate(pairs):
        if si not in meas_g:
            continue
        rec = meas_g[si]
        fa, fb = rec["fa"], rec["fb"]
        com = p["com"]
        keep = np.array([int(j) not in refs[:2] for j in com])
        va = np.abs(fa[p["ia"]][keep])
        vb = np.abs(fb[p["ib"]][keep])
        m = va > 1e-300
        if int(np.sum(m)) < 3:
            continue
        lam = float(np.median(vb[m] / va[m]))
        if lam <= 0:
            continue
        rows.append(dict(si=si, ha=p["ra"]["h"], hb=p["rb"]["h"],
                         lam=lam, tau_b=p["rb"]["tau"]))
    cum = 0.0
    for r in rows:
        cum += math.log(r["lam"])
        r["cum"] = cum
    return rows


def jacobi_family(pairs, z):
    """G3: entering-level transfer products from the deeper rung's
    chain; equal-h steps carry the empty product."""
    fam = {}
    for si, p in enumerate(pairs):
        ha, hb = p["ra"]["h"], p["rb"]["h"]
        if hb < ha:
            continue
        al, be = p["rb"]["al"], p["rb"]["be"]
        if hb > ha and (len(al) < hb or len(be) < hb or ha < 1):
            continue
        J, lognorm = jacobi_product(al, be, ha, hb, z) \
            if hb > ha else (np.eye(2), 0.0)
        fam[si] = dict(J=J / max(float(np.linalg.norm(J)), 1e-300),
                       lognorm=lognorm, dh=hb - ha)
    return fam


def jacobi_score(fam, meas_g, tag):
    """Global-conjugation scoring of the Jacobi candidate against
    the gauge-(i) measured steps (robust, v3)."""
    common = sorted(si for si in fam
                    if si in meas_g and meas_g[si]["M"] is not None)
    if len(common) < 2:
        print("    [%s] JACOBI: < 2 comparable steps -> "
              "UNAVAILABLE" % tag)
        return None
    As = [fam[si]["J"] for si in common]
    Bs = [meas_g[si]["M"] for si in common]
    med, d_id, d_jt, smin, n = robust_conj_score(As, Bs)
    kj = [kappa(fam[si]["J"]) for si in common]
    km = [meas_g[si]["kap"] for si in common]
    n_dh0 = sum(1 for si in common if fam[si]["dh"] == 0)
    print("    [%s] JACOBI: %d steps (%d with dh=0); global "
          "conjugation candidates: d_P med %.4f at S=Id, %.4f at "
          "joint-LSQ S (stack s_min/s_max %.1e)"
          % (tag, n, n_dh0, d_id, d_jt, smin))
    print("    [%s] SCORED median d_P = %.4f (better candidate); "
          "median d_P(J, Id) = %.4f; kappa corr(J, M) = %.3f"
          % (tag, med,
             family_dp(As, [np.eye(2)] * len(As), np.eye(2)),
             pearson(kj, km)))
    return dict(med=med, common=common)


# ------------------------------------------------------------------ main
def main():
    section("PRIME.PORT.MOEBIUS.GAUGEFW.01 -- source-frozen gauge "
            "firewall + scalar cocycle + Jacobi transfer "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- build the truth ladder (all frame-A zones, "
            "h <= %d; machinery verbatim)" % H_DEEP_MAX)
    rungs, rk_max = build_ladder(tag="truth")
    check("W1 >= %d rungs built" % MIN_RUNGS,
          len(rungs) >= MIN_RUNGS, "%d rungs" % len(rungs),
          kill="K1")
    check("W2 rank-2 exact on every rung (max s3/s1 %.1e <= %.0e)"
          % (rk_max, RANK_BAR), rk_max <= RANK_BAR, kill="K1")
    jstar, used_frac = jstar_refs(rungs)
    check("W3 frozen reference set built (|J*| %d >= %d at "
          "presence >= %.2f)" % (len(jstar), MIN_JSTAR,
                                 used_frac or 0.0),
          len(jstar) >= MIN_JSTAR, kill="K1")
    if len(jstar) < MIN_JSTAR:
        return finish({})
    refs = jstar[:3]
    print("    J* = %s; reference pair (jr1, jr2) = (%d, %d); "
          "step anchors = %s" % (jstar, jstar[0], jstar[1], refs))
    pairs, n_skip_pairs = ladder_pairs(rungs)
    print("    %d consecutive pairs with >= %d common port nodes "
          "(%d typed skips)" % (len(pairs), MIN_COMMON_J,
                                n_skip_pairs))

    # ------------------------------------------------------------ G0
    section("G0 -- baseline: the per-rung-normalized machinery the "
            "reviewer challenged (verbatim; printed, not a claim)")
    fit_res, id_res = [], []
    for p in pairs:
        Pa = unit_pairs(p["ra"]["gS"][p["ia"]],
                        p["ra"]["fS"][p["ia"]])
        Pb = unit_pairs(p["rb"]["gS"][p["ib"]],
                        p["rb"]["fS"][p["ib"]])
        order = np.argsort(p["com"])
        i0, i1, i2 = order[0], order[1], order[2]
        seps = [chordal(Pa[[u]], Pa[[v]])[0]
                for u, v in ((i0, i1), (i0, i2), (i1, i2))] \
            + [chordal(Pb[[u]], Pb[[v]])[0]
               for u, v in ((i0, i1), (i0, i2), (i1, i2))]
        Ta = norm_map(Pa[i0], Pa[i1], Pa[i2])
        Tb = norm_map(Pb[i0], Pb[i1], Pb[i2])
        if min(seps) <= REF_SEP_MIN or Ta is None or Tb is None:
            continue
        Na, Nb = apply_hom(Ta, Pa), apply_hom(Tb, Pb)
        T, res = moebius_fit(Na, Nb)
        keep = np.ones(len(p["com"]), dtype=bool)
        keep[[i0, i1, i2]] = False
        fit_res.append(float(np.median(res[keep])))
        id_res.append(float(np.median(
            chordal(Na, Nb)[keep])))
    med_fit = float(np.median(fit_res)) if fit_res else float("inf")
    med_idn = float(np.median(id_res)) if id_res else float("inf")
    norm_invariant = med_idn <= RAW_INV_BAR
    print("    %d normalized steps; med fit res %.4f; med id-res "
          "(identity candidate) %.4f -> baseline %s"
          % (len(fit_res), med_fit, med_idn,
             "NORM-INVARIANT" if norm_invariant else "NORM-MOVING"))
    check("G0.1 baseline computed (%d steps)" % len(fit_res),
          len(fit_res) >= MIN_PAIRS, kill="K1")

    # ------------------------------------------------------------ G1
    section("G1 -- the three SOURCE-FROZEN gauges (raw chordal "
            "deviation, NO renormalization; anchor step maps)")
    st_dev = frame_selftest(rungs, refs)
    check("G1.0 FRAME SELF-TEST: all gauge frames satisfy their "
          "defining conditions (max dev W %.1e / A %.1e / D %.1e "
          "<= 1e-8)" % (st_dev["W"], st_dev["A"], st_dev["D"]),
          max(st_dev.values()) <= 1e-8, kill="K1")
    meas = measure_gauges(rungs, pairs, refs)
    print("    step          raw/spread (i)W    raw/spread (ii)A"
          "   raw/spread (iii)D    kap(W)     kap(A)     kap(D)")
    for si, p in enumerate(pairs):
        cols = []
        kaps = []
        for g in GAUGES:
            if si in meas[g]:
                cols.append("%.4f/%.4f" % (meas[g][si]["raw"],
                                           meas[g][si]["spr"]))
                kaps.append(("%+.3e" % meas[g][si]["kap"])
                            if meas[g][si]["M"] is not None
                            else "    -    ")
            else:
                cols.append("  -   /  -   ")
                kaps.append("    -    ")
        print("    h %3d->%3d   %s      %s      %s   %s %s %s"
              % (p["ra"]["h"], p["rb"]["h"], cols[0], cols[1],
                 cols[2], kaps[0], kaps[1], kaps[2]))
    raw_label = {}
    for g in GAUGES:
        rv = [meas[g][si]["raw"] for si in meas[g]]
        sv = [meas[g][si]["spr"] for si in meas[g]]
        med = float(np.median(rv)) if rv else float("inf")
        med_s = float(np.median(sv)) if sv else 0.0
        if med_s < RAW_INV_BAR:
            raw_label[g] = "RAW-DEGENERATE"
        elif med <= RAW_INV_BAR:
            raw_label[g] = "RAW-INVARIANT"
        else:
            raw_label[g] = "RAW-MOVING"
        nM = sum(1 for si in meas[g]
                 if meas[g][si]["M"] is not None)
        d_id = [proj_dist(meas[g][si]["M"], np.eye(2))
                for si in meas[g]
                if meas[g][si]["M"] is not None]
        print("    %-16s: %d steps (%d anchor maps), raw dev %s | "
              "med spread %.4f (rel motion %s) | med d_P(M, Id) "
              "%.4f -> %s"
              % (GAUGE_NAMES[g], len(rv), nM,
                 quart(rv) if rv else "none", med_s,
                 "%.2f" % (med / med_s) if med_s > 0 else "n/a",
                 float(np.median(d_id)) if d_id else float("nan"),
                 raw_label[g]))
    nW = sum(1 for si in meas["W"]
             if meas["W"][si]["M"] is not None)
    check("G1.1 >= %d gauge-(i) steps with anchor maps" % MIN_PAIRS,
          nW >= MIN_PAIRS, "%d steps" % nW, kill="K1")
    print("\n    CROSS-GAUGE (ONE global conjugation, robust v3: "
          "better of S=Id and joint-LSQ S):")
    cross = {}
    for ga, gb in (("W", "A"), ("W", "D"), ("A", "D")):
        med, d_id, d_jt, smin, n = cross_gauge(meas, ga, gb)
        cross[(ga, gb)] = med
        print("    %s vs %s : SCORED med d_P %.4f over %d steps "
              "(S=Id %.4f | joint-LSQ %.4f, stack s_min/s_max "
              "%.1e)" % (ga, gb, med, n, d_id, d_jt, smin))
    all_pairs_ok = all(v <= DP_ROBUST_BAR for v in cross.values())
    any_pair_part = all(v <= DP_PART_BAR for v in cross.values())
    nondeg = [g for g in GAUGES
              if raw_label[g] != "RAW-DEGENERATE"]
    labels_agree = len(set(raw_label[g] for g in nondeg)) <= 1
    if all_pairs_ok and labels_agree:
        g1_label = "GAUGE-ROBUST"
    elif (norm_invariant
          and not any(raw_label[g] == "RAW-INVARIANT"
                      for g in GAUGES)
          and not any_pair_part):
        g1_label = "GAUGE-MADE"
    else:
        g1_label = "GAUGE-PARTIAL"
    sub = ",".join("%s:%s" % (g, raw_label[g][4:]) for g in GAUGES)
    print("    TYPED: cross-gauge medians %s vs bars %.2f/%.2f; "
          "raw labels {%s}; baseline %s -> %s"
          % (["%.4f" % cross[k] for k in cross],
             DP_ROBUST_BAR, DP_PART_BAR, sub,
             "NORM-INVARIANT" if norm_invariant else "NORM-MOVING",
             g1_label))
    check("G1.2 typed: %s (%s)" % (g1_label, sub), True)

    # ------------------------------------------------------------ G2
    section("G2 -- the scalar cocycle lambda_h (gauge (i) frozen) "
            "vs the tau ladder")
    rows = lambda_ladder(meas["W"], pairs, refs)
    print("    step          lambda_h   cum log lambda   tau_b"
          "        log tau_b")
    for r in rows:
        lt = math.log(r["tau_b"]) if r["tau_b"] > 0 else float("nan")
        print("    h %3d->%3d   %9.4f   %+12.4f    %+.3e   %s"
              % (r["ha"], r["hb"], r["lam"], r["cum"], r["tau_b"],
                 "%+9.4f" % lt if lt == lt else "   n/a  "))
    ok_rows = [r for r in rows if r["tau_b"] > 0]
    cum_v = [r["cum"] for r in ok_rows]
    ltau_v = [math.log(r["tau_b"]) for r in ok_rows]
    corr = pearson(cum_v, ltau_v)
    slope = (float(np.polyfit(ltau_v, cum_v, 1)[0])
             if len(ok_rows) >= 3 else float("nan"))
    g2_label = ("LAMBDA-IS-WALL" if abs(corr) >= LAM_WALL_CORR
                else "LAMBDA-PARTIAL" if abs(corr) >= LAM_PART_CORR
                else "LAMBDA-FLAT") if corr == corr else \
        "LAMBDA-FLAT"
    check("G2.1 lambda ladder measured (%d steps, %d with tau > 0)"
          % (len(rows), len(ok_rows)), len(ok_rows) >= 3,
          kill="K1")
    print("    corr(cumsum log lambda, log tau) = %.4f; OLS slope "
          "d(cum log lambda)/d(log tau) = %.4f" % (corr, slope))
    print("    TYPED: |corr| %.4f vs bars %.2f / %.2f -> %s"
          % (abs(corr) if corr == corr else float("nan"),
             LAM_WALL_CORR, LAM_PART_CORR, g2_label))
    for g in ("A", "D"):
        rg = lambda_ladder(meas[g], pairs, refs)
        og = [r for r in rg if r["tau_b"] > 0]
        cg = pearson([r["cum"] for r in og],
                     [math.log(r["tau_b"]) for r in og])
        print("    (unscored) gauge %s: corr = %s over %d steps"
              % (g, "%.4f" % cg if cg == cg else "n/a", len(og)))
    s1r = [(math.log(r["s1"]), math.log(r["tau"]))
           for r in rungs if "s1" in r and r["tau"] > 0]
    print("    (unscored, v3 x) extraction-scale ladder: corr(log "
          "s1, log tau) = %s over %d rungs"
          % ("%.4f" % pearson([a for a, _ in s1r],
                              [b for _, b in s1r])
             if len(s1r) >= 3 else "n/a", len(s1r)))
    check("G2.2 typed: %s" % g2_label, True)

    # ------------------------------------------------------------ G3
    section("G3 -- Jacobi transfer identification at z_ref = %.1f "
            "(cd_pick chain convention frozen)" % Z_REF)
    fam = jacobi_family(pairs, Z_REF)
    print("    step          dh   log|prod|   kap(J)      "
          "kap(M gauge i)")
    for si in sorted(fam):
        if si not in meas["W"] or meas["W"][si]["M"] is None:
            continue
        print("    h %3d->%3d  %4d   %+8.3f   %+.3e   %+.3e"
              % (pairs[si]["ra"]["h"], pairs[si]["rb"]["h"],
                 fam[si]["dh"], fam[si]["lognorm"],
                 kappa(fam[si]["J"]), meas["W"][si]["kap"]))
    jsc = jacobi_score(fam, meas["W"], "truth")
    if jsc is None:
        g3_label = "JACOBI-UNAVAILABLE"
    else:
        g3_label = ("JACOBI-DERIVED" if jsc["med"] <= JAC_DER_BAR
                    else "JACOBI-PARTIAL"
                    if jsc["med"] <= JAC_PART_BAR
                    else "JACOBI-DEAD")
    # G2/G3 bridge: does the scalar cocycle track the transfer
    # growth? (unscored diagnostic)
    lam_of = {r["si"]: math.log(r["lam"]) for r in rows}
    xs_b, ys_b = [], []
    for si in fam:
        if fam[si]["dh"] > 0 and si in lam_of:
            xs_b.append(lam_of[si])
            ys_b.append(fam[si]["lognorm"])
    print("    (unscored bridge) corr(log lambda_h, log transfer "
          "growth) = %s over %d steps"
          % ("%.4f" % pearson(xs_b, ys_b)
             if len(xs_b) >= 3 else "n/a", len(xs_b)))
    print("    TYPED: %s (med d_P %s vs bars %.2f / %.2f)"
          % (g3_label,
             "%.4f" % jsc["med"] if jsc else "n/a",
             JAC_DER_BAR, JAC_PART_BAR))
    check("G3.1 typed: %s" % g3_label, True)

    # ------------------------------------------------------------ SM
    section("SM -- the SMOOTH-MASS world (mask actual, mass smooth;"
            " frame-surviving control, same frozen gauges)")
    sm_rungs, _sm_rk = build_ladder(
        comb_of=lambda uu, alpha: (uu, cells_of(uu, alpha)[1]),
        tag="smooth")
    sm_stats = dict(g1=None, g2=None, g3=None, alive=None)
    if sm_rungs:
        alive = [r for r in sm_rungs if r["lamE"] < 1.0]
        sm_stats["alive"] = (len(alive), len(sm_rungs))
        sm_frame_dead = len(alive) == 0
        print("    frame survival census: lam(E) < 1 on %d / %d "
              "smooth rungs (min tau %+.3e, max %+.3e)%s"
              % (len(alive), len(sm_rungs),
                 min(r["tau"] for r in sm_rungs),
                 max(r["tau"] for r in sm_rungs),
                 "  -> typed SMOOTH-FRAME-DEAD (v3 ix): the "
                 "smooth-mass world is NOT frame-surviving here; "
                 "its measurements below carry that caveat"
                 if sm_frame_dead else ""))
        sm_pairs, sm_skip = ladder_pairs(sm_rungs)
        print("    %d smooth pairs (%d typed skips)"
              % (len(sm_pairs), sm_skip))
        if len(sm_pairs) >= MIN_SMOOTH_STEPS:
            sm_meas = measure_gauges(sm_rungs, sm_pairs, refs)
            for g in GAUGES:
                rv = [sm_meas[g][si]["raw"] for si in sm_meas[g]]
                sv = [sm_meas[g][si]["spr"] for si in sm_meas[g]]
                print("    smooth %-16s: %d steps, raw dev %s | "
                      "med spread %.4f"
                      % (GAUGE_NAMES[g], len(rv),
                         quart(rv) if rv else "none",
                         float(np.median(sv)) if sv else 0.0))
            rvW = [sm_meas["W"][si]["raw"] for si in sm_meas["W"]]
            sm_stats["g1"] = (float(np.median(rvW))
                              if rvW else float("inf"))
            sm_rows = lambda_ladder(sm_meas["W"], sm_pairs, refs)
            sm_ok = [r for r in sm_rows if r["tau_b"] != 0]
            sm_corr = pearson([r["cum"] for r in sm_ok],
                              [math.log(abs(r["tau_b"]))
                               for r in sm_ok])
            sm_stats["g2"] = sm_corr
            print("    smooth G2: corr(cum log lambda, log|tau|) "
                  "= %s over %d steps (tau < 0 throughout when "
                  "frame dead, disclosed)"
                  % ("%.4f" % sm_corr if sm_corr == sm_corr
                     else "n/a", len(sm_ok)))
            sm_fam = jacobi_family(sm_pairs, Z_REF)
            sm_jsc = jacobi_score(sm_fam, sm_meas["W"], "smooth")
            if sm_jsc is not None:
                sm_stats["g3"] = sm_jsc["med"]
        else:
            print("    typed: SMOOTH-UNAVAILABLE (%d < %d steps)"
                  % (len(sm_pairs), MIN_SMOOTH_STEPS))
    else:
        print("    typed: SMOOTH-UNAVAILABLE (no rungs)")
    caveat = ""
    if g3_label == "JACOBI-DERIVED":
        if sm_stats["g3"] is not None \
                and sm_stats["g3"] <= JAC_DER_BAR:
            caveat = "+UNIVERSAL-KINEMATICS"
            print("    HONEST CAVEAT: the identification holds on "
                  "the SMOOTH-MASS world too -> generic OPRL "
                  "kinematics; the arithmetic sits in the scalar "
                  "cocycle / the measure itself.")
        elif sm_stats["g3"] is not None:
            print("    caveat test: smooth med d_P %.4f > %.2f -> "
                  "the identification is NOT generic OPRL "
                  "kinematics on this evidence."
                  % (sm_stats["g3"], JAC_DER_BAR))
        else:
            print("    caveat test: smooth world unavailable -- "
                  "generic-kinematics question left open (typed).")
    check("SM.1 smooth-mass control measured (alive %s, G1 med %s,"
          " G2 corr %s, G3 med %s)"
          % (sm_stats["alive"],
             "%.4f" % sm_stats["g1"]
             if sm_stats["g1"] is not None else "n/a",
             "%.4f" % sm_stats["g2"]
             if sm_stats["g2"] == sm_stats["g2"]
             and sm_stats["g2"] is not None else "n/a",
             "%.4f" % sm_stats["g3"]
             if sm_stats["g3"] is not None else "n/a"), True)

    # ------------------------------------------------------------ C
    section("C -- controls (kz %d, must fire; frame channels "
            "reported)" % CTRL_KZ)
    ok = True
    for nmc, kw in (("Epstein", dict(comb=eps_comb(CTRL_KZ))),
                    ("scramble", dict(scramble_seed=1))):
        rc = rung_all(CTRL_KZ, **kw)
        if not isinstance(rc, dict):
            print("    %-8s: rung not built (%r) -> fires via "
                  "FRAME" % (nmc, rc))
            continue
        frame_dead = ("lamC" not in rc or rc["lamO"] > 1.0
                      or rc["lamC"] > 1.0)
        if frame_dead:
            why = ("window unavailable" if "lamC" not in rc else
                   "lam(out) %.3e" % rc["lamO"]
                   if rc["lamO"] > 1.0 else
                   "lam(C_J) %.3e" % rc["lamC"])
            print("    %-8s: fires via FRAME (%s)" % (nmc, why))
            continue
        if "fS" not in rc:
            print("    %-8s: frame alive but extraction "
                  "unavailable -> fires via FRAME" % nmc)
            continue
        print("    %-8s: frame ALIVE and extraction available -> "
              "SILENT" % nmc)
        ok = False
    check("C1 CONTROLS FIRE (frame death on both controls; the "
          "smooth-mass world is the frame-surviving control)",
          ok, kill="K3")

    return finish(dict(g1=g1_label, sub=sub, g2=g2_label,
                       corr=corr, slope=slope, g3=g3_label,
                       caveat=caveat, cross=cross,
                       med_fit=med_fit, med_idn=med_idn,
                       jmed=(jsc["med"] if jsc else float("inf")),
                       sm=sm_stats))


def finish(st):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K3": "CONTROL-DEAD"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("GAUGEFW-MEASURED / %s (%s) / %s / %s%s"
                   % (st["g1"], st["sub"], st["g2"], st["g3"],
                      st["caveat"]))
        print("\n  VERDICT: %s" % VERDICT)
        print("  (baseline med id-res %.4f; cross-gauge d_P %s; "
              "lambda-tau corr %.4f slope %.4f; jacobi med d_P "
              "%s; smooth: %r)"
              % (st["med_idn"],
                 ["%.4f" % st["cross"][k] for k in st["cross"]],
                 st["corr"], st["slope"],
                 "%.4f" % st["jmed"]
                 if st["jmed"] < float("inf") else "n/a",
                 st["sm"]))
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# ------------- frozen probe source mobius_control_census_probe (embedded BYTE-EXACT, raw string)
_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""mobius_control_census_probe -- PRIME.PORT.MOEBIUS.CENSUS.01
(EXPLORATION ONLY, experiments/; round 48, reviewer probe 4: run
the IDENTICAL Moebius-analysis pipeline on SIX worlds and report
the full discriminator table with NO post-hoc selection -- this
decides whether the Moebius structure is arithmetic dynamics,
universal geometry, or artifact, 2026-08-09).

THE QUESTION (frozen): port_schur_cocycle_probe measured a clean
per-rung Moebius step on the PSL(2,R)-normalized port carrier
m = g/f (median residual 0.0015, |alpha| < 1 on 100%), and
moebius_source_step_probe typed it CARRIER-INVARIANT.  But the
only controls run so far (Epstein, scramble at kz 9) die at the
FRAME, so nothing yet separates "arithmetic dynamics" from
"rank-2 kinematics that any window of this geometry produces".
The smooth worlds of lattice_parametrix_probe (B1) and
edge_bulk_smoothing_probe (Z1/Z2) keep the WINDOW GEOMETRY
intact (same positions, smoothed masses), so their frames should
survive where Epstein/scramble frame-die -- verify -- and they
are the honest controls for the census.

THE SIX WORLDS (frozen; identical pipeline, full ladder each):
  W1  TRUTH:      masses 2 Lambda(n)/sqrt(n) at u_n = log n;
  W2  EPSTEIN:    lambda_eps recursion comb of x^2 + 5 y^2
                  (per-rung N_E = floor(exp(2 alpha)) + 1);
  W3  SCRAMBLE:   positions ~ U(0, 2 alpha), seed 1 (the only
                  RNG in the probe), true masses;
  W4  LATTICE-SMOOTH (B1): true positions, fully smooth
                  quadrature masses 2 e^{u/2} du (lattice_
                  parametrix verbatim) -- no Lambda information;
  W5  EDGE-SMOOTHED (Z1): B2-style local-average masses on the
                  edge zone u > U - 1 only, interior exact
                  (edge_bulk_smoothing verbatim);
  W6  INTERIOR-SMOOTHED (Z2): local-average masses on u <= U - 1
                  only, edge exact (edge_bulk_smoothing
                  verbatim).

THE LADDER (frozen, port_schur_cocycle verbatim): all frame-A
zones (core.frame_a_zones()) with h <= 900, sorted by (h, kz);
consecutive rung pairs with >= 8 common port alias indices.

FROZEN PROTOCOL (2026-08-09; all bars frozen before the run; the
NO-POST-HOC-SELECTION RULE: every world runs the identical
pipeline end to end, every discriminator is computed wherever it
mechanically runs, and every number is printed -- no world, rung,
step, or discriminator is dropped after seeing results):

 P   THE PIPELINE PER WORLD (identical, port_schur_cocycle /
     moebius_source_step verbatim): build the windows (heavy
     build: tent assembly, folded measures, Lanczos chain, Gram
     E), the 12-index window compression C_J (J = {2,...,24}),
     the dressed port D_P and the gauge-fixed IIKS generators
     (f, g) on the port-decile nodes.  A rung's carrier is VALID
     iff the commutator [Y, D_P] is numerically rank 2
     (s3/s1 <= 1e-6, identical bar for all worlds; the truth
     ladder is additionally warded at the predecessor's 1e-10,
     K1).  Per consecutive valid pair with >= 8 common alias
     indices, five discriminators:
     (a) CR   fit-free cross-ratio defect: from the common nodes
         (sorted by alias index) take K = min(n, 12) evenly
         spaced nodes; battery = all C(K, 4) quadruples whose
         six pairwise chordal separations are >= 1e-3 in BOTH
         rungs (well-conditioned); per quadruple the homogeneous
         cross-ratio cr = ([p0 p2][p1 p3] : [p0 p3][p1 p2]) as a
         unit pair, defect = chordal(cr_a, cr_b); per-step value
         = median over the battery (typed skip if < 5
         quadruples).  Fit-free: Moebius maps preserve cr
         exactly.  (The battery rule is frozen HERE; the
         parallel crossratio probe was not in the tree at freeze
         time -- amendment (ii).)
     (b) STEP the three-anchor step map: anchors = the three
         deepest common nodes (smallest alias j, predecessor
         verbatim; degenerate anchors = typed skip); S =
         T_b^{-1} T_a with T the (0, 1, inf) normalizers;
         per-step value = median chordal(S p_a, p_b) on the
         NON-anchor common nodes; |alpha| = the Cayley datum of
         the det-normalized S_n = S / sqrt(|det S|) (frozen
         convention).
     (c) JRES J-contractivity residual: min eig(J - S_n^* J S_n)
         with J = [[0, -i], [i, 0]] (upper-half-plane signature)
         on the det-normalized S_n; for real 2x2 this equals
         -(1 - sign det S) sized, i.e. 0 for orientation-
         preserving steps and -2 for orientation-reversing ones
         -- the census is the orientation/contractivity
         coherence of the ladder.
     (d) RAW  raw identity distance: median chordal(p_a, p_b)
         over ALL common nodes, gauge-fixed but UNNORMALIZED (no
         PSL(2,R) three-point normalization).
     (e) TAU  tau-factor sign census: per rung with an available
         window (>= 8 of the 12 alias indices), the sign of
         det(I - C_J) via slogdet; the world's census = the
         number of sign flips along the ladder.
     WORLD VALUES: ladder medians of (a), (b), (d); ladder MIN
     of (c) plus the det > 0 fraction; flip count for (e).

 F   FRAME-SURVIVAL CENSUS (part of the deliverable): per world
     report #rungs built (Lanczos completes), #carrier-valid
     (rank-2 bar), #window-available (>= 8 alias indices),
     #window-ALIVE (available AND lam(I-E_out) subcritical
     lam(out) < 1 AND lam(C_J) < 1), #full 12-window, #measured
     steps.  FROZEN FRAME-ALIVE RULE: a world is FRAME-ALIVE iff
     #built >= 10 AND #window-alive >= 0.5 x #built AND
     #carrier-valid >= 10.  FROZEN FALLBACK: if any FRAME-ALIVE
     world has < 5 window-available rungs, discriminator (e) is
     additionally computed on the largest common window = the
     port-decile alias indices present on >= 0.80 of the rungs
     of EVERY frame-alive world (12 smallest; needs >= 4), via
     the stored Lanczos chains; the fallback census then stands
     in for (e) wherever the primary is N/A.

 T   TYPED READING (frozen decision rules, no cherry-picking).
     PASS bars per discriminator and world: (a) median <= 0.05;
     (b) median <= 0.05; (c) ladder min >= -1e-8 (all steps
     orientation-preserving J-isometries); (d) median <= 0.05;
     (e) >= 5 windowed rungs and 0 sign flips.  A discriminator
     with < 10 measured steps (or < 5 windowed rungs for (e)) in
     a world is N/A there; N/A counts as FAIL in the typing of a
     frame-alive world (typed, reported).  Per discriminator D:
       D-ARITHMETIC iff truth passes AND >= 1 control is
         frame-alive AND ALL frame-alive controls fail;
       D-GEOMETRIC  iff truth passes AND >= 2 frame-alive
         controls pass;
       D-UNDECIDED  otherwise (including truth-fails and the
         no-frame-alive-controls case: frame-only separation).
     Frame-DEAD controls' discriminator values are printed
     (no post-hoc selection) but do not enter the typing.
     The reviewer's expectation under test: the Moebius/cr
     structure itself types GEOMETRIC (rank-2 kinematics), while
     the arithmetic separation lives in (c), in (e), or in
     neither -- then the census says the route needs the
     scalar-cocycle/determinant bridge instead (the parallel
     tau_mobius_factor probe's territory).

KILLS: K1 truth-pipeline ward breaks (>= 30 truth rungs, truth
rank ward 1e-10, >= 30 truth steps, truth frame-alive, Epstein
sieve ward) -> PIPELINE-BROKEN.  Frame death of any CONTROL
world is a reported census outcome, not a kill.

VERDICT (frozen enum): MOEBIUSCENSUS-MEASURED with the
per-discriminator typing a:/b:/c:/d:/e: each in {ARITHMETIC,
GEOMETRIC, UNDECIDED(...)}; else PIPELINE-BROKEN.

SPEC v2 AMENDMENTS (documented before the run; fail-first
preserved): (i) the Epstein recursion is sieve-accelerated
(vectorized r-count + forward-push divisor sieve), warded in-run
against the verbatim O(N^2) recursion at N = 2000 (max dev
<= 1e-9, K1); (ii) the quadruple-battery rule for (a) is frozen
in this docstring (the parallel crossratio probe was absent from
the tree at freeze time); (iii) the carrier-validity bar is
1e-6 identically for all six worlds; the predecessor's 1e-10 is
kept as the TRUTH ward only (a control failing rank-2 is a
frame-death channel, not a kill); (iv) each rung stores its
Lanczos chain and negative-arm data so the frozen fallback
window can be recompressed without a second heavy pass --
bookkeeping only, physics verbatim; (v) the frame-alive rule is
quantified as printed above (the predecessors' single-rung
controls never needed a ladder-level rule); (vi) after run 1
(which measured win-ALIVE = 0 on all five controls) the frame
table gained the median lam(out) / lam(C_J) columns, the
fire-channel counts, and the explicit availability-vs-
subcriticality note for the fallback clause, and the verdict
block gained the computed frame-dead context lines -- REPORTING
ONLY: no bar, rule, or pipeline change; fail-first preserved.

NO RH claim -- a six-world discriminator census on compressed
truncations is a numerical measurement, not a theorem about
zeros.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared
scramble world (seed 1); stdout only.  No marker moves.

Sources (read-only): v563_paper2_readouts; carrier pipeline
verbatim from port_schur_cocycle_probe.py (PRIME.PORT.
SCHURSTEP.01) / moebius_source_step_probe.py (PRIME.PORT.
MOEBIUS.SOURCE.01); smooth worlds verbatim from
lattice_parametrix_probe.py (PRIME.PORT.LATTICE.PARAMETRIX.01,
B1) and edge_bulk_smoothing_probe.py (PRIME.PORT.LATTICE.
PARAMETRIX.02, Z1/Z2).  IIKS = Its-Izergin-Korepin-Slavnov.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/mobius_control_census_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from itertools import combinations

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

H_DEEP_MAX = 900
JWIN = tuple(range(2, 25, 2))
MIN_COMMON_J = 8
REF_SEP_MIN = 1e-6
CARRIER_RK_BAR = 1e-6       # identical validity bar, all worlds (iii)
TRUTH_RK_BAR = 1e-10        # predecessor ward, truth only (K1)
MIN_RUNGS_TRUTH = 30
MIN_STEPS_TRUTH = 30

# frame-alive rule (v)
MIN_BUILT_ALIVE = 10
WIN_ALIVE_FRAC = 0.5
MIN_CARRIER_ALIVE = 10

# discriminator bars (frozen)
CR_MAX_NODES = 12
CR_SEP_MIN = 1e-3
CR_MIN_QUADS = 5
BAR_A = 0.05
BAR_B = 0.05
BAR_C = -1e-8
BAR_D = 0.05
MIN_STEPS_WORLD = 10
MIN_WIN_RUNGS_E = 5

# fallback window (F)
FB_PRESENCE_FRAC = 0.80
FB_MAX_NODES = 12
FB_MIN_NODES = 4

EPS_WARD_N = 2000
EPS_WARD_BAR = 1e-9
SCRAMBLE_SEED = 1

WORLDS = ("W1", "W2", "W3", "W4", "W5", "W6")
WNAME = {"W1": "truth", "W2": "epstein", "W3": "scramble",
         "W4": "lattice-smooth", "W5": "edge-smoothed",
         "W6": "interior-smoothed"}
CONTROLS = ("W2", "W3", "W4", "W5", "W6")

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


# --------- pipeline, verbatim from port_schur_cocycle_probe
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def lambda_eps_slow(N):
    """The predecessors' verbatim O(N^2) Epstein recursion (ward
    reference only, amendment (i))."""
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


def lambda_eps(N):
    """Sieve-accelerated Epstein recursion: vectorized r-count +
    forward-push divisor sieve; warded against lambda_eps_slow at
    N = 2000 (amendment (i))."""
    s = int(math.isqrt(N)) + 1
    g = np.arange(-s, s + 1)
    v = (g[:, None] ** 2 + 5 * g[None, :] ** 2).ravel()
    v = v[(v >= 1) & (v <= N)]
    a = np.bincount(v, minlength=N + 1).astype(float) / 2.0
    lam = np.zeros(N + 1)
    nn = np.arange(N + 1, dtype=float)
    nn[0] = 1.0
    acc = a * np.log(nn)
    for n in range(2, N + 1):
        lam[n] = acc[n]
        if lam[n] != 0.0 and 2 * n <= N:
            acc[2 * n::n] -= lam[n] * a[2:(N // n) + 1]
    return lam


_EPS_CACHE = {}


def eps_comb(alpha):
    N_E = int(math.floor(math.exp(2.0 * alpha))) + 1
    if N_E not in _EPS_CACHE:
        lamE_ = lambda_eps(N_E)
        nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
        _EPS_CACHE[N_E] = (np.log(nn.astype(float)),
                           2.0 * lamE_[nn] / np.sqrt(
                               nn.astype(float)))
    return _EPS_CACHE[N_E]


# --------- smooth-world mass constructions, verbatim
def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


def smoothed_masses(uu, mm, zone_mask):
    """B2-style local-average masses inside the zone, exact outside
    (edge_bulk_smoothing verbatim)."""
    du = cell_widths(uu)
    m_shape = 2.0 * np.exp(uu / 2.0) * du
    out = mm.copy()
    for i in np.where(zone_mask)[0]:
        w = (np.abs(uu - uu[i]) <= 0.5) & zone_mask
        s_true = float(np.sum(mm[w]))
        s_shape = float(np.sum(m_shape[w]))
        out[i] = m_shape[i] * (s_true / s_shape
                               if s_shape > 0 else 1.0)
    return out


def world_source(world, rr):
    """The (positions, masses) of a world on one rung.  W1/W4/W5/W6
    share the true positions; W2 replaces the comb; W3 scrambles
    positions upstream (build_window seed)."""
    uu = np.asarray(rr["uu"], float)
    mm = 2.0 * np.asarray(rr["lam"], float)
    if world in ("W1", "W3"):
        return uu, mm
    if world == "W2":
        return eps_comb(float(rr["alpha"]))
    if world == "W4":
        return uu, 2.0 * np.exp(uu / 2.0) * cell_widths(uu)
    edge = uu > float(np.max(uu)) - 1.0
    if world == "W5":
        return uu, smoothed_masses(uu, mm, edge)
    return uu, smoothed_masses(uu, mm, ~edge)          # W6


def folded_measure(d_arm, L, sign=+1.0):
    jj = np.arange(L)
    keep = (sign * d_arm) > 0.0
    jj = jj[keep]
    th = 2.0 * math.pi * jj / L
    wt = (np.abs(d_arm[keep]) / (2.0 * L)) * 4.0 * np.sin(
        th / 2.0) ** 2
    fold = np.minimum(jj, L - jj)
    uf, inv = np.unique(fold, return_inverse=True)
    wagg = np.zeros(len(uf))
    np.add.at(wagg, inv, wt)
    xs = np.cos(2.0 * math.pi * uf / L)
    m = wagg > 1e-300
    return xs[m], wagg[m], uf[m]


def lanczos_chain(x, w, n):
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
        if bnorm <= 1e-14:
            steps = k + 1
            break
        be[k] = bnorm
        Q[:, k + 1] = z / bnorm
    return al[:steps], be[:max(steps - 1, 0)], m0, steps


def eval_chain(al, be, m0, y, n):
    P = np.zeros((len(y), n))
    P[:, 0] = 1.0 / math.sqrt(m0)
    if n > 1:
        P[:, 1] = (y - al[0]) * P[:, 0] / be[0]
    for k in range(1, n - 1):
        P[:, k + 1] = ((y - al[k]) * P[:, k]
                       - be[k - 1] * P[:, k - 1]) / be[k]
    return P


def antisym_generators(C):
    """Canonical (f, g) with C = f g^T - g f^T (SPEC v2 extraction,
    verbatim)."""
    U, sv, _Vh = np.linalg.svd(C)
    s1 = sv[0]
    f = math.sqrt(s1) * U[:, 0]
    g = math.sqrt(s1) * U[:, 1]
    Ct = np.outer(f, g) - np.outer(g, f)
    if np.linalg.norm(Ct + C) < np.linalg.norm(Ct - C):
        g = -g
    return f, g, sv


def gauge_fix(f, g, jp):
    """FROZEN GAUGE (lax2 verbatim)."""
    m0 = int(np.argmin(jp))
    r = math.hypot(f[m0], g[m0])
    c, s = f[m0] / r, g[m0] / r
    return c * f + s * g, -s * f + c * g


def rung_all(kz, world):
    """One heavy build per (rung, world): identical pipeline; the
    world enters ONLY through the source comb (P).  Chain data is
    stored for the frozen fallback recompression (amendment iv)."""
    rr = core.build_window(
        kz, scramble_seed=(SCRAMBLE_SEED if world == "W3"
                           else None))
    h, M, D, alpha = rr["h"], rr["M"], rr["D"], rr["alpha"]
    if h > H_DEEP_MAX:
        return "TOO-DEEP"
    uu, mm = world_source(world, rr)
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    d = grid_density(c_ar + c_at)
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    if len(xs) < 4 or len(ys) < 4:
        return None
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    E = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    E = 0.5 * (E + E.T)
    out = dict(kz=kz, h=h, al=al, be=be, m0=m0, ys=ys, vs=vs,
               uf_n=uf_n)
    # ---- window compression (port_cocycle_window verbatim)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    jav = [j for j in JWIN if j in idx]
    out["full"] = (len(jav) == len(JWIN))
    if len(jav) >= MIN_COMMON_J:
        iw = [idx[j] for j in jav]
        io = [k for k in range(E.shape[0]) if k not in set(iw)]
        Eo = E[np.ix_(io, io)]
        IO = np.eye(len(io)) - Eo
        CJ = (E[np.ix_(iw, iw)]
              + E[np.ix_(iw, io)] @ np.linalg.solve(
                  IO, E[np.ix_(io, iw)]))
        CJ = 0.5 * (CJ + CJ.T)
        out["lamO"] = float(np.linalg.eigvalsh(Eo)[-1])
        out["lamC"] = float(np.linalg.eigvalsh(CJ)[-1])
        sgn, ld = np.linalg.slogdet(np.eye(len(jav)) - CJ)
        out["detsgn"], out["detld"] = float(sgn), float(ld)
    # ---- dressed port + IIKS generators (verbatim)
    tau_m = (2.0 * math.pi * uf_n / L) / D
    port = tau_m <= float(np.max(tau_m)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) >= 4 and len(ib) >= 1:
        P = E[np.ix_(ip, ip)]
        X = E[np.ix_(ip, ib)]
        R = E[np.ix_(ib, ib)]
        IR = np.eye(len(ib)) - R
        DP = P + X @ np.linalg.solve(IR, X.T)
        DP = 0.5 * (DP + DP.T)
        Y = np.diag(ys[ip])
        C = Y @ DP - DP @ Y
        f, g, sv = antisym_generators(C)
        f, g = gauge_fix(f, g, uf_n[ip])
        out["f"], out["g"] = f, g
        out["jp"] = uf_n[ip]
        out["rk"] = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return out


def rebuild_E(r):
    """Recompute the Gram E of a stored rung from its Lanczos chain
    (fallback pass only; amendment iv)."""
    Pn = eval_chain(r["al"], r["be"], r["m0"], r["ys"], r["h"])
    E = (np.sqrt(r["vs"])[:, None] * (Pn @ Pn.T)
         * np.sqrt(r["vs"])[None, :])
    return 0.5 * (E + E.T)


# ------------------------------------------- homogeneous RP^1 machinery
def unit_pairs(g, f):
    P = np.stack([np.asarray(g, float), np.asarray(f, float)],
                 axis=1)
    return P / np.linalg.norm(P, axis=1)[:, None]


def chordal(P, Q):
    """Chordal distance on RP^1 between unit pair rows."""
    return np.abs(P[:, 0] * Q[:, 1] - P[:, 1] * Q[:, 0])


def norm_map(p0, p1, p2):
    """The unique PSL(2, R) map sending p0 -> 0, p1 -> 1,
    p2 -> infinity (verbatim); None if degenerate."""
    M = np.stack([p2, p0], axis=1)
    if abs(float(np.linalg.det(M))) < 1e-12:
        return None
    T0 = np.linalg.inv(M)
    s, t = T0 @ p1
    if abs(s) < 1e-10 or abs(t) < 1e-10:
        return None
    return np.diag([1.0 / s, 1.0 / t]) @ T0


def apply_hom(T, P):
    Q = (T @ P.T).T
    n = np.linalg.norm(Q, axis=1)
    n[n < 1e-300] = 1.0
    return Q / n[:, None]


def cayley_alpha(T):
    den = T[1, 0] * 1j + T[1, 1]
    if abs(den) < 1e-300:
        return float("inf")
    z = (T[0, 0] * 1j + T[0, 1]) / den
    return abs((z - 1j) / (z + 1j))


J_SIG = np.array([[0.0, -1.0j], [1.0j, 0.0]])


def j_residual(Sn):
    """min eig(J - Sn^* J Sn), upper-half-plane signature."""
    R = J_SIG - Sn.conj().T @ J_SIG @ Sn
    R = 0.5 * (R + R.conj().T)
    return float(np.linalg.eigvalsh(R)[0])


def br(p, q):
    return p[0] * q[1] - p[1] * q[0]


def cr_pair(P4):
    """Homogeneous cross-ratio of four unit pairs as a unit pair;
    None if degenerate."""
    num = br(P4[0], P4[2]) * br(P4[1], P4[3])
    den = br(P4[0], P4[3]) * br(P4[1], P4[2])
    v = np.array([num, den])
    n = float(np.linalg.norm(v))
    if n < 1e-300:
        return None
    return v / n


def cr_defect_step(Pa, Pb):
    """(a): median cross-ratio defect over the frozen
    well-conditioned quadruple battery; (value, n_quads)."""
    n = len(Pa)
    K = min(n, CR_MAX_NODES)
    sel = np.unique(np.round(np.linspace(0, n - 1, K)).astype(int))
    defects = []
    for quad in combinations(sel, 4):
        qa, qb = Pa[list(quad)], Pb[list(quad)]
        ok = True
        for u, v in combinations(range(4), 2):
            if (chordal(qa[[u]], qa[[v]])[0] < CR_SEP_MIN
                    or chordal(qb[[u]], qb[[v]])[0] < CR_SEP_MIN):
                ok = False
                break
        if not ok:
            continue
        ca, cb = cr_pair(qa), cr_pair(qb)
        if ca is None or cb is None:
            continue
        defects.append(abs(ca[0] * cb[1] - ca[1] * cb[0]))
    if len(defects) < CR_MIN_QUADS:
        return None, len(defects)
    return float(np.median(defects)), len(defects)


def measure_world(rungs):
    """The identical per-world measurement: consecutive valid-
    carrier pairs, five discriminators, typed skips counted."""
    steps = []
    skips = dict(no_carrier=0, common_j=0, anchor=0, battery=0)
    for ra, rb in zip(rungs[:-1], rungs[1:]):
        if ("f" not in ra or "f" not in rb
                or ra["rk"] > CARRIER_RK_BAR
                or rb["rk"] > CARRIER_RK_BAR):
            skips["no_carrier"] += 1
            continue
        com, ia, ib = np.intersect1d(ra["jp"], rb["jp"],
                                     return_indices=True)
        if len(com) < MIN_COMMON_J:
            skips["common_j"] += 1
            continue
        Pa = unit_pairs(ra["g"][ia], ra["f"][ia])
        Pb = unit_pairs(rb["g"][ib], rb["f"][ib])
        st = dict(ha=ra["h"], hb=rb["h"], n=len(com))
        # (d) raw identity distance (always computable here)
        st["raw"] = float(np.median(chordal(Pa, Pb)))
        # (a) cross-ratio defect
        crv, nq = cr_defect_step(Pa, Pb)
        st["cr"], st["nq"] = crv, nq
        if crv is None:
            skips["battery"] += 1
        # (b)/(c) three-anchor step map (com sorted ascending)
        seps = [chordal(Pa[[u]], Pa[[v]])[0]
                for u, v in ((0, 1), (0, 2), (1, 2))] \
            + [chordal(Pb[[u]], Pb[[v]])[0]
               for u, v in ((0, 1), (0, 2), (1, 2))]
        Ta = norm_map(Pa[0], Pa[1], Pa[2])
        Tb = norm_map(Pb[0], Pb[1], Pb[2])
        if min(seps) <= REF_SEP_MIN or Ta is None or Tb is None:
            skips["anchor"] += 1
            st["step"] = st["alpha"] = st["jres"] = None
            st["dsg"] = 0.0
        else:
            S = np.linalg.inv(Tb) @ Ta
            ds = float(np.linalg.det(S))
            if abs(ds) < 1e-300:
                skips["anchor"] += 1
                st["step"] = st["alpha"] = st["jres"] = None
                st["dsg"] = 0.0
            else:
                Sn = S / math.sqrt(abs(ds))
                keep = np.ones(len(com), dtype=bool)
                keep[[0, 1, 2]] = False
                st["step"] = float(np.median(chordal(
                    apply_hom(S, Pa), Pb)[keep]))
                st["alpha"] = cayley_alpha(Sn)
                st["jres"] = j_residual(Sn)
                st["dsg"] = math.copysign(1.0, ds)
        steps.append(st)
    return steps, skips


def frame_census(rungs):
    lo = [r["lamO"] for r in rungs if "lamC" in r]
    lc = [r["lamC"] for r in rungs if "lamC" in r]
    c = dict(built=len(rungs),
             carrier=sum(1 for r in rungs if "f" in r),
             valid=sum(1 for r in rungs
                       if "f" in r and r["rk"] <= CARRIER_RK_BAR),
             winav=sum(1 for r in rungs if "lamC" in r),
             winalive=sum(1 for r in rungs if "lamC" in r
                          and r["lamO"] < 1.0 and r["lamC"] < 1.0),
             full=sum(1 for r in rungs if r.get("full")),
             rkmax=max([r["rk"] for r in rungs if "f" in r],
                       default=float("inf")),
             medO=(float(np.median(lo)) if lo else float("nan")),
             medC=(float(np.median(lc)) if lc else float("nan")),
             nfireO=sum(1 for v in lo if v > 1.0),
             nfireC=sum(1 for v in lc if v > 1.0))
    c["alive"] = (c["built"] >= MIN_BUILT_ALIVE
                  and c["winalive"] >= WIN_ALIVE_FRAC * c["built"]
                  and c["valid"] >= MIN_CARRIER_ALIVE)
    return c


def sign_flips(rungs, key="detsgn"):
    sg = [r[key] for r in rungs if key in r]
    flips = sum(1 for u, v in zip(sg[:-1], sg[1:]) if u != v)
    return len(sg), sum(1 for s in sg if s > 0), flips


def fmt(v, spec="%.4f"):
    return (spec % v) if v is not None else "   -  "


def main():
    section("PRIME.PORT.MOEBIUS.CENSUS.01 -- six-world Moebius "
            "discriminator census (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; NO post-hoc selection; no marker "
          "moves.")
    print("\nS0 -- firewall + Epstein sieve ward")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    dev = float(np.max(np.abs(lambda_eps(EPS_WARD_N)
                              - lambda_eps_slow(EPS_WARD_N))))
    check("S0.2 EPSTEIN SIEVE WARD: fast vs verbatim at N = %d, "
          "max dev %.2e <= %.0e (amendment i)"
          % (EPS_WARD_N, dev, EPS_WARD_BAR),
          dev <= EPS_WARD_BAR, kill="K1")

    # ------------------------------------------------------------ P
    section("P -- build the six ladders (identical pipeline; all "
            "frame-A zones, h <= %d)" % H_DEEP_MAX)
    zones = core.frame_a_zones()
    world_rungs = {}
    for w in WORLDS:
        rungs = []
        n_fail = 0
        for kz in zones:
            r = rung_all(kz, w)
            if not isinstance(r, dict):
                if r is None:
                    n_fail += 1
                continue
            rungs.append(r)
        rungs.sort(key=lambda r: (r["h"], r["kz"]))
        world_rungs[w] = rungs
        print("    %s %-17s: %d rungs built, %d Lanczos/arm "
              "failures  [%.1f s]"
              % (w, WNAME[w], len(rungs), n_fail, time.time() - T0),
              flush=True)

    # ------------------------------------------------------------ F
    section("F -- frame-survival census (part of the deliverable)")
    print("    world                 built carrier rank2  win-av "
          "win-ALIVE full12  worst-rk   med-lamO   med-lamC  "
          "fires(O/C)  FRAME")
    census = {}
    for w in WORLDS:
        c = frame_census(world_rungs[w])
        census[w] = c
        print("    %s %-17s  %4d  %5d  %5d   %5d   %5d   %5d   "
              "%.1e  %9.3e  %9.3e   %2d/%2d     %s"
              % (w, WNAME[w], c["built"], c["carrier"], c["valid"],
                 c["winav"], c["winalive"], c["full"], c["rkmax"],
                 c["medO"], c["medC"], c["nfireO"], c["nfireC"],
                 "ALIVE" if c["alive"] else "DEAD"))
    fa_controls = [w for w in CONTROLS if census[w]["alive"]]
    print("    frame-alive controls: %s (rule: built >= %d, "
          "win-alive >= %.2f x built, rank2-valid >= %d)"
          % (fa_controls or "NONE", MIN_BUILT_ALIVE,
             WIN_ALIVE_FRAC, MIN_CARRIER_ALIVE))
    keep12 = [w for w in WORLDS
              if census[w]["winav"] >= MIN_WIN_RUNGS_E]
    print("    12-window AVAILABILITY: kept by %s; the smooth "
          "worlds' death channel is SUBCRITICALITY (lam > 1), "
          "not availability." % ", ".join(keep12))
    check("F.1 frame census reported (six worlds; truth must be "
          "ALIVE)", census["W1"]["alive"], kill="K1")

    # frozen fallback window, only if a frame-alive world lost it
    fb_needed = any(census[w]["winav"] < MIN_WIN_RUNGS_E
                    for w in WORLDS if census[w]["alive"])
    jfb = []
    if fb_needed:
        sets = []
        for w in [x for x in WORLDS if census[x]["alive"]]:
            rr = [r for r in world_rungs[w] if "jp" in r]
            cnt = {}
            for r in rr:
                for j in set(int(x) for x in r["jp"]):
                    cnt[j] = cnt.get(j, 0) + 1
            sets.append({j for j, n in cnt.items()
                         if n >= FB_PRESENCE_FRAC * len(rr)})
        jfb = sorted(set.intersection(*sets))[:FB_MAX_NODES] \
            if sets else []
        print("    FALLBACK WINDOW fired: J_fb = %s" % jfb)
        if len(jfb) >= FB_MIN_NODES:
            for w in WORLDS:
                for r in world_rungs[w]:
                    idx = {int(j): k for k, j
                           in enumerate(r["uf_n"])}
                    if not all(j in idx for j in jfb):
                        continue
                    E = rebuild_E(r)
                    iw = [idx[j] for j in jfb]
                    io = [k for k in range(E.shape[0])
                          if k not in set(iw)]
                    IO = np.eye(len(io)) - E[np.ix_(io, io)]
                    Cfb = (E[np.ix_(iw, iw)]
                           + E[np.ix_(iw, io)] @ np.linalg.solve(
                               IO, E[np.ix_(io, iw)]))
                    Cfb = 0.5 * (Cfb + Cfb.T)
                    sgn, _ = np.linalg.slogdet(
                        np.eye(len(jfb)) - Cfb)
                    r["detsgn_fb"] = float(sgn)
    else:
        print("    fallback window NOT needed (every frame-alive "
              "world keeps >= %d windowed rungs)." % MIN_WIN_RUNGS_E)

    # ------------------------------------------------------------ D
    section("D -- the five discriminators, per world (identical "
            "pipeline; full per-step tables)")
    wsum = {}
    for w in WORLDS:
        rungs = world_rungs[w]
        steps, skips = measure_world(rungs)
        print("\n  %s %s -- %d steps (typed skips: %d no-carrier, "
              "%d common-j, %d anchor, %d battery)"
              % (w, WNAME[w], len(steps), skips["no_carrier"],
                 skips["common_j"], skips["anchor"],
                 skips["battery"]))
        for st in steps:
            print("    h %4d->%4d n %2d | cr %s(q%3d) | step %s "
                  "|a| %s | jres %s dsg %+.0f | raw %s"
                  % (st["ha"], st["hb"], st["n"], fmt(st["cr"]),
                     st["nq"], fmt(st["step"]),
                     fmt(st["alpha"], "%.3f"),
                     fmt(st["jres"], "%+.1e"), st["dsg"],
                     fmt(st["raw"])))
        a_v = [s["cr"] for s in steps if s["cr"] is not None]
        b_v = [s["step"] for s in steps if s["step"] is not None]
        c_v = [s["jres"] for s in steps if s["jres"] is not None]
        d_v = [s["raw"] for s in steps]
        al_v = [s["alpha"] for s in steps
                if s["alpha"] is not None]
        nw, npos, nfl = sign_flips(rungs, "detsgn")
        nwf, nposf, nflf = sign_flips(rungs, "detsgn_fb")
        vals = dict(
            n_steps=len(steps),
            a=(float(np.median(a_v)) if len(a_v)
               >= MIN_STEPS_WORLD else None),
            b=(float(np.median(b_v)) if len(b_v)
               >= MIN_STEPS_WORLD else None),
            c=(float(np.min(c_v)) if len(c_v)
               >= MIN_STEPS_WORLD else None),
            cfrac=(float(np.mean([s["dsg"] > 0 for s in steps
                                  if s["jres"] is not None]))
                   if len(c_v) >= MIN_STEPS_WORLD else None),
            d=(float(np.median(d_v)) if len(d_v)
               >= MIN_STEPS_WORLD else None),
            alpha=(float(np.median(al_v)) if al_v else None),
            e=((nw, npos, nfl) if nw >= MIN_WIN_RUNGS_E else
               ((nwf, nposf, nflf) if nwf >= MIN_WIN_RUNGS_E
                else None)),
            e_fb=(nw < MIN_WIN_RUNGS_E and nwf >= MIN_WIN_RUNGS_E))
        wsum[w] = vals

    # ------------------------------------------------------------ T
    section("T -- the six-world five-discriminator table + frozen "
            "typing")
    print("    bars: (a) med <= %.2f; (b) med <= %.2f; (c) min >= "
          "%.0e; (d) med <= %.2f; (e) >= %d rungs, 0 flips"
          % (BAR_A, BAR_B, BAR_C, BAR_D, MIN_WIN_RUNGS_E))

    def passes(w, d):
        v = wsum[w]
        if d == "a":
            return None if v["a"] is None else (v["a"] <= BAR_A)
        if d == "b":
            return None if v["b"] is None else (v["b"] <= BAR_B)
        if d == "c":
            return None if v["c"] is None else (v["c"] >= BAR_C)
        if d == "d":
            return None if v["d"] is None else (v["d"] <= BAR_D)
        if v["e"] is None:
            return None
        return v["e"][2] == 0

    print("\n    world                 steps  a:cr-def    "
          "b:step-res  |alpha|  c:jres-min  det>0  d:raw-id    "
          "e:tau-signs        FRAME")
    for w in WORLDS:
        v = wsum[w]
        e_txt = ("-" if v["e"] is None else
                 "%d rungs %d+ %dflip%s" % (v["e"][0], v["e"][1],
                                            v["e"][2],
                                            " FB" if v["e_fb"]
                                            else ""))
        marks = {d: ("P" if passes(w, d) is True else
                     "F" if passes(w, d) is False else "-")
                 for d in "abcde"}
        print("    %s %-17s  %4d   %s %s  %s %s  %s   %s %s  "
              "%s   %s %s  %-18s %s  %s"
              % (w, WNAME[w], v["n_steps"],
                 fmt(v["a"]), marks["a"], fmt(v["b"]), marks["b"],
                 fmt(v["alpha"], "%.3f"),
                 fmt(v["c"], "%+.1e"), marks["c"],
                 fmt(v["cfrac"], "%.2f"),
                 fmt(v["d"]), marks["d"], e_txt, marks["e"],
                 "ALIVE" if census[w]["alive"] else "DEAD"))

    typing = {}
    for d in "abcde":
        t = passes("W1", d)
        if t is not True:
            typing[d] = ("UNDECIDED(truth-fails)" if t is False
                         else "UNDECIDED(truth-n/a)")
        elif not fa_controls:
            typing[d] = "UNDECIDED(no-frame-alive-controls)"
        else:
            pv = [passes(w, d) for w in fa_controls]
            n_pass = sum(1 for x in pv if x is True)
            if all(x is not True for x in pv):
                typing[d] = "ARITHMETIC"
            elif n_pass >= 2:
                typing[d] = "GEOMETRIC"
            else:
                typing[d] = "UNDECIDED"
    print("\n    per-discriminator typing (frame-alive controls "
          "only: %s):" % (fa_controls or "NONE"))
    for d, nm in (("a", "cross-ratio defect"),
                  ("b", "three-anchor step map"),
                  ("c", "J-contractivity"),
                  ("d", "raw identity distance"),
                  ("e", "tau-factor signs")):
        print("      (%s) %-24s -> %s" % (d, nm, typing[d]))
    print("\n    FRAME-DEAD CONTEXT (computed, printed, NOT typed "
          "-- no post-hoc selection):")
    for d in "abcde":
        cp = [w for w in CONTROLS if passes(w, d) is True]
        print("      (%s) controls meeting the bar anyway: %s"
              % (d, ", ".join(cp) if cp else "none"))
    print("      frame separation: truth win-alive %d/%d; "
          "controls win-alive %s -- the arithmetic/control "
          "separation happens at the FRAME (window "
          "subcriticality), upstream of every carrier "
          "discriminator."
          % (census["W1"]["winalive"], census["W1"]["winav"],
             ["%s %d/%d" % (w, census[w]["winalive"],
                            census[w]["winav"])
              for w in CONTROLS]))
    check("T.1 typed reading computed (frozen decision rules)",
          True)

    # ------------------------------------------------------------ K1
    section("K -- truth-pipeline wards (K1)")
    tr = world_rungs["W1"]
    rk_t = max([r["rk"] for r in tr if "f" in r],
               default=float("inf"))
    check("K.1 >= %d truth rungs built" % MIN_RUNGS_TRUTH,
          len(tr) >= MIN_RUNGS_TRUTH, "%d rungs" % len(tr),
          kill="K1")
    check("K.2 truth rank-2 ward (max s3/s1 %.1e <= %.0e, "
          "predecessor bar)" % (rk_t, TRUTH_RK_BAR),
          rk_t <= TRUTH_RK_BAR, kill="K1")
    check("K.3 >= %d truth steps measured" % MIN_STEPS_TRUTH,
          wsum["W1"]["n_steps"] >= MIN_STEPS_TRUTH,
          "%d steps" % wsum["W1"]["n_steps"], kill="K1")

    # ------------------------------------------------------------ V
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        print("\n  VERDICT: PIPELINE-BROKEN")
    else:
        print("\n  VERDICT: MOEBIUSCENSUS-MEASURED / "
              + " ".join("%s:%s" % (d, typing[d]) for d in "abcde"))
        print("  (frame-alive controls: %s; frame-dead: %s)"
              % (", ".join(fa_controls) or "none",
                 ", ".join(w for w in CONTROLS
                           if w not in fa_controls) or "none"))
        if not fa_controls:
            print("  PLAIN ANSWER: with zero frame-alive controls "
                  "the census cannot type any discriminator as "
                  "ARITHMETIC or GEOMETRIC -- the arithmetic "
                  "separates at the FRAME (window "
                  "subcriticality), and the Moebius/cr route "
                  "needs the scalar-cocycle/determinant bridge "
                  "(parallel tau_mobius_factor probe) for any "
                  "claim finer than frame survival.")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_VD_RE = re.compile(r"VERDICT[:\]]")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _census(out):
    marks = _PF_RE.findall(out)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    verdict = ""
    for line in out.splitlines():
        if _VD_RE.search(line):
            verdict = line.strip()
    return len(marks), fails, verdict


def _exec_probe(name, src, run_entry=True):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace (round-31 convention); capture and re-emit
    stdout; return (stdout, exit_code, byte_equal_or_None)."""
    if src[:1] == "\n":
        src = src[1:]
    path = _probe_file(name)
    same = None
    if path is not None:
        with open(path, encoding="utf-8") as fh:
            same = (fh.read() == src)
    fname = path or os.path.abspath(__file__)
    mod = types.ModuleType(name)
    mod.__file__ = fname
    sys.modules[name] = mod
    buf = io.StringIO()
    code = 0
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if run_entry and callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_fails, exp_verdict,
          exp_code, gates):
    n, fails, verdict = _census(out)
    ok = (n == exp_n and fails == list(exp_fails)
          and exp_verdict in verdict and code == exp_code
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d) | FAILs %s "
          "(exp %s) | exit %d (exp %d) | %s\n      verdict line: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             ",".join(exp_fails) if exp_fails else "none",
             code, exp_code, prov, verdict), flush=True)
    return ok


_PLAN = (
    ('mobius_crossratio_firewall_probe', _SRC_0, 10, (), 'CRFIREWALL-MEASURED', 0),
    ('iiks_gauge_firewall_probe', _SRC_1, 13, (), 'GAUGEFW-MEASURED', 0),
    ('mobius_control_census_probe', _SRC_2, 7, (), 'MOEBIUSCENSUS-MEASURED', 0),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v891 -- PRIME.PORT.MOEBIUS.CRFIREWALL.01 + PRIME.PORT.MOEBIUS.GAUGEFW.01 + PRIME.PORT.MOEBIUS.CENSUS.01: the honest kill battery of the Moebius/carrier-invariance route -- CR-DEAD, GAUGE-MADE, all census discriminators undecided')
    print("(frozen probes embedded byte-exact and executed verbatim; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    for name, src, exp_n, exp_fails, exp_verdict, exp_code in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_fails,
              exp_verdict, exp_code, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v891: %d/%d pattern gates passed | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the Moebius route is killed fit-free: the normalized invariance was manufactured, the scalar cocycle does not track the wall, and the arithmetic separates at the frame')
    print("[%s] v891 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
