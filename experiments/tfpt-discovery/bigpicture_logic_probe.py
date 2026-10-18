#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""bigpicture_logic_probe -- PRIME.BIGPICTURE.LOGIC.01

FROZEN SPEC (2026-08-15).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim about zeta.  It closes no gate and narrows no
gate.  It is a FOUNDATIONS AUDIT of the campaign's own logical
architecture: the joints between the grand claims, typed and warded.

=======================================================================
MISSION (the six joints)
=======================================================================
J1  THE THREE-FORMS EQUIVALENCE QUESTION (the headline).  The corpus
    says the one open input holds "three equivalent lemma forms"
    (uniform Weyl-disk contraction; ground-eigenvector sign positions;
    Hausdorff cell positivity).  Type EVERY direction of every form's
    relation to RH, decide whether the mutual equivalences are direct
    or RH-routed, and answer: CAN PARTIAL (FINITE) RESULTS TRANSFER
    BETWEEN FORMS?  The answer is demonstrated numerically with an
    explicit counterexample world (a synthetic zero configuration that
    keeps one instrument positive while another fires).
J2  THE OCT VOCABULARY BOUNDARY.  The Obstruction Completeness
    Theorem's clause (ii) ("no blanket-untested class left") is
    completeness OVER THE CORPUS VOCABULARY.  Enumerate structural
    argument classes never in that vocabulary, verify their absence
    from the atlas artifacts by machine (absence gates), and type each
    honestly (UNPRICED / REDUCES / NO-KNOWN-EXPORT).
J3  THE LOCALIZATION LATTICE.  "Localized Weil positivity" names a
    FAMILY of statements with different test classes and quantifier
    structures (one-a Hausdorff / all-a screw sections / cofinal-mesh
    wall / per-n CCM tents / Euler--Pick nodes).  Build the lattice,
    ward every claimed arrow, and prove (by explicit counterexample)
    that mesh-monotonicity of section positivity is FALSE in general
    -- confirming that the corpus's own cofinal correction was
    load-bearing, not pedantic.
J4  THE FALSIFICATION ASYMMETRY.  Both certified instruments are
    DISPROOF-SOUND (a certified negative would contradict RH through
    the forward direction alone) but REACH-CAPPED: their certified
    slices see off-line zeros only in territory classical verification
    (Platt--Trudgian 2021, T = 3.000175e12) closed long ago.  Type the
    true two-sided epistemic reach per instrument and demonstrate the
    blindness/firing dichotomy numerically in the synthetic world.
J5  THE DESCENT CHAIN (roadmap Stage 3).  Enumerate every link from
    the Stage-2 interface to RH per entry form and find the weakest.
    Key structural fact: the only kernel-checked end-to-end extraction
    (v848 + CofinalWeil.lean) consumes the WALL form (H_cof), which is
    NOT one of the three entry forms and is not producible from them
    by any corpus arrow short of RH itself.
J6  THE HOSTILE-REFEREE SWEEP.  The load-bearing sentences of the
    abstract/late sections that could not be grounded verbatim, each
    typed with its correction.

=======================================================================
METHOD
=======================================================================
(1) GREP WARDS: every per-edge status assertion is warded by a
    whitespace-normalized substring that must appear in the owning
    frozen artifact (paper body, frozen probe, Lean module, or
    verification module).  A ward failure fails the probe.
(2) RECOMPUTE WARDS: the Euler--Pick N=1 floor and the N<=4 ladder
    are recomputed from mpmath's zeta (declared: this logic probe is
    NOT source-only; it may consume zeta as an oracle because it
    certifies the AUDIT, not the mathematics), and the Hausdorff
    cells n+k<=6 at a=256 are recomputed from high-order derivatives.
(3) COUNTEREXAMPLE WORLDS (all synthetic; no claim about zeta):
    W0  an on-line comb (RvM quantiles, M pairs)          -- control;
    W1  W0 + one off-line quadruple ABOVE gamma_1         -- the
        transfer/blindness world: Hausdorff field stays positive at
        every computed depth while the Euler--Pick matrix acquires a
        certified negative pivot at small N;
    W2  W0 + one off-line quadruple BELOW gamma_1         -- the
        fires-iff-can control: the Hausdorff n-channel flips sign.
(4) MESH COUNTEREXAMPLE: an explicit continuous kernel whose
    Toeplitz sections at mesh delta are PSD at EVERY size while a
    section at mesh delta/2 is indefinite (aliasing) -- mesh
    monotonicity (coarse => fine) is FALSE in general; fine => coarse
    is trivially TRUE on nested lattices (verified).
(5) DAG GATES: the J1/J3/J5 implication graphs are data structures;
    a closure computation asserts that RH is NOT reachable from TRUE
    through proven edges (any TRUE->RH path must cross an OPEN edge)
    -- if this gate ever fails, the corpus would contain an RH proof
    claim, which it forbids.

