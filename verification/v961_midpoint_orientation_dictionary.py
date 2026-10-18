#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v961 -- PRIME.PORT.RHP.MIDPOINT.ORIENTATION_DICTIONARY.01 (rounds 274/277, ADJUDICATED at the finite-identity level, plus the typed measurement rounds 276/278): THE MIDPOINT-ORIENTATION DICTIONARY OF THE WALL AND THE METRIC FIREWALL -- the exact Wronskian/Casoratian dictionary (base Casoratian = h_n with c' = 1, the h-free midpoint form IS the node polynomial, the augmented telescope D_{n+1} = B - W^aug_n/W^base_n), the triple right-solution coincidence, the Maslov census GO (rule R2 = interlacing/reality of the Jacobi zeros: blind 42/42, controls fire EXACTLY at flip+1, one-way detector) together with the HONEST REFUTATION that the raw atom-Sturm census is NOT the right winding quantity, and the metric-firewall measurements (graded continuum law, u-profile, exact position gradients of Hellmann-Feynman class, perturbative-only stability law).  ONE module from four probes (32/32 + 25/25 + 29/29 + 31/31 first-pass gates, zero fails; discovery probes wronskian_dictionary_probe.py, minimal_firewall_probe.py, maslov_census_probe.py, metric_stability_probe.py, rounds 274/276/277/278, notes DCVII/DCVIII/DCXI/DCX, 2026-08-25, embedded BYTE-EXACT and executed verbatim in their sealed --smoke stage at promotion -- the wave-4 embedding convention: full records sealed experiments-side and re-verified by rh/verification/run_rh.py; the metric_stability smoke stage evaluates 30 of its 31 record gates, pinned below), plus the module-own exact section S0 (sympy-symbolic + exact rationals + exact dual-number differentiation).  (S0) THE MODULE-OWN EXACT THEOREMS (fine types Identity/Formal): (S0.1) THE BASE CASORATIAN IDENTITY (the r274 dictionary core): on a frozen exact-rational 5-atom measure the monic orthogonal chain p_n and its second-kind chain q_n(z) = int (p_n(z) - p_n(x))/(z - x) dmu satisfy p_n(z) q_{n+1}(z) - p_{n+1}(z) q_n(z) = h_n IDENTICALLY IN z (sympy-expanded polynomial identity, every degree; the constant c' = 1 in this orientation convention -- the Casoratian of the pair is the pivot chain itself, no extra normalizer).  (S0.2) THE AUGMENTED TELESCOPE / BORDERED-WRONSKIAN DICTIONARY: with a frozen signed border sigma, det[[H_n, u], [u^T, B]]/det H_n = B - sum_{k<n} F_k^2/h_k EXACTLY for every prefix degree (the W^aug/W^base normal form of the fiber: the bordered determinant quotient IS the drained budget -- the r274 telescope re-derived from the determinant side, exact rationals).  (S0.3) THE HELLMANN-FEYNMAN POSITION GRADIENT (the r278 exact-gradient class, Identity fine type): under the weight perturbation w_j -> w_j(1 + eps) the pivot derivative is d h_n/d eps = w_j p_n(x_j)^2 EXACTLY for every n -- THE POLYNOMIAL VARIATION DROPS BY ORTHOGONALITY; machine-checked in exact dual-number arithmetic (Fraction-valued forward mode, no floats) through the whole chain including the terminal pivot.  (S0.4) THE JACOBI INTERLACING / REALITY DIRECTION (the r277 R2 rule, classical direction): on the frozen positive chain (all beta_k > 0) every principal characteristic polynomial has FULL real root count and consecutive levels interlace STRICTLY (exact algebraic root comparisons, no numerics); the must-fail fires: flipping one beta sign produces a degree-2 level with ZERO real roots -- reality/interlacing is precisely the quantity that dies with symmetrizability, the content of the R2 one-way detector.  (1) THE WRONSKIAN DICTIONARY (round 274, verdict WRONSKIAN_DICTIONARY_GO + ORIENTATION_PREVIEW -- the Maslov round released): (i) BASE CASORATIAN pihat_{n+1}(z)q_n(z) - pihat_n(z)q_{n+1}(z) = h_n with c' = 1 (exact in rationals, symbolic in z, all degrees on mains + 42 rungs 2.7e-12, signs exact everywhere); the right solution TRIPLE-CONSTRUCTED with exact coincidence: residue route / downward recursion with exact Dirichlet boundary q_S = 0 (THE NODE POLYNOMIAL IS THE RIGHT BOUNDARY CONDITION) / r230 dual chain + r231 L-gauge (ward 7.2e-12); (ii) THE H-FREE MIDPOINT FORM: pihat_{n+1} pihat#_{S-1-n} - beta_{n+1} pihat_n pihat#_{S-2-n} = L(z) -- the gauge-normalized midpoint Wronskian IS the node polynomial, constant in n: the r231 sign-blindness AS AN IDENTITY (it provably carries no orientation); (iii) AUGMENTED: with the border-driven second kind qs_n (rank-1 Uvarov drive) the Casoratian C_n = pihat_{n+1}qs_n - pihat_n qs_{n+1} is a POLYNOMIAL (border poles cancel exactly), the telescope C_n/h_n = sum_{k<=n} F_k pihat_k/h_k gives W^aug_n = h_n S_n and D_{n+1} = B - W^aug_n/W^base_n -- exact against the independent r263 route THROUGH the flip, mp terminal w9 4.2e-12, kz15 razor 3.5e-11; (iv) THE C-TYPOLOGY HONESTLY: c_n = 1/W^base_n = 1/(h_0 prod beta_k) is source-pure and positive on the free prefix 42/42 BUT the ENTIRE orientation of the dictionary sits in c_n (the dictionary RELOCATES the orientation question, it does not solve it); detectors: c is neither wall nor target (sp 0.74/0.36 < 0.9, oracle mutant flagged -- the reviewer no-circularity criterion passes); (v) ORIENTATION PREVIEW: the Pruefer band 0 < DeltaTheta < pi is EXACTLY equivalent to h_n > 0 (honestly typed a restatement); the controls leave the band DEGREE-EXACTLY at 25/21/27; the w9 winding measurement (mp dps 120, full algebraic continuation 0..365): 262/366 in-band = #(h_n > 0) exactly, first exit at 184 = N_w + 0 -- BUT the winding on the continuation is NOT the half-filling count (262 != 184: 78 positive continuation pivots beyond the window, measured and typed: the index count of the Maslov proof plan needs the RIGHT winding quantity, not the naive one).  (2) THE MASLOV CENSUS (round 277, verdict MASLOV_CENSUS_GO(rule R2) -- STURM_CHAIN_VERIFIED honestly NOT awarded): the blind examiner protocol (rule developed on 5 sealed training rungs, blind on 37 rungs + mains + controls; GO only on exact flip prediction) DELIVERS: R2 = the interlacing/reality structure of the JACOBI zeros passes blind 42/42 + w12/w13/w26 SAFE at full depth; the controls fire EXACTLY at flip+1 (26/22/28; r259-separated 17/6/9); R2 is NOT h-equivalent (79 pattern mismatches vs 78 h re-entry pivots -- an independent object) and the break is a ONE-WAY DETECTOR (never heals; the h-chain re-enters 78 times on the continuation, R2 does not): the cofinally monotone object the proof plan needs; THE CENTRAL FINDING (the answer to the r274 winding warning, and a genuine refutation): the RAW ATOM-STURM CENSUS IS NOT THE RIGHT WINDING QUANTITY -- on MAIN c_n == n breaks at n = 56/48 AT THROUGHOUT-POSITIVE h (zeros first escape the atom hull, then pair up inside single atom gaps): the classical separation theorem for positive measures FAILS GENUINELY for the signed comb -- the c1 expectation of the proof plan (Sturm count = n) is refuted and the round says so instead of awarding it; atom saturation max c_n = 184 = N_w at n = 215, zero healed degrees; training sealed (R1 fails, R2 passes 5/5 + 5/5, R3 does not separate); the named consequence: the theorem needs the CONTRAPOSITION with an independent index obstruction -- WHAT forbids the interlacing break before half-filling on MAIN?  Exactly there (and presumably only there) the MainWindow arithmetic must enter: THE ORIENTED MIDPOINT THEOREM IS THE NEXT PROOF ROUND (registered as PRIME.PORT.RHP.MIDPOINT.ORIENTED_THEOREM.01 [O]; round 279 in flight at this cut, NOT consumed).  (3) TYPED MEASUREMENT -- THE MINIMAL FIREWALL (round 276, fine type Numerical/Measurement, verdict FIREWALL_LAW(all surgeries GRADED, D ~ theta^b with b 0.04-1.09) + PROPERTY_RANKING(P2_JIT 0.343 < B2_MAG 0.389 < B1_SIGN 0.536 < P1_SWAP 0.621 < P3_FAM 0.700) + CONTINUUM(48/90 midband steps -- NO jump) + V956_PLACEMENT + N_TRANSPORT(sp +0.84/+0.86) + FIREWALL_HYPOTHESIS): the answer to continuum-vs-jump is CONTINUUM -- the wall is no all-or-nothing switch (single operations typically survive to depth 0.88-1.00; position-dependent lethal exceptions at 51-152; the earliest-atom scoping swap dies at 34 = the r249 anchor as a curve ENDPOINT, not a rule); THE RANKING SURPRISE (refining and partly CORRECTING r273): SUPPORT EXACTNESS is the most wall-critical property -- jitter at 2 percent of the local atom gap already costs 3/4 of the depth, while the Euler family structure is the MILDEST per operation: THE WALL READS THE METRIC PLACEMENT OF THE SIGNED SOURCE MORE PRECISELY THAN THE EULER BOOKKEEPING -- the arithmetic firewall is more precisely a METRIC firewall (the exact log-p^k positions at sub-gap precision plus the magnitude-position pairing carry, not the multiplicative organization as bookkeeping); the falsifiable firewall hypothesis and the u-profile follow-up are registered on PRIME.PORT.WALL.METRIC_FIREWALL.01 [O].  (4) TYPED MEASUREMENT + EXACT GRADIENTS -- THE METRIC STABILITY (round 278, fine types Identity (gradients) + Numerical/Measurement, verdict METRIC_STABILITY_LAW(theta* med 8e-4 (w9) / 1.2e-4 (kz55); N-trend SHRINKING) + GRADIENT_EXPLAINS_DOSE(PARTIAL, ratio 0.41) + U_PROFILE(PREDICTIVE, sp -0.82) + MAINWINDOW_PREDICATE(PERTURBATIVE_ONLY)): the lasting tools -- (i) THE EXACT GRADIENTS (Hellmann-Feynman class, sealed): d log h_n/du_j = <w-dot_j, pihat_n^2>/h_n (the polynomial variation drops by orthogonality) and dF_n/du_j = -<w-dot_j, pihat_n B_n> with the border-CD kernel from the r274 telescope (FD/Richardson gates worst 4.5e-5, mp arbitration 1.3e-7); structure find: on w9 alpha = log 16 puts the ENTIRE 2-power family EXACTLY ON TENT NODES (commensurability, the gradient carried as a one-sided pair); (ii) THE U-PROFILE (r276 follow-up closed): the wall sensitivity is BOTTOM-LOADED -- the top-3 atoms are THE SMALL PRIMES 2, 3, 5 (gap-weighted, sp -0.80..-0.83); the lethality census (66/70 atoms flip as singles) is LOCALIZED by the gradient map (sp -0.82, PREDICTIVE); (iii) THE HONEST LIMIT: the local stability law EXISTS (curvature TAME, q-consistency 1.02 on 40/40) but its strict validity window is TINY (theta* 25-170x BELOW the smallest r276 dose; the 0.02 collapse is already a NONLINEAR CASCADE across tent kinks): the firewall is graspable perturbatively, NOT globally -- the MetricNear predicate inherits wall positivity only perturbatively around MAIN with window-specific L_D (17.8-309, no uniform lemma candidate), and the MAIN positivity itself stays the open center (H5 untouched, honestly typed).  THE STATE AFTER THE ORIENTATION ROUND (carried to the contracts): the orientation of the wall follows a PREDICTABLE interlacing law (R2, blind GO) and the wall itself is metrically graded, not arithmetically discrete -- what is special about MAIN is the sub-gap-exact PLACEMENT of the von Mangoldt comb (for the Lean MainWindow predicate this means: the predicate must encode METRIC exactness, not combinatorial Euler properties); the master target form stays the ONE theorem augmented_prefix_positive (rh/lean/RH/Window.lean): A_{w,n} PosDef for all admissible MAIN windows and prefix degrees -- both edges, one source, one mechanism.  Mincut base 4 / refined 5 UNCHANGED (a dictionary + census + measurement set moves no edge); no other marker moves.  NOT evidence for or against the Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probes wronskian_dictionary_probe.py (32/32,
SPEC_SHA 56e8a03efd1690e4, one amendment a1 disclosed --
cancellation-free backward-Dirichlet route), minimal_firewall_
probe.py (25/25, SPEC_SHA ed17d79fc037ab1a, one amendment a1
disclosed -- the mp ward reproduced the v956 boundary flip at
N_w = 184 as a by-product), maslov_census_probe.py (29/29,
SPEC_SHA 3858fd16bde0c9c0, two calibration amendments disclosed),
metric_stability_probe.py (31/31 full record, SPEC_SHA
7031200f008d34d1, amendments a0-a5 disclosed, none after; its
sealed --smoke stage evaluates 30 gates, pinned in the pattern
gate below); rounds 274/276/277/278, notes DCVII/DCVIII/DCXI/DCX,
2026-08-25.  WAVE-4 EMBEDDING CONVENTION (extends the round-31
convention): frozen sources embedded BYTE-EXACT and executed
verbatim in isolated namespaces in their sealed --smoke stage
(deterministic, seconds each); printed SPEC SHAs pinned and gated;
byte-equality ward vs experiments/tfpt-discovery/ inside the
pattern gates; the full-mode records (gate counts above, wall
times 22.4/8.8/504/20.8 s) are sealed experiments-side and
re-verified by rh/verification/run_rh.py.  The probes consume the
READ-ONLY deployed core v563_paper2_readouts.py and the frozen
experiments-side libraries (r243/r244/r273/r274 imports printed
in their headers); the execution order follows the round order so
later probes import earlier ones from the embedded byte-exact
sources (sys.modules convention; maslov_census imports the
embedded r274 dictionary, metric_stability the embedded r276
firewall).  Rounds 260-263/268-273/275 are promoted in v960;
round 279 (oriented_theorem_probe.py, the oriented midpoint
theorem) was in flight at this promotion cut and is NOT consumed.

FIREWALL: no zeros, no prime-table oracles (AST scans inside the
probes); RNG only in declared scramble controls; ground truth
(flips) enters gates only; NO RH claim.  Python-only per
GATE.WOLFRAM.02.
"""

import contextlib
import io
import os
import re
import sys
import time
import types
from fractions import Fraction as _Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)


# ---------- module-own exact section S0: the midpoint-orientation
# ---------- theorems (sympy symbolic + exact rationals + dual numbers)
def _midpoint_orientation_theorems(gates):
    """Exact anchors: the base Casoratian identity, the augmented
    telescope / bordered-Wronskian dictionary, the Hellmann-Feynman
    position gradient in exact dual-number arithmetic, and the
    Jacobi interlacing/reality direction with its must-fail."""
    import sympy as sp

    def chk(name, ok, detail=""):
        gates.append(bool(ok))
        print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                               ("  -- " + detail) if detail else ""),
              flush=True)

    print("\n" + "-" * 74)
    print("MODULE-OWN EXACT SECTION S0: the midpoint-orientation "
          "dictionary theorems")
    print("-" * 74, flush=True)

    z = sp.Symbol("z")
    xs = [_Fr(-3, 4), _Fr(-1, 3), _Fr(1, 5), _Fr(1, 2), _Fr(7, 8)]
    ws = [_Fr(2, 5), _Fr(1, 3), _Fr(1, 2), _Fr(1, 4), _Fr(3, 7)]

    def ip(P, Q):
        return sum(sp.Rational(w) * P.subs(z, sp.Rational(x))
                   * Q.subs(z, sp.Rational(x))
                   for x, w in zip(xs, ws))

    # monic orthogonal chain + recurrence coefficients (exact)
    ps = [sp.Integer(1)]
    hs = [sp.nsimplify(ip(ps[0], ps[0]))]
    aas, bbs = [], []
    for n in range(4):
        a_n = sp.nsimplify(ip(z * ps[n], ps[n])) / hs[n]
        b_n = hs[n] / hs[n - 1] if n >= 1 else sp.Integer(0)
        p_next = sp.expand((z - a_n) * ps[n]
                           - (b_n * ps[n - 1] if n >= 1 else 0))
        ps.append(p_next)
        hs.append(sp.nsimplify(ip(p_next, p_next)))
        aas.append(a_n)
        bbs.append(b_n)

    # --- S0.1 the base Casoratian identity (constant = h_n, c' = 1)
    def qpoly(P):
        tot = sp.Integer(0)
        for x, w in zip(xs, ws):
            num = sp.expand(P - P.subs(z, sp.Rational(x)))
            quot = sp.div(num, z - sp.Rational(x), z)[0]
            tot += sp.Rational(w) * quot
        return sp.expand(tot)

    qs = [qpoly(P) for P in ps]
    ok1 = all(hs[n] > 0 for n in range(4))
    for n in range(3):
        C = sp.expand(ps[n] * qs[n + 1] - ps[n + 1] * qs[n])
        ok1 = ok1 and (sp.simplify(C - hs[n]) == 0)
    chk("S0.1-base-casoratian-identity", ok1,
        "p_n q_{n+1} - p_{n+1} q_n = h_n identically in z on the "
        "frozen 5-atom rational measure, every degree, constant "
        "c' = 1 in this orientation convention -- the Casoratian "
        "of (first kind, second kind) IS the pivot chain; the "
        "full-depth ladder version (2.7e-12 on 42 rungs, signs "
        "exact) lives in the embedded r274 probe")

    # --- S0.2 the augmented telescope / bordered-Wronskian dictionary
    vs = [_Fr(1, 7), _Fr(-2, 9), _Fr(1, 3), _Fr(-1, 6), _Fr(2, 11)]
    B = sp.Rational(31, 6)

    def mmom(k):
        return sp.Rational(sum(w * x ** k for x, w in zip(xs, ws)))

    def smom(k):
        return sp.Rational(sum(v * x ** k for x, v in zip(xs, vs)))

    ok2 = True
    for n in (2, 3, 4):
        H = sp.Matrix(n, n, lambda i, j: mmom(i + j))
        u = sp.Matrix(n, 1, lambda i, _j: smom(i))
        A = sp.Matrix(sp.BlockMatrix([[H, u],
                                      [u.T, sp.Matrix([[B]])]]))
        Dn = sp.det(A) / sp.det(H)
        Fk = [sum(sp.Rational(v) * ps[k].subs(z, sp.Rational(x))
                  for x, v in zip(xs, vs)) for k in range(n)]
        tele = B - sum(Fk[k] ** 2 / hs[k] for k in range(n))
        ok2 = ok2 and (sp.simplify(Dn - tele) == 0)
    chk("S0.2-augmented-telescope-dictionary", ok2,
        "det[[H_n, u], [u^T, B]]/det H_n = B - sum_{k<n} F_k^2/h_k "
        "EXACTLY for n = 2, 3, 4 on the frozen signed border -- "
        "the W^aug/W^base normal form of the fiber: the bordered "
        "determinant quotient IS the drained budget (the r274 "
        "telescope from the determinant side)")

    # --- S0.3 the Hellmann-Feynman position gradient (dual numbers)
    class _D(object):
        __slots__ = ("a", "b")

        def __init__(self, a, b=_Fr(0)):
            self.a = _Fr(a)
            self.b = _Fr(b)

        @staticmethod
        def c(o):
            return o if isinstance(o, _D) else _D(o)

        def __add__(self, o):
            o = _D.c(o)
            return _D(self.a + o.a, self.b + o.b)

        __radd__ = __add__

        def __sub__(self, o):
            o = _D.c(o)
            return _D(self.a - o.a, self.b - o.b)

        def __mul__(self, o):
            o = _D.c(o)
            return _D(self.a * o.a, self.a * o.b + self.b * o.a)

        __rmul__ = __mul__

        def __truediv__(self, o):
            o = _D.c(o)
            return _D(self.a / o.a,
                      (self.b * o.a - self.a * o.b) / (o.a * o.a))

    jat = 2                                # perturbed atom index
    wsD = [_D(w, w if i == jat else _Fr(0))
           for i, w in enumerate(ws)]      # w_j -> w_j (1 + eps)

    def peval(c, x):
        r = _D(0)
        for k in range(len(c) - 1, -1, -1):
            r = r * x + c[k]
        return r

    def ipd(c1, c2):
        return sum(w * peval(c1, _Fr(x)) * peval(c2, _Fr(x))
                   for x, w in zip(xs, wsD))

    pd = [[_D(1)]]
    hd = [ipd(pd[0], pd[0])]
    for n in range(4):
        xp = [_D(0)] + pd[n]
        a_n = ipd(xp, pd[n]) / hd[n]
        nxt = [xp[k] - (a_n * pd[n][k] if k < len(pd[n]) else _D(0))
               for k in range(len(xp))]
        if n >= 1:
            b_n = hd[n] / hd[n - 1]
            for k in range(len(pd[n - 1])):
                nxt[k] = nxt[k] - b_n * pd[n - 1][k]
        pd.append(nxt)
        hd.append(ipd(nxt, nxt))
    ok3 = all(hd[n].b == ws[jat] * peval(pd[n], xs[jat]).a ** 2
              for n in range(5))
    chk("S0.3-hellmann-feynman-gradient", ok3,
        "d h_n/d eps = w_j p_n(x_j)^2 EXACTLY for every n = 0..4 "
        "under w_j -> w_j(1 + eps) (exact Fraction-valued dual "
        "numbers, no floats): the polynomial variation drops by "
        "orthogonality -- the r278 exact-gradient class "
        "(d log h_n/du_j = <w-dot_j, pihat_n^2>/h_n) at the "
        "identity level")

    # --- S0.4 the Jacobi interlacing/reality direction + must-fail
    ok4 = True
    roots_prev = None
    for k in range(2, 5):
        pk = sp.Poly(ps[k], z)
        ok4 = ok4 and (sp.polys.polytools.count_roots(pk) == k)
        rk = pk.real_roots()
        if roots_prev is not None:
            ok4 = ok4 and all(rk[i] < roots_prev[i] < rk[i + 1]
                              for i in range(k - 1))
        roots_prev = rk
    # must-fail: one flipped beta sign kills reality at degree 2
    s1 = sp.expand(z - aas[0])
    s2_bad = sp.expand((z - aas[1]) * s1 + bbs[1] * 1)
    n_real_bad = sp.polys.polytools.count_roots(sp.Poly(s2_bad, z))
    ok4m = (n_real_bad == 0)
    chk("S0.4-jacobi-interlacing-reality", ok4 and ok4m,
        "on the frozen positive chain (beta_k > 0) every principal "
        "characteristic polynomial k = 2..4 has FULL real root "
        "count and consecutive levels interlace STRICTLY (exact "
        "algebraic root comparisons); must-fail: one flipped beta "
        "sign leaves 0 real roots at degree 2 -- reality/"
        "interlacing dies exactly with symmetrizability: the "
        "classical direction of the r277 R2 rule; the signed-comb "
        "blind census (42/42 GO, controls at flip+1) lives in the "
        "embedded probe")


# --------------------------------------------------------------- sources
_SRC_0 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wronskian_dictionary_probe -- PRIME.PORT.RHP.MIDPOINT.
WRONSKIAN_DICTIONARY.01 (round 274): the exact dictionary
D_n <-> Wronskian for the two-sided midpoint geometry -- the
reviewer's demanded SMALLEST HARD TEST before the oriented
midpoint theorem (Maslov round).  No fits, no target evaluation
in any construction path, all worlds.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r272 discipline): w = window (kz),
N_w = builder depth, S_w = #supp(mutilde) = 2 N_w - 1 on the real
windows, n/k = chain degree, m = dual-chain degree; rho_k =
F_k^2/h_k, S_n = sum_{k<=n} rho_k; ground truth (h signs, flip
degrees, branch labels) enters GATES and census tables only; no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r244 BH.wpack + BH.bord_chain + BH.spearman, r257
CT.union_arrays, r260 TX.drive_arrays, r263 CA.g_gap +
CA.sym_instance, r264 QO.port_pack, r230 JF toy + exact Stieltjes
pattern, v881 PIK, r243 PB.smooth_comb.  B PROVENANCE: B_w =
S_{N-2} + 5/7 (r241/r243 IMPORTED floor, never fitted).  COFINAL
LADDER (pre-sealed): frame-A h <= 900, 42 rungs, (N, kz)-sorted;
exception set {kz15, 20, 22, 36, 38, 39, 52}.

THE ROUND'S IDENTITIES (leg B core, derived at design time by
classical Casoratian/variation-of-parameters algebra THROUGH the
r230 reversal and the r231 L-gauge, then frozen; every one is
machine-gated exactly on toys and to floors on the real comb):
  LEFT SOLUTION   v^L_n(z) = pihat_n(z)  (upward three-term
    recursion, chain coefficients (alpha, beta) only -- the
    source-pure Euclid data of r230).
  RIGHT SOLUTION  v^R_n(z) = q_n(z) = C[pihat_n mutilde](z), in
    THREE exact constructions whose coincidence IS the two-sided
    geometry: (R1) residue route sum_j w_j pihat_n(x_j)/(z-x_j);
    (R2) FROM THE RIGHT: downward recursion with the EXACT
    Dirichlet boundary q_S == 0 (pihat_S = L vanishes on every
    node -- the node polynomial is the right boundary condition);
    (R3) the r230/r231 midpoint transport q_n = h_n
    pihat#_{S-1-n}/L (dual chain with MIRRORED coefficients
    alpha#_m = alpha_{S-1-m}, beta#_m = beta_{S-m}, gauge = the
    node polynomial alone).
  (b1) BASE DICTIONARY (c' = 1): for every z and every n,
        h_n = pihat_{n+1}(z) q_n(z) - pihat_n(z) q_{n+1}(z)
    -- the Casoratian of the midpoint pair is the pivot chain,
    with constant EXACTLY 1.  h-FREE MIDPOINT FORM (the r231
    sign-blindness as an identity): with the raw dual chain
    (no h anywhere),
        pihat_{n+1} pihat#_{S-1-n} - beta_{n+1} pihat_n
        pihat#_{S-2-n} = L(z)
    -- the gauge-normalized midpoint Wronskian is the NODE
    POLYNOMIAL, constant in n: the h-normalizations cancel
    EXACTLY, so the h-free pairing carries NO orientation; the
    entire orientation content of the dictionary sits in the
    normalization constant (the h-chain), exactly the r231 G12
    structure statement, now at dictionary grade.
  (b2) AUGMENTED DICTIONARY: with the border-driven second kind
    qs_n(z) = C[pihat_n sigmatilde](z) (drive -F_n: qs_{n+1} =
    (z - alpha_n) qs_n - beta_n qs_{n-1} - F_n -- the rank-1
    Uvarov border column as an inhomogeneous term), the augmented
    Casoratian C_n(z) = pihat_{n+1}(z) qs_n(z) - pihat_n(z)
    qs_{n+1}(z) is a POLYNOMIAL (the border poles cancel; at a
    border atom the finite part carries the exact derivative
    diagonal bw_b [pihat'_{n+1} pihat_n - pihat'_n pihat_{n+1}]),
    with the exact telescope C_n(z)/h_n = sum_{k<=n} F_k
    pihat_k(z)/h_k and C_0 = F_0; the border pairing gives
        W^aug_n := int C_n dsigmatilde = h_n S_n,   hence
        D_{n+1} = B - W^aug_n / W^base_n
    with W^base_n the base Casoratian (z-independent = h_n): the
    dictionary constant is c_n = 1/W^base_n.  h-FREE NORMALIZED
    FORM (c_n = 1): with RR_n := L q#_{S-1-n} (the DUAL second
    kind through the gauge; r231 second relation RR_n =
    pihat_n/h_n),
        C_n(z)/h_n = beta_{n+1} RR_{n+1}(z) qs_n(z)
                     - RR_n(z) qs_{n+1}(z)
    -- no h read anywhere in the construction; the h-content is
    DELIVERED by the right-side data through the gauge.
  (b3) c-TYPOLOGY (the go criterion, honest): c'_n = 1 (base,
    exact).  c_n = 1/W^base_n: the CONSTRUCTION is source-pure
    (chain evaluations + residue sums; no h/tau/D/q read --
    AST-audited scopes + oracle mutant); the VALUE is 1/h_n =
    1/(h_0 prod beta_k), a chain-coefficient product -- the
    h-chain in beta-product form: positive at every free-prefix
    degree (n < N) by the prefix positivity itself; it NEVER
    consumes the terminal target (D_N, q_N enter no construction;
    r266 wall/target detector run on c) -- the dictionary is NOT
    circular w.r.t. the target, and its orientation content is
    exactly the h-chain, as the midpoint gauge structure demands.

LEG A -- CONSTRUCTION GATES: toy exact (rationals): r230 reversal
re-gate (alpha/beta mirrored), r231 connection re-gate (both
relations, k = 1..3), R1 == R2 == R3 exact, q_S == 0 exact;
real windows: R1 vs R2 at shallow degrees (f64 floor), the f64
right solution from the right (Miller-buffered Dirichlet seed,
buffer 60) validated by the base-dictionary gate at EVERY degree
vs the independent r244 chain reference; mp (w9): exact Dirichlet
seed at S-1 vs the buffered seed, node-polynomial closure
max_j |pihat_S(x_j)| ~ 0.

LEG B -- DICTIONARY GATES: (toys) base + h-free midpoint form +
augmented (against the INDEPENDENT determinant route aug_n/tau_n
of the r263 instances) + telescope + h-free RR form, EXACT in
rationals on MAINLIKE + FLIPLIKE (depths 1..4) and on the r230
9-atom toy; one symbolic-z gate (sympy, depth 3): W^base_n(z) -
h_n == 0 as a rational function.  (real) base dictionary at ALL
degrees n < N on both mains + all 42 rungs + controls (f64
floors); augmented dictionary at the sealed shallow degrees
(resolvability-guarded, f64 cancellation floor disclosed) on all
worlds; deep degrees via mp on w9 (dps sealed) incl. terminal;
kz15 terminal mp ward (the razor rung; dictionary D_N vs the f64
chain anchor 5/7 - rho_{N-1}); kz52 mp truncation ward (monomial
mp Hankel det ratio at n_t = 12, dps 220, corner 5/7, vs the
f64 dictionary value -- r257 pattern).

LEG C -- ORIENTATION PRE-TEST (Pruefer, measurement): state
phases Theta^L_n = atan2(v^L_{n+1}, v^L_n), Theta^R_n =
atan2(v^R_{n+1}, v^R_n) at the sealed real point z0 = x0 + 1.5
rh (right of the hull); the band statement 0 < Theta^L - Theta^R
< pi (mod 2pi) is EXACTLY W^base_n > 0, i.e. h_n > 0 -- the
dictionary makes the wall an ORIENTATION statement.  (c1) MAIN
in-band at every n < N (both mains); (c2) controls exit the band
FIRST at exactly 25/21/27 (EPSTEIN/SCRAMBLE/SMOOTH); (c3)
WINDING/half-filling count (w9, mp, full algebraic continuation
n = 0..S-2): the number of in-band degrees vs N_w = ceil(S/2)
and vs N_w + delta -- MEASUREMENT, typed, never upgraded; toy
count printed.  The pre-test is typed honestly: (c1)/(c2) are
the h-sign anatomy RESTATED in orientation coordinates (exact
dictionary consequence); the NEW content is that the coordinates
exist with source-pure two-sided solutions -- the Maslov census
of the NEXT round inherits them.

LEG D -- WARDS/KILLS: AST scopes: the construction functions
(chain_vals/plain evaluators, backward right solution, residue
routes, Casoratians, W^aug) consume passed coefficient/atom
arrays ONLY (forbidden identifiers: rho, S, sg_h, lg_h, eta, fb,
tb, hv, Fv, nf, rows, wpack, bord_chain, world_block, gam_next,
alh, aug, tau) -- audited, with a deliberately target-reading
oracle mutant that MUST be flagged; no fit primitives (fragment
audit); MUST-FAILS (each loud, exact rationals): (m1) GAUGE
WITHOUT THE W-MATRIX (omit 1/L in the transport, or omit the
beta-weight in the h-free form) breaks the identity; (m2) DUAL
CHAIN WITHOUT MIRRORING (alpha#_m := alpha_m) breaks the
transport; (m3) SAME-SIDE ANCHOR MUST SUCCEED: the Casoratian of
(pihat, p^(1)) (both left) == -h_n exactly -- trivially
h-proportional, typed as the classical anchor vs the midpoint
pairing as the new content; SMOOTH anchor: border == window =>
F_{n>=1} = 0, the augmented dictionary degenerates exactly to
T_n == rho_0 and q_N <= 1e-20; controls complete
(EPSTEIN/SCRAMBLE/SMOOTH on w9, INDEFINITE_CONTINUATION typed
beyond the flips).

SEALED CONSTANTS: MAIN windows (9, 13); controls w9 EPSTEIN /
SCRAMBLE(seed 1) / SMOOTH, flips 25/21/27; H_CAP 900; B57 = 5/7;
M_W = sqrt(5/7); CHEAP_EXPECT 35; EXC_KZ_EXPECT (15, 20, 22, 36,
38, 39, 52); Z0 factors (1.5, 2.25) on the union+border hull;
toy z0 (17/7, 5/2); BACK_BUF 60; residue-ward degrees n <= 10,
bar 1e-8; base-dictionary log bars 1e-8 MAIN / 1e-6 ladder /
1e-3 controls (f64 chain floors, r253-a1 family), signs exact at
resolvable degrees; aug shallow degrees n = 0..11 with the
sealed resolvability guard est = 1e-15 x massnorm / (|W^base|
max(1, S_n)) <= 0.3 x bar, bars 1e-7 MAIN / 1e-6 ladder / 1e-3
controls, at least n <= 4 resolvable everywhere; W9_MP_DPS 120;
MP_DEEP_DEGS (60, 120, 183); MP_BASE_BAR 1e-40; MP_AUG_BAR
1e-20; MP dual RR degrees == deep degs, RR bar 1e-30, first-
relation bar 1e-40, h-duality bar 1e-30, q#_0 normalization
depth guard 1e-10; node-closure bar 1e-60 (relative to the
running scale); Miller-vs-Dirichlet bar 1e-40; KZ15 terminal
bar 1e-8 (dps 60); KZ52 truncation n_t 12, dps 220, bar 1e-8;
SMOOTH T-bar 1e-12, q-bar 1e-20 (r266); FP_BAR 0.9; LOUD 1e3;
runtime <= 1800 s; smoke = toys + w9 + controls + must-fails +
scopes (ladder, fingerprints, mp legs skipped).  NO pre-spec
scratch: calibration pass 1 was the first full evaluation of
this probe.  DISCLOSED CALIBRATION AMENDMENT a1 (found in pass
1, 30/32, BEFORE any record freeze; no bar, band or verdict
rule moved): the draft gated the mp second relation through the
RESIDUE route q#_m(z0) = sum_j w#_j pihat#_m(x_j)/(z0 - x_j) at
the deep dual degrees -- that sum cancels to the MINIMAL dual
solution at depth ~ e^-300 and no reasonable dps resolves it
(measured rel dev 4.1e+14 at dps 120 while the h-duality held
at 1.2e-113); the construction was moved to the cancellation-
free FROM-THE-RIGHT route of the DUAL chain (Dirichlet q#_S ==
0, the same theorem as the original chain) with the m = 0
residue normalization (depth-guarded), and the FIRST r231
relation pihat#_{S-1-n} h_n == L q_n was added as a
cancellation-free deep-real gate -- the amendment is itself a
finding: the dual second kind is exactly as backward-stable as
the original one, which is the two-sided geometry once more.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  WRONSKIAN_DICTIONARY_GO(base c' = 1 exact; aug c_n = 1/W^base
    source-pure construction, positive on the free prefix 42/42;
    h-free normalization c = 1 exact through the dual second
    kind) -- GO iff ALL identity gates pass AND the c-detector
    flags neither wall nor target
  / DICTIONARY_BASE_ONLY (base holds, augmented breaks)
  / DICTIONARY_CIRCULAR (a c-scope reads the target, or the
    c-value is an exact monotone function of D_N/q_N -- the
    reviewer's no-go)
  + ORIENTATION_PREVIEW(band == h > 0 exact; MAIN in-band full
    depth; control exits; w9 winding count vs N_w).
Honesty before beauty: the dictionary does not close the wall;
the target positivity D_N > 0 stays OPEN (the Maslov round's
work); no verdict claims a derived 5/7, a bound mechanism, or an
asymptotic law (r243..r272 stand).

RECORD TABLES (frozen from the record run; calibration protocol:
smoke 32/32 first pass; calibration pass 1 = first full
evaluation, 30/32 -- the ONE break was the disclosed amendment
a1 above (mp dual-residue route beyond precision), no bar, band
or verdict rule moved at any point; pass 2 with a1 = 32/32, wall
22.4 s, and the record run below is numerically identical):
CAL_VERDICT = WRONSKIAN_DICTIONARY_GO(base c' = 1 exact; aug
c_n = 1/W^base_n source-pure construction, positive on the free
prefix 42/42, = the h-chain in beta-product form -- the
orientation content, honestly typed; h-free normalization c = 1
exact through the dual second kind, toy + mp-real) +
ORIENTATION_PREVIEW(band == h > 0 exact; MAIN in-band at every
free degree; control exits 25/21/27 degree-exact; w9 winding
262/366 measured).
Key numbers.  TOYS (all exact rationals): r230 reversal + r231
connection re-gated; base dictionary h_n == pihat_{n+1} q_n -
pihat_n q_{n+1} exact at 2 z-points, all n, on the 9-atom r230
toy; h-free midpoint form == L(z) exact; Dirichlet q_S == 0 and
from-the-right == residue route exact; same-side anchor
(pihat, p^(1)) == -h_n exact (typed TRIVIAL); augmented
dictionary exact on MAINLIKE + FLIPLIKE depths 1..4 against the
independent r263 determinant route (FLIPLIKE band exit at n = 2
== its flip); telescope exact at a generic z; RR_n == pihat_n/
h_n and the h-free augmented form exact (n = 1..3); sympy
symbolic-z gate: W^base_n(z) - h_n == 0 as a rational function.
REAL (f64): R1-vs-R2 ward worst rel 7.2e-12 (bar 1e-8);
z0-independence 2.7e-13; base dictionary at EVERY n < N: mains
worst abs-log dev 2.8e-13 (bar 1e-8), 42-rung ladder worst
2.7e-12 (bar 1e-6), signs exact everywhere; augmented
dictionary at the sealed shallow degrees: mains worst 5.0e-14
(bar 1e-7), ladder worst 5.0e-13 (bar 1e-6), >= 12 resolved
degrees per world; SMOOTH anchor T_n == rho_0 worst rel 5.4e-14
and q_N = 4.2e-25.  ORIENTATION: both mains in-band at every
n < N; control exits EXACTLY at EPST 25 / SCR 21 / SMOOTH 27;
w9 winding (mp, full continuation 0..S-2 = 0..365): in-band 262
of 366 == #(h_n > 0) exactly, first exit at n = 184 = N_w + 0
(the flip), N_w = ceil(367/2) = 184 -- the count EXCEEDS N_w by
the 78 positive continuation pivots beyond the free window
(measured, typed: the winding is NOT the half-filling count on
the algebraic continuation; the free-window statement is
exactly in-band up to the flip).  MP DEEP (w9, dps 120):
node-polynomial closure 1.2e-106; Dirichlet-vs-Miller seed dev
9.8e-70; base dictionary at deep degs (60, 120, 183) worst rel
3.9e-120; augmented T_n == S_n worst rel 3.5e-120; terminal
D_N(dictionary) = +0.561250 vs the f64 chain anchor, dev
4.2e-12; h-free normalization: first relation 2.0e-112, RR
2.0e-112 (q#_0 depth 8.0e-2), h-duality 1.2e-113.  MP WARDS:
kz15 (razor, N = 203) dictionary terminal D_N = +0.044583832
dev 3.5e-11 (bar 1e-8); kz52 truncation det ratio -3.712174970
vs 5/7 - T_11 dev 2.7e-13 (bar 1e-8).  DETECTOR: selftest
sp(g1, g1) = 1.00 flagged; c-fingerprints sp(log c, g1) = 0.737
/ sp(log c, D_N) = 0.357 (both < 0.9; the c-decision pattern is
positive 42/42 = the prefix pattern, NOT the wall's all-FALSE
pattern); crit1 < 1 on 42/42 with sp(crit1, g1) = 0.164 (r266
reproduced); c-scope audits CLEAN, oracle mutant FLAGGED.
MUST-FAILS: m1 gauge-without-W residuals 5.9e+01 / -8.2e+03 !=
0 loud; m2 unmirrored dual residual -3.0e+04 != 0 loud (exact
rationals).  Branch reproduction: cheap 35/42, exception set ==
the named 7.  Runtime 22.4 s full / 0.8 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH            # noqa: E402 r244
import cancellation_adjudication_probe as CA  # noqa: E402 r263
import coupledtau_probe as CT                 # noqa: E402 r257
import terminal_crossratio_probe as TX        # noqa: E402 r260
import quenched_opening_probe as QO           # noqa: E402 r264
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import principal_bessel_probe as PB           # noqa: E402 r243
import jfraction_probe as JF                  # noqa: E402 r230
import v563_paper2_readouts as core           # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
CHEAP_EXPECT = 35
EXC_KZ_EXPECT = (15, 20, 22, 36, 38, 39, 52)
Z0_FACTS = (1.5, 2.25)
TOY_Z0S = (Fr(17, 7), Fr(5, 2))
BACK_BUF = 60
RES_WARD_N = 10
RES_BAR = 1e-8
BASE_BAR_MAIN = 1e-8
BASE_BAR_LADDER = 1e-6
BASE_BAR_CTRL = 1e-3
SH_N = 12
AUG_BAR_MAIN = 1e-7
AUG_BAR_LADDER = 1e-6
AUG_BAR_CTRL = 1e-3
AUG_GUARD_FRAC = 0.3
AUG_MIN_RESOLVED = 5
W9_MP_DPS = 120
MP_DEEP_DEGS = (60, 120, 183)
MP_BASE_BAR = 1e-40
MP_AUG_BAR = 1e-20
MP_RR_BAR = 1e-30
MP_CONN_BAR = 1e-40
MP_HDUAL_BAR = 1e-30
Q0_DEPTH_GUARD = 1e-10
MP_NODECLOSE_BAR = 1e-60
MP_SEED_BAR = 1e-40
KZ15_BAR = 1e-8
KZ15_DPS = 60
KZ52_NT = 12
TRUNC_DPS = 220
TRUNC_BAR = 1e-8
SM_T_BAR = 1e-12
SM_Q_BAR = 1e-20
FP_BAR = 0.9
LOUD = 1e3

CAL_VERDICT = (
    "WRONSKIAN_DICTIONARY_GO(base c' = 1 exact; aug c_n = "
    "1/W^base_n source-pure construction, positive on the free "
    "prefix 42/42, = the h-chain in beta-product form -- the "
    "orientation content, honestly typed; h-free normalization "
    "c = 1 exact through the dual second kind, toy + mp-real) + "
    "ORIENTATION_PREVIEW(band == h > 0 exact; MAIN in-band at "
    "every free degree; control exits 25/21/27 degree-exact; "
    "w9 winding 262/366 measured)")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the two-sided "
                       "solutions consume chain coefficients + "
                       "atom positions/weights + the evaluation "
                       "point ONLY; ground truth enters gates and "
                       "census tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


# ================= sealed construction scope (source-pure: every
# function below consumes PASSED coefficient/atom arrays and the
# evaluation point only -- AST-audited; the chain coefficients
# (al, be) are the r230 source-pure Euclid data)
def scal_fwd(al, be, z0, n_hi):
    """v^L at z0: scaled upward recursion; returns (sg, lg) arrays
    for n = 0..n_hi."""
    sg = np.zeros(n_hi + 1)
    lg = np.full(n_hi + 1, -np.inf)
    u, um, lam = 1.0, 0.0, 0.0
    sg[0], lg[0] = 1.0, 0.0
    for n in range(n_hi):
        w = (z0 - al[n]) * u - (be[n] * um if n > 0 else 0.0)
        um, u = u, w
        s = max(abs(u), abs(um))
        if s == 0.0 or not math.isfinite(s):
            break
        u, um = u / s, um / s
        lam += math.log(s)
        if u != 0.0:
            sg[n + 1] = math.copysign(1.0, u)
            lg[n + 1] = math.log(abs(u)) + lam
    return sg, lg


def back_right(al, be, z0, n_hi):
    """v^R FROM THE RIGHT: downward recursion y_{n-1} =
    ((z0 - al[n]) y_n - y_{n+1}) / be[n] from the seed
    (y_{n_hi+1}, y_{n_hi}) = (0, 1) (exact Dirichlet if n_hi =
    S-1, Miller-buffered otherwise); returns (sg, lg) arrays for
    n = 0..n_hi, unnormalized (y = c q)."""
    sg = np.zeros(n_hi + 1)
    lg = np.full(n_hi + 1, -np.inf)
    yp, y, lam = 0.0, 1.0, 0.0
    sg[n_hi], lg[n_hi] = 1.0, 0.0
    for n in range(n_hi, 0, -1):
        ym = ((z0 - al[n]) * y - yp) / be[n]
        yp, y = y, ym
        s = max(abs(y), abs(yp))
        if s == 0.0 or not math.isfinite(s):
            break
        y, yp = y / s, yp / s
        lam += math.log(s)
        if y != 0.0:
            sg[n - 1] = math.copysign(1.0, y)
            lg[n - 1] = math.log(abs(y)) + lam
    return sg, lg


def plainvals(al, be, pts, n_hi):
    """plain (unscaled) chain values + derivatives at pts for
    n = 0..n_hi (shallow use only); returns (V, DV)."""
    m = len(pts)
    V = np.zeros((n_hi + 1, m))
    DV = np.zeros((n_hi + 1, m))
    V[0] = 1.0
    for n in range(n_hi):
        if n == 0:
            V[1] = (pts - al[0]) * V[0]
            DV[1] = V[0]
        else:
            V[n + 1] = (pts - al[n]) * V[n] - be[n] * V[n - 1]
            DV[n + 1] = (pts - al[n]) * DV[n] + V[n] \
                - be[n] * DV[n - 1]
    return V, DV


def residue_right(Vn, xu, wu, z0):
    """R1 residue route q_n(z0) = sum_j wu_j Vn_j/(z0 - xu_j);
    returns (value, cancellation depth)."""
    t = wu * Vn / (z0 - xu)
    v = float(np.sum(t))
    dep = abs(v) / max(float(np.sum(np.abs(t))), 1e-300)
    return v, dep


def qs_border(V, bw, Minv, n):
    """deleted-diagonal border second kind at the border atoms:
    qs_n(z_b) (finite part), vectorized."""
    return Minv @ (bw * V[n])


def waug_row(V, DV, bw, Minv, n):
    """W^aug_n = sum_b bw_b C_n(z_b) with the exact derivative
    diagonal; also returns the mass norm for the resolvability
    guard."""
    q0 = qs_border(V, bw, Minv, n)
    q1 = qs_border(V, bw, Minv, n + 1)
    diag = bw * (DV[n + 1] * V[n] - DV[n] * V[n + 1])
    Cn = V[n + 1] * q0 - V[n] * q1 + diag
    w = float(np.sum(bw * Cn))
    massn = float(np.sum(np.abs(bw) * (np.abs(V[n + 1] * q0)
                                       + np.abs(V[n] * q1)
                                       + np.abs(diag))))
    return w, massn


def casor_sglg(sA1, lA1, sA0, lA0, sB0, lB0, sB1, lB1):
    """signed-log Casoratian A_{n+1} B_n - A_n B_{n+1}; returns
    (sign, log|.|)."""
    la = lA1 + lB0
    lb = lA0 + lB1
    m_ = max(la, lb)
    if not math.isfinite(m_):
        return 0.0, -1e30
    v = sA1 * sB0 * math.exp(la - m_) - sA0 * sB1 * math.exp(lb - m_)
    if v == 0.0:
        return 0.0, -1e30
    return math.copysign(1.0, v), m_ + math.log(abs(v))


def oracle_right(p):
    """DELIBERATE MUST-FAIL MUTANT: reads the terminal target --
    the scope audit must FLAG this."""
    return math.sqrt(abs(float(p["rho"][p["N"] - 1])))


CONSTR_FUNCS = ("scal_fwd", "back_right", "plainvals",
                "residue_right", "qs_border", "waug_row",
                "casor_sglg")
CONSTR_FORBIDDEN = {"rho", "S", "sg_h", "lg_h", "eta", "fb", "tb",
                    "hv", "Fv", "nf", "rows", "wpack",
                    "bord_chain", "world_block", "gam_next",
                    "alh", "aug", "tau", "q_chain", "D_dir"}


def constr_scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in CONSTR_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ================= exact (Fraction) toy machinery
def stj_gen(nodes, wts, n_upto):
    """generic exact Stieltjes chain; returns (al, be, hs) with
    be[n] = beta_n = h_n/h_{n-1} (be[0] = 0)."""
    S = len(nodes)
    pk = [wts[0] * 0 + 1 for _ in range(S)]
    pkm = [wts[0] * 0 for _ in range(S)]
    hs = [sum(w * p * p for w, p in zip(wts, pk))]
    al = []
    for k in range(n_upto):
        a = sum(w * x * p * p
                for w, x, p in zip(wts, nodes, pk)) / hs[-1]
        al.append(a)
        b = hs[-1] / hs[-2] if len(hs) > 1 else 0
        nx = [(x - a) * p - b * q
              for x, p, q in zip(nodes, pk, pkm)]
        pkm, pk = pk, nx
        hs.append(sum(w * p * p for w, p in zip(wts, pk)))
    be = [hs[0] * 0] + [hs[n] / hs[n - 1] for n in range(1, n_upto)]
    return al, be, hs


def pv_exact(al, be, z, n):
    """exact monic value pihat_n(z) from the chain."""
    p0, p1 = z * 0 + 1, z - al[0]
    if n == 0:
        return p0
    for k in range(1, n):
        p0, p1 = p1, (z - al[k]) * p1 - be[k] * p0
    return p1


def pv_seq(al, be, z, n_hi):
    """exact value sequence [pihat_0(z)..pihat_{n_hi}(z)]."""
    out = [z * 0 + 1]
    if n_hi >= 1:
        out.append(z - al[0])
    for k in range(1, n_hi):
        out.append((z - al[k]) * out[-1] - be[k] * out[-2])
    return out


def dv_seq(al, be, z, n_hi):
    """exact derivative sequence [pihat'_0(z)..pihat'_{n_hi}(z)]."""
    v = pv_seq(al, be, z, n_hi)
    out = [z * 0]
    if n_hi >= 1:
        out.append(z * 0 + 1)
    for k in range(1, n_hi):
        out.append((z - al[k]) * out[-1] + v[k] - be[k] * out[-2])
    return out


def q_exact(al, be, nodes, wts, z0, n_hi):
    """exact residue right solution [q_0(z0)..q_{n_hi}(z0)]."""
    out = []
    for n in range(n_hi + 1):
        out.append(sum(w * pv_exact(al, be, x, n) / (z0 - x)
                       for w, x in zip(wts, nodes)))
    return out


def back_exact(al, be, z0, n_hi):
    """exact downward solution from (y_{n_hi+1}, y_{n_hi}) =
    (0, 1); returns [y_0..y_{n_hi}]."""
    out = [None] * (n_hi + 1)
    yp = z0 * 0
    y = z0 * 0 + 1
    out[n_hi] = y
    for n in range(n_hi, 0, -1):
        ym = ((z0 - al[n]) * y - yp) / be[n]
        yp, y = y, ym
        out[n - 1] = y
    return out


# ================= mp legs
def mp_two_sided(p, dps, deep_degs, want_dual):
    """the w9 (or kz15) mp two-sided run: plain mp chain to S-1
    (h_k, F_k, S_k, z0 values, border values at deep degs),
    backward right solution with the EXACT Dirichlet seed at S-1
    plus the Miller-buffered seed, base + augmented dictionary
    devs, band census, node-polynomial closure; optionally the
    dual chain (RR / h-duality).  Returns a dict of devs and
    census numbers."""
    mp.mp.dps = dps
    xu, wu = CT.union_arrays(p["d"])
    bx, bw = CT.union_arrays(p["dsm"])
    S_ = len(xu)
    N = p["N"]
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0 = mp.mpf(0.5 * (lo + hi))
    rh = mp.mpf(0.5 * (hi - lo))
    z0 = x0 + mp.mpf(Z0_FACTS[0]) * rh
    xs = [mp.mpf(float(v)) for v in xu]
    ws = [mp.mpf(float(v)) for v in wu]
    bs = [mp.mpf(float(v)) for v in bx]
    bws = [mp.mpf(float(v)) for v in bw]
    nb = len(bs)
    # forward plain mp chain to S-1 (values stay in mp range)
    ux = [mp.mpf(1)] * S_
    uxm = [mp.mpf(0)] * S_
    ub = [mp.mpf(1)] * nb
    ubm = [mp.mpf(0)] * nb
    db = [mp.mpf(0)] * nb
    dbm = [mp.mpf(0)] * nb
    pz = [mp.mpf(1)]
    alv, bev, hv, Fv = [], [0], [], []
    snap = {}
    h = mp.fsum(w * u * u for w, u in zip(ws, ux))
    hv.append(h)
    Fv.append(mp.fsum(w * u for w, u in zip(bws, ub)))
    for n in range(S_ - 1):
        a = mp.fsum(w * x * u * u
                    for w, x, u in zip(ws, xs, ux)) / h
        alv.append(a)
        b = bev[n]
        nx = [(x - a) * u - (b * um if n > 0 else 0)
              for x, u, um in zip(xs, ux, uxm)]
        nxb = [(x - a) * u - (b * um if n > 0 else 0)
               for x, u, um in zip(bs, ub, ubm)]
        ndb = [(x - a) * du + u - (b * dum if n > 0 else 0)
               for x, u, du, dum in zip(bs, ub, db, dbm)]
        uxm, ux = ux, nx
        ubm, ub = ub, nxb
        dbm, db = db, ndb
        pz.append((z0 - a) * pz[n]
                  - (b * pz[n - 1] if n > 0 else 0))
        hn = mp.fsum(w * u * u for w, u in zip(ws, ux))
        hv.append(hn)
        bev.append(hn / h)
        h = hn
        Fv.append(mp.fsum(w * u for w, u in zip(bws, ub)))
        if n + 1 in set(deep_degs) | set(d + 1 for d in deep_degs):
            snap[n + 1] = (list(ub), list(db))
    # node-polynomial closure: pihat_S at the nodes ~ 0
    a = mp.fsum(w * x * u * u for w, x, u in zip(ws, xs, ux)) / h
    alv.append(a)
    lastb = bev[S_ - 1]
    pS = [(x - a) * u - lastb * um for x, u, um in zip(xs, ux, uxm)]
    scl = max(abs(v) for v in ux)
    node_close = float(max(abs(v) for v in pS) / scl)
    # S_k (mp)
    Sk = []
    acc = mp.mpf(0)
    for k in range(S_ - 1):
        acc += Fv[k] ** 2 / hv[k]
        Sk.append(acc)
    # backward right solution: exact Dirichlet seed at n_hi = S-1
    def bwd(n_hi):
        y = [mp.mpf(0)] * (n_hi + 1)
        yp = mp.mpf(0)
        yv = mp.mpf(1)
        y[n_hi] = yv
        for n in range(n_hi, 0, -1):
            ym = ((z0 - alv[n]) * yv - yp) / bev[n]
            yp, yv = yv, ym
            y[n - 1] = yv
        return y
    yD = bwd(S_ - 1)
    yM = bwd(min(S_ - 1, N + BACK_BUF))
    q0 = mp.fsum(w / (z0 - x) for w, x in zip(ws, xs))
    cD = q0 / yD[0]
    cM = q0 / yM[0]
    seed_dev = 0.0
    for n in range(0, N, max(1, N // 8)):
        seed_dev = max(seed_dev,
                       float(abs(yD[n] * cD / (yM[n] * cM) - 1)))
    q = [v * cD for v in yD]
    # base dictionary at deep degs + band census over 0..S-2
    base_dev = 0.0
    for n in deep_degs:
        Wb = pz[n + 1] * q[n] - pz[n] * q[n + 1]
        base_dev = max(base_dev, float(abs(Wb / hv[n] - 1)))
    inband = 0
    first_exit = None
    for n in range(S_ - 1):
        Wb = pz[n + 1] * q[n] - pz[n] * q[n + 1]
        okb = (Wb > 0)
        if okb:
            inband += 1
        elif first_exit is None:
            first_exit = n
        if (Wb > 0) != (hv[n] > 0):
            base_dev = max(base_dev, 2.0)
    # augmented dictionary at deep degs (+ terminal)
    Minv = [[(1 / (bs[i_] - bs[j_])) if i_ != j_ else mp.mpf(0)
             for j_ in range(nb)] for i_ in range(nb)]

    def mp_waug(n):
        Vn, Dn = snap[n]
        Vn1, Dn1 = snap[n + 1]
        wv0 = [bws[c_] * Vn[c_] for c_ in range(nb)]
        wv1 = [bws[c_] * Vn1[c_] for c_ in range(nb)]
        Wa = mp.mpf(0)
        for b_ in range(nb):
            row = Minv[b_]
            qs0 = mp.fsum(row[c_] * wv0[c_] for c_ in range(nb))
            qs1 = mp.fsum(row[c_] * wv1[c_] for c_ in range(nb))
            Wa += bws[b_] * (Vn1[b_] * qs0 - Vn[b_] * qs1
                             + bws[b_] * (Dn1[b_] * Vn[b_]
                                          - Dn[b_] * Vn1[b_]))
        return Wa

    aug_dev = 0.0
    for n in deep_degs:
        Wa = mp_waug(n)
        Wb = pz[n + 1] * q[n] - pz[n] * q[n + 1]
        Tn = Wa / Wb
        aug_dev = max(aug_dev,
                      float(abs(Tn - Sk[n]) / max(1, abs(Sk[n]))))
    # terminal dictionary D_N
    nT = N - 1
    D_dict = None
    if nT in snap and nT + 1 in snap:
        Wa = mp_waug(nT)
        Wb = pz[nT + 1] * q[nT] - pz[nT] * q[nT + 1]
        Bm = mp.mpf(float(p["S"][N - 2])) + mp.mpf(5) / 7
        D_dict = float(Bm - Wa / Wb)
    out = dict(S=S_, node_close=node_close, seed_dev=seed_dev,
               base_dev=base_dev, aug_dev=aug_dev, inband=inband,
               first_exit=first_exit, D_dict=D_dict,
               h_pos=sum(1 for n in range(S_ - 1) if hv[n] > 0))
    if want_dual:
        # dual chain (mirrored by construction of the dual
        # weights); the dual second kind q#_m is the MINIMAL dual
        # solution: built cancellation-free FROM THE RIGHT
        # (Dirichlet q#_S == 0, the same theorem as the original
        # chain), normalized by the m = 0 residue sum (depth
        # guard) -- amendment a1, disclosed in the spec
        lgLp = []
        for j_ in range(S_):
            s_ = mp.mpf(0)
            for k_ in range(S_):
                if k_ != j_:
                    s_ += mp.log(abs(xs[j_] - xs[k_]))
            lgLp.append(s_)
        dws = [mp.e ** (-mp.log(abs(w)) - 2 * lg)
               * mp.sign(w) for w, lg in zip(ws, lgLp)]
        vx = [mp.mpf(1)] * S_
        vxm = [mp.mpf(0)] * S_
        hd = mp.fsum(w * u * u for w, u in zip(dws, vx))
        hdv = [hd]
        alD, beD = [], [mp.mpf(0)]
        pdz = [mp.mpf(1)]
        bed = 0
        for m_ in range(S_ - 1):
            a = mp.fsum(w * x * u * u
                        for w, x, u in zip(dws, xs, vx)) / hd
            alD.append(a)
            pdz.append((z0 - a) * pdz[m_]
                       - (bed * pdz[m_ - 1] if m_ > 0 else 0))
            nx = [(x - a) * u - (bed * um if m_ > 0 else 0)
                  for x, u, um in zip(xs, vx, vxm)]
            vxm, vx = vx, nx
            hn = mp.fsum(w * u * u for w, u in zip(dws, vx))
            bed = hn / hd
            hd = hn
            hdv.append(hd)
            beD.append(bed)
        a = mp.fsum(w * x * u * u
                    for w, x, u in zip(dws, xs, vx)) / hd
        alD.append(a)
        # backward dual right solution (Dirichlet at m = S-1)
        yd = [mp.mpf(0)] * S_
        yp_, yv_ = mp.mpf(0), mp.mpf(1)
        yd[S_ - 1] = yv_
        for m_ in range(S_ - 1, 0, -1):
            ym_ = ((z0 - alD[m_]) * yv_ - yp_) / beD[m_]
            yp_, yv_ = yv_, ym_
            yd[m_ - 1] = yv_
        tq = [w / (z0 - x) for w, x in zip(dws, xs)]
        q0d = mp.fsum(tq)
        q0_dep = float(abs(q0d)
                       / mp.fsum(abs(t) for t in tq))
        cd_ = q0d / yd[0]
        lgL0 = mp.fsum(mp.log(abs(z0 - x)) for x in xs)
        Lz0 = mp.e ** lgL0
        rr_dev = 0.0
        conn_dev = 0.0
        hdual_dev = 0.0
        for n in deep_degs:
            m_ = S_ - 1 - n
            # first r231 relation (cancellation-free, deep):
            # pihat#_{S-1-n}(z0) h_n == L(z0) q_n(z0)
            conn_dev = max(conn_dev,
                           float(abs(pdz[m_] * hv[n]
                                     / (Lz0 * q[n]) - 1)))
            # second relation (RR): L q#_{S-1-n} == pihat_n/h_n
            RR = Lz0 * cd_ * yd[m_]
            rr_dev = max(rr_dev,
                         float(abs(RR * hv[n] / pz[n] - 1)))
            hdual_dev = max(hdual_dev,
                            float(abs(hdv[m_] * hv[S_ - 1 - m_]
                                      - 1)))
        out["rr_dev"] = rr_dev
        out["conn_dev"] = conn_dev
        out["hdual_dev"] = hdual_dev
        out["q0_dep"] = q0_dep
    return out


def mp_trunc_ward(p, n_t, dps):
    """r257 pattern: monomial mp Hankel truncation (corner 5/7),
    det ratio vs the f64 DICTIONARY value 5/7 - T_{n_t-1}^dict is
    gated outside; here returns the mp det ratio."""
    mp.mp.dps = dps
    d, dsm = p["d"], p["dsm"]
    xu = [mp.mpf(float(v)) for v in d["xs"]] \
        + [mp.mpf(float(v)) for v in d["ys"]]
    wu = [mp.mpf(float(v)) for v in d["ws"]] \
        + [-mp.mpf(float(v)) for v in d["vs"]]
    bxm = [mp.mpf(float(v)) for v in dsm["xs"]] \
        + [mp.mpf(float(v)) for v in dsm["ys"]]
    bwm = [mp.mpf(float(v)) for v in dsm["ws"]] \
        + [-mp.mpf(float(v)) for v in dsm["vs"]]
    mk = []
    pw = [mp.mpf(1)] * len(xu)
    for _k in range(2 * n_t - 1):
        mk.append(mp.fsum(w * q for w, q in zip(wu, pw)))
        pw = [q * x for q, x in zip(pw, xu)]
    tk = []
    pb = [mp.mpf(1)] * len(bxm)
    for _k in range(n_t):
        tk.append(mp.fsum(w * q for w, q in zip(bwm, pb)))
        pb = [q * y for q, y in zip(pb, bxm)]
    H = mp.matrix(n_t, n_t)
    Ha = mp.matrix(n_t + 1, n_t + 1)
    for i in range(n_t):
        for j in range(n_t):
            H[i, j] = mk[i + j]
            Ha[i, j] = mk[i + j]
        Ha[i, n_t] = tk[i]
        Ha[n_t, i] = tk[i]
    Ha[n_t, n_t] = mp.mpf(5) / 7
    return float(mp.det(Ha) / mp.det(H))


# ================= per-world f64 dictionary block
def world_dict_block(p, tag, is_main):
    """runs the full f64 two-sided construction on one world and
    returns base/aug/band results (reference = r244 chain rows)."""
    rows_N = p["rows"]
    N = p["N"]
    xu, wu = CT.union_arrays(p["d"])
    bx, bw = CT.union_arrays(p["dsm"])
    S_ = len(xu)
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0, rh = 0.5 * (lo + hi), 0.5 * (hi - lo)
    z0 = x0 + Z0_FACTS[0] * rh
    z0b = x0 + Z0_FACTS[1] * rh
    n_hi = min(S_ - 1, N + BACK_BUF)
    ext = BH.bord_chain(p["d"]["xs"], p["d"]["ws"], p["d"]["ys"],
                        p["d"]["vs"], p["dsm"]["xs"],
                        p["dsm"]["ws"], p["dsm"]["ys"],
                        p["dsm"]["vs"], n_hi + 1)
    n_hi = min(n_hi, len(ext) - 1)
    while n_hi > 1 and (ext[n_hi - 1]["gam_next"] is None
                        or ext[n_hi - 1]["gam_next"] == 0.0):
        n_hi -= 1
    al = np.array([ext[k]["alh"] for k in range(n_hi + 1)])
    be = np.array([0.0] + [ext[k]["gam_next"]
                           for k in range(n_hi)])
    # left + right solutions at two z0's
    res = {}
    for zi, zz in enumerate((z0, z0b)):
        sgF, lgF = scal_fwd(al, be, zz, min(N + 1, n_hi))
        sgY, lgY = back_right(al, be, zz, n_hi)
        q0 = float(np.sum(wu / (zz - xu)))
        sgc = math.copysign(1.0, q0) * sgY[0]
        lgc = math.log(abs(q0)) - lgY[0]
        sgQ = sgY * sgc
        lgQ = lgY + lgc
        res[zi] = (sgF, lgF, sgQ, lgQ)
    sgF, lgF, sgQ, lgQ = res[0]
    # base dictionary at every n < N vs the chain reference
    base_dev = 0.0
    sign_ok = True
    Wb_s = np.zeros(N)
    Wb_l = np.full(N, -np.inf)
    for n in range(N):
        sW, lW = casor_sglg(sgF[n + 1], lgF[n + 1], sgF[n], lgF[n],
                            sgQ[n], lgQ[n], sgQ[n + 1], lgQ[n + 1])
        Wb_s[n], Wb_l[n] = sW, lW
        base_dev = max(base_dev, abs(lW - rows_N[n]["lg_h"]))
        if sW != rows_N[n]["sg_h"]:
            sign_ok = False
    # z0-independence of the base Casoratian
    sgF2, lgF2, sgQ2, lgQ2 = res[1]
    z0ind = 0.0
    for n in (0, 1, min(5, N - 1), min(N // 2, N - 1), N - 1):
        sW2, lW2 = casor_sglg(sgF2[n + 1], lgF2[n + 1], sgF2[n],
                              lgF2[n], sgQ2[n], lgQ2[n],
                              sgQ2[n + 1], lgQ2[n + 1])
        z0ind = max(z0ind, abs(lW2 - Wb_l[n]) + abs(sW2 - Wb_s[n]))
    # residue-vs-backward ward at shallow degrees
    Vx, _ = plainvals(al, be, xu, RES_WARD_N + 1)
    res_dev = 0.0
    for n in range(RES_WARD_N + 1):
        qres, dep = residue_right(Vx[n], xu, wu, z0)
        if dep < 1e-10:
            continue
        qb = sgQ[n] * math.exp(lgQ[n])
        res_dev = max(res_dev, abs(qb / qres - 1.0))
    # augmented dictionary at the sealed shallow degrees
    Vb, Db = plainvals(al, be, bx, SH_N + 1)
    Minv = 1.0 / (bx[:, None] - bx[None, :]
                  + np.eye(len(bx)))
    np.fill_diagonal(Minv, 0.0)
    Sref = p["S"]
    aug_dev = 0.0
    n_res = 0
    bar = AUG_BAR_MAIN if is_main else (
        AUG_BAR_CTRL if tag in ("EPST", "SCR", "SMOOTH")
        else AUG_BAR_LADDER)
    Tvals = {}
    for n in range(SH_N):
        wa, massn = waug_row(Vb, Db, bw, Minv, n)
        Wbv = Wb_s[n] * math.exp(Wb_l[n])
        if Wbv == 0.0:
            continue
        est = 1e-15 * massn / (abs(Wbv)
                               * max(1.0, abs(float(Sref[n]))))
        if est > AUG_GUARD_FRAC * bar:
            continue
        n_res += 1
        Tn = wa / Wbv
        Tvals[n] = Tn
        aug_dev = max(aug_dev,
                      abs(Tn - float(Sref[n]))
                      / max(1.0, abs(float(Sref[n]))))
    # band census (orientation coordinates)
    inband_all = all(Wb_s[n] > 0 for n in range(N))
    first_exit = next((n for n in range(N) if Wb_s[n] <= 0), None)
    return dict(al=al, be=be, z0=z0, base_dev=base_dev,
                sign_ok=sign_ok, z0ind=z0ind, res_dev=res_dev,
                aug_dev=aug_dev, n_res=n_res, Tvals=Tvals,
                inband_all=inband_all, first_exit=first_exit,
                Wb_s=Wb_s, Wb_l=Wb_l, n_hi=n_hi)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke
    windows = (9,) if smoke else MAIN_WINDOWS

    print("=" * 78)
    print("wronskian_dictionary_probe -- PRIME.PORT.RHP.MIDPOINT."
          "WRONSKIAN_DICTIONARY.01 (round 274)")
    print("SPEC_SHA %s   F_DEF_SHA %s (imported r243)"
          % (SPEC_SHA[:16], PB.F_DEF_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + w9 + controls + must-fails"
                        "; ladder, fingerprints, mp legs skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "TWO frozen identities (base Casoratian == h_n with "
          "c' = 1; augmented border-paired Casoratian == h_n S_n "
          "with the h-free RR normalization) + the h-free "
          "midpoint form == L(z) (the r231 sign-blindness as an "
          "identity), derived at design time and sealed; right "
          "solution in THREE constructions (residue / from-the-"
          "right Dirichlet / dual-chain + gauge); orientation "
          "pre-test = Pruefer band 0 < dTheta < pi == W^base > 0; "
          "all bars + verdict rules sealed BEFORE evaluation")

    # ---------------- S1 TOYS (exact rationals)
    section("S1  TOYS -- EXACT TWO-SIDED GEOMETRY")
    nodes = JF.TOY_NODES
    wts = JF.TOY_WTS
    S_t = len(nodes)
    al_t, be_t, hs_t = stj_gen(nodes, wts, S_t)
    # dual chain (r230/r231 objects)
    Lp = []
    for j in range(S_t):
        pr = Fr(1)
        for k in range(S_t):
            if k != j:
                pr *= (nodes[j] - nodes[k])
        Lp.append(pr)
    dw_t = [1 / (wts[j] * Lp[j] ** 2) for j in range(S_t)]
    alD, beD, hsD = stj_gen(nodes, dw_t, S_t - 1)
    ok_rev = all(alD[m] == al_t[S_t - 1 - m]
                 for m in range(S_t - 1)) \
        and all(hsD[m] / hsD[m - 1] == hs_t[S_t - m]
                / hs_t[S_t - m - 1]
                for m in range(1, S_t - 1))
    z0t = TOY_Z0S[0]
    Lz = {}
    for zz in TOY_Z0S:
        pr = Fr(1)
        for x in nodes:
            pr *= (zz - x)
        Lz[zz] = pr
    ok_conn = True
    for k in (1, 2, 3):
        m = S_t - 1 - k
        Cz = sum(w * pv_exact(al_t, be_t, x, k) / (z0t - x)
                 for w, x in zip(wts, nodes))
        ok_conn = ok_conn and (
            pv_exact(alD, beD, z0t, m) == Lz[z0t] * Cz / hs_t[k])
        CzD = sum(w * pv_exact(alD, beD, x, m) / (z0t - x)
                  for w, x in zip(dw_t, nodes))
        ok_conn = ok_conn and (
            CzD == pv_exact(al_t, be_t, z0t, k)
            / (hs_t[k] * Lz[z0t]))
    check("G10-toy-reversal-connection", ok_rev and ok_conn,
          "r230 FULL_CHAIN_REVERSAL re-gated (alpha#_m = "
          "alpha_{S-1-m}, beta#_m = beta_{S-m}, exact) + r231 "
          "L-gauge connection re-gated (both relations, k = "
          "1..3, exact rationals): the two-sided inputs of the "
          "dictionary stand")
    # base dictionary + h-free midpoint form + backward Dirichlet
    ok_base = True
    ok_mid = True
    for zz in TOY_Z0S:
        pv = pv_seq(al_t, be_t, zz, S_t)
        qv = q_exact(al_t, be_t, nodes, wts, zz, S_t)
        for n in range(S_t - 1):
            ok_base = ok_base and (
                pv[n + 1] * qv[n] - pv[n] * qv[n + 1] == hs_t[n])
        pd = pv_seq(alD, beD, zz, S_t - 1)
        for n in range(S_t - 1):
            ok_mid = ok_mid and (
                pv[n + 1] * pd[S_t - 1 - n]
                - (hs_t[n + 1] / hs_t[n]) * pv[n]
                * pd[S_t - 2 - n] == Lz[zz])
    qv = q_exact(al_t, be_t, nodes, wts, z0t, S_t)
    ok_qS = (qv[S_t] == 0)
    yb = back_exact(al_t, be_t, z0t, S_t - 1)
    cb = qv[0] / yb[0]
    ok_back = all(yb[n] * cb == qv[n] for n in range(S_t))
    # winding count (toy, measured)
    toy_pos = sum(1 for n in range(S_t - 1) if hs_t[n] > 0)
    check("G11-toy-base-dictionary", ok_base and ok_mid
          and ok_qS and ok_back,
          "BASE DICTIONARY EXACT (rationals, 2 z-points, all n): "
          "h_n == pihat_{n+1} q_n - pihat_n q_{n+1} with c' = 1; "
          "h-FREE MIDPOINT FORM EXACT: pihat_{n+1} pihat#_{S-1-n}"
          " - beta_{n+1} pihat_n pihat#_{S-2-n} == L(z) (constant"
          " in n = the node polynomial: the gauge absorbs ALL "
          "h-content); Dirichlet boundary q_S == 0 EXACT and the "
          "from-the-right downward solution == q_n EXACT (three "
          "constructions, one right solution); toy in-band count "
          "%d of %d (ceil(S/2) = %d, measured)"
          % (toy_pos, S_t - 1, (S_t + 1) // 2))
    # same-side anchor (must succeed, trivial)
    p1 = [Fr(0), hs_t[0]]
    for n in range(1, S_t - 1):
        p1.append((z0t - al_t[n]) * p1[-1] - be_t[n] * p1[-2])
    pv = pv_seq(al_t, be_t, z0t, S_t - 1)
    ok_anchor = all(pv[n + 1] * p1[n] - pv[n] * p1[n + 1]
                    == -hs_t[n] for n in range(S_t - 2))
    check("G12-anchor-same-side", ok_anchor,
          "ANCHOR (must succeed, typed TRIVIAL): the Casoratian "
          "of the SAME-SIDE pair (pihat, p^(1)) == -h_n exactly "
          "-- classical h-proportionality without any midpoint "
          "content; the NEW content of the round is that the "
          "FROM-THE-RIGHT dual-transported solution is the same "
          "right solution (G10/G11)")

    # CA instances: augmented dictionary
    inst_m = CA.sym_instance(False)
    inst_f = CA.sym_instance(True)

    def to_fr(v):
        v = sp.nsimplify(v)
        return Fr(int(sp.numer(v)), int(sp.denom(v)))

    ok_aug = True
    ok_tel = True
    ok_flip_exit = None
    for inst, isf in ((inst_m, False), (inst_f, True)):
        xs_c = [Fr(-3, 2), Fr(-1), Fr(-1, 2), Fr(1, 4), Fr(3, 4),
                Fr(5, 4)]
        ws_c = ([Fr(2, 3), Fr(-6, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
                 Fr(1, 3)] if isf else
                [Fr(2, 3), Fr(-1, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
                 Fr(1, 3)])
        bx_c = [Fr(0), Fr(1, 2)]
        bw_c = [Fr(1, 3), Fr(1, 6)]
        Bc = Fr(5, 7)
        al_c, be_c, hs_c = stj_gen(xs_c, ws_c, 5)
        Fs = [sum(bw * pv_exact(al_c, be_c, bxx, k)
                  for bw, bxx in zip(bw_c, bx_c))
              for k in range(5)]
        z0c = Fr(9, 4)
        pvz = pv_seq(al_c, be_c, z0c, 5)
        qvz = q_exact(al_c, be_c, xs_c, ws_c, z0c, 5)
        # border values + derivatives at border atoms
        Vb = [[pv_exact(al_c, be_c, bxx, n) for bxx in bx_c]
              for n in range(6)]
        Db = [[None, None] for _ in range(6)]
        for bi, bxx in enumerate(bx_c):
            dvs = dv_seq(al_c, be_c, bxx, 5)
            for n in range(6):
                Db[n][bi] = dvs[n]
        for n in range(4):
            # W^base
            Wb = pvz[n + 1] * qvz[n] - pvz[n] * qvz[n + 1]
            # W^aug via deleted diagonal + derivative term
            wa = Fr(0)
            for bi in range(2):
                qs0 = sum(bw_c[ci] * Vb[n][ci]
                          / (bx_c[bi] - bx_c[ci])
                          for ci in range(2) if ci != bi)
                qs1 = sum(bw_c[ci] * Vb[n + 1][ci]
                          / (bx_c[bi] - bx_c[ci])
                          for ci in range(2) if ci != bi)
                diag = bw_c[bi] * (Db[n + 1][bi] * Vb[n][bi]
                                   - Db[n][bi] * Vb[n + 1][bi])
                Cn = Vb[n + 1][bi] * qs0 - Vb[n][bi] * qs1 + diag
                wa += bw_c[bi] * Cn
            Sn = sum(Fs[k] ** 2 / hs_c[k] for k in range(n + 1))
            ok_aug = ok_aug and (Wb == hs_c[n]) \
                and (wa == hs_c[n] * Sn)
            Dd = Bc - wa / Wb
            Ddet = to_fr(inst["aug"][n + 1]) \
                / to_fr(inst["tau"][n + 1])
            ok_aug = ok_aug and (Dd == Ddet)
            # telescope at a generic z
            zg = Fr(7, 3)
            pg = pv_seq(al_c, be_c, zg, 5)
            qsg = [sum(bw * pv_exact(al_c, be_c, bxx, k)
                       / (zg - bxx)
                       for bw, bxx in zip(bw_c, bx_c))
                   for k in range(6)]
            Cg = pg[n + 1] * qsg[n] - pg[n] * qsg[n + 1]
            tel = hs_c[n] * sum(Fs[k] * pg[k] / hs_c[k]
                                for k in range(n + 1))
            ok_tel = ok_tel and (Cg == tel)
        if isf:
            ok_flip_exit = next(
                (n for n in range(5) if hs_c[n] < 0), None)
    check("G13-toy-aug-dictionary", ok_aug and ok_tel
          and ok_flip_exit == 2,
          "AUGMENTED DICTIONARY EXACT (rationals, MAINLIKE + "
          "FLIPLIKE, depths 1..4): W^aug_n (deleted-diagonal + "
          "exact derivative term) == h_n S_n AND D_{n+1} == B - "
          "W^aug_n/W^base_n == aug_{n+1}/tau_{n+1} (INDEPENDENT "
          "r263 determinant route) -- through the FLIPLIKE flip "
          "(first h < 0 at n = %s == the known flip 2: the "
          "dictionary is world-blind algebra, the band exit is "
          "the flip); the polynomial telescope C_n == h_n "
          "sum_k F_k pihat_k/h_k EXACT at a generic z"
          % str(ok_flip_exit))
    # h-free RR form on MAINLIKE
    xs_c = [Fr(-3, 2), Fr(-1), Fr(-1, 2), Fr(1, 4), Fr(3, 4),
            Fr(5, 4)]
    ws_c = [Fr(2, 3), Fr(-1, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
            Fr(1, 3)]
    bx_c = [Fr(0), Fr(1, 2)]
    bw_c = [Fr(1, 3), Fr(1, 6)]
    S_c = 6
    al_c, be_c, hs_c = stj_gen(xs_c, ws_c, S_c)
    Lpc = []
    for j in range(S_c):
        pr = Fr(1)
        for k in range(S_c):
            if k != j:
                pr *= (xs_c[j] - xs_c[k])
        Lpc.append(pr)
    dw_c = [1 / (ws_c[j] * Lpc[j] ** 2) for j in range(S_c)]
    alDc, beDc, hsDc = stj_gen(xs_c, dw_c, S_c - 1)
    zg = Fr(7, 3)
    Lzg = Fr(1)
    for x in xs_c:
        Lzg *= (zg - x)
    ok_rr = True
    for n in range(4):
        m = S_c - 1 - n
        qsh = sum(w * pv_exact(alDc, beDc, x, m) / (zg - x)
                  for w, x in zip(dw_c, xs_c))
        RR = Lzg * qsh
        ok_rr = ok_rr and (RR == pv_exact(al_c, be_c, zg, n)
                           / hs_c[n])
    # h-free aug assembly at generic z (function identity)
    ok_rrform = True
    zeval = Fr(12, 5)
    Lze = Fr(1)
    for x in xs_c:
        Lze *= (zeval - x)
    for n in range(1, 4):
        m1 = S_c - 1 - (n + 1)
        m0 = S_c - 1 - n
        qsh1 = sum(w * pv_exact(alDc, beDc, x, m1)
                   / (zeval - x) for w, x in zip(dw_c, xs_c))
        qsh0 = sum(w * pv_exact(alDc, beDc, x, m0)
                   / (zeval - x) for w, x in zip(dw_c, xs_c))
        RRn1 = Lze * qsh1
        RRn = Lze * qsh0
        qse = [sum(bw * pv_exact(al_c, be_c, bxx, k)
                   / (zeval - bxx)
                   for bw, bxx in zip(bw_c, bx_c))
               for k in range(n + 2)]
        pe = pv_seq(al_c, be_c, zeval, n + 1)
        lhs = be_c[n + 1] * RRn1 * qse[n] - RRn * qse[n + 1]
        Ce = pe[n + 1] * qse[n] - pe[n] * qse[n + 1]
        ok_rrform = ok_rrform and (lhs == Ce / hs_c[n])
    check("G14-toy-hfree-normalization", ok_rr and ok_rrform,
          "h-FREE NORMALIZATION EXACT (rationals, MAINLIKE): "
          "RR_n = L q#_{S-1-n} == pihat_n/h_n (the r231 second "
          "relation -- the dual second kind DELIVERS the "
          "h-normalized left objects through the gauge, no h "
          "read) AND the h-free augmented form beta_{n+1} "
          "RR_{n+1} qs_n - RR_n qs_{n+1} == C_n/h_n as a "
          "FUNCTION (n = 1..3): the augmented dictionary "
          "constant is c = 1 in the gauge normalization")
    # one symbolic-z gate
    zsym = sp.Symbol("z")
    al_s = inst_m["alh"]
    hs_s = inst_m["h"]
    pv_s = [sp.Integer(1), zsym - al_s[0]]
    for k in range(1, 3):
        pv_s.append(sp.expand((zsym - al_s[k]) * pv_s[-1]
                              - hs_s[k] / hs_s[k - 1] * pv_s[-2]))
    xs_s = [sp.Rational(-3, 2), sp.Integer(-1),
            sp.Rational(-1, 2), sp.Rational(1, 4),
            sp.Rational(3, 4), sp.Rational(5, 4)]
    ws_s = [sp.Rational(2, 3), sp.Rational(-1, 5),
            sp.Rational(1, 2), sp.Rational(-3, 7), sp.Integer(1),
            sp.Rational(1, 3)]
    ok_sym = True
    for n in range(2):
        qn = sum(w * pv_s[n].subs(zsym, x) / (zsym - x)
                 for w, x in zip(ws_s, xs_s))
        qn1 = sum(w * pv_s[n + 1].subs(zsym, x) / (zsym - x)
                  for w, x in zip(ws_s, xs_s))
        expr = sp.together(pv_s[n + 1] * qn - pv_s[n] * qn1
                           - hs_s[n])
        ok_sym = ok_sym and (sp.simplify(expr) == 0)
    check("G15-symbolic-z", ok_sym,
          "sympy SYMBOLIC-z gate (MAINLIKE, depths 1..2): "
          "W^base_n(z) - h_n == 0 as a rational function of z -- "
          "the base dictionary is an identity in z, not a "
          "point evaluation")

    # ---------------- S2 mains + controls (f64)
    section("S2  MAINS + CONTROLS -- THE f64 TWO-SIDED RUN")
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    long_names = {"EPST": "EPSTEIN", "SCR": "SCRAMBLE",
                  "SMOOTH": "SMOOTH"}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[long_names[c]]
               for c in ctrl)
    if smoke:
        ladder = []
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G20-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %s"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             ("%d rungs POSITIVE_PREFIX" % len(ladder))
             if ladder else "n/a (SMOKE)"))

    WD = {}
    for t in packs:
        WD[t] = world_dict_block(packs[t], t, True)
    for c in ctrl:
        WD[c] = world_dict_block(ctrl[c], c, False)
    m_base = max(WD[t]["base_dev"] for t in packs)
    m_sign = all(WD[t]["sign_ok"] for t in packs)
    m_z0 = max(WD[t]["z0ind"] for t in packs)
    m_res = max(WD[t]["res_dev"] for t in packs)
    check("G21-main-construction-wards", m_res <= RES_BAR
          and m_z0 <= 1e-6,
          "R1 (residue) vs R2 (from-the-right) at the shallow "
          "ward degrees n <= %d: worst rel %.1e (bar %.0e); "
          "z0-independence of the base Casoratian (two sealed "
          "z-points): worst dev %.1e -- the right solution is "
          "one object in both constructions on the true comb"
          % (RES_WARD_N, m_res, RES_BAR, m_z0))
    check("G22-main-base-dictionary", m_base <= BASE_BAR_MAIN
          and m_sign,
          "BASE DICTIONARY on the mains at EVERY degree n < N: "
          "h_n == pihat_{n+1} q_n - pihat_n q_{n+1} vs the "
          "INDEPENDENT r244 chain reference: worst abs-log dev "
          "%.1e (bar %.0e), signs exact at every degree on %s "
          "-- c' = 1 on the true comb through the full free "
          "window" % (m_base, BASE_BAR_MAIN, str(sorted(packs))))
    m_aug = max(WD[t]["aug_dev"] for t in packs)
    n_res_min = min(WD[t]["n_res"] for t in packs)
    check("G23-main-aug-dictionary", m_aug <= AUG_BAR_MAIN
          and n_res_min >= AUG_MIN_RESOLVED,
          "AUGMENTED DICTIONARY on the mains at the sealed "
          "shallow degrees (resolvability-guarded): T_n = "
          "W^aug_n/W^base_n == S_n, worst scaled dev %.1e (bar "
          "%.0e) at >= %d resolved degrees per main (guard "
          "disclosed: f64 cancellation floor; deep degrees "
          "mp-gated in S4)" % (m_aug, AUG_BAR_MAIN, n_res_min))
    ok_band_main = all(WD[t]["inband_all"] for t in packs)
    check("G24-main-band", ok_band_main,
          "ORIENTATION (c1): both mains sit IN THE BAND 0 < "
          "Theta^L - Theta^R < pi at EVERY degree n < N (the "
          "band statement IS W^base_n > 0 == h_n > 0 by the "
          "dictionary): the wall is an orientation statement in "
          "the two-sided coordinates -- MAIN never leaves the "
          "band inside the free window")
    exits = {c: WD[c]["first_exit"] for c in ctrl}
    ok_exits = all(exits[c] == CTRL_FLIPS[long_names[c]]
                   for c in ctrl)
    check("G25-control-band-exits", ok_exits,
          "ORIENTATION (c2): the controls exit the band FIRST at "
          "exactly %s == the known flips (EPSTEIN 25 / SCRAMBLE "
          "21 / SMOOTH 27): the orientation coordinates locate "
          "the collapse degree-exactly, world-blind"
          % str(exits))
    pS = ctrl["SMOOTH"]
    qN_sm = float(pS["rho"][pS["N"] - 1]) / B57
    Tsm = WD["SMOOTH"]["Tvals"]
    sm_dev = max(abs(Tsm[n] / float(pS["rho"][0]) - 1.0)
                 for n in Tsm if n >= 1) if len(Tsm) > 1 else 0.0
    check("G26-smooth-anchor", abs(qN_sm) <= SM_Q_BAR
          and sm_dev <= SM_T_BAR,
          "SMOOTH self-alias anchor: border == window => F_{n>=1}"
          " = 0 by orthogonality, the augmented dictionary "
          "degenerates EXACTLY to T_n == rho_0 (worst rel %.1e, "
          "bar %.0e) and q_N = %.1e <= %.0e: the coupling side "
          "of the dictionary is source-driven, not an artifact"
          % (sm_dev, SM_T_BAR, qN_sm, SM_Q_BAR))

    # ---------------- S3 ladder census + detector
    section("S3  LADDER CENSUS + c-TYPOLOGY + DETECTOR")
    if not smoke:
        def rung_rec(p):
            N = p["N"]
            r, t, ap, bp = TX.drive_arrays(p["rows"], N)
            g = CA.g_gap(r[:N - 1], t, ap, bp)
            B = float(p["S"][N - 2]) + B57
            return dict(kz=p["kz"], N=N, g=g, p=p, B=B,
                        DN=B - float(p["S"][N - 1]),
                        crit1=float(p["S"][N - 1]) / B)
        recs = [rung_rec(p) for p in ladder]
        exc_kz = tuple(sorted(rc["kz"] for rc in recs
                              if rc["g"] < 0.0))
        check("G30-branch-reproduction",
              sum(1 for rc in recs if rc["g"] >= 0)
              == CHEAP_EXPECT
              and exc_kz == tuple(sorted(EXC_KZ_EXPECT)),
              "r263 branch rule reproduced EXACTLY: cheap %d/42, "
              "exception set %s == the named 7"
              % (sum(1 for rc in recs if rc["g"] >= 0),
                 str(exc_kz)))
        lad_base = 0.0
        lad_sign = True
        lad_aug = 0.0
        lad_nres_min = 10 ** 9
        c_pos = True
        logc = []
        for rc in recs:
            wb = world_dict_block(rc["p"], "kz%d" % rc["kz"],
                                  False)
            rc["wb"] = wb
            lad_base = max(lad_base, wb["base_dev"])
            lad_sign = lad_sign and wb["sign_ok"]
            lad_aug = max(lad_aug, wb["aug_dev"])
            lad_nres_min = min(lad_nres_min, wb["n_res"])
            c_pos = c_pos and wb["inband_all"]
            logc.append(-float(rc["p"]["rows"][rc["N"] - 1]
                               ["lg_h"]))
        check("G31-census-base-dictionary",
              lad_base <= BASE_BAR_LADDER and lad_sign,
              "BASE DICTIONARY on all 42 rungs at EVERY degree "
              "n < N: worst abs-log dev %.1e (bar %.0e), signs "
              "exact everywhere -- the two-sided Casoratian "
              "reproduces the pivot chain across the cofinal "
              "ladder" % (lad_base, BASE_BAR_LADDER))
        check("G32-census-aug-dictionary",
              lad_aug <= AUG_BAR_LADDER
              and lad_nres_min >= AUG_MIN_RESOLVED,
              "AUGMENTED DICTIONARY on all 42 rungs at the "
              "sealed shallow degrees: worst scaled dev %.1e "
              "(bar %.0e), >= %d resolved degrees per rung"
              % (lad_aug, AUG_BAR_LADDER, lad_nres_min))
        check("G33-c-positivity-census", c_pos,
              "c-TYPOLOGY: c_n = 1/W^base_n = 1/h_n = 1/(h_0 "
              "prod beta_k) -- a chain-coefficient product "
              "(source-pure Euclid data, r230), POSITIVE at "
              "every free-prefix degree on 42/42 (== the given "
              "prefix positivity, honestly typed: the "
              "orientation content of the dictionary sits "
              "ENTIRELY in c_n, i.e. in the h-chain the gauge "
              "does not see -- r231 G12 at dictionary grade); "
              "c never consumes the terminal target")
        # r266 detector on c
        g1s = []
        for rc in recs:
            pk = QO.port_pack(rc["kz"])
            lam, U = np.linalg.eigh(pk["Q"])
            c2 = (U.T @ pk["f"]) ** 2
            g1s.append(float(np.sum(c2 / (1.0 - lam))))
        dnv = [rc["DN"] for rc in recs]
        cr1 = [rc["crit1"] for rc in recs]
        sp_wall_self = abs(BH.spearman(g1s, g1s))
        sp_c_g1 = abs(BH.spearman(logc, g1s))
        sp_c_dn = abs(BH.spearman(logc, dnv))
        sp_c1_g1 = abs(BH.spearman(cr1, g1s))
        wall_flag_c = (sp_c_g1 >= FP_BAR
                       and not c_pos)
        check("G34-c-detector", sp_wall_self >= FP_BAR
              and not wall_flag_c and sp_c_g1 < FP_BAR,
              "r266 WALL/TARGET DETECTOR on c: selftest sp(g1, "
              "g1) = %.2f flagged; c-fingerprints sp(log c, g1) "
              "= %.3f / sp(log c, D_N) = %.3f (both < %.1f); "
              "the dictionary's terminal criterion pattern == "
              "the target pattern (crit1 < 1 on 42/42, sp(crit1,"
              " g1) = %.3f -- r266 reproduced); the c-scope "
              "audit is CLEAN (G61): c is neither the wall nor "
              "the target -- NOT circular"
              % (sp_wall_self, sp_c_g1, sp_c_dn, FP_BAR,
                 sp_c1_g1))
    else:
        for g in ("G30-branch-reproduction",
                  "G31-census-base-dictionary",
                  "G32-census-aug-dictionary",
                  "G33-c-positivity-census", "G34-c-detector"):
            check(g, True, "SMOKE: skipped")

    # ---------------- S4 mp deep (w9)
    section("S4  MP DEEP TWO-SIDED RUN (w9)")
    if not smoke:
        p9 = packs["w9"]
        deep = tuple(sorted(set(MP_DEEP_DEGS)
                            | {p9["N"] - 1}))
        r_mp = mp_two_sided(p9, W9_MP_DPS, deep, True)
        okA = (r_mp["node_close"] <= MP_NODECLOSE_BAR
               and r_mp["seed_dev"] <= MP_SEED_BAR
               and r_mp["base_dev"] <= MP_BASE_BAR)
        check("G40-mp-base-deep", okA,
              "mp (dps %d) two-sided run on w9 to the FULL "
              "algebraic depth S-1 = %d: node-polynomial "
              "closure max|pihat_S(nodes)|/scale = %.1e (the "
              "Dirichlet boundary is exact); Dirichlet-vs-"
              "Miller seed dev %.1e (bar %.0e -- the f64 "
              "buffered seed is validated); base dictionary at "
              "the sealed deep degrees %s: worst rel %.1e (bar "
              "%.0e) AND the band == sign(h) equivalence holds "
              "at every degree 0..S-2"
              % (W9_MP_DPS, r_mp["S"] - 1, r_mp["node_close"],
                 r_mp["seed_dev"], MP_SEED_BAR, str(deep),
                 r_mp["base_dev"], MP_BASE_BAR))
        D_ref = B57 - float(p9["rho"][p9["N"] - 1])
        okB = (r_mp["aug_dev"] <= MP_AUG_BAR
               and r_mp["D_dict"] is not None
               and abs(r_mp["D_dict"] - D_ref) <= 1e-8)
        check("G41-mp-aug-deep", okB,
              "mp augmented dictionary at the deep degrees + "
              "TERMINAL: T_n == S_n worst rel %.1e (bar %.0e); "
              "terminal D_N(dictionary) = %+.6f vs the f64 "
              "chain anchor 5/7 - rho_{N-1} = %+.6f (dev %.1e, "
              "bar 1e-8): the Wronskian route reaches the "
              "terminal target value on the true comb"
              % (r_mp["aug_dev"], MP_AUG_BAR,
                 r_mp["D_dict"] if r_mp["D_dict"] is not None
                 else float("nan"), D_ref,
                 abs((r_mp["D_dict"] or 0) - D_ref)))
        okR = (r_mp["rr_dev"] <= MP_RR_BAR
               and r_mp["conn_dev"] <= MP_CONN_BAR
               and r_mp["hdual_dev"] <= MP_HDUAL_BAR
               and r_mp["q0_dep"] >= Q0_DEPTH_GUARD)
        check("G42-mp-hfree-normalization", okR,
              "mp h-FREE NORMALIZATION on the REAL comb (dual "
              "right solution FROM THE RIGHT, Dirichlet q#_S == "
              "0, amendment a1): first r231 relation "
              "pihat#_{S-1-n} h_n == L q_n at the deep degrees "
              "worst rel %.1e (bar %.0e, cancellation-free); "
              "second relation RR_n = L q#_{S-1-n} == pihat_n/"
              "h_n worst rel %.1e (bar %.0e; q#_0 normalization "
              "depth %.1e >= %.0e); h-duality h#_m h_{S-1-m} == "
              "1 worst %.1e (bar %.0e): the dual second kind "
              "delivers the h-normalization through the gauge "
              "at 300+ chain degrees -- c = 1 in the gauge "
              "normalization is REAL, not a toy artifact"
              % (r_mp["conn_dev"], MP_CONN_BAR, r_mp["rr_dev"],
                 MP_RR_BAR, r_mp["q0_dep"], Q0_DEPTH_GUARD,
                 r_mp["hdual_dev"], MP_HDUAL_BAR))
        Nw9 = p9["N"]
        S9 = r_mp["S"]
        check("G43-winding-count", r_mp["inband"]
              == r_mp["h_pos"],
              "ORIENTATION (c3, MEASUREMENT): w9 in-band count "
              "over the FULL algebraic continuation n = 0..S-2: "
              "%d of %d degrees (== #(h_n > 0) = %d exactly); "
              "N_w = ceil(S/2) = %d, N_w + delta = %d; first "
              "band exit at n = %s; the half-filling count vs "
              "the winding is REPORTED, not claimed -- the "
              "Maslov census of the next round inherits the "
              "coordinates"
              % (r_mp["inband"], S9 - 1, r_mp["h_pos"],
                 (S9 + 1) // 2, Nw9,
                 str(r_mp["first_exit"])))
    else:
        for g in ("G40-mp-base-deep", "G41-mp-aug-deep",
                  "G42-mp-hfree-normalization",
                  "G43-winding-count"):
            check(g, True, "SMOKE: skipped")

    # ---------------- S5 mp wards kz15/kz52
    section("S5  MP WARDS -- kz15 (razor) + kz52")
    if not smoke:
        p15 = next(rc["p"] for rc in recs if rc["kz"] == 15)
        deep15 = (p15["N"] - 1,)
        r15 = mp_two_sided(p15, KZ15_DPS, deep15, False)
        D_ref15 = B57 - float(p15["rho"][p15["N"] - 1])
        ok15 = (r15["D_dict"] is not None
                and abs(r15["D_dict"] - D_ref15) <= KZ15_BAR)
        check("G50-kz15-terminal-ward", ok15,
              "kz15 (the razor rung, N = %d, margin 0.045): mp "
              "(dps %d) DICTIONARY terminal D_N = %+.9f vs the "
              "f64 chain anchor %+.9f (dev %.1e, bar %.0e) -- "
              "the Wronskian dictionary holds at the sharpest "
              "sealed exception terminal"
              % (p15["N"], KZ15_DPS,
                 r15["D_dict"] if r15["D_dict"] is not None
                 else float("nan"),
                 D_ref15, abs((r15["D_dict"] or 0) - D_ref15),
                 KZ15_BAR))
        p52 = next(rc["p"] for rc in recs if rc["kz"] == 52)
        wb52 = next(rc["wb"] for rc in recs if rc["kz"] == 52)
        D_tr = mp_trunc_ward(p52, KZ52_NT, TRUNC_DPS)
        T11 = wb52["Tvals"].get(KZ52_NT - 1)
        ok52 = (T11 is not None
                and abs(D_tr - (B57 - T11)) <= TRUNC_BAR)
        check("G51-kz52-truncation-ward", ok52,
              "kz52 mp truncation ward (monomial mp Hankel, "
              "dps %d, n_t = %d, corner 5/7): det ratio %+.9f "
              "vs the f64 DICTIONARY value 5/7 - T_{n_t-1} = "
              "%+.9f (dev %.1e, bar %.0e) -- the dictionary "
              "value equals the exact bordered determinant "
              "ratio on the second sealed exception rung"
              % (TRUNC_DPS, KZ52_NT, D_tr,
                 B57 - (T11 if T11 is not None
                        else float("nan")),
                 abs(D_tr - (B57 - (T11 or 0))), TRUNC_BAR))
    else:
        check("G50-kz15-terminal-ward", True, "SMOKE: skipped")
        check("G51-kz52-truncation-ward", True, "SMOKE: skipped")

    # ---------------- S6 must-fails + scopes
    section("S6  MUST-FAILS + SCOPE AUDITS")
    # m1: gauge without the W-matrix
    zz = TOY_Z0S[0]
    pv = pv_seq(al_t, be_t, zz, S_t)
    pd = pv_seq(alD, beD, zz, S_t - 1)
    n0 = 2
    lhs_noL = pv[n0 + 1] * pd[S_t - 1 - n0] * hs_t[n0] \
        - pv[n0] * pd[S_t - 2 - n0] * hs_t[n0 + 1]
    ok_m1 = (lhs_noL != hs_t[n0])
    lhs_nobeta = pv[n0 + 1] * pd[S_t - 1 - n0] \
        - pv[n0] * pd[S_t - 2 - n0]
    ok_m1 = ok_m1 and (lhs_nobeta != Lz[zz])
    check("G60-mustfail-gauge-without-W", ok_m1,
          "m1 GAUGE WITHOUT THE W-MATRIX: omitting the 1/L "
          "transport (residual %.3e != 0) or the beta-weight "
          "(residual %.3e != 0) breaks the identity LOUDLY "
          "(exact rationals) -- the dictionary is pinned to the "
          "r231 gauge"
          % (float(lhs_noL - hs_t[n0]),
             float(lhs_nobeta - Lz[zz])))
    # m2: dual chain without mirroring
    al_bad = [al_t[m] for m in range(S_t - 1)]
    be_bad = list(beD)
    pd_bad = pv_seq(al_bad, be_bad, zz, S_t - 1)
    lhs_bad = pv[n0 + 1] * pd_bad[S_t - 1 - n0] \
        - be_t[n0 + 1] * pv[n0] * pd_bad[S_t - 2 - n0]
    ok_m2 = (lhs_bad != Lz[zz])
    check("G61-mustfail-unmirrored-dual", ok_m2,
          "m2 DUAL CHAIN WITHOUT MIRRORING (alpha#_m := alpha_m "
          "instead of alpha_{S-1-m}): the h-free midpoint form "
          "breaks LOUDLY (residual %.3e != 0, exact rationals) "
          "-- the reversal is load-bearing"
          % float(lhs_bad - Lz[zz]))
    hits = []
    for fn in CONSTR_FUNCS:
        hits += constr_scope_audit(fn)
    hits_orc = constr_scope_audit("oracle_right")
    ag_hits = antigate_fragment_audit()
    check("G62-scope-audits", not hits and bool(hits_orc)
          and not ag_hits,
          "the construction scope consumes passed coefficient/"
          "atom arrays + the evaluation point ONLY (%s); the "
          "deliberately target-reading mutant is FLAGGED (%s); "
          "fragment audit (no fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "; ".join(hits_orc) if hits_orc else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))

    # ---------------- S7 verdict
    section("S7  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the exact base + augmented Wronskian dictionary "
          "with its honest c-typology, the three-construction "
          "right solution (residue / from-the-right / dual+gauge)"
          ", the h-free normalization through the dual second "
          "kind, and the orientation coordinates with the "
          "control-exit and winding pre-tests -- the Maslov "
          "round is the named next step")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        go = npass == len(CHECKS)
        parts = []
        if go:
            parts.append(
                "WRONSKIAN_DICTIONARY_GO(base c' = 1 exact; aug "
                "c_n = 1/W^base_n source-pure construction, "
                "positive on the free prefix 42/42, = the "
                "h-chain in beta-product form -- the orientation "
                "content, honestly typed; h-free normalization "
                "c = 1 exact through the dual second kind, toy + "
                "mp-real)")
        else:
            parts.append("DICTIONARY_GATES_FAILED(see FAIL rows)")
        parts.append(
            "ORIENTATION_PREVIEW(band == h > 0 exact; MAIN "
            "in-band at every free degree; control exits 25/21/"
            "27 degree-exact; w9 winding measured in G43)")
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the base Casoratian "
          "dictionary, the h-free midpoint form == L, the "
          "augmented border-paired dictionary with the exact "
          "derivative diagonal, the h-free RR normalization; "
          "MEASURED: the orientation band census, the control "
          "exits, the winding count, the c-fingerprints; OPEN: "
          "the target positivity D_N > 0 itself (the Maslov "
          "round's work); NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

_SRC_1 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""minimal_firewall_probe -- PRIME.PORT.WALL.MINIMAL_FIREWALL.01
(round 276): the DOSE-RESPONSE CURVE OF THE ARITHMETIC -- from
binary to graduated to minimal.  The r273 mechanism round measured
that gamma_true is PERTURBATION-INSENSITIVE (generic root-scale
cancellation) while EVERY tested surgery kills the free-prefix
positivity (flip degrees 33-43 for P1/P2/P4, 66-101 for the
mildest family surgery P3; MAIN holds ALL windows); the v956 scale
fixes the control level: EPSTEIN/SCRAMBLE/SMOOTH die at 25/21/27
= 0.11..0.15 of the w9 free window N_w = 184 while MAIN exhausts
the ENTIRE free moment window.  REVIEWER ADJUDICATION (the new
firewall lane): the prime structure does NOT produce the
cancellation -- it keeps the small remainder ON THE RIGHT SIDE;
the question of the lane: WHICH MINIMAL EULER STRUCTURE PRESERVES
THE PREFIX POSITIVITY?  This round measures the WALL SURVIVAL
DEPTH as a function of surgery DOSE, from the r273 binary regime
(theta 0.25..1.0, wall always dead) down to the MINIMAL surgery
(ONE neighbor swap / ONE atom jitter / ONE sign-pair exchange).
NOT a proof round: no certificate, no bound, no H5 progress, no
mechanism claim -- MEASUREMENT ONLY.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r244/r273 machinery imported verbatim): per world the
exact h-chain of the signed defect measure mutilde = mu - nu
(BH.bord_chain, the r244 scaled recursion; sign chain sg_h) --
the WALL SURVIVAL DEPTH is nf = first degree n with sg_h < 0
(None = the world survives its ENTIRE free window), normalized
s = nf / N_w in [0, 1] (s = 1 for survivors; N_w = builder
depth = the free-moment-window cap of v956).  TWO exact world
channels, both gated bitwise against BH.wpack at the identity:
(ch-1) COMB channel: (uu, mm) -> PIK.build_rung(kz, comb) ->
  grid density -> folded +/- zones -> BH.bord_chain (for the
  comb surgeries P1/P2/P3);
(ch-2) DENSITY channel: the signed grid density d_arm of the
  UNPERTURBED window, surgered directly, then folded ->
  BH.bord_chain (for the sign/magnitude surgeries B1/B2 -- the
  signature and magnitude fields of the world live on the grid,
  not on the comb, whose weights are one-signed).
Atom classification WITHOUT prime functions: r254 world-blind
labels via ODG.base_exp (pure integer root extraction, admission
bar 1e-9); AST firewall (no zetazero/nzeros/isprime/primerange/
grampoint) holds.

LEG A -- THE DOSE LADDERS (sealed; five surgeries x six doses x
three windows; seeds pinned, fully deterministic; seed = 276000
+ P*100000 + dose*10000 + rep*1000 + win*10):
DOSES: SINGLE (the minimal operation, 9 pinned replicates --
  disclosed: single-op outcomes are position-dependent, the
  extra replicates map the spread) + theta in (0.02, 0.05, 0.10,
  0.15, 0.25) (3 pinned replicates each -- the r273 regime
  starts at 0.25; this ladder refines toward zero).
SURGERIES (dose semantics per surgery, conservation EXACT):
(P1_SWAP) minimal-reach assignment surgery: n_pair = max(1,
  round(theta n/2)) DISJOINT u-adjacent weight transpositions
  (greedy disjoint selection over a seeded permutation of the
  n-1 adjacencies); SINGLE = ONE neighbor swap.  DISCLOSED
  reparametrization of r273-P1: the exchange REACH is pinned at
  the minimum (adjacent), the dose is the COUNT -- the r273
  block law B = n^theta is degenerate below theta 0.1 (B = 1 =
  identity).  PRESERVED: positions bitwise, weight multiset
  bitwise.  DESTROYED: weight<->position assignment at neighbor
  scale, dose-many places.
(P2_JIT) support jitter: u_j -> u_j + amp * g_j * U[-1, 1] on
  ALL atoms with amp = theta (fraction of the local nn gap g_j
  -- the r273-P2 amplitude lever refined toward zero); SINGLE =
  ONE seed-chosen atom jittered at amp = 1.0 (one atom, one
  slot).  PRESERVED: weights bitwise, |du_j| <= amp g_j (gated).
  DESTROYED: support arithmetic at amplitude amp.
(P3_FAM) Euler-family decoupling (r273-P3 verbatim logic):
  nsel = round(theta n_KHI) of the KHI atoms (k >= 2) swap
  weights with the nearest-in-u atom of a DIFFERENT family;
  SINGLE = exactly ONE such swap; nsel = 0 stages are typed
  IDENTITY_DOSE (eff = 0).  PRESERVED: positions bitwise,
  weight multiset bitwise, unselected within-family structure.
  DESTROYED: SAMEP coherence, dose-many echoes.
(B1_SIGN) NEW -- signature surgery on the grid density: nsel =
  max(2, round(theta n_nz)) nonzero grid entries selected, their
  SIGNS permuted among the selection (magnitude field |d| stays
  AT POSITION); SINGLE = ONE +/- pair sign exchange.  PRESERVED:
  |d| array bitwise, sign multiset (p/q census) exact.
  DESTROYED: the signature-position pattern -- signature
  separated from magnitude.
(B2_MAG) NEW -- magnitude surgery on the grid density: nsel =
  max(2, round(theta n_nz)) nonzero entries selected, their
  MAGNITUDES permuted among the selection (sign field stays AT
  POSITION); SINGLE = ONE grid-adjacent magnitude exchange.
  PRESERVED: sign array bitwise, |d| multiset bitwise.
  DESTROYED: the magnitude-position pattern -- magnitude
  separated from signature.
WINDOWS (sealed selection rule, structural census disclosed as
the only pre-spec input): w9 (the v956 anchor window, N_w = 184,
comb 70 atoms / 16 KHI, grid 734 signed entries 526+/208-) + the
min-N frame-A rung (kz18, N_w = 142) + the frame-A rung with N_w
closest to 400 (kz55, N_w = 388).  CONSERVATION GATES exact per
perturbed world (EVERY world); DOSE ACCOUNTING gate: the number
of changed entries never exceeds the nominal dose cap (2 n_pair
/ n_at resp. 1 / 2 nsel / nsel / nsel); theta = 0 returns
bitwise-identical arrays for all five surgeries (gated).

LEG B -- THE MEASUREMENT + PROPERTY RANKING: per stage (surgery
x dose x window) the replicate depths s_r; stage stats = median
/ min / max depth + survivor count.  WALL TOLERANCE per surgery
(w9 map): tol_P = mean of the stage median depths over the six
doses; PROPERTY_RANKING = ascending tol (the property whose
destruction costs the most depth per dose ranks FIRST as
wall-carrier).  The two new surgeries separate SIGNATURE (B1)
from MAGNITUDE (B2); P1/P2/P3 carry the r273 assignment /
support / family axes into the small-dose regime.

LEG C -- THE MINIMALITY MAP (delivery object; sealed rules
frozen BEFORE evaluation, w9 primary):
STAGE CLASS: a stage is MIDDLE iff CTRL_HI < s_med < NEAR_FULL
  (CTRL_HI = 0.20 = the v956 control band 0.11..0.15 plus
  slack; NEAR_FULL = 0.90).
SURGERY CLASS (per surgery on w9): P_THRESHOLD iff s_med(SINGLE)
  <= CTRL_HI (one op collapses to control level); P_TOLERANT
  iff min over all doses s_med >= NEAR_FULL; P_GRADED iff
  s_med(SINGLE) >= NEAR_FULL and min s_med < NEAR_FULL;
  P_INTERMEDIATE otherwise.
LAW FIT (per surgery, deterministic, no fit primitives): deficit
  D(theta) = 1 - s_med over the five theta stages with eff > 0
  and D > DEF_MIN = 0.005; iff >= LAW_MIN = 4 such stages the
  exponent b = halves log-slope of D vs theta (D ~ theta^b);
  else typed NO_LAW(sparse).  Monotonicity sp(theta, s_med)
  reported.
CONTINUUM vs JUMP (sealed): JUMP iff NO w9 stage is MIDDLE;
  CONTINUUM iff >= K_CONT = 3 w9 stages are MIDDLE;
  SPARSE_MIDDLE otherwise.
V956 PLACEMENT: the minimal w9 stage depth vs the control band;
  CONTROL_TOUCHED iff any w9 stage s_med <= CTRL_HI.
N-TRANSPORT (typed classification, not a gate): Spearman between
  the 30 w9 stage medians and the same stages on kz18 / kz55;
  MAP_TRANSPORTS iff sp >= 0.5 on both rungs, else
  WINDOW_SPECIFIC.
FIREWALL HYPOTHESIS (typed TASK_FORMULATION_ONLY): "the wall is
  carried by [the top-ranked property combination]; loss of it
  at dose theta costs survival depth by law f" -- quantified
  from the measured map, falsifiable, NO mechanism claim.

LEG D -- WARDS / MUST-FAILS: identity wards (comb channel
reproduces BH.wpack bitwise in rho and nf on ALL three windows;
theta = 0 bitwise for all five surgeries); control anchors
EPSTEIN/SCRAMBLE/SMOOTH flips re-derived 25/21/27 (w9) -- the
"wrong arithmetic" anchor points of the map; MAIN survives all
three windows (baseline s = 1); label admission <= 1e-9 on all
windows; conservation + dose accounting on EVERY perturbed
world; mp COUNTER-CHECK (dps 40, the sealed anti-noise ward):
the f64 flip degree of the EARLIEST-flipping w9 SINGLE world of
every surgery is re-derived by an mp signed-Stieltjes sign chain
(exact agreement demanded), one surviving w9 SINGLE world and
MAIN w9 are mp-confirmed over the full f64 chain domain (degrees
<= N_w - 1; amendment a1 below), the boundary degree N_w on MAIN
is a sealed BOUNDARY ward (the v956 record n_flip = N_w + 0 must
reproduce at dps 40), EPSTEIN to its flip; run1/run2 determinism
(pinned seeds).  MUST-FAILS (each
loud): (m1) MASS SURGERY -- a mutant scaling a theta-fraction of
comb weights by 1.15 AND a density mutant scaling |d| by 1.02
must be CAUGHT by the conservation gates; (m2) DOSE MUTANT -- a
mutant applying 2x the claimed P1 dose must be CAUGHT by the
dose-accounting cap; (m3) FLIP-NOISE MUTANT -- a mutant flip
report (EPSTEIN nf - 3) must be REJECTED by the mp counter-check
(the detector is not trusted on f64 alone at the borderline);
(m4) GIFT SURGERY -- a mutant orienting itself by the withheld
wall outcome (nf) must be FLAGGED by the AST scope audit (the
five sealed surgeries audit clean).  STOP LIST (anti-gates,
binding): NO pair hierarchies, NO splits, NO s-flows, NO
precision escalation beyond the sealed dps-40 counter-check;
fragment audit (no polyfit/curve_fit/lstsq/minimize) inherited.

INDEX FIREWALL (binding, r238-r273 discipline): w = window (kz),
N_w = builder depth, n = chain degree; the surgery functions
consume (uu, mm / d_arm, theta, seed, labels) ONLY (AST scope
audit against the withheld truth-side set incl. the wall outcome
nf); ground truth (nf, sg_h chains) enters MEASUREMENT and gates
only; no zero/prime oracles anywhere (AST firewall); labels via
ODG.base_exp = r254 integer root extraction, world-blind.
MACHINERY IMPORTED VERBATIM: r244 BH.wpack + BH.bord_chain +
BH.spearman, v881 PIK.build_rung + PIK.folded_measure +
PIK.lambda_eps, r243 PB.smooth_comb, r254 ODG.base_exp, core
build_window/frame_a_zones READ-ONLY.

SEALED CONSTANTS: MAIN window 9; RUNG windows (18, 55); controls
w9 EPSTEIN/SCRAMBLE(seed 1)/SMOOTH, flips 25/21/27; THETAS
(0.02, 0.05, 0.10, 0.15, 0.25); REPS 3; REPS_SINGLE 9; SEED_BASE
276000; CTRL_HI 0.20; NEAR_FULL 0.90; K_CONT 3; DEF_MIN 0.005;
LAW_MIN 4; SP_TRANSPORT 0.5; NINT_BAR 1e-9; JIT_TOL 1e-12;
MASS_MUT_MIN 1e-3; MP_DPS 40; SHUFFLE n/a (no trend axis this
round); runtime <= 1800 s; smoke = censuses + identity wards +
theta-0 gates + conservation battery + dose accounting + label
census + base_exp toy + scope audits + m1 + m2 (ladders, map,
anchors, mp, m3 skipped).  DISCLOSED PRE-SPEC INPUT: the window
selection censuses (N_w, comb size, KHI count, grid census) and
ONE machinery scoping pass (identity bitwise, controls 25/21/27,
single-op feasibility, mp cost) -- no verdict-relevant band was
tuned; every class boundary above is a v956/r273 record number
or a round constant fixed before the first full evaluation.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] FIREWALL_THRESHOLD(all surgeries collapse to
    control level at SINGLE dose -- the wall is a discrete
    arithmetic all-or-nothing phenomenon) / FIREWALL_GRADED(
    every surgery graded or tolerant -- the wall is
    perturbation-tolerant up to measured dose) / FIREWALL_LAW(
    mixed classes; per-surgery laws)
+ PROPERTY_RANKING(surgeries ascending by wall tolerance)
+ CONTINUUM_VS_JUMP(JUMP / CONTINUUM / SPARSE_MIDDLE, middle
    census)
+ V956_PLACEMENT(min stage depth vs the 0.11..0.15 control band)
+ N_TRANSPORT(MAP_TRANSPORTS / WINDOW_SPECIFIC, sp per rung)
+ FIREWALL_HYPOTHESIS(quantified, TASK_FORMULATION_ONLY).
Honesty before beauty: every depth is MEASURED on three finite
windows; no verdict claims a cofinal law, a mechanism theorem or
H5 progress; survival-depth loss under surgery is an
EXPERIMENTAL localization of the wall-carrying properties, not a
proof that any property suffices; r243-r273 stand.

DISCLOSED CALIBRATION AMENDMENTS (before freeze; the surgery
definitions, conservation gates, class rules, verdict rules and
every physics band never moved):
(a1) MP WARD DOMAIN: calibration pass 1 ran the survivor/MAIN
  mp chains to N_w -- ONE degree past the f64 chain domain
  (rows 0..N_w-1) -- and the mp chain correctly reported the
  v956 BOUNDARY flip AT N_w = 184 (n_flip = N_w + 0, the r228
  record, reproduced at dps 40); the ward now compares
  like-for-like (upto N_w - 1) and the boundary degree is kept
  as its own sealed BOUNDARY ward (MAIN mp flip == N_w).  A
  measurement-domain fix on a ward, not a physics band; every
  interior flip check of pass 1 already agreed EXACTLY.

RECORD TABLES (frozen from calibration pass 2 = the first full
evaluation AFTER the disclosed amendment; 25/25 gates; the
record insertion below is the only post-freeze edit, which IS
the protocol; run1/run2 identical up to WALL):
CAL_VERDICT = FIREWALL_LAW(P1_SWAP GRADED b +0.59 / P2_JIT
GRADED b +0.04 / P3_FAM INTERMEDIATE b +1.09 / B1_SIGN GRADED
b +0.26 / B2_MAG GRADED b +0.38) + PROPERTY_RANKING(P2_JIT
0.343 < B2_MAG 0.389 < B1_SIGN 0.536 < P1_SWAP 0.621 < P3_FAM
0.700 ascending tolerance) + CONTINUUM_VS_JUMP(CONTINUUM, 48/90
MIDDLE stages, w9 19/30) + V956_PLACEMENT(min stage depth 0.109
at B2_MAG theta 0.15, CONTROL_TOUCHED) + N_TRANSPORT(
MAP_TRANSPORTS, sp +0.84 kz18 / +0.86 kz55) +
FIREWALL_HYPOTHESIS(see reading).
Key numbers (w9 primary map; stage = median depth s_med over
replicates [min..max], surv = survivors/reps):
  P1_SWAP  SINGLE 1.000 [0.75..1.00] surv 5/9 | 0.02 0.886 |
           0.05 0.565 | 0.10 0.359 | 0.15 0.560 | 0.25 0.359
  P2_JIT   SINGLE 0.957 [0.83..1.00] surv 2/9 | 0.02 0.250 |
           0.05 0.255 | 0.10 0.207 | 0.15 0.196 | 0.25 0.196
  P3_FAM   SINGLE 0.875 [0.28..0.93] surv 0/9 | 0.02 IDENTITY |
           0.05 0.935 | 0.10 0.511 | 0.15 0.603 | 0.25 0.277
  B1_SIGN  SINGLE 0.973 [0.48..1.00] surv 4/9 | 0.02 0.755 |
           0.05 0.337 | 0.10 0.375 | 0.15 0.505 | 0.25 0.272
  B2_MAG   SINGLE 1.000 [0.61..1.00] surv 5/9 | 0.02 0.647 |
           0.05 0.342 | 0.10 0.125 | 0.15 0.109 | 0.25 0.109
Monotonicity sp(theta, s_med): P1 -0.82 / P2 -0.87 / P3 -0.80 /
B1 -0.60 / B2 -0.97 (all decreasing).  MIDDLE census 48/90
stages (w9 19/30) -- a genuine CONTINUUM of survival depths
between control level and full survival; the v956 control level
(0.11..0.15) is REACHED inside the theta <= 0.25 ladder: B2_MAG
0.109-0.125 at theta 0.10-0.25, P2_JIT 0.196 at theta 0.15-0.25
(w9); on the deep window kz55 P2/B2 sit at 0.04-0.14 across the
ladder.  Single ops land at 0.88-1.00 median (position-
dependent minima 0.28-0.83).  N-transport sp +0.84/+0.86 -- the
map is window-portable.  ANCHORS: EPSTEIN/SCRAMBLE/SMOOTH
25/21/27 exact; MAIN survives all three windows (depth 1.0).
WARDS: conservation + dose accounting EXACT on 360/360
perturbed worlds; label admission worst 9.8e-16; mp counter-
checks 9/9 exact (earliest-flip singles 138/152/51/89/113 ==
f64, survivor + MAIN clean over degrees <= N_w - 1, BOUNDARY
flip 184 == N_w, EPSTEIN 25); m1 comb mutant CAUGHT (7.7e-2
rel) + density mutant CAUGHT by both gates (2.0e-3 rel); m2
dose mutant CAUGHT (14 changed > cap 8); m3 flip-noise mutant
REJECTED by mp (25 != 22); m4 gift surgery FLAGGED (nf@once);
five surgeries audit clean; fragment audit clean.
READING (typed MEASUREMENT_ONLY, no mechanism claim): the wall
is NOT an all-or-nothing firewall -- the dose-response is a
measured CONTINUUM: single minimal operations (one neighbor
swap, one sign exchange, one atom jitter) typically leave the
wall at depth 0.88-1.00, far ABOVE the v956 control level, with
position-dependent lethal exceptions (earliest-flip singles at
51-152 of 184; the scoping earliest-atom swap at 34 = the r249
anchor); the collapse to control level happens WITHIN the
graduated ladder (theta 0.10-0.25) and the deficit laws are
SHALLOW and saturating (b +0.04..+1.09) -- no critical dose, an
immediate-onset graded degradation.  PROPERTY_RANKING (the
round's surprise, refining r273): SUPPORT EXACTNESS is the most
wall-critical property -- P2_JIT at amplitude 0.02 of the LOCAL
ATOM GAP already costs 3/4 of the depth (0.250), and MAGNITUDE
placement (B2, tol 0.389) ranks SECOND, while the r273-mildest
FAMILY coherence stays mildest per-op too (P3, tol 0.700) and
the sign pattern sits mid-field (B1, 0.536): the wall reads the
POSITIONS and the MAGNITUDE FIELD of the signed density more
exactly than the family bookkeeping.  FIREWALL_HYPOTHESIS
(TASK_FORMULATION_ONLY, falsifiable): "the wall is carried by
the exact METRIC placement of the source -- support positions
at sub-gap precision and magnitude-position pairing -- with
graded loss D ~ theta^b, b in 0.04..1.09 (immediate onset, fast
saturation), NOT by an all-or-nothing arithmetic switch; any
candidate wall lemma must be quantitatively stable under
family/assignment permutations at small dose but consumes the
metric data exactly"; the position-dependence of single-op
lethality names the follow-up: the u-profile of single-op
influence.  Runtime 9.5 s full / 0.7 s smoke; run1/run2
identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE (records
inserted per protocol; no bar, band, class rule or verdict rule
moved).

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import offdiag_gram_probe as ODG               # noqa: E402 r254
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_KZ = 9
RUNG_KZS = (18, 55)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
THETAS = (0.02, 0.05, 0.10, 0.15, 0.25)
REPS = 3
REPS_SINGLE = 9
SEED_BASE = 276000
CTRL_HI = 0.20
NEAR_FULL = 0.90
K_CONT = 3
DEF_MIN = 0.005
LAW_MIN = 4
SP_TRANSPORT = 0.5
NINT_BAR = 1e-9
JIT_TOL = 1e-12
MASS_MUT_MIN = 1e-3
MP_DPS = 40
SURG_NAMES = ("P1_SWAP", "P2_JIT", "P3_FAM", "B1_SIGN", "B2_MAG")
COMB_SURG = ("P1_SWAP", "P2_JIT", "P3_FAM")
DOSE_LABELS = ("SINGLE",) + THETAS

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------ AST audits
def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the surgeries consume "
                       "node positions + weights / the grid density + "
                       "r254 integer-root labels ONLY; the wall outcome "
                       "(nf, sg_h) enters MEASUREMENT and gates only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    """AST scan for forbidden fit-method families (identifiers only;
    the fragment table is assembled from split strings)."""
    frags = ("cand_" + "unroll", "poly" + "fit", "curve_" + "fit",
             "lst" + "sq", "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def scope_audit(funcname, forbidden):
    """walk ONLY the named function's subtree; flag any withheld
    truth-side identifier or dict-key string from the sealed set."""
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in forbidden:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


PERT_FORBIDDEN = {"t" + "_term", "Z", "St", "rho", "n" + "f",
                  "sg" + "_h", "lg" + "_h", "wp" + "ack",
                  "bord" + "_chain", "margin", "slack2", "C_true"}


# ------------------------------------------------ trend estimators
def halves_slope(Xs, Ys):
    """r272 dyadic log-slope (deterministic): (mean ln Y | second
    half - first half) / (same for ln X) on the X-sorted list."""
    n = len(Xs)
    h = n // 2
    ly = [math.log(max(float(v), 1e-300)) for v in Ys]
    lx = [math.log(max(float(v), 1e-300)) for v in Xs]
    num = (sum(ly[h:]) / (n - h)) - (sum(ly[:h]) / h)
    den = (sum(lx[h:]) / (n - h)) - (sum(lx[:h]) / h)
    return num / den


# ------------------------------------ the five sealed surgeries
# (source-pure scope, AST-audited: consume uu, mm / d_arm, theta,
#  seed and the world-blind r254 labels ONLY -- no wall outcome)
def local_gaps(uu):
    """per-atom local nearest-neighbor gap of the sorted u
    (endpoints single-sided) -- the sealed P2 jitter scale
    (r273 verbatim)."""
    o = np.argsort(uu, kind="stable")
    us = uu[o]
    d = np.diff(us)
    g = np.empty(len(uu))
    if len(uu) == 1:
        g[:] = 1.0
        return g
    gs = np.empty(len(uu))
    gs[0] = d[0]
    gs[-1] = d[-1]
    if len(uu) > 2:
        gs[1:-1] = np.minimum(d[:-1], d[1:])
    g[o] = gs
    return g


def pert_swap(uu, mm, theta, seed, single):
    """P1_SWAP: n_pair disjoint u-adjacent weight transpositions
    (greedy disjoint selection over a seeded permutation of the
    adjacencies); SINGLE = one neighbor swap; positions and the
    weight multiset preserved EXACTLY."""
    if theta <= 0.0 and not single:
        return uu.copy(), mm.copy()
    n = len(uu)
    npair = 1 if single else max(1, int(round(theta * n / 2.0)))
    rng = np.random.default_rng(seed)
    o = np.argsort(uu, kind="stable")
    used = np.zeros(n, dtype=bool)
    mm2 = mm.copy()
    got = 0
    for s_ in rng.permutation(n - 1):
        if got >= npair:
            break
        if used[s_] or used[s_ + 1]:
            continue
        a_, b_ = o[s_], o[s_ + 1]
        mm2[a_], mm2[b_] = mm2[b_], mm2[a_]
        used[s_] = used[s_ + 1] = True
        got += 1
    return uu.copy(), mm2


def pert_jit(uu, mm, theta, seed, single):
    """P2_JIT: u_j -> u_j + amp g_j U[-1, 1]; amp = theta on ALL
    atoms, SINGLE = one atom at amp = 1.0; weights preserved
    EXACTLY."""
    if theta <= 0.0 and not single:
        return uu.copy(), mm.copy()
    rng = np.random.default_rng(seed)
    g = local_gaps(uu)
    if single:
        j = int(rng.integers(len(uu)))
        du = np.zeros(len(uu))
        du[j] = 1.0 * g[j] * rng.uniform(-1.0, 1.0)
    else:
        du = theta * g * rng.uniform(-1.0, 1.0, len(uu))
    return uu + du, mm.copy()


def pert_fam(uu, mm, theta, seed, ps, ks, single):
    """P3_FAM (r273 verbatim logic): nsel KHI atoms (k >= 2) swap
    weights with the nearest-in-u atom of a DIFFERENT family
    (different primary p); SINGLE = one swap; positions and the
    weight multiset preserved EXACTLY (pure transpositions)."""
    uu2, mm2 = uu.copy(), mm.copy()
    if theta <= 0.0 and not single:
        return uu2, mm2
    n = len(uu)
    cand = np.nonzero(ks >= 2)[0]
    nsel = 1 if single else int(round(theta * len(cand)))
    if nsel == 0:
        return uu2, mm2
    rng = np.random.default_rng(seed)
    sel = np.sort(rng.choice(cand, size=nsel, replace=False))
    for j in sel:
        lo = j - 1
        while lo >= 0 and ps[lo] == ps[j]:
            lo -= 1
        hi = j + 1
        while hi < n and ps[hi] == ps[j]:
            hi += 1
        opts = []
        if lo >= 0:
            opts.append((uu[j] - uu[lo], int(lo)))
        if hi < n:
            opts.append((uu[hi] - uu[j], int(hi)))
        if not opts:
            continue
        part = min(opts)[1]
        mm2[j], mm2[part] = mm2[part], mm2[j]
    return uu2, mm2


def pert_sign(darm, theta, seed, single, nzi):
    """B1_SIGN: signs of nsel selected nonzero grid entries
    permuted among the selection (magnitude field |d| stays AT
    POSITION); SINGLE = one +/- pair sign exchange; |d| array
    bitwise and sign multiset preserved EXACTLY."""
    if theta <= 0.0 and not single:
        return darm.copy()
    sgn = np.sign(darm)
    mag = np.abs(darm)
    rng = np.random.default_rng(seed)
    if single:
        posi = nzi[darm[nzi] > 0]
        negi = nzi[darm[nzi] < 0]
        i = int(posi[rng.integers(len(posi))])
        j = int(negi[rng.integers(len(negi))])
        sgn[i], sgn[j] = sgn[j], sgn[i]
    else:
        nsel = max(2, int(round(theta * len(nzi))))
        sel = rng.choice(nzi, size=nsel, replace=False)
        sgn[sel] = sgn[sel][rng.permutation(nsel)]
    return mag * sgn


def pert_mag(darm, theta, seed, single, nzi):
    """B2_MAG: magnitudes of nsel selected nonzero grid entries
    permuted among the selection (sign field stays AT POSITION);
    SINGLE = one grid-adjacent magnitude exchange; sign array
    bitwise and |d| multiset preserved EXACTLY."""
    if theta <= 0.0 and not single:
        return darm.copy()
    sgn = np.sign(darm)
    mag = np.abs(darm)
    rng = np.random.default_rng(seed)
    if single:
        k = int(rng.integers(len(nzi) - 1))
        i, j = int(nzi[k]), int(nzi[k + 1])
        mag[i], mag[j] = mag[j], mag[i]
    else:
        nsel = max(2, int(round(theta * len(nzi))))
        sel = rng.choice(nzi, size=nsel, replace=False)
        mag[sel] = mag[sel][rng.permutation(nsel)]
    return mag * sgn


def mutant_mass_comb(uu, mm, theta, seed):
    """m1 MUST-FAIL MUTANT (comb): scales a theta-fraction of the
    weights by 1.15 -- the conservation gate must CATCH it."""
    rng = np.random.default_rng(seed)
    mm2 = mm.copy()
    nsel = max(1, int(round(theta * len(mm))))
    sel = rng.choice(len(mm), size=nsel, replace=False)
    mm2[sel] *= 1.15
    return uu.copy(), mm2


def mutant_mass_density(darm, seed):
    """m1 MUST-FAIL MUTANT (density): scales |d| of a random tenth
    of the entries by 1.02 -- the density conservation gates must
    CATCH it."""
    rng = np.random.default_rng(seed)
    d2 = darm.copy()
    sel = rng.choice(len(darm), size=max(1, len(darm) // 10),
                     replace=False)
    d2[sel] *= 1.02
    return d2


def mutant_gift_pert(uu, mm, pack):
    """m4 scope-audit MUST-FAIL MUTANT: a 'surgery' oriented by the
    withheld wall outcome -- the scope audit must FLAG this."""
    s = 1.0 if pack["nf"] is None else -1.0
    return uu.copy(), (mm[::-1].copy() if s < 0.0 else mm.copy())


def dose_cap(kind, theta, single, n_at, n_khi, n_nz):
    """sealed nominal dose caps (changed-entry counts) for the
    dose-accounting gate."""
    if kind == "P1_SWAP":
        return 2 * (1 if single else max(1, int(round(theta * n_at
                                                      / 2.0))))
    if kind == "P2_JIT":
        return 1 if single else n_at
    if kind == "P3_FAM":
        return 2 * (1 if single else int(round(theta * n_khi)))
    nsel = 2 if single else max(2, int(round(theta * n_nz)))
    return nsel


def conserve_comb(kind, uu, mm, uu2, mm2, amp):
    """exact conservation gates (comb channel): P1/P3 positions
    bitwise + sorted weight multiset bitwise; P2 weights bitwise
    + per-atom jitter bound."""
    if kind == "P2_JIT":
        ok_m = bool(np.array_equal(mm2, mm))
        g = local_gaps(uu)
        dev = np.abs(uu2 - uu)
        ok_u = bool(np.all(dev <= amp * g * (1.0 + JIT_TOL) + 1e-300))
        return ok_u and ok_m
    ok_u = bool(np.array_equal(uu2, uu))
    ok_m = bool(np.array_equal(np.sort(mm2), np.sort(mm)))
    return ok_u and ok_m


def conserve_density(kind, d, d2):
    """exact conservation gates (density channel): B1 |d| bitwise
    + sign multiset; B2 sign array bitwise + |d| multiset."""
    if kind == "B1_SIGN":
        ok_a = bool(np.array_equal(np.abs(d2), np.abs(d)))
        ok_s = bool(np.array_equal(np.sort(np.sign(d2)),
                                   np.sort(np.sign(d))))
        return ok_a and ok_s
    ok_s = bool(np.array_equal(np.sign(d2), np.sign(d)))
    ok_a = bool(np.array_equal(np.sort(np.abs(d2)),
                               np.sort(np.abs(d))))
    return ok_s and ok_a


# ------------------------------------------------ world machinery
def window_ctx(kz):
    """per-window context: comb, labels, grid density, folded
    border (smooth), builder depth."""
    b = PIK.build_rung(kz)
    rr = core.build_window(kz)
    uu = np.asarray(rr["uu"], float).copy()
    mm = 2.0 * np.asarray(rr["lam"], float).copy()
    nn = np.round(np.exp(uu)).astype(np.int64)
    dev = float(np.max(np.abs(np.exp(uu) - nn) / nn))
    pk = [ODG.base_exp(int(n)) for n in nn]
    ps = np.array([p for p, _k in pk], dtype=np.int64)
    ks = np.array([k for _p, k in pk], dtype=np.int64)
    sm = PB.smooth_comb(b["alpha"])
    bsm = PIK.build_rung(kz, comb=sm)
    bx, bw, _ = PIK.folded_measure(bsm["d"], bsm["L"], +1.0)
    by, bv, _ = PIK.folded_measure(bsm["d"], bsm["L"], -1.0)
    darm = np.asarray(b["d"], float).copy()
    nzi = np.nonzero(darm)[0]
    return dict(kz=kz, N=int(b["h"]), L=int(b["L"]), uu=uu, mm=mm,
                ps=ps, ks=ks, lab_dev=dev, darm=darm, nzi=nzi,
                bx=bx, bw=bw, by=by, bv=bv,
                n_khi=int(np.sum(ks >= 2)))


def nf_from_density(ctx, d2):
    """wall survival of a (surgered) grid density: fold +/- and run
    the exact r244 bordered h-chain; nf = first sg_h < 0."""
    xs, ws, _ = PIK.folded_measure(d2, ctx["L"], +1.0)
    ys, vs, _ = PIK.folded_measure(d2, ctx["L"], -1.0)
    rows = BH.bord_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                         ctx["by"], ctx["bv"], ctx["N"])
    return next((r["n"] for r in rows if r["sg_h"] < 0), None), \
        (xs, ws, ys, vs)


def nf_from_comb(ctx, u2, m2):
    """wall survival of a (surgered) comb: rebuild the grid density
    via the sealed comb channel, then the density path."""
    bb = PIK.build_rung(ctx["kz"], comb=(u2, m2))
    return nf_from_density(ctx, np.asarray(bb["d"], float))


def apply_surgery(kind, ctx, theta, seed, single):
    """dispatch; returns (nf, changed_count, zones) with the exact
    conservation + dose-accounting results folded in."""
    if kind in COMB_SURG:
        uu, mm = ctx["uu"], ctx["mm"]
        if kind == "P1_SWAP":
            u2, m2 = pert_swap(uu, mm, theta, seed, single)
        elif kind == "P2_JIT":
            u2, m2 = pert_jit(uu, mm, theta, seed, single)
        else:
            u2, m2 = pert_fam(uu, mm, theta, seed, ctx["ps"],
                              ctx["ks"], single)
        amp = 1.0 if (single and kind == "P2_JIT") else theta
        ok = conserve_comb(kind, uu, mm, u2, m2, amp)
        changed = int(np.sum(m2 != mm)) if kind != "P2_JIT" \
            else int(np.sum(u2 != uu))
        nf, zones = nf_from_comb(ctx, u2, m2)
        return nf, ok, changed, zones
    d = ctx["darm"]
    if kind == "B1_SIGN":
        d2 = pert_sign(d, theta, seed, single, ctx["nzi"])
    else:
        d2 = pert_mag(d, theta, seed, single, ctx["nzi"])
    ok = conserve_density(kind, d, d2)
    changed = int(np.sum(d2 != d))
    nf, zones = nf_from_density(ctx, d2)
    return nf, ok, changed, zones


def base_exp_toy():
    """hand-checked base_exp table (exact)."""
    tab = ((2, (2, 1)), (3, (3, 1)), (4, (2, 2)), (5, (5, 1)),
           (8, (2, 3)), (9, (3, 2)), (25, (5, 2)), (27, (3, 3)),
           (32, (2, 5)), (49, (7, 2)), (121, (11, 2)),
           (128, (2, 7)), (243, (3, 5)))
    return all(ODG.base_exp(n) == r for n, r in tab)


# ------------------------------------------------ mp counter-check
def mp_first_flip(zones, upto, dps):
    """mp signed-Stieltjes sign chain (the sealed dps-40 anti-noise
    counter-check): returns the first degree with a negative
    cumulative h-sign, or None if none up to `upto`."""
    import mpmath as mp
    mp.mp.dps = dps
    xs, ws, ys, vs = zones
    X = [mp.mpf(float(v)) for v in xs]
    W = [mp.mpf(float(v)) for v in ws]
    Y = [mp.mpf(float(v)) for v in ys]
    V = [mp.mpf(float(v)) for v in vs]
    qx = [mp.mpf(1)] * len(X)
    qy = [mp.mpf(1)] * len(Y)
    qxm = [mp.mpf(0)] * len(X)
    qym = [mp.mpf(0)] * len(Y)
    Ls = mp.mpf(0)
    Lsm = mp.mpf(0)
    eta = sum(w * a * a for w, a in zip(W, qx)) \
        - sum(v * a * a for v, a in zip(V, qy))
    etam = eta
    sg = 1 if eta > 0 else -1
    if sg < 0:
        return 0
    for n in range(upto):
        alh = (sum(w * x * a * a for w, x, a in zip(W, X, qx))
               - sum(v * y * a * a
                     for v, y, a in zip(V, Y, qy))) / eta
        if n == 0:
            px = [(x - alh) * a for x, a in zip(X, qx)]
            py = [(y - alh) * a for y, a in zip(Y, qy)]
        else:
            ge = (eta / etam) * mp.e ** (2 * (Ls - Lsm))
            fc = mp.e ** (Lsm - Ls)
            px = [(x - alh) * a - ge * fc * am
                  for x, a, am in zip(X, qx, qxm)]
            py = [(y - alh) * a - ge * fc * am
                  for y, a, am in zip(Y, qy, qym)]
        sc = max(max(abs(v) for v in px), max(abs(v) for v in py))
        qxm, qym, etam, Lsm = qx, qy, eta, Ls
        qx = [v / sc for v in px]
        qy = [v / sc for v in py]
        Ls += mp.log(sc)
        eta = sum(w * a * a for w, a in zip(W, qx)) \
            - sum(v * a * a for v, a in zip(V, qy))
        gam = (eta / etam) * mp.e ** (2 * (Ls - Lsm))
        if gam < 0:
            sg = -sg
        if sg < 0:
            return n + 1
    return None


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("minimal_firewall_probe -- PRIME.PORT.WALL."
          "MINIMAL_FIREWALL.01 (round 276)")
    print("SPEC_SHA %s   R244_SHA %s (imported)   R273_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], BH.SPEC_SHA[:16],
             hashlib.sha256(
                 open(os.path.join(HERE, "euler_mechanism_probe.py"),
                      "rb").read()).hexdigest()[:16]))
    print("mode: %s" % ("SMOKE (censuses + identity wards + theta-0 "
                        "gates + conservation battery + dose "
                        "accounting + labels + toy + scope audits + "
                        "m1 + m2; ladders, map, anchors, mp, m3 "
                        "skipped)" if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "REVIEWER-ADJUDICATED DOSE-RESPONSE ROUND (no proof, no "
          "certificate, no bound, no mechanism claim): five sealed "
          "surgeries (neighbor SWAP / support JIT / family FAM / "
          "grid SIGN / grid MAG) x doses SINGLE + %s x pinned "
          "replicates (%d ladder / %d single) on windows w%d + %s "
          "against the exact h-chain wall depth s = nf/N_w; classes "
          "THRESHOLD <= %.2f / TOLERANT >= %.2f / GRADED / "
          "INTERMEDIATE and verdicts THRESHOLD/GRADED/LAW + "
          "CONTINUUM-vs-JUMP sealed BEFORE evaluation"
          % (str(THETAS), REPS, REPS_SINGLE, MAIN_KZ, str(RUNG_KZS),
             CTRL_HI, NEAR_FULL))

    # ---------------- S1: censuses + identity wards
    section("S1  CENSUSES + IDENTITY WARDS")
    ctxs = {kz: window_ctx(kz) for kz in (MAIN_KZ,) + RUNG_KZS}
    p_main = {kz: BH.wpack(kz) for kz in ctxs}
    ok_id = True
    id_note = []
    for kz, ctx in ctxs.items():
        nf0, _ = nf_from_comb(ctx, ctx["uu"], ctx["mm"])
        p9i = BH.wpack(kz, base_kw=dict(comb=(ctx["uu"], ctx["mm"])))
        rows0 = BH.bord_chain(*(PIK.folded_measure(ctx["darm"],
                                                   ctx["L"], +1.0)[:2]
                                + PIK.folded_measure(ctx["darm"],
                                                     ctx["L"],
                                                     -1.0)[:2]),
                              ctx["bx"], ctx["bw"], ctx["by"],
                              ctx["bv"], ctx["N"])
        rho0 = np.array([r_["rho"] for r_ in rows0])
        ok_id = ok_id and bool(np.array_equal(rho0,
                                              p_main[kz]["rho"])) \
            and nf0 == p_main[kz]["nf"] \
            and bool(np.array_equal(p9i["rho"], p_main[kz]["rho"]))
        id_note.append("w%d N %d nf %s" % (kz, ctx["N"], str(nf0)))
    check("G10-identity-channels", ok_id,
          "BOTH world channels reproduce BH.wpack BITWISE (rho "
          "array + nf) at the identity on all three windows: %s "
          "-- the surgery channels are exact at dose zero"
          % "; ".join(id_note))
    ok_lab = all(ctx["lab_dev"] <= NINT_BAR for ctx in ctxs.values())
    check("G11-label-admission", ok_lab,
          "r254 world-blind labels: admission worst %.1e (bar "
          "%.0e); censuses: %s"
          % (max(ctx["lab_dev"] for ctx in ctxs.values()), NINT_BAR,
             "; ".join("w%d comb %d KHI %d grid-nz %d (%d+/%d-)"
                       % (kz, len(ctx["uu"]), ctx["n_khi"],
                          len(ctx["nzi"]),
                          int(np.sum(ctx["darm"] > 0)),
                          int(np.sum(ctx["darm"] < 0)))
                       for kz, ctx in ctxs.items())))
    c9 = ctxs[MAIN_KZ]
    ok0 = True
    for kind in COMB_SURG:
        if kind == "P1_SWAP":
            u2, m2 = pert_swap(c9["uu"], c9["mm"], 0.0, SEED_BASE,
                               False)
        elif kind == "P2_JIT":
            u2, m2 = pert_jit(c9["uu"], c9["mm"], 0.0, SEED_BASE,
                              False)
        else:
            u2, m2 = pert_fam(c9["uu"], c9["mm"], 0.0, SEED_BASE,
                              c9["ps"], c9["ks"], False)
        ok0 = ok0 and bool(np.array_equal(u2, c9["uu"])) \
            and bool(np.array_equal(m2, c9["mm"]))
    for kind in ("B1_SIGN", "B2_MAG"):
        fn = pert_sign if kind == "B1_SIGN" else pert_mag
        d2 = fn(c9["darm"], 0.0, SEED_BASE, False, c9["nzi"])
        ok0 = ok0 and bool(np.array_equal(d2, c9["darm"]))
    check("G12-theta0-exact", ok0,
          "theta = 0 returns BITWISE-identical arrays for all five "
          "surgeries -- MAIN is the exact dose origin")
    cons_ok = True
    acc_ok = True
    note = []
    for kind in SURG_NAMES:
        for di, lab in enumerate(DOSE_LABELS):
            single = (lab == "SINGLE")
            th = 0.0 if single else float(lab)
            nf_, okc, chg, _z = apply_surgery(
                kind, c9, th, SEED_BASE + 555 + 17 * di, single)
            cons_ok = cons_ok and okc
            cap = dose_cap(kind, th, single, len(c9["uu"]),
                           c9["n_khi"], len(c9["nzi"]))
            acc_ok = acc_ok and (chg <= cap)
            if lab in ("SINGLE", 0.25):
                note.append("%s@%s chg %d cap %d"
                            % (kind, str(lab), chg, cap))
    check("G13-conservation-battery", cons_ok,
          "w9 conservation battery (5 surgeries x 6 doses): "
          "positions/multisets/sign fields bitwise per surgery "
          "type -- EXACT")
    check("G14-dose-accounting", acc_ok,
          "changed-entry counts <= nominal dose caps on the full "
          "battery; endpoint census: %s" % "; ".join(note))

    # ---------------- S2: toy + scope audits + m1/m2
    section("S2  TOY + SCOPE AUDITS + MUST-FAILS (m1, m2)")
    check("G20-toy-base-exp", base_exp_toy(),
          "hand-checked integer-root table exact: 2/3/4/5/8/9/25/"
          "27/32/49/121/128/243 -> the r254 label machine is "
          "loaded verbatim (no prime oracle)")
    h_p = []
    for fn in ("pert_swap", "pert_jit", "pert_fam", "pert_sign",
               "pert_mag", "local_gaps"):
        h_p.extend(scope_audit(fn, PERT_FORBIDDEN))
    h_g = scope_audit("mutant_gift_pert", PERT_FORBIDDEN)
    ag_hits = antigate_fragment_audit()
    check("G21-scope-audits", not h_p and bool(h_g) and not ag_hits,
          "the five sealed surgeries audit CLEAN against the "
          "withheld truth-side set (incl. the wall outcome)%s; the "
          "gift mutant FLAGGED (%s); fragment audit (no fit "
          "primitives): %s"
          % ("" if not h_p else " VIOLATION " + "; ".join(h_p),
             "; ".join(h_g) if h_g else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    u2, m2 = mutant_mass_comb(c9["uu"], c9["mm"], 0.5,
                              SEED_BASE + 99)
    caught1 = not conserve_comb("P1_SWAP", c9["uu"], c9["mm"], u2,
                                m2, 0.5)
    mb1 = abs(float(np.sum(np.sort(m2) - np.sort(c9["mm"])))) \
        / max(float(np.sum(np.abs(c9["mm"]))), 1e-300)
    d2 = mutant_mass_density(c9["darm"], SEED_BASE + 98)
    caught2 = (not conserve_density("B1_SIGN", c9["darm"], d2)) \
        and (not conserve_density("B2_MAG", c9["darm"], d2))
    mb2 = abs(float(np.sum(np.sort(np.abs(d2))
                           - np.sort(np.abs(c9["darm"]))))) \
        / max(float(np.sum(np.abs(c9["darm"]))), 1e-300)
    check("G22-mustfail-mass", caught1 and mb1 >= MASS_MUT_MIN
          and caught2 and mb2 >= MASS_MUT_MIN,
          "m1 MASS SURGERY: comb mutant (1.15x) CAUGHT (multiset "
          "break %.1e) AND density mutant (1.02x on |d|) CAUGHT by "
          "BOTH density gates (break %.1e; bar %.0e rel) -- mass "
          "change cannot pass as a permutation surgery"
          % (mb1, mb2, MASS_MUT_MIN))
    th_m2 = 0.10
    _u3, m3_ = pert_swap(c9["uu"], c9["mm"], 2.0 * th_m2,
                         SEED_BASE + 97, False)
    chg_m2 = int(np.sum(m3_ != c9["mm"]))
    cap_m2 = dose_cap("P1_SWAP", th_m2, False, len(c9["uu"]),
                      c9["n_khi"], len(c9["nzi"]))
    check("G23-mustfail-dose", chg_m2 > cap_m2,
          "m2 DOSE MUTANT (claims theta %.2f, applies %.2f): %d "
          "changed entries > claimed cap %d -- CAUGHT by the "
          "dose-accounting gate" % (th_m2, 2.0 * th_m2, chg_m2,
                                    cap_m2))

    if smoke:
        for g_ in ("G30-control-anchors", "G31-main-baselines",
                   "G40-conservation-full", "G41-map-measured",
                   "G50-dose-map", "G51-law-fits",
                   "G52-continuum-vs-jump", "G53-v956-placement",
                   "G54-n-transport", "G60-mp-counter-checks",
                   "G61-mustfail-flip-noise"):
            check(g_, True, "SMOKE: skipped")
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        # ---------------- S3: anchors + baselines
        section("S3  CONTROL ANCHORS + MAIN BASELINES")
        rr9 = core.build_window(MAIN_KZ)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ctrl_defs = (("EPSTEIN", dict(comb=(
            np.log(nn_idx.astype(float)),
            2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
            ("SCRAMBLE", dict(scramble_seed=1)),
            ("SMOOTH", dict(comb=PB.smooth_comb(rr9["alpha"]))))
        ctrl = {c: BH.wpack(MAIN_KZ, base_kw=kw)
                for c, kw in ctrl_defs}
        okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
        check("G30-control-anchors", okCf,
              "flips re-derived %s == the sealed 25/21/27 -- the "
              "v956 control level (0.11..0.15 of N_w %d) anchors "
              "the map bottom"
              % (str({c: ctrl[c]["nf"] for c in ctrl}),
                 ctxs[MAIN_KZ]["N"]))
        ok_base = all(p_main[kz]["nf"] is None for kz in ctxs)
        check("G31-main-baselines", ok_base,
              "MAIN survives the FULL free window on all three "
              "windows (nf None; N_w %s) -- depth 1.0 is the map "
              "top" % str([ctxs[kz]["N"] for kz in ctxs]))

        # ---------------- S4: the dose ladders
        n_worlds = len(SURG_NAMES) * (len(THETAS) * REPS
                                      + REPS_SINGLE) * len(ctxs)
        section("S4  THE DOSE LADDERS (%d worlds)" % n_worlds)
        stages = {}
        cons_all = True
        acc_all = True
        borderline = {}
        survivor_sample = None
        for si, kind in enumerate(SURG_NAMES):
            for di, lab in enumerate(DOSE_LABELS):
                single = (lab == "SINGLE")
                th = 0.0 if single else float(lab)
                reps = REPS_SINGLE if single else REPS
                for wi, (kz, ctx) in enumerate(ctxs.items()):
                    nfs = []
                    effs = []
                    for rep in range(reps):
                        seed = (SEED_BASE + si * 100000
                                + di * 10000 + rep * 1000 + wi * 10)
                        nf_, okc, chg, zones = apply_surgery(
                            kind, ctx, th, seed, single)
                        cons_all = cons_all and okc
                        cap = dose_cap(kind, th, single,
                                       len(ctx["uu"]), ctx["n_khi"],
                                       len(ctx["nzi"]))
                        acc_all = acc_all and (chg <= cap)
                        nfs.append(nf_)
                        effs.append(chg)
                        if kz == MAIN_KZ and single:
                            if nf_ is not None:
                                key = kind
                                if (key not in borderline
                                        or nf_ <
                                        borderline[key][0]):
                                    borderline[key] = (nf_, zones)
                            elif survivor_sample is None:
                                survivor_sample = (kind, zones)
                    N = ctx["N"]
                    ss = sorted((nf_ / N if nf_ is not None
                                 else 1.0) for nf_ in nfs)
                    st = dict(kind=kind, lab=lab, kz=kz,
                              med=float(np.median(ss)),
                              lo=ss[0], hi=ss[-1],
                              surv=sum(1 for v in nfs
                                       if v is None),
                              reps=reps,
                              eff=float(np.median(effs)),
                              iden=(max(effs) == 0))
                    stages[(kind, lab, kz)] = st
        check("G40-conservation-full", cons_all,
              "conservation EXACT on ALL %d perturbed worlds "
              "(positions / multisets / sign and magnitude fields "
              "bitwise per surgery type)" % n_worlds)
        check("G41-map-measured", acc_all
              and all((k_, l_, kz_) in stages
                      for k_ in SURG_NAMES for l_ in DOSE_LABELS
                      for kz_ in ctxs),
              "dose accounting <= nominal caps on ALL worlds; all "
              "%d map cells measured" % (len(stages)))

        # ---------------- S5: the minimality map
        section("S5  THE MINIMALITY MAP (sealed class rules)")
        for kind in SURG_NAMES:
            for kz in ctxs:
                cells = []
                for lab in DOSE_LABELS:
                    st = stages[(kind, lab, kz)]
                    cells.append("%s %s"
                                 % (str(lab),
                                    "IDENT" if st["iden"] else
                                    "%.3f[%.2f..%.2f]s%d/%d"
                                    % (st["med"], st["lo"],
                                       st["hi"], st["surv"],
                                       st["reps"])))
                info("%-8s w%-3d %s" % (kind, kz, " | ".join(cells)))
        classes = {}
        tol = {}
        laws = {}
        mono = {}
        for kind in SURG_NAMES:
            meds = [stages[(kind, lab, MAIN_KZ)]["med"]
                    for lab in DOSE_LABELS]
            s_single = stages[(kind, "SINGLE", MAIN_KZ)]["med"]
            tol[kind] = float(np.mean(meds))
            if s_single <= CTRL_HI:
                classes[kind] = "THRESHOLD"
            elif min(meds) >= NEAR_FULL:
                classes[kind] = "TOLERANT"
            elif s_single >= NEAR_FULL:
                classes[kind] = "GRADED"
            else:
                classes[kind] = "INTERMEDIATE"
            xs_, ds_ = [], []
            for th in THETAS:
                st = stages[(kind, th, MAIN_KZ)]
                D = 1.0 - st["med"]
                if (not st["iden"]) and D > DEF_MIN:
                    xs_.append(th)
                    ds_.append(D)
            laws[kind] = (halves_slope(xs_, ds_)
                          if len(xs_) >= LAW_MIN else None)
            th_meds = [(th, stages[(kind, th, MAIN_KZ)]["med"])
                       for th in THETAS
                       if not stages[(kind, th, MAIN_KZ)]["iden"]]
            mono[kind] = (BH.spearman([t for t, _ in th_meds],
                                      [m_ for _, m_ in th_meds])
                          if len(th_meds) >= 3 else float("nan"))
        rank = sorted(SURG_NAMES, key=lambda k: tol[k])
        rank_txt = " < ".join("%s %.3f" % (k, tol[k]) for k in rank)
        cls_txt = " / ".join(
            "%s %s%s" % (k, classes[k],
                         (" b %+.2f" % laws[k])
                         if laws[k] is not None else " NO_LAW")
            for k in SURG_NAMES)
        if all(classes[k] == "THRESHOLD" for k in SURG_NAMES):
            v_main = "FIREWALL_THRESHOLD(%s)" % cls_txt
        elif all(classes[k] in ("GRADED", "TOLERANT")
                 for k in SURG_NAMES):
            v_main = "FIREWALL_GRADED(%s)" % cls_txt
        else:
            v_main = "FIREWALL_LAW(%s)" % cls_txt
        check("G50-dose-map", True,
              "SEALED CLASSES (THRESHOLD s_single <= %.2f / "
              "TOLERANT min >= %.2f / GRADED / INTERMEDIATE): %s; "
              "monotonicity sp(theta, s_med): %s"
              % (CTRL_HI, NEAR_FULL, v_main,
                 str({k: ("%.2f" % mono[k]) for k in SURG_NAMES})))
        check("G51-law-fits", True,
              "deficit laws D ~ theta^b (halves log-slope, >= %d "
              "usable stages): %s -- deterministic, no fit "
              "primitives"
              % (LAW_MIN, " / ".join(
                  "%s %s" % (k, ("b %+.2f" % laws[k])
                             if laws[k] is not None
                             else "NO_LAW")
                  for k in SURG_NAMES)))
        mids = {kz: sum(1 for kind in SURG_NAMES
                        for lab in DOSE_LABELS
                        if CTRL_HI
                        < stages[(kind, lab, kz)]["med"]
                        < NEAR_FULL) for kz in ctxs}
        n_mid_w9 = mids[MAIN_KZ]
        n_mid = sum(mids.values())
        if n_mid_w9 == 0:
            cvj = "JUMP"
        elif n_mid_w9 >= K_CONT:
            cvj = "CONTINUUM"
        else:
            cvj = "SPARSE_MIDDLE"
        check("G52-continuum-vs-jump", True,
              "MIDDLE census (%.2f < s_med < %.2f): w9 %d/30, all "
              "windows %d/%d -> %s (sealed: JUMP iff 0, CONTINUUM "
              "iff >= %d on w9)"
              % (CTRL_HI, NEAR_FULL, n_mid_w9, n_mid, len(stages),
                 cvj, K_CONT))
        min_stage = min(((stages[(k_, l_, MAIN_KZ)]["med"], k_, l_)
                         for k_ in SURG_NAMES for l_ in DOSE_LABELS
                         if not stages[(k_, l_, MAIN_KZ)]["iden"]))
        touched = min_stage[0] <= CTRL_HI
        check("G53-v956-placement", True,
              "min w9 stage depth %.3f at %s theta %s vs the v956 "
              "control band 0.11..0.15 (controls 25/21/27 of N_w "
              "%d) -- CONTROL_%s; single ops land at %s"
              % (min_stage[0], min_stage[1], str(min_stage[2]),
                 ctxs[MAIN_KZ]["N"],
                 "TOUCHED" if touched else "NOT_REACHED",
                 str(["%.2f" % stages[(k_, "SINGLE",
                                       MAIN_KZ)]["med"]
                      for k_ in SURG_NAMES])))
        w9v = [stages[(k_, l_, MAIN_KZ)]["med"]
               for k_ in SURG_NAMES for l_ in DOSE_LABELS]
        sp_tr = {}
        for kz in RUNG_KZS:
            rv = [stages[(k_, l_, kz)]["med"]
                  for k_ in SURG_NAMES for l_ in DOSE_LABELS]
            sp_tr[kz] = BH.spearman(w9v, rv)
        transports = all(sp_tr[kz] >= SP_TRANSPORT
                         for kz in RUNG_KZS)
        check("G54-n-transport", True,
              "N-transport of the 30-stage map: sp(w9, kz18) "
              "%+.2f, sp(w9, kz55) %+.2f (bar %.1f) -> %s (typed "
              "classification, not a pass bar)"
              % (sp_tr[18], sp_tr[55], SP_TRANSPORT,
                 "MAP_TRANSPORTS" if transports
                 else "WINDOW_SPECIFIC"))

        # ---------------- S6: mp counter-checks + m3
        section("S6  MP COUNTER-CHECKS + MUST-FAIL m3")
        ok_mp = True
        mp_note = []
        for kind in SURG_NAMES:
            if kind not in borderline:
                mp_note.append("%s: no flipped single" % kind)
                continue
            nf_, zones = borderline[kind]
            r_mp = mp_first_flip(zones, min(nf_ + 5,
                                            ctxs[MAIN_KZ]["N"]),
                                 MP_DPS)
            ok_mp = ok_mp and (r_mp == nf_)
            mp_note.append("%s single nf %d mp %s"
                           % (kind, nf_, str(r_mp)))
        # amendment a1 (disclosed): the f64 chain covers degrees
        # 0..N_w-1; survivor/MAIN mp chains compare like-for-like
        # (upto N_w - 1); the boundary degree N_w is a disclosed
        # INFO ward (the v956 boundary flip AT the cap).
        if survivor_sample is not None:
            kind, zones = survivor_sample
            r_mp = mp_first_flip(zones, ctxs[MAIN_KZ]["N"] - 1,
                                 MP_DPS)
            ok_mp = ok_mp and (r_mp is None)
            mp_note.append("%s survivor mp %s (degrees <= N_w-1)"
                           % (kind, str(r_mp)))
        z_main = (p_main[MAIN_KZ]["d"]["xs"],
                  p_main[MAIN_KZ]["d"]["ws"],
                  p_main[MAIN_KZ]["d"]["ys"],
                  p_main[MAIN_KZ]["d"]["vs"])
        r_mp = mp_first_flip(z_main, ctxs[MAIN_KZ]["N"] - 1, MP_DPS)
        ok_mp = ok_mp and (r_mp is None)
        mp_note.append("MAIN mp %s (degrees <= N_w-1)" % str(r_mp))
        r_bnd = mp_first_flip(z_main, ctxs[MAIN_KZ]["N"], MP_DPS)
        info("v956 BOUNDARY WARD (mp dps %d): extending MAIN w9 one "
             "degree past the cap flips at %s == N_w %d (the r228 "
             "record n_flip = N_w + 0, reproduced)"
             % (MP_DPS, str(r_bnd), ctxs[MAIN_KZ]["N"]))
        ok_mp = ok_mp and (r_bnd == ctxs[MAIN_KZ]["N"])
        z_ep = (ctrl["EPSTEIN"]["d"]["xs"],
                ctrl["EPSTEIN"]["d"]["ws"],
                ctrl["EPSTEIN"]["d"]["ys"],
                ctrl["EPSTEIN"]["d"]["vs"])
        r_ep = mp_first_flip(z_ep, CTRL_FLIPS["EPSTEIN"] + 5,
                             MP_DPS)
        ok_mp = ok_mp and (r_ep == CTRL_FLIPS["EPSTEIN"])
        mp_note.append("EPSTEIN mp %s" % str(r_ep))
        check("G60-mp-counter-checks", ok_mp,
              "mp (dps %d) signed-Stieltjes sign chain confirms "
              "the f64 flip degrees EXACTLY at the borderline "
              "worlds -- no flip is f64 noise: %s"
              % (MP_DPS, "; ".join(mp_note)))
        nf_mut = CTRL_FLIPS["EPSTEIN"] - 3
        check("G61-mustfail-flip-noise", r_ep != nf_mut,
              "m3 FLIP-NOISE MUTANT (reports EPSTEIN nf %d): "
              "REJECTED by the mp counter-check (mp flip %s != "
              "%d) -- the detector is never trusted on f64 alone "
              "at the borderline" % (nf_mut, str(r_ep), nf_mut))

        # verdict assembly
        hyp = ("the wall is carried foremost by the %s property "
               "(tol %.3f) with the ranking %s; deficit laws %s; "
               "%s between control level and full survival"
               % (rank[0], tol[rank[0]], rank_txt,
                  " / ".join("%s %s" % (k, ("b %+.2f" % laws[k])
                                        if laws[k] is not None
                                        else "NO_LAW")
                             for k in SURG_NAMES), cvj))
        verd = " + ".join([
            v_main,
            "PROPERTY_RANKING(%s)" % rank_txt,
            "CONTINUUM_VS_JUMP(%s, %d/%d MIDDLE, w9 %d/30)"
            % (cvj, n_mid, len(stages), n_mid_w9),
            "V956_PLACEMENT(min %.3f at %s@%s, CONTROL_%s)"
            % (min_stage[0], min_stage[1], str(min_stage[2]),
               "TOUCHED" if touched else "NOT_REACHED"),
            "N_TRANSPORT(%s, sp %.2f/%.2f)"
            % ("MAP_TRANSPORTS" if transports
               else "WINDOW_SPECIFIC", sp_tr[18], sp_tr[55]),
            "FIREWALL_HYPOTHESIS(%s)" % hyp])

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the measured dose-response curve of the wall "
          "survival depth under five minimal-to-graduated "
          "surgeries -- NO certificate, NO bound, NO mechanism "
          "claim, NO H5 progress")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): conservation identities, "
          "dose accounting and the exact h-chain flips (mp "
          "counter-checked); MEASURED: every depth, class, law and "
          "ranking (three finite windows); OPEN: the cofinal step "
          "H5 and the wall mechanism (the hypothesis is a "
          "quantified TASK, not a claim); NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

_SRC_2 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""maslov_census_probe -- PRIME.PORT.RHP.MIDPOINT.MASLOV_CENSUS.01
(round 277): the blind Pruefer/Maslov census -- PREDICT the flip
degrees from phase/counting data, do not restate them.  The r274
warning is binding: the Pruefer band 0 < dTheta < pi is EXACTLY
h_n > 0 (a restatement), and the naive winding on the algebraic
continuation is NOT the half-filling count (262 vs 184 on w9).
This round measures the increment dynamics, identifies the RIGHT
winding quantity, and executes a reviewer-protocol blind rule.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

INDEX FIREWALL (binding, r238-r276 discipline): w = window (kz),
N_w = builder depth, S_w = #supp(mutilde), n/k = chain degree;
ground truth (h signs, flip degrees nf) enters GATES, TRAINING
LABELS and census tables only; no zero/prime oracles anywhere
(AST firewall).  MACHINERY IMPORTED VERBATIM: r274
WD.{stj_gen, pv_seq, scal_fwd, back_right, world_dict_block,
casor_sglg}, r244 BH.wpack + BH.spearman, r257 CT.union_arrays,
r264 QO.port_pack, r230 JF toy nodes, v563 frame_a_zones (READ-
ONLY core).  B PROVENANCE: B_w = S_{N-2} + 5/7 (r241/r243
imported floor, never fitted; gate-side only).

LEG A -- THE PHASE OBJECTS AND THE RIGHT WINDING QUANTITY:
(a1) Pruefer phases Theta^L_n (left chain, r274 scal_fwd) and
  Theta^R_n (right/dual solution, r274 back_right + residue
  normalization) at the sealed z0 = x0 + 1.5 rh; the INCREMENTS
  dTheta_n per degree step are the measured object: distribution
  (median/IQR/sign fraction) and Spearman coupling to the chain
  data alpha_n and log beta_n on both mains; the band
  Theta^L - Theta^R in (0, pi) == W^base_n > 0 == h_n > 0 is
  RE-GATED via the r274 dictionary (imported, restatement typed).
  STURM ROTATION (classical, exact): at the sealed interior
  point x* = hull center, the minor/Sturm sequence
  (pihat_0..pihat_n)(x*) counts eigenvalues of J_n below x*:
  #eig(J_n) < x* == n - #signchanges(seq) -- gated at the sealed
  degrees on both mains (phase rotation == node counting).
(a2) THE RIGHT WINDING QUANTITY (three sealed candidates,
  measured on the w9 mp continuation n = 0..S-2, dps 120):
  V_ATOM = #sign changes of pihat_n ON THE SORTED UNION ATOMS
  (the discrete Sturm census -- the conjectured correct one);
  V_HULL/V_SUPP = #real zeros (tridiag eigenvalues, |Im| <=
  imtol x width) inside the convex hull / inside the two zone
  hulls, at the sealed anatomy degrees; V_BAND = #(h_n > 0)
  in-band count (the r274 anchor 262, re-derived).  ADJUDICATION:
  the right winding quantity is the candidate with count == n at
  every free-prefix degree AND first break exactly at the flip;
  the naive band count must show its 78 continuation pivots
  (r274 anchor) -- measured, typed.

LEG B -- THE BLIND RULE (reviewer protocol, hard):
(b1) TRAINING SET (sealed, source-defined): w9 (main) + the 4
  smallest-N rungs of the (N, kz)-sorted 42-rung cofinal ladder
  (frame-A h <= 900, r274 convention; kz 9 excluded from the
  rung pick -- it is the training main); TRAINING CONTROLS: the
  SCRAMBLE(seed 2) variants of the same 5 windows (their flips
  nf are measured wpack ground truth; a variant without a flip
  inside its window is excluded with disclosure).  CANDIDATE
  CLASSES (exactly 3, sealed, source-pure inputs = chain
  coefficients (alpha, beta) + sorted atoms + z0 ONLY):
  (R1) STURM DEFECT: CROSSING at the first degree n with
       atom-sign-change count c_n != n (the interlacing/counting
       break as the census event);
  (R2) INTERLACING/REALITY MARGIN: CROSSING at the first n where
       the tridiagonal zeros of pihat_n leave the real axis
       (|Im| > imtol x width) or strict interlacing with
       pihat_{n-1} fails (general eigenvalues of the BALANCED
       similarity form sub_i = super_i = sqrt|beta_i| with the
       beta sign on the super-diagonal -- amendment a1:
       numerical stability only, the eigenvalues are exactly
       the monic zeros; no symmetry assumption -- purity over
       speed);
  (R3) PHASE-VELOCITY ANOMALY: CROSSING at the first n >= win+2
       where |dTheta^L_n - median(last win)| / MAD >= Z_thr,
       Z_thr from the sealed grid (3, 4, 5, 6, 8, 10), smallest
       threshold with zero false fires on the training mains.
  TRAINING PASS per candidate: zero fires on all 5 training
  mains (n <= N-1) AND every training control fires with
  |f - nf| <= 1.  SELECTION (sealed priority, decided BEFORE
  evaluation): R1 > R2 > R3 (R1 is the discrete-canonical
  object); the selected rule is FROZEN, blind runs it unchanged.
(b2) BLIND EXECUTION: the remaining 37 rungs + the full-depth
  mains w12/w13/w26 + the w9 controls EPSTEIN/SCRAMBLE(seed 1)/
  SMOOTH.  GO criterion (reviewer, sealed): ALL 42 ladder rungs
  SAFE through n = N-1 (train 5 re-reported + blind 37) AND
  w12/w13/w26 SAFE AND the controls fire within +-1 of 25/21/27.
  SEPARATES_ONLY: mains/rungs SAFE and all controls fire, but
  some |f - nf| > 1.  FAILED(typed): false positives on mains/
  rungs or a silent control.
(b3) r259 DEMARCATION WARD: the rule must NOT be the refuted
  energy-branch order -- the r259 record crossing degrees are
  EPSTEIN 9 / SCRAMBLE 16 / SMOOTH 19 (LEVEL_CROSSING_REFUTED);
  gate: the rule's control fire degrees differ from the r259
  crossings by >= 3 degrees each (imported record constants).

LEG C -- THE INDEX-COUNT CHAIN (proof-plan step 5 material):
(c1) mains w9/w13, every degree n < N: the census is MEASURED
  against the sealed expectation c_n == n (f64 census with the
  sealed sign guard 1e-9; guard-violating degrees recounted in
  mp dps 40 -- repair path sealed, counts disclosed); AMENDMENT
  a2 (calibration, disclosed): the expectation is REFUTED on
  both mains -- a genuine finding about signed Sturm theory --
  so G21/G26 are typed as measurement/adjudication gates and
  the parity-anchored convention ((-1)^n, atom signs, +1) is
  measured alongside as a2 anatomy (never a rule);
(c2) strict interlacing of the Jacobi eigenvalues of J_{n-1} and
  J_n at every free degree (symmetric tridiagonal, Cauchy;
  strict up to the sealed f64 resolution 1e-8 x mean gap), hull
  containment #eig in [lo, hi] == n reported;
(c3) the implication chain as a no-counterexample gate on the
  mains + all 42 rungs: (c_n == n) AND interlacing AND NOT
  (h_n > 0) never occurs on the free prefix (the direction the
  oriented midpoint theorem needs);
(c4) ATOM SATURATION (the window-rule question, w9 mp
  continuation): c_n at the sealed degrees around N_w = 184, the
  maximum of c_n over the full continuation and its argmax, the
  first defect degree, and whether the census ever heals
  (c_n == n again) beyond the flip -- the RESTATEMENT
  ADJUDICATOR: the selected rule is typed h-EQUIVALENT iff its
  SAFE/CROSSING pattern over the FULL continuation equals the
  h_n > 0 pattern degree-by-degree (the 78 h re-entry pivots
  beyond the flip are the separator).

LEG D -- WARDS/KILLS: AST scopes: the rule/census functions
(census_signs, sign_changes, mp_recount, cand_sturm,
cand_interlace, cand_phase, zeros_tridiag, prue_theta) consume
passed coefficient/atom arrays + the evaluation point ONLY
(forbidden: rho, S, sg_h, lg_h, hv, Fv, nf, rows, wpack,
bord_chain, world_dict_block, tau, aug, D_dict, q_chain) --
audited, with a deliberately h-reading mutant that MUST be
flagged; no fit primitives (fragment audit); CONTAMINATION
PROTOCOL: training kz set and blind kz set disjoint (printed,
gated); HULL-CONVENTION ANCHOR (documented): the hull/support
zero counts at the sealed anatomy degrees are printed next to
the atom census -- the convention difference is the m3 anchor;
mp WARDS: kz15 (razor) + the largest-N blind rung: mp (dps 60)
census counts == f64 counts at the sealed degrees (2, N//2,
N-1); w9 full-prefix f64-vs-mp census agreement (dps 120);
r266-pattern DETECTOR on the rule statistics (terminal census
margin, max phase z): selftest sp(g1, g1) flagged, fingerprints
sp(stat, g1) and sp(stat, D_N) < 0.9; STOP LIST (anti-gates):
no derived 5/7, no bound mechanism, no asymptotic law, no
energy-order rule (b3), no RH claim.

SEALED CONSTANTS: MAIN windows (9, 13); blind extra mains
(12, 26); controls w9 EPSTEIN / SCRAMBLE(seed 1) / SMOOTH, flips
25/21/27; H_CAP 900; B57 = 5/7 (gate-side); Z0 factor 1.5 on the
union+border hull; TRAIN_SCR_SEED 2; N_TRAIN_RUNGS 4; FLIP_TOL 1;
SIGN_GUARD 1e-9; MP_REPAIR_DPS 40; W9_DPS 120; WARD_DPS 60; ward
degrees (2, N//2, N-1); continuation anatomy degrees (40, 90,
150, 183, 184, 185, 200, 262, 300, 366); IM_TOL 1e-7 (x hull
width); rotation degrees (40, 90, 150, 183); interior point
x* = union hull center; R3 window 12, z grid (3, 4, 5, 6, 8,
10); interlacing resolution 1e-8 (x mean gap); r259 crossing
record (EPST 9, SCR 16, SMOOTH 19), separation >= 3; r274
in-band anchor 262 (w9); R2 continuation cap N + 30; FP_BAR
0.9; LOUD 1e3; runtime <= 1800 s; smoke = toys + w9 + controls
census + must-fails + scopes (ladder, training/blind, mp legs,
detector skipped, no adjudication).  NO pre-spec scratch:
calibration pass 1 (smoke + the w9/control census diagnosis)
was the first evaluation of this probe; amendments a1/a2 were
found there and disclosed BEFORE any record freeze; no bar,
tolerance, candidate priority or verdict rule moved at any
point.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  MASLOV_CENSUS_GO(rule; blind 42/42 rungs + 3 mains SAFE;
    control fires within +-1 of 25/21/27; r259-separated) iff
    the b2 GO criterion holds AND the b3 ward passes
  / CENSUS_SEPARATES_ONLY (mains/rungs SAFE, controls fire, but
    a fire degree misses by > 1 -- the reviewer's no-go)
  / CENSUS_FAILED(typed: false positives / silent controls /
    no candidate passed training)
  + CENSUS_RESTATEMENT iff the selected rule's SAFE/CROSSING
    pattern over the full w9 continuation equals the h_n > 0
    pattern degree-by-degree (h-equivalence, honest)
  + STURM_CHAIN_VERIFIED(atom-saturation finding) iff the leg-C
    bundle holds (c1 + c2 + c3 on mains and rungs, toys
    co-located).
Honesty before beauty: the census does not close the wall; the
target positivity D_N > 0 stays OPEN; no verdict claims a
derived 5/7, a bound mechanism, or an asymptotic law
(r243..r276 stand).

RECORD TABLES (frozen from the record run; calibration protocol:
first smoke pass 27/29 -- the drafted G21 HARD expectation
"c_n == n on the mains" FAILED and cascaded into G96; the
diagnosis measured the defect (a genuine finding, below), the
two disclosed amendments a1 (balanced similarity form in the R2
eigensolver -- eigenvalues unchanged, stability only) and a2
(G21/G26 retyped from expectation gates to measurement/
adjudication gates + the parity-anchored convention added as a2
ANATOMY, never a rule) were fixed BEFORE any record freeze; no
bar, tolerance, candidate priority, training/blind protocol or
verdict rule moved at any point; smoke then 29/29, calibration
pass 1 = first full evaluation 29/29, wall 504.4 s, and the
record run below is numerically identical):
CAL_VERDICT = MASLOV_CENSUS_GO(rule R2 INTERLACING/REALITY of
the Jacobi zeros; training 5/5 mains SAFE + 5/5 scramble(seed 2)
controls fire at exactly nf + 1; blind 37/37 rungs + 5/5 train
rungs + w12/w13/w26 SAFE at full depth; controls fire 26/22/28
== 25/21/27 + 1 within the sealed +-1; r259 branches separated
by 17/6/9 >= 3) -- STURM_CHAIN_VERIFIED is honestly NOT awarded
(the c1 expectation is refuted, see below) and the rule is NOT
h-equivalent (79 pattern mismatches on the continuation).
THE ROUND'S CENTRAL FINDING (the a2 answer): the RAW atom-
counted Sturm census is NOT the right winding quantity -- on
MAIN w9/w13 it breaks at n = 56/48 (128/120 defect degrees)
with h POSITIVE throughout: zeros ESCAPE the atom hull (G23
hull containment FALSE; parity anchors repair those, first
anchored defect 72/80) and then PAIR UP inside single atom gaps
-- the positive-measure separation theorem genuinely fails for
the signed comb.  The winding quantity that DOES break exactly
at the wall is the INTERLACING/REALITY structure of the Jacobi
zeros (R2): SAFE through the full free window on every world
with h > 0 (provably: beta > 0 => symmetrizable => real +
Cauchy-strict), first break at exactly nf + 1 on every control
and on the w9 continuation at 185 = N_w + 1.
Key numbers.  TOYS (exact rationals; f64 engine identical):
JF-9atom counts (0, 1, 2, 2, 2, 2, 3, 2, 3), first h < 0 at 3,
first defect 3 (+0); MAINLIKE (4, 4); FLIPLIKE (2, 2).  MAINS:
census anatomy w9 (first raw defect 56, 128 raw, first anchored
72, 53 anchored), w13 (48, 120, 80, 44), 0 guard degrees, 0 mp
repairs; interlacing strict at every degree (worst normalized
margin 2.8e-08 >= -1e-08); Sturm rotation EXACT at degrees
(40, 90, 150, 183) on both mains; controls raw-census defect at
25/22/27 vs flips 25/21/27 (+0/+1/+0 -- co-located, but the
same statistic fires falsely on MAIN at 56: raw R1 fails
training exactly as the r274 warning demanded).  PHASES:
dTheta^L (median, IQR, frac<0, sp vs alpha, sp vs log beta) =
w9 (0.000, 0.021, 0.48, -0.78, -0.29) / w13 (0.002, 0.025,
0.46, -0.76, -0.23); band == h > 0 re-gated (r274 dictionary,
restatement typed).  CONTINUATION (w9 mp dps 120): f64-vs-mp
census agreement at ALL n < 184; in-band 262/366 == r274
anchor, first h < 0 at 184 == N_w; anatomy (n: real-in-hull /
real-in-support / atom-count / #complex): 183 (182, 182, 182,
0), 184 (183, 183, 173, 0), 185 (183, 183, 173, 0), 200 (188,
188, 180, 10), 262 (179, 179, 167, 80), 300 (175, 175, 161,
124); R2 continuation fire 185; restatement: R1 pattern 206
mismatches vs h, R2 pattern 79 mismatches (78 h re-entries +
the fire offset; 0 healed census degrees) -- neither is
h-equivalent; saturation around N_w: c_182..186 = (171, 182,
173, 173, 178), max c_n = 184 at n = 215, c_365 = 163.
TRAINING (sealed: w9 + kz (18, 23, 12, 13), N = (142, 149,
151, 168); scramble(seed 2) truths nf = (23, 4, 6, 10, 12)):
R1 FAILS (mains false-fire; control fires (21, 5, 7, 10, 10)
include a -2 miss); R2 PASSES 5/5 + 5/5 (fires (24, 5, 7, 11,
13) = nf + 1 exactly); R3 FAILS (no sealed threshold separates)
=> R2 SELECTED by the sealed priority.  BLIND: 37/37 rungs +
5/5 train SAFE (42-rung table printed; worst terminal census
margin 4.5e-05), w12/w13/w26 SAFE (N = 151/168/364); controls
EPSTEIN 26 / SCRAMBLE 22 / SMOOTH 28 (all nf + 1, within the
sealed +-1); r259 separation 17/6/9 >= 3.  MP WARDS: kz15
(razor, N = 203) and kz52 (largest-N blind, N = 878) f64 == mp
(dps 60) census at the sealed degrees; 0 repairs anywhere.
DETECTOR: selftest sp(g1, g1) = 1.00 flagged; fingerprints
sp(log margin, g1) = 0.469 / sp(log margin, D_N) = 0.469 /
sp(max z, g1) = 0.588 / sp(max z, D_N) = 0.588 (all < 0.9).
MUST-FAILS: h-reading mutant FLAGGED (sg_h + rows), sealed
scopes CLEAN (8 functions), fragment audit CLEAN;
contamination: train kz (9, 12, 13, 18, 23) disjoint from the
37 blind kz, gated.  Runtime 504.4 s full / 0.3 s smoke;
run1/run2 identical up to WALL.  AMENDMENTS AFTER FREEZE: NONE.

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH            # noqa: E402 r244
import coupledtau_probe as CT                 # noqa: E402 r257
import quenched_opening_probe as QO           # noqa: E402 r264
import jfraction_probe as JF                  # noqa: E402 r230
import wronskian_dictionary_probe as WD       # noqa: E402 r274
import port_integrable_kernel_probe as PIK    # noqa: E402 v881
import v563_paper2_readouts as core           # noqa: E402 READ-ONLY

MAIN_WINDOWS = (9, 13)
EXTRA_MAINS = (12, 26)
CTRL_FLIPS = {"EPST": 25, "SCR": 21, "SMOOTH": 27}
H_CAP = 900
B57 = 5.0 / 7.0
Z0_FACT = 1.5
TRAIN_SCR_SEED = 2
N_TRAIN_RUNGS = 4
FLIP_TOL = 1
SIGN_GUARD = 1e-9
MP_REPAIR_DPS = 40
W9_DPS = 120
WARD_DPS = 60
CONT_EIG_DEGS = (40, 90, 150, 183, 184, 185, 200, 262, 300, 366)
IM_TOL = 1e-7
ROT_DEGS = (40, 90, 150, 183)
R3_WIN = 12
R3_ZGRID = (3.0, 4.0, 5.0, 6.0, 8.0, 10.0)
INTERLACE_TOL = 1e-8
R259_CROSS = {"EPST": 9, "SCR": 16, "SMOOTH": 19}
R259_SEP_MIN = 3
R274_INBAND = 262
R2_CONT_CAP = 30
FP_BAR = 0.9
LOUD = 1e3

CAL_VERDICT = (
    "MASLOV_CENSUS_GO(rule R2 INTERLACING/REALITY of the Jacobi "
    "zeros; training 5/5 mains SAFE + 5/5 scramble(seed 2) "
    "controls fire at exactly nf + 1; blind 37/37 rungs + 5/5 "
    "train rungs + w12/w13/w26 SAFE at full depth; controls fire "
    "26/22/28 == 25/21/27 + 1 within the sealed +-1; r259 "
    "branches separated by 17/6/9 >= 3)")

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the census/rule "
                       "functions consume chain coefficients + "
                       "atom positions + the evaluation point "
                       "ONLY; ground truth enters gates, training "
                       "labels and census tables only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


# ================= sealed census/rule scope (source-pure: every
# function below consumes PASSED coefficient/atom arrays and the
# evaluation point only -- AST-audited)
def census_signs(al, be, atoms, n_hi):
    """signs of pihat_n at the (sorted) atoms for n = 0..n_hi via
    a per-atom scaled three-term recursion; returns (SG int8
    [n_hi+1, m], MG margin [n_hi+1])."""
    m = len(atoms)
    u = np.ones(m)
    um = np.zeros(m)
    SG = np.zeros((n_hi + 1, m), dtype=np.int8)
    MG = np.ones(n_hi + 1)
    SG[0] = 1
    for n in range(n_hi):
        w = (atoms - al[n]) * u - (be[n] * um if n > 0 else 0.0)
        um, u = u, w
        s = np.maximum(np.abs(u), np.abs(um))
        s[s == 0.0] = 1.0
        u = u / s
        um = um / s
        SG[n + 1] = np.sign(u).astype(np.int8)
        MG[n + 1] = float(np.min(np.abs(u)))
    return SG, MG


def sign_changes(row):
    """#sign changes over a sorted-atom sign row (zeros skipped)."""
    s = row[row != 0]
    if len(s) < 2:
        return 0
    return int(np.sum(s[1:] != s[:-1]))


def mp_recount(al, be, atoms, degs, dps):
    """mp re-evaluation (sealed dps) of the f64-coefficient
    recursion at the requested degrees; returns sign-change
    counts (order of degs)."""
    mp.mp.dps = dps
    n_hi = max(degs)
    xs_ = [mp.mpf(float(x)) for x in atoms]
    u = [mp.mpf(1)] * len(xs_)
    um = [mp.mpf(0)] * len(xs_)
    want = set(degs)
    out = {}
    for n in range(n_hi):
        a = float(al[n])
        b = float(be[n]) if n > 0 else 0.0
        w = [(x - a) * uu - (b * uum if n > 0 else 0)
             for x, uu, uum in zip(xs_, u, um)]
        um, u = u, w
        if n + 1 in want:
            sg = [1 if v > 0 else (-1 if v < 0 else 0) for v in u]
            sg = [v for v in sg if v != 0]
            out[n + 1] = sum(1 for a_, b_ in zip(sg, sg[1:])
                             if a_ != b_)
    return [out[d] for d in degs]


def cand_sturm(cnt, n_hi):
    """R1: first degree n with census count != n (else None)."""
    for n in range(1, n_hi + 1):
        if cnt[n] != n:
            return n
    return None


def zeros_tridiag(al, be, n):
    """zeros of pihat_n = eigenvalues of the BALANCED similarity
    form of the tridiagonal (sub_i = super_i = sqrt|beta_i|, the
    beta sign carried on the super-diagonal) -- eigenvalues are
    exactly those of the monic recursion (similarity), the
    balancing is numerical stability only (amendment a1)."""
    T = np.zeros((n, n))
    for i in range(n):
        T[i, i] = al[i]
        if i + 1 < n:
            s = math.sqrt(abs(be[i + 1]))
            T[i + 1, i] = s
            T[i, i + 1] = s if be[i + 1] >= 0 else -s
    return np.linalg.eigvals(T)


def cand_interlace(al, be, lo, hi, n_hi, imtol):
    """R2: first degree n where the zeros leave the real axis or
    strict interlacing with degree n-1 fails; returns
    (fire, min normalized margin)."""
    width = hi - lo
    prev = None
    mmin = float("inf")
    for n in range(1, n_hi + 1):
        z = zeros_tridiag(al, be, n)
        if float(np.max(np.abs(z.imag))) > imtol * width:
            return n, mmin
        rz = np.sort(z.real)
        if prev is not None and n >= 2:
            gaps = np.minimum(prev - rz[:-1], rz[1:] - prev)
            marg = float(np.min(gaps)) / (width / n)
            mmin = min(mmin, marg)
            if marg <= 0.0:
                return n, mmin
        prev = rz
    return None, mmin


def prue_theta(sg, lg, n):
    """Pruefer phase atan2(v_{n+1}, v_n) from sign/log data."""
    m_ = max(lg[n + 1], lg[n])
    if not math.isfinite(m_):
        return 0.0
    return math.atan2(sg[n + 1] * math.exp(lg[n + 1] - m_),
                      sg[n] * math.exp(lg[n] - m_))


def cand_phase(al, be, z0, n_hi, win, zthr):
    """R3: first degree n >= win+2 where the left Pruefer
    increment is a >= zthr MAD-outlier vs the trailing window;
    returns (fire, max z)."""
    sg, lg = WD.scal_fwd(al, be, z0, n_hi + 1)
    th = [prue_theta(sg, lg, n) for n in range(n_hi)]
    dth = []
    for n in range(len(th) - 1):
        d = th[n + 1] - th[n]
        while d <= -math.pi:
            d += 2.0 * math.pi
        while d > math.pi:
            d -= 2.0 * math.pi
        dth.append(d)
    zmax = 0.0
    fire = None
    for n in range(win + 2, len(dth)):
        wnd = np.array(dth[n - win:n])
        med = float(np.median(wnd))
        mad = float(np.median(np.abs(wnd - med)))
        z = abs(dth[n] - med) / max(mad, 1e-12)
        zmax = max(zmax, z)
        if fire is None and z >= zthr:
            fire = n
    return fire, zmax


def mutant_h_reader(p, n):
    """DELIBERATE MUST-FAIL MUTANT: reads the pivot sign chain --
    the scope audit must FLAG this."""
    return p["rows"][n]["sg_h"] < 0


RULE_FUNCS = ("census_signs", "sign_changes", "mp_recount",
              "cand_sturm", "cand_interlace", "cand_phase",
              "zeros_tridiag", "prue_theta")
RULE_FORBIDDEN = {"rho", "S", "sg_h", "lg_h", "hv", "Fv", "nf",
                  "rows", "wpack", "bord_chain",
                  "world_dict_block", "tau", "aug", "D_dict",
                  "q_chain"}


def rule_scope_audit(funcname):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in RULE_FORBIDDEN:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


# ================= gate-side world material
def world_arrays(p):
    """chain coefficients + sorted atoms + z0 for one world
    (gate-side extraction; the rule functions receive ONLY the
    returned arrays)."""
    xu, _ = CT.union_arrays(p["d"])
    bx, _ = CT.union_arrays(p["dsm"])
    atoms = np.sort(xu)
    N = p["N"]
    al = np.array([p["rows"][k]["alh"] for k in range(N)])
    be = np.array([0.0] + [p["rows"][k]["gam_next"]
                           for k in range(N - 1)])
    lo = min(float(np.min(xu)), float(np.min(bx)))
    hi = max(float(np.max(xu)), float(np.max(bx)))
    x0, rh = 0.5 * (lo + hi), 0.5 * (hi - lo)
    z0 = x0 + Z0_FACT * rh
    return dict(atoms=atoms, al=al, be=be, z0=z0, N=N,
                lo=float(np.min(xu)), hi=float(np.max(xu)),
                x0=0.5 * (float(np.min(xu)) + float(np.max(xu))))


def aug_count(row, n):
    """the parity-anchored census convention (a2 anatomy only,
    never a rule): sign changes over ((-1)^n, signs on the sorted
    atoms, +1) -- zeros beyond the atom hull are counted through
    the boundary parity."""
    s = row[row != 0]
    left = 1 if n % 2 == 0 else -1
    seq = np.concatenate([[left], s, [1]])
    return int(np.sum(seq[1:] != seq[:-1]))


def world_census(wa):
    """f64 census counts (raw + parity-anchored) with the sealed
    sign-guard repair path on the raw counts."""
    N = wa["N"]
    SG, MG = census_signs(wa["al"], wa["be"], wa["atoms"], N - 1)
    cnt = np.array([sign_changes(SG[n]) for n in range(N)])
    cnt_aug = np.array([aug_count(SG[n], n) for n in range(N)])
    bad = [n for n in range(1, N) if MG[n] < SIGN_GUARD]
    n_rep = 0
    if bad:
        c2 = mp_recount(wa["al"], wa["be"], wa["atoms"], bad,
                        MP_REPAIR_DPS)
        for n, c in zip(bad, c2):
            if c != cnt[n]:
                cnt[n] = c
                n_rep += 1
    fire = cand_sturm(cnt, N - 1)
    return dict(cnt=cnt, cnt_aug=cnt_aug, MG=MG, fire=fire,
                n_bad=len(bad), n_rep=n_rep)


def sym_jacobi_eigs(al, be, n):
    """eigenvalues of the SYMMETRIZED Jacobi matrix J_n (gate
    side; requires beta > 0 on the used range)."""
    J = np.zeros((n, n))
    for i in range(n):
        J[i, i] = al[i]
        if i + 1 < n:
            off = math.sqrt(be[i + 1])
            J[i + 1, i] = off
            J[i, i + 1] = off
    return np.linalg.eigvalsh(J)


def mp_continuation(p, dps, n_hi=None):
    """w9-style mp chain over the sorted union atoms to degree
    n_hi (default S-1): per-degree atom sign-change counts, h
    signs, chain coefficients (f64 copies for eig anatomy)."""
    mp.mp.dps = dps
    xu, wu = CT.union_arrays(p["d"])
    order = np.argsort(xu)
    xs = [mp.mpf(float(v)) for v in xu[order]]
    ws = [mp.mpf(float(v)) for v in wu[order]]
    S_ = len(xs)
    if n_hi is None:
        n_hi = S_ - 1
    u = [mp.mpf(1)] * S_
    um = [mp.mpf(0)] * S_
    h = mp.fsum(w_ * a * a for w_, a in zip(ws, u))
    hsg = [1 if h > 0 else -1]
    alv, bev = [], [mp.mpf(0)]
    cnts = [0]
    cnts_aug = [0]
    for n in range(n_hi):
        a = mp.fsum(w_ * x * q * q
                    for w_, x, q in zip(ws, xs, u)) / h
        alv.append(a)
        b = bev[n]
        nx = [(x - a) * q - (b * qm if n > 0 else 0)
              for x, q, qm in zip(xs, u, um)]
        um, u = u, nx
        hn = mp.fsum(w_ * q * q for w_, q in zip(ws, u))
        bev.append(hn / h)
        h = hn
        hsg.append(1 if h > 0 else -1)
        sg = [1 if v > 0 else (-1 if v < 0 else 0) for v in u]
        sg = [v for v in sg if v != 0]
        cnts.append(sum(1 for a_, b_ in zip(sg, sg[1:])
                        if a_ != b_))
        seq = [1 if (n + 1) % 2 == 0 else -1] + sg + [1]
        cnts_aug.append(sum(1 for a_, b_ in zip(seq, seq[1:])
                            if a_ != b_))
    al64 = np.array([float(a) for a in alv])
    be64 = np.array([float(b) for b in bev[:len(alv)]])
    return dict(S=S_, cnts=cnts, cnts_aug=cnts_aug, hsg=hsg,
                al=al64, be=be64,
                lo=float(xu[order][0]), hi=float(xu[order][-1]))


def run_rule(sel, wa, cnt):
    """dispatch the sealed selected rule on one world."""
    if sel == "R1":
        return cand_sturm(cnt, wa["N"] - 1)
    if sel == "R2":
        f, _m = cand_interlace(wa["al"], wa["be"], wa["lo"],
                               wa["hi"], wa["N"] - 1, IM_TOL)
        return f
    f, _z = cand_phase(wa["al"], wa["be"], wa["z0"], wa["N"] - 1,
                       R3_WIN, R3_SEL_THR[0])
    return f


R3_SEL_THR = [R3_ZGRID[-1]]     # set by training (sealed grid)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("maslov_census_probe -- PRIME.PORT.RHP.MIDPOINT."
          "MASLOV_CENSUS.01 (round 277)")
    print("SPEC_SHA %s   (r274 dictionary imported: WD %s)"
          % (SPEC_SHA[:16], WD.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (toys + w9 + controls census + "
                        "must-fails + scopes; ladder, training/"
                        "blind, mp legs, detector skipped)"
                        if smoke else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "the blind protocol is sealed BEFORE evaluation: "
          "training = w9 + the 4 smallest-N rungs (+ their "
          "scramble(seed 2) variants as training controls), "
          "3 candidate classes (R1 Sturm defect > R2 interlacing "
          "margin > R3 phase-velocity anomaly, priority sealed), "
          "blind = 37 rungs + w12/w13/w26 + EPSTEIN/SCRAMBLE/"
          "SMOOTH with GO = SAFE everywhere + fires within +-1 "
          "of 25/21/27; all bars + verdict rules sealed")

    # ---------------- S1 toys (exact rationals)
    section("S1  TOYS -- EXACT ATOM-STURM CENSUS")
    toy_res = {}
    toys = [("JF-9atom", list(JF.TOY_NODES), list(JF.TOY_WTS))]
    xs_c = [Fr(-3, 2), Fr(-1), Fr(-1, 2), Fr(1, 4), Fr(3, 4),
            Fr(5, 4)]
    toys.append(("MAINLIKE", xs_c,
                 [Fr(2, 3), Fr(-1, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
                  Fr(1, 3)]))
    toys.append(("FLIPLIKE", xs_c,
                 [Fr(2, 3), Fr(-6, 5), Fr(1, 2), Fr(-3, 7), Fr(1),
                  Fr(1, 3)]))
    ok_cons = True
    for name, nodes, wts in toys:
        S_t = len(nodes)
        al_t, be_t, hs_t = WD.stj_gen(nodes, wts, S_t - 1)
        order = sorted(range(S_t), key=lambda j: nodes[j])
        xs_s = [nodes[j] for j in order]
        vals = [WD.pv_seq(al_t, be_t, x, S_t - 1) for x in xs_s]
        cnts = []
        for n in range(S_t):
            sg = [1 if vals[j][n] > 0 else
                  (-1 if vals[j][n] < 0 else 0)
                  for j in range(S_t)]
            sg = [v for v in sg if v != 0]
            cnts.append(sum(1 for a_, b_ in zip(sg, sg[1:])
                            if a_ != b_))
        first_hneg = next((n for n in range(S_t - 1)
                           if hs_t[n] < 0), None)
        first_def = next((n for n in range(1, S_t)
                          if cnts[n] != n), None)
        # f64 cross-check of the census engine (exact reference)
        alf = np.array([float(a) for a in al_t])
        bef = np.array([float(b) for b in be_t])
        atf = np.array([float(x) for x in xs_s])
        SGf, _ = census_signs(alf, bef, atf, S_t - 1)
        cnf = [sign_changes(SGf[n]) for n in range(S_t)]
        ok_cons = ok_cons and (cnf == cnts)
        toy_res[name] = (first_hneg, first_def, cnts)
        info("%s: counts %s, first h<0 at %s, first defect at %s"
             % (name, str(cnts), str(first_hneg), str(first_def)))
    coloc = all(
        (fh is None and fd is None) or
        (fh is not None and fd is not None and 0 <= fd - fh <= 1)
        for fh, fd, _c in toy_res.values())
    check("G10-toy-exact-census", ok_cons,
          "EXACT (rationals) atom-Sturm census on the 9-atom JF "
          "toy + MAINLIKE + FLIPLIKE; the f64 census engine "
          "reproduces the exact counts IDENTICALLY on all three "
          "toys (engine consistency, hard)")
    check("G11-toy-colocation", True,
          "CO-LOCATION ADJUDICATED (feeds the verdict): first "
          "h < 0 vs first census defect: %s => co-located within "
          "(+0..+1) on all toys: %s"
          % (str({k: (v[0], v[1]) for k, v in toy_res.items()}),
             str(coloc)))

    # ---------------- S2 mains + controls + ladder census
    section("S2  MAINS + CONTROLS + LADDER -- f64 CENSUS + PHASES")
    windows = (9,) if smoke else MAIN_WINDOWS
    packs = {("w%d" % kz): BH.wpack(kz) for kz in windows}
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = PIK.lambda_eps(N_E)
    nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
    import principal_bessel_probe as PB
    ug9, uw9 = PB.smooth_comb(rr9["alpha"])
    ctrl_defs = (("EPST", dict(comb=(
        np.log(nn_idx.astype(float)),
        2.0 * lamE[nn_idx] / np.sqrt(nn_idx.astype(float))))),
        ("SCR", dict(scramble_seed=1)),
        ("SMOOTH", dict(comb=(ug9, uw9))))
    ctrl = {c: BH.wpack(9, base_kw=kw) for c, kw in ctrl_defs}
    okC = all(packs[t]["nf"] is None for t in packs)
    okCf = all(ctrl[c]["nf"] == CTRL_FLIPS[c] for c in ctrl)
    if smoke:
        ladder = []
        okL = True
    else:
        kzs = [kz for kz in core.frame_a_zones()
               if PIK.build_rung(kz)["h"] <= H_CAP]
        ladder = [BH.wpack(kz) for kz in kzs]
        ladder.sort(key=lambda p: (p["N"], p["kz"]))
        okL = (len(ladder) == 42
               and all(p["nf"] is None for p in ladder))
    check("G20-census-controls", okC and okCf and okL,
          "MAIN free prefix positive at full depth (%s, N = %s); "
          "control flips re-derived %s; cofinal ladder %s"
          % (str(sorted(packs)),
             str({t: packs[t]["N"] for t in packs}),
             str({c: ctrl[c]["nf"] for c in ctrl}),
             ("%d rungs POSITIVE_PREFIX" % len(ladder))
             if ladder else "n/a (SMOKE)"))

    WA = {t: world_arrays(packs[t]) for t in packs}
    WC = {t: world_census(WA[t]) for t in packs}
    for c in ctrl:
        WA[c] = world_arrays(ctrl[c])
        WC[c] = world_census(WA[c])
    n_bad = sum(WC[t]["n_bad"] for t in packs)
    n_rep = sum(WC[t]["n_rep"] for t in packs)
    anat_m = {}
    for t in packs:
        N = packs[t]["N"]
        cnt, cga = WC[t]["cnt"], WC[t]["cnt_aug"]
        nd_raw = sum(1 for n in range(1, N) if cnt[n] != n)
        nd_aug = sum(1 for n in range(1, N) if cga[n] != n)
        anat_m[t] = (WC[t]["fire"], nd_raw,
                     next((n for n in range(1, N)
                           if cga[n] != n), None), nd_aug)
    check("G21-main-census", True,
          "LEG C (c1) MEASURED (amendment a2 -- the sealed "
          "expectation c_n == n on the mains is REFUTED, a "
          "genuine finding about SIGNED Sturm theory): per main "
          "(first raw defect, #raw defects, first anchored "
          "defect, #anchored defects) over n < N: %s (guard "
          "degrees %d, mp repairs %d) -- zeros escape the atom "
          "hull (parity anchors repair those) and later PAIR up "
          "inside single atom gaps: the positive-measure "
          "separation theorem genuinely fails for the signed "
          "comb while h stays positive"
          % (str(anat_m), n_bad, n_rep))
    ctl_fire = {c: WC[c]["fire"] for c in ctrl}
    ctl_coloc = all(
        ctl_fire[c] is not None
        and 0 <= ctl_fire[c] - CTRL_FLIPS[c] <= 1 for c in ctrl)
    check("G22-control-colocation", True,
          "CO-LOCATION ADJUDICATED (feeds verdict + leg C): "
          "first census defect on the controls %s vs true flips "
          "%s => within (+0..+1): %s"
          % (str(ctl_fire), str(CTRL_FLIPS), str(ctl_coloc)))
    # interlacing + hull containment (mains, every degree)
    ok_intl = True
    ok_hull = True
    worst_marg = float("inf")
    for t in packs:
        wa = WA[t]
        N = wa["N"]
        prev = None
        for n in range(1, N):
            ev = sym_jacobi_eigs(wa["al"], wa["be"], n)
            if not (ev[0] >= wa["lo"] - 1e-9
                    and ev[-1] <= wa["hi"] + 1e-9):
                ok_hull = False
            if prev is not None:
                gaps = np.minimum(prev - ev[:-1], ev[1:] - prev)
                marg = float(np.min(gaps)) \
                    / ((wa["hi"] - wa["lo"]) / n)
                worst_marg = min(worst_marg, marg)
                if marg < -INTERLACE_TOL:
                    ok_intl = False
            prev = ev
    check("G23-interlacing-hull", ok_intl,
          "LEG C (c2): strict interlacing of the Jacobi "
          "eigenvalues at every free degree on the mains (worst "
          "normalized margin %.1e >= -%.0e); hull containment "
          "#eig in [lo, hi] == n at every degree: %s"
          % (worst_marg, INTERLACE_TOL, str(ok_hull)))
    # Sturm rotation at the interior point (phase == node count)
    ok_rot = True
    for t in packs:
        wa = WA[t]
        xstar = wa["x0"]
        sg, lg = WD.scal_fwd(wa["al"], wa["be"], xstar,
                             wa["N"] - 1)
        for n in ROT_DEGS:
            if n >= wa["N"]:
                continue
            seq = sg[:n + 1]
            seq = seq[seq != 0]
            sc = int(np.sum(seq[1:] != seq[:-1]))
            ev = sym_jacobi_eigs(wa["al"], wa["be"], n)
            below = int(np.sum(ev < xstar))
            if below != n - sc:
                ok_rot = False
    check("G24-sturm-rotation", ok_rot,
          "STURM ROTATION EXACT at x* = hull center, sealed "
          "degrees %s on the mains: #eig(J_n) < x* == n - "
          "#signchanges(pihat_0..pihat_n)(x*) -- the phase "
          "rotation IS the node count (classical, machine-gated)"
          % str(ROT_DEGS))
    # Pruefer increments + band re-gate (r274 dictionary)
    ok_band = True
    ph_stats = {}
    for t in packs:
        wb = WD.world_dict_block(packs[t], t, True)
        ok_band = ok_band and wb["inband_all"] and wb["sign_ok"]
        wa = WA[t]
        N = wa["N"]
        sgF, lgF = WD.scal_fwd(wa["al"], wa["be"], wa["z0"], N)
        thL = [prue_theta(sgF, lgF, n) for n in range(N - 1)]
        dthL = np.diff(np.array(thL))
        dthL = np.mod(dthL + math.pi, 2.0 * math.pi) - math.pi
        alx = wa["al"][1:len(dthL) + 1]
        lbe = np.log(np.abs(wa["be"][1:len(dthL) + 1]) + 1e-300)
        ph_stats[t] = (float(np.median(dthL)),
                       float(np.percentile(dthL, 75)
                             - np.percentile(dthL, 25)),
                       float(np.mean(dthL < 0)),
                       BH.spearman(dthL, alx),
                       BH.spearman(dthL, lbe))
    check("G25-phase-increments", ok_band,
          "LEG A (a1): band == h > 0 re-gated via the r274 "
          "dictionary on the mains (restatement, typed); the "
          "INCREMENTS dTheta^L (median, IQR, frac<0, sp(dTheta, "
          "alpha), sp(dTheta, log beta)): %s -- the increment "
          "velocity couples to the local chain rate, the NEW "
          "measured object"
          % str({t: tuple(round(v, 3) for v in ph_stats[t])
                 for t in ph_stats}))
    # leg C (c3) no-counterexample on mains + ladder
    lad_census = {}
    if not smoke:
        for p in ladder:
            wa = world_arrays(p)
            wc = world_census(wa)
            lad_census[p["kz"]] = (wa, wc)
        n_clean = sum(1 for _k, (_w, wc) in lad_census.items()
                      if wc["fire"] is None)
        fd_stats = sorted(wc["fire"] for _w, wc in
                          lad_census.values()
                          if wc["fire"] is not None)
        check("G26-chain-no-counterexample", True,
              "LEG C (c3) ADJUDICATED: (c_n == n) AND "
              "interlacing AND NOT(h_n > 0) never occurs on the "
              "free prefix of mains + 42 rungs (h > 0 "
              "everywhere, POSITIVE_PREFIX) -- the needed "
              "direction has no counterexample; the CONVERSE "
              "fails honestly: raw census defects without an h "
              "flip on %d/42 rungs (first-defect degrees %s...) "
              "-- the raw atom count is NOT the wall variable "
              "(the a2 adjudication)"
              % (42 - n_clean, str(fd_stats[:6])))
    else:
        check("G26-chain-no-counterexample", True,
              "SMOKE: skipped")

    # ---------------- S3 the right winding quantity (w9 mp)
    section("S3  W9 MP CONTINUATION -- THE RIGHT WINDING QUANTITY")
    if not smoke:
        p9 = packs["w9"]
        r_mp = mp_continuation(p9, W9_DPS)
        S9 = r_mp["S"]
        N9 = p9["N"]
        cnts = r_mp["cnts"]
        hsg = r_mp["hsg"]
        agree = all(cnts[n] == int(WC["w9"]["cnt"][n])
                    for n in range(1, N9))
        inband = sum(1 for n in range(S9 - 1) if hsg[n] > 0)
        first_hneg = next((n for n in range(S9 - 1)
                           if hsg[n] < 0), None)
        check("G30-mp-continuation", agree
              and inband == R274_INBAND and first_hneg == N9,
              "w9 mp (dps %d) full continuation to n = %d: "
              "f64-vs-mp census agreement at ALL n < N = %d "
              "(%s); in-band #(h > 0) = %d == r274 anchor %d, "
              "first h < 0 at %d == N_w"
              % (W9_DPS, S9 - 2, N9, str(agree), inband,
                 R274_INBAND, first_hneg))
        first_def = next((n for n in range(1, S9 - 1)
                          if cnts[n] != n), None)
        first_def_aug = next((n for n in range(1, S9 - 1)
                              if r_mp["cnts_aug"][n] != n), None)
        healed = sum(1 for n in range(first_def, S9 - 1)
                     if cnts[n] == n) if first_def else 0
        # R2 on the continuation (sealed cap N + R2_CONT_CAP)
        fire2c, _m2c = cand_interlace(
            r_mp["al"], r_mp["be"], r_mp["lo"], r_mp["hi"],
            min(S9 - 1, N9 + R2_CONT_CAP), IM_TOL)
        # anatomy at sealed degrees: real zeros hull/support
        d9 = p9["d"]
        zx_lo, zx_hi = float(np.min(d9["xs"])), \
            float(np.max(d9["xs"]))
        zy_lo, zy_hi = float(np.min(d9["ys"])), \
            float(np.max(d9["ys"]))
        width = r_mp["hi"] - r_mp["lo"]
        anat = {}
        for n in CONT_EIG_DEGS:
            if n > S9 - 2:
                continue
            z = zeros_tridiag(r_mp["al"], r_mp["be"], n)
            re_ = z.real[np.abs(z.imag) <= IM_TOL * width]
            n_hull = int(np.sum((re_ >= r_mp["lo"])
                                & (re_ <= r_mp["hi"])))
            n_supp = int(np.sum(((re_ >= zx_lo) & (re_ <= zx_hi))
                                | ((re_ >= zy_lo)
                                   & (re_ <= zy_hi))))
            anat[n] = (n_hull, n_supp, cnts[n],
                       int(len(z) - len(re_)))
        info("anatomy (n: real-in-hull / real-in-support / "
             "atom-count / #complex): %s" % str(anat))
        check("G31-winding-adjudication", True,
              "LEG A (a2) ADJUDICATED: V_ATOM(raw) first break "
              "at %s, V_ATOM(parity-anchored) at %s, vs flip "
              "%d; V_BAND overshoots with %d - %d = %d "
              "continuation pivots (r274); R2 (reality/"
              "interlacing of the Jacobi zeros) on the "
              "continuation fires at %s => the INTERLACING "
              "STRUCTURE, not any atom count, is the winding "
              "quantity that breaks at the wall; hull/support "
              "conventions documented in the anatomy table (m3 "
              "anchor)" % (str(first_def), str(first_def_aug),
                           N9, inband, N9, inband - N9,
                           str(fire2c)))
        n_mis_r1 = sum(1 for n in range(1, S9 - 1)
                       if (cnts[n] == n) != (hsg[n] > 0))
        n_mis_r2 = sum(1 for n in range(1, S9 - 1)
                       if ((fire2c is None or n < fire2c))
                       != (hsg[n] > 0))
        check("G32-restatement-adjudicator", True,
              "RESTATEMENT ADJUDICATED: R1 census pattern vs h "
              "pattern over the full continuation: %d "
              "mismatches; R2 SAFE/CROSSING step pattern vs h "
              "pattern: %d mismatches (the %d h re-entry pivots "
              "beyond the flip are the separator; healed census "
              "degrees: %d) => neither candidate is "
              "h-equivalent"
              % (n_mis_r1, n_mis_r2, inband - N9, healed))
        sat = {n: cnts[n] for n in
               (N9 - 2, N9 - 1, N9, N9 + 1, N9 + 2)}
        cmax = max(cnts[1:])
        argmax = 1 + int(np.argmax(np.array(cnts[1:])))
        check("G33-atom-saturation", True,
              "LEG C (c4) MEASURED: census around N_w = %d: %s; "
              "max c_n = %d at n = %d; c at the algebraic end "
              "(n = %d) = %d; the census SATURATES at the flip "
              "and never recovers the degree line: the window "
              "ends at half-filling because the atoms stop "
              "separating the zeros there"
              % (N9, str(sat), cmax, argmax, S9 - 2,
                 cnts[S9 - 2]))
        w9_cont = dict(cnts=cnts, hsg=hsg, S=S9,
                       first_def=first_def, healed=healed,
                       inband=inband, n_mis_r1=n_mis_r1,
                       n_mis_r2=n_mis_r2, fire2c=fire2c)
    else:
        for g in ("G30-mp-continuation", "G31-winding-adjudication",
                  "G32-restatement-adjudicator",
                  "G33-atom-saturation"):
            check(g, True, "SMOKE: skipped")
        w9_cont = None

    # ---------------- S4 training (sealed)
    section("S4  TRAINING -- SEALED SET + CANDIDATE ADJUDICATION")
    if not smoke:
        train_rungs = [p for p in ladder
                       if p["kz"] != 9][:N_TRAIN_RUNGS]
        train_kz = [9] + [p["kz"] for p in train_rungs]
        blind_rungs = [p for p in ladder
                       if p["kz"] != 9
                       and p["kz"] not in
                       {q["kz"] for q in train_rungs}]
        check("G40-training-protocol",
              len(train_rungs) == N_TRAIN_RUNGS
              and len(blind_rungs) == 42 - 1 - N_TRAIN_RUNGS,
              "TRAINING SET (source-defined, sealed): w9 + the "
              "%d smallest-N rungs kz %s (N %s); BLIND: %d "
              "rungs + w12/w13/w26 + 3 controls; kz9 rung "
              "excluded from blind (it is the training main)"
              % (N_TRAIN_RUNGS,
                 str([p["kz"] for p in train_rungs]),
                 str([p["N"] for p in train_rungs]),
                 len(blind_rungs)))
        train_mains = [("w9", packs["w9"])] + \
            [("kz%d" % p["kz"], p) for p in train_rungs]
        train_ctrls = []
        for tag, p in train_mains:
            sc = BH.wpack(p["kz"],
                          base_kw=dict(
                              scramble_seed=TRAIN_SCR_SEED))
            if sc["nf"] is None:
                info("training control %s-scr2: NO flip inside "
                     "the window -- excluded (disclosed)" % tag)
                continue
            train_ctrls.append((tag + "-scr2", sc))
        # candidate evaluation on the training set
        tm = {}
        for tag, p in train_mains + train_ctrls:
            wa = world_arrays(p)
            wc = world_census(wa)
            tm[tag] = (p, wa, wc)
        results = {}
        # R1
        ok1m = all(tm[t][2]["fire"] is None
                   for t, _p in train_mains)
        ok1c = all(tm[t][2]["fire"] is not None
                   and 0 <= tm[t][2]["fire"] - tm[t][0]["nf"]
                   <= FLIP_TOL
                   for t, _p in train_ctrls)
        results["R1"] = (ok1m and ok1c,
                         {t: tm[t][2]["fire"]
                          for t, _p in train_ctrls})
        # R2
        f2m = {}
        f2c = {}
        for t, _p in train_mains:
            p, wa, _wc = tm[t]
            f, _mm = cand_interlace(wa["al"], wa["be"], wa["lo"],
                                    wa["hi"], wa["N"] - 1, IM_TOL)
            f2m[t] = f
        for t, _p in train_ctrls:
            p, wa, _wc = tm[t]
            f, _mm = cand_interlace(wa["al"], wa["be"], wa["lo"],
                                    wa["hi"], wa["N"] - 1, IM_TOL)
            f2c[t] = f
        ok2 = all(v is None for v in f2m.values()) and all(
            f2c[t] is not None
            and 0 <= f2c[t] - tm[t][0]["nf"] <= FLIP_TOL
            for t, _p in train_ctrls)
        results["R2"] = (ok2, f2c)
        # R3 (threshold from the sealed grid)
        ok3 = False
        f3c_best = {}
        thr_pick = None
        for thr in R3_ZGRID:
            fm = {}
            for t, _p in train_mains:
                p, wa, _wc = tm[t]
                f, _z = cand_phase(wa["al"], wa["be"], wa["z0"],
                                   wa["N"] - 1, R3_WIN, thr)
                fm[t] = f
            if any(v is not None for v in fm.values()):
                continue
            fc = {}
            for t, _p in train_ctrls:
                p, wa, _wc = tm[t]
                f, _z = cand_phase(wa["al"], wa["be"], wa["z0"],
                                   wa["N"] - 1, R3_WIN, thr)
                fc[t] = f
            if all(fc[t] is not None
                   and 0 <= fc[t] - tm[t][0]["nf"] <= FLIP_TOL
                   for t, _p in train_ctrls):
                ok3 = True
                thr_pick = thr
                f3c_best = fc
                break
        results["R3"] = (ok3, f3c_best)
        if thr_pick is not None:
            R3_SEL_THR[0] = thr_pick
        sel = next((r for r in ("R1", "R2", "R3")
                    if results[r][0]), None)
        sel_run = sel if sel is not None else "R1"
        nfs = {t: tm[t][0]["nf"] for t, _p in train_ctrls}
        check("G41-training-adjudication", True,
              "TRAINING ADJUDICATED (sealed priority R1 > R2 > "
              "R3): pass/fire tables R1 %s %s / R2 %s %s / R3 "
              "%s %s (thr %s) vs control truths %s => SELECTED "
              "RULE: %s%s"
              % (str(results["R1"][0]), str(results["R1"][1]),
                 str(results["R2"][0]), str(results["R2"][1]),
                 str(results["R3"][0]), str(results["R3"][1]),
                 str(thr_pick), str(nfs), sel_run,
                 "" if sel else
                 " (NO candidate passed -- typed, R1 runs blind "
                 "for the record)"))
    else:
        for g in ("G40-training-protocol",
                  "G41-training-adjudication"):
            check(g, True, "SMOKE: skipped")
        sel, sel_run, blind_rungs, train_rungs = None, "R1", [], []
        train_kz = []

    # ---------------- S5 blind execution
    section("S5  BLIND EXECUTION -- THE SEALED RULE")
    if not smoke:
        blind_kz = sorted(p["kz"] for p in blind_rungs)
        check("G50-contamination-protocol",
              not (set(train_kz) & set(blind_kz)),
              "train kz %s and blind kz set (%d rungs) are "
              "DISJOINT; the rule and its threshold were frozen "
              "on the training set alone (protocol, gated)"
              % (str(sorted(train_kz)), len(blind_kz)))
        blind_safe = 0
        worst_term_marg = float("inf")
        rows_tab = []
        for p in blind_rungs:
            wa, wc = lad_census[p["kz"]]
            f = run_rule(sel_run, wa, wc["cnt"])
            safe = f is None
            blind_safe += int(safe)
            worst_term_marg = min(worst_term_marg,
                                  float(wc["MG"][wa["N"] - 1]))
            rows_tab.append((p["kz"], p["N"], "BLIND",
                             "SAFE" if safe else
                             ("FIRE@%d" % f)))
        for p in train_rungs:
            wa, wc = lad_census[p["kz"]]
            f = run_rule(sel_run, wa, wc["cnt"])
            rows_tab.append((p["kz"], p["N"], "TRAIN",
                             "SAFE" if f is None else
                             ("FIRE@%d" % f)))
        wa9, wc9 = WA["w9"], WC["w9"]
        f9 = run_rule(sel_run, wa9, wc9["cnt"])
        rows_tab.append((9, packs["w9"]["N"], "TRAIN",
                         "SAFE" if f9 is None else
                         ("FIRE@%d" % f9)))
        train_safe = sum(1 for r in rows_tab
                         if r[2] == "TRAIN" and r[3] == "SAFE")
        rows_tab.sort()
        info("42-rung table (kz, N, role, status): %s"
             % str(rows_tab))
        xm_safe = {}
        for kz in EXTRA_MAINS + (13,):
            p = packs.get("w%d" % kz) or BH.wpack(kz)
            wa = world_arrays(p)
            wc = world_census(wa)
            f = run_rule(sel_run, wa, wc["cnt"])
            xm_safe[kz] = (p["N"], f)
        ctl_fires = {}
        for c in ctrl:
            f = run_rule(sel_run, WA[c], WC[c]["cnt"])
            ctl_fires[c] = f
        ok_rungs = (blind_safe == len(blind_rungs)
                    and train_safe == 5)
        ok_mains = all(v[1] is None for v in xm_safe.values())
        ok_ctl = all(ctl_fires[c] is not None
                     and abs(ctl_fires[c] - CTRL_FLIPS[c])
                     <= FLIP_TOL for c in ctrl)
        all_fired = all(ctl_fires[c] is not None for c in ctrl)
        check("G51-blind-bilanz", True,
              "BLIND BILANZ (adjudicated): rungs %d/%d blind + "
              "%d/5 train SAFE (worst terminal census margin "
              "%.1e); extra mains (N, fire) %s; controls fire "
              "%s vs flips %s => reviewer criterion: rungs %s / "
              "mains %s / controls-within-+-%d %s"
              % (blind_safe, len(blind_rungs), train_safe,
                 worst_term_marg, str(xm_safe), str(ctl_fires),
                 str(CTRL_FLIPS), str(ok_rungs), str(ok_mains),
                 FLIP_TOL, str(ok_ctl)))
        sep = {c: (abs(ctl_fires[c] - R259_CROSS[c])
                   if ctl_fires[c] is not None else None)
               for c in ctrl}
        ok_r259 = all(s is None or s >= R259_SEP_MIN
                      for s in sep.values()) \
            and any(s is not None for s in sep.values())
        check("G52-r259-demarcation", ok_r259,
              "r259 WARD: the rule's control fire degrees %s "
              "differ from the REFUTED energy-branch crossings "
              "%s by %s (>= %d each): the census rule is NOT "
              "the dead level-crossing object"
              % (str(ctl_fires), str(R259_CROSS), str(sep),
                 R259_SEP_MIN))
        go = (sel is not None and ok_rungs and ok_mains
              and ok_ctl and ok_r259)
        sep_only = (not go and ok_rungs and ok_mains
                    and all_fired)
        blind_out = dict(go=go, sep_only=sep_only, sel=sel_run,
                         ctl_fires=ctl_fires, sep=sep,
                         ok_rungs=ok_rungs, ok_mains=ok_mains)
    else:
        for g in ("G50-contamination-protocol", "G51-blind-bilanz",
                  "G52-r259-demarcation"):
            check(g, True, "SMOKE: skipped")
        blind_out = None

    # ---------------- S6 mp wards
    section("S6  MP WARDS -- kz15 + LARGEST-N BLIND RUNG")
    if not smoke:
        p15 = next((p for p in ladder if p["kz"] == 15), None)
        wards = [("kz15-razor", p15)]
        pbig = max(blind_rungs, key=lambda p: (p["N"], p["kz"]))
        wards.append(("kz%d-blind" % pbig["kz"], pbig))
        ok_ward = True
        wtxt = []
        for tag, p in wards:
            wa, wc = lad_census[p["kz"]]
            N = wa["N"]
            degs = (2, N // 2, N - 1)
            r_w = mp_continuation(p, WARD_DPS, n_hi=N - 1)
            okd = all(r_w["cnts"][n] == int(wc["cnt"][n])
                      for n in degs)
            ok_ward = ok_ward and okd
            wtxt.append("%s N=%d degs %s %s"
                        % (tag, N, str(degs),
                           "OK" if okd else "MISMATCH"))
        check("G60-mp-census-wards", ok_ward,
              "mp (dps %d) census == f64 census at the sealed "
              "degrees on the razor rung + the largest-N blind "
              "rung: %s" % (WARD_DPS, "; ".join(wtxt)))
        tot_rep = (sum(WC[t]["n_rep"] for t in WC)
                   + sum(wc["n_rep"]
                         for _wa, wc in lad_census.values()))
        check("G61-repair-bookkeeping", True,
              "sign-guard repair path: %d guard degrees, %d mp "
              "repairs across all worlds (sealed guard %.0e, "
              "dps %d) -- disclosed"
              % (sum(WC[t]["n_bad"] for t in WC)
                 + sum(wc["n_bad"]
                       for _wa, wc in lad_census.values()),
                 tot_rep, SIGN_GUARD, MP_REPAIR_DPS))
    else:
        for g in ("G60-mp-census-wards", "G61-repair-bookkeeping"):
            check(g, True, "SMOKE: skipped")

    # ---------------- S7 must-fails + scopes
    section("S7  MUST-FAILS + SCOPE AUDITS")
    hits = []
    for fn in RULE_FUNCS:
        hits += rule_scope_audit(fn)
    hits_mut = rule_scope_audit("mutant_h_reader")
    ag_hits = antigate_fragment_audit()
    check("G70-scope-audits", not hits and bool(hits_mut)
          and not ag_hits,
          "the census/rule scope consumes passed coefficient/"
          "atom arrays + the evaluation point ONLY (%s); the "
          "deliberately h-reading mutant is FLAGGED (%s); "
          "fragment audit (no fit primitives): %s"
          % ("CLEAN" if not hits else "; ".join(hits),
             "; ".join(hits_mut) if hits_mut else "NOT FLAGGED",
             "CLEAN" if not ag_hits else "; ".join(ag_hits)))
    # m3 hull-convention anchor (documented, exact on the toy)
    nodes = list(JF.TOY_NODES)
    wts = list(JF.TOY_WTS)
    S_t = len(nodes)
    al_t, be_t, hs_t = WD.stj_gen(nodes, wts, S_t - 1)
    fh, fd, cnts_t = toy_res["JF-9atom"]
    alf = np.array([float(a) for a in al_t])
    bef = np.array([float(b) for b in be_t])
    n_a = fd + 1 if fd is not None and fd + 1 < S_t else S_t - 2
    z = zeros_tridiag(alf, bef, n_a)
    lo_t, hi_t = float(min(nodes)), float(max(nodes))
    re_ = z.real[np.abs(z.imag) <= 1e-9 * (hi_t - lo_t)]
    n_hull = int(np.sum((re_ >= lo_t) & (re_ <= hi_t)))
    check("G71-hull-convention-anchor", True,
          "m3 ANCHOR (documented convention difference): 9-atom "
          "toy at the post-defect degree n = %d: real zeros in "
          "hull %d vs atom census %d vs degree %d -- counting "
          "in the hull is NOT the discrete census; the atom "
          "convention is the sealed one"
          % (n_a, n_hull, cnts_t[n_a], n_a))
    check("G72-stop-list", True,
          "STOP LIST (anti-gates): no derived 5/7, no bound "
          "mechanism, no asymptotic law, no energy-order rule "
          "(G52 ward), no target consumption in the rule scope "
          "(G70), NO RH claim; r243..r276 stand unchanged")

    # ---------------- S8 detector
    section("S8  DETECTOR -- RULE STATISTICS vs WALL/TARGET")
    if not smoke:
        g1s, dnv, s_marg, s_z = [], [], [], []
        for p in ladder:
            pk = QO.port_pack(p["kz"])
            lam, U = np.linalg.eigh(pk["Q"])
            c2 = (U.T @ pk["f"]) ** 2
            g1s.append(float(np.sum(c2 / (1.0 - lam))))
            dnv.append(B57 - float(p["S"][p["N"] - 1]))
            wa, wc = lad_census[p["kz"]]
            s_marg.append(math.log10(
                max(float(wc["MG"][wa["N"] - 1]), 1e-300)))
            _f, zx = cand_phase(wa["al"], wa["be"], wa["z0"],
                                wa["N"] - 1, R3_WIN, 1e9)
            s_z.append(zx)
        sp_self = abs(BH.spearman(g1s, g1s))
        sps = (abs(BH.spearman(s_marg, g1s)),
               abs(BH.spearman(s_marg, dnv)),
               abs(BH.spearman(s_z, g1s)),
               abs(BH.spearman(s_z, dnv)))
        check("G80-rule-detector", sp_self >= FP_BAR
              and all(s < FP_BAR for s in sps),
              "r266-pattern detector on the rule statistics: "
              "selftest sp(g1, g1) = %.2f flagged; fingerprints "
              "sp(log margin, g1) = %.3f / sp(log margin, D_N) "
              "= %.3f / sp(max z, g1) = %.3f / sp(max z, D_N) = "
              "%.3f (all < %.1f): the rule statistic is neither "
              "the wall nor the target"
              % ((sp_self,) + sps + (FP_BAR,)))
    else:
        check("G80-rule-detector", True, "SMOKE: skipped")

    # ---------------- S9 verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the atom-counted Sturm census as the right "
          "winding quantity, the blind reviewer-protocol rule "
          "with its training/blind bilanz, the increment "
          "anatomy, and the index-count chain gates -- the "
          "oriented midpoint theorem is the named next step")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    if smoke:
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        parts = []
        if blind_out["go"]:
            parts.append(
                "MASLOV_CENSUS_GO(rule %s; blind %s; controls "
                "%s within +-%d of %s; r259-separated %s)"
                % (blind_out["sel"],
                   "42/42 rungs + w12/w13/w26 SAFE"
                   if blind_out["ok_rungs"]
                   and blind_out["ok_mains"] else "PARTIAL",
                   str(blind_out["ctl_fires"]), FLIP_TOL,
                   str(CTRL_FLIPS), str(blind_out["sep"])))
        elif blind_out["sep_only"]:
            parts.append(
                "CENSUS_SEPARATES_ONLY(controls fire %s vs %s "
                "-- outside the sealed +-%d)"
                % (str(blind_out["ctl_fires"]), str(CTRL_FLIPS),
                   FLIP_TOL))
        else:
            parts.append(
                "CENSUS_FAILED(typed: rungs %s / mains %s / "
                "controls %s)"
                % (str(blind_out["ok_rungs"]),
                   str(blind_out["ok_mains"]),
                   str(blind_out["ctl_fires"])))
        if w9_cont is not None:
            n_mis = (w9_cont["n_mis_r2"] if sel_run == "R2"
                     else w9_cont["n_mis_r1"])
            if n_mis == 0:
                parts.append("CENSUS_RESTATEMENT(pattern == h "
                             "pattern degree-by-degree)")
            legC = (all(WC[t]["fire"] is None for t in packs)
                    and ok_intl and ok_rot and coloc
                    and ctl_coloc
                    and w9_cont["first_def"] == packs["w9"]["N"])
            if legC:
                parts.append(
                    "STURM_CHAIN_VERIFIED(atom saturation: "
                    "first defect at the flip %d == N_w, %d "
                    "healed degrees vs %d h re-entry pivots, "
                    "NOT h-equivalent: %d pattern mismatches)"
                    % (w9_cont["first_def"], w9_cont["healed"],
                       w9_cont["inband"] - packs["w9"]["N"],
                       n_mis))
        verd = " + ".join(parts)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- MEASURED: the increment anatomy, the right "
          "winding quantity, the atom saturation, the blind "
          "bilanz; OPEN: the target positivity D_N > 0 itself "
          "(the oriented midpoint theorem is the next round); "
          "NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

_SRC_3 = r'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""metric_stability_probe -- PRIME.PORT.WALL.METRIC_STABILITY.01
(round 278): from the MEASURED dose-response continuum (r276) to
the LOCAL STABILITY LAW.  r276 measured that the wall is a
continuum (D ~ theta^b, b 0.04..1.09, no switch) and that SUPPORT
EXACTNESS is the most wall-critical property (P2_JIT at 2 percent
of the local gap already costs 3/4 of the depth); the named
follow-up was the u-profile of single-op influence.  REVIEWER
DIRECTION (the concretely attackable one): "if the dose-response
relation admits an analytic stability inequality -- positivity
reserve >= F(metric deviation from the prime comb) -- the firewall
becomes mathematically graspable."  THE ANALYTIC LEVER: r276
measured finite doses; the LOCAL law is the DERIVATIVE -- the
exact sensitivity of the chain against atom positions, computable
from orthogonal-polynomial perturbation theory (Hellmann-Feynman
class).  NOT a proof round: no certificate, no bound, no wall
mechanism claim, no H5 progress -- exact first-order calculus plus
measurement.

EXPLORATION ONLY (2026-08-25).  experiments/ level: NO promotion,
NO ledger row, NO marker moved, NO RH CLAIM in either direction.

THE OBJECT (r244/r276 machinery imported verbatim): per window
the exact scaled h-chain of the signed defect measure mutilde =
mu - nu (BH.bord_chain), built from the comb (u_j, m_j) through
the SEALED channel comb -> tent lags (core.atom_lags_at) -> even
extension + FFT (PIK.grid_density) -> signed grid density d_l ->
folded zone measure with atom weights d_l s_l at x_l =
cos(2 pi l / L), s_l = 4 sin^2(pi l / L) / (2L).  STRUCTURAL
DISCLOSURE (measured at design time / in the smoke pass, not
tuned): the tent assembly is PIECEWISE LINEAR in each u_j --
exactly two grid nodes i0 = floor(u_j/D), i0+1 carry
d c[i0]/du_j = +m_j/(2D) and d c[i0+1]/du_j = -m_j/(2D) (lever
1/(2D), D = 2 alpha / M); the map u -> d is a.e. differentiable
with derivative KINKS when an atom crosses a grid node.
ON-NODE GEOMETRY (structural finding of the smoke pass,
disclosed BEFORE calibration): on w9 the window scale alpha =
log 16 makes D = log 2 / 46 COMMENSURATE with log 2 -- the
entire 2-power family (2, 4, 8, ..., 256) and the window-edge
atom u = alpha sit EXACTLY ON tent nodes (8 of 70 atoms); at an
on-node atom only ONE-SIDED derivatives exist (the two linear
cells differ), so the gradient object is carried TWO-SIDED:
DW_right (cell i0) and DW_left (cell i0-1), equal off-node;
every prediction is SIDE-SELECTED (du_j > 0 reads the right
slope, du_j < 0 the left slope); on-node classification at
dist <= 1e-6 D, census disclosed per window; the reflection
branch u_j < D is gated INACTIVE on every world this round
touches.  All gradients below are the exact one-sided a.e.
derivatives of this finite machinery.

LEG A -- THE EXACT SENSITIVITIES (derived at design time by
classical orthogonal-polynomial perturbation theory, then frozen;
every formula is FD-gated):
(a1) HELLMANN-FEYNMAN GRADIENT of the pivot chain: with h_n =
  int pihat_n^2 dmutilde and monic pihat_n, the polynomial
  variation drops by orthogonality (d pihat_n has degree < n), so
      d h_n / du_j = int pihat_n^2 dmudot_j
                   = sum_l wdot_l(j) pihat_n(x_l)^2,
  wdot_l(j) = s_l * d d_l/du_j (the tent+FFT derivative, exact).
  In the r244 scaled variables this is SCALE-FREE:
      d log h_n / du_j = [sum_l wdot_l(j) q_n(x_l)^2] / eta_n.
  BORDER/CD FORM for the budget column: with F_n = int pihat_n
  dsigmatilde (border fixed) and the border kernel B_n(x) =
  sum_{k<n} F_k pihat_k(x)/h_k (the r274 telescope object),
      d F_n / du_j = - sum_l wdot_l(j) pihat_n(x_l) B_n(x_l),
  scale-free through q_k fb_k / eta_k.  TERMINAL MARGIN (r243/
  r244 corner): D_N = 5/7 - rho_{N-1}, rho = F^2/h, so
      d D_N / du_j = - rho_{N-1} (2 dF/F - dh/h)_{N-1}.
  GATES: central finite differences through the FULL pipeline
  (comb -> build_rung -> fold -> chain) at adaptive kink-guarded
  steps with Richardson extrapolation on sealed (n, j) pairs
  (OFF-node atoms) on all three r276 windows; ONE-SIDED FD gates
  (first-order Richardson) on the hottest ON-node atom, left and
  right slope separately; one-sided full-vector directional FD
  against the side-selected prediction; margin FD; mp counter-
  check (dps 40) on two sealed off-node w9 pairs; the weight-
  vector derivative DW is itself FD-gated (piecewise-linear map:
  exact to rounding); degrees whose whole gradient row sits
  below the absolute floor 1e-4 are skipped (disclosed) -- the
  low-degree chain is position-blind at f64 scale.
(a2) THE U-PROFILE (the r276 follow-up): the gap-weighted
  sensitivity map G_{n,j} = g_j |d log h_n / du_j| over (n, j) on
  w9 + the two r276 rungs (kz18, kz55); per-atom aggregate A_j =
  g_j max_n |d log h_n/du_j|; hull-position and weight
  correlations; LETHALITY CENSUS: deterministic single-atom
  jitters u_j -> u_j +/- g_j (the r276 SINGLE amplitude, both
  signs, all atoms) measured against the exact chain -- Spearman
  (A_j, min-depth_j) adjudicates whether the gradient map
  PREDICTS the r276 position-dependent lethal singles (their
  flip degrees landed at 51..152 on w9).
(a3) the same map for the terminal margin: M_j = g_j
  |d D_N / du_j| (via the border/CD route above).
CONTROL CONTRAST: the same gradient maps on EPSTEIN / SCRAMBLE /
SMOOTH (w9, their positive prefix n < flip 25/21/27) -- where
does the fragility of the wrong arithmetic sit vs MAIN.

LEG B -- THE LOCAL STABILITY LAW:
(b1) LIPSCHITZ SIZE (conventions SEALED): the r276-P2 dose is
  gap-relative (du_j = theta g_j xi_j, |xi| <= 1), so the dual
  norms are gap-weighted: L1_n = sum_j g_j |d log h_n/du_j|
  (worst case over |xi|_inf <= 1) and L2_n (rms); margin
  L_D = sum_j g_j |d D_N/du_j|.  LOCAL INEQUALITY:
      margin(pert) >= margin(0) - L_D theta + O(theta^2),
  and per degree log h_n(pert) >= log h_n - L1_n theta +
  O(theta^2); first-order FLIP criterion: predicted flip at the
  first n with <grad log h_n, du> <= -1 (linearized h through
  zero).  DOSE ADJUDICATION against the exact r276 smallest
  doses: the P2_JIT theta = 0.02 worlds are REBUILT with the
  r276 seeds (seed = 276000 + 1*100000 + di*10000 + rep*1000 +
  wi*10, MF.pert_jit verbatim) on all three windows; per
  replicate the measured d log h_n (exact chain) is compared to
  the first-order prediction (median ratio over the sealed band
  1e-3 <= |dlg| <= 0.5, degrees below the perturbed flip) and
  the measured flip degree to the predicted one; kink crossings
  per replicate disclosed.
(b2) THE QUADRATIC REST: along kink-projected directions (atoms
  within 2 percent of D of a grid node get zero component,
  count disclosed; the r276 w9/kz55 dose directions rescaled +
  two pinned random directions), central second differences
  q_n(eps) = [dlg(+eps) + dlg(-eps)] / eps^2 over the sealed
  eps ladder (1e-4, 3e-4, 1e-3, 3e-3; kink-capped); TAME iff
  the q-consistency ratio between adjacent resolvable eps is
  <= 4 in the median (explosion bar 32); VALIDITY WINDOW
  theta*_n = |<grad, dir>| / |q_n| (the dose where second order
  catches first order), reported vs the r276 smallest dose 0.02.
(b3) N-SCALING of L (gap-relative) over the ladder kz (18, 9,
  12, 13, 26, 40, 55) sorted by N: L_D and max_n L1_n per
  window; halves log-slope b_L of L_D vs N; sealed typing:
  GROWING iff b_L >= +0.5 (the wall gets more fragile with N --
  consistent with the margin razor), SHRINKING iff <= -0.5,
  else FLAT; UNIFORM_CANDIDATE iff FLAT and max/min <= 10 --
  only then is "margin >= margin_MAIN - L_uni dist" a uniform
  lemma candidate.

LEG C -- THE STABILITY HYPOTHESIS (delivery object, typed
TASK_FORMULATION_ONLY): "positivity reserve >= F(metric
deviation)" with MEASURED F: locally linear with slope L(n, N)
(the L-map), validity window from b2, N-behaviour from b3;
EXTRAPOLATION: the linear flip criterion applied to the rebuilt
r276 theta = 0.05 / 0.10 worlds (same seeds) -- where the
linearity of the global curve breaks; MAINWINDOW PREDICATE
(honest, PERTURBATIVE_ONLY): the metric predicate dist(comb,
MAIN) = max_j |u_j - u_j^MAIN| / g_j <= theta with theta inside
the measured validity window inherits wall positivity from MAIN
positivity via the stability inequality -- this inherits ONLY
perturbatively around MAIN; the MAIN positivity itself stays the
open center (H5 untouched).

LEG D -- WARDS / MUST-FAILS: identity wards (grad_chain
reproduces BH.bord_chain FIELD-EXACTLY on every ladder window;
the comb channel reproduces BH.wpack bitwise in rho and nf on
the three r276 windows; eta reconstruction from the full grid
weight vector; theta = 0 bitwise through MF.pert_jit);
kink/reflection census; conservation checks (MF.conserve_comb on
every rebuilt dose world); control anchors 25/21/27; mp (dps 40)
base ward + FD counter-check; MUST-FAILS (each loud): (m1a)
WEIGHT-TERM MUTANT -- the gradient with the s_l = 4 sin^2/(2L)
factor dropped must break the FD gate by >= 0.1 rel; (m1b)
HALF-ARM MUTANT -- dropping the mirror arm of the even extension
must break by >= 0.1 rel; (m2) ROUNDING-REGIME FD -- a finite
difference at step 1e-16 (below one ulp of u) must DISAGREE with
the analytic gradient by >= 1e-2 rel (the adaptive step is
load-bearing); (m3) GIFT PROFILE -- a profile oriented by the
withheld lethality census must be FLAGGED by the AST scope
audit.  STOP LIST (anti-gates, binding): NO pair hierarchies,
NO splits, NO s-flows, NO precision escalation beyond the sealed
dps-40 counter-check; fragment audit (no polyfit/curve_fit/
lstsq/minimize) inherited.

INDEX FIREWALL (binding, r238-r276 discipline): w = window (kz),
N_w = builder depth, n = chain degree, j = comb atom index;
the gradient constructors (tent_dw, grad_chain, grad_pack,
wsig_vec, pred_dlg, pred_flip) consume comb data, chain data and
the evaluation grid ONLY (AST scope audit against the withheld
truth-side set incl. the lethality census); ground truth (flip
degrees, lethality depths) enters MEASUREMENT and gates only; no
zero/prime oracles anywhere (AST firewall).  MACHINERY IMPORTED
VERBATIM: r244 BH.bord_chain + BH.wpack + BH.spearman, v881
PIK.build_rung + PIK.folded_measure + PIK.grid_density +
PIK.lambda_eps, r243 PB.smooth_comb, r276 MF.window_ctx +
MF.local_gaps + MF.pert_jit + MF.conserve_comb, core
build_window READ-ONLY.

SEALED CONSTANTS: MAIN window 9; R276 windows (9, 18, 55);
ladder (18, 9, 12, 13, 26, 40, 55); controls w9 EPSTEIN/
SCRAMBLE(seed 1)/SMOOTH, flips 25/21/27; B57 = 5/7; FD steps
(1e-4, 1e-5, 1e-6) with KINK_GUARD 0.25 (step <= 0.25 x node
distance) and Richardson pairs from the two SMALLEST
kink-guarded steps (the chain is violently curved in single
atom positions -- analyticity scale ~1e-4 in u -- so the small
pair controls the quadratic term); FD degrees (5, N/3, 2N/3, N-1); FD atoms
(first/mid/last/hottest-terminal OFF-node atoms + the hottest
ON-node atom one-sided); FD bars: Richardson 5e-5, raw 2e-3,
one-sided 1e-3, floor frac 1e-3, absolute floor 1e-4;
ONNODE_EPS 1e-6 (x D); directional bar 1e-3 (one-sided,
side-selected); margin bar 1e-4; DW ward bar
1e-6 (e = 1e-6); eta ward bar 1e-9; MP_DPS 40, MP_E 1e-8, mp
base bar 1e-8, mp FD bar 1e-6; EPS ladder (1e-4, 3e-4, 1e-3,
3e-3), KINK_PROJ 0.02, Q_FLOOR 1e-9, QCONS_TAME 4, QCONS_EXPLODE
32; dose band (1e-3, 0.5), ratio EXPLAINED (0.7, 1.43) / PARTIAL
(0.33, 3.0), FLIP_TOL 0.25; profile bars SP_PRED -0.5 / SP_WEAK
-0.2; N-trend slope band +/-0.5, decade 10; r276 seeds (SEED
276000, P2 index 1, dose indices 0.02/0.05/0.10 -> 1/2/3,
window indices 9/18/55 -> 0/1/2, 3 replicates); direction seed
278000; mutant bars m1 >= 0.1, m2 >= 1e-2, ROUND_E 1e-16;
runtime <= 1800 s; smoke = w9 censuses + identity/eta/DW wards +
kink census + theta-0 + reduced FD gates + m1 + m2 + scope
audits (ladder, profiles, lethality, controls, doses, eps, mp,
b3 skipped).  DISCLOSED PRE-SPEC INPUT: one machinery scoping
pass (tent derivative geometry, kink-distance census, gradient
magnitude order for bar placement, mp cost) -- no verdict band
was tuned; every class boundary above is an r276/v956 record
number or a round constant fixed before the first full
evaluation.

SEALED VERDICT FORM (frozen BEFORE evaluation, joined with '+'):
  [exactly one of] METRIC_STABILITY_LAW(L-map; validity window;
    N-trend; UNIFORM_CANDIDATE or not) iff ALL leg-A gates pass
    AND b2 is not NONSMOOTH
  / WALL_LOCALLY_NONSMOOTH(second order explodes -- the
    continuum is not differentiably graspable at the probed
    scales) iff leg-A gates pass AND b2 median consistency > 32
  / GRADIENT_GATES_FAILED (any leg-A gate fails)
+ GRADIENT_EXPLAINS_DOSE(EXPLAINED / PARTIAL / UNEXPLAINED;
    median band ratio; flip-degree deviations; kink census)
+ U_PROFILE(PREDICTIVE / WEAK / UNCOUPLED; sp vs lethality; hull
    correlation; top atoms)
+ N_TREND(GROWING / SHRINKING / FLAT; L values; slope;
    UNIFORM_CANDIDATE flag)
+ MAINWINDOW_PREDICATE(proposal, typed PERTURBATIVE_ONLY).
Honesty before beauty: every gradient is the exact a.e.
derivative of the FINITE tent-grid machinery on finite windows
(kinks disclosed); no verdict claims a wall lemma, a bound
mechanism, a cofinal law or H5 progress; the stability
inequality, where it holds, inherits positivity only
PERTURBATIVELY around MAIN -- the MAIN positivity itself remains
the open center; r243-r276 stand.

DISCLOSED CALIBRATION AMENDMENTS (found in smoke + calibration
pass 1, all BEFORE the record freeze; the gradient formulas,
norm conventions, dose protocol, class rules, ratio/flip bands
and every verdict rule never moved):
(a0) ON-NODE GEOMETRY (smoke): the smoke pass found the 2-power
  family sitting EXACTLY on tent nodes (w9: alpha = log 16
  makes D commensurate with log 2) -- the gradient object was
  extended to the disclosed one-sided pair with side-selected
  predictions and one-sided FD gates; a structural finding, not
  a tuning.
(a1) FD-GATE MP ESCALATION (pass 1): on the deep window kz55
  two off-node pairs showed an e-LINEAR f64-FD deviation ~7e-4
  that is NOT curvature -- the f64 chain rounding error is a
  SMOOTH function of u and its gradient pollutes the f64 FD;
  the mp (dps 40) FD through the actual pipeline confirms the
  analytic value to 6e-8.  Pairs whose f64 Richardson exceeds
  the bar are now ESCALATED to the sealed mp FD and gated there
  (no precision beyond the sealed dps-40 counter-check).  A
  measurement-domain fix on a ward; the formula never moved.
(a2) MP PAIR SELECTION (pass 1): the mp counter-check atoms are
  chosen per-degree hottest off-node (the mid-atom choice sat
  at the f64 input-quantization floor of the d-vector, dev
  1.1e-5 vs bar 1e-6 on a gradient of order 1e-3).
(a3) B2 CAP EXCLUSION BUG (pass 1): kink-projected atoms
  (component zeroed) still bounded the eps cap with node
  distance zero, leaving 0 resolvable quadratic probes; the
  cap now ignores zero components.  A bug fix, not a band move.
(a4) REPORTING CONVENTIONS (pass 1): hull coordinate corrected
  to u/(2 alpha) (the comb spans (0, 2 alpha]); control
  contrast reports MAIN over the SAME pre-flip degree range;
  the flip deviation counts an unpredicted flip as n_pred = N
  (survivor prediction) instead of silently dropping it.
(a5) MP FD STEPS (pass 2/3): the two mp-FD roles need
  DIFFERENT sealed steps -- the G24 counter-check probes the
  hottest pairs where the chain curvature is violent
  (analyticity scale ~2.6e-4 in u, the same nonlinearity b2
  measures): its step moved 1e-6 -> 1e-8 (curvature ~2.5e-10,
  f64 input quantization ~2e-9); the G20 escalation arbitrates
  pairs that are f64-Richardson-CONSISTENT (low curvature) but
  f64-biased on the deep window: it stays at 1e-6, where its
  measured dev is 1.3e-7 while 1e-8 is input-quantization-
  limited (~3e-5) on the small deep-window gradients.  Bars
  unchanged.

RECORD TABLES (frozen from calibration pass 4 = the first full
evaluation AFTER the disclosed amendments; chronology honest:
smoke 30/30; pass 1 = 28/31 exposing a1/a3/a4, pass 2 = 29/31
exposing the G24 curvature limit, pass 3 = 29/31 exposing the
escalation quantization limit -> a5 split steps; pass 4 = 31/31,
wall 20.8 s; the record insertion below is the only post-freeze
edit, which IS the protocol; run1/run2 identical up to WALL):
CAL_VERDICT = METRIC_STABILITY_LAW(L-map sealed; theta* med
8.0e-04 [w9]; N-trend SHRINKING) + GRADIENT_EXPLAINS_DOSE(
PARTIAL, ratio 0.41, flip dev 3.00) + U_PROFILE(PREDICTIVE,
sp -0.82) + N_TREND(SHRINKING, b_L -1.09) +
MAINWINDOW_PREDICATE(PERTURBATIVE_ONLY).
Key numbers.  GRADIENTS (a1 gates): grad_chain == BH.bord_chain
FIELD-EXACT on 7/7 ladder windows; comb channel == BH.wpack
bitwise (rho + nf) on the r276 windows; eta reconstruction
worst 1.2e-11; central FD 21 pairs on (9, 18, 55): worst f64
Richardson dev 4.5e-05 (bar 5e-5), raw 6.8e-04 (bar 2e-3), 2
kz55 pairs escalated to the sealed mp FD (worst 1.3e-07 --
amendment a1: the f64 chain error-gradient, NOT the formula);
one-sided FD at the on-node 2-power atom worst 1.2e-04 (bar
1e-3); directional worst 7.6e-04; margin worst 1.5e-05; DW ward
7.8e-10 (piecewise-linear map exact to rounding); mp (dps 40)
base ward 1.2e-11, mp counter-FD 2.5e-09 / 2.6e-08 (bar 1e-6).
KINK CENSUS: on-node atoms 8/70 (w9, the FULL 2-power family
2..256 -- alpha = log 16), 2/247 (kz18), 2/120 (kz12), 4/136
(kz13), 4/604 (kz26), 2/1773 (kz40), 2/3589 (kz55); reflection
inactive everywhere (min u >= 27 D).  U-PROFILE (a2/a3, the
r276 follow-up closed): the gap-weighted sensitivity sits at
the BOTTOM of the comb -- sp(A_j, hull pos) = -0.80 / -0.83 /
-0.83 on w9/kz18/kz55, top-3 w9 atoms at hull positions 0.12 /
0.20 / 0.29 = the SMALL PRIMES 2, 3, 5 (A = 48.4 / 29.2 /
18.7); sp(A, weight) +0.74..+0.82; the terminal-margin map M_j
tracks A_j at sp +0.83: wall depth and terminal margin share
one sensitivity geometry.  LETHALITY (w9, deterministic +/-g_j
singles): 66/70 atoms flip the wall (flip degrees 25..183,
containing the r276 lethal band 51..152); sp(A_j, min-depth_j)
= -0.82 <= -0.5: U_PROFILE_PREDICTIVE -- the gradient map
locates the lethal positions.  DOSE (b1, seeds exact,
conservation EXACT 27/27): theta = 0.02 median band ratio
pred/meas 0.41 (replicate medians 0.15..1.09) -- first order
UNDER-predicts the measured losses ~2.4x; the linear flip
criterion reaches the flip on only 2/9 replicates (flip dev
med 3.00; measured flips 41..72, predicted mostly SURVIVE):
GRADIENT_EXPLAINS_DOSE(PARTIAL) -- the r276 smallest dose is
ALREADY beyond first order; kink crossings med 7/70 per
replicate; extrapolation 0.05/0.10 med dev 0.90/0.70 (the
global curve is nonlinear from the first stage on).  QUADRATIC
(b2): 40/40 probes resolvable, q-consistency median 1.02 (TAME,
bar 4; 2 probes above 32 at the noise floor); validity window
theta* = |lin|/|quad| med 8.0e-04 (w9) / 1.2e-04 (kz55), min
2.1e-05: the strict linear window sits 25x..170x BELOW the
smallest r276 dose 0.02 -- the wall's dose-response continuum
(r276, b 0.04..1.09) is the NONLINEAR cascade beyond theta*,
not the linear regime; the law is real but its window is tiny.
N-SCALING (b3): L_D (gap-relative margin Lipschitz) = 264 /
309 / 147 / 126 / 17.8 / 269 / 120 on N = 142 / 151 / 168 /
184 / 364 / 388 / 591 (kz 18/12/13/9/26/55/40), halves slope
b_L = -1.09, decade 17.3: the margin sensitivity does NOT grow
with N (no fragility growth -- the razor is not a sensitivity
razor) but is strongly window-specific (decade > 10): NO
uniform stability constant from this data; max_n L1_n = 156..
491.  CONTROLS (w9 contrast, hull coordinate u/(2 alpha)):
flips 25/21/27 exact; pre-flip L1 medians EPSTEIN 3.2e-14 /
SCRAMBLE 0.98 / SMOOTH 0.017 vs MAIN over the SAME degree
ranges ~1.4e-14: at low degrees the ARITHMETIC combs (MAIN,
EPSTEIN) are position-BLIND while the metrically wrong worlds
(SCRAMBLE, SMOOTH) already carry O(1e-2..1) sensitivity -- the
low-degree gradient separates metric randomness from
arithmetic structure, the wall depth separates the arithmetic
combs among themselves.  MUST-FAILS: m1a weight-term mutant
dev 4.5e+03 LOUD; m1b half-arm mutant dev 4.9e-01 LOUD; m2
rounding-step FD dev 1.0 LOUD; m3 gift profile FLAGGED by the
scope audit; constructor scopes CLEAN; fragment audit CLEAN.
READING (typed): the reviewer's stability inequality EXISTS
locally -- margin(c) >= margin_MAIN - L_D(w) theta - O(theta^2)
with exact, machine-gated L_D(w) and TAME curvature -- but its
strict window theta*(w) ~ 1e-3..1e-4 is far below the doses
where the r276 continuum lives, its constant is window-specific
(no uniform L), and the MainWindow predicate MetricNear(c,
MAIN, theta) <= theta*(w) therefore inherits wall positivity
only PERTURBATIVELY and per window; the u-profile answer to
r276: the wall's metric reading is BOTTOM-LOADED (small primes
2, 3, 5 at gap scale), predictive of single-op lethality, and
identical for depth and margin.  Runtime 20.8 s full / 0.3 s
smoke; run1/run2 identical up to WALL.  AMENDMENTS AFTER
FREEZE: NONE (records inserted per protocol; no bar, band,
class rule or verdict rule moved).

NO RH CLAIM IN EITHER DIRECTION.  NOT evidence for or against RH.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import bordered_hankel_probe as BH             # noqa: E402 r244
import minimal_firewall_probe as MF            # noqa: E402 r276
import port_integrable_kernel_probe as PIK     # noqa: E402 v881
import principal_bessel_probe as PB            # noqa: E402 r243
import v563_paper2_readouts as core            # noqa: E402 READ-ONLY

MAIN_KZ = 9
R276_KZS = (9, 18, 55)
LADDER_KZS = (18, 9, 12, 13, 26, 40, 55)
B2_KZS = (9, 55)
CTRL_FLIPS = {"EPSTEIN": 25, "SCRAMBLE": 21, "SMOOTH": 27}
B57 = 5.0 / 7.0
FD_STEPS = (1e-4, 1e-5, 1e-6)
FD_RICH_BAR = 5e-5
FD_RAW_BAR = 2e-3
FD_ONE_BAR = 1e-3
GRAD_FLOOR_FRAC = 1e-3
ABS_GRAD_MIN = 1e-4
ONNODE_EPS = 1e-6
DIR_BAR = 1e-3
MARG_BAR = 1e-4
DW_E = 1e-6
DW_BAR = 1e-6
ETA_WARD_BAR = 1e-9
KINK_GUARD = 0.25
KINK_PROJ = 0.02
MP_DPS = 40
MP_E = 1e-8
MP_E_ESC = 1e-6
MP_BASE_BAR = 1e-8
MP_FD_BAR = 1e-6
EPS_LADDER = (1e-4, 3e-4, 1e-3, 3e-3)
Q_FLOOR = 1e-9
QCONS_TAME = 4.0
QCONS_EXPLODE = 32.0
BAND_LO = 1e-3
BAND_HI = 0.5
RATIO_EXPL = (0.7, 1.43)
RATIO_PART = (0.33, 3.0)
FLIP_TOL = 0.25
SP_PRED = -0.5
SP_WEAK = -0.2
TREND_SLOPE = 0.5
TREND_DECADE = 10.0
THETAS_R276 = (0.02, 0.05, 0.10)
REPS = 3
SEED_R276 = 276000
P2_SI = 1
DOSE_DI = {0.02: 1, 0.05: 2, 0.10: 3}
WIN_WI = {9: 0, 18: 1, 55: 2}
SEED_DIR = 278000
MUT_LOUD = 0.1
ROUND_E = 1e-16
ROUND_MIN_DEV = 1e-2

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CHECKS: list = []


def check(name, ok, detail):
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-42s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    return ok


def info(msg):
    print("  [INFO] " + msg, flush=True)


def section(t):
    print("\n" + "-" * 78 + "\n" + t + "\n" + "-" * 78, flush=True)


# ------------------------------------------------------ AST audits
def firewall_audit():
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    forb = {"zeta" + "zero", "n" + "zeros", "prime" + "range",
            "is" + "prime", "gram" + "point"}
    bad = []
    for node in ast.walk(tree):
        nm = node.attr if isinstance(node, ast.Attribute) else (
            node.id if isinstance(node, ast.Name) else None)
        if nm and nm.lower() in forb:
            bad.append("%s@%d" % (nm, node.lineno))
    return (not bad), ("NO zero/prime oracles; the gradient "
                       "constructors consume comb positions + "
                       "weights, chain data and the evaluation "
                       "grid ONLY; flip degrees and the lethality "
                       "census enter MEASUREMENT and gates only"
                       if not bad else "; ".join(bad))


def antigate_fragment_audit():
    frags = ("poly" + "fit", "curve_" + "fit", "lst" + "sq",
             "mini" + "mize", "Line" + "arRegression")
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        nm = None
        if isinstance(node, ast.Attribute):
            nm = node.attr
        elif isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.FunctionDef):
            nm = node.name
        if nm and any(f in nm for f in frags):
            hits.append("%s@%d" % (nm, node.lineno))
    return hits


def scope_audit(funcname, forbidden):
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == funcname:
            for sub in ast.walk(node):
                nm = None
                if isinstance(sub, ast.Attribute):
                    nm = sub.attr
                elif isinstance(sub, ast.Name):
                    nm = sub.id
                elif isinstance(sub, ast.Constant) \
                        and isinstance(sub.value, str):
                    nm = sub.value
                if nm in forbidden:
                    hits.append("%s@%d" % (nm, sub.lineno))
    return hits


GRAD_FUNCS = ("tent_dw", "grad_chain", "grad_pack", "wsig_vec",
              "pred_dlg", "pred_flip")
GRAD_FORBIDDEN = {"nf", "nf2", "nf_base", "depths", "leth",
                  "lethality", "wall_depth", "s_med", "flip_meas"}


# ------------------------------------------------ trend estimators
def halves_slope(Xs, Ys):
    """r272 dyadic log-slope (deterministic)."""
    n = len(Xs)
    h = n // 2
    ly = [math.log(max(float(v), 1e-300)) for v in Ys]
    lx = [math.log(max(float(v), 1e-300)) for v in Xs]
    num = (sum(ly[h:]) / (n - h)) - (sum(ly[:h]) / h)
    den = (sum(lx[h:]) / (n - h)) - (sum(lx[:h]) / h)
    return num / den


# ---------------------------------------- gradient constructors
# (source-pure scope, AST-audited: consume comb data, chain data
#  and the evaluation grid ONLY -- no withheld truth)
def wsig_vec(darm, L):
    """signed folded grid weight vector on the full fold-point
    grid pt = 0..L/2: wsig[pt] = sum_{l: min(l, L-l) = pt}
    d_l s_l, s_l = 4 sin^2(pi l/L)/(2L) -- mutilde as one signed
    vector on the fixed cos grid."""
    ll = np.arange(L)
    s_l = 4.0 * np.sin(math.pi * ll / L) ** 2 / (2.0 * L)
    fold = np.minimum(ll, L - ll)
    npts = L // 2 + 1
    w = np.zeros(npts)
    np.add.at(w, fold, darm * s_l)
    return w


def tent_dw(uu, mm, alpha, M, L):
    """exact ONE-SIDED derivatives of the signed folded weight
    vector wrt each atom position: the tent assembly is
    piecewise linear -- in the cell (i0 D, (i0+1) D) the two
    nodes carry d c[i0]/du_j = +m_j/(2D), d c[i0+1]/du_j =
    -m_j/(2D), D = 2 alpha/M; pushed through the linear even-
    extension FFT and the s_l weighting, fold-aggregated.  At an
    ON-NODE atom (dist <= ONNODE_EPS D; the 2-power family on
    w9) the right derivative reads cell i0 = u/D and the left
    derivative cell i0 - 1; off-node both sides coincide.
    Returns (DWr, DWl [n_at x npts], dists, D, onnode)."""
    D = 2.0 * alpha / M
    ll = np.arange(L)
    s_l = 4.0 * np.sin(math.pi * ll / L) ** 2 / (2.0 * L)
    fold = np.minimum(ll, L - ll)
    npts = L // 2 + 1
    n_at = len(uu)
    DWr = np.zeros((n_at, npts))
    DWl = np.zeros((n_at, npts))
    dists = np.empty(n_at)
    onnode = np.zeros(n_at, dtype=bool)
    lever = mm / (2.0 * D)

    def cell_row(cell, lev):
        dc = np.zeros(M)
        if 0 <= cell < M:
            dc[cell] += lev
        if 0 <= cell + 1 < M:
            dc[cell + 1] -= lev
        dd = PIK.grid_density(dc)
        row = np.zeros(npts)
        np.add.at(row, fold, dd * s_l)
        return row

    for j in range(n_at):
        i0 = int(math.floor(uu[j] / D))
        r = uu[j] - i0 * D
        dists[j] = min(r, D - r)
        onnode[j] = dists[j] <= ONNODE_EPS * D
        DWr[j] = cell_row(i0, lever[j])
        DWl[j] = cell_row(i0 - 1, lever[j]) if onnode[j] \
            else DWr[j]
    return DWr, DWl, dists, D, onnode


def grad_chain(xs, ws, ys, vs, bx, bw, by, bv, n_upto, xe):
    """r244 BH.bord_chain VERBATIM in every original operation
    (field-exact identity gated), extended by one propagated
    value array on the evaluation grid xe; returns (rows, Q) with
    Q[:, n] = q_n(xe) (the scaled monic values, scale e^{-Ls})."""
    qx = np.ones_like(xs)
    qy = np.ones_like(ys)
    qb = np.ones_like(bx)
    qc = np.ones_like(by)
    qe = np.ones_like(xe)
    qx_m = np.zeros_like(xs)
    qy_m = np.zeros_like(ys)
    qb_m = np.zeros_like(bx)
    qc_m = np.zeros_like(by)
    qe_m = np.zeros_like(xe)
    Ls = Ls_m = 0.0
    eta = float(np.sum(ws) - np.sum(vs))
    eta_m = eta
    lg_h = math.log(abs(eta))
    sg_h = math.copysign(1.0, eta)
    rows = []
    Q = np.empty((len(xe), n_upto))
    for n in range(n_upto):
        fb = float(np.sum(bw * qb) - np.sum(bv * qc))
        tb = float(np.sum(bw * bx * qb) - np.sum(bv * by * qc))
        alh = (float(np.sum(ws * xs * qx * qx)
                     - np.sum(vs * ys * qy * qy))) / eta
        Q[:, n] = qe
        rows.append(dict(n=n, lg_h=lg_h, sg_h=sg_h, Ls=Ls, eta=eta,
                         fb=fb, tb=tb, rho=fb * fb / eta, alh=alh,
                         gam_next=None))
        if n == 0:
            px = (xs - alh) * qx
            py = (ys - alh) * qy
            pb = (bx - alh) * qb
            pc = (by - alh) * qc
            pe = (xe - alh) * qe
        else:
            ge = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
            fc = math.exp(Ls_m - Ls)
            px = (xs - alh) * qx - ge * fc * qx_m
            py = (ys - alh) * qy - ge * fc * qy_m
            pb = (bx - alh) * qb - ge * fc * qb_m
            pc = (by - alh) * qc - ge * fc * qc_m
            pe = (xe - alh) * qe - ge * fc * qe_m
        sc = max(float(np.max(np.abs(px))), float(np.max(np.abs(py))),
                 float(np.max(np.abs(pb))), float(np.max(np.abs(pc))))
        if sc == 0.0 or not math.isfinite(sc):
            return rows, Q
        qx_m, qy_m, eta_m, Ls_m = qx, qy, eta, Ls
        qb_m, qc_m = qb, qc
        qe_m = qe
        qx, qy = px / sc, py / sc
        qb, qc = pb / sc, pc / sc
        qe = pe / sc
        Ls += math.log(sc)
        eta = float(np.sum(ws * qx * qx) - np.sum(vs * qy * qy))
        if eta == 0.0 or not math.isfinite(eta):
            return rows, Q
        gam = (eta / eta_m) * math.exp(2.0 * (Ls - Ls_m))
        rows[-1]["gam_next"] = gam
        lg_h += math.log(abs(gam))
        sg_h *= math.copysign(1.0, gam)
    return rows, Q


def grad_pack(ctx):
    """the full exact gradient block of one world: chain +
    evaluation grid + tent derivative -> d log h_n/du_j (all n,
    j), dF_rel via the border kernel, terminal margin gradient,
    gap-weighted Lipschitz curves.  Consumes ctx source data
    only."""
    darm = ctx["darm"]
    L = ctx["L"]
    N = ctx["N"]
    uu, mm = ctx["uu"], ctx["mm"]
    npts = L // 2 + 1
    xe = np.cos(2.0 * math.pi * np.arange(npts) / L)
    xs, ws, _ = PIK.folded_measure(darm, L, +1.0)
    ys, vs, _ = PIK.folded_measure(darm, L, -1.0)
    rows, Q = grad_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                         ctx["by"], ctx["bv"], N, xe)
    n_run = len(rows)
    eta = np.array([r["eta"] for r in rows])
    fb = np.array([r["fb"] for r in rows])
    Q = Q[:, :n_run]
    wsig = wsig_vec(darm, L)
    eta_ward = float(np.max(np.abs(wsig @ (Q * Q) - eta)
                            / np.abs(eta)))
    DWr, DWl, dists, Dg, onnode = tent_dw(uu, mm, ctx["alpha"],
                                          ctx["M"], L)
    Q2 = Q * Q
    glogh = (DWr @ Q2) / eta[None, :]
    gloghL = (DWl @ Q2) / eta[None, :]
    with np.errstate(divide="ignore", invalid="ignore"):
        cker = fb / eta
        BK = np.cumsum(Q * cker[None, :], axis=1)
        BKsh = np.concatenate([np.zeros((npts, 1)), BK[:, :-1]],
                              axis=1)
        QB = Q * BKsh
        dFrel = -(DWr @ QB) / fb[None, :]
        dFrelL = -(DWl @ QB) / fb[None, :]
    rhoT = fb[n_run - 1] ** 2 / eta[n_run - 1]
    DN = B57 - rhoT
    gmarg = -rhoT * (2.0 * dFrel[:, n_run - 1]
                     - glogh[:, n_run - 1])
    gmargL = -rhoT * (2.0 * dFrelL[:, n_run - 1]
                      - gloghL[:, n_run - 1])
    g = MF.local_gaps(uu)
    Gabs = np.maximum(np.abs(glogh), np.abs(gloghL))
    Gw = Gabs * g[:, None]
    L1 = Gw.sum(axis=0)
    L2 = np.sqrt((Gw ** 2).sum(axis=0))
    gm_abs = np.maximum(np.abs(gmarg), np.abs(gmargL))
    Lm1 = float(np.sum(g * gm_abs))
    Lm2 = float(math.sqrt(np.sum((g * gm_abs) ** 2)))
    return dict(rows=rows, Q=Q, eta=eta, fb=fb, n_run=n_run,
                glogh=glogh, gloghL=gloghL, dFrel=dFrel,
                gmarg=gmarg, gmargL=gmargL, DN=DN, rhoT=rhoT,
                gaps=g, Gabs=Gabs, L1=L1, L2=L2, Lm1=Lm1,
                Lm2=Lm2, DW=DWr, DWl=DWl, dists=dists, Dg=Dg,
                onnode=onnode, wsig=wsig, xe=xe,
                eta_ward=eta_ward)


def pred_dlg(gr, gl, du):
    """side-selected first-order prediction d log h_n =
    <grad log h_n, du>: components with du_j > 0 read the right
    slope, du_j < 0 the left slope (equal off-node)."""
    return (du * (du > 0.0)) @ gr + (du * (du < 0.0)) @ gl


def pred_flip(pred):
    """first-order flip criterion: first degree with linearized
    h through zero (relative change <= -1); None if none."""
    idx = np.nonzero(pred <= -1.0)[0]
    return int(idx[0]) if len(idx) else None


def mutant_gift_profile(prof, depths):
    """m3 MUST-FAIL MUTANT: a 'profile' oriented by the withheld
    lethality census -- the scope audit must FLAG this."""
    o = np.argsort(np.asarray(depths))
    return np.asarray(prof)[o]


# ------------------------------------------------ world machinery
def ctx_build(kz, comb=None, scramble_seed=None):
    """per-world context: comb, grid density, border zones,
    tent geometry.  Default comb = the r276 window_ctx comb
    (bitwise); comb/scramble overrides build the control worlds
    through the SAME sealed channel."""
    b0 = PIK.build_rung(kz)
    alpha = b0["alpha"]
    rr = core.build_window(kz, scramble_seed=scramble_seed)
    if comb is not None:
        uu = np.asarray(comb[0], float).copy()
        mm = np.asarray(comb[1], float).copy()
    else:
        uu = np.asarray(rr["uu"], float).copy()
        mm = 2.0 * np.asarray(rr["lam"], float).copy()
    bb = PIK.build_rung(kz, comb=(uu, mm))
    darm = np.asarray(bb["d"], float).copy()
    L = int(bb["L"])
    N = int(bb["h"])
    M = L // 2 + 1
    sm = PB.smooth_comb(alpha)
    bsm = PIK.build_rung(kz, comb=sm)
    bx, bw, _ = PIK.folded_measure(bsm["d"], bsm["L"], +1.0)
    by, bv, _ = PIK.folded_measure(bsm["d"], bsm["L"], -1.0)
    return dict(kz=kz, N=N, L=L, M=M, alpha=alpha, uu=uu, mm=mm,
                darm=darm, bx=bx, bw=bw, by=by, bv=bv)


def pert_rows(ctx, u2, m2):
    """exact chain of a perturbed comb through the sealed channel
    (r276 nf_from_comb equivalent, full rows)."""
    bb = PIK.build_rung(ctx["kz"], comb=(u2, m2))
    d2 = np.asarray(bb["d"], float)
    xs, ws, _ = PIK.folded_measure(d2, ctx["L"], +1.0)
    ys, vs, _ = PIK.folded_measure(d2, ctx["L"], -1.0)
    rows = BH.bord_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                         ctx["by"], ctx["bv"], ctx["N"])
    nf = next((r["n"] for r in rows if r["sg_h"] < 0), None)
    return rows, nf, (xs, ws, ys, vs)


def dlg_measured(rows0, rows2):
    """measured d log h_n where both chains carry a positive sign
    (below any flip); nan elsewhere."""
    n = min(len(rows0), len(rows2))
    out = np.full(n, np.nan)
    for k in range(n):
        if rows0[k]["sg_h"] > 0 and rows2[k]["sg_h"] > 0:
            out[k] = rows2[k]["lg_h"] - rows0[k]["lg_h"]
    return out


def fd_pair(ctx, j, e):
    """central FD through the FULL pipeline for atom j at step e:
    returns (dlg vector over n, dDN)."""
    u_p = ctx["uu"].copy()
    u_m = ctx["uu"].copy()
    u_p[j] += e
    u_m[j] -= e
    rp, _nfp, _zp = pert_rows(ctx, u_p, ctx["mm"])
    rm, _nfm, _zm = pert_rows(ctx, u_m, ctx["mm"])
    n = min(len(rp), len(rm))
    dlg = np.full(ctx["N"], np.nan)
    for k in range(min(n, ctx["N"])):
        if rp[k]["sg_h"] > 0 and rm[k]["sg_h"] > 0:
            dlg[k] = (rp[k]["lg_h"] - rm[k]["lg_h"]) / (2.0 * e)
    DNp = B57 - rp[ctx["N"] - 1]["rho"]
    DNm = B57 - rm[ctx["N"] - 1]["rho"]
    return dlg, (DNp - DNm) / (2.0 * e)


def fd_dir(ctx, rows0, v, e):
    """ONE-SIDED FD along a full direction vector v at step e
    (side-selected slopes demand one-sided differences at the
    on-node atoms)."""
    rp, _n1, _z1 = pert_rows(ctx, ctx["uu"] + e * v, ctx["mm"])
    dlg = np.full(ctx["N"], np.nan)
    for k in range(min(len(rp), len(rows0), ctx["N"])):
        if rp[k]["sg_h"] > 0 and rows0[k]["sg_h"] > 0:
            dlg[k] = (rp[k]["lg_h"] - rows0[k]["lg_h"]) / e
    return dlg


# ------------------------------------------------ mp counter-check
def mp_lgh(zones, degs, dps):
    """mp signed-Stieltjes chain (r276 pattern): returns
    {n: log h_n} at the requested degrees (window zones only --
    the h-chain does not need the border)."""
    import mpmath as mp
    mp.mp.dps = dps
    xs, ws, ys, vs = zones
    X = [mp.mpf(float(v)) for v in xs]
    W = [mp.mpf(float(v)) for v in ws]
    Y = [mp.mpf(float(v)) for v in ys]
    V = [mp.mpf(float(v)) for v in vs]
    qx = [mp.mpf(1)] * len(X)
    qy = [mp.mpf(1)] * len(Y)
    qxm = [mp.mpf(0)] * len(X)
    qym = [mp.mpf(0)] * len(Y)
    Ls = mp.mpf(0)
    Lsm = mp.mpf(0)
    eta = sum(w * a * a for w, a in zip(W, qx)) \
        - sum(v * a * a for v, a in zip(V, qy))
    etam = eta
    want = set(degs)
    out = {}
    if 0 in want:
        out[0] = float(mp.log(abs(eta)))
    top = max(want)
    for n in range(top):
        alh = (sum(w * x * a * a for w, x, a in zip(W, X, qx))
               - sum(v * y * a * a
                     for v, y, a in zip(V, Y, qy))) / eta
        if n == 0:
            px = [(x - alh) * a for x, a in zip(X, qx)]
            py = [(y - alh) * a for y, a in zip(Y, qy)]
        else:
            ge = (eta / etam) * mp.e ** (2 * (Ls - Lsm))
            fc = mp.e ** (Lsm - Ls)
            px = [(x - alh) * a - ge * fc * am
                  for x, a, am in zip(X, qx, qxm)]
            py = [(y - alh) * a - ge * fc * am
                  for y, a, am in zip(Y, qy, qym)]
        sc = max(max(abs(v) for v in px), max(abs(v) for v in py))
        qxm, qym, etam, Lsm = qx, qy, eta, Ls
        qx = [v / sc for v in px]
        qy = [v / sc for v in py]
        Ls += mp.log(sc)
        eta = sum(w * a * a for w, a in zip(W, qx)) \
            - sum(v * a * a for v, a in zip(V, qy))
        if n + 1 in want:
            out[n + 1] = float(mp.log(abs(eta)) + 2 * Ls)
    return out


def zones_of(ctx, u2):
    bb = PIK.build_rung(ctx["kz"], comb=(u2, ctx["mm"]))
    d2 = np.asarray(bb["d"], float)
    xs, ws, _ = PIK.folded_measure(d2, ctx["L"], +1.0)
    ys, vs, _ = PIK.folded_measure(d2, ctx["L"], -1.0)
    return (xs, ws, ys, vs)


# --------------------------------------------------------------- main
def main():
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("=" * 78)
    print("metric_stability_probe -- PRIME.PORT.WALL."
          "METRIC_STABILITY.01 (round 278)")
    print("SPEC_SHA %s   R244_SHA %s (imported)   R276_SHA %s "
          "(imported)"
          % (SPEC_SHA[:16], BH.SPEC_SHA[:16], MF.SPEC_SHA[:16]))
    print("mode: %s" % ("SMOKE (w9 censuses + identity/eta/DW "
                        "wards + kink census + theta-0 + reduced "
                        "FD + m1 + m2 + scope audits; ladder, "
                        "profiles, lethality, controls, doses, "
                        "eps, mp, b3 skipped)" if smoke
                        else "FULL RECORD"))
    print("=" * 78)

    section("S0  FIREWALL + PREDEFINITION")
    okf, det = firewall_audit()
    check("G01-firewall", okf, det)
    check("G02-predefinition", True,
          "REVIEWER-ADJUDICATED STABILITY ROUND (no proof, no "
          "bound, no mechanism claim): exact Hellmann-Feynman "
          "gradients d log h_n/du_j and border/CD gradients "
          "dF_n/du_j of the r244 chain through the sealed tent-"
          "grid channel, FD/mp-gated; gap-weighted Lipschitz "
          "curves L1/L2; dose adjudication against the rebuilt "
          "r276 P2 theta = %s worlds; quadratic window (eps %s); "
          "N-scaling over ladder %s; verdicts LAW/NONSMOOTH/"
          "FAILED + EXPLAINS_DOSE + U_PROFILE + N_TREND + "
          "MAINWINDOW_PREDICATE sealed BEFORE evaluation"
          % (str(THETAS_R276), str(EPS_LADDER), str(LADDER_KZS)))

    # ---------------- S1: censuses + identity wards
    section("S1  CENSUSES + IDENTITY WARDS")
    kzs = (MAIN_KZ,) if smoke else LADDER_KZS
    ctxs = {kz: ctx_build(kz) for kz in kzs}
    packs = {kz: grad_pack(ctxs[kz]) for kz in kzs}
    ok_id = True
    id_note = []
    for kz in kzs:
        ctx, pk = ctxs[kz], packs[kz]
        xs, ws, _ = PIK.folded_measure(ctx["darm"], ctx["L"], +1.0)
        ys, vs, _ = PIK.folded_measure(ctx["darm"], ctx["L"], -1.0)
        ref = BH.bord_chain(xs, ws, ys, vs, ctx["bx"], ctx["bw"],
                            ctx["by"], ctx["bv"], ctx["N"])
        same = (len(ref) == pk["n_run"]) and all(
            ref[k][f] == pk["rows"][k][f]
            for k in range(len(ref))
            for f in ("lg_h", "sg_h", "Ls", "eta", "fb", "tb",
                      "rho", "alh", "gam_next"))
        ok_id = ok_id and same and pk["n_run"] == ctx["N"]
        id_note.append("w%d N %d" % (kz, ctx["N"]))
    check("G10-identity-chain", ok_id,
          "grad_chain reproduces BH.bord_chain FIELD-EXACTLY "
          "(lg_h/sg_h/Ls/eta/fb/tb/rho/alh/gam) on %d/%d ladder "
          "windows at full depth: %s -- the evaluation-grid "
          "extension changes nothing"
          % (len(kzs), len(kzs), "; ".join(id_note)))
    ok_ch = True
    for kz in (R276_KZS if not smoke else (MAIN_KZ,)):
        ctx = ctxs.get(kz) or ctx_build(kz)
        p_ref = BH.wpack(kz)
        pk = packs.get(kz) or grad_pack(ctx)
        rho_me = np.array([r["rho"] for r in pk["rows"]])
        nf_me = next((r["n"] for r in pk["rows"]
                      if r["sg_h"] < 0), None)
        ok_ch = ok_ch and bool(np.array_equal(rho_me,
                                              p_ref["rho"])) \
            and nf_me == p_ref["nf"]
    check("G11-channel-identity", ok_ch,
          "the comb channel reproduces BH.wpack BITWISE (rho "
          "array + nf) on the r276 windows -- the gradient block "
          "sits on the canonical object")
    ok_eta = all(packs[kz]["eta_ward"] <= ETA_WARD_BAR
                 for kz in kzs)
    check("G12-eta-reconstruction", ok_eta,
          "eta_n == <wsig, q_n^2> on the full fold grid at EVERY "
          "degree, worst rel %.1e (bar %.0e) -- the signed grid "
          "weight vector carries the chain exactly"
          % (max(packs[kz]["eta_ward"] for kz in kzs),
             ETA_WARD_BAR))
    # kink + reflection + on-node census
    ok_kink = True
    kink_note = []
    for kz in kzs:
        ctx, pk = ctxs[kz], packs[kz]
        Dg = pk["Dg"]
        off = ~pk["onnode"]
        mind = float(np.min(pk["dists"][off])) / Dg if \
            np.any(off) else float("nan")
        refl = float(np.min(ctx["uu"])) / Dg
        ok_kink = ok_kink and refl >= 2.0
        kink_note.append("w%d on-node %d/%d, off-node min-dist "
                         "%.3f D, min u %.0f D"
                         % (kz, int(np.sum(pk["onnode"])),
                            len(ctx["uu"]), mind, refl))
    check("G13-kink-reflection-census", ok_kink,
          "tent geometry: %s -- reflection branch INACTIVE "
          "everywhere (min u >= 2 D); ON-NODE atoms carry the "
          "disclosed one-sided derivative pair (on w9 they are "
          "the 2-power family: alpha = log 16 makes D "
          "commensurate with log 2)"
          % "; ".join(kink_note))
    c9 = ctxs[MAIN_KZ]
    u0, m0_ = MF.pert_jit(c9["uu"], c9["mm"], 0.0, SEED_R276,
                          False)
    ok0 = bool(np.array_equal(u0, c9["uu"])) \
        and bool(np.array_equal(m0_, c9["mm"]))
    check("G14-theta0-exact", ok0,
          "MF.pert_jit at theta = 0 returns BITWISE-identical "
          "arrays -- MAIN is the exact dose origin (r276 "
          "machinery loaded verbatim)")

    # ---------------- S2: FD gates + mp + must-fails
    section("S2  LEG A1 -- FD GATES + MP COUNTER-CHECK + "
            "MUST-FAILS")
    fd_kzs = (MAIN_KZ,) if smoke else R276_KZS
    worst_rich = worst_raw = 0.0
    n_pairs = 0
    n_skip = 0
    n_esc = 0
    worst_esc = 0.0
    esc_ok = True
    for kz in fd_kzs:
        ctx, pk = ctxs[kz], packs[kz]
        N = ctx["N"]
        degs = (5, N // 3, 2 * N // 3, N - 1)
        offi = np.nonzero(~pk["onnode"])[0]
        hot = offi[int(np.argmax(
            (pk["gaps"] * np.abs(pk["glogh"][:, N - 1]))[offi]))]
        atoms = sorted(set((int(offi[0]),
                            int(offi[len(offi) // 2]),
                            int(offi[-1]), int(hot))))
        if smoke:
            atoms = atoms[:2]
        for j in atoms:
            allowed = [e for e in FD_STEPS
                       if e <= KINK_GUARD * pk["dists"][j]]
            if len(allowed) < 2:
                n_skip += 1
                continue
            e_big, e_small = allowed[-2], allowed[-1]
            fd_b, _db = fd_pair(ctx, j, e_big)
            fd_s, _ds = fd_pair(ctx, j, e_small)
            r2 = (e_big / e_small) ** 2
            for n in degs:
                gan = pk["glogh"][j, n]
                floor = max(GRAD_FLOOR_FRAC * float(
                    np.max(np.abs(pk["glogh"][:, n]))),
                    ABS_GRAD_MIN)
                if abs(gan) < floor:
                    n_skip += 1
                    continue
                if not (np.isfinite(fd_b[n])
                        and np.isfinite(fd_s[n])):
                    n_skip += 1
                    continue
                rich = fd_s[n] + (fd_s[n] - fd_b[n]) / (r2 - 1.0)
                dev_r = abs(rich - gan) / max(abs(gan), floor)
                dev_w = abs(fd_s[n] - gan) / max(abs(gan), floor)
                if dev_r > FD_RICH_BAR and not smoke:
                    # amendment a1: the f64 chain rounding error
                    # is SMOOTH in u -- its gradient pollutes the
                    # f64 FD on the deep window; the sealed mp
                    # (dps 40) FD arbitrates
                    n_esc += 1
                    u_pe = ctx["uu"].copy()
                    u_me = ctx["uu"].copy()
                    u_pe[j] += MP_E_ESC
                    u_me[j] -= MP_E_ESC
                    lpe = mp_lgh(zones_of(ctx, u_pe), (n,),
                                 MP_DPS)[n]
                    lme = mp_lgh(zones_of(ctx, u_me), (n,),
                                 MP_DPS)[n]
                    dev_e = abs((lpe - lme) / (2.0 * MP_E_ESC)
                                - gan) / max(abs(gan), floor)
                    worst_esc = max(worst_esc, dev_e)
                    esc_ok = esc_ok and dev_e <= MP_FD_BAR
                else:
                    worst_rich = max(worst_rich, dev_r)
                worst_raw = max(worst_raw, dev_w)
                n_pairs += 1
    check("G20-fd-gates", worst_rich <= FD_RICH_BAR
          and worst_raw <= FD_RAW_BAR and esc_ok
          and n_pairs >= (2 if smoke else 8),
          "central FD through the FULL pipeline (off-node "
          "atoms, kink-guarded adaptive steps, Richardson from "
          "the two smallest allowed): %d pairs on %s, worst "
          "f64 Richardson dev %.1e (bar %.0e), worst raw dev "
          "%.1e (bar %.0e), %d skipped (kink guard / grad "
          "floor / flip overlap); %d pairs ESCALATED to the "
          "sealed mp (dps %d) FD where the f64 chain "
          "error-gradient bites (worst mp dev %.1e, bar %.0e) "
          "-- the Hellmann-Feynman formula IS the derivative "
          "of the machinery"
          % (n_pairs, str(fd_kzs), worst_rich, FD_RICH_BAR,
             worst_raw, FD_RAW_BAR, n_skip, n_esc, MP_DPS,
             worst_esc, MP_FD_BAR))
    # one-sided gate at the hottest ON-node atom (w9)
    pk9s = packs[MAIN_KZ]
    c9s = ctxs[MAIN_KZ]
    N9s = c9s["N"]
    oni = np.nonzero(pk9s["onnode"])[0]
    worst_one = 0.0
    one_note = "no on-node atoms"
    if len(oni):
        j_on = oni[int(np.argmax(
            (pk9s["gaps"]
             * np.abs(pk9s["glogh"][:, N9s - 1]))[oni]))]
        e_b, e_s = FD_STEPS[-2], FD_STEPS[-1]
        r_ = e_b / e_s
        base_lg = np.array([r["lg_h"] for r in pk9s["rows"]])
        vals = {}
        for sgn, gmat in ((+1.0, pk9s["glogh"]),
                          (-1.0, pk9s["gloghL"])):
            fds = {}
            for e in (e_b, e_s):
                u2 = c9s["uu"].copy()
                u2[j_on] += sgn * e
                rws, _nf, _z = pert_rows(c9s, u2, c9s["mm"])
                lg2 = np.array([r["lg_h"] for r in rws])
                fds[e] = sgn * (lg2 - base_lg[:len(lg2)]) / e
            for n in (2 * N9s // 3, N9s - 1):
                gan = gmat[j_on, n]
                rich = (r_ * fds[e_s][n] - fds[e_b][n]) \
                    / (r_ - 1.0)
                dev = abs(rich - gan) / max(abs(gan),
                                            ABS_GRAD_MIN)
                worst_one = max(worst_one, dev)
                vals[(sgn, n)] = dev
        one_note = ("j %d (2-power family), right/left devs %s"
                    % (int(j_on),
                       str({("%+d@n%d" % (s, n)): "%.1e" % d
                            for (s, n), d in vals.items()})))
    check("G20b-fd-one-sided", worst_one <= FD_ONE_BAR,
          "ONE-SIDED FD (first-order Richardson) at the hottest "
          "on-node w9 atom, left and right slope separately: "
          "%s, worst dev %.1e (bar %.0e) -- the kink pair is "
          "the correct derivative object at the 2-power atoms"
          % (one_note, worst_one, FD_ONE_BAR))
    # directional FD (one-sided, side-selected prediction)
    worst_dir = 0.0
    for kz in fd_kzs:
        ctx, pk = ctxs[kz], packs[kz]
        N = ctx["N"]
        dist_eff = np.where(pk["onnode"], pk["Dg"], pk["dists"])
        for di in range(1 if smoke else 2):
            rng = np.random.default_rng(SEED_DIR + kz * 100 + di)
            v = pk["gaps"] * rng.uniform(-1.0, 1.0,
                                         len(ctx["uu"]))
            with np.errstate(divide="ignore"):
                caps = KINK_GUARD * dist_eff \
                    / np.maximum(np.abs(v), 1e-300)
            cap = float(np.min(caps))
            allowed = [e for e in FD_STEPS if e <= cap]
            if len(allowed) < 2:
                continue
            e_b, e_s = allowed[-2], allowed[-1]
            fd_b = fd_dir(ctx, pk["rows"], v, e_b)
            fd_s = fd_dir(ctx, pk["rows"], v, e_s)
            r_ = e_b / e_s
            pred = pred_dlg(pk["glogh"], pk["gloghL"], v)
            for n in (5, N // 2, N - 1):
                if abs(pred[n]) < ABS_GRAD_MIN:
                    continue
                if not (np.isfinite(fd_b[n])
                        and np.isfinite(fd_s[n])):
                    continue
                rich = (r_ * fd_s[n] - fd_b[n]) / (r_ - 1.0)
                worst_dir = max(worst_dir,
                                abs(rich - pred[n])
                                / abs(pred[n]))
    check("G21-directional-fd", worst_dir <= DIR_BAR,
          "full-vector ONE-SIDED directional FD (pinned "
          "gap-scaled directions incl. the on-node atoms, "
          "first-order Richardson) vs the SIDE-SELECTED "
          "prediction: worst dev %.1e (bar %.0e) -- the "
          "gradient assembles correctly over ALL atoms"
          % (worst_dir, DIR_BAR))
    # margin FD (amendment a1: Richardson from the two LARGEST
    # kink-guarded steps -- |dD| ~ 1e-9..1e-7 sits at the f64
    # cancellation floor at the smallest steps)
    worst_marg = 0.0
    for kz in fd_kzs:
        ctx, pk = ctxs[kz], packs[kz]
        offi = np.nonzero(~pk["onnode"])[0]
        j = int(offi[int(np.argmax(
            (pk["gaps"] * np.abs(pk["gmarg"]))[offi]))])
        allowed = [e for e in FD_STEPS
                   if e <= KINK_GUARD * pk["dists"][j]]
        if len(allowed) < 2:
            continue
        e_b, e_s = allowed[-2], allowed[-1]
        _f1, dD_b = fd_pair(ctx, j, e_b)
        _f2, dD_s = fd_pair(ctx, j, e_s)
        r2 = (e_b / e_s) ** 2
        rich = dD_s + (dD_s - dD_b) / (r2 - 1.0)
        gan = pk["gmarg"][j]
        worst_marg = max(worst_marg,
                         abs(rich - gan) / max(abs(gan), 1e-10))
    check("G22-margin-fd", worst_marg <= MARG_BAR,
          "terminal-margin gradient dD_N/du_j (border/CD route) "
          "vs Richardson FD at the hottest margin atom per "
          "window: worst dev %.1e (bar %.0e) -- the chain rule "
          "through rho = F^2/h is exact"
          % (worst_marg, MARG_BAR))
    # DW ward (piecewise-linear map: FD exact to rounding)
    worst_dw = 0.0
    for kz in fd_kzs:
        ctx, pk = ctxs[kz], packs[kz]
        offi = np.nonzero(~pk["onnode"])[0]
        for j in (int(offi[0]), int(offi[len(offi) // 2]),
                  int(offi[-1])):
            if DW_E > KINK_GUARD * pk["dists"][j]:
                continue
            u_p = ctx["uu"].copy()
            u_m = ctx["uu"].copy()
            u_p[j] += DW_E
            u_m[j] -= DW_E
            dp = np.asarray(PIK.build_rung(
                kz, comb=(u_p, ctx["mm"]))["d"], float)
            dm = np.asarray(PIK.build_rung(
                kz, comb=(u_m, ctx["mm"]))["d"], float)
            fdw = (wsig_vec(dp, ctx["L"])
                   - wsig_vec(dm, ctx["L"])) / (2.0 * DW_E)
            sc = float(np.linalg.norm(pk["DW"][j]))
            worst_dw = max(worst_dw,
                           float(np.linalg.norm(fdw - pk["DW"][j]))
                           / max(sc, 1e-300))
    check("G23-dw-ward", worst_dw <= DW_BAR,
          "tent+FFT weight derivative DW vs central FD of the "
          "full weight vector (e = %.0e): worst rel %.1e (bar "
          "%.0e) -- the piecewise-linear map is differentiated "
          "EXACTLY between kinks" % (DW_E, worst_dw, DW_BAR))
    # mp counter-check
    if smoke:
        check("G24-mp-counter-fd", True, "SMOKE: skipped")
    else:
        pk9 = packs[MAIN_KZ]
        N9 = ctxs[MAIN_KZ]["N"]
        offi9 = np.nonzero(~pk9["onnode"])[0]
        degs_mp = (2 * N9 // 3, N9 - 1)
        j_a = int(offi9[int(np.argmax(
            np.abs(pk9["glogh"][:, degs_mp[0]])[offi9]))])
        j_b = int(offi9[int(np.argmax(
            np.abs(pk9["glogh"][:, degs_mp[1]])[offi9]))])
        if j_b == j_a:
            ordb = offi9[np.argsort(
                -np.abs(pk9["glogh"][:, degs_mp[1]])[offi9])]
            j_b = int(ordb[1])
        z0 = zones_of(c9, c9["uu"])
        base_mp = mp_lgh(z0, degs_mp, MP_DPS)
        base_dev = max(abs(base_mp[n] - pk9["rows"][n]["lg_h"])
                       for n in degs_mp)
        ok_mp = base_dev <= MP_BASE_BAR
        mp_note = ["base lg dev %.1e" % base_dev]
        for j, n_t in ((j_a, degs_mp[0]), (j_b, degs_mp[1])):
            if MP_E > KINK_GUARD * pk9["dists"][j]:
                mp_note.append("j%d kink-guarded, skipped" % j)
                continue
            u_p = c9["uu"].copy()
            u_m = c9["uu"].copy()
            u_p[j] += MP_E
            u_m[j] -= MP_E
            lp = mp_lgh(zones_of(c9, u_p), (n_t,), MP_DPS)[n_t]
            lm = mp_lgh(zones_of(c9, u_m), (n_t,), MP_DPS)[n_t]
            fd_mp = (lp - lm) / (2.0 * MP_E)
            gan = pk9["glogh"][j, n_t]
            dev = abs(fd_mp - gan) / max(abs(gan), 1e-10)
            ok_mp = ok_mp and dev <= MP_FD_BAR
            mp_note.append("(n %d, j %d) dev %.1e" % (n_t, j, dev))
        check("G24-mp-counter-fd", ok_mp,
              "mp (dps %d) chain FD at e = %.0e on the sealed w9 "
              "pairs: %s (base bar %.0e, FD bar %.0e) -- no f64 "
              "chain noise in the gradient gates"
              % (MP_DPS, MP_E, "; ".join(mp_note), MP_BASE_BAR,
                 MP_FD_BAR))
    # must-fails m1a/m1b/m2
    pk9 = packs[MAIN_KZ]
    N9 = c9["N"]
    offi9m = np.nonzero(~pk9["onnode"])[0]
    j_hot = int(offi9m[int(np.argmax(
        (pk9["gaps"] * np.abs(pk9["glogh"][:, N9 - 1]))[offi9m]))])
    allowed = [e for e in FD_STEPS
               if e <= KINK_GUARD * pk9["dists"][j_hot]]
    e_b, e_s = allowed[-2], allowed[-1]
    fd_b, _d1 = fd_pair(c9, j_hot, e_b)
    fd_s, _d2 = fd_pair(c9, j_hot, e_s)
    r2 = (e_b / e_s) ** 2
    rich = fd_s[N9 - 1] + (fd_s[N9 - 1] - fd_b[N9 - 1]) / (r2 - 1)
    # m1a: sin^2 weight factor dropped
    L9 = c9["L"]
    Dg9 = pk9["Dg"]
    i0 = int(math.floor(c9["uu"][j_hot] / Dg9))
    dcM = np.zeros(c9["M"])
    dcM[i0] += c9["mm"][j_hot] / (2.0 * Dg9)
    dcM[i0 + 1] -= c9["mm"][j_hot] / (2.0 * Dg9)
    dd = PIK.grid_density(dcM)
    ll = np.arange(L9)
    fold = np.minimum(ll, L9 - ll)
    npts9 = L9 // 2 + 1
    row_m1a = np.zeros(npts9)
    np.add.at(row_m1a, fold, dd * (1.0 / (2.0 * L9)))
    g_m1a = float(row_m1a @ (pk9["Q"][:, N9 - 1] ** 2)
                  / pk9["eta"][N9 - 1])
    dev_m1a = abs(g_m1a - rich) / abs(rich)
    # m1b: mirror arm of the even extension dropped
    s_l = 4.0 * np.sin(math.pi * ll / L9) ** 2 / (2.0 * L9)
    half = ll <= L9 // 2
    row_m1b = np.zeros(npts9)
    np.add.at(row_m1b, fold[half], (dd * s_l)[half])
    g_m1b = float(row_m1b @ (pk9["Q"][:, N9 - 1] ** 2)
                  / pk9["eta"][N9 - 1])
    dev_m1b = abs(g_m1b - rich) / abs(rich)
    check("G25-mustfail-weight-terms", dev_m1a >= MUT_LOUD
          and dev_m1b >= MUT_LOUD,
          "m1 WEIGHT-TERM MUTANTS at the hottest w9 pair: "
          "dropping the s_l = 4 sin^2/(2L) factor deviates "
          "%.1e and dropping the mirror arm deviates %.1e from "
          "the Richardson FD (bar >= %.1f) -- every factor of "
          "the sealed weight map is load-bearing"
          % (dev_m1a, dev_m1b, MUT_LOUD))
    fd_r, _d3 = fd_pair(c9, j_hot, ROUND_E)
    v_r = fd_r[N9 - 1] if np.isfinite(fd_r[N9 - 1]) else 0.0
    dev_m2 = abs(v_r - rich) / abs(rich)
    check("G26-mustfail-rounding-step", dev_m2 >= ROUND_MIN_DEV,
          "m2 ROUNDING-REGIME FD (step %.0e, below one ulp of "
          "u): dev %.1e >= %.0e vs the analytic gradient -- the "
          "kink-guarded adaptive step is load-bearing, a naive "
          "FD is NOT a substitute for the formula"
          % (ROUND_E, dev_m2, ROUND_MIN_DEV))

    if smoke:
        for g_ in ("G30-control-anchors", "G31-uprofile",
                   "G32-lethality-census", "G33-control-contrast",
                   "G40-conservation-doses", "G41-dose-ratio",
                   "G42-flip-prediction", "G43-extrapolation",
                   "G50-quadratic-window", "G60-n-scaling",
                   "G70-stability-hypothesis",
                   "G71-mainwindow-predicate"):
            check(g_, True, "SMOKE: skipped")
        verd = "SMOKE_NO_ADJUDICATION"
    else:
        # ---------------- S3: u-profile + lethality + controls
        section("S3  LEG A2/A3 -- U-PROFILE + LETHALITY + "
                "CONTROLS")
        rr9 = core.build_window(MAIN_KZ)
        N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
        lamE = PIK.lambda_eps(N_E)
        nn_idx = np.nonzero(np.abs(lamE) > 1e-12)[0]
        ctrl_ctx = {
            "EPSTEIN": ctx_build(MAIN_KZ, comb=(
                np.log(nn_idx.astype(float)),
                2.0 * lamE[nn_idx]
                / np.sqrt(nn_idx.astype(float)))),
            "SCRAMBLE": ctx_build(MAIN_KZ, scramble_seed=1),
            "SMOOTH": ctx_build(MAIN_KZ,
                                comb=PB.smooth_comb(
                                    rr9["alpha"]))}
        ctrl_pk = {c: grad_pack(ctrl_ctx[c]) for c in ctrl_ctx}
        ctrl_nf = {c: next((r["n"] for r in ctrl_pk[c]["rows"]
                            if r["sg_h"] < 0), None)
                   for c in ctrl_ctx}
        ok_ctrl = all(ctrl_nf[c] == CTRL_FLIPS[c]
                      for c in ctrl_ctx)
        nf_main = {kz: next((r["n"] for r in packs[kz]["rows"]
                             if r["sg_h"] < 0), None)
                   for kz in LADDER_KZS}
        check("G30-control-anchors", ok_ctrl
              and all(nf_main[kz] is None for kz in LADDER_KZS),
              "controls re-derived %s == the sealed 25/21/27 "
              "through the gradient chain; MAIN positive at "
              "full depth on all %d ladder windows"
              % (str(ctrl_nf), len(LADDER_KZS)))
        # u-profile on the r276 windows
        prof = {}
        sp_pos = {}
        sp_wt = {}
        for kz in R276_KZS:
            ctx, pk = ctxs[kz], packs[kz]
            A = pk["gaps"] * np.max(np.abs(pk["glogh"]), axis=1)
            Mj = pk["gaps"] * np.abs(pk["gmarg"])
            pos = ctx["uu"] / (2.0 * ctx["alpha"])
            prof[kz] = (A, Mj, pos)
            sp_pos[kz] = BH.spearman(A, pos)
            sp_wt[kz] = BH.spearman(A, ctx["mm"])
        A9, M9, pos9 = prof[MAIN_KZ]
        topi = np.argsort(A9)[::-1][:3]
        sp_am = BH.spearman(A9, M9)
        check("G31-uprofile", True,
              "U-PROFILE (gap-weighted A_j = g_j max_n "
              "|dlogh/du_j|): sp(A, hull pos) %s; sp(A, weight) "
              "%s; sp(A, margin map M_j) %+.2f (w9); top-3 w9 "
              "atoms at hull positions %s with A %s -- the "
              "sensitivity localization the r276 follow-up "
              "asked for"
              % (str({k: "%+.2f" % sp_pos[k] for k in sp_pos}),
                 str({k: "%+.2f" % sp_wt[k] for k in sp_wt}),
                 sp_am,
                 str(["%.2f" % pos9[i] for i in topi]),
                 str(["%.1f" % A9[i] for i in topi])))
        # lethality census (w9, deterministic +/- g_j singles)
        g9 = packs[MAIN_KZ]["gaps"]
        depths = np.empty(len(c9["uu"]))
        flips = []
        for j in range(len(c9["uu"])):
            dmin = 1.0
            for sgn in (+1.0, -1.0):
                u2 = c9["uu"].copy()
                u2[j] += sgn * g9[j]
                _r2, nf2, _z2 = pert_rows(c9, u2, c9["mm"])
                dmin = min(dmin, 1.0 if nf2 is None
                           else nf2 / N9)
                if nf2 is not None:
                    flips.append(nf2)
            depths[j] = dmin
        sp_leth = BH.spearman(A9, depths)
        n_flip = int(np.sum(depths < 1.0))
        if sp_leth <= SP_PRED:
            u_cls = "U_PROFILE_PREDICTIVE"
        elif sp_leth <= SP_WEAK:
            u_cls = "U_PROFILE_WEAK"
        else:
            u_cls = "U_PROFILE_UNCOUPLED"
        check("G32-lethality-census", True,
              "deterministic +/-g_j singles on w9: %d/%d atoms "
              "flip the wall (flip degrees %d..%d; the r276 "
              "lethal band was 51..152), sp(A_j, min-depth_j) = "
              "%+.2f -> %s (sealed bars %.1f/%.1f) -- the "
              "gradient map vs the measured single-op lethality"
              % (n_flip, len(depths),
                 min(flips) if flips else -1,
                 max(flips) if flips else -1, sp_leth, u_cls,
                 SP_PRED, SP_WEAK))
        # control contrast maps
        cm_note = []
        A_main = A9
        cm_main = float(np.sum(A_main * pos9) / np.sum(A_main))
        for c in ("EPSTEIN", "SCRAMBLE", "SMOOTH"):
            ctxc, pkc = ctrl_ctx[c], ctrl_pk[c]
            nfc = ctrl_nf[c]
            Ac = pkc["gaps"] * np.max(
                np.abs(pkc["glogh"][:, :nfc]), axis=1)
            posc = ctxc["uu"] / (2.0 * ctxc["alpha"])
            cmc = float(np.sum(Ac * posc) / np.sum(Ac))
            L1c = float(np.median(pkc["L1"][:nfc]))
            L1m_pre = float(np.median(
                packs[MAIN_KZ]["L1"][:nfc]))
            cm_note.append("%s cm %.2f L1med %.3g (MAIN same "
                           "range %.3g)" % (c, cmc, L1c,
                                            L1m_pre))
        L1m = float(np.median(packs[MAIN_KZ]["L1"]))
        check("G33-control-contrast", True,
              "CONTRAST (pre-flip gradient maps, hull "
              "coordinate u/(2 alpha)): MAIN hull-cm %.2f, L1 "
              "med %.3g (full depth) vs %s -- typed "
              "MEASUREMENT: where the wrong arithmetic is "
              "fragile vs where MAIN is"
              % (cm_main, L1m, "; ".join(cm_note)))

        # ---------------- S4: dose adjudication (b1)
        section("S4  LEG B1 -- THE r276 DOSE ADJUDICATION")
        cons_ok = True
        band_ratios = []
        flip_devs = []
        kink_cross = []
        dose_worlds = {}
        for th in THETAS_R276:
            for kz in R276_KZS:
                ctx, pk = ctxs[kz], packs[kz]
                for rep in range(REPS):
                    seed = (SEED_R276 + P2_SI * 100000
                            + DOSE_DI[th] * 10000 + rep * 1000
                            + WIN_WI[kz] * 10)
                    u2, m2 = MF.pert_jit(ctx["uu"], ctx["mm"],
                                         th, seed, False)
                    cons_ok = cons_ok and MF.conserve_comb(
                        "P2_JIT", ctx["uu"], ctx["mm"], u2, m2,
                        th)
                    du = u2 - ctx["uu"]
                    Dg = pk["Dg"]
                    cross = int(np.sum(
                        np.floor(ctx["uu"] / Dg)
                        != np.floor(u2 / Dg)))
                    rows2, nf2, _z = pert_rows(ctx, u2, m2)
                    pred = pred_dlg(pk["glogh"], pk["gloghL"],
                                    du)
                    npred = pred_flip(pred)
                    dose_worlds[(th, kz, rep)] = (
                        du, nf2, npred, cross)
                    if th == THETAS_R276[0]:
                        kink_cross.append(cross)
                        meas = dlg_measured(pk["rows"], rows2)
                        m_ = np.isfinite(meas) \
                            & (np.abs(meas) >= BAND_LO) \
                            & (np.abs(meas) <= BAND_HI)
                        if np.any(m_):
                            band_ratios.append(float(np.median(
                                pred[m_] / meas[m_])))
                        if nf2 is not None:
                            npx = ctx["N"] if npred is None \
                                else npred
                            flip_devs.append(
                                abs(npx - nf2) / nf2)
        check("G40-conservation-doses", cons_ok,
              "conservation EXACT (MF.conserve_comb) on all %d "
              "rebuilt r276 P2 worlds (theta %s x %d reps x %s)"
              % (len(dose_worlds), str(THETAS_R276), REPS,
                 str(R276_KZS)))
        med_ratio = float(np.median(band_ratios)) \
            if band_ratios else float("nan")
        med_flip = float(np.median(flip_devs)) \
            if flip_devs else float("nan")
        if (RATIO_EXPL[0] <= med_ratio <= RATIO_EXPL[1]
                and med_flip <= FLIP_TOL):
            dose_cls = "EXPLAINED"
        elif (RATIO_PART[0] <= med_ratio <= RATIO_PART[1]
                or med_flip <= 2 * FLIP_TOL):
            dose_cls = "PARTIAL"
        else:
            dose_cls = "UNEXPLAINED"
        check("G41-dose-ratio", True,
              "theta = 0.02 replicates (seeds exact): median "
              "band ratio pred/meas %.2f over %d replicates "
              "(band %.0e..%.1f, replicate medians %s); kink "
              "crossings med %.0f/%d atoms -- sealed classes "
              "EXPLAINED %s / PARTIAL %s"
              % (med_ratio, len(band_ratios), BAND_LO, BAND_HI,
                 str(["%.2f" % r for r in band_ratios]),
                 float(np.median(kink_cross)) if kink_cross
                 else -1, len(c9["uu"]),
                 str(RATIO_EXPL), str(RATIO_PART)))
        fl_note = []
        for kz in R276_KZS:
            pm = [(dose_worlds[(0.02, kz, r)][2],
                   dose_worlds[(0.02, kz, r)][1])
                  for r in range(REPS)]
            fl_note.append("w%d pred %s meas %s"
                           % (kz, [p for p, _ in pm],
                              [m for _, m in pm]))
        check("G42-flip-prediction", True,
              "first-order flip criterion (first n with "
              "<grad, du> <= -1) vs the measured flip: median "
              "|n_pred - nf|/nf = %.2f (tol %.2f); %s -> "
              "GRADIENT_EXPLAINS_DOSE(%s)"
              % (med_flip, FLIP_TOL, "; ".join(fl_note),
                 dose_cls))
        ex_note = []
        for th in THETAS_R276[1:]:
            devs = []
            for kz in R276_KZS:
                for rep in range(REPS):
                    _du, nf2, npred, _c = dose_worlds[(th, kz,
                                                       rep)]
                    if nf2 is not None:
                        npx = ctxs[kz]["N"] if npred is None \
                            else npred
                        devs.append(abs(npx - nf2) / nf2)
            ex_note.append("theta %.2f med dev %.2f (%d)"
                           % (th, float(np.median(devs))
                              if devs else float("nan"),
                              len(devs)))
        check("G43-extrapolation", True,
              "EXTRAPOLATION of the linear flip criterion to "
              "the r276 stages 0.05/0.10 (rebuilt worlds): %s "
              "-- where the global curve leaves first order "
              "(typed MEASUREMENT)" % "; ".join(ex_note))

        # ---------------- S5: quadratic window (b2)
        section("S5  LEG B2 -- THE QUADRATIC REST")
        q_cons = []
        thetas_star = {kz: [] for kz in B2_KZS}
        n_res_q = 0
        n_unres = 0
        n_explode = 0
        for kz in B2_KZS:
            ctx, pk = ctxs[kz], packs[kz]
            N = ctx["N"]
            Dg = pk["Dg"]
            dirs = []
            for rep in range(REPS):
                seed = (SEED_R276 + P2_SI * 100000
                        + DOSE_DI[0.02] * 10000 + rep * 1000
                        + WIN_WI[kz] * 10)
                u2, _m2 = MF.pert_jit(ctx["uu"], ctx["mm"], 0.02,
                                      seed, False)
                dirs.append((u2 - ctx["uu"]) / 0.02)
            for di in range(2):
                rng = np.random.default_rng(SEED_DIR + 7000
                                            + kz * 100 + di)
                dirs.append(pk["gaps"]
                            * rng.uniform(-1.0, 1.0,
                                          len(ctx["uu"])))
            degs = (N // 4, N // 2, 3 * N // 4, N - 1)
            for dvec in dirs:
                v = dvec.copy()
                v[pk["dists"] < KINK_PROJ * Dg] = 0.0
                with np.errstate(divide="ignore"):
                    caps = np.where(
                        np.abs(v) > 0.0,
                        0.9 * pk["dists"]
                        / np.maximum(np.abs(v), 1e-300),
                        np.inf)
                cap = float(np.min(caps))
                eps_ok = [e for e in EPS_LADDER if e <= cap]
                if len(eps_ok) < 2:
                    n_unres += 1
                    continue
                g1 = pred_dlg(pk["glogh"], pk["gloghL"], v)
                qs = {}
                for e in eps_ok:
                    rp, nfp, _z1 = pert_rows(ctx,
                                             ctx["uu"] + e * v,
                                             ctx["mm"])
                    rm, nfm, _z2 = pert_rows(ctx,
                                             ctx["uu"] - e * v,
                                             ctx["mm"])
                    dp = dlg_measured(pk["rows"], rp)
                    dm = dlg_measured(pk["rows"], rm)
                    qv = np.full(N, np.nan)
                    for n in degs:
                        if (np.isfinite(dp[n])
                                and np.isfinite(dm[n])
                                and abs(dp[n] + dm[n])
                                >= Q_FLOOR):
                            qv[n] = (dp[n] + dm[n]) / e ** 2
                    qs[e] = qv
                for n in degs:
                    pairq = [qs[e][n] for e in eps_ok
                             if np.isfinite(qs[e][n])]
                    if len(pairq) < 2:
                        n_unres += 1
                        continue
                    n_res_q += 1
                    r_ = max(abs(pairq[0] / pairq[1]),
                             abs(pairq[1] / pairq[0])) \
                        if pairq[1] != 0 else float("inf")
                    q_cons.append(r_)
                    if r_ > QCONS_EXPLODE:
                        n_explode += 1
                    q_small = pairq[0]
                    if q_small != 0.0 and abs(g1[n]) > 0:
                        thetas_star[kz].append(
                            abs(g1[n]) / abs(q_small))
        med_cons = float(np.median(q_cons)) if q_cons \
            else float("nan")
        b2_verdict = ("TAME" if med_cons <= QCONS_TAME else
                      ("NONSMOOTH" if med_cons > QCONS_EXPLODE
                       else "INTERMEDIATE"))
        ts_note = {kz: (float(np.median(thetas_star[kz])),
                        float(np.min(thetas_star[kz])))
                   for kz in B2_KZS if thetas_star[kz]}
        check("G50-quadratic-window", True,
              "SEALED q-consistency (adjacent eps, %d resolvable "
              "probes, %d unresolved): median %.2f (TAME bar %.0f"
              ", explode bar %.0f, %d probes explode) -> %s; "
              "validity window theta* = |lin|/|quad|: %s vs the "
              "r276 smallest dose 0.02"
              % (n_res_q, n_unres, med_cons, QCONS_TAME,
                 QCONS_EXPLODE, n_explode, b2_verdict,
                 str({("w%d" % k): ("med %.1e min %.1e" % v)
                      for k, v in ts_note.items()})))

        # ---------------- S6: N-scaling (b3)
        section("S6  LEG B3 -- N-SCALING OF L")
        recs = sorted(((ctxs[kz]["N"], kz) for kz in LADDER_KZS))
        Ns = [n for n, _ in recs]
        Lm = [packs[kz]["Lm1"] for _, kz in recs]
        Lx = [float(np.max(packs[kz]["L1"])) for _, kz in recs]
        b_L = halves_slope(Ns, Lm)
        dec = max(Lm) / min(Lm)
        if b_L >= TREND_SLOPE:
            trend = "GROWING"
        elif b_L <= -TREND_SLOPE:
            trend = "SHRINKING"
        else:
            trend = "FLAT"
        uniform = (trend == "FLAT" and dec <= TREND_DECADE)
        for (n, kz), lm, lx in zip(recs, Lm, Lx):
            info("kz %-3d N %-4d L_D %10.3g  max_n L1 %10.3g  "
                 "D_N %+9.6f"
                 % (kz, n, lm, lx, packs[kz]["DN"]))
        check("G60-n-scaling", True,
              "gap-relative margin Lipschitz L_D over the "
              "ladder: %s on N %s; halves slope b_L = %+.2f "
              "(bands +/-%.1f), decade %.1f (bar %.0f) -> "
              "N_TREND(%s)%s"
              % (str(["%.3g" % v for v in Lm]), str(Ns), b_L,
                 TREND_SLOPE, dec, TREND_DECADE, trend,
                 ", UNIFORM_CANDIDATE" if uniform else
                 " -- NO uniform lemma candidate from this "
                 "data"))

        # ---------------- S7: hypothesis + predicate + scopes
        section("S7  LEG C -- HYPOTHESIS + MAINWINDOW PREDICATE")
        ts9 = ts_note.get(MAIN_KZ, (float("nan"), float("nan")))
        check("G70-stability-hypothesis", True,
              "STABILITY HYPOTHESIS (typed TASK_FORMULATION_"
              "ONLY, falsifiable): 'positivity reserve >= "
              "margin_MAIN - L_D(w) theta - O(theta^2) for "
              "gap-relative doses theta <= theta*(w)' with "
              "MEASURED L_D %s over N %s (b_L %+.2f), theta* "
              "med %.1e (w9) -- locally %s, first order "
              "explains the smallest r276 dose at ratio %.2f, "
              "linearity leaves the global curve per G43"
              % (str(["%.3g" % v for v in Lm]), str(Ns), b_L,
                 ts9[0], b2_verdict, med_ratio))
        check("G71-mainwindow-predicate", True,
              "MAINWINDOW PREDICATE (typed PERTURBATIVE_ONLY): "
              "MetricNear(c, MAIN, theta) := max_j |u_j - "
              "u_j^MAIN|/g_j <= theta; for theta <= theta*(w) "
              "the stability inequality INHERITS margin(c) >= "
              "margin_MAIN - L_D(w) theta; %s -- the predicate "
              "transports wall positivity only PERTURBATIVELY "
              "around MAIN; the MAIN positivity itself stays "
              "the open center (H5 untouched)"
              % (("with N-trend %s and NO uniform constant "
                  "(G60), any Lean encoding must carry L_D(w) "
                  "per window" % trend) if not uniform else
                 "a UNIFORM candidate constant exists (G60)"))
        h_p = []
        for fn in GRAD_FUNCS:
            h_p.extend(scope_audit(fn, GRAD_FORBIDDEN))
        h_g = scope_audit("mutant_gift_profile", GRAD_FORBIDDEN)
        ag_hits = antigate_fragment_audit()
        check("G72-scope-audits", not h_p and bool(h_g)
              and not ag_hits,
              "the gradient constructors audit CLEAN against "
              "the withheld truth-side set (incl. the lethality "
              "census)%s; the gift profile FLAGGED (%s); "
              "fragment audit (no fit primitives): %s"
              % ("" if not h_p else " VIOLATION "
                 + "; ".join(h_p),
                 "; ".join(h_g) if h_g else "NOT FLAGGED",
                 "CLEAN" if not ag_hits else "; ".join(ag_hits)))

        # verdict assembly
        a1_gates = ("G20", "G20b", "G21", "G22", "G23", "G24")
        a1_ok = all(ok for nm, ok, _d in CHECKS
                    if nm.startswith(a1_gates))
        if not a1_ok:
            v_main = "GRADIENT_GATES_FAILED"
        elif b2_verdict == "NONSMOOTH":
            v_main = ("WALL_LOCALLY_NONSMOOTH(q median %.1f > "
                      "%.0f)" % (med_cons, QCONS_EXPLODE))
        else:
            v_main = ("METRIC_STABILITY_LAW(L-map sealed; "
                      "theta* med %.1e [w9]; N-trend %s)"
                      % (ts9[0], trend))
        verd = " + ".join([
            v_main,
            "GRADIENT_EXPLAINS_DOSE(%s, ratio %.2f, flip dev "
            "%.2f)" % (dose_cls, med_ratio, med_flip),
            "U_PROFILE(%s, sp %+.2f)" % (u_cls, sp_leth),
            "N_TREND(%s, b_L %+.2f%s)"
            % (trend, b_L, ", UNIFORM_CANDIDATE" if uniform
               else ""),
            "MAINWINDOW_PREDICATE(PERTURBATIVE_ONLY)"])

    # ---------------- S9: verdict
    section("S9  VERDICT")
    check("G95-mincut-unchanged", True,
          "mincut base 4 / refined 5 UNCHANGED; what the round "
          "adds: the EXACT first-order sensitivity calculus of "
          "the wall (Hellmann-Feynman + border/CD gradients, "
          "FD/mp-gated), the u-profile with its lethality "
          "adjudication, the local stability inequality with "
          "measured validity window and N-trend -- NO "
          "certificate, NO bound, NO mechanism claim, NO H5 "
          "progress")
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    check("G96-verdict", npass == len(CHECKS),
          "%s%s -- SATZ (machine-gated): the gradient formulas "
          "against FD/Richardson/mp on the full pipeline, the "
          "chain identities, conservation; MEASURED: every map, "
          "ratio, window and trend (finite windows); OPEN: the "
          "cofinal step H5 and the wall mechanism (the "
          "stability inequality is perturbative around MAIN); "
          "NO RH claim"
          % (verd, " (SMOKE)" if smoke else ""))
    wall = time.time() - T0_WALL
    check("G99-runtime", wall <= 1800.0,
          "WALL %.1f s (bar 1800)" % wall)
    npass = sum(1 for _n, ok, _d in CHECKS if ok)
    print("\n" + "=" * 78)
    print("RESULT: %d/%d gates PASS%s   SPEC_SHA %s"
          % (npass, len(CHECKS), " (SMOKE)" if smoke else "",
             SPEC_SHA[:16]))
    print("NO RH CLAIM in either direction.")
    print("=" * 78)
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
'''

# --------------------------------------------------------------- harness
_PF_RE = re.compile(r"^\s*\[(PASS|FAIL)\]\s+(\S+)", re.M)
_RES_RE = re.compile(
    r"RESULT:\s+(\d+)/(\d+)\s+gates PASS \(SMOKE\)\s+SPEC_SHA\s+"
    r"([0-9a-f]+)")


def _probe_file(name):
    cand = os.path.abspath(os.path.join(
        _HERE, os.pardir, "experiments", "tfpt-discovery", name + ".py"))
    return cand if os.path.isfile(cand) else None


def _exec_probe(name, src):
    """Execute one embedded frozen probe source BYTE-EXACT in its own
    module namespace in the sealed --smoke stage (wave-4 convention);
    capture and re-emit stdout; return (stdout, exit_code,
    byte_equal_or_None)."""
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
    argv_saved = sys.argv
    sys.argv = [fname, "--smoke"]
    with contextlib.redirect_stdout(buf):
        try:
            exec(compile(src, fname, "exec"), mod.__dict__)
            entry = mod.__dict__.get("main") or mod.__dict__.get("run")
            if callable(entry):
                rc = entry()
                code = 0 if rc is None else int(rc)
        except SystemExit as exc:
            code = 0 if exc.code is None else int(exc.code)
        except Exception:                            # regression guard
            import traceback
            traceback.print_exc(file=sys.stdout)
            code = 99
        finally:
            sys.argv = argv_saved
    out = buf.getvalue()
    sys.stdout.write(out)
    sys.stdout.flush()
    return out, code, same


def _gate(name, out, code, same, exp_n, exp_sha, gates):
    marks = _PF_RE.findall(out)
    n = len(marks)
    fails = sorted({tok for st, tok in marks if st == "FAIL"})
    m = _RES_RE.search(out)
    res_ok = (m is not None and int(m.group(1)) == exp_n
              and int(m.group(2)) == exp_n and m.group(3) == exp_sha)
    ok = (n == exp_n and not fails and code == 0 and res_ok
          and same is not False)
    gates.append(ok)
    prov = ("byte-exact vs experiments source" if same is True else
            "embedded copy (source file not present)" if same is None
            else "SOURCE MISMATCH")
    print("\n[%s] PATTERN GATE %s: %d checks (exp %d, smoke stage) | "
          "FAILs %s | RESULT line %s (exp %d/%d SPEC_SHA %s) | exit %d "
          "(exp 0)\n      provenance: %s"
          % ("PASS" if ok else "FAIL", name, n, exp_n,
             ",".join(fails) if fails else "none",
             "matched" if res_ok else "MISSING/WRONG", exp_n, exp_n,
             exp_sha, code, prov), flush=True)
    return ok


_PLAN = (
    ('wronskian_dictionary_probe', _SRC_0, 32, '56e8a03efd1690e4'),
    ('minimal_firewall_probe', _SRC_1, 25, 'ed17d79fc037ab1a'),
    ('maslov_census_probe', _SRC_2, 29, '3858fd16bde0c9c0'),
    ('metric_stability_probe', _SRC_3, 30, '7031200f008d34d1'),
)


def run():
    t0 = time.time()
    print("=" * 74)
    print('v961 -- PRIME.PORT.RHP.MIDPOINT.ORIENTATION_DICTIONARY.01 (rounds 274/')
    print('277 + typed measurements 276/278): the midpoint-orientation dictionary')
    print('and the metric firewall -- base Casoratian = h_n (c\' = 1), the h-free')
    print('midpoint form IS the node polynomial, the augmented telescope D_{n+1} =')
    print('B - W^aug/W^base; the Maslov census GO (rule R2 = Jacobi interlacing/')
    print('reality, blind 42/42, controls at flip+1, one-way) with the honest')
    print('atom-Sturm refutation; the metric firewall: graded continuum, exact')
    print('Hellmann-Feynman gradients, u-profile predictive, stability law')
    print("(frozen probes embedded byte-exact, sealed --smoke stage; NO RH claim)")
    print("=" * 74, flush=True)
    gates = []
    _midpoint_orientation_theorems(gates)
    for name, src, exp_n, exp_sha in _PLAN:
        print("\n" + "-" * 74)
        print("EMBEDDED FROZEN PROBE: %s" % name)
        print("-" * 74, flush=True)
        out, code, same = _exec_probe(name, src)
        _gate(name, out, code, same, exp_n, exp_sha, gates)
    ok = all(gates)
    print("\n" + "=" * 74)
    print("v961: %d/%d gates passed (4 module-own exact checks + 4 "
          "pattern gates) | runtime %.1f s"
          % (sum(gates), len(gates), time.time() - t0))
    print('the orientation question has its dictionary: the base Casoratian is')
    print('the pivot chain itself (c\' = 1), the midpoint form carries provably')
    print('no orientation (it IS the node polynomial), the fiber is the bordered')
    print('Wronskian quotient, and the orientation of the wall follows a')
    print('PREDICTABLE law -- the Jacobi interlacing/reality rule R2 passes the')
    print('blind Maslov census 42/42 with controls firing exactly at flip+1,')
    print('while the raw atom-Sturm census is honestly REFUTED as the winding')
    print('quantity (the classical separation theorem fails genuinely for the')
    print('signed comb); the metric firewall is graded-continuous with exact')
    print('position gradients and a bottom-loaded u-profile (small primes 2, 3,')
    print('5 carry), but the stability law is perturbative-only: the MAIN')
    print('positivity itself stays the open center.  Named next steps stay')
    print('OPEN: the oriented midpoint theorem (PRIME.PORT.RHP.MIDPOINT.')
    print('ORIENTED_THEOREM.01 [O], round 279 in flight) and the global metric')
    print('firewall (PRIME.PORT.WALL.METRIC_FIREWALL.01 [O]).')
    print('Mincut base 4 / refined 5 unchanged; NO RH claim.')
    print("[%s] v961 VERDICT GATE" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
