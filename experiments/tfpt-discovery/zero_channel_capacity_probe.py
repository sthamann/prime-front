#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""zero_channel_capacity_probe -- PRIME.ZERO.CHANNEL.CAPACITY.01

FROZEN SPEC (2026-08-21).  EXPLORATION ONLY.  EXPLORATORY INSTRUMENT-
CHARACTERIZATION ROUND.  This probe writes no verification module,
paper, ledger, website, manifest, Lean file or status marker.  It
makes NO RH claim in any direction, NO storage/physics claim and NO
arithmetic-novelty claim.  It closes no gate and narrows no gate.
HONEST FRAMING (fixed): this round measures the INSTRUMENT'S resolving
power over controlled zero-configurations -- a codec/sensitivity
characterization of the already-demonstrated r187/r190 dictionary.
The dictionary is: WRITE = move a controlled subset of zeros along
the line; READ = the S2 spike-coherence detector; NOISE = engine
tolerances and selection/jitter variability.  Every verdict below is
numbers-only.

=======================================================================
MISSION.  r187 (zero_causal_synth_probe, SPEC c20e87eec6d158b9, note
DVIII) demonstrated the causal write->read arc: the S2 signature
responds dose-monotonically to controlled zero movements (ZB first
response (0.10, 1e-2), first death (0.05, 1e-4)), requires the exact
ordinates (ZA: EXACT-ORDINATES-REQUIRED; the ZC R-token scale 0.003),
and Z0 synthesis is essentially perfect (|dC| = 0.0006 on C = 131.04).
r190 (zb_wiggle_strat_probe, SPEC 8639b3a78503a0f9, note DXI) measured
the channel noise: matched-dose selection spreads 5.09/3.07/3.98,
per-zero leverage dC in [-1.69, -1.04] for the lowest 10 zeros
(gamma_2 strongest), strong subadditivity (+5.32 on -13.21), the
low-m valley, depth stability |dW| = 0.0014; upgrade-by-reference
ZERO-CAUSALITY-DEMONSTRATED-WITH-STRATIFICATION.  THIS round
characterizes that dictionary AS A CHANNEL, information-
theoretically, everything predefined: a frozen codebook of ON-LINE
ordinate-shift patterns, a frozen vector of S2-type readings, a
frozen decoder, empirical mutual information per band, the
resolution limit against the r187 ZC scale 0.003, and the code-
structure questions (linearity / redundancy / placement asymmetry).
CONTEXT CITATION (not upgraded): round 107 (PRIME.CODE.SYNTHESIS.01,
note CDVII, verdict CODE-READING-TRUE-DECODING-DIRECTION) adjudicated
the operator's primes-as-error-correcting-code intuition at the Gram
grammar -- structure vindicated, decoding direction only.  This round
OPERATIONALIZES a code-reading question at the zero-comb dictionary;
its outcome types as instrument characterization and does NOT upgrade
the round-107 verdict.
=======================================================================
ENGINE (REUSED FAITHFULLY, no new construction): this probe IMPORTS
zero_causal_synth_probe (the frozen r187 module; identity gated on
SPEC c20e87eec6d158b9) and uses ITS functions verbatim: ward_cache7/
ward_cache_big (the only np.load sites, inside the imported module's
ward_ functions -- delegated wards, disclosed), spike_positions,
osc_dens, weights_from_dens, synth_weights, landau_field, coherence,
d2_eval_syn.  Same depth (D2 synthesis N_D2 = 2e6, alt checkpoint
1e6), same window (q-1/2, q+1/2], same chunk 20000, same detector
(n7000 Landau field, grid 4096, INTRAND bands for the W5/Z0 anchor
replication).  S2-ONLY round (r187: SYNTH-S1-DEAD-PREDICTED).

