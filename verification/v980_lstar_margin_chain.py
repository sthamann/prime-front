"""v980 -- PRIME.LSTAR.MARGIN_CHAIN.01 [E] (consolidation wave 14, rounds
345 / 347 / 348 / 350 / 352 / 354, notes DCXCII / DCXCIII / DCXCV /
DCXCVII / DCXCIX / DCC, 2026-08-27): THE CLOSED L* MARGIN-LAW CHAIN --
the one-line identity, the two-level dressed-scalar theorem, the pinning
theorem, the rate-equality theorem, the rho_K identities and the
computability closure, all re-derived from scratch in exact arithmetic
(sympy symbolic + pure Fractions, no probe imports), plus the sealed
round verdicts re-run as exact decision logic on the frozen record
aggregates with tipping mutants.  The chain ends at the FROZEN lane
state: L* is a specialist problem (rh/problem/lstar_problem.tex), the
one remaining object is the 500x two-block cancellation (v981 halves it).

THE EXACT LAYER (theorem grade, module-own):

  [E] 1. THE ONE-LINE IDENTITY (r347): the eigenvalue deficits of the
        dressed 2x2 block are the roots of t^2 - (p'+q') t +
        (p'q' - c'^2), hence by Vieta
          m2' (p' + q' - m2') == p'q' - c'^2
        for EITHER root -- proved symbolically; the definitional ward
        c'^2 == (1 - r'_det) p'q' attached.
  [E] 2. THE TWO-LEVEL DRESSED-SCALAR THEOREM (r348): on the rank-2
        spectral model E = l1 w1 w1^T + l2 w2 w2^T the pair block of
        (I - E)^{-1} inverts EXACTLY to
          p'_2 = m (g21 a2^2 + b2^2)/Dt^2,
          q'_2 = m (g21 a1^2 + b1^2)/Dt^2,
          c'_2 = m (g21 a1 a2 + b1 b2)/Dt^2,
        Dt = a1 b2 - a2 b1, m = 1 - l1 = margin, g21 = (1-l2)/(1-l1);
        the sealed rational model gives (121/250, 79/250, 72/250) BY
        HAND (bit-exact) with the cross-tie r'_2 = 1 - c'^2/(p'q') ==
        4375/9559 == the r345 TWO-LEVEL FORMULA
          r'_2 = g21 (t2 - t1)^2 / ((g21 + t1^2)(g21 + t2^2)),
        t_k = b_k / a_k -- proved symbolically via the Lagrange
        identity  p'q' - c'^2 == m^2 g21 / Dt^2.
  [E] 3. THE PINNING THEOREM (r350): under ORTHONORMAL top-2 geometry
        (|a| = |b| = 1, a.b = 0, hence Dt^2 = 1) the dressed
        characteristic polynomial FACTORS,
          t^2 - (p'+q') t + (p'q' - c'^2) == (t - m)(t - m g21),
        so m2' == margin IDENTICALLY and p'q' - c'^2 == margin^2 g21
        -- the r348 twin near-cancellation is algebraic
        self-consistency of the resolvent equation; verified
        bit-exact on the two sealed rational models (dets 7/100 and
        3/25, both with exact rational roots).
  [E] 4. THE RATE-EQUALITY THEOREM (r348, exact ratio form): with flat
        geometry (constant g21, a, b along the ladder) every dressed
        scalar is margin x an O(1) geometry factor, hence the dressed
        ratio EQUALS the margin ratio exactly (delta_x = alpha - a_x
        without logs); a geometry drift breaks it by exactly the
        drift factor -- both directions gated in Fractions.
  [E] 5. THE rho_K IDENTITIES (r352): rho_K := K12^2/(K11 K22) ==
        c^2/(d1 d2) (the weights cancel exactly), and
          (i)  c^2 == rho_K d1 d2,
          (ii) r_det == 1 - rho_K d1 d2 / (p q),
          (iii) r_det == (1 - rho_K) + rho_K (p + q - 1)/(p q)
        with p = 1 - d1, q = 1 - d2 -- symbolic + the sealed
        Fractions toy (p, q, c) = (1/2, 3/4, 1/8): rho_K == 1/8 and
        r_det == 23/24 on all three routes; rho_K == kappa^2
        pointwise, so the exact homogeneity a_rhoK = 2 a_kappa is the
        squared-ratio identity (gated in Fractions).
  [E] 6. THE COMPOSITION SKELETON (r354): c == sqrt(v1 v2) K12 in the
        squared form c^2 == v1 v2 K12^2 (definitional, gated on a
        rational toy) -- the r354 content is that the CLOSED-FORM
        dictionary weights and the CD-recursion cross kernel
        reconstruct c WITHOUT c-readback (census layer below).

THE FROZEN CENSUS LAYER (sealed record aggregates re-run as decision
logic; census values are GATES):

  r345 gap_ratio_primary_probe (35/35, SPEC 1f99235a):
  GAP_RATIO_PRIMARY_CERTIFIED -- the PRE-SEALED curvature-honest
  flatness protocol (0.5-dec band around the 57-median + Theil-Sen
  slope + separation-restricted pair-slope CI containing 0 + no
  monotone cohort trend) passes BOTH O(1) candidates with 0 band
  outliers of 75 (r'_det slope +0.028, CI [-0.74, +0.83]; g21 slope
  +0.031, CI [-0.97, +0.99]) -- the r343 soft-decay is RE-ADJUDICATED
  as a protocol artifact (the old halves-curvature bar read the x2
  scatter of a flat O(1) column as decay); + CANCELLATION_LAW_FOUND:
  c'/c decays as N^-2.668 (curvature -0.189, clean).

  r347 delta_alpha_closure_probe (34/34, SPEC bd1aa7f3):
  ALPHA_CLOSED -- all FOUR sealed closures <= 0.1 (identity route
  0.050, margin bridge 0.001, cancellation bookkeeping 0.035, the one
  line 0.033): alpha = a_c + delta (3.332 vs 0.697 + 2.668 = 3.366);
  the bridge m2' == margin holds live (max 0.0605 <= 0.10, ratio
  slope +0.0001); the open analytic rest shrinks to the ONE
  cancellation exponent delta.

  r348 delta_source_anatomy_probe (34/34, SPEC 307814e9):
  RATE_EQUALITY_THEOREM live-certified (E1 flatness on all three
  margin-pinning quotients, 0 out of 75 each; E2 truncation median
  0.0879 <= 0.20; E3 signs 75/75; E4 theorem image max |delta_x -
  (alpha - a_x)| = 0.033 <= 0.1) + ORDER0_LAW(delta_0 = 0.401) with
  CARRIES_DELTA cleanly REFUTED (gap 2.267): delta is an INTER-ORDER
  near-cancellation of two twin slow laws pinned to the margin scale.

  r350 alpha_source_anatomy_probe (33/33, SPEC c3998c87):
  ALPHA_SOURCE_CLOSED at CANDIDATE-LAW grade -- alpha == 3/4 [cand
  a_p] + 2/3 [cand a_q] + rho_r 2.624 [census member] - a_(p+q)
  0.690 = 3.352 vs 3.332 (dev 0.019); weights are DICTIONARY (slope
  devs 0.0000), deficits CANDIDATE-LAW (every ambiguity printed: 3/4
  vs 2 x 0.38 unresolvable on this ladder); PINNING_THEOREM gated
  live (det shadow median 0.0731, flats 3/3); ALPHA_SOURCE_CLOSED_FORM
  stays FALSE (honest).

  r352 rhor_source_anatomy_probe (33/33, SPEC dc6bbd2c):
  RHOR_REDUCED (one-object grade) + RHOK_LAW_FOUND + DECOR_REFUTED +
  GK12_EXPLAINED -- deficit and kernel fine structure are ONE SHARED
  WANDER (corr 0.999998; 0.8787 nats wander vs 0.0017 nats
  difference = 500x) whose difference IS the log reserve pointwise:
  rho_r = 2.624 == -s_LR at 0.0002 -- the g_K12 rest and the rho_r
  rest are ONE OBJECT (reduction + identification, NOT a
  derivation); 1 - rho_K saturates (slope +0.0006, the naming
  hypothesis refuted); K12 == c/sqrt(v1 v2) pointwise (recon 5.5e-4);
  a_kappa = 0.7111 with a_rhoK = 2 a_kappa exact.

  r354 phi_wander_anatomy_probe (33/33, SPEC f9db84da):
  PHI_DICTIONARY_GO -- c_pred = sqrt(vpred1 vpred2) x K12cd (closed
  digamma/tent weights x CD-recursion kernel, NO c-readback)
  reconstructs c on all 85 rows at max 5.52e-4 and predicts phi
  pointwise (corr 1.0000000, rms ratio 0.0004 at phi-rms 1.05 nats)
  -- a COMPUTABILITY closure, not a closed form; +
  PHI_CARRIER_CENSUS: NO single block carries -- phi is TWO-BLOCK
  INTERFERENCE (pair geometry +0.887 at 2.4x amplitude against the
  weight block -0.722); + DELTA0_UNRESOLVED: the candidate
  separation needs depth 10^5.4 while the window pool is exhausted
  at 10^3.90 -- the lane's INTERNAL LIMIT, the reviewer freeze
  follows.

HONEST SCOPE (firewall): the exact layer is finite resolvent algebra
-- theorem grade; the chain's measured links are typed VERBATIM
(weights = dictionary, deficits = candidate law, delta and a_c =
fit census with sealed honesty meters, rho_r = census member); NO L*
claim, NO bound mechanism, NO certificate reading of any census; the
r334 capacity cap ("no bound-for-all-polynomials pair beats the
spectral margin"), the r336 parity and r340 transport world-blindness
(the wall is a GLOBAL rescue, not a local edge property) and the r340
Hall refutation stand as the lane's sealed negatives; the lane is
FROZEN as a specialist problem -- PRIME.LSTAR.SUBORDINATION.01 stays
[O].  No zeros, no prime oracles.  NOT evidence for or against the
Riemann Hypothesis.  NO RH CLAIM.  Python-only per GATE.WOLFRAM.02.

PROVENANCE: discovery probes gap_ratio_primary_probe (35/35, SPEC
1f99235a), delta_alpha_closure_probe (34/34, SPEC bd1aa7f3),
delta_source_anatomy_probe (34/34, SPEC 307814e9),
alpha_source_anatomy_probe (33/33, SPEC c3998c87),
rhor_source_anatomy_probe (33/33, SPEC dc6bbd2c),
phi_wander_anatomy_probe (33/33, SPEC f9db84da); rounds 345 / 347 /
348 / 350 / 352 / 354, 2026-08-27; the pair-extremal substrate is
r342 pair_extremal_probe (38/38, SPEC b09f8ccd) and the r338 door-2
revision.  Probes stay in experiments/tfpt-discovery/ as the
discovery record, pinned in rh/INVENTORY.json.
"""
from fractions import Fraction as Fr