FIREWALL / SCOPE: exploration only; synthetic worlds carry no
information about zeta's actual zeros; mpmath zeta is used only for
recompute wards of published enclosure values; nothing here is
evidence for or against RH.  NO RH claim.
"""

import hashlib
import math
import re
import sys
import time

import numpy as np
import mpmath as mp

T0 = time.time()

# ---------------------------------------------------------------- spec
FROZEN_SPEC = """\
PRIME.BIGPICTURE.LOGIC.01 spec v1 (2026-08-15, frozen before the
run of record).  J1 forms = {HAUS_ALL (one a=256), SCREW_ALL_A,
EP_ALL_N, WEYL_CONTRACTION, SIGN_POSITIONS, H_COF}; per-direction
status in {KERNEL, CLASSICAL, PROBE+CLASSICAL, CERTIFIED-FINITE,
MEASURED, OPEN}; gate G-DAG: RH unreachable from TRUE via proven
edges; gate G-EQ: two-sided (citation-grade) forms == {HAUS_ALL,
SCREW_ALL_A, EP_ALL_N}, one-sided == {WEYL_CONTRACTION,
SIGN_POSITIONS, H_COF}; gate G-TRANSFER: the only direct
inter-currency edge is the (AC) weld EP <-> Weil-on-exp-cone; no
finite-to-finite transfer edge exists in the corpus.  Worlds:
M = 400 RvM-quantile pairs; W1 off-line quadruple gamma = 20,
delta = 0.30; W2 gamma = 5, delta = 0.49; safe point a = 256;
Hausdorff depth n+k <= 50 (W1/W0), n <= 240 k = 0 (W2); Euler-Pick
SV nodes sigma_j = 1 + 1/j, N <= 24, LDLT at dps 200, fire = first
negative pivot.  Mesh counterexample k(t) = cos t - 0.6 cos((1+2pi)t),
coarse delta = 1.0 (PSD to size 48), fine delta = 0.5 (indefinite by
size 48).  Recompute wards: EP N=1 in [4.5917135e-2, 4.5917136e-2];
EP N=4 lambda_min in [8.278338e-15, 1.3840906e-14]; Hausdorff true
cells n+k <= 6 at a = 256 all positive.  J2 absence gates: the atlas
artifact set must NOT contain {o-minimal, ergodic, multiplicative
chaos, Fyodorov, unique ergodicity, functoriality} (case-insensitive).
Composite verdict = BIGPICTURE-FINDINGS(n_fundamental) with the
fundamental findings named; gates N/N required for a valid audit.
"""
SPEC_SHA = hashlib.sha256(FROZEN_SPEC.encode()).hexdigest()[:16]

CHECKS = []
FAILS = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    tag = "PASS" if ok else "FAIL"
    if not ok:
        FAILS.append(name)
    print("  [%s] %s%s" % (tag, name, (" -- " + detail) if detail else ""))


def section(title):
    print("\n" + "=" * 72 + "\n" + title + "\n" + "=" * 72)


# ------------------------------------------------------------ file I/O
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
assert os.path.exists(os.path.join(ROOT, "tfpt_prime_front.tex")), ROOT

PATHS = {
    "P":    "tfpt_prime_front.tex",
    "HAUS": "experiments/tfpt-discovery/hausdorff_safepoint_probe.py",
    "KREIN": "experiments/tfpt-discovery/krein_screw_realization_probe.py",
    "SVPIN": "experiments/tfpt-discovery/stieltjes_vitali_pin_probe.py",
    "VBK":  "experiments/tfpt-discovery/vbk_invariant_probe.py",
    "MOON": "experiments/tfpt-discovery/moonshot_sol_probe.py",
    "ROAD": "experiments/tfpt-discovery/roadmap_probe.py",
    "ATLAS": "experiments/tfpt-discovery/kill_atlas_dag_probe.py",
    "LEV":  "experiments/tfpt-discovery/levinson_class_probe.py",
    "ARB":  "experiments/tfpt-discovery/realroot_arbiter_probe.py",
    "EPLAD": "experiments/tfpt-discovery/eulerpick_ladder_probe.py",
    "SIEVE4": "experiments/tfpt-discovery/sieve4_eulerpick_n4_probe.py",
    "SCREWIND": "experiments/tfpt-discovery/screwind_induction_probe.py",
    "SPEXP": "experiments/tfpt-discovery/sp_expsum_pricing_probe.py",
    "COHOM": "experiments/tfpt-discovery/cohomspec_probe.py",
    "V848": "verification/v848_extraction_chain.py",
    "V912": "verification/v912_form_convergence_theorem.py",
    "V913": "verification/v913_signed_alignment_localization.py",
    "LCW":  "experiments/lean4-carrier-rigidity/TfptCarrier/CofinalWeil.lean",
    "LCP":  "experiments/lean4-carrier-rigidity/TfptCarrier/CofinalPredefinition.lean",
    "LSV":  "experiments/lean4-carrier-rigidity/TfptCarrier/SVSkeleton.lean",
    "LEP":  "experiments/lean4-carrier-rigidity/TfptCarrier/EulerPick.lean",
    "UNTESTED": "experiments/tfpt-discovery/untested_sign_sources_probe.py",
    "SAT":  "experiments/tfpt-discovery/sat_projection_alignment_probe.py",
    "BIRD": "experiments/tfpt-discovery/birdseye_shape_freedom_probe.py",
}

_CACHE = {}


def _text(key):
    if key not in _CACHE:
        with open(os.path.join(ROOT, PATHS[key]), encoding="utf-8",
                  errors="replace") as fh:
            _CACHE[key] = re.sub(r"\s+", " ", fh.read())
    return _CACHE[key]


def ward(key, token):
    """Whitespace-normalized substring ward against a frozen artifact."""
    return re.sub(r"\s+", " ", token) in _text(key)


# =====================================================================
section("J1  THE FORM-EQUIVALENCE GRAPH (per-edge status, warded)")
# =====================================================================
# Statements (exact quantifiers):
#   RH          : all nontrivial zeros on Re = 1/2.
#   HAUS_ALL    : C_{n,k}(256) >= 0 for ALL n,k >= 0 (ONE safe point).
#   SCREW_ALL_A : every finite section of the accelerant -g'' positive,
#                 for EVERY window depth a (continuum screw property).
#   EP_ALL_N    : pickMatrix P_N >= 0 at SV nodes for EVERY N.
#   WEYL_CONTR  : the Weyl disks of the Krein realization contract to
#                 the point xi'/xi(1/2+sigma) (the round-90 lemma's
#                 CONCLUSION, i.e. Form B as written in the paper).
#   SIGN_POS    : TPL(i) / ground-eigenvector sign positions (Form C).
#   H_COF       : positivity of the predeclared wall family at every
#                 rung, cofinal in the mesh-refinement order (E4).
# Statuses: KERNEL / CLASSICAL / PROBE+CLASSICAL / CERTIFIED-FINITE /
#           MEASURED / OPEN.
PROVEN = {"KERNEL", "CLASSICAL", "PROBE+CLASSICAL", "CERTIFIED-FINITE"}

EDGES = [
    # (src, dst, status, ward_key, ward_token, note)
    ("RH", "HAUS_ALL", "CLASSICAL", "HAUS",
     "CLAIMED THEOREM: RH <=> C_{n,k}(a) >= 0 for all n, k >= 0",
     "forward: under RH every summand is >= 0 (genus-0 pair expansion,"
     " cited); quantifier-free per cell"),
    ("HAUS_ALL", "RH", "PROBE+CLASSICAL", "HAUS",
     "Widder, The Laplace Transform 1941",
     "backward: Hausdorff/Widder moment theorem + no-atom-at-0 +"
     " identity-theorem continuation; skeleton gated 40/40"),
    ("RH", "SCREW_ALL_A", "CLASSICAL", "KREIN",
     "all-a version is Suzuki's RH-equivalence and is NOT assumed",
     "Suzuki: g screw on R <=> RH (cited both ways; corpus never"
     " assumes it)"),
    ("SCREW_ALL_A", "RH", "CLASSICAL", "KREIN",
     "all-a version is Suzuki's RH-equivalence and is NOT assumed",
     "same citation, reverse direction"),
    ("RH", "EP_ALL_N", "KERNEL", "LEP",
     "pickMatrix_posSemidef",
     "forward: real ordinates => PSD, kernel-checked for finite"
     " families; identification P = xi'/xi cited"),
    ("EP_ALL_N", "RH", "CLASSICAL", "VBK",
     "V0c",
     "backward: Pick 1916 + interior accumulation + identity theorem"
     " + pole contradiction (V0c, audited and pinned)"),
    ("WEYL_CONTR", "RH", "PROBE+CLASSICAL", "SVPIN",
     "SVPIN-ROUTE-OPEN",
     "contraction => (SV) => RH; skeleton sound gate by gate;"
     " sv_implies_rh Lean-packaged with cited fields"),
    ("RH", "WEYL_CONTR", "OPEN", "KREIN",
     "SUZKREIN-CARRIER-OPEN",
     "RH gives section positivity (Suzuki); positivity => contraction"
     " is EXACTLY the open round-90 lemma (limit-point behaviour is"
     " measured, not proven)"),
    ("SIGN_POS", "RH", "PROBE+CLASSICAL", "ARB",
     "R3 alone is RH-hard",
     "sign positions => TPL(i) => real-spectrum architecture =>"
     " Weil positivity => RH; skeleton audited, legs classical-cited,"
     " one named conditional (CF simplicity/evenness)"),
    ("RH", "SIGN_POS", "OPEN", "ARB",
     "Connes par. 6.6 open",
     "thinning persistence has no proof even under RH"),
    ("H_COF", "RH", "PROBE+CLASSICAL", "V848",
     "EXTRACTION-CHAIN-COMPLETE",
     "v848 + v912 (unconditional rate) + CofinalWeil.lean +"
     " E7 density leg (cited) + Weil criterion (cited)"),
    ("RH", "H_COF", "OPEN", "P",
     "uniformity as the open item",
     "RH gives the LIMIT Q_W(f) >= 0 per element; positivity of the"
     " FINITE rung forms at a mesh good for ALL rungs needs the"
     " h-uniformity the corpus calls the asymptotic mountain"),
    # certified finite regions (TRUE -> region), and their non-arrows
    ("TRUE", "HAUS_FINITE_K1E19", "CLASSICAL", "MOON",
     "MOONSHOT-PARTIAL",
     "C_{n,k}(256) > 0 for all n, k <= 1e19, from Platt-Trudgian +"
     " Rosser alone"),
    ("HAUS_FINITE_K1E19", "HAUS_ALL", "OPEN", "MOON",
     "1e19",
     "the k -> infinity quantifier is untouched (stated inside the"
     " theorem)"),
    ("TRUE", "EP_CERT_N4", "CERTIFIED-FINITE", "ROAD",
     "8.278338e-15",
     "lambda_min(P_4) certified positive at cap 1e13"),
    ("EP_CERT_N4", "EP_ALL_N", "OPEN", "ROAD",
     "KNOWLEDGE-walled",
     "N = 5 is knowledge-walled (psi beyond 1e19)"),
    ("TRUE", "HAUS_CERT_D86", "CERTIFIED-FINITE", "HAUS",
     "HAUSDORFF-CERTIFIED-DEPTH",
     "certified depth 86 (5290 cells)"),
    # the ONE direct inter-currency edge in the corpus:
    ("EP_ALL_N", "WEIL_ON_EXP_CONE", "PROBE+CLASSICAL", "VBK",
     "(AC)",
     "the (AC) weld: c^T P_N c = <-g'', f_c * ~f_c> -- Euler-Pick"
     " positivity IS Weil positivity on exponential autocorrelations"
     " (symbolic identity, gated); the only direct inter-currency"
     " bridge, and it does NOT reach tents, lattice combs, Hausdorff"
     " cells or eigenvector signs"),
]

n_ward_fail = 0
for (src, dst, st, key, tok, note) in EDGES:
    ok = ward(key, tok)
    if not ok:
        n_ward_fail += 1
        print("    MISSING WARD: %s->%s token %r in %s" % (src, dst, tok, key))
check("J1.G1 every edge's grep ward found in its owning artifact",
      n_ward_fail == 0, "%d edges warded" % len(EDGES))

# G-DAG: RH must NOT be reachable from TRUE through proven edges.
adj = {}
for (src, dst, st, *_rest) in EDGES:
    if st in PROVEN:
        adj.setdefault(src, set()).add(dst)
reach, stack = set(), ["TRUE"]
while stack:
    u = stack.pop()
    for v in adj.get(u, ()):  # noqa: B905
        if v not in reach:
            reach.add(v)
            stack.append(v)
check("J1.G2 RH is UNREACHABLE from TRUE via proven edges (no"
      " unconditional RH path hides in the corpus map)",
      "RH" not in reach, "reachable set = %s" % sorted(reach))

# G-EQ: which forms have citation-grade equivalence with RH?
fwd = {(s, d): st for (s, d, st, *_r) in EDGES}
FORMS = ["HAUS_ALL", "SCREW_ALL_A", "EP_ALL_N",
         "WEYL_CONTR", "SIGN_POS", "H_COF"]
two_sided = [f for f in FORMS
             if fwd.get((f, "RH")) in PROVEN and fwd.get(("RH", f)) in PROVEN]
one_sided = [f for f in FORMS
             if fwd.get((f, "RH")) in PROVEN and fwd.get(("RH", f)) == "OPEN"]
check("J1.G3 two-sided (citation-grade) RH-equivalences are EXACTLY"
      " {HAUS_ALL, SCREW_ALL_A, EP_ALL_N}",
      set(two_sided) == {"HAUS_ALL", "SCREW_ALL_A", "EP_ALL_N"},
      str(two_sided))
check("J1.G4 one-sided (form => RH proven, RH => form OPEN) are EXACTLY"
      " {WEYL_CONTR, SIGN_POS, H_COF}",
      set(one_sided) == {"WEYL_CONTR", "SIGN_POS", "H_COF"},
      str(one_sided))

# G-TRANSFER (structural half): no direct inter-form edge exists except
# the (AC) weld; every mutual equivalence among the two-sided forms
# routes through RH.
direct_interform = [(s, d) for (s, d, st, *_r) in EDGES
                    if s in FORMS and d in FORMS and st in PROVEN]
check("J1.G5 NO direct form-to-form edge exists in the corpus"
      " (all mutual equivalences route through RH; the (AC) weld"
      " lands on the exp-cone, not on another form)",
      direct_interform == [], str(direct_interform))
check("J1.G6 the paper's 'three equivalent lemma forms' sentence"
      " exists (the sentence under audit)",
      ward("P", "three equivalent lemma") and
      ward("P", "uniform Weyl-disk contraction") and
      ward("P", "Hausdorff cell positivity"))

print("""
  J1 TYPED RESULT (the headline):
    'three equivalent lemma forms' as printed names WEYL_CONTR,
    SIGN_POS, HAUS_ALL.  Of these only HAUS_ALL is a citation-grade
    two-sided RH equivalence; WEYL_CONTR and SIGN_POS have RH => form
    OPEN (round-90 lemma; Connes 6.6) -- they are RH-SUFFICIENT
    PENDANTS, possibly strictly stronger than RH.  The genuine
    two-sided forms in the corpus are HAUS_ALL, SCREW_ALL_A (Suzuki)
    and EP_ALL_N (Euler-Pick), and every mutual equivalence among
    them ROUTES THROUGH RH: no direct A<=>B edge exists, so partial
    (finite) progress in one currency transfers to NO other currency.
    The one direct bridge, the (AC) weld, maps finite Euler-Pick
    positivity onto Weil positivity restricted to the finite
    exponential-autocorrelation cone -- and stops there.""")

# =====================================================================
section("J1-NUM  THE TRANSFER COUNTEREXAMPLE WORLD (+ J4 dichotomy)")
# =====================================================================
A_SAFE = 256.0
M_COMB = 400
DEPTH = 50          # W0/W1 full field n+k <= DEPTH
N_ROW = 240         # W2 n-channel row length
GAMMA_OFF_HI, DELTA_OFF_HI = 20.0, 0.30     # W1: above gamma_1
GAMMA_OFF_LO, DELTA_OFF_LO = 5.0, 0.49      # W2: below gamma_1
N_EP_MAX = 24
EP_DPS = 200


def rvm_quantiles(m):
    """First m Riemann-von-Mangoldt quantiles: N(t) = j - 1/2."""
    out = []
    for j in range(1, m + 1):
        lo, hi = 2.0, 10.0
        f = lambda t: t / (2 * math.pi) * math.log(t / (2 * math.pi * math.e)) + 7.0 / 8.0 - (j - 0.5)
        while f(hi) < 0:
            hi *= 2
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            if f(mid) < 0:
                lo = mid
            else:
                hi = mid
        out.append(0.5 * (lo + hi))
    return out


GAMMAS = rvm_quantiles(M_COMB)
print("  comb: M = %d RvM quantiles, gamma_1 = %.4f, gamma_M = %.2f"
      % (M_COMB, GAMMAS[0], GAMMAS[-1]))


def z_pairs(extra=None):
    """Pair z-values: on-line z = -gamma^2 (real), plus optional
    off-line quadruple as the conjugate pair z = (delta+i gamma)^2."""
    zs = [complex(-g * g, 0.0) for g in GAMMAS]
    if extra is not None:
        d, g = extra
        z = complex(d * d - g * g, 2 * d * g)
        zs.append(z)
        zs.append(z.conjugate())
    return np.array(zs, dtype=complex)


def hausdorff_field(zs, nmax, kmax):
    """C[n,k] = sum_pairs Re( y^{n+1} (1-y)^k ), y = a/(a-z)."""
    y = A_SAFE / (A_SAFE - zs)                      # (P,)
    u = 1.0 - y
    Y = np.empty((len(zs), nmax + 1), dtype=complex)
    U = np.empty((len(zs), kmax + 1), dtype=complex)
    Y[:, 0] = y
    for n in range(1, nmax + 1):
        Y[:, n] = Y[:, n - 1] * y
    U[:, 0] = 1.0
    for k in range(1, kmax + 1):
        U[:, k] = U[:, k - 1] * u
    return np.real(Y.T @ U)                          # (nmax+1, kmax+1)


# --- W0 control: all cells positive
C0 = hausdorff_field(z_pairs(), DEPTH, DEPTH)
mask = np.add.outer(np.arange(DEPTH + 1), np.arange(DEPTH + 1)) <= DEPTH
w0_min = float(C0[mask].min())
check("J1.N1 W0 (on-line comb): all Hausdorff cells n+k <= %d positive"
      % DEPTH, w0_min > 0, "min cell %.3e" % w0_min)

# --- W1 blindness: off-line ABOVE gamma_1, field stays positive
C1 = hausdorff_field(z_pairs((DELTA_OFF_HI, GAMMA_OFF_HI)), DEPTH, DEPTH)
w1_min = float(C1[mask].min())
check("J1.N2 W1 (off-line at gamma=%.0f > gamma_1, delta=%.2f): ALL"
      " Hausdorff cells n+k <= %d STAY positive (the blindness law"
      " in action)" % (GAMMA_OFF_HI, DELTA_OFF_HI, DEPTH),
      w1_min > 0, "min cell %.3e" % w1_min)
# and the n-channel stays positive far deeper:
b_row_w1 = hausdorff_field(z_pairs((DELTA_OFF_HI, GAMMA_OFF_HI)),
                           N_ROW, 0)[:, 0]
check("J1.N3 W1 n-channel b_n positive through n = %d (|y_off| < y_1:"
      " dominated forever -- no depth ever fires)" % N_ROW,
      float(b_row_w1.min()) > 0, "min b_n %.3e" % float(b_row_w1.min()))

# --- W2 fires-iff-can: off-line BELOW gamma_1 flips the n-channel
b_row_w2 = hausdorff_field(z_pairs((DELTA_OFF_LO, GAMMA_OFF_LO)),
                           N_ROW, 0)[:, 0]
neg_idx = np.where(b_row_w2 < 0)[0]
check("J1.N4 W2 (off-line at gamma=%.0f < gamma_1, delta=%.2f): the"
      " Hausdorff n-channel FIRES (first negative b_n at n = %s)"
      % (GAMMA_OFF_LO, DELTA_OFF_LO,
         str(int(neg_idx[0])) if len(neg_idx) else "NONE"),
      len(neg_idx) > 0)

# --- Euler-Pick on the same worlds (mpmath LDLT, exact-sign pivots)
mp.mp.dps = EP_DPS


def ep_pins(zs_np, sigmas):
    """P(sigma) = 2 sigma * sum_pairs Re(1/(sigma^2 - z)) in mpmath."""
    zs = [mp.mpc(z.real, z.imag) for z in zs_np]
    out = []
    for s in sigmas:
        s2 = s * s
        tot = mp.mpf(0)
        for z in zs:
            tot += mp.re(1 / (s2 - z))
        out.append(2 * s * tot)
    return out


def ldlt_pivots(Mm):
    """Symmetric LDLT without pivoting; returns the diagonal pivots."""
    n = Mm.rows
    A = Mm.copy()
    piv = []
    for k in range(n):
        d = A[k, k]
        piv.append(d)
        if d == 0:
            break
        for i in range(k + 1, n):
            lik = A[i, k] / d
            for j in range(k + 1, i + 1):
                A[i, j] -= lik * A[j, k]
        # (lower triangle only; symmetric access via A[j,k])
    return piv


def ep_first_negative(zs_np, nmax):
    sigmas = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, nmax + 1)]
    pins = ep_pins(zs_np, sigmas)
    Mfull = mp.matrix(nmax, nmax)
    for i in range(nmax):
        for j in range(nmax):
            Mfull[i, j] = (pins[i] + pins[j]) / (sigmas[i] + sigmas[j])
    piv = ldlt_pivots(Mfull)
    for k, p in enumerate(piv):
        if p < 0:
            return k + 1, p
    return None, min(piv)


t_ep = time.time()
n0_fire, p0 = ep_first_negative(z_pairs(), N_EP_MAX)
check("J1.N5 W0 Euler-Pick sections PSD through N = %d (matches the"
      " kernel-checked forward theorem pickMatrix_posSemidef)"
      % N_EP_MAX, n0_fire is None, "min pivot %s" % mp.nstr(p0, 6))
n1_fire, p1 = ep_first_negative(z_pairs((DELTA_OFF_HI, GAMMA_OFF_HI)),
                                N_EP_MAX)
check("J1.N6 W1 Euler-Pick FIRES: negative pivot at N = %s <= %d"
      " (same world in which the Hausdorff field is positive at"
      " every computed depth)" % (str(n1_fire), N_EP_MAX),
      n1_fire is not None,
      "pivot %s (LDLT dps %d), %.1f s" % (mp.nstr(p1, 6), EP_DPS,
                                          time.time() - t_ep))

check("J1.N7 TRANSFER-NONE demonstrated: W1 has every Hausdorff cell"
      " (n+k <= %d, and b_n to n = %d) positive while an Euler-Pick"
      " section is indefinite -- no map 'Hausdorff depth d => EP"
      " positivity to N(d)' with N(%d) >= %s can exist; combined with"
      " the blindness law (J1.N3: NO depth fires above gamma_1) no"
      " depth-to-depth transfer exists at all"
      % (DEPTH, N_ROW, DEPTH, str(n1_fire)),
      (w1_min > 0) and (float(b_row_w1.min()) > 0)
      and (n1_fire is not None))

# --- recompute wards against published enclosures (true source)
mp.mp.dps = 60


def xilog(s):
    return (1 / s + 1 / (s - 1) - mp.log(mp.pi) / 2
            + mp.digamma(s / 2) / 2 + mp.zeta(s, derivative=1) / mp.zeta(s))


P1 = xilog(mp.mpf("2.5")) / 2
check("J1.N8 recompute ward: true-source Euler-Pick N=1 value in the"
      " published certified floor [4.5917135e-2, 4.5917136e-2]",
      mp.mpf("4.5917135e-2") <= P1 <= mp.mpf("4.5917136e-2"),
      mp.nstr(P1, 12))

sig4 = [mp.mpf(1) + mp.mpf(1) / j for j in range(1, 5)]
pins4 = [xilog(mp.mpf("0.5") + s) for s in sig4]
M4 = mp.matrix(4, 4)
for i in range(4):
    for j in range(4):
        M4[i, j] = (pins4[i] + pins4[j]) / (sig4[i] + sig4[j])
ev4 = mp.eigsy(M4, eigvals_only=True)
lam4 = min(ev4)
check("J1.N9 recompute ward: true-source lambda_min(P_4) inside the"
      " round-100 certified enclosure [8.278338e-15, 1.3840906e-14]",
      mp.mpf("8.278338e-15") * (1 - mp.mpf("1e-6")) <= lam4
      <= mp.mpf("1.3840906e-14") * (1 + mp.mpf("1e-6")),
      mp.nstr(lam4, 10))

# --- Hausdorff true-source small cells (mp.diff of F at a = 256)
F = lambda z: xilog(mp.mpf("0.5") + mp.sqrt(z)) / (2 * mp.sqrt(z))
a = mp.mpf(256)
bvals = []
for n in range(0, 7):
    d = mp.diff(F, a, n)
    bvals.append(a ** (n + 1) * (-1) ** n / mp.factorial(n) * d)
cells_ok, worst = True, None
for n in range(0, 7):
    for k in range(0, 7 - n):
        c = mp.mpf(0)
        for i in range(k + 1):
            c += (-1) ** i * mp.binomial(k, i) * bvals[n + i]
        if worst is None or c < worst:
            worst = c
        if c <= 0:
            cells_ok = False
check("J1.N10 recompute ward: true-source Hausdorff cells n+k <= 6 at"
      " a = 256 all positive (matches the frozen probe's 561/561"
      " region)", cells_ok, "min cell %s" % mp.nstr(worst, 8))

# =====================================================================
section("J3  THE LOCALIZATION LATTICE (family, not a single statement)")
# =====================================================================
LOCALIZATIONS = {
    "WEIL_FULL":   "Q_W(f) >= 0 for the FULL admissible even compact"
                   " BV class (Weil's criterion; <=> RH, cited)",
    "H_COF":       "wall: predeclared tent family, window [0,17/4],"
                   " EVERY rung, meshes COFINAL in D_j = 2^-j",
    "SCREW_ALL_A": "screw: every finite section of -g'', EVERY depth a"
                   " (continuum kernel; Suzuki <=> RH)",
    "CCM_PN":      "CCM P(n): tent class on [1,n], per n an"
                   " infinite-dimensional cone, ALL n <=> RH (cited)",
    "HAUS_ALL":    "Hausdorff: ALL (n,k) at ONE safe point a = 256",
    "EP_ALL_N":    "Euler-Pick: exponential autocorrelations at the SV"
                   " nodes, ALL N",
}
LATTICE_WARDS = [
    ("V912 density leg is scoped to the WALL topology only", "V912",
     "density of the dyadic"),
    ("v848 carries the corrected mesh-cofinal quantifier", "V848",
     "cofinal IN THE MESH-REFINEMENT ORDER"),
    ("paper carries the E4 mesh-order correction", "P",
     "corrected its statement (mesh order)"),
    ("CCM P(n) typed as localized Weil positivity (paper)", "P",
     "localized Weil positivity"),
    ("screw hypothesis typed as localized Weil positivity (probe)",
     "KREIN", "localized Weil"),
    ("Hausdorff route carries its OWN completion leg (Widder), not E7",
     "HAUS", "Widder"),
    ("SVPIN route carries its OWN completion leg (Pick/Vitali), not E7",
     "SVPIN", "Vitali"),
]
lw_fail = 0
for (nm, key, tok) in LATTICE_WARDS:
    if not ward(key, tok):
        lw_fail += 1
        print("    MISSING LATTICE WARD: %s (%r in %s)" % (nm, tok, key))
check("J3.G1 all lattice wards found (%d)" % len(LATTICE_WARDS),
      lw_fail == 0)

# mesh-monotonicity counterexample: coarse-PSD-all-sizes, fine-indefinite
W1_, W2_, B_ = 1.0, 1.0 + 2 * math.pi, 0.6
kfun = lambda t: math.cos(W1_ * t) - B_ * math.cos(W2_ * t)
SZ = 48
coarse = np.array([kfun(j * 1.0) for j in range(SZ)])
fine = np.array([kfun(j * 0.5) for j in range(SZ)])
from scipy.linalg import toeplitz, eigvalsh  # noqa: E402

lam_coarse = min(float(eigvalsh(toeplitz(coarse[:m]))[0])
                 for m in range(2, SZ + 1))
lam_fine = float(eigvalsh(toeplitz(fine))[0])
check("J3.G2 MESH-MONOTONICITY-FALSE: k(t) = cos t - 0.6 cos((1+2pi)t)"
      " has ALL Toeplitz sections at mesh 1.0 PSD (aliasing hides the"
      " negative mass) while the mesh-0.5 section is indefinite",
      lam_coarse > -1e-10 and lam_fine < -0.05,
      "coarse min eig %.2e (sizes 2..%d), fine min eig %.3f"
      % (lam_coarse, SZ, lam_fine))
# fine => coarse on nested lattices IS monotone (principal submatrix):
psd_fine = np.array([math.exp(-abs(j * 0.5)) for j in range(SZ)])
sub = psd_fine[::2][: SZ // 2]
lam_f = float(eigvalsh(toeplitz(psd_fine))[0])
lam_c = float(eigvalsh(toeplitz(sub))[0])
check("J3.G3 fine => coarse IS monotone on nested lattices (principal"
      " submatrix), i.e. the corpus's cofinal-refinement phrasing is"
      " the correct quantifier", lam_f > -1e-12 and lam_c >= lam_f - 1e-12,
      "fine %.2e, coarse %.2e" % (lam_f, lam_c))

print("""
  J3 TYPED RESULT: 'localized Weil positivity' is a FAMILY of six
  inequivalent localizations with DIFFERENT quantifier structures
  (one-a / all-a / cofinal-mesh / per-n / all-N).  Proven arrows:
  WEIL_FULL => each localization (restriction; trivial); each
  localization => RH only through its OWN completion leg (E7 density
  for the wall; Widder for Hausdorff; Pick for the pins; CCM's own
  reduction for P(n)) -- there is NO shared completion leg and NO
  proven localization-to-localization arrow.  Mesh-monotonicity
  (coarse => fine) is FALSE in general (J3.G2); the corpus's own
  mesh-cofinal correction (v848/atlas) already fences this -- no
  missing-arrow VIOLATION found in the corpus prose, but the umbrella
  phrase 'the same single input' is accurate only up to RH-routing.""")

# =====================================================================
section("J4  TWO-SIDED INSTRUMENT REACH (disproof-sound, reach-capped)")
# =====================================================================
INSTRUMENTS = [
    {"name": "Euler-Pick certified ladder (N <= 4)",
     "disproof_dir": "KERNEL (forward: real ordinates => PSD;"
                     " certified hi < 0 would contradict RH)",
     "confirm_dir": "NONE (finite N says nothing about RH)",
     "offline_reach": "gamma ~ 5-8 at certified N (detection law"
                      " N*(delta) = 6.1 + 1.95 log10(1/delta);"
                      " gamma-reach costs O(gamma) rungs)",
     "cap": 8.0,
     "wards": [("EPLAD", "EULERPICK-CERTIFIED"),
               ("P", "territory classical verification closed decades ago")]},
    {"name": "Hausdorff Pascal field (certified depth 86, a = 256)",
     "disproof_dir": "PROBE+CLASSICAL (forward: RH => every cell a"
                     " positive sum -- summand-wise, no uniformity)",
     "confirm_dir": "NONE (finite depth says nothing about RH)",
     "offline_reach": "gamma < gamma_1 = 14.13 ONLY (provably blind"
                      " above gamma_1 at the safe point; k=0 channel,"
                      " d* ~ 1/delta)",
     "cap": 14.134725,
     "wards": [("HAUS", "HAUSDORFF-CERTIFIED-DEPTH"),
               ("P", "provably blind at the safe point")]},
    {"name": "CCM P(n) Galerkin sections (n <= 13)",
     "disproof_dir": "PROBE+CLASSICAL (certified negative section"
                     " would refute RH via CCM's reduction)",
     "confirm_dir": "NONE",
     "offline_reach": "resolution-limited margins for n >= 4",
     "cap": None,
     "wards": [("P", "a certified negative anywhere would have refuted RH")]},
]
T_PT = 3.000175332800e12    # Platt-Trudgian verified height (cited)
j4_fail = 0
for ins in INSTRUMENTS:
    for (key, tok) in ins["wards"]:
        if not ward(key, tok):
            j4_fail += 1
            print("    MISSING J4 WARD: %r in %s" % (tok, key))
check("J4.G1 all instrument wards found", j4_fail == 0)
caps_below = all(ins["cap"] is None or ins["cap"] < T_PT
                 for ins in INSTRUMENTS)
check("J4.G2 REACH CAP: every certified off-line-visibility window sits"
      " STRICTLY BELOW the classically verified height T = 3.0002e12"
      " -- given the cited Platt-Trudgian input, the certified"
      " channels are GUARANTEED empty: 'open and empty' carries zero"
      " evidential weight and zero live falsification power",
      caps_below, "caps: 8, 14.13 << 3.0e12")
check("J4.G3 the blindness/firing dichotomy is reproduced in the"
      " synthetic worlds (J1.N2/N3 blind above gamma_1; J1.N4 fires"
      " below)", (w1_min > 0) and (len(neg_idx) > 0))
print("""
  J4 TYPED RESULT: both certified instruments are DISPROOF-SOUND
  (the disproof direction consumes only the proven forward
  implication -- kernel-checked for Euler-Pick, summand-elementary
  for Hausdorff) but their certified reach is capped at gamma ~ 8
  resp. gamma_1 = 14.13, both aeons below the cited Platt-Trudgian
  height.  A blind instrument cannot disprove: the 'standing disproof
  channels' of the roadmap are, in their certified ranges,
  consistency checks whose emptiness is a THEOREM given the cited
  inputs, not an observation.  The corpus's own scope notes state
  the caps; the roadmap headline sentence does not.""")

# =====================================================================
section("J2  THE OCT VOCABULARY BOUNDARY (unpriced external classes)")
# =====================================================================
UNPRICED = [
    {"class": "ergodic / measure-rigidity positivity transfer"
              " (auxiliary flow or group averaging -> pointwise)",
     "corpus_coverage": "NONE (proportion pricing covers liminf"
                        " classes; rigidity-type transfer never"
                        " enumerated)", "verdict": "UNPRICED"},
    {"class": "model-theoretic / o-minimality definability counting"
              " (Pila-Wilkie style)",
     "corpus_coverage": "NONE (would reduce to density/counting IF it"
                        " lands there; as an alignment source it is"
                        " new)", "verdict": "UNPRICED"},
    {"class": "representation-theoretic positivity of a bigger group"
              " (functoriality / Arthur unitarity)",
     "corpus_coverage": "PARTIAL-INTERFACE (spec-sheet P7 covers the"
                        " cohomology precedent; general rep-theoretic"
                        " positivity is not cohomology)",
     "verdict": "UNPRICED"},
    {"class": "multiplicative chaos / GMC, Fyodorov-Hiary-Keating",
     "corpus_coverage": "REDUCES-IN-SPIRIT (unconditional outputs are"
                        " distributional magnitude statements failing"
                        " P1) but NOT literally enumerated",
     "verdict": "REDUCES-WITH-ENUMERATION-GAP"},
    {"class": "arithmetic quantum unique ergodicity",
     "corpus_coverage": "NONE; no known export to zeta ordinate"
                        " alignment; rate-free equidistribution would"
                        " reduce to the priced U1 Weyl class",
     "verdict": "NO-KNOWN-EXPORT"},
    {"class": "higher-order Fourier uniformity of Moebius"
              " (Green-Tao-Ziegler)",
     "corpus_coverage": "NONE (E7 prices exact multiplicative"
                        " transforms, not uniformity norms)",
     "verdict": "UNPRICED"},
]
ABSENCE_KEYS = ["ATLAS", "UNTESTED", "SAT", "BIRD", "LEV", "V913"]
ABSENCE_TOKENS = ["o-minimal", "ergodic", "multiplicative chaos",
                  "fyodorov", "unique ergodicity", "functoriality"]
hits = []
for key in ABSENCE_KEYS:
    low = _text(key).lower()
    for tok in ABSENCE_TOKENS:
        if tok in low:
            hits.append((key, tok))
check("J2.G1 ABSENCE GATES: none of the six external class keywords"
      " occurs in any atlas artifact (the classes are genuinely"
      " outside the enumeration, not silently priced)",
      hits == [], str(hits))
check("J2.G2 the corpus's own fence exists: atlas completeness typed"
      " as 'an editorial claim, typed as such, not a gate'",
      ward("P", "an editorial claim, typed as such, not a gate"))
check("J2.G3 tally wards: 24 -> 25 candidates, 0 PASS (levinson probe)",
      ward("LEV", "24 -> 25") and ward("LEV", "0 PASS"))
for u in UNPRICED:
    print("    %-58s %s" % (u["class"][:58], u["verdict"]))
print("""
  J2 TYPED RESULT: the OCT's clause (ii) is complete over the corpus
  vocabulary ONLY.  Six structural argument classes were never
  enumerated (absence-gated above); four are UNPRICED, one reduces
  in spirit with an enumeration gap, one has no known export.  For
  the unpriced classes the only corpus constraint is the spec-sheet
  interface P1-P6 (a filter, not a pricing).  This is the honest
  boundary of the OCT -- sharper than the published sentence
  'no blanket-untested class left', which is vocabulary-relative.""")

# =====================================================================
section("J5  THE DESCENT CHAIN (roadmap Stage 3, per entry form)")
# =====================================================================
STAGE3_LINKS = [
    ("Stage-2 finite acceptance gates -> ANY infinite-quantifier form",
     "OPEN", "the acceptance gates (M2d) check FINITE sections (cells"
     " n+k <= 86, extend k <= 1e19 reach); NO machinery converts a"
     " gate-passing candidate into an all-quantifier statement --"
     " v912 covers per-element convergence for the WALL chain only"),
    ("entry HAUS_ALL -> RH", "PROBE+CLASSICAL",
     "Widder + no-atom + continuation (D5); NOT kernel-checked, NOT"
     " v848; the CofinalPredefinition non-interference hardening does"
     " not cover the (n,k) family (it does not need to -- the Pascal"
     " field is a priori fixed -- but the Lean guarantees do not"
     " extend to it)"),
    ("entry SCREW_ALL_A -> RH", "CLASSICAL",
     "Suzuki equivalence (cited); OR via the OPEN round-90 contraction"
     " lemma + SVPIN if run through the carrier"),
    ("entry WEYL_CONTR -> RH", "PROBE+CLASSICAL",
     "SVPIN skeleton (D4) + Pick backward; sound gate-by-gate,"
     " Lean-packaged composition with three cited fields"),
    ("entry SIGN_POS -> RH", "PROBE+CLASSICAL(CONDITIONAL)",
     "real-root architecture skeleton: determination lemma classical,"
     " CF simplicity/evenness named conditional, measured support"
     " convicted circular -- the WEAKEST per-form descent"),
    ("v848/CofinalWeil extraction (D1) usable from any entry form?",
     "NO", "the kernel-checked chain consumes H_COF (predeclared wall"
     " family, mesh-cofinal) -- NOT one of the three entry forms; no"
     " corpus arrow produces H_COF from HAUS_ALL/WEYL_CONTR/SIGN_POS"
     " short of RH itself (test-class mismatch: tents vs cells vs"
     " disks vs signs)"),
]
check("J5.G1 roadmap wards: Stage-3 label + 'ANY ONE of the three"
      " lemma forms' + 'No step of Stage 3 is new mathematics' all"
      " present in the frozen roadmap probe",
      ward("ROAD", "CONDITIONAL-KERNEL-CHECKED")
      and ward("ROAD", "in ANY ONE of the three lemma forms")
      and ward("ROAD", "No step of Stage 3 is new mathematics"))
check("J5.G2 v848 consumes H_cof and NOTHING else (hypothesis (H)"
      " isolated; wall family)",
      ward("V848", "hypothesis (H)")
      and ward("V848", "cofinal finite positivity"))
check("J5.G3 ABSENCE GATE: the Lean extraction tier"
      " (CofinalWeil/CofinalPredefinition) nowhere mentions the"
      " Hausdorff family -- the kernel-checked lane is form-specific",
      "hausdorff" not in _text("LCW").lower()
      and "hausdorff" not in _text("LCP").lower())
check("J5.G4 the SVPIN honesty lock exists (skeleton alone yields"
      " nothing)", ward("LSV", "skeleton_not_unconditional"))
for (nm, st, note) in STAGE3_LINKS:
    print("    [%-28s] %s" % (st[:28], nm))
print("""
  J5 TYPED RESULT: Stage 3 is 'conditional-complete' ONLY per entry
  form and only citation-grade: for HAUS_ALL and WEYL_CONTR the
  descent is probe-gated + classical (not kernel-checked); for
  SIGN_POS it additionally rests on the CF-realness conditional --
  the weakest link among the descents.  The single kernel-checked
  end-to-end extraction (v848 + CofinalWeil) accepts ONLY the wall
  form H_COF, which is not among the three entry forms and is not
  producible from them.  The weakest link OVERALL is the Stage-2 ->
  Stage-3 interface itself: acceptance gates are finite, the entry
  forms are infinite-quantifier statements, and no corpus machinery
  bridges that jump (for the wall chain v912 bridges convergence,
  not positivity).""")

# =====================================================================
section("J6  HOSTILE-REFEREE SWEEP (load-bearing sentences, graded)")
# =====================================================================
SENTENCES = [
    ("'three equivalent lemma forms' (paper, twice + roadmap)",
     "NOT-GROUNDED-AS-STATED",
     "only HAUS_ALL is a proven two-sided equivalence among the three"
     " named; WEYL_CONTR and SIGN_POS have RH => form OPEN (J1.G3/G4)"
     " -- FENCE NEEDED: 'three RH-sufficient lemma forms, one of them"
     " a proven equivalence'"),
    ("'Stage 3 (conditional-complete; assembly, machine-held)'",
     "PARTIALLY-GROUNDED",
     "machine-held only for the H_COF entry no Stage-2 gate produces;"
     " per-form descents are probe-gated+classical; SIGN_POS entry"
     " conditional (J5)"),
    ("'two certified falsification instruments ... standing disproof"
     " channels ... open and empty'",
     "GROUNDED-WITH-CAP",
     "disproof-sound but reach-capped below Platt-Trudgian; emptiness"
     " is a theorem given the cited inputs, not an observation (J4)"),
    ("OCT clause (ii): 'no blanket-untested class left'",
     "VOCABULARY-RELATIVE",
     "true over the 25 enumerated classes; six external structural"
     " classes never enumerated (J2); in-text fence exists"),
    ("'R3 alone implies Weil positivity'",
     "GROUNDED-CONDITIONAL",
     "presupposes the trace-formula identification (determination"
     " leg) that defines the limit; typed as architecture-internal in"
     " the arbiter"),
    ("'(AC) identity gated symbolically exactly'",
     "GROUNDED",
     "'exactly' applies to the symbolic layer; the numeric weld"
     " carries the declared 3.4e-4 taper residual (paper states"
     " both)"),
]
for (s, grade, note) in SENTENCES:
    print("    [%-24s] %s" % (grade, s))
check("J6.G1 all graded sentences exist in their artifacts",
      ward("P", "three equivalent lemma")
      and ward("ROAD", "CONDITIONAL-KERNEL-CHECKED")
      and ward("ROAD", "standing disproof")
      and ward("P", "R3 alone implies Weil positivity")
      and ward("P", "gated symbolically exactly"))
check("J6.G2 the document-wide no-RH fence is present (the audit"
      " inherits it)", ward("P",
      "No claim of progress on the Riemann Hypothesis"))

# =====================================================================
section("COMPOSITE VERDICT")
# =====================================================================
n_pass = sum(1 for (_n, ok) in CHECKS if ok)
n_tot = len(CHECKS)
FINDINGS_FUNDAMENTAL = [
    "F1 FORMS-EQUIVALENCE-ONE-SIDED: of the advertised 'three"
    " equivalent lemma forms' only the Hausdorff form is a proven"
    " (citation-grade) RH equivalence; Weyl-disk contraction and"
    " sign positions are RH-sufficient pendants with RH => form OPEN;"
    " all mutual equivalences route through RH; TRANSFER-NONE for"
    " partial/finite results (counterexample world J1.N7).",
    "F2 STAGE3-ENTRY-FORM-MISMATCH: the only kernel-checked"
    " extraction (v848/CofinalWeil) accepts the wall form H_COF,"
    " which is not among the three entry forms and not producible"
    " from them; per-form descents are probe-gated+classical, the"
    " sign-position descent conditional; the finite->infinite"
    " quantifier jump at the Stage-2/3 interface has no machinery.",
    "F3 FALSIFIER-REACH-CAP: both certified instruments are"
    " disproof-sound but provably blind above gamma ~ 8 resp."
    " gamma_1 = 14.13; given Platt-Trudgian their certified channels"
    " are empty BY THEOREM -- zero live falsification power in the"
    " certified ranges.",
]
FINDINGS_BOUNDARY = [
    "F4 OCT-VOCABULARY-BOUNDARY: six structural argument classes"
    " outside the enumeration (4 UNPRICED, 1 reduces-with-gap,"
    " 1 no-known-export).",
    "F5 LOCALIZATION-IS-A-FAMILY: six inequivalent localizations,"
    " no shared completion leg, mesh-monotonicity false in general"
    " (counterexample J3.G2); corpus prose already fenced -- no"
    " violation found.",
    "F6 PROSE-GRADE: two sentences graded conditional/with-cap"
    " (J6 table); no fatal misstatement found.",
]
print("\n  gates: %d/%d PASS%s" % (n_pass, n_tot,
      "" if not FAILS else "  FAILED: %s" % FAILS))
print("\n  FUNDAMENTAL FINDINGS (%d):" % len(FINDINGS_FUNDAMENTAL))
for f in FINDINGS_FUNDAMENTAL:
    print("   - %s" % f)
print("\n  BOUNDARY FINDINGS (%d):" % len(FINDINGS_BOUNDARY))
for f in FINDINGS_BOUNDARY:
    print("   - %s" % f)
verdict = ("BIGPICTURE-FINDINGS(%d)" % len(FINDINGS_FUNDAMENTAL)
           if n_pass == n_tot else "AUDIT-INVALID")
print("\nVERDICT: %s" % verdict)
print("SPEC_SHA %s | runtime %.1f s | gates %d/%d"
      % (SPEC_SHA, time.time() - T0, n_pass, n_tot))
print("\nNO STATEMENT ABOUT THE RIEMANN HYPOTHESIS IS MADE.  The"
      " synthetic worlds are counterexample constructions about the"
      " INSTRUMENTS, not about zeta.  Nothing here closes, narrows or"
      " moves any gate, marker or ledger row.")
sys.exit(0 if n_pass == n_tot else 1)