=======================================================================
C1  THE CODEBOOK AND THE READOUT (all frozen)
=======================================================================
SYMBOLS: K = 4 disjoint bands of M_BAND = 200 consecutive zeros of
the synthesis prefix gbig[:2e6]; per band a TERNARY symbol s in
{0, +, -}: gamma -> gamma + sgn(s) * eps for every zero of the band
(coherent on-line translation; the configuration stays "legal" --
no off-line zeros).  PLACEMENTS: LOW = indices [0, 800) (gamma ~
14.1-237), MID = indices [2000, 2800) (gamma ~ 2504-3327, the lower
edge of the r190 leverage window 2500-9900).  EPS GRID (spans the
r187 ZC-token scale 0.003): (0.001, 0.003, 0.01, 0.03).  The
off-line (delta, f) channel and an extension test-point set are
disclosed cost non-goals A0(iii).
READOUT: R_DIM = 21 signed S2-type readings of the synthesized comb
w against the frozen n7000 Landau field Z(u) at the 465 true prime-
power atoms: 16 contiguous index blocks + 4 contiguous index blocks
(two window scales) + the global reading; each reading y_j =
sum_{i in B_j} w_i Z(u_i) / sqrt(sum_{i in B_j} w_i^2 * z_ms) with
the engine's grid mean-square z_ms (the signed per-block form of the
r184/r185 C statistic; norm-nonlinear through the denominator).
DECODER (frozen): EXACT NEAREST-CENTROID -- all 3^4 = 81 codeword
readings are synthesized noiselessly per cell (deterministic engine;
superposition in osc-space is exact by construction, the readout map
osc -> y carries the norm nonlinearity exactly), Euclidean distance,
unweighted.  Disclosed A0(i): the train/test split of the brief
degenerates -- the engine is deterministic, centroids are exact
synthesis, nothing is fitted; evaluation noise seeds are disjoint
from everything by the seed registry.  Disclosed A0(iv): the
unweighted decoder is suboptimal (no noise whitening) -- all
capacities below are LOWER bounds of the instrument's separating
power.
=======================================================================
C2  THE CHANNEL NOISE + THE CAPACITY MEASUREMENT (all frozen)
=======================================================================
NOISE (the channel; ZC family of the r187 registry): seeded ordinate
jitter on the frozen pool = indices [4000, 24000) (20000 zeros;
inside the r190 mid-leverage window; DISJOINT from both placements
-- noise never touches encoded symbols), gamma -> gamma + eps_noise
* u_r with unit draws u_r ~ uniform(-1, 1)^20000, rng([3100, r]),
r = 0..NREAL-1, NREAL = 2*N_MSG + 16*N_AVG = 480.  eps_noise is
selected by the FROZEN RULE from candidates (0.001, 0.003, 0.01) in
ONE disclosed calibration pass (--calib, log kept; measures noise
sigma and template norms ONLY -- never decodes): the candidate
minimizing |log10(median-band MF-SNR at eps_sig = 0.003, LOW)|,
where SNR_b = ||t_b|| / sigma_b, t_b the (0.003, +) template of LOW
band b, sigma_b = std over 16 calib realizations of <dy_noise,
t_b/||t_b||> -- the rule places the decode threshold mid-grid.  The
measured pick is frozen in A1 before any decoding.
CELLS: 2 placements x 4 eps = 8 capacity cells, cell index ci = 4 *
placement + eps-index.  N_MSG = 48 seeded messages per cell,
rng([3000, ci, m]) -> 4 iid uniform ternary symbols; noise
realization r = m (PAIRED across cells, disclosed A0(ii): variance-
reduced cross-cell comparison; distinct within cell).  Decode ->
per-band 3x3 confusion -> empirical mutual information: plug-in MI
+ Miller-Madow bias correction (Miller 1955; in bits, correction
(m_x + m_y - m_xy - 1)/(2 N ln 2); MAY slightly exceed log2 3 =
1.585 at zero error, disclosed A0(vi)).  NULL CELL (capacity must
be 0): encoding disabled, intended messages rng([3200, m]),
realizations r = 48..95, decoded against the eps = 0.003 centroids
of each placement (A0(v)).  MI_CRIT = max(0.05, max over the 8 null
per-band MIs clipped at 0).  RESOLUTION LIMIT per placement = the
smallest grid eps with median-over-bands MI > MI_CRIT; compare with
the r187 scale 0.003.  BUDGET currency: 200 * eps per band (zeros
moved x shift magnitude); error-rate-vs-budget curve reported.
MULTI-READING AVERAGING (the r190-noise-model prediction leg): cell
(LOW, 0.001), N_AVG = 24 messages rng([3000, 99, m]), 16 readings
each (realizations r = 96 + 16 m + j; nested subsets n_read = 1, 4,
16; reading VECTORS averaged before decoding).  Prediction P2: the
matched-filter noise sigma of the averaged reading falls ~ 1/
sqrt(n_read); GATE (frozen window): sigma(16-mean)/sigma(single) in
[0.15, 0.42] (1/4 with estimator slack).  RESLIM-AVG reported: does
(LOW, 0.001, n_read = 16) clear MI_CRIT (resolving below the single-
reading limit by averaging)?
=======================================================================
C3  THE CODE-STRUCTURE QUESTIONS (typed as instrument facts)
=======================================================================
(i) LINEARITY: all 6 LOW band pairs x 4 eps, symbols (+, +),
noiseless: NL = ||y(b & b') - y0 - (y(b) - y0) - (y(b') - y0)|| /
||(y(b) - y0) + (y(b') - y0)||; NL_CRIT = 0.2; LINEARITY-SCALE =
smallest grid eps with max-pair NL > 0.2 (linear regime = plain
codec; breakdown = interference/channel memory).  Continuity number
with r190 (+5.32 subadditivity at off-line delta 0.4): the global-C
nonadditivity of bands 0 & 1 at (LOW, 0.03).
(ii) REDUNDANCY (erasure correction over the physical channel):
parity sub-codebook x_3 = x_0 + x_1 + x_2 mod 3 at the strongest
cell (LOW, 0.03); N_ERA = 48 coded messages, info symbols
rng([3400, m]); erased band e = m mod 4, its TRANSMITTED symbol
replaced by rng([3300, m]) uniform ternary (may equal the original,
prob 1/3 -- chance baseline unchanged, disclosed A0(vii)); noise
realizations r = m (paired, A0(ii)).  Decoder knows e, decodes all
bands by nearest-centroid, RESTORES band e from the parity of the
other three decoded symbols; recovery = restored == intended.
Chance 1/3; significance bar 1/3 + 3 sqrt((1/3)(2/3)/48) = 0.5374.
Recovery above the bar = the channel supports distributed/redundant
encoding (readings keep the bands separable end-to-end).
(iii) ASYMMETRY (the r190 leverage law as channel gain): template-
norm gain ratio mean_MID/mean_LOW per eps and MI totals per
placement; tokens CHANNEL-GAIN-MID>LOW (mean ratio >= 1.25),
CHANNEL-GAIN-LOW>MID (<= 0.8), else CHANNEL-GAIN-FLAT.
=======================================================================
C4  CONTROLS + FROZEN PREDICTIONS + TAXONOMY
=======================================================================
CONTROLS: W5-DIRECT + Z0 replication against the r190 full-precision
record (C_W5 = 131.038817, band 12.599123, R = 10.400630; C_Z0 =
131.038259, R = 10.403004; bars 0.005); NULL cell (above); DEPTH
PARITY (one reduced-depth check, r190 recipe: base synthesis
truncated to 1e6, moved band + jitter draws FIXED): |C_Z0(1e6) -
C_Z0(2e6)| <= 0.01, template (LOW, band 0, 0.03, +) corr >= 0.9 and
norm ratio in [0.5, 1.5]; ENGINE IDENTITY gate on the imported SPEC.
FROZEN PREDICTIONS (before any evaluation): P1 template norms
strictly increasing in eps for every (placement, band, sign) (linear
regime: max phase eps*u <= 0.24 rad).  P2 the sqrt-averaging window
(above).  P3 MID gain > LOW (the r190 leverage law read as channel
gain).  P4 NL grows with eps and NL(0.001) < 0.2 (a linear small-
dose regime exists; r190 subadditivity lives at large dose).  P5
null capacity 0 within the seeded band.
HONEST OUTCOME TAXONOMY (frozen adjudication; verdict gates
DEFINITIONAL per house convention):
  ENGINE-DRIFT            the identity gate or the W5/Z0 replication
                          fails -- honest stop, everything printed.
  CHANNEL-DEGENERATE      no capacity cell clears MI_CRIT (the
                          readings do not separate the codebook;
                          equally reportable).
  CHANNEL-CHARACTERIZED(RESLIM(eps*_LOW, eps*_MID), capacity
                          surface, LINEARITY-SCALE) otherwise, plus
                          CODE-STRUCTURE-LINEAR-CODEC xor
                          CODE-STRUCTURE-INTERFERENCE-MEMORY (by
                          NL_CRIT over the grid), optionally
                          CODE-STRUCTURE-REDUNDANT-DISTRIBUTED (the
                          erasure bar), and the CHANNEL-GAIN token.
  Plus always: RESLIM-AVG token; NO-RH-CLAIM; NO-STORAGE-CLAIM;
  NO-ARITHMETIC-NOVELTY-CLAIM.
LOOP GUARD (machine-checked, r187/r190 convention): the verified
cache as DATA for controlled configurations is control-construction
(Epstein class); ZERO-VERIF-AS-HYP and RH-GRANT are ancestors of
NOTHING delivered; no census-forall-k, no A_0-triangle, no RH-
conditional second moment is consumed.  AST firewall on THIS file:
no zero-oracle names, no zeta use, np.load NOWHERE (wards delegated
to the imported frozen engine), no verification/ import.

Bars: anchors <= 0.005 (r190 full-precision record); depth sanity
<= 0.01; template corr >= 0.9, norm ratio [0.5, 1.5]; null median-
band MI <= 0.15 per placement, pooled null accuracy in [0.15,
0.52]; averaging window [0.15, 0.42]; runtime <= 2700 s.  Gates
G01..G28.  Smoke mode (--smoke): structural only (depth 2e5/1e5,
eps grid (0.003, 0.03), N_MSG = 8, N_AVG = 4 with reads (1, 4),
N_ERA = 8, nnull 5; record-replication and window gates SMOKE-
scoped to finiteness).
AMENDMENT BLOCK (disclosed at freeze; house protocol):
  A0 (pre-freeze design choices): (i) exact-centroid decoder, the
  train half degenerates (deterministic engine, nothing fitted);
  (ii) noise realizations paired across cells (r = m) and reused by
  the erasure leg; (iii) off-line channel + extension test points =
  cost non-goals; (iv) unweighted Euclidean decoder -> capacities
  are lower bounds; (v) null cell decoded against the eps = 0.003
  centroids; (vi) MM-corrected MI may exceed log2 3 at zero error;
  (vii) the erasure corrupt symbol may equal the original; (viii)
  seed registry 3000/3100/3200/3300/3400 exhaustive, no reruns.
  A1 (at freeze, after smoke1 + the ONE disclosed calibration pass;
  logs kept as zero_channel_capacity_probe.smoke1.log / .calib1.log,
  both at pre-freeze SPEC 477cedabd88f077e): smoke1 (structural,
  27/28) found ONE instrument-scoping bug -- the G13 null-control
  gate enforced the full-N bars at smoke N = 8, where the Miller-
  Madow MI fluctuation is O(0.8) bits; fixed by SMOKE-scoping G13 to
  finiteness (the full N = 48 bars are UNTOUCHED; no grid, seed,
  decoder, estimator, bar or taxonomy rule changed).  The
  calibration pass (anchors replicated exactly: C_W5 = 131.038817,
  band 12.599123, R = 10.400630; C_Z0 = 131.038259, R = 10.403004)
  measured (LOW, eps_sig = 0.003) template norms 0.0018/0.0012/
  0.0014/0.0009 and the candidate ladder: eps_noise = 0.001 ->
  median MF-SNR 4.310 (|log10| 0.635), 0.003 -> 1.434 (0.157),
  0.01 -> 0.427 (0.369); the frozen rule picks EPS_NOISE = 0.003 --
  the r187 ZC-token scale itself is the frozen channel-noise scale.
  Decoding was never run pre-freeze.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import math
import os
import statistics
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import zero_causal_synth_probe as ZS          # the frozen r187 engine

# ---------------------------------------------------------------- frozen
R187_SPEC16 = "c20e87eec6d158b9"
N_D2 = 2_000_000
N_ALT = 1_000_000
M_BAND = 200
K_BANDS = 4
PLC_START = {"LOW": 0, "MID": 2000}
PLC_ORDER = ("LOW", "MID")
EPS_GRID = (0.001, 0.003, 0.01, 0.03)
NOISE_LO, NOISE_HI = 4000, 24000
EPS_NOISE_CANDS = (0.001, 0.003, 0.01)
EPS_NOISE = 0.003            # A1: frozen from the calibration pass
EPS_SIG_CAL = 0.003
N_CALREAL = 16
NBLK_FINE, NBLK_COARSE = 16, 4
N_MSG = 48
N_AVG = 24
NREADS = (1, 4, 16)
N_ERA = 48
AVG_CELL_CODE = 99
SEED_MSG, SEED_NOISE, SEED_NULL = 3000, 3100, 3200
SEED_ERA_SYM, SEED_ERA_MSG = 3300, 3400
REC = dict(C_W5=131.038817, BAND_W5=12.599123, R_W5=10.400630,
           C_Z0=131.038259, R_Z0=10.403004)
TOL_REC = 0.005
NNULL = 20
MI_FLOOR = 0.05
NULL_MI_BAR = 0.15
NULL_ACC_WIN = (0.15, 0.52)
AVG_WIN = (0.15, 0.42)
NL_CRIT = 0.2
GAIN_HI, GAIN_LO = 1.25, 0.8
ERA_EPS_IDX = -1             # strongest grid eps
AVG_EPS_IDX = 0              # weakest grid eps
NULL_EPS = 0.003
DEPTH_CORR_MIN = 0.9
DEPTH_NORM_WIN = (0.5, 1.5)
Z0_DEPTH_TOL = 0.01
RUNTIME_BAR = 2700.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()

CHECKS: list = []


def check(name: str, ok: bool, detail: str) -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg: str) -> None:
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "siegel" + "z", "siegel" + "theta",
            "n" + "zeros", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        if nm is None:
            continue
        low = nm.lower()
        if low in forb:
            bad.append("forbidden %s @%d" % (nm, node.lineno))
        if low == "zeta":
            bad.append("zeta use @%d" % node.lineno)
        if isinstance(node, ast.Attribute) and nm == "load":
            bad.append("np.load in this file @%d (wards are "
                       "delegated to the imported engine)"
                       % node.lineno)
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; NO zeta; np.load NOWHERE in "
                       "this file (wards delegated to the frozen "
                       "engine); no verification/ import")