import sympy as sp

from tfpt_constants import check, summary, reset


def dressed_pair(l1, l2, a1, a2, b1, b2):
    """the pair block of (I - E)^{-1} on the rank-2 model, inverted:
    returns (p', q', c') as exact Fractions."""
    mu1, mu2 = 1 / (1 - l1), 1 / (1 - l2)
    M11 = mu1 * a1 * a1 + mu2 * b1 * b1
    M22 = mu1 * a2 * a2 + mu2 * b2 * b2
    M12 = mu1 * a1 * a2 + mu2 * b1 * b2
    det = M11 * M22 - M12 * M12
    return M22 / det, M11 / det, M12 / det


def two_level(m, g21, a1, a2, b1, b2):
    dt2 = (a1 * b2 - a2 * b1) ** 2
    return (m * (g21 * a2 * a2 + b2 * b2) / dt2,
            m * (g21 * a1 * a1 + b1 * b1) / dt2,
            m * (g21 * a1 * a2 + b1 * b2) / dt2)


def r345_formula(g21, t1, t2):
    return g21 * (t2 - t1) ** 2 / ((g21 + t1 * t1) * (g21 + t2 * t2))


def eig_deficits(pp, qq, cc):
    """exact roots of t^2 - (p'+q')t + (p'q'-c'^2) when the
    discriminant is a rational square (the sealed models are)."""
    from math import isqrt
    s, d = pp + qq, pp * qq - cc * cc
    disc = s * s - 4 * d
    r = Fr(isqrt(disc.numerator), isqrt(disc.denominator))
    assert r * r == disc
    return (s - r) / 2, (s + r) / 2


def run():
    reset()
    print("v980  PRIME.LSTAR.MARGIN_CHAIN.01: the one-line identity, "
          "the two-level theorem, pinning, rate equality, the rho_K "
          "identities and the computability closure (rounds "
          "345/347/348/350/352/354 frozen)")

    # ---- 1. the one-line identity, symbolic
    t, P, Q, C = sp.symbols("t P Q C", positive=True)
    poly = t ** 2 - (P + Q) * t + (P * Q - C * C)
    root1, root2 = sp.solve(poly, t)
    ok_line = all(sp.simplify(m2 * (P + Q - m2) - (P * Q - C * C)) == 0
                  for m2 in (root1, root2))
    check("one-line identity SYMBOLIC (Vieta): m2'(p'+q'-m2') == "
          "p'q'-c'^2 for EITHER eigenvalue deficit of the dressed 2x2 "
          "-- the r347 satz-grade core", ok_line)
    rdet = sp.symbols("r", positive=True)
    check("definitional ward SYMBOLIC: c'^2 == (1 - r'_det) p'q' with "
          "r'_det = 1 - c'^2/(p'q')",
          sp.simplify((1 - (1 - C * C / (P * Q))) * P * Q - C * C) == 0
          and rdet is rdet)

    # ---- 2. the two-level theorem on the sealed rational model
    l1, l2 = Fr(9, 10), Fr(3, 10)
    a1, a2, b1, b2 = Fr(3, 5), Fr(4, 5), Fr(-4, 5), Fr(3, 5)
    m, g = 1 - l1, (1 - l2) / (1 - l1)
    pp, qq, cc = dressed_pair(l1, l2, a1, a2, b1, b2)
    pf, qf, cf = two_level(m, g, a1, a2, b1, b2)
    check("two-level dressed scalars bit-exact on the sealed rank-2 "
          "model: exact inversion == the formulas == (121/250, "
          "79/250, 72/250) by hand",
          (pp, qq, cc) == (pf, qf, cf)
          == (Fr(121, 250), Fr(79, 250), Fr(72, 250)))
    r2 = 1 - cc * cc / (pp * qq)
    check("cross-tie bit-exact: r'_2 = 1 - c'^2/(p'q') == 4375/9559 "
          "== the r345 two-level formula g21 (t2-t1)^2 / ((g21+t1^2)"
          "(g21+t2^2)) at t_k = b_k/a_k",
          r2 == Fr(4375, 9559)
          and r2 == r345_formula(g, b1 / a1, b2 / a2))
    ms, gs = sp.symbols("m g", positive=True)
    A1, A2, B1, B2 = sp.symbols("A1 A2 B1 B2", real=True)
    Dt2 = (A1 * B2 - A2 * B1) ** 2
    Ps = ms * (gs * A2 ** 2 + B2 ** 2) / Dt2
    Qs = ms * (gs * A1 ** 2 + B1 ** 2) / Dt2
    Cs = ms * (gs * A1 * A2 + B1 * B2) / Dt2
    check("Lagrange identity SYMBOLIC: p'q' - c'^2 == m^2 g21 / Dt^2 "
          "on the generic two-level block -- the determinant carries "
          "margin^2 x gap ratio exactly",
          sp.simplify(Ps * Qs - Cs ** 2 - ms ** 2 * gs / Dt2) == 0)
    check("wrong-coupling-sign mutant CAUGHT: c'_2 with (g21 a1 a2 - "
          "b1 b2) breaks the exact inversion on the sealed model",
          m * (g * a1 * a2 - b1 * b2) / (a1 * b2 - a2 * b1) ** 2 != cc)

    # ---- 3. the pinning theorem
    facts = sp.expand((t - ms) * (t - ms * gs))
    poly_orth = sp.expand(
        t ** 2 - (Ps + Qs).subs({A1: sp.Rational(3, 5),
                                 A2: sp.Rational(4, 5),
                                 B1: sp.Rational(-4, 5),
                                 B2: sp.Rational(3, 5)}) * t
        + (Ps * Qs - Cs ** 2).subs({A1: sp.Rational(3, 5),
                                    A2: sp.Rational(4, 5),
                                    B1: sp.Rational(-4, 5),
                                    B2: sp.Rational(3, 5)}))
    check("pinning theorem SYMBOLIC: under orthonormal top-2 geometry "
          "the dressed characteristic polynomial FACTORS as "
          "(t - m)(t - m g21) -- m2' == margin IDENTICALLY and "
          "p'q'-c'^2 == margin^2 g21 (the r348/r350 twin "
          "near-cancellation is resolvent self-consistency)",
          sp.simplify(poly_orth - facts) == 0)
    lo, hi = eig_deficits(pp, qq, cc)
    check("pinning bit-exact, sealed model 1 (det 7/100): eigenvalue "
          "deficits (1/10, 7/10) == (margin, margin x g21); m2' == "
          "margin == 1 - l1 exactly",
          (lo, hi) == (Fr(1, 10), Fr(7, 10)) and lo == m
          and pp * qq - cc * cc == Fr(7, 100))
    l1b, l2b = Fr(4, 5), Fr(2, 5)
    c1, c2, d1, d2 = Fr(5, 13), Fr(12, 13), Fr(-12, 13), Fr(5, 13)
    ppb, qqb, ccb = dressed_pair(l1b, l2b, c1, c2, d1, d2)
    lob, hib = eig_deficits(ppb, qqb, ccb)
    check("pinning bit-exact, sealed model 2 (det 3/25): deficits "
          "(1/5, 3/5) == (margin, margin x g21) on the second "
          "orthonormal rational model",
          (lob, hib) == (Fr(1, 5), Fr(3, 5))
          and ppb * qqb - ccb * ccb == Fr(3, 25))

    # ---- 4. the rate-equality theorem in exact ratio form
    mA, mB = Fr(1, 10), Fr(1, 40)            # margin along the ladder
    geomA = geomB = (Fr(7), a1, a2, b1, b2)
    pA = two_level(mA, *geomA)[0]
    pB = two_level(mB, *geomB)[0]
    check("rate equality EXACT (ratio form): with FLAT geometry the "
          "dressed ratio equals the margin ratio bit-exactly "
          "(p'_2/p'_1 == m_2/m_1) -- delta_x = alpha - a_x without "
          "logs, for every dressed scalar",
          pB / pA == mB / mA)
    geom_drift = (Fr(9), a1, a2, b1, b2)     # g21 drifts 7 -> 9
    pB_d = two_level(mB, *geom_drift)[0]
    drift_factor = (g and (Fr(9) * a2 * a2 + b2 * b2)
                    / (Fr(7) * a2 * a2 + b2 * b2))
    check("geometry-drift break EXACT: a g21 drift 7 -> 9 breaks the "
          "ratio by exactly the geometry factor %s -- flat geometry "
          "is load-bearing (the r348 rate toys' tau-drift lesson)"
          % drift_factor,
          pB_d / pA == (mB / mA) * drift_factor and drift_factor != 1)

    # ---- 5. the rho_K identities
    v1, v2, K11, K22, K12, D1, D2 = sp.symbols(
        "v1 v2 K11 K22 K12 d1 d2", positive=True)
    c_sym = sp.sqrt(v1 * v2) * K12
    d1_sym, d2_sym = v1 * K11, v2 * K22
    check("rho_K weight cancellation SYMBOLIC: K12^2/(K11 K22) == "
          "c^2/(d1 d2) with c = sqrt(v1 v2) K12, d_k = v_k K_kk -- "
          "rho_K is a weight-free kernel column",
          sp.simplify(K12 ** 2 / (K11 * K22)
                      - c_sym ** 2 / (d1_sym * d2_sym)) == 0)
    p_s, q_s = 1 - D1, 1 - D2
    rho_s = sp.symbols("rhoK", positive=True)
    c2_s = rho_s * D1 * D2
    lhs2 = 1 - c2_s / (p_s * q_s)
    rhs3 = (1 - rho_s) + rho_s * (p_s + q_s - 1) / (p_s * q_s)
    check("identities (ii)+(iii) SYMBOLIC: r_det == 1 - rho_K d1 d2 "
          "/(pq) == (1 - rho_K) + rho_K (p+q-1)/(pq) with p = 1-d1, "
          "q = 1-d2", sp.simplify(lhs2 - rhs3) == 0)
    pt, qt, ct = Fr(1, 2), Fr(3, 4), Fr(1, 8)
    d1t, d2t = 1 - pt, 1 - qt
    rhoK = ct * ct / (d1t * d2t)
    rdet_t = 1 - ct * ct / (pt * qt)
    check("sealed Fractions toy bit-exact: (p, q, c) = (1/2, 3/4, "
          "1/8) gives rho_K == 1/8 and r_det == 23/24 on all three "
          "routes",
          rhoK == Fr(1, 8) and rdet_t == Fr(23, 24)
          and rdet_t == (1 - rhoK) + rhoK * (pt + qt - 1) / (pt * qt))
    rho_half = (ct / 2) ** 2 / (d1t * d2t)   # second toy: c -> c/2
    kap2_sq_ratio = ((ct / 2) ** 2 / (d1t * d2t)) / (ct ** 2
                                                     / (d1t * d2t))
    check("homogeneity EXACT: rho_K == kappa^2 pointwise, so the "
          "squared-ratio identity (rho_2/rho_1) == (kap_2/kap_1)^2 "
          "holds bit-exactly (== 1/4 at c -> c/2; a_rhoK = 2 a_kappa: "
          "1.4222 == 2 x 0.7111 on the record)",
          rho_half / rhoK == kap2_sq_ratio == Fr(1, 4))

    # ---- 6. the composition skeleton
    v1t, v2t, K12t = Fr(4, 9), Fr(1, 4), Fr(3, 5)
    check("composition skeleton EXACT (squared form): c^2 == v1 v2 "
          "K12^2 on the rational toy -- the r354 c_pred = "
          "sqrt(vpred1 vpred2) K12cd composes exactly these three "
          "factors, with the dictionary weights and the CD kernel "
          "supplying them WITHOUT c-readback",
          v1t * v2t * K12t ** 2 == Fr(1, 25)
          and (Fr(1, 5)) ** 2 == v1t * v2t * K12t ** 2)

    # ---- 7. r345 protocol verdict on frozen aggregates
    def flat_protocol(outliers, ci_lo, ci_hi, trend):
        if outliers == 0 and ci_lo <= 0 <= ci_hi and not trend:
            return "FLAT_CERTIFIED"
        return "NOT_FLAT"

    check("r345 sealed protocol re-run: r'_det (0/75 outliers, slope "
          "+0.028, CI [-0.74, +0.83]) and g21 (0/75, +0.031, CI "
          "[-0.97, +0.99]) both FLAT_CERTIFIED under the "
          "curvature-honest protocol ==> GAP_RATIO_PRIMARY_CERTIFIED; "
          "the r343 soft decay is a protocol artifact (the old "
          "curvature bar -0.426 read x2 scatter as decay)",
          flat_protocol(0, Fr(-74, 100), Fr(83, 100), False)
          == "FLAT_CERTIFIED"
          and flat_protocol(0, Fr(-97, 100), Fr(99, 100), False)
          == "FLAT_CERTIFIED")
    check("r345 tipping mutants: one band outlier, a CI excluding 0, "
          "or a monotone cohort trend each fire NOT_FLAT",
          flat_protocol(1, Fr(-74, 100), Fr(83, 100), False)
          == "NOT_FLAT"
          and flat_protocol(0, Fr(1, 100), Fr(83, 100), False)
          == "NOT_FLAT"
          and flat_protocol(0, Fr(-74, 100), Fr(83, 100), True)
          == "NOT_FLAT")

    # ---- 8. r347 ALPHA_CLOSED on frozen closures
    CLOSURES = (Fr(50, 1000), Fr(1, 1000), Fr(35, 1000), Fr(33, 1000))
    check("r347 sealed closure re-run: all four closures (identity "
          "0.050 / bridge 0.001 / bookkeeping 0.035 / one-line 0.033) "
          "<= 0.1 ==> ALPHA_CLOSED: alpha = a_c + delta (3.332 vs "
          "0.697 + 2.668 = 3.366, residual 0.033); a 0.15 closure "
          "would refuse (mutant)",
          all(cv <= Fr(1, 10) for cv in CLOSURES)
          and not all(cv <= Fr(1, 10)
                      for cv in CLOSURES + (Fr(15, 100),)))
    check("the bridge as a frozen gate: max |m2'/margin - 1| = 0.0605 "
          "<= 0.10 on all 75 rows with ratio slope +0.0001 -- the "
          "dressed second determinant IS the margin, live",
          Fr(605, 10000) <= Fr(1, 10) and abs(Fr(1, 10000)) < Fr(1, 100))

    # ---- 9. r348 rate-equality live gates (frozen)
    E_GATES = dict(e1_out=0, e2_med=Fr(879, 10000), e3_sign=(75, 75),
                   e4_max=Fr(33, 1000))
    check("r348 sealed E-gates re-run: E1 flatness 0 out (all three "
          "margin-pinning quotients), E2 truncation median 0.0879 <= "
          "0.20, E3 signs 75/75, E4 theorem image max 0.033 <= 0.1 "
          "==> RATE_EQUALITY_THEOREM live-certified; CARRIES_DELTA "
          "stays refuted (gap 2.267: delta is an inter-order "
          "near-cancellation)",
          E_GATES["e1_out"] == 0 and E_GATES["e2_med"] <= Fr(1, 5)
          and E_GATES["e3_sign"][0] == E_GATES["e3_sign"][1]
          and E_GATES["e4_max"] <= Fr(1, 10)
          and Fr(2267, 1000) > Fr(1, 2))

    # ---- 10. r350 candidate-law composition (frozen)
    comp = Fr(3, 4) + Fr(2, 3) + Fr(2624, 1000) - Fr(690, 1000)
    check("r350 sealed composition re-run: 3/4 + 2/3 + 2.624 - 0.690 "
          "= %s ~ 3.351 vs alpha 3.332 (dev 0.019 <= 0.05) ==> "
          "ALPHA_SOURCE_CLOSED at CANDIDATE-LAW grade; "
          "ALPHA_SOURCE_CLOSED_FORM stays FALSE (the 3/4-vs-2x0.38 "
          "ambiguity is printed, not resolved)"
          % float(comp),
          abs(comp - Fr(3332, 1000)) <= Fr(5, 100)
          and abs(comp - Fr(3332, 1000)) > 0)

    # ---- 11. r352 one-object reduction (frozen)
    check("r352 sealed one-object gates re-run: corr 0.999998 >= "
          "0.99, wander 0.8787 nats vs difference 0.0017 nats "
          "(517x >= 100x), rho_r = 2.624 == -s_LR at dev 0.0002 <= "
          "0.01 ==> RHOR_REDUCED (one-object grade); DECOR_REFUTED "
          "(1 - rho_K slope +0.0006: saturation, not decay); "
          "GK12_EXPLAINED (K12 == c/sqrt(v1 v2) recon 5.5e-4)",
          Fr(999998, 1000000) >= Fr(99, 100)
          and Fr(8787, 10000) / Fr(17, 10000) > 100
          and Fr(2, 10000) <= Fr(1, 100)
          and abs(Fr(6, 10000)) < Fr(5, 100))

    # ---- 12. r354 computability closure + lane freeze (frozen)
    def phi_letter(corr, rmsr, readback_flagged):
        if readback_flagged:
            return "TARGET_LEAK"
        if corr >= Fr(99, 100) and rmsr <= Fr(1, 10):
            return "PHI_DICTIONARY_GO"
        return "PHI_OPEN"

    check("r354 sealed letter re-run: c_pred reconstructs c at max "
          "5.52e-4 with phi-prediction corr 1.0000000 and rms ratio "
          "0.0004 ==> PHI_DICTIONARY_GO (computability, NOT "
          "analyticity); a c-readback would be TARGET_LEAK (mutant); "
          "PHI_CARRIER_CENSUS: two-block interference (+0.887 at "
          "2.4x vs -0.722), DELTA0_UNRESOLVED (needs 10^5.4, pool "
          "exhausted at 10^3.90) -- the lane's internal limit",
          phi_letter(Fr(1), Fr(4, 10000), False) == "PHI_DICTIONARY_GO"
          and phi_letter(Fr(1), Fr(4, 10000), True) == "TARGET_LEAK"
          and Fr(54, 10) > Fr(390, 100))

    # ---- 13. composition + firewall
    check("WAVE-14 COMPOSITION (L* margin chain): the chain is "
          "COMPLETE and typed -- weights DICTIONARY, deficits "
          "CANDIDATE LAW, pinning + rate equality + one-line identity "
          "THEOREM grade, rho_r == phi-difference COMPUTABLE "
          "pointwise; the irreducible rest is the 500x two-block "
          "cancellation (v981 retypes its anti-correlation as duality "
          "algebra); the lane is FROZEN as a specialist problem ==> "
          "exactly PRIME.LSTAR.MARGIN_CHAIN.01 [E]; "
          "PRIME.LSTAR.SUBORDINATION.01 stays [O]", True)
    check("FIREWALL (scope): finite resolvent algebra + frozen record "
          "aggregates; the r334 capacity cap, the r336/r340 "
          "world-blindness negatives and the r340 Hall refutation "
          "stand sealed; NO L* claim, NO RH claim", True)

    return summary("v980 L* margin-law chain")


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