# ------------------------------------------------------------- helpers
def mi_mm(true_s: list, dec_s: list, nsym: int = 3) -> float:
    """plug-in mutual information + Miller-Madow correction, bits."""
    n = len(true_s)
    cnt = np.zeros((nsym, nsym))
    for a, b in zip(true_s, dec_s):
        cnt[a][b] += 1.0
    p = cnt / n
    px = p.sum(axis=1)
    py = p.sum(axis=0)
    mi = 0.0
    for i in range(nsym):
        for j in range(nsym):
            if p[i][j] > 0:
                mi += p[i][j] * math.log2(p[i][j] / (px[i] * py[j]))
    mx = int(np.sum(px > 0))
    my = int(np.sum(py > 0))
    mxy = int(np.sum(p > 0))
    return mi + (mx + my - mxy - 1) / (2.0 * n * math.log(2.0))


def block_bounds(na: int) -> list:
    """(lo, hi) index blocks: 16-scale + 4-scale + global."""
    out = []
    for nblk in (NBLK_FINE, NBLK_COARSE):
        for j in range(nblk):
            out.append((int(round(na * j / nblk)),
                        int(round(na * (j + 1) / nblk))))
    out.append((0, na))
    return out


# ============================================================== main
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--smoke", action="store_true")
    ap.add_argument("--calib", action="store_true")
    args = ap.parse_args()
    smoke = args.smoke
    calib = args.calib
    full = not smoke

    print("=" * 78)
    print("zero_channel_capacity_probe -- PRIME.ZERO.CHANNEL."
          "CAPACITY.01  (EXPLORATORY INSTRUMENT-CHARACTERIZATION)")
    print("SPEC_SHA %s%s" % (SPEC_SHA[:16],
                             "  [SMOKE]" if smoke else
                             "  [CALIB]" if calib else ""))
    print("=" * 78)

    n_d2 = 200_000 if smoke else N_D2
    n_alt = 100_000 if smoke else N_ALT
    eps_grid = (0.003, 0.03) if smoke else EPS_GRID
    n_msg = 8 if smoke else N_MSG
    n_avg = 4 if smoke else N_AVG
    nreads = (1, 4) if smoke else NREADS
    n_era = 8 if smoke else N_ERA
    nnull = 5 if smoke else NNULL
    nread_max = nreads[-1]
    nreal = 2 * n_msg + nread_max * n_avg
    n_eps = len(eps_grid)
    null_ei = eps_grid.index(NULL_EPS)

    # ------------------------------------------------------------ S0
    section("S0  FIREWALL + ENGINE IDENTITY + WARDS")
    ok_fw, det = firewall_audit()
    check("G01-firewall-ast", ok_fw, det)
    check("G02-spec-seal", len(__doc__) > 4000,
          "SPEC_SHA %s (sha256 of __doc__)" % SPEC_SHA[:16])
    ok3 = ZS.SPEC_SHA[:16] == R187_SPEC16
    check("G03-engine-identity", ok3,
          "imported zero_causal_synth_probe SPEC %s == r187 record %s "
          "(engine reused verbatim, no reconstruction)"
          % (ZS.SPEC_SHA[:16], R187_SPEC16))
    gam7 = ZS.ward_cache7()
    gbig = ZS.ward_cache_big()
    mono7 = bool(np.all(np.diff(gam7) > 0))
    ovl = float(np.max(np.abs(gbig[:len(gam7)] - gam7)))
    okb = (len(gam7) == 7000 and len(gbig) == 20_000_000 and mono7
           and gam7[0] > 14.13 and ovl <= 1e-8)
    check("G04-ward-caches", okb,
          "n7000: %d (gamma_1 %.6f); big: %d (top %.4f); monotone %s; "
          "overlap %.2e <= 1e-8 (delegated wards, PT21 pedigree)"
          % (len(gam7), gam7[0], len(gbig), float(gbig[-1]), mono7,
             ovl))

    qs, us_atoms, w_true = ZS.spike_positions()
    us_ep = np.concatenate([np.log(qs - 0.5), np.log(qs + 0.5)])
    na = len(qs)
    ugrid = ZS.SPIKE_LO + (np.arange(1, ZS.SPIKE_GRID_N + 1)
                           * (ZS.SPIKE_HI - ZS.SPIKE_LO)
                           / (ZS.SPIKE_GRID_N + 1))
    zgrid = ZS.landau_field(gam7, ugrid)
    z_ms = float(np.mean(zgrid ** 2))
    z_at = ZS.landau_field(gam7, us_atoms)
    blks = block_bounds(na)
    info("spike support %d atoms; Landau grid rms %.2f; readout "
         "R_DIM = %d (16 + 4 blocks + global)"
         % (na, math.sqrt(z_ms), len(blks)))

    def readout(w: np.ndarray) -> np.ndarray:
        y = np.empty(len(blks))
        for j, (lo, hi) in enumerate(blks):
            num = float(np.dot(w[lo:hi], z_at[lo:hi]))
            den = float(np.dot(w[lo:hi], w[lo:hi]))
            y[j] = num / math.sqrt(den * z_ms)
        return y

    def y_of(osc: np.ndarray) -> np.ndarray:
        return readout(ZS.synth_weights(qs, osc))

    # ------------------------------------------------------------ S1
    section("S1  ANCHOR REPLICATION (W5-DIRECT + Z0, r190 record)")
    w5 = ZS.d2_eval_syn(gam7, us_atoms, w_true, z_ms, nnull,
                        ZS.FAM_CODE["Z0"], 0, intrand=True)
    ok5 = (abs(w5["C"] - REC["C_W5"]) <= TOL_REC
           and abs(w5["nullmax"] - REC["BAND_W5"]) <= TOL_REC
           and abs(w5["R"] - REC["R_W5"]) <= TOL_REC) if full \
        else np.isfinite(w5["C"])
    check("G05-w5-direct-rep", ok5,
          "W5-DIRECT: C = %.6f (rec 131.038817), band %.6f (rec "
          "12.599123), R = %.6f (rec 10.400630)%s"
          % (w5["C"], w5["nullmax"], w5["R"],
             "" if full else " [SMOKE-scoped]"))

    t0 = time.time()
    gs_syn = gbig[:n_d2]
    F_base = ZS.osc_dens(gs_syn, us_ep)
    osc_base = ZS.weights_from_dens(qs, F_base[:na], F_base[na:])
    w_z0 = ZS.synth_weights(qs, osc_base)
    info("base pass (true ordinates, %d zeros x %d endpoints): %.0f s"
         % (n_d2, len(us_ep), time.time() - t0))
    z0 = ZS.d2_eval_syn(gam7, us_atoms, w_z0, z_ms, nnull,
                        ZS.FAM_CODE["Z0"], 0, intrand=True)
    C_Z0 = z0["C"]
    ok6 = (abs(C_Z0 - REC["C_Z0"]) <= TOL_REC
           and abs(z0["R"] - REC["R_Z0"]) <= TOL_REC) if full \
        else np.isfinite(C_Z0)
    check("G06-z0-s2-rep", ok6,
          "Z0-S2: C_Z0 = %.6f (rec 131.038259), R = %.6f (rec "
          "10.403004)%s" % (C_Z0, z0["R"],
                            "" if full else " [SMOKE-scoped]"))
    if full and not (ok3 and ok5 and ok6):
        section("S9  TAXONOMY VERDICT")
        check("G27-taxonomy", True,
              "DEFINITIONAL: ENGINE-DRIFT (identity/anchor replication "
              "failed) -- honest stop, everything measured is printed")
        rt = time.time() - T0_WALL
        check("G28-runtime", rt <= RUNTIME_BAR,
              "runtime %.1f s <= %.0f s" % (rt, RUNTIME_BAR))
        print("\nCOMPOSITE VERDICT: ENGINE-DRIFT + NO-RH-CLAIM + "
              "NO-STORAGE-CLAIM + NO-ARITHMETIC-NOVELTY-CLAIM")
        print("SPEC_SHA %s" % SPEC_SHA[:16])
        return 1

    # ------------------------------------------------------------ S2
    section("S2  C1 CODEBOOK -- band templates (on-line shifts)")
    y0 = y_of(osc_base)
    band_idx = {}
    inc_on = {}
    for plc in PLC_ORDER:
        st = PLC_START[plc]
        for b in range(K_BANDS):
            lo = st + b * M_BAND
            band_idx[(plc, b)] = (lo, lo + M_BAND)
            gsel = gs_syn[lo: lo + M_BAND]
            Fo = ZS.osc_dens(gsel, us_ep)
            inc_on[(plc, b)] = ZS.weights_from_dens(qs, Fo[:na],
                                                    Fo[na:])
    tpl_osc = {}
    tpl_y = {}
    tpl_norm = {}
    for plc in PLC_ORDER:
        for ei, eps in enumerate(eps_grid):
            for b in range(K_BANDS):
                lo, hi = band_idx[(plc, b)]
                for s in (1, 2):
                    sgn = 1.0 if s == 1 else -1.0
                    gsh = gs_syn[lo:hi] + sgn * eps
                    Fs = ZS.osc_dens(gsh, us_ep)
                    dosc = (ZS.weights_from_dens(qs, Fs[:na], Fs[na:])
                            - inc_on[(plc, b)])
                    tpl_osc[(plc, ei, b, s)] = dosc
                    ty = y_of(osc_base + dosc) - y0
                    tpl_y[(plc, ei, b, s)] = ty
                    tpl_norm[(plc, ei, b, s)] = float(
                        np.linalg.norm(ty))
    check("G07-codebook-freeze", True,
          "DEFINITIONAL: K = %d bands x %d zeros, ternary shifts, "
          "placements LOW %s MID %s (gamma LOW [%.1f, %.1f], MID "
          "[%.1f, %.1f]), eps grid %s -- all templates synthesized"
          % (K_BANDS, M_BAND, str([0, K_BANDS * M_BAND]),
             str([PLC_START["MID"],
                  PLC_START["MID"] + K_BANDS * M_BAND]),
             float(gs_syn[0]),
             float(gs_syn[K_BANDS * M_BAND - 1]),
             float(gs_syn[PLC_START["MID"]]),
             float(gs_syn[PLC_START["MID"] + K_BANDS * M_BAND - 1]),
             str(eps_grid)))
    mono_ok = True
    for plc in PLC_ORDER:
        for b in range(K_BANDS):
            for s in (1, 2):
                seq = [tpl_norm[(plc, ei, b, s)]
                       for ei in range(n_eps)]
                if any(seq[i + 1] <= seq[i]
                       for i in range(len(seq) - 1)):
                    mono_ok = False
    check("G08-template-monotone", mono_ok,
          "P1: ||template|| strictly increasing in eps for all %d "
          "(placement, band, sign) chains" % (2 * K_BANDS * 2))
    print("\n  TEMPLATE NORMS ||y(band at +eps) - y0||")
    print("  %-6s %-5s" % ("plc", "band")
          + "".join("%10.4g" % e for e in eps_grid))
    for plc in PLC_ORDER:
        for b in range(K_BANDS):
            print("  %-6s %-5d" % (plc, b)
                  + "".join("%10.4f" % tpl_norm[(plc, ei, b, 1)]
                            for ei in range(n_eps)))
    check("G09-template-table", True,
          "DEFINITIONAL: norms above; mean LOW %.4f vs MID %.4f at "
          "eps = %.3g"
          % (statistics.mean(tpl_norm[("LOW", n_eps - 1, b, 1)]
                             for b in range(K_BANDS)),
             statistics.mean(tpl_norm[("MID", n_eps - 1, b, 1)]
                             for b in range(K_BANDS)),
             eps_grid[-1]))

    # ------------------------------------------------------------ S3
    section("S3  C2 NOISE CHANNEL (ZC-class jitter, pool [%d, %d))"
            % (NOISE_LO, NOISE_HI))
    g_pool = gs_syn[NOISE_LO: min(NOISE_HI, n_d2)]
    npool = len(g_pool)
    Fp = ZS.osc_dens(g_pool, us_ep)
    inc_pool_on = ZS.weights_from_dens(qs, Fp[:na], Fp[na:])

    def noise_inc(r: int, scale: float) -> np.ndarray:
        rng = np.random.default_rng([SEED_NOISE, r])
        gj = g_pool + scale * rng.uniform(-1.0, 1.0, npool)
        Fj = ZS.osc_dens(gj, us_ep)
        return (ZS.weights_from_dens(qs, Fj[:na], Fj[na:])
                - inc_pool_on)

    if calib:
        print("  [CAL] calibration pass: noise sigma + SNR ladder "
              "(NO decoding)")
        tref = {b: tpl_y[("LOW", eps_grid.index(EPS_SIG_CAL), b, 1)]
                for b in range(K_BANDS)}
        for cand in EPS_NOISE_CANDS:
            projs = {b: [] for b in range(K_BANDS)}
            for r in range(N_CALREAL):
                dy = y_of(osc_base + noise_inc(r, cand)) - y0
                for b in range(K_BANDS):
                    projs[b].append(float(
                        np.dot(dy, tref[b])
                        / np.linalg.norm(tref[b])))
            snrs = []
            for b in range(K_BANDS):
                sig = statistics.stdev(projs[b])
                snrs.append(float(np.linalg.norm(tref[b])) / sig)
            med = statistics.median(snrs)
            print("  [CAL] eps_noise %-7.4g sigma_b %s  SNR_b %s  "
                  "median SNR %.3f  |log10| %.3f"
                  % (cand,
                     " ".join("%.4f" % (np.linalg.norm(tref[b])
                                        / snrs[b])
                              for b in range(K_BANDS)),
                     " ".join("%.2f" % s for s in snrs), med,
                     abs(math.log10(med))))
        print("  [CAL] template norms at (LOW, 0.003): %s"
              % " ".join("%.4f" % np.linalg.norm(tref[b])
                         for b in range(K_BANDS)))
        print("\nCALIB DONE -- eps_noise to be frozen in A1 by the "
              "spec rule (min |log10(median SNR)|) BEFORE any "
              "decoding.")
        return 0

    t0 = time.time()
    dnoise = [noise_inc(r, EPS_NOISE) for r in range(nreal)]
    dy_noise = [y_of(osc_base + d) - y0 for d in dnoise]
    info("noise pass: %d realizations x %d pool zeros at eps_noise "
         "= %.4g: %.0f s"
         % (nreal, npool, EPS_NOISE, time.time() - t0))
    sig_ei = eps_grid.index(EPS_SIG_CAL)
    sigs = []
    snrs = []
    for b in range(K_BANDS):
        t = tpl_y[("LOW", sig_ei, b, 1)]
        that = t / np.linalg.norm(t)
        pr = [float(np.dot(dy_noise[r], that))
              for r in range(n_msg, 2 * n_msg)]
        sigs.append(statistics.stdev(pr))
        snrs.append(float(np.linalg.norm(t)) / sigs[-1])
    check("G10-noise-model", True,
          "DEFINITIONAL: frozen eps_noise = %.4g (A1); MF noise "
          "sigma per LOW band at eps_sig 0.003: %s; SNR %s (median "
          "%.2f)" % (EPS_NOISE, " ".join("%.4f" % s for s in sigs),
                     " ".join("%.2f" % s for s in snrs),
                     statistics.median(snrs)))
    t0h = tpl_y[("LOW", sig_ei, 0, 1)]
    that0 = t0h / np.linalg.norm(t0h)
    base_r = 2 * n_msg
    singles = [float(np.dot(dy_noise[base_r + i], that0))
               for i in range(nread_max * n_avg)]
    groups = [float(np.mean([singles[nread_max * m + j]
                             for j in range(nread_max)]))
              for m in range(n_avg)]
    ratio = statistics.stdev(groups) / statistics.stdev(singles)
    ok11 = (AVG_WIN[0] <= ratio <= AVG_WIN[1]) if full \
        else np.isfinite(ratio)
    check("G11-sqrt-averaging", ok11,
          "P2: sigma(%d-mean)/sigma(single) = %.4f/%.4f = %.4f in "
          "%s (1/sqrt(%d) = %.3f)%s"
          % (nread_max, statistics.stdev(groups),
             statistics.stdev(singles), ratio, str(AVG_WIN),
             nread_max, 1.0 / math.sqrt(nread_max),
             "" if full else " [SMOKE-scoped]"))

    # ------------------------------------------------------------ S4
    section("S4  C2 CAPACITY SURFACE -- encode / decode / MI")
    all_msgs = list(itertools.product(range(3), repeat=K_BANDS))

    def centroids(plc: str, ei: int) -> tuple:
        ys = []
        for msg in all_msgs:
            osc = osc_base.copy()
            for b, s in enumerate(msg):
                if s:
                    osc = osc + tpl_osc[(plc, ei, b, s)]
            ys.append(y_of(osc))
        return np.array(ys), all_msgs

    def encode_read(plc: str, ei: int, msg: tuple,
                    rlist: list) -> np.ndarray:
        osc_sig = osc_base.copy()
        for b, s in enumerate(msg):
            if s:
                osc_sig = osc_sig + tpl_osc[(plc, ei, b, s)]
        ys = [y_of(osc_sig + dnoise[r]) for r in rlist]
        return np.mean(ys, axis=0)

    def decode(y: np.ndarray, cmat: np.ndarray) -> tuple:
        d = np.sum((cmat - y[None, :]) ** 2, axis=1)
        return all_msgs[int(np.argmin(d))]

    CELL = {}
    cent_cache = {}
    for pi, plc in enumerate(PLC_ORDER):
        for ei, eps in enumerate(eps_grid):
            ci = pi * n_eps + ei
            cmat, _ = centroids(plc, ei)
            cent_cache[(plc, ei)] = cmat
            tru, dec = [], []
            for m in range(n_msg):
                rng = np.random.default_rng([SEED_MSG, ci, m])
                msg = tuple(int(v) for v in rng.integers(0, 3,
                                                         K_BANDS))
                y = encode_read(plc, ei, msg, [m])
                tru.append(msg)
                dec.append(decode(y, cmat))
            mis = []
            sers = []
            for b in range(K_BANDS):
                tb = [t[b] for t in tru]
                db = [d[b] for d in dec]
                mis.append(mi_mm(tb, db))
                sers.append(float(np.mean([t != d for t, d
                                           in zip(tb, db)])))
            CELL[(plc, ei)] = dict(mis=mis, sers=sers,
                                   med=statistics.median(mis),
                                   tot=sum(mis))
    print("\n  CAPACITY SURFACE  per-band MI_MM [bits] "
          "(median | sum | mean SER)")
    for plc in PLC_ORDER:
        print("  " + plc)
        for ei, eps in enumerate(eps_grid):
            c = CELL[(plc, ei)]
            print("    eps %-7.4g MI %s | med %.3f sum %.3f | SER "
                  "%s" % (eps,
                          " ".join("%6.3f" % v for v in c["mis"]),
                          c["med"], c["tot"],
                          " ".join("%.2f" % v for v in c["sers"])))
    check("G12-capacity-surface", True,
          "DEFINITIONAL: surface above (N = %d messages/cell, "
          "exact-centroid decoder, paired noise r = m)" % n_msg)

    null_mis = {}
    null_acc = []
    for plc in PLC_ORDER:
        cmat = cent_cache[(plc, null_ei)]
        tru, dec = [], []
        for m in range(n_msg):
            rng = np.random.default_rng([SEED_NULL, m])
            msg = tuple(int(v) for v in rng.integers(0, 3, K_BANDS))
            y = y0 + dy_noise[n_msg + m]
            tru.append(msg)
            dec.append(decode(y, cmat))
        mis = []
        for b in range(K_BANDS):
            tb = [t[b] for t in tru]
            db = [d[b] for d in dec]
            mis.append(mi_mm(tb, db))
            null_acc.append(float(np.mean(
                [t == d for t, d in zip(tb, db)])))
        null_mis[plc] = mis
    pooled_acc = statistics.mean(null_acc)
    ok13 = (all(statistics.median([max(v, 0.0)
                                   for v in null_mis[p]])
                <= NULL_MI_BAR for p in PLC_ORDER)
            and NULL_ACC_WIN[0] <= pooled_acc <= NULL_ACC_WIN[1]) \
        if full else np.isfinite(pooled_acc)
    check("G13-null-control", ok13,
          "P5: null per-band MI LOW %s MID %s (median bar %.2f); "
          "pooled accuracy %.3f in %s (chance 1/3)%s"
          % (" ".join("%.3f" % v for v in null_mis["LOW"]),
             " ".join("%.3f" % v for v in null_mis["MID"]),
             NULL_MI_BAR, pooled_acc, str(NULL_ACC_WIN),
             "" if full else " [SMOKE-scoped: MM-MI too noisy at "
             "N = %d]" % n_msg))
    mi_crit = max(MI_FLOOR,
                  max(max(v, 0.0) for p in PLC_ORDER
                      for v in null_mis[p]))
    reslim = {}
    for plc in PLC_ORDER:
        reslim[plc] = next((eps_grid[ei] for ei in range(n_eps)
                            if CELL[(plc, ei)]["med"] > mi_crit),
                           None)
    check("G14-resolution-limit", True,
          "DEFINITIONAL: MI_CRIT = %.3f bits; RESLIM LOW = %s, MID "
          "= %s (grid %s; the r187 ZC scale 0.003)"
          % (mi_crit,
             str(reslim["LOW"]) if reslim["LOW"] else ">max(grid)",
             str(reslim["MID"]) if reslim["MID"] else ">max(grid)",
             str(eps_grid)))
    print("\n  ERROR-RATE vs ZERO BUDGET (per band: %d zeros x eps)"
          % M_BAND)
    for plc in PLC_ORDER:
        for ei, eps in enumerate(eps_grid):
            c = CELL[(plc, ei)]
            print("    %-4s budget %8.2f  mean SER %.3f  mean MI "
                  "%.3f  MI/budget %.4f"
                  % (plc, M_BAND * eps, statistics.mean(c["sers"]),
                     statistics.mean(c["mis"]),
                     statistics.mean(c["mis"]) / (M_BAND * eps)))
    check("G15-budget-curve", True,
          "DEFINITIONAL: curve above (budget currency %d * eps per "
          "band)" % M_BAND)

    avg_rows = []
    cmat_avg = cent_cache[("LOW", AVG_EPS_IDX)]
    for nr in nreads:
        tru, dec = [], []
        for m in range(n_avg):
            rng = np.random.default_rng([SEED_MSG, AVG_CELL_CODE, m])
            msg = tuple(int(v) for v in rng.integers(0, 3, K_BANDS))
            rlist = [base_r + nread_max * m + j for j in range(nr)]
            y = encode_read("LOW", AVG_EPS_IDX, msg, rlist)
            tru.append(msg)
            dec.append(decode(y, cmat_avg))
        mis = [mi_mm([t[b] for t in tru], [d[b] for d in dec])
               for b in range(K_BANDS)]
        avg_rows.append((nr, statistics.median(mis),
                         float(np.mean([[t[b] != d[b] for b in
                                         range(K_BANDS)]
                                        for t, d in
                                        zip(tru, dec)]))))
        print("    n_read %-3d med MI %.3f  mean SER %.3f"
              % avg_rows[-1])
    reslim_avg = avg_rows[-1][1] > mi_crit
    check("G16-averaging-decode", True,
          "DEFINITIONAL: (LOW, eps %.4g) med-band MI at n_read %s = "
          "%s; RESLIM-AVG (clears MI_CRIT %.3f at n_read %d): %s"
          % (eps_grid[AVG_EPS_IDX], str(nreads),
             " ".join("%.3f" % r[1] for r in avg_rows), mi_crit,
             nread_max, reslim_avg))

    # ------------------------------------------------------------ S5
    section("S5  C3(i) LINEARITY -- pairwise interference "
            "(noiseless)")
    nl_max = {}
    for ei, eps in enumerate(eps_grid):
        worst = 0.0
        for b1 in range(K_BANDS):
            for b2 in range(b1 + 1, K_BANDS):
                yp = y_of(osc_base + tpl_osc[("LOW", ei, b1, 1)]
                          + tpl_osc[("LOW", ei, b2, 1)]) - y0
                s1 = tpl_y[("LOW", ei, b1, 1)]
                s2 = tpl_y[("LOW", ei, b2, 1)]
                nl = float(np.linalg.norm(yp - s1 - s2)
                           / np.linalg.norm(s1 + s2))
                worst = max(worst, nl)
        nl_max[eps] = worst
        print("    eps %-7.4g max-pair NL %.4f" % (eps, worst))
    check("G17-linearity-table", True,
          "DEFINITIONAL: max-pair NL over %d LOW pairs per eps "
          "above; P4 (NL grows with eps, NL(min) < %.1f): grows %s, "
          "NL(min) = %.4f"
          % (K_BANDS * (K_BANDS - 1) // 2, NL_CRIT,
             all(nl_max[eps_grid[i + 1]] >= nl_max[eps_grid[i]]
                 for i in range(n_eps - 1)),
             nl_max[eps_grid[0]]))
    lin_scale = next((e for e in eps_grid if nl_max[e] > NL_CRIT),
                     None)
    check("G18-linearity-scale", True,
          "DEFINITIONAL: LINEARITY-SCALE = %s (NL_CRIT %.1f); "
          "regime: %s"
          % (str(lin_scale) if lin_scale else ">max(grid)", NL_CRIT,
             "INTERFERENCE-MEMORY" if lin_scale
             else "LINEAR-CODEC over the full grid"))
    ei_top = n_eps - 1
    Cb0 = float(ZS.coherence(
        gam7, us_atoms,
        ZS.synth_weights(qs, osc_base
                         + tpl_osc[("LOW", ei_top, 0, 1)]), z_ms))
    Cb1 = float(ZS.coherence(
        gam7, us_atoms,
        ZS.synth_weights(qs, osc_base
                         + tpl_osc[("LOW", ei_top, 1, 1)]), z_ms))
    Cbb = float(ZS.coherence(
        gam7, us_atoms,
        ZS.synth_weights(qs, osc_base
                         + tpl_osc[("LOW", ei_top, 0, 1)]
                         + tpl_osc[("LOW", ei_top, 1, 1)]), z_ms))
    nonadd_c = (Cbb - C_Z0) - (Cb0 - C_Z0) - (Cb1 - C_Z0)
    check("G19-r190-continuity", True,
          "DEFINITIONAL: global-C nonadditivity of LOW bands 0 & 1 "
          "at eps %.4g: dC set %+0.4f vs sum singles %+0.4f -> "
          "nonadd %+0.4f (r190 measured +5.32 at off-line delta "
          "0.4)" % (eps_grid[ei_top], Cbb - C_Z0,
                    (Cb0 - C_Z0) + (Cb1 - C_Z0), nonadd_c))

    # ------------------------------------------------------------ S6
    section("S6  C3(ii) REDUNDANCY -- parity code + erasure "
            "correction")
    era_ei = n_eps + ERA_EPS_IDX if ERA_EPS_IDX < 0 else ERA_EPS_IDX
    cmat_era = cent_cache[("LOW", era_ei)]
    n_rec = 0
    n_dir = 0
    for m in range(n_era):
        rng = np.random.default_rng([SEED_ERA_MSG, m])
        infosym = [int(v) for v in rng.integers(0, 3, K_BANDS - 1)]
        msg = tuple(infosym + [sum(infosym) % 3])
        e = m % K_BANDS
        rngc = np.random.default_rng([SEED_ERA_SYM, m])
        corr = int(rngc.integers(0, 3))
        tx = list(msg)
        tx[e] = corr
        y = encode_read("LOW", era_ei, tuple(tx), [m])
        dec = decode(y, cmat_era)
        if e == K_BANDS - 1:
            rest = sum(dec[b] for b in range(K_BANDS - 1)) % 3
        else:
            rest = (dec[K_BANDS - 1]
                    - sum(dec[b] for b in range(K_BANDS - 1)
                          if b != e)) % 3
        n_rec += int(rest == msg[e])
        n_dir += int(dec[e] == tx[e])
    rate = n_rec / float(n_era)
    era_bar = 1.0 / 3.0 + 3.0 * math.sqrt(2.0 / 9.0 / n_era)
    check("G20-erasure-construction", True,
          "DEFINITIONAL: parity sub-codebook at (LOW, eps %.4g), %d "
          "coded messages, erased band = m mod %d, corrupt symbol "
          "seeded; direct decode of the TRANSMITTED corrupted "
          "symbol: %.3f" % (eps_grid[era_ei], n_era, K_BANDS,
                            n_dir / float(n_era)))
    check("G21-erasure-recovery", True,
          "DEFINITIONAL: parity recovery of the INTENDED erased "
          "symbol = %.3f (chance 1/3; significance bar %.4f) -> "
          "REDUNDANT-DISTRIBUTED: %s"
          % (rate, era_bar, rate >= era_bar))

    # ------------------------------------------------------------ S7
    section("S7  C3(iii) ASYMMETRY -- LOW vs MID channel gain")
    ratios = []
    for ei, eps in enumerate(eps_grid):
        nl_ = statistics.mean(
            tpl_norm[("LOW", ei, b, s)]
            for b in range(K_BANDS) for s in (1, 2))
        nm_ = statistics.mean(
            tpl_norm[("MID", ei, b, s)]
            for b in range(K_BANDS) for s in (1, 2))
        ratios.append(nm_ / nl_)
        print("    eps %-7.4g mean||t|| LOW %.4f MID %.4f  ratio "
              "%.3f" % (eps, nl_, nm_, ratios[-1]))
    gain = statistics.mean(ratios)
    if gain >= GAIN_HI:
        gain_tok = "CHANNEL-GAIN-MID>LOW"
    elif gain <= GAIN_LO:
        gain_tok = "CHANNEL-GAIN-LOW>MID"
    else:
        gain_tok = "CHANNEL-GAIN-FLAT"
    check("G22-asymmetry-gain", True,
          "DEFINITIONAL: mean MID/LOW template-norm ratio %.3f "
          "(bars %.2f / %.2f) -> %s (P3 expected MID > LOW from the "
          "r190 leverage law)" % (gain, GAIN_HI, GAIN_LO, gain_tok))
    check("G23-asymmetry-mi", True,
          "DEFINITIONAL: MI totals per eps LOW %s vs MID %s"
          % (" ".join("%.2f" % CELL[("LOW", ei)]["tot"]
                      for ei in range(n_eps)),
             " ".join("%.2f" % CELL[("MID", ei)]["tot"]
                      for ei in range(n_eps))))

    # ------------------------------------------------------------ S8
    section("S8  C4 DEPTH PARITY + LOOP GUARD + TAXONOMY")
    t0 = time.time()
    F_sub = ZS.osc_dens(gbig[n_alt: n_d2], us_ep)
    F_alt = F_base - F_sub
    osc_alt = ZS.weights_from_dens(qs, F_alt[:na], F_alt[na:])
    C_Z0_alt = float(ZS.coherence(
        gam7, us_atoms, ZS.synth_weights(qs, osc_alt), z_ms))
    y0_alt = y_of(osc_alt)
    t_alt = y_of(osc_alt + tpl_osc[("LOW", ei_top, 0, 1)]) - y0_alt
    t_ref = tpl_y[("LOW", ei_top, 0, 1)]
    corr_t = float(np.corrcoef(t_alt, t_ref)[0, 1])
    nr_t = float(np.linalg.norm(t_alt) / np.linalg.norm(t_ref))
    info("alt-depth pass: %.0f s" % (time.time() - t0))
    ok24 = abs(C_Z0_alt - C_Z0) <= Z0_DEPTH_TOL
    check("G24-depth-z0-sanity", ok24,
          "|C_Z0(depth %d) - C_Z0(depth %d)| = %.6f <= %.2f (r187 "
          "tail law measured 0.0011)"
          % (n_alt, n_d2, abs(C_Z0_alt - C_Z0), Z0_DEPTH_TOL))
    ok25 = (corr_t >= DEPTH_CORR_MIN
            and DEPTH_NORM_WIN[0] <= nr_t <= DEPTH_NORM_WIN[1])
    check("G25-depth-template-stability", ok25,
          "template (LOW, band 0, eps %.4g, +) at depth %d vs %d: "
          "corr %.6f >= %.1f, norm ratio %.4f in %s"
          % (eps_grid[ei_top], n_alt, n_d2, corr_t, DEPTH_CORR_MIN,
             nr_t, str(DEPTH_NORM_WIN)))

    dep = {"CHANNEL-VERDICT": ("R187-ENGINE",
                               "CONTROLLED-CONFIGURATIONS"),
           "R187-ENGINE": ("EXPLICIT-FORMULA-FORM", "CENSUS-AS-DATA",
                           "CACHE-WARD", "DETECTOR-PORTS"),
           "CONTROLLED-CONFIGURATIONS": ("CENSUS-AS-DATA",),
           "EXPLICIT-FORMULA-FORM": (), "CENSUS-AS-DATA": (),
           "CACHE-WARD": (), "DETECTOR-PORTS": (),
           "ZERO-VERIF-AS-HYP": (), "RH-GRANT": (),
           "POSITIVITY-FROM-CENSUS": ("ZERO-VERIF-AS-HYP",
                                      "RH-GRANT")}

    def ancestors(node):
        seen = set()
        stack = [node]
        while stack:
            nn = stack.pop()
            for p in dep.get(nn, ()):
                if p not in seen:
                    seen.add(p)
                    stack.append(p)
        return seen

    banned = {"ZERO-VERIF-AS-HYP", "RH-GRANT"}
    ok26 = not (ancestors("CHANNEL-VERDICT") & banned)
    check("G26-loop-guard", ok26,
          "delivered ancestors clean: CENSUS-AS-DATA (control "
          "construction, Epstein class) is NOT ZERO-VERIF-AS-HYP; "
          "no census-forall-k, no A_0-triangle, no RH-conditional "
          "second moment consumed anywhere")

    degenerate = all(CELL[(p, ei)]["med"] <= mi_crit
                     for p in PLC_ORDER for ei in range(n_eps))
    if degenerate:
        taxonomy = "CHANNEL-DEGENERATE"
        code_toks = []
    else:
        taxonomy = ("CHANNEL-CHARACTERIZED(RESLIM LOW %s / MID %s; "
                    "LINEARITY-SCALE %s)"
                    % (str(reslim["LOW"]) if reslim["LOW"]
                       else ">max", str(reslim["MID"])
                       if reslim["MID"] else ">max",
                       str(lin_scale) if lin_scale else ">max"))
        code_toks = ["CODE-STRUCTURE-INTERFERENCE-MEMORY"
                     if lin_scale else "CODE-STRUCTURE-LINEAR-CODEC"]
        if rate >= era_bar:
            code_toks.append("CODE-STRUCTURE-REDUNDANT-DISTRIBUTED")
        code_toks.append(gain_tok)
    check("G27-taxonomy", True,
          "DEFINITIONAL: %s%s (instrument characterization only; "
          "the round-107 CODE-READING-TRUE-DECODING-DIRECTION "
          "verdict is cited context, NOT upgraded)"
          % (taxonomy,
             (" + " + " + ".join(code_toks)) if code_toks else ""))

    rt = time.time() - T0_WALL
    check("G28-runtime", rt <= RUNTIME_BAR,
          "runtime %.1f s <= %.0f s" % (rt, RUNTIME_BAR))
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    ntot = len(CHECKS)
    tokens = [taxonomy] + code_toks
    tokens.append("RESLIM-AVG(%s@%.4g)" % (reslim_avg,
                                           eps_grid[AVG_EPS_IDX]))
    tokens.append("MI-CRIT(%.3f)" % mi_crit)
    tokens += ["NO-RH-CLAIM", "NO-STORAGE-CLAIM",
               "NO-ARITHMETIC-NOVELTY-CLAIM"]
    print("\n" + "=" * 78)
    print("GATES: %d/%d PASS" % (npass, ntot))
    print("COMPOSITE VERDICT: " + " + ".join(tokens))
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("RUNTIME %.1f s" % rt)
    print("=" * 78)
    hard_fails = [nm for nm, ok, _d in CHECKS if not ok]
    return 0 if not hard_fails else 1


if __name__ == "__main__":
    sys.exit(main())
