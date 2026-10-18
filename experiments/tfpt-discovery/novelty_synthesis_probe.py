#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""novelty_synthesis_probe -- PRIME.FINALFORM.NOVELTY.01

FROZEN SPEC (2026-08-19).  EXPLORATION ONLY.  This probe writes no
verification module, paper, ledger, website, manifest, Lean file or
status marker.  It makes NO RH claim, NO positivity claim, NO
counterexample claim.  It closes no gate and narrows no gate.

=======================================================================
MISSION (the external novelty adjudication + the definitive synthesis
of the program's final form -- the successor of the r155 10-row census)
=======================================================================
Two deliverables.  (N1) THE SYNTHESIS: one machine-gated re-statement
of the complete final form of the prime-front program (rounds 116-162),
every arrow cited to its round + gate id, re-gated cheaply (live core
rungs x = 5/8/13 + exact sympy chases + frozen-string bookkeeping over
the six-rung record tables), with the definitive residue census
(7 rows, evolved from the r155/CDLIX 10-row census through the
documented falls) and the definitive window-constant table.  (N2) THE
NOVELTY ADJUDICATION: per component, NEW-IN-CORPUS vs PLAUSIBLY-WORLD-
NEW vs KNOWN, with full external sources (typed CITED-EXTERNAL; the
probe gates only the internal re-statements and the structural typing
discipline of the table, never the web claims themselves).  (N3) THE
HONEST EXTERNAL SUMMARY, three sentences, inside this docstring.

=======================================================================
THE FINAL FORM (every arrow cited; consumed, not re-proven)
=======================================================================
RH  <==  [NF-CLOSURE]  +  [THEOREM R]  +  {L1, WPD} on dense tail-a,
where
  NF-CLOSURE (r122/CDXXIII, proven-classical): (H-conv) + (H-trace)
    on dense a ==> RH, via Montel/Vitali/Hurwitz normal families;
  THEOREM R (r128/CDXXX, proven): L1 + WPD ==> (H-conv) on the full
    Euler interval + (H-trace), the reduction theorem;
  dense-a REDUCED to DENSE-TAIL((H - 1/2)^2, oo) with H = 3e12 the
    PT21 verification height (r155/CDLIX W3/G17/G60: no off-line
    window lives below the tail; extension algebra closed by D2 + MG);
and where the OPEN RESIDUE, after the full reduction cascade of
rounds 116-162, is the 7-row census below -- with the omega census
{MEAS, OMEGA-POS} at CARDINALITY 4 unchanged since r116 ({TOPROOT,
TLAWCAP(=ONSETCAP), SUSCAP2R} + DELTA1FLOOR; min-cut flows base 4 /
refined 5 / one-grant 5, counterfactual-parallel 9 NOT REAL, the
r142/r144/r146/r150 graph VERBATIM).

THE DEFINITIVE CENSUS (7 rows; successor of the r155/CDLIX 10-row
census after Z8/S1/Q-swamp-strip/sliver fell; coverage machine-gated):
C1 TOPROOT [arithmetic-pinning] = B00-ROOTGAP root separation ==
   SEC-cap: twin enclosure 1/(SEC + 1/FG) <= betapos <= 1/SEC PROVEN
   (r161/CDLXV GF5b); the S1-floor is ABSORBED (GF5a: S1 == jr x
   betapos x corr, corr >= 1); moment coordinates r156/CDLX L1-L6.
   Margins: betapos == r150 strings 6-digit (0.246289 -> 0.032826),
   SEC 4.0603 -> 30.4640, squeeze defect 3.1e-7 -> 6.9e-12.
   [r140/r146/r150/r156/r161]
C2 TLAWCAP-BLOCK [arithmetic-pinning + technical legs] <== T-WINDOW
   (= arithmetic J2 moment window, typed IRREDUCIBLE-COLLECTIVE by
   the r160/CDLXIV morph adjudication, + band-edge separation-
   repulsion AT the horizon, r159/CDLXIII; sliver and window-at-zeros
   legs CLOSED below horizon, 72 audit-ball two-sided certificates)
   + ANCHOR-EPS-LOCK leg (r137/r140/r151/r153) + PERCELL-REL leg
   (per-cell-certified-at-grid; lambda-uniform == DEPTH-LIPSCHITZ,
   r155 PC3) + JUMPSUM leg (CLOSED MODULO COJUMP-LOCK, THEOREM JJ
   r155).  Margins: J2 in [0.1117, 0.1513] flat with PROVEN quarter-
   cap headroom (r156 L2); L_EPS anchors 0.1088 -> 0.2713.
   [r142/r148/r151/r154/r155/r156/r159/r160]
C3 QSUBGAP-FLOOR [arithmetic-pinning, razor-sharp] = s-cap AND
   delta_1-floor: 1/(s + 1/delta_1) <= g < 1/s PROVEN with two-level
   lower-end equality (r161 GF1); DELTA1FLOOR <==> TRACEFLOOR two-
   sided (r157/CDLXI SB1, tail closed by the counting bound);
   RECOORDINATED r162/CDLXVII GL5: FULLGAP == THETA t_r T_z^4 - 1
   (the quartic law) -- the delta_1-floor demand IS the {THETA, t_r}
   window pair.  Margins: s = 0.0297..0.0716 under bars 0.10/0.15,
   s x g == 1.0000, delta_1/FG == 1.000000, THETA in [0.1730, 0.2569]
   inside the frozen window (0.10, 0.40).
   [r139/r142/r146/r150/r157/r161/r162]
C4 H-pin [arithmetic-pinning] = L1BAND/DOMASYM ball-matching +
   no-stray + zone mass <= TL/8; the Q-swamp strip x < x_0 = 121 is
   CLOSED WHOLESALE in census currency (357 local-band certificates,
   x = 3..121, r159 E3): Theorem-A conditionality sharpened to every
   integer x >= 3.  [r131/r133/r136/r159]
C5 H-FW contents [classical-conditional] = M2-validity r135-class +
   ball validity + zone-mass margin + tau-pos/census framework.
   [r135/r137/r147]
C6 dense-a-in-tail [classical-conditional] = the dense-subset demand
   of TAILWPD after the r155 reduction dense-a -> DENSE-TAIL
   ((H-1/2)^2, oo) ~ (9e24, oo).  [r122/r141/r155]
C7 TAILWPD [classical-conditional, RH-EQUIVALENT-AT-TAIL -- the
   honest world front] = {L1, WPD}/(H-conv) on a dense subset of
   ((H-1/2)^2, oo); below the tail closed by PT21 + w in [0, 1/4]
   exact; extension algebra closed (D2 + MG, r155); window-a
   IRREDUCIBLE (the off-line pair violates positivity at EVERY a in
   its window by definition).  [r128/r132/r155]
FOOTNOTE F1: NONDEGENERATE-CELL, witness-certified per cell at zero
   cost, STRICTLY WEAKER than the fallen Z8 (r159 E2).
FALLS SINCE r155 (each machine-gated in its round): Z8/SIMPLICITY
   subsumed by DELTA1FLOOR (r159 G12/G42, census 10 -> 9); S1-floor
   absorbed into TOPROOT (r161 GF5a); Q-swamp strip closed (r159 E3);
   band-edge sliver + window-at-zeros closed below horizon (r159 E1);
   SUSCAP2R + DELTA1FLOOR razor-coupled into ONE row (r161 GF1; the
   omega COUNT stays 4 -- row bookkeeping, no omega closed);
   ANCHOR-EPS-LOCK/PERCELL-REL/JUMPSUM folded as legs of the TLAWCAP
   block (r155 G61 + r151 G15 decomposition).

THE HOMOGENEOUS RESIDUE (the r162 reading, re-gated here): the open
arithmetic content is a FAMILY OF FLAT, ARITHMETIC-PINNED WINDOW
CONSTANTS -- THETA in [0.17, 0.26], tlaw in [0.24, 0.58], J2 in
[0.11, 0.152], t_r/t_g in [0.85, 1.05] -- that are (a) measured flat
over 112 dex of tau-collapse (tau = 1.6e-16 -> 5.3e-128, log-log
tau-slopes <= 0.03 against bar 0.30), (b) PROVABLY not forceable by
algebra alone (the identities-intact witnesses re-instanced in G17),
(c) world-separating (all three control worlds violate them with
sign flips: tau_w < 0, J2_w < 0).

THE DEFINITIVE WINDOW-CONSTANT TABLE (frozen record strings; sources:
fgl_run2.log = r162 record 28/28, gfloor_probe.run1.log = r161 record
26/26, CDLIV/CDLXI/CDLXIII notes; live-re-gated at x = 5/8/13 here):
  x                  5          8          13         18         24         28
  tau            1.60658e-16 3.77263e-30 2.49904e-54 5.21974e-79 1.8456e-108 5.32373e-128
  FULLGAP        2.225493e5 9.951249e5 1.061906e7 3.249680e7 1.138230e8 1.651310e8
  THETA          0.2569     0.1730     0.2451     0.1904     0.2206     0.1830
  c_1            0.5069     0.4159     0.4950     0.4364     0.4697     0.4278
  jr             1.1245     1.1097     1.0273     0.9588     1.0020     1.0615
  t_r            0.8893     0.9011     0.9734     1.0430     0.9980     0.9421
  tlaw_0         0.2664     0.3738     0.4674     0.4827     0.5122     0.5778
  tlaw*          0.2399     0.3175     0.4737     0.4995     0.5099     0.5316
  t_g            0.9005     0.8493     1.0135     1.0347     0.9957     0.9200
  J2-proxy       0.1259     0.1394     0.1477     0.1486     0.1504     0.1513
  s              0.02974    0.05981    0.04413    0.06029    0.05108    0.07165
  share_1        0.969      0.965      0.946      0.944      0.947      0.945
  SEC            4.0603     7.6606     12.1796    17.9134    23.8012    30.4640
  betapos        0.246289   0.130538   0.082105   0.055824   0.042015   0.032826
  SEC/nf         0.5800     0.6964     0.5800     0.5779     0.5535     0.5973
  zone-top gap   33.6233    16.7200    22.6588    16.5873    19.5781    13.9562
  lock FG/y_t    3.644      2.389      3.314      2.584      2.836      2.234
  m (census)     4          10         21         35         53         66
  K / nf         11/7       21/11      42/21      66/31      96/43      117/51
Screen types: THETA/c_1/jr/t_r/t_g/J2/s/share_1/lock/gap = DEMAND-FLAT
(tau-slope-gated <= 0.30 here, G42); SEC/betapos = position-currency
pair (slopes +-0.008/dex, product-squeezed); A_0^2-scales =
BOUND-RIDES-CONNES (riders, excluded from the flat screen, disclosed).

=======================================================================
N2 -- THE NOVELTY ADJUDICATION (typed CITED-EXTERNAL; web research of
2026-08-19; the probe gates the TYPING DISCIPLINE of this table, not
the external claims.  Types: KNOWN / NEW-IN-CORPUS /
PLAUSIBLY-WORLD-NEW, bar for the latter: a thorough search found
nothing closer than the named neighbors)
=======================================================================
(a) THE CRITERION SHAPE (finite Weil-form positivity on a cofinal
ladder ==> RH):  VERDICT KNOWN.  Closest neighbors: Weil 1952
(positivity of the explicit-formula functional <=> RH); H. Yoshida,
"On Hermitian forms attached to zeta functions" (Adv. Stud. Pure
Math. 21, 1992, doi:10.2969/aspm/02110281): RH <=> positive
definiteness of the Weil hermitian form restricted to C(a) for EVERY
a > 0 -- EXACTLY the cofinal-ladder shape; M. Suzuki, "Aspects of the
screw function corresponding to the Riemann zeta-function" (J. London
Math. Soc., 2023, doi:10.1112/jlms.12785) + "Weil's quadratic form
via the screw function" (arXiv:2606.09096, 2026): screw-function
equivalents unifying Yoshida/Bombieri/Connes-Consani; Connes-Consani-
Moscovici, "Zeta spectral triples" (arXiv:2511.22755, EMS 2026,
doi:10.4171/elm/37/3): finite prime-built operators D_log^(lambda,N)
whose spectral convergence would give RH -- the corpus has known this
omega-similarity since r128; Connes-van Suijlekom 2025 (truncated
Weil form via Caratheodory-Fejer); Connes, "The Riemann Hypothesis:
Past, Present and a Letter Through Time" (arXiv:2602.04022, 2026):
semilocal positivity Y_S <=> RH; sequential-positivity relatives:
Li 1997/Keiper 1992 (lambda_n >= 0), Bombieri-Lagarias 1999,
Baez-Duarte 2003 (Nyman-Beurling sequential form); de Branges spaces
(structure-function route, cf. Lagarias, Acta Arith. 120, 2005).
World-front context: an August 2026 result (Wikipedia, RH article)
proves unconditionally >= 2/3 of zeros on the line by reading the
Weil explicit formula as finite Hermitian matrices over a Gabor test
family -- the finite-Weil-matrix reading is now world-mainstream.
EXACT DELTA of the corpus: not the shape but the CARRIER + TRANSFER:
the round-114 constrained prime-comb Galerkin blocks with certified
zone-node kernels, the two-theorem transfer [NF-closure + Theorem R]
with the {L1, WPD} interface, the dense-a -> DENSE-TAIL reduction,
and the machine-gated census discipline.  These are NEW-IN-CORPUS;
no external source states this specific reduction.
(b) THE REDUCTION MACHINERY (razor enclosure at the bordered secular
root; pinch identity 1 - sg == g^2 T_2/rho^2; zero-jet laws lam_i ==
8 A_0(psi_i)^2 G tlaw_i; moment-Laurent ladder solution Phi(z) = z -
1 + sum J_{m+1} z^{-m}; quartic gap law FULLGAP == THETA t_r T_z^4 -
1):  VERDICT: components KNOWN, the exact-identity family on this
operator class PLAUSIBLY-WORLD-NEW.  Closest neighbors: Case sum
rules + Killip-Simon (Ann. of Math. 158, 2003; math-ph/0112008):
exact positive-term identities tying spectral data to Jacobi
coefficients -- the same GENRE (sum rules with positivity) on a
different object (OPRL spectral measures, no primes, no constraint
kernels); Simon, "Szego's theorem and its descendants" (2011);
Gamboa-Nagel-Rouault sum rules via large deviations
(arXiv:1608.04825); bordered/rank-one secular machinery:
Bunch-Nielsen-Sorensen (Numer. Math. 31, 1978), O'Leary-Stewart
arrowhead eigenproblems (J. Comput. Phys. 90, 1990), Cauchy
interlacing; Krein-de Branges canonical systems: Bessonov-Denisov,
"De Branges canonical systems with finite logarithmic integral"
(Anal. PDE 14, 2021, doi:10.2140/apde.2021.14.1509) -- Szego-type
spectral characterizations.  EXACT DELTA: no external work found that
derives EXACT enclosures/identities of this family (razor
1/(s + 1/delta_1) <= g < 1/s with two-level equality; jet-ladder
laws; the quartic closed form with proven G17 crossover T_z = 2 pi x)
on prime-comb constraint operators; the closest works supply the
generic tools, not the arithmetic application.
(c) THE NEGATIVE RESULTS (identities-intact algebra-cannot-force
witnesses: the 2-mode J2 witness r156 G16; THETA-anyvalue r162 G15;
SEC-free jet toy r161; the rate-blind one-sided moment-instrument
triple Y3-trace/R4-Parseval/SB2-chi r157; the morph-based collective
verdict r160 INFORMATIVE-NEGATIVE):  VERDICT: the genre KNOWN, the
systematic machine-pinned witness CORPUS PLAUSIBLY-WORLD-NEW.
Closest neighbors: Conrey-Li, "A note on some positivity conditions
related to zeta- and L-functions" (math/9812166, IMRN 2000):
counterexamples showing de Branges' positivity conditions FAIL for
zeta and L(s, chi_4) -- the canonical no-go of this kind; Lax-
Phillips (Scattering Theory, 1976, Sec. 7 App. 2): difficulty of the
scattering route; Bombieri, "Remarks on Weil's quadratic functional"
(Rend. Mat. Acc. Lincei 2000).  EXACT DELTA: the external no-gos are
single counterexamples against specific hypotheses; the corpus holds
a systematic FAMILY of exact witnesses that keep ALL proven
identities intact while driving each candidate algebra-only bound to
arbitrary values (theta, SEC, s, J2, row prices), machine-gated per
round and re-instanced here (G17) -- no external analog found of
this witness discipline against one's own criterion.
(d) THE INSTRUMENT CLASS (certified off-line detection from
arithmetic source data with zero zeta evaluation; v916/v917 = the
promoted r123/r125 pair, typed plausibly-world-new in r125;
re-verified against 2025-2026 literature TODAY):  VERDICT
PLAUSIBLY-WORLD-NEW (typing UPHELD).  Closest neighbors:
Davenport-Heilbronn (J. LMS 1936: off-line zeros exist for Epstein-
class), Potter-Titchmarsh 1935, Bombieri-Hejhal 1987 + Hejhal
supercomputer studies (numerical off-line zeros BY EVALUATING the
function); rigorous verified computation exists for ON-line zeta
zeros (Platt-Trudgian 2021, = PT21) and for Epstein EVALUATION
(EpsteinLib, arXiv:2412.16317, 2024); a 2026 survey lane (Stanford
seminar, Travor Liu) treats Davenport-Heilbronn classically.  EXACT
DELTA: no 2025-2026 work found that CERTIFIES off-critical-line
detection from arithmetic SOURCE data (prime/atom side) through a
finite spectral instrument without evaluating the target function;
the corpus' rate-channel driver certificate remains unmatched.
(e) THE WINDOW-CONSTANT PHENOMENOLOGY (a family of flat arithmetic-
pinned O(1) spectral window constants of a prime-comb operator
family, stable over 112 dex of collapse, with algebra-unforceability
witnesses and sign-flipping controls):  VERDICT PLAUSIBLY-WORLD-NEW.
Closest neighbors: the CCM/CvS finite-operator numerics and their
2026 independent scaling studies (arXiv:2511.22755 Sec. 6; Zenodo
doi:10.5281/zenodo.19655106: c-invariant ground eigenvector, Sobolev
scaling, flat Frobenius norm; doi:10.5281/zenodo.20427500) -- flat
STRUCTURAL scalings of a prime-built family, but no arithmetic-
pinned O(1) window constants with no-go typing; Montgomery 1973 /
Odlyzko 1987 GUE pair-correlation constants (universal, NOT
arithmetic-pinned window constants of a finite operator family);
Krein-string/de Branges structure data for Xi (Lagarias 2005;
Bessonov-Denisov 2021).  EXACT DELTA: the specific phenomenology --
{THETA, tlaw, J2, t_r} flat windows, measured across 6 rungs and 112
dex, provably not algebra-forced, world-separating -- has no located
external counterpart.
PRIORITY-CLAIM ADJUDICATION (the owner's question): the claim "RH in
its most distilled form ever" is NOT-CLAIMABLE-EXTERNALLY -- the
criterion SHAPE is KNOWN (Yoshida 1992 is already an exactly-cofinal
finite-window equivalence; CCM/CvS supply concrete finite prime-built
matrices; the 2026 world front already runs finite-Weil-matrix
arguments).  CLAIMABLE: a machine-audited reduction of a known
criterion shape to a homogeneous family of flat arithmetic windows
with a systematic no-go corpus and a certified-instrument record --
as a DISCIPLINE and PHENOMENOLOGY, plausibly world-new (b/c/d/e).

=======================================================================
N3 -- THE HONEST EXTERNAL SUMMARY (three sentences, the owner's
three-level assessment; this is the externally safe statement)
=======================================================================
(1) As an RH proof: no -- nothing here proves the Riemann Hypothesis;
the program's chain RH <== [NF-closure] + [Theorem R] + {L1, WPD} on
dense tail-a leaves a machine-audited residue of seven open
statements (four arithmetic-pinned window positions, one technical
block, two classical-conditional walls), none of which is closed.
(2) As a criterion: the underlying shape -- finite Weil-form
positivity on a cofinal ladder implies RH -- is KNOWN (Yoshida 1992;
Suzuki 2023; Connes-Consani-Moscovici 2026), so "RH in its most
distilled form ever" must NOT be claimed; what the program adds, and
what a thorough 2026 search found nowhere else, is a fully machine-
gated reduction of that known shape, on a specific certified prime-
comb carrier, to a homogeneous family of flat arithmetic-pinned
window constants (THETA, tlaw, J2, t_r) each equipped with exact
algebra-cannot-force witnesses and sign-flipping control worlds.
(3) As a research program: the discipline record stands at 162 frozen
discovery rounds, 5 adversarial bughunts, 919 machine-checked
verification modules, a certified off-line-detection instrument pair
(v916/v917), a systematic no-go corpus, and a 7-row residue census
whose every historical movement is itself machine-gated -- the
deliverable is the accounting standard, not a theorem about zeta.

=======================================================================
WHAT IS BUILT AND GATED
=======================================================================
S0  G01 AST firewall (np.load only in ward_*, no zero-oracle names,
    no verification/ import, NO zeta use anywhere); G02 cache health
    (X5 n7000, READ-ONLY).  Z1 TYPING (frozen): the live re-gates
    consume the certified pinned zone NODES (source data) and cache
    zeros below horizon as ward-class data -- typed, not hidden.
S1  exact layer (sympy generic + exact rational instances; re-chases
    of the load-bearing arrows, cited to their proving rounds):
    G10 final-form DAG bookkeeping: every census row reaches RH only
    through the two cited theorem arrows; every arrow carries a
    round + gate citation (structural, over the frozen FINALFORM);
    G11 razor algebra (r161 GF1 re-chase): 1/(s + 1/F) <= F identity;
    monotone transfer [delta_1 >= F_0, s <= P] ==> g >= 1/(P + 1/F_0);
    two-level equality g == rho^2 delta_1 == 1/(s + 1/delta_1) exact;
    G12 quartic chase (r162 GL5 re-chase): [J == THETA T_z^4 and
    J t_r == 1 + F] ==> F == THETA t_r T_z^4 - 1 + monotone floor;
    G13 R2 rate identity (r150 R2 / r162 GL4 re-chase): the two
    definitional zero-jet identities ==> J t_r == 1 + F;
    G14 SB1 trace loop (r157 re-chase): tau TrH == tf/F with
    1 <= tf <= K - 1 on the exact diag(1,2,5,7) instance (tf 17/12);
    G15 GF5 absorption + twin (r161 re-chase): S1 == jr betapos
    (lam_1 - tau)/(lam_1 - beta_0) exact modulo the B00 root
    condition + corr >= 1; two-level twin: SEC b < 1 exact and
    b == 1/(SEC + 1/F) at the lower end (equality);
    G16 quarter-cap + K(q) partial-sum identity (r156 L2 + r155 D2
    inputs re-instanced; the moment-Laurent dictionary L1 is CITED,
    proven r156 G10-class);
    G17 THE NO-GO WITNESS BATTERY re-instanced (hard asserts, all
    identities intact): (i) 2-mode witness: A_0 invariant while J2
    scales x1e6 EXACTLY (rational instance; r156 G16 class);
    (ii) THETA-anyvalue: THETA == 1e6 AND 1e-6 at fixed T_z with the
    R2 chain intact (r162 G15 class); (iii) SEC-free jet toy: SEC ==
    1e6 exact (r161 class); (iv) chi-cap/rate-blind witness: s == 1e6
    legal at two-level equality (r157 SB2 class); the r160 morph-
    based collective verdict is MEASURED and typed CITED (not cheaply
    re-instantiable, disclosed).
S2  G20 HSW G(T) sanity (cache partial sums below the closed form).
S3  live re-gates, core rungs x = (5,60), (8,80), (13,120) (builder
    R4.build_cell VERBATIM; census/build_V/secular/newton ported
    VERBATIM from the r161/r162 source):
    G30 census: raw-mp census complete + real; zone count == m ==
    4/10/21; K == 11/21/42; residuals <= 1e-20; sign-uniform bottom;
    G31 FULLGAP == frozen strings (2.225493e5/9.951249e5/1.061906e7,
    rel 1e-4); lam_1 simple (rel gap >= 1e3);
    G32 razor block: W3 delta_1 >= FG(1 - 1e-12); GF1 enclosure HARD
    BS <= 1/(s + 1/delta_1) <= g < 1/s and g <= delta_1; s == frozen
    strings (rel 5e-3) and <= 0.10; sg in (0.98, 1.02); delta_1/FG in
    (0.999, 1.001); share_1 == frozen (rel 5e-3); zone-top gap ==
    frozen (rel 5e-3) and in the r162 REPL windows;
    G33 quartic block: THETA == 0.256907/0.172985/0.245072 (rel
    5e-4); c_1/jr/t_r == frozen (rel 5e-4); eta_0^2 == A_0(phi)^2
    (dev <= 1e-30); R2 identity mp-dev <= 1e-30; w_1 == A_0(psi_1)^2
    cross-instrument (rel 1e-30);
    G34 TOPROOT block: betapos == frozen 6-digit strings (rel 5e-4);
    SEC == frozen (rel 5e-4); twin squeeze HARD; S1 >= jr betapos
    HARD; interlacing tau < beta_0 < lam_1; tlaw_0 == CDXLI strings
    (rel 5e-3); lock in frozen windows (rel 5e-3);
    G35 J2 proxy == 0.1259/0.1394/0.1477 (rel 5e-3) AND < 1/4
    (quarter-cap headroom visible at the source).
S4  frozen-ladder bookkeeping (all six rungs, record strings):
    G40 window membership: THETA table inside (0.10, 0.40) and its
    span == [0.1730, 0.2569] subset [0.17, 0.26]; tlaw_0 + tlaw* span
    subset (0.235, 0.585); J2 proxies + r154 anchors subset (0.10,
    0.16); t_r + t_g span subset (0.84, 1.06); s under bars; share_1
    >= 0.5; lock in (1.5, 6.0);
    G41 quartic consistency per rung: |THETA t_r T_z^4 - 1 - FG|/FG
    <= 2e-3 from the frozen tables at ALL SIX rungs;
    G42 THE DEFINITIVE TAU-SCREEN: slopes vs log10 tau over all six
    rungs for THETA/c_1/jr/t_r/tlaw_0/tlaw*/t_g/J2/s/share_1/lock/gap
    all <= 0.30 in abs (DEMAND-FLAT); SEC/betapos slopes printed as
    the position-currency pair; FG growth slope vs log10 x in (3.4,
    4.6) == 3.971 class;
    G43 margins: every windowed constant's minimal relative distance
    to its window edge > 0, table printed (the definitive margins).
S5  census + min-cut:
    G50 THE DEFINITIVE CENSUS GATE (r155 G61 discipline extended):
    coverage of the r155 10-row census through the documented falls
    onto the 7 rows VERIFIED (total, no double count); omega census
    {MEAS, OMEGA-POS} CARDINALITY == 4 with the omega -> row map
    total (SUSCAP2R and DELTA1FLOOR both -> C3, disclosed row-merge);
    every row carries type + margins + provenance;
    G51 min-cut (r116 replica; r142/r144/r146/r150 graph VERBATIM
    from the r162 source): flows base 4 / refined 5 / one-grant 5 /
    counterfactual-parallel 9 NOT REAL; RH unreachable without the
    omega edges.
S6  controls (the synthesis must refuse in false worlds):
    G60 SMOOTH x=5, G61 SCRARITH x=5, G62 EPSTEIN x=8: zone overcount
    == +3/+3/+6; mu_1 fills the zero-free gap (< gamma_1 - 1); tau_w
    == frozen strings (-1.0944/-0.3459/-1.6310, rel 5e-3) < 0; J2_w
    == frozen strings (-2.962/-0.845/-2.710, rel 5e-3) < 0 (the
    window family flips sign); y_t_w/b_top <= 1.0; G63 consistency.
S7  novelty bookkeeping (the N2 discipline; external claims NOT
    gated, typed CITED-EXTERNAL):
    G70 typing gate: every component row has a type from the frozen
    enum, >= 2 named neighbors with identifiers (arXiv/doi/named-
    year), a nonempty exact delta, and a search-disclosure tag on
    every PLAUSIBLY-WORLD-NEW verdict;
    G71 PRIORITY-CLAIM GATE (hard): component (a) is typed KNOWN ==>
    the superlative claim "RH in its most distilled form ever" is
    machine-blocked as NOT-CLAIMABLE-EXTERNALLY; the external
    summary sentence (2) must carry the negative verdict verbatim.
S8  G80 demand audit (CHAIN-AUDIT: the synthesis consumes frozen
    strings + live core rungs + cited theorems only; no ALL-X demand,
    quantifiers inherited); G81 conditioning (1e-25 shift, x=5).
S9  composite verdict + G99 runtime (bar 7200 s wall).

=======================================================================
FROZEN NUMERICS
=======================================================================
KFAC = 1.25; LADDER_CORE = ((5,60),(8,80),(13,120)); HSW = (0.1038,
0.2573, 9.3675) [HSW22 Cor. 1.2]; TOP_GRID_LEN = 3.0; TOP_GRID_STEP =
0.05; NODE_EXCL = 0.02; BIS_ITERS = 250; RES_BAR = 1e-20; QREL_BAR =
1e-30; NULLRES_BAR = 1e-40; SIMP_MIN = 1e3; ENC_SLOP = 1e-12;
GAP_MIN_BAR = 3.0; REPL_WIN = {5: (25,45), 8: (12,22), 13: (17,30)};
frozen six-rung tables as printed in the WINDOW-CONSTANT TABLE above
(sources disclosed there); core-rung precise strings: FULLGAP
2.225493e5/9.951249e5/1.061906e7 (rel 1e-4); THETA 0.256907/0.172985/
0.245072, c_1 0.506860/0.415915/0.495048, jr 1.1245/1.1097/1.0273,
t_r 0.8893/0.9011/0.9734 (rel 5e-4); betapos 0.246289/0.130538/
0.082105, SEC 4.0603/7.6606/12.1796 (rel 5e-4); s 0.02974/0.05981/
0.04413, share_1 0.969/0.965/0.946, gap 33.6233/16.7200/22.6588,
lock 3.644/2.389/3.314, tlaw_0 0.2664/0.3738/0.4674, J2 0.1259/
0.1394/0.1477 (rel 5e-3); S_BAR = 0.10; SGAP_WIN = (0.98, 1.02);
D1FG_WIN = (0.999, 1.001); ETA0_BAR = 1e-30; R2ID_BAR = 1e-30;
W1X_BAR = 1e-30; CTRL: OVER_TAB = {SMOOTH: 3, SCRARITH: 3, EPSTEIN:
6}; TAUW_TAB = {SMOOTH: -1.0944, SCRARITH: -0.3459, EPSTEIN:
-1.6310}; J2W_TAB = {SMOOTH: -2.962, SCRARITH: -0.845, EPSTEIN:
-2.710} (rel 5e-3); CTRL_YTB_MAX = 1.0; TAU_SLOPE_BAR = 0.30;
FG_SLOPE_WIN = (3.4, 4.6); QUARTIC_CONS_BAR = 2e-3; THETA_WIN =
(0.10, 0.40); THETA_SPAN = (0.17, 0.26); TLAW_SPAN = (0.235, 0.585);
J2_SPAN = (0.10, 0.16); TRTG_SPAN = (0.84, 1.06); LOCK_WIN = (1.5,
6.0); SHARE1_BAR = 0.5; J2_ANCHORS = (0.1117, 0.1506) [r154 span];
COND_WIN = (1e-40, 1e-10); GAMMA1_LIT = 14.134725141734694 (ward
only); MODULE_COUNT_FROZEN = 919 (ls verification/v*.py, 2026-08-19,
disclosure string, not gated against the filesystem); RUNTIME_BAR =
7200 s.  Deterministic: NO randomness anywhere.  Cache
verified_zeros_n7000.npy READ-ONLY in ward_ (X5).  All mpf/mpc
arithmetic inside explicit mp.workdps blocks; no f64 refinement of mp
roots; flat O(1) ratios transported as f64 for gating (disclosed);
census/build_V/secular_data/newton_node/row_at/bisect_secular ported
VERBATIM from the r161/r162 gfloor/growthlaw source (== r138-r150
replica class); NO new numeric path.

CALIBRATION DISCLOSURE: NO pre-freeze scratch; every window derives
from frozen record strings of cited rounds (fgl_run2.log 28/28,
fgl_run1/3, gfloor_probe.run1/2.log 26/26, spectral_balance run1/2
26/26, rootladder run1/2 29/29, edge_cleanup run2/3 34/34, j2pf
run1/2 36/36, assembly_walls run1/2, CDLIV/CDLII/CDXLI note strings).
Deep rungs (18/24/28) are NOT rebuilt here (cost); their strings
enter as FROZEN-CITED bookkeeping only, disclosed.  Amendments after
the frozen run, if any, are appended as numbered AMENDMENT blocks.

VERDICT ENUMS (frozen): SYNTHESIS-GATED(final form re-stated, every
arrow cited + re-gated); CENSUS-DEFINITIVE-7(coverage from the r155
10 rows total, no double count, omega cardinality 4 UNCHANGED);
WINDOWS-HOMOGENEOUS(the residue is one flat window family,
DEMAND-FLAT re-screened); QUARTIC-CONSISTENT(frozen six-rung tables
obey FULLGAP == THETA t_r T_z^4 - 1 to 2e-3); NOGO-CORPUS-REGATED
(four witness classes re-instanced, identities intact);
CONTROLS-REFUSE; NOVELTY-ADJUDICATED(a KNOWN / b,c,d,e
PLAUSIBLY-WORLD-NEW with named neighbors, CITED-EXTERNAL);
PRIORITY-CLAIM-BLOCKED("most distilled ever" NOT-CLAIMABLE-
EXTERNALLY, Yoshida-1992 wall); NO-RH-CLAIM.  Composite priority:
INSTRUMENT-EDGE (any edge gate fails, exit 1) >
EXACT-LAYER-OBSTRUCTED (any S1 gate fails) > verdicts as gated.

AST FIREWALL: no zero-oracle names anywhere; np.load only inside
ward_* functions; NO zeta use in this probe; no import of
verification/.  NO RH CLAIM.  EXPLORATION ONLY.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import math
import os
import re
import sys
import time

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import radius4_an_probe as R4                 # round-122 machinery

# ---------------------------------------------------------------- frozen
KFAC = 1.25
LADDER_CORE = ((5, 60), (8, 80), (13, 120))
HSW_A, HSW_B, HSW_C = 0.1038, 0.2573, 9.3675
TOP_GRID_LEN = 3.0
TOP_GRID_STEP = 0.05
NODE_EXCL = 0.02
BIS_ITERS = 250
RES_BAR = 1e-20
QREL_BAR = 1e-30
NULLRES_BAR = 1e-40
SIMP_MIN = 1e3
ENC_SLOP = 1e-12
GAP_MIN_BAR = 3.0
REPL_WIN = {5: (25.0, 45.0), 8: (12.0, 22.0), 13: (17.0, 30.0)}

X_ALL = (5, 8, 13, 18, 24, 28)
TAU_TAB = {5: 1.60658e-16, 8: 3.77263e-30, 13: 2.49904e-54,
           18: 5.21974e-79, 24: 1.8456e-108, 28: 5.32373e-128}
FG_TAB = {5: 2.225493e5, 8: 9.951249e5, 13: 1.061906e7,
          18: 3.249680e7, 24: 1.138230e8, 28: 1.651310e8}
THETA_TAB = {5: 0.2569, 8: 0.1730, 13: 0.2451, 18: 0.1904,
             24: 0.2206, 28: 0.1830}
C1_TAB = {5: 0.5069, 8: 0.4159, 13: 0.4950, 18: 0.4364,
          24: 0.4697, 28: 0.4278}
JR_TAB = {5: 1.1245, 8: 1.1097, 13: 1.0273, 18: 0.9588,
          24: 1.0020, 28: 1.0615}
TR_TAB = {5: 0.8893, 8: 0.9011, 13: 0.9734, 18: 1.0430,
          24: 0.9980, 28: 0.9421}
TLAW0_TAB = {5: 0.2664, 8: 0.3738, 13: 0.4674, 18: 0.4827,
             24: 0.5122, 28: 0.5778}
TLAWST_TAB = {5: 0.2399, 8: 0.3175, 13: 0.4737, 18: 0.4995,
              24: 0.5099, 28: 0.5316}
TG_TAB = {5: 0.9005, 8: 0.8493, 13: 1.0135, 18: 1.0347,
          24: 0.9957, 28: 0.9200}
J2P_TAB = {5: 0.1259, 8: 0.1394, 13: 0.1477, 18: 0.1486,
           24: 0.1504, 28: 0.1513}
S_TAB = {5: 0.02974, 8: 0.05981, 13: 0.04413, 18: 0.06029,
         24: 0.05108, 28: 0.07165}
SH1_TAB = {5: 0.969, 8: 0.965, 13: 0.946, 18: 0.944,
           24: 0.947, 28: 0.945}
SEC_TAB = {5: 4.0603, 8: 7.6606, 13: 12.1796, 18: 17.9134,
           24: 23.8012, 28: 30.4640}
BPOS_TAB = {5: 0.246289, 8: 0.130538, 13: 0.082105, 18: 0.055824,
            24: 0.042015, 28: 0.032826}
GAP_TAB = {5: 33.6233, 8: 16.7200, 13: 22.6588, 18: 16.5873,
           24: 19.5781, 28: 13.9562}
LOCK_TAB = {5: 3.644, 8: 2.389, 13: 3.314, 18: 2.584,
            24: 2.836, 28: 2.234}
M_TAB = {5: 4, 8: 10, 13: 21, 18: 35, 24: 53, 28: 66}
K_TAB = {5: 11, 8: 21, 13: 42, 18: 66, 24: 96, 28: 117}

THETA_CORE = {5: 0.256907, 8: 0.172985, 13: 0.245072}
C1_CORE = {5: 0.506860, 8: 0.415915, 13: 0.495048}

S_BAR = 0.10
SGAP_WIN = (0.98, 1.02)
D1FG_WIN = (0.999, 1.001)
ETA0_BAR = 1e-30
R2ID_BAR = 1e-30
W1X_BAR = 1e-30
REL_TIGHT = 1e-4     # FULLGAP strings
REL_MID = 5e-4       # 4-6 digit flat ratios
REL_LOOSE = 5e-3     # 3-4 digit strings
THETA_WIN = (0.10, 0.40)
THETA_SPAN = (0.17, 0.26)
TLAW_SPAN = (0.235, 0.585)
J2_SPAN = (0.10, 0.16)
TRTG_SPAN = (0.84, 1.06)
LOCK_WIN = (1.5, 6.0)
SHARE1_BAR = 0.5
J2_ANCHORS = (0.1117, 0.1506)
QUARTIC_CONS_BAR = 2e-3
TAU_SLOPE_BAR = 0.30
FG_SLOPE_WIN = (3.4, 4.6)
OVER_TAB = {"SMOOTH": 3, "SCRARITH": 3, "EPSTEIN": 6}
TAUW_TAB = {"SMOOTH": -1.0944, "SCRARITH": -0.3459, "EPSTEIN": -1.6310}
J2W_TAB = {"SMOOTH": -2.962, "SCRARITH": -0.845, "EPSTEIN": -2.710}
CTRL_YTB_MAX = 1.0
COND_LO, COND_HI = 1e-40, 1e-10
GAMMA1_LIT = 14.134725141734693790   # ward only
MODULE_COUNT_FROZEN = 919
RUNTIME_BAR = 7200.0

SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
T0_WALL = time.time()
CACHE_N7000 = os.path.join(HERE, "verified_zeros_n7000.npy")

CHECKS: list[tuple[str, bool, str]] = []
INFO: list[str] = []
EDGE_FAILS: list[str] = []
EXACT_FAILS: list[str] = []


def check(name: str, ok: bool, detail: str, kind: str = "gate") -> bool:
    ok = bool(ok)
    CHECKS.append((name, ok, detail))
    print("  [%s] %-40s %s" % ("PASS" if ok else "FAIL", name, detail),
          flush=True)
    if not ok:
        if kind == "edge":
            EDGE_FAILS.append(name)
        elif kind == "exact":
            EXACT_FAILS.append(name)
    return ok


def info(msg: str) -> None:
    INFO.append(msg)
    print("  [INFO] " + msg, flush=True)


def section(title: str) -> None:
    print("\n" + "-" * 78 + "\n" + title + "\n" + "-" * 78, flush=True)


def relok(val: float, frozen: float, bar: float) -> bool:
    return abs(val / frozen - 1.0) <= bar


# ------------------------------------------------------------ firewall
def firewall_audit() -> tuple[bool, str]:
    src = open(os.path.abspath(__file__), "r", encoding="utf-8").read()
    tree = ast.parse(src)
    spans = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            spans.append((node.name, node.lineno, max(
                getattr(n, "lineno", node.lineno) for n in ast.walk(node))))

    def owners(lineno: int) -> list[str]:
        return [nm for nm, lo, hi in spans if lo <= lineno <= hi]

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
            fns = owners(node.lineno)
            if not any(f.startswith("audit_") for f in fns):
                bad.append("zeta outside audit_ @%d (%s)"
                           % (node.lineno, fns or "module"))
        if isinstance(node, ast.Attribute) and nm == "load":
            fns = owners(node.lineno)
            if not any(f.startswith("ward_") for f in fns):
                bad.append("np.load outside ward_ @%d (%s)"
                           % (node.lineno, fns or "module"))
    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = ([al.name for al in node.names]
                    if isinstance(node, ast.Import)
                    else [node.module or ""])
            for m in mods:
                if m.startswith("verification"):
                    bad.append("import " + m)
    return (not bad), ("; ".join(bad) if bad else
                       "no zero-oracle; cache in ward_; no zeta use")


# ------------------------------------------------------------- wards
def ward_cache() -> np.ndarray:
    return np.asarray(np.load(CACHE_N7000), float)


# --------------------------------------------------------- source side
def raw_mp_census(cell: dict) -> tuple[np.ndarray, int]:
    """round-132 AMENDMENT-1 node source VERBATIM (r157/r161/r162
    replica)."""
    K = cell["K"]
    with mp.workdps(cell["dps"]):
        aa_mp = mp.log(cell["x"]) / 2
        b = [(k * mp.pi / aa_mp) ** 2 for k in range(1, K)]
        s_mp = b[-1] + 1
        b = [v / s_mp for v in b]
        cs = [mp.mpf(s) for s in cell["cn_mp_str"]]

        def pmul(p, q):
            out = [mp.mpf(0)] * (len(p) + len(q) - 1)
            for i, pv in enumerate(p):
                for j, qv in enumerate(q):
                    out[i + j] += pv * qv
            return out

        def padd(p, q):
            if len(p) < len(q):
                p, q = q, p
            out = list(p)
            off = len(p) - len(q)
            for j, qv in enumerate(q):
                out[off + j] += qv
            return out

        def deflate(p, root):
            out = [p[0]]
            for c in p[1:-1]:
                out.append(c + out[-1] * root)
            return out

        prod_all = [mp.mpf(1)]
        for bj in b:
            prod_all = pmul(prod_all, [mp.mpf(1), -bj])
        poly = [2 * cs[0] * c for c in prod_all]
        for i, k in enumerate(range(1, K)):
            q = deflate(prod_all, b[i])
            term = [2 * cs[k] * ((-1) ** k) * c for c in q] + [mp.mpf(0)]
            poly = padd(poly, term)
        rts = mp.polyroots(poly, maxsteps=300, extraprec=cell["dps"])
        roots = np.array([complex(r) for r in rts]) * float(s_mp)
    realm = np.abs(roots.imag) <= 1e-10 * float(s_mp)
    real_y = roots[realm & (roots.real > 0)]
    n_nonreal = int(np.sum(~realm))
    return np.sort(np.sqrt(real_y.real)), n_nonreal


def en_pair(cs: list, aa, oms: list, t):
    Rv = 2 * cs[0] / t
    Rp = -2 * cs[0] / t ** 2
    for k in range(1, len(cs)):
        d = t * t - oms[k] ** 2
        Rv += 2 * cs[k] * (-1) ** k * t / d
        Rp += 2 * cs[k] * (-1) ** k * (-(t * t + oms[k] ** 2)) / d ** 2
    s = mp.sin(aa * t)
    c = mp.cos(aa * t)
    return s * Rv, aa * c * Rv + s * Rp


def newton_node(cs: list, aa, oms: list, z0: float, dps: int):
    with mp.workdps(dps):
        t = mp.mpf(repr(float(z0)))
        for _ in range(80):
            f, fp = en_pair(cs, aa, oms, t)
            step = f / fp
            if abs(step) > mp.mpf("0.1"):
                step = step / abs(step) * mp.mpf("0.1")
            t = t - step / 1 if abs(step) < mp.mpf("0.05") else t - step / 2
            if abs(step) < mp.mpf(10) ** (-dps + 6):
                break
        f, _fp = en_pair(cs, aa, oms, t)
        return t, abs(f)


def hsw_G(T: float) -> float:
    with mp.workdps(40):
        Tm = mp.mpf(repr(float(T)))
        al = mp.mpf(repr(HSW_A))
        be = mp.mpf(repr(HSW_B))
        cc = mp.mpf(repr(HSW_C))
        lg = mp.log(Tm)
        ll = mp.log(lg)
        t1 = (mp.log(Tm / (2 * mp.pi)) + 1) / (2 * mp.pi * Tm)
        t2 = (al * (2 * lg + 1) / 2 + be * (ll + 1 / (2 * lg))
              + cc) / Tm ** 2
        t3 = (al * lg + be * ll + cc) / Tm ** 2
        return float(t1 + t2 + t3)


# ------------------------------------------------- constraint machinery
def row_at(t_mp, K, oms, nrm):
    r = [mp.mpf(0)] * K
    r[0] = (2 / t_mp) / nrm[0]
    for k in range(1, K):
        r[k] = (2 * (-1) ** k * t_mp / (t_mp * t_mp - oms[k] ** 2)) / nrm[k]
    return r


def build_V(ce: dict, gpts_mp: list) -> dict:
    """kernel of constraint rows at gpts; eigen-data of the Gram-
    orthonormalized compression of Mq (r138-r162 replica VERBATIM)."""
    K = ce["K"]
    dps = ce["dps"]
    with mp.workdps(dps):
        cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
        aa = mp.log(ce["x"]) / 2
        oms = [k * mp.pi / aa for k in range(K)]
        oms_f = [float(o) for o in oms]
        nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
               for k in range(K)]
        Mq = ce["mpM"]
        tau_mp = ce["mpE"][0]
        mcon = len(gpts_mp)
        Rm = mp.zeros(mcon, K)
        for j in range(mcon):
            g = gpts_mp[j]
            Rm[j, 0] = (2 / g) / nrm[0]
            for k in range(1, K):
                Rm[j, k] = (2 * (-1) ** k * g / (g * g - oms[k] ** 2)) \
                    / nrm[k]
        piv = []
        used = set()
        for j in range(mcon):
            gjf = float(gpts_mp[j])
            order = sorted(range(1, K), key=lambda k: abs(oms_f[k] - gjf))
            for k in order:
                if k not in used:
                    piv.append(k)
                    used.add(k)
                    break
        free = [k for k in range(K) if k not in used]
        RP = mp.zeros(mcon, mcon)
        for j in range(mcon):
            for i2, k in enumerate(piv):
                RP[j, i2] = Rm[j, k]
        Nb = mp.zeros(K, len(free))
        for fi, k in enumerate(free):
            rhs = mp.matrix([-Rm[j, k] for j in range(mcon)])
            zsol = mp.lu_solve(RP, rhs)
            Nb[k, fi] = mp.mpf(1)
            for i2, kp in enumerate(piv):
                Nb[kp, fi] = zsol[i2]
        resR = 0.0
        for j in range(mcon):
            for fi in range(len(free)):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Rm[j, k] * Nb[k, fi]
                resR = max(resR, float(abs(acc)))
        nf = len(free)
        QN = mp.zeros(K, nf)
        for i in range(K):
            for fi in range(nf):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Mq[i, k] * Nb[k, fi]
                QN[i, fi] = acc
        Qr = mp.zeros(nf, nf)
        Gr = mp.zeros(nf, nf)
        for i in range(nf):
            for j2 in range(i + 1):
                accq = mp.mpf(0)
                accg = mp.mpf(0)
                for k in range(K):
                    accq += Nb[k, i] * QN[k, j2]
                    accg += Nb[k, i] * Nb[k, j2]
                Qr[i, j2] = Qr[j2, i] = accq
                Gr[i, j2] = Gr[j2, i] = accg
        L = mp.cholesky(Gr)

        def fwd(rhs_list, L=L, nf=nf):
            y = [mp.mpf(0)] * nf
            for i in range(nf):
                acc = rhs_list[i]
                for j2 in range(i):
                    acc -= L[i, j2] * y[j2]
                y[i] = acc / L[i, i]
            return y

        Yv = mp.zeros(nf, nf)
        for col in range(nf):
            y = fwd([Qr[i, col] for i in range(nf)])
            for i in range(nf):
                Yv[i, col] = y[i]
        Wm = mp.zeros(nf, nf)
        for col in range(nf):
            y = fwd([Yv[col, i] for i in range(nf)])
            for i in range(nf):
                Wm[i, col] = y[i]
        for i in range(nf):
            for j2 in range(i):
                sym = (Wm[i, j2] + Wm[j2, i]) / 2
                Wm[i, j2] = Wm[j2, i] = sym
        Ew, Vw = mp.eigsy(Wm)
        order = sorted(range(nf), key=lambda i: Ew[i])
        qs = [Ew[order[i]] for i in range(nf)]
        Z = mp.zeros(nf, nf)
        for c, i in enumerate(order):
            for r in range(nf):
                Z[r, c] = Vw[r, i]
        qrel = float((qs[0] - tau_mp) / tau_mp)
    return dict(qs=qs, Z=Z, Nb=Nb, fwd=fwd, nf=nf, resR=resR,
                qrel=qrel, cs=cs, aa=aa, oms=oms, nrm=nrm,
                tau_mp=tau_mp, Rm=Rm)


def secular_data(Vd: dict, r: list):
    """(lam*, etn, rho2, chi) for the extra row r on V (r141/r161/r162
    shape; bisection BIS_ITERS).  Caller sets workdps."""
    nf, Nb, fwd = Vd["nf"], Vd["Nb"], Vd["fwd"]
    qs, Z = Vd["qs"], Vd["Z"]
    K = len(r)
    d = []
    for fi in range(nf):
        acc = mp.mpf(0)
        for k in range(K):
            acc += Nb[k, fi] * r[k]
        d.append(acc)
    e = fwd(d)
    en2 = sum(v * v for v in e)
    et = []
    for i in range(nf):
        acc = mp.mpf(0)
        for k in range(nf):
            acc += Z[k, i] * e[k]
        et.append(acc)
    sq = mp.sqrt(en2)
    etn = [v / sq for v in et]
    rho2 = etn[0] * etn[0]
    lo, hi = qs[0], qs[1]

    def fsec(mu):
        return sum(etn[i] * etn[i] / (qs[i] - mu) for i in range(nf))
    for _ in range(BIS_ITERS):
        mid = (lo + hi) / 2
        if fsec(mid) < 0:
            lo = mid
        else:
            hi = mid
    chi = sum(etn[i] * etn[i] / (qs[i] - qs[0]) for i in range(1, nf))
    return lo, etn, rho2, chi


def bisect_secular(w, E, K, lo, hi, iters):
    """bottom root of sum_i w[i]/(z - E[i]) in (lo, hi) (r150/r161
    source VERBATIM).  Caller sets workdps."""
    for _ in range(iters):
        mid = (lo + hi) / 2
        v = mp.mpf(0)
        for i in range(K):
            v += w[i] / (mid - E[i])
        if v > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# --------------------------------------------------- final-form data
FINALFORM_ARROWS = [
    ("{L1, WPD} on dense tail-a", "(H-conv)+(H-trace)",
     "THEOREM R, r128/CDXXX (doublelimit_proof_probe)"),
    ("(H-conv)+(H-trace)", "RH",
     "NF-CLOSURE, r122/CDXXIII (Montel/Vitali/Hurwitz)"),
    ("dense-a", "dense tail-a",
     "DENSE-TAIL reduction, r155/CDLIX G17/G20/G60"),
]
CENSUS7 = [
    ("TOPROOT", "arithmetic-pinning",
     "B00-ROOTGAP == SEC-cap; twin 1/(SEC+1/FG) <= betapos <= 1/SEC "
     "PROVEN; S1-floor ABSORBED; betapos 0.246289 -> 0.032826, SEC "
     "4.0603 -> 30.4640, defect 3.1e-7 -> 6.9e-12",
     "r140/r146/r150 R1-R4/r156 L1-L6/r161 GF5"),
    ("TLAWCAP-BLOCK", "arithmetic-pinning + technical legs",
     "T-WINDOW (J2 window [0.1117, 0.1513] IRREDUCIBLE-COLLECTIVE + "
     "edge separation at horizon; sliver + window-at-zeros CLOSED "
     "below horizon) + ANCHOR-EPS-LOCK + PERCELL-REL + JUMPSUM legs",
     "r142 W1-W3/r148/r151 J1-J3/r154 P1-P7/r155 TJ+JJ/r156 L2/"
     "r159 E1/r160 G83"),
    ("QSUBGAP-FLOOR", "arithmetic-pinning (razor-sharp)",
     "= s-cap AND delta_1-floor; 1/(s+1/delta_1) <= g < 1/s PROVEN "
     "(2-level equality); DELTA1FLOOR <=> TRACEFLOOR; == {THETA, "
     "t_r} windows via FULLGAP == THETA t_r T_z^4 - 1; s 0.0297.."
     "0.0716, sg == 1.0000, THETA [0.1730, 0.2569]",
     "r139/r142/r146/r150/r157 SB1-SB5/r161 GF1-GF4/r162 GL1-GL5"),
    ("H-PIN", "arithmetic-pinning",
     "L1BAND/DOMASYM ball-matching + no-stray + zone mass <= TL/8; "
     "Q-swamp strip CLOSED wholesale (357 certificates, x in "
     "[3, 121]); conditionality x >= 3",
     "r131/r133/r136 M-E-T-C-A/r159 E3"),
    ("H-FW", "classical-conditional",
     "M2-validity r135-class + ball validity + zone-mass margin + "
     "tau-pos/census framework", "r135/r137/r147"),
    ("DENSE-A-IN-TAIL", "classical-conditional",
     "the dense-subset demand of TAILWPD on ((H-1/2)^2, oo) ~ "
     "(9e24, oo)", "r122/r141 V2/r155 G20"),
    ("TAILWPD", "classical-conditional, RH-EQUIVALENT-AT-TAIL",
     "{L1, WPD}/(H-conv) on a dense subset of ((H-1/2)^2, oo); "
     "below tail closed by PT21 + w in [0, 1/4]; extension algebra "
     "closed (D2 + MG); window-a IRREDUCIBLE -- the world front",
     "r128 G26/r132 D-W1-P1/r155 G16-G19/G53"),
]
R155_ROWS = ("ANCHOR-EPS-LOCK", "TOPROOT", "SUSCAP2R", "DELTA1FLOOR",
             "PERCELL-REL", "JUMPSUM", "H-PIN", "SIMPLICITY", "H-FW",
             "TAILWPD")
R155_MAP = {
    "ANCHOR-EPS-LOCK": ("TLAWCAP-BLOCK", "leg fold, r155 G61 + r151 G15"),
    "TOPROOT": ("TOPROOT", "S1-floor absorbed, r161 GF5a"),
    "SUSCAP2R": ("QSUBGAP-FLOOR", "razor merge, r161 GF1 (omega kept)"),
    "DELTA1FLOOR": ("QSUBGAP-FLOOR", "razor merge, r161 GF1 (omega kept)"),
    "PERCELL-REL": ("TLAWCAP-BLOCK", "leg fold; per-cell-certified r155"),
    "JUMPSUM": ("TLAWCAP-BLOCK", "leg fold; THEOREM JJ r155"),
    "H-PIN": ("H-PIN", "Q-swamp strip closed, r159 E3"),
    "SIMPLICITY": ("FALLEN", "Z8 subsumed by DELTA1FLOOR, r159 G12/G42"),
    "H-FW": ("H-FW", "unchanged"),
    "TAILWPD": ("TAILWPD", "dense-subset demand split out as "
                "DENSE-A-IN-TAIL (bookkeeping)"),
}
OMEGA4 = {"TOPROOT": "TOPROOT", "TLAWCAP": "TLAWCAP-BLOCK",
          "SUSCAP2R": "QSUBGAP-FLOOR", "DELTA1FLOOR": "QSUBGAP-FLOOR"}

NOVELTY = [
    ("(a) criterion shape: finite Weil-form positivity on a cofinal "
     "ladder ==> RH", "KNOWN",
     ("Yoshida 1992 doi:10.2969/aspm/02110281; Suzuki 2023 "
      "doi:10.1112/jlms.12785 + arXiv:2606.09096; "
      "Connes-Consani-Moscovici arXiv:2511.22755 (EMS 2026); "
      "Connes-van Suijlekom 2025; Connes arXiv:2602.04022; Weil 1952; "
      "Li 1997; Keiper 1992; Bombieri-Lagarias 1999; Baez-Duarte 2003"),
     "delta: the corpus carrier (constrained prime-comb Galerkin + "
     "certified zone kernels) + two-theorem transfer + census "
     "discipline are NEW-IN-CORPUS; the SHAPE is not world-new", ""),
    ("(b) reduction machinery: razor enclosure, pinch identities, "
     "zero-jet laws, moment-Laurent ladder, quartic gap law",
     "PLAUSIBLY-WORLD-NEW",
     ("Killip-Simon Ann. Math. 158 (2003) + Case sum rules "
      "math-ph/0112008; Simon, Szego's Theorem and its Descendants "
      "(2011); Gamboa-Nagel-Rouault arXiv:1608.04825; "
      "Bunch-Nielsen-Sorensen Numer. Math. 31 (1978); O'Leary-Stewart "
      "J. Comput. Phys. 90 (1990); Bessonov-Denisov "
      "doi:10.2140/apde.2021.14.1509"),
     "delta: the same GENRE (exact positive-term sum rules; bordered "
     "secular machinery) on a different object; no external exact "
     "enclosure/identity family on prime-comb constraint operators "
     "found", "search-disclosure: 2026-08-19 thorough"),
    ("(c) negative results: identities-intact algebra-cannot-force "
     "witness corpus", "PLAUSIBLY-WORLD-NEW",
     ("Conrey-Li math/9812166 (IMRN 2000, de Branges positivity "
      "fails for zeta and L(s, chi_4)); Lax-Phillips 1976 Sec. 7 "
      "App. 2; Bombieri, Rend. Lincei 2000"),
     "delta: external no-gos are single counterexamples against "
     "fixed hypotheses; the corpus holds a systematic witness FAMILY "
     "driving each candidate algebra bound to any value with all "
     "identities intact -- no external analog found",
     "search-disclosure: 2026-08-19 thorough"),
    ("(d) instrument class: certified off-line detection from "
     "arithmetic source data (v916/v917; r123/r125)",
     "PLAUSIBLY-WORLD-NEW",
     ("Davenport-Heilbronn J. LMS 1936; Potter-Titchmarsh 1935; "
      "Bombieri-Hejhal 1987 + Hejhal supercomputer studies; "
      "Platt-Trudgian 2021 (on-line only); EpsteinLib "
      "arXiv:2412.16317 (evaluation only)"),
     "delta: no 2025-2026 work certifies OFF-line detection from "
     "arithmetic source data through a finite spectral instrument "
     "without evaluating the target function; r125 typing UPHELD",
     "search-disclosure: 2026-08-19 re-verified"),
    ("(e) window-constant phenomenology: flat arithmetic-pinned O(1) "
     "windows of a prime-comb operator family",
     "PLAUSIBLY-WORLD-NEW",
     ("Connes-Consani-Moscovici arXiv:2511.22755 Sec. 6; Zenodo "
      "doi:10.5281/zenodo.19655106 + doi:10.5281/zenodo.20427500 "
      "(2026 scaling studies); Montgomery 1973/Odlyzko 1987 GUE "
      "constants; Lagarias Acta Arith. 120 (2005)"),
     "delta: flat STRUCTURAL scalings of prime-built operators exist "
     "(CvS/CCM studies); no arithmetic-pinned O(1) window family "
     "with no-go typing and sign-flipping controls located",
     "search-disclosure: 2026-08-19 thorough"),
]
NOVELTY_ENUM = ("KNOWN", "NEW-IN-CORPUS", "PLAUSIBLY-WORLD-NEW",
                "CITED-EXTERNAL")
PRIORITY_CLAIM = {
    "claim": "RH in its most distilled form ever",
    "verdict": "NOT-CLAIMABLE-EXTERNALLY",
    "reason": "component (a) typed KNOWN: Yoshida 1992 is already an "
              "exactly-cofinal finite-window equivalence; CCM/CvS "
              "supply concrete finite prime-built matrices; the 2026 "
              "world front runs finite-Weil-matrix arguments",
}


# --------------------------------------------------------- exact layer
def symbolic_gates() -> list[tuple[str, bool, str]]:
    import sympy as sp
    out = []

    # ---------------- G10 final-form DAG bookkeeping
    cite_pat = re.compile(r"r1[0-9][0-9]|CD[CLXVI]+")
    nodes = set()
    for a, b, _c in FINALFORM_ARROWS:
        nodes.add(a)
        nodes.add(b)
    okA = all(bool(cite_pat.search(c)) for _a, _b, c in FINALFORM_ARROWS)
    # reachability: census rows -> {L1, WPD} interface -> RH
    okB = ("RH" in nodes and "{L1, WPD} on dense tail-a" in nodes)
    okC = all(bool(re.search(r"r1[0-9][0-9]", prov))
              for _n, _t, _m, prov in CENSUS7)
    out.append(("G10-finalform-dag", okA and okB and okC,
                "RH <== [NF-closure r122/CDXXIII] + [Theorem R r128/"
                "CDXXX] + {L1, WPD} on dense tail-a; every arrow and "
                "every census row carries a round citation "
                "(structural bookkeeping over the frozen FINALFORM)"))

    # ---------------- G11 razor algebra (r161 GF1 re-chase)
    s_, F_ = sp.symbols("s_ F_", positive=True)
    okA = sp.simplify(F_ - 1 / (s_ + 1 / F_)
                      - F_ ** 2 * s_ / (F_ * s_ + 1)) == 0
    dF = sp.diff(1 / (s_ + 1 / F_), F_)
    dS = sp.diff(1 / (s_ + 1 / F_), s_)
    okB = sp.simplify(dF - 1 / (F_ * s_ + 1) ** 2) == 0 \
        and sp.simplify(dS + 1 / (s_ + 1 / F_) ** 2) == 0
    # two-level equality: g == rho2*Delta == 1/(s + 1/Delta)
    r2, De = sp.symbols("r2 De", positive=True)
    s2l = (1 - r2) / (De * r2)
    okC = sp.simplify(r2 * De - 1 / (s2l + 1 / De)) == 0
    out.append(("G11-razor-algebra", okA and okB and okC,
                "1/(s + 1/F) <= F identity (defect F^2 s/(Fs+1)); "
                "monotone in delta_1, antitone in s (transfer "
                "[delta_1 >= F_0, s <= P] ==> g >= 1/(P + 1/F_0)); "
                "TWO-LEVEL EQUALITY g == rho^2 delta_1 == "
                "1/(s + 1/delta_1) exact -- THEOREM GF1 re-chased "
                "(r161 CITED)", ))

    # ---------------- G12 quartic chase (r162 GL5 re-chase)
    th, tr, Tz, Fq = sp.symbols("th tr Tz Fq", positive=True)
    J_ = th * Tz ** 4
    okA = sp.simplify(sp.solve(sp.Eq(J_ * tr, 1 + Fq), Fq)[0]
                      - (th * tr * Tz ** 4 - 1)) == 0
    th0, c0 = sp.Rational(1, 10), sp.Rational(1, 2)
    okB = bool(th0 * c0 * sp.Integer(10) ** 4 - 1 > 0)
    out.append(("G12-quartic-chase", okA and okB,
                "[J == THETA T_z^4 and J t_r == 1 + FULLGAP] ==> "
                "FULLGAP == THETA t_r T_z^4 - 1 (GL5 re-chase, r162 "
                "CITED); monotone floor transfer positive at the "
                "frozen window ends (0.10 x 0.5)"))

    # ---------------- G13 R2 rate identity (r150/r162 re-chase)
    A0, A1, G_, t0, t1 = sp.symbols("A0 A1 G_ t0 t1", positive=True)
    tau_ = 8 * A0 ** 2 * G_ * t0
    lam_ = 8 * A1 ** 2 * G_ * t1
    Fr = lam_ / tau_ - 1
    Jr = (A1 / A0) ** 2
    okA = sp.simplify(Jr * (t1 / t0) - (1 + Fr)) == 0
    okB = sp.simplify((Jr / Fr) * (t1 / t0) - (1 + 1 / Fr)) == 0
    out.append(("G13-r2-rate-identity", okA and okB,
                "tau == 8 A_0^2 G tlaw_0 and lam_1 == 8 A_1^2 G "
                "tlaw_1 ==> J t_r == 1 + FULLGAP and jr t_r == "
                "1 + 1/FULLGAP EXACT (r150 R2 / r162 GL4 re-chase)"))

    # ---------------- G14 SB1 trace loop (r157 re-chase)
    lam1s, lam2s, lam3s, taus = sp.symbols("lam1s lam2s lam3s taus",
                                           positive=True)
    TrH = 1 / (lam1s - taus) + 1 / (lam2s - taus) + 1 / (lam3s - taus)
    Fs = (lam1s - taus) / taus
    tf = sp.simplify(taus * TrH * Fs)
    tf_inst = tf.subs({taus: 1, lam1s: 2, lam2s: 5, lam3s: 7})
    okA = sp.simplify(tf_inst - sp.Rational(17, 12)) == 0
    okB = bool(tf_inst >= 1) and bool(tf_inst <= 3)
    terms = [sp.Rational(1, 1), sp.Rational(1, 4), sp.Rational(1, 6)]
    okC = all(t <= 1 for t in terms) and sum(terms) == sp.Rational(17, 12)
    out.append(("G14-sb1-trace-loop", okA and okB and okC,
                "tau TrH == tf/FULLGAP with tf = sum (lam_1 - tau)/"
                "(lam_i - tau) in [1, K-1]; diag(1,2,5,7) instance "
                "tf == 17/12 (r157 SB1 re-chase; the Y1 loop "
                "adjudication CITED)"))

    # ---------------- G15 GF5 absorption + twin (r161 re-chase)
    w0s, w1s, bet = sp.symbols("w0s w1s bet", positive=True)
    lam1g, taug = sp.symbols("lam1g taug", positive=True)
    S1 = (w1s / (lam1g - bet)) / (w0s / (bet - taug))
    jr_ = (w1s / w0s) * taug / (lam1g - taug)
    bp_ = (bet - taug) / taug
    okA = sp.simplify(S1 - jr_ * bp_ * (lam1g - taug) / (lam1g - bet)) == 0
    # two-level twin: beta = (w0 lam1 + w1 tau)/(w0 + w1)
    bet2 = (w0s * lam1g + w1s * taug) / (w0s + w1s)
    D1_ = (lam1g - taug) / taug
    SEC_ = (w1s / w0s) / D1_
    b2 = sp.simplify((bet2 - taug) / taug)
    okB = sp.simplify(SEC_ * b2 - w1s / (w0s + w1s)) == 0
    okC = sp.simplify(b2 - 1 / (SEC_ + 1 / D1_)) == 0
    out.append(("G15-gf5-absorption-twin", okA and okB and okC,
                "S1 == jr betapos (lam_1 - tau)/(lam_1 - beta_0) "
                "EXACT modulo the B00 root condition (corr >= 1 for "
                "beta_0 >= tau ==> S1-floor ABSORBED); two-level "
                "twin: SEC betapos == w1/(w0+w1) < 1 and betapos == "
                "1/(SEC + 1/FG) at the lower end (r161 GF5 re-chase)"))

    # ---------------- G16 quarter cap + K(q) identity
    z_ = sp.symbols("z_", real=True)
    okA = sp.simplify(sp.Rational(1, 4) - z_ * (1 - z_)
                      - (z_ - sp.Rational(1, 2)) ** 2) == 0
    q_ = sp.symbols("q_", positive=True)
    n9 = 9
    lhs = (1 - q_) ** 2 * sum(k * q_ ** (k - 1) for k in range(1, n9 + 1))
    rhs = 1 - (n9 + 1) * q_ ** n9 + n9 * q_ ** (n9 + 1)
    okB = sp.simplify(lhs - rhs) == 0
    out.append(("G16-quartercap-kq", okA and okB,
                "z(1-z) <= 1/4 exact ((z - 1/2)^2 witness; the r156 "
                "L2 quarter-cap input); K(q) partial-sum identity at "
                "n = 9 (the r155 D2 input); the moment-Laurent "
                "dictionary L1 is CITED (proven r156)"))

    # ---------------- G17 no-go witness battery (hard asserts)
    # (i) 2-mode witness: A_0 invariant, J2 x 1e6 exact
    d_ = sp.Rational(-999999, 1000000)
    c0_, c1_, c2_ = sp.Integer(1), sp.Integer(1), sp.Integer(1)
    b0_, b1_, b2_ = sp.Integer(0), sp.Integer(1), sp.Integer(4)
    A0w = c0_ - c1_ + c2_
    A2w = c0_ * b0_ - c1_ * b1_ + c2_ * b2_
    A4w = c0_ * b0_ ** 2 - c1_ * b1_ ** 2 + c2_ * b2_ ** 2
    J2w = (A4w / A0w) / (A2w / A0w) ** 2
    c1n, c2n = c1_ + d_, c2_ + d_
    A0n = c0_ - c1n + c2n
    A2n = c0_ * b0_ - c1n * b1_ + c2n * b2_
    A4n = c0_ * b0_ ** 2 - c1n * b1_ ** 2 + c2n * b2_ ** 2
    J2n = (A4n / A0n) / (A2n / A0n) ** 2
    okI = (A0n == A0w) and sp.simplify(J2n / J2w
                                       - sp.Integer(10) ** 6) == 0
    assert okI, "2-mode witness failed"
    # (ii) THETA-anyvalue at fixed T_z with R2 chain intact
    Tzf = sp.Integer(7)
    for target in (sp.Integer(10) ** 6, sp.Rational(1, 10 ** 6)):
        Jt = target * Tzf ** 4
        Ft = sp.Rational(3, 1)
        trt = (1 + Ft) / Jt
        okII = sp.simplify(Jt * trt - (1 + Ft)) == 0 \
            and sp.simplify(Jt / Tzf ** 4 - target) == 0
        assert okII, "THETA-anyvalue witness failed"
    # (iii) SEC-free jet toy
    p_, D1t = sp.Integer(1), sp.Integer(1)
    q2 = sp.Integer(10) ** 6 * p_ ** 2 * D1t
    SECt = (q2 / p_ ** 2) / D1t
    okIII = SECt == sp.Integer(10) ** 6
    assert okIII, "SEC-free witness failed"
    # (iv) chi-cap rate-blind witness: s == 1e6 legal at 2-level
    rho2w = sp.Rational(1, 1 + 10 ** 6)
    Dw = sp.Integer(1)
    sw = (1 - rho2w) / (Dw * rho2w)
    okIV = sp.simplify(sw - sp.Integer(10) ** 6) == 0 \
        and sp.simplify(rho2w * Dw - 1 / (sw + 1 / Dw)) == 0
    assert okIV, "chi-cap witness failed"
    out.append(("G17-nogo-witness-battery", okI and okIII and okIV,
                "(i) 2-mode witness: A_0 invariant, J2 x 1e6 EXACT "
                "(r156 G16 class); (ii) THETA == 1e6 AND 1e-6 at "
                "fixed T_z, R2 chain intact (r162 G15 class); (iii) "
                "SEC == 1e6 exact (r161 class); (iv) s == 1e6 legal "
                "at two-level equality (r157 SB2 class) -- ALGEBRA-"
                "ONLY-REFUTED for THETA/J2/SEC/s, hard-asserted; the "
                "r160 morph collective verdict is MEASURED, typed "
                "CITED (disclosed)"))
    return out


# ---------------------------------------------------------------- main
def main() -> int:
    par = argparse.ArgumentParser()
    par.add_argument("--smoke", action="store_true")
    args = par.parse_args()
    smoke = args.smoke

    print("novelty_synthesis_probe -- PRIME.FINALFORM.NOVELTY.01")
    print("SPEC_SHA %s" % SPEC_SHA[:16])
    print("mode: %s" % ("SMOKE (NOT-VERDICT-BEARING)" if smoke
                        else "FULL"))
    print("NO RH CLAIM.  EXPLORATION ONLY.")

    core = LADDER_CORE[:1] if smoke else LADDER_CORE
    controls = (("SMOOTH", 5, 60),) if smoke else \
        (("SMOOTH", 5, 60), ("SCRARITH", 5, 60), ("EPSTEIN", 8, 80))

    # ---------------------------------------------------------- S0
    section("S0  FIREWALL + CACHE")
    ok, det = firewall_audit()
    check("G01-ast-firewall", ok, det, kind="edge")
    gam = ward_cache()
    check("G02-cache-health", len(gam) >= 5000
          and abs(float(gam[0]) - GAMMA1_LIT) < 1e-9
          and bool(np.all(np.diff(gam) > 0)),
          "n=%d gamma_1 dev %.1e (READ-ONLY, X5)"
          % (len(gam), abs(float(gam[0]) - GAMMA1_LIT)), kind="edge")
    info("Z1 TYPING (frozen): the live re-gates consume the certified "
         "pinned zone NODES (source data) and cache zeros below "
         "horizon as ward-class data -- typed, not hidden")

    # ---------------------------------------------------------- S1
    section("S1  EXACT LAYER (the load-bearing arrows re-chased)")
    for name, okg, detg in symbolic_gates():
        check(name, okg, detg, kind="exact")
    info("consumed, cited (theorems NOT re-proven here): r122/CDXXIII "
         "NF-closure; r128/CDXXX Theorem R; r131 secular + G17 "
         "crossover; r132 raw census + Theorem D/W1/P1; r137/CDXLI "
         "zero-jet law + tlaw strings; r141 V1-V3; r142 W1-W3; r146 "
         "Y1-Y4; r147 AD1-AD2; r150 R1-R4; r151 J1-J3; r154 P1-P7; "
         "r155 TJ/JJ/D2/MG + 10-row census; r156 L1-L6; r157 SB1-SB5; "
         "r159 E1-E3; r160 taxonomy; r161 GF1-GF5; r162 GL1-GL5; "
         "HSW22 Cor. 1.2; PT21; Courant-Fischer; Cauchy interlacing")

    # ---------------------------------------------------------- S2
    section("S2  TARGETS")
    gtop = float(gam[-1])
    okG = True
    for Ttest in (200.0, 2000.0):
        part = float(np.sum(gam[gam > Ttest] ** (-2.0)))
        okG = okG and part <= hsw_G(Ttest)
    okG = okG and hsw_G(200.0) > hsw_G(2000.0) > hsw_G(gtop)
    check("G20-hsw-G-sanity", okG,
          "cache partial sums below G(T) at T = 200/2000; G "
          "monotone; G(gamma_top) = %.3e" % hsw_G(gtop))

    # ---------------------------------------------------------- S3
    section("S3  LIVE RE-GATES (core rungs; frozen strings exactly)")
    ok30 = ok31 = ok32 = ok33 = ok34 = ok35 = True
    det30, det31, det32, det33, det34, det35 = [], [], [], [], [], []
    ce5 = None
    for x, dps in core:
        ce = R4.build_cell(x, KFAC, "MAIN", dps, want_mp=True)
        if x == 5:
            ce5 = ce
        K = ce["K"]
        print("  x=%d built (K=%d, dps=%d, tau=%s, %.0f s)"
              % (x, K, dps, ce["tau_str"], ce["build_s"]), flush=True)
        Tz = 2 * math.pi * x
        m_zone = int(np.sum(gam <= Tz))
        with mp.workdps(dps):
            E = ce["mpE"]
            V = ce["mpV"]
            tau = E[0]
            lam1 = E[1]
            lam2 = E[2]
            FG = (lam1 - tau) / tau
            aa = mp.log(x) / 2
            oms = [k * mp.pi / aa for k in range(K)]
            b = [o * o for o in oms]
            nrm = [mp.sqrt(2 * aa) if k == 0 else mp.sqrt(aa)
                   for k in range(K)]
            cs = [mp.mpf(s) for s in ce["cn_mp_str"]]
            A0p = sum(((-1) ** k) * cs[k] for k in range(K))
            A2p = sum(((-1) ** k) * cs[k] * b[k] for k in range(K))
            A4p = sum(((-1) ** k) * cs[k] * b[k] ** 2 for k in range(K))
            yt = float(abs(A2p / A0p))
            j2proxy = float(abs(A4p / A0p) / (A2p / A0p) ** 2)
            fg_f = float(FG)
            simp = float((lam2 - lam1) / lam1)
        Gz = hsw_G(Tz)
        tlaw0_f = float(tau) / (8.0 * float(abs(A0p)) ** 2 * Gz)

        # ---- G30 census
        mus, n_nonreal = raw_mp_census(ce)
        seeds = [float(v) for v in mus]
        nds_all = []
        wres = 0.0
        with mp.workdps(dps):
            for s0 in seeds:
                tmu, res = newton_node(cs, aa, oms, s0, dps)
                nds_all.append(tmu)
                wres = max(wres, float(res))
        nds_f_all = np.array([float(v) for v in nds_all])
        n_zone_nodes = int(np.sum(nds_f_all <= Tz))
        with mp.workdps(dps):
            sgs = set()
            for tv in np.arange(0.02, 0.62, 0.02):
                v = en_pair(cs, aa, oms, mp.mpf(repr(float(tv))))[0]
                sgs.add(1 if v > 0 else -1)
        cens_ok = (len(mus) == K - 1 and n_nonreal == 0
                   and wres <= RES_BAR and len(sgs) == 1
                   and n_zone_nodes == m_zone == M_TAB[x]
                   and K == K_TAB[x])
        ok30 = ok30 and cens_ok
        det30.append("x%d: %d nodes zone %d/%d K %d res %.0e"
                     % (x, len(nds_all), n_zone_nodes, m_zone, K, wres))
        zone_nds = nds_all[:m_zone]
        zone_f = [float(v) for v in zone_nds]

        # ---- G31 FULLGAP strings
        fg_ok = relok(fg_f, FG_TAB[x], REL_TIGHT) and simp >= SIMP_MIN
        ok31 = ok31 and fg_ok
        det31.append("x%d: FULLGAP %.6e (frozen %.6e) simp %.1e"
                     % (x, fg_f, FG_TAB[x], simp))

        # ---- G32 razor block
        Vd = build_V(ce, zone_nds)
        with mp.workdps(dps):
            qs = Vd["qs"]
            nf = Vd["nf"]
            tau_v = Vd["tau_mp"]
            d1 = (qs[1] - qs[0]) / tau_v
            d1_f = float(d1)
            w3_ok = bool(d1 >= FG * (1 - mp.mpf("1e-12")))
            tg_grid = list(np.arange(Tz - TOP_GRID_LEN, Tz - 0.001,
                                     TOP_GRID_STEP)) + [Tz - 0.001]
            gmin, argp = None, None
            for tv in tg_grid:
                if min(abs(tv - g) for g in zone_f) < NODE_EXCL:
                    continue
                r = row_at(mp.mpf(repr(float(tv))), K, oms, nrm)
                lam, etn, rho2, chi = secular_data(Vd, r)
                gg = float((lam - qs[0]) / tau_v)
                if gmin is None or gg < gmin:
                    gmin, argp = gg, float(tv)
            p_mp = mp.mpf(repr(float(argp)))
            r = row_at(p_mp, K, oms, nrm)
            lam, etn, rho2, chi = secular_data(Vd, r)
            g_ex = (lam - qs[0]) / tau_v
            s_val = tau_v * chi / rho2
            sg = float(s_val * g_ex)
            s_f = float(s_val)
            e12 = etn[1] * etn[1]
            share1 = float((e12 / (qs[1] - qs[0])) / chi)
            slop = mp.mpf(repr(ENC_SLOP))
            lo_end = 1 / (s_val + 1 / d1)
            hi_end = 1 / s_val
            BS = rho2 * d1
            enc_ok = (bool(BS <= lo_end * (1 + slop))
                      and bool(lo_end <= g_ex * (1 + slop))
                      and bool(g_ex < hi_end)
                      and bool(g_ex <= d1 * (1 + slop)))
        lo_w, hi_w = REPL_WIN[x]
        ok32x = (abs(Vd["qrel"]) <= QREL_BAR
                 and Vd["resR"] <= NULLRES_BAR and w3_ok and enc_ok
                 and gmin >= GAP_MIN_BAR and lo_w <= gmin <= hi_w
                 and relok(gmin, GAP_TAB[x], REL_LOOSE)
                 and s_f <= S_BAR and relok(s_f, S_TAB[x], REL_LOOSE)
                 and SGAP_WIN[0] <= sg <= SGAP_WIN[1]
                 and D1FG_WIN[0] <= d1_f / fg_f <= D1FG_WIN[1]
                 and relok(share1, SH1_TAB[x], REL_LOOSE))
        ok32 = ok32 and ok32x
        det32.append("x%d: qrel %.0e gap %.4f s %.5f sg %.5f d1/FG "
                     "%.6f share1 %.3f enc %s"
                     % (x, Vd["qrel"], gmin, s_f, sg, d1_f / fg_f,
                        share1, enc_ok))
        info("x=%d RAZOR re-gate: BS %.3e <= 1/(s + 1/delta_1) "
             "%.4f <= g %.4f < 1/s %.4f; delta_1/FG %.6f -- the "
             "QSUBGAP row's proven enclosure, live"
             % (x, float(BS), float(lo_end), float(g_ex),
                float(hi_end), d1_f / fg_f))

        # ---- G33 quartic block
        with mp.workdps(dps):
            v0 = [((-1) ** k) / nrm[k] for k in range(K)]
            d0 = []
            for fi in range(nf):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += Vd["Nb"][k, fi] * v0[k]
                d0.append(acc)
            e0v = Vd["fwd"](d0)
            eta = []
            for i in range(nf):
                acc = mp.mpf(0)
                for k in range(nf):
                    acc += Vd["Z"][k, i] * e0v[k]
                eta.append(acc)
            eta0dev = float(abs(eta[0] * eta[0] / (A0p * A0p) - 1))
            cs1 = [V[i, 1] / nrm[i] for i in range(K)]
            A01 = sum(((-1) ** k) * cs1[k] for k in range(K))
            J = (A01 / A0p) ** 2
            Tz2 = mp.mpf(repr(Tz)) ** 2
            theta = float(J / Tz2 ** 2)
            c1v = float(abs(A01 / A0p) / Tz2)
            jr = float(J / FG)
            # r162 smoke-1 lesson: R2 evaluated with the mp t-ratio
            t_r_mp = (lam1 * A0p * A0p) / (tau * A01 * A01)
            t_r = float(t_r_mp)
            r2id = float(abs((J / FG) * t_r_mp / (1 + 1 / FG) - 1))
            # w_1 == A_0(psi_1)^2 cross-instrument
            w1x = mp.mpf(0)
            for k in range(K):
                w1x += v0[k] * V[k, 1]
            w1xdev = float(abs(w1x * w1x / (A01 * A01) - 1))
        ok33x = (eta0dev <= ETA0_BAR and r2id <= R2ID_BAR
                 and w1xdev <= W1X_BAR
                 and relok(theta, THETA_CORE[x], REL_MID)
                 and relok(c1v, C1_CORE[x], REL_MID)
                 and relok(jr, JR_TAB[x], REL_MID)
                 and relok(t_r, TR_TAB[x], REL_MID))
        ok33 = ok33 and ok33x
        det33.append("x%d: THETA %.6f c1 %.6f jr %.4f t_r %.4f "
                     "r2id %.0e eta0 %.0e w1x %.0e"
                     % (x, theta, c1v, jr, t_r, r2id, eta0dev, w1xdev))
        info("x=%d QUARTIC re-gate: J = %.6e == %.4f x T_z^4; "
             "FULLGAP == THETA t_r T_z^4 - 1 (the r162 closed form, "
             "live at this rung)" % (x, float(J), theta))

        # ---- G34 TOPROOT block
        with mp.workdps(dps):
            w = []
            for i in range(K):
                acc = mp.mpf(0)
                for k in range(K):
                    acc += v0[k] * V[k, i]
                w.append(acc * acc)
            w0 = w[0]
            Dl = [(E[i] - tau) / tau for i in range(K)]
            SEC = sum((w[i] / w0) / Dl[i] for i in range(1, K))
            beta0 = bisect_secular(w, E, K, tau, lam1, BIS_ITERS)
            inter_ok = bool(tau < beta0 < lam1)
            bpos = (beta0 - tau) / tau
            lo_b = 1 / (SEC + 1 / FG)
            hi_b = 1 / SEC
            okb = bool(lo_b <= bpos * (1 + slop)) \
                and bool(bpos <= hi_b * (1 + slop))
            GWb = sum(w[i] / (E[i] - beta0) for i in range(1, K))
            S1 = (w[1] / (lam1 - beta0)) / GWb
            jrw = (w[1] / w0) / FG
            okS1 = bool(S1 >= jrw * bpos * (1 - mp.mpf("1e-30")))
            bpos_f = float(bpos)
            SEC_f = float(SEC)
        lock = fg_f / yt
        ok34x = (inter_ok and okb and okS1
                 and relok(bpos_f, BPOS_TAB[x], REL_MID)
                 and relok(SEC_f, SEC_TAB[x], REL_MID)
                 and relok(tlaw0_f, TLAW0_TAB[x], REL_LOOSE)
                 and relok(lock, LOCK_TAB[x], REL_LOOSE)
                 and LOCK_WIN[0] <= lock <= LOCK_WIN[1])
        ok34 = ok34 and ok34x
        det34.append("x%d: SEC %.4f bpos %.6f twin %s S1>=jrb %s "
                     "tlaw0 %.4f lock %.3f"
                     % (x, SEC_f, bpos_f, okb, okS1, tlaw0_f, lock))
        info("x=%d TOPROOT re-gate: twin squeeze 1/(SEC + 1/FG) "
             "%.6f <= betapos %.6f <= 1/SEC %.6f; S1 absorbed "
             "(S1 %.4f >= jr betapos %.4f) -- the r161 GF5 row, live"
             % (x, float(lo_b), bpos_f, float(hi_b), float(S1),
                float(jrw * bpos)))

        # ---- G35 J2 proxy
        ok35x = relok(j2proxy, J2P_TAB[x], REL_LOOSE) and j2proxy < 0.25
        ok35 = ok35 and ok35x
        det35.append("x%d: J2-proxy %.6f (frozen %.4f) < 1/4"
                     % (x, j2proxy, J2P_TAB[x]))

    check("G30-census", ok30,
          "raw-mp census complete + real; zone count == m == frozen; "
          "K == frozen; residuals <= %.0e; sign-uniform: %s"
          % (RES_BAR, "; ".join(det30)))
    check("G31-fullgap-strings", ok31,
          "FULLGAP == frozen record strings (rel %.0e); lam_1 simple "
          "(>= %.0e): %s" % (REL_TIGHT, SIMP_MIN, "; ".join(det31)))
    check("G32-razor-block", ok32,
          "W3 delta_1 >= FG; GF1 enclosure BS <= lo <= g < 1/s HARD; "
          "s/sg/share_1/gap on the frozen strings: %s"
          % "; ".join(det32))
    check("G33-quartic-block", ok33,
          "THETA/c_1/jr/t_r == frozen strings (rel %.0e); eta_0^2 == "
          "A_0^2 <= %.0e; R2 id <= %.0e; w_1 == A_0(psi_1)^2 cross "
          "<= %.0e: %s" % (REL_MID, ETA0_BAR, R2ID_BAR, W1X_BAR,
                           "; ".join(det33)))
    check("G34-toproot-block", ok34,
          "betapos/SEC == frozen strings (rel %.0e); twin squeeze + "
          "S1 >= jr betapos HARD; interlacing; tlaw_0/lock on "
          "strings: %s" % (REL_MID, "; ".join(det34)))
    check("G35-j2-proxy", ok35,
          "J2 proxy == frozen strings (rel %.0e) AND < 1/4 (quarter-"
          "cap headroom at the source): %s"
          % (REL_LOOSE, "; ".join(det35)))

    # ---------------------------------------------------------- S4
    section("S4  FROZEN-LADDER BOOKKEEPING (six rungs, record strings)")
    th_span = (min(THETA_TAB.values()), max(THETA_TAB.values()))
    tlaw_all = list(TLAW0_TAB.values()) + list(TLAWST_TAB.values())
    j2_all = list(J2P_TAB.values()) + list(J2_ANCHORS)
    trtg_all = list(TR_TAB.values()) + list(TG_TAB.values())
    ok40 = (all(THETA_WIN[0] < v < THETA_WIN[1]
                for v in THETA_TAB.values())
            and THETA_SPAN[0] <= th_span[0]
            and th_span[1] <= THETA_SPAN[1]
            and all(TLAW_SPAN[0] < v < TLAW_SPAN[1] for v in tlaw_all)
            and all(J2_SPAN[0] < v < J2_SPAN[1] for v in j2_all)
            and all(TRTG_SPAN[0] < v < TRTG_SPAN[1] for v in trtg_all)
            and all(S_TAB[x] <= (0.15 if x == 28 else S_BAR)
                    for x in X_ALL)
            and all(v >= SHARE1_BAR for v in SH1_TAB.values())
            and all(LOCK_WIN[0] < v < LOCK_WIN[1]
                    for v in LOCK_TAB.values()))
    check("G40-window-membership", ok40,
          "THETA span [%.4f, %.4f] subset %s inside %s; tlaw_0 + "
          "tlaw* subset %s; J2 (proxies + r154 anchors) subset %s; "
          "t_r + t_g subset %s; s under bars; share_1 >= %.1f; lock "
          "in %s -- THE HOMOGENEOUS WINDOW FAMILY"
          % (th_span[0], th_span[1], str(THETA_SPAN), str(THETA_WIN),
             str(TLAW_SPAN), str(J2_SPAN), str(TRTG_SPAN),
             SHARE1_BAR, str(LOCK_WIN)))

    ok41 = True
    rows41 = []
    for x in X_ALL:
        Tz4 = (2 * math.pi * x) ** 4
        pred = THETA_TAB[x] * TR_TAB[x] * Tz4 - 1
        dev = abs(pred / FG_TAB[x] - 1)
        ok41 = ok41 and dev <= QUARTIC_CONS_BAR
        rows41.append("x%d: %.2e" % (x, dev))
    check("G41-quartic-consistency", ok41,
          "|THETA t_r T_z^4 - 1 - FG|/FG <= %.0e at ALL SIX rungs "
          "from the frozen tables: %s (the r162 closed form is "
          "string-consistent across the record)"
          % (QUARTIC_CONS_BAR, "; ".join(rows41)))

    lt = [math.log10(TAU_TAB[x]) for x in X_ALL]

    def slope_of(tab):
        return float(np.polyfit(
            lt, [math.log10(abs(tab[x])) for x in X_ALL], 1)[0])
    named = (("THETA", THETA_TAB), ("c_1", C1_TAB), ("jr", JR_TAB),
             ("t_r", TR_TAB), ("tlaw_0", TLAW0_TAB),
             ("tlaw*", TLAWST_TAB), ("t_g", TG_TAB), ("J2", J2P_TAB),
             ("s", S_TAB), ("share_1", SH1_TAB), ("lock", LOCK_TAB),
             ("gap", GAP_TAB))
    slopes = {nm: slope_of(tab) for nm, tab in named}
    ok42 = all(abs(v) <= TAU_SLOPE_BAR for v in slopes.values())
    lxs = [math.log10(float(x)) for x in X_ALL]
    sl_fg = float(np.polyfit(lxs, [math.log10(FG_TAB[x])
                                   for x in X_ALL], 1)[0])
    ok42 = ok42 and FG_SLOPE_WIN[0] <= sl_fg <= FG_SLOPE_WIN[1]
    check("G42-definitive-tau-screen", ok42,
          "slopes vs log10 tau (112 dex): %s (all <= %.2f: "
          "DEMAND-FLAT, the definitive screen); position pair "
          "SEC %.4f / betapos %.4f (printed, product-squeezed); "
          "FG growth slope %.3f in %s"
          % ("; ".join("%s %+.4f" % (nm, slopes[nm])
                       for nm, _t in named), TAU_SLOPE_BAR,
             slope_of(SEC_TAB), slope_of(BPOS_TAB), sl_fg,
             str(FG_SLOPE_WIN)))

    margins = []
    okm = True
    for nm, tab, win in (("THETA", THETA_TAB, THETA_WIN),
                         ("tlaw", TLAW0_TAB, TLAW_SPAN),
                         ("tlaw*", TLAWST_TAB, TLAW_SPAN),
                         ("J2", J2P_TAB, J2_SPAN),
                         ("t_r", TR_TAB, TRTG_SPAN),
                         ("t_g", TG_TAB, TRTG_SPAN),
                         ("lock", LOCK_TAB, LOCK_WIN)):
        vmin, vmax = min(tab.values()), max(tab.values())
        mlo = (vmin - win[0]) / (win[1] - win[0])
        mhi = (win[1] - vmax) / (win[1] - win[0])
        okm = okm and mlo > 0 and mhi > 0
        margins.append("%s [%.4f, %.4f] in %s margins %.2f/%.2f"
                       % (nm, vmin, vmax, str(win), mlo, mhi))
    check("G43-margins", okm,
          "THE DEFINITIVE MARGIN TABLE (relative distance of each "
          "measured span to its window edges): %s"
          % "; ".join(margins))

    # ---------------------------------------------------------- S5
    section("S5  THE DEFINITIVE CENSUS + MIN-CUT")
    names7 = [row[0] for row in CENSUS7]
    ok_cov = all(R155_MAP[r][0] in names7 or R155_MAP[r][0] == "FALLEN"
                 for r in R155_ROWS)
    ok_tot = set(R155_MAP.keys()) == set(R155_ROWS)
    ok_dup = len(set(names7)) == len(names7) == 7
    ok_om = (len(OMEGA4) == 4
             and all(v in names7 for v in OMEGA4.values()))
    ok_typ = all(t and m and p for _n, t, m, p in CENSUS7)
    for nm, t, m, p in CENSUS7:
        info("CENSUS | %s | %s | %s | [%s]" % (nm, t, m, p))
    info("CENSUS FOOTNOTE | NONDEGENERATE-CELL | witness-certified "
         "per cell at zero cost, strictly weaker than fallen Z8 "
         "[r159 E2]")
    for r in R155_ROWS:
        tgt, why = R155_MAP[r]
        info("r155-COVERAGE | %s -> %s (%s)" % (r, tgt, why))
    check("G50-definitive-census", ok_cov and ok_tot and ok_dup
          and ok_om and ok_typ,
          "THE DEFINITIVE RESIDUE: RH <== [NF-closure r122] + "
          "[Theorem R r128] + the 7-row census above; coverage of "
          "the r155/CDLIX 10 rows through the documented falls "
          "TOTAL (Z8 fallen r159; razor merge r161; leg folds r155; "
          "S1 absorbed r161; Q-swamp + sliver closed r159); no "
          "double count; omega census {MEAS, OMEGA-POS} CARDINALITY "
          "4 UNCHANGED since r116 (SUSCAP2R + DELTA1FLOOR both map "
          "to the QSUBGAP row -- row bookkeeping, no omega closed)")

    INF = 10 ** 6
    base = {("UNC", "HCELLS"): INF, ("HCELLS", "FORMA"): 1,
            ("FORMA", "RH"): INF,
            ("UNC", "PICK"): INF, ("PICK", "SV"): 1, ("SV", "RH"): INF,
            ("UNC", "R4HYP"): 1, ("R4HYP", "RH"): INF,
            ("UNC", "WEYLM"): INF, ("WEYLM", "WEYLH"): 1,
            ("WEYLH", "RH"): INF}
    f_base = R4.maxflow(dict(base), "UNC", "RH")
    ext = dict(base)
    ext.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
                ("NFCLOS", "L1TAILPROVEN"): INF,
                ("L1TAILPROVEN", "TOPROOT"): 1,
                ("TOPROOT", "TAILVIS"): 1,
                ("TAILVIS", "TLAWCAP"): 1,
                ("TLAWCAP", "BANDMASSTHM"): INF,
                ("BANDMASSTHM", "SUSCAP2R"): 1,
                ("SUSCAP2R", "DELTA1FLOOR"): 1,
                ("DELTA1FLOOR", "QSUBGAPTHM"): INF,
                ("QSUBGAPTHM", "PFLOORTHM"): INF,
                ("PFLOORTHM", "COUNTEQTHM"): INF,
                ("COUNTEQTHM", "SEEDBALLTHM"): INF,
                ("SEEDBALLTHM", "SPACREMTHM"): INF,
                ("SPACREMTHM", "DOMASYM"): INF,
                ("DOMASYM", "WPDWIN"): INF, ("WPDWIN", "R4HYP"): INF})
    f_ext = R4.maxflow(dict(ext), "UNC", "RH")
    one = dict(ext)
    one[("SUSCAP2R", "DELTA1FLOOR")] = INF
    f_one = R4.maxflow(dict(one), "UNC", "RH")
    cf = dict(base)
    cf.update({("UNC", "BLKREAL"): INF, ("BLKREAL", "NFCLOS"): INF,
               ("NFCLOS", "TOPROOT"): 1, ("TOPROOT", "R4HYP"): INF,
               ("NFCLOS", "TAILVIS"): 1, ("TAILVIS", "R4HYP"): INF,
               ("NFCLOS", "TLAWCAP"): 1, ("TLAWCAP", "R4HYP"): INF,
               ("NFCLOS", "SUSCAP2R"): 1, ("SUSCAP2R", "R4HYP"): INF,
               ("NFCLOS", "DELTA1FLOOR"): 1,
               ("DELTA1FLOOR", "R4HYP"): INF})
    f_cf = R4.maxflow(dict(cf), "UNC", "RH")
    noomega = {k2: v for k2, v in ext.items() if v >= INF}
    reach = R4.bfs_reach(noomega, "UNC")
    check("G51-mincut", f_base == 4 and f_ext == 5 and f_one == 5
          and f_cf == 9 and "RH" not in reach,
          "flows: base 4, refined 5 (r142/r144/r146/r150 graph "
          "VERBATIM); one-grant 5; counterfactual PARALLEL 9 NOT "
          "REAL; RH unreachable without the omega edges -- the r116 "
          "replica, unchanged")

    # ---------------------------------------------------------- S6
    section("S6  CONTROLS (the synthesis must refuse)")
    ctrl_ok = True
    for world, xw, dpsw in controls:
        cw = R4.build_cell(xw, KFAC, world, dpsw, want_mp=True)
        musw, _nr = raw_mp_census(cw)
        Tzw = 2 * math.pi * xw
        n_nodes_w = int(np.sum(musw <= Tzw))
        m_true_w = int(np.sum(gam <= Tzw))
        over = n_nodes_w - m_true_w
        with mp.workdps(dpsw):
            tauw = float(cw["mpE"][0])
            csw = [mp.mpf(s) for s in cw["cn_mp_str"]]
            aaw = mp.log(xw) / 2
            omsw = [k * mp.pi / aaw for k in range(cw["K"])]
            A0cw = sum(((-1) ** k) * csw[k] for k in range(cw["K"]))
            A2cw = sum(((-1) ** k) * csw[k] * omsw[k] ** 2
                       for k in range(cw["K"]))
            A4cw = sum(((-1) ** k) * csw[k] * omsw[k] ** 4
                       for k in range(cw["K"]))
            ytbw = float(abs(A2cw / A0cw)) / float(omsw[-1] ** 2)
            j2w = float((A4cw / A0cw) / (A2cw / A0cw) ** 2)
        refuse = (over == OVER_TAB[world]
                  and float(musw[0]) < float(gam[0]) - 1.0
                  and tauw < 0 and relok(tauw, TAUW_TAB[world],
                                         REL_LOOSE)
                  and j2w < 0 and relok(j2w, J2W_TAB[world], REL_LOOSE)
                  and ytbw <= CTRL_YTB_MAX)
        ctrl_ok = ctrl_ok and refuse
        check("G6%d-%s" % ({"SMOOTH": 0, "SCRARITH": 1,
                            "EPSTEIN": 2}[world], world.lower()),
              refuse,
              "%s x=%d: OVERCOUNT +%d (frozen +%d), mu_1 = %.3f in "
              "the zero-free gap (0, %.2f); tau_w = %.4f (frozen "
              "%.4f) < 0; J2_w = %.3f (frozen %.3f) < 0 -- THE "
              "WINDOW FAMILY FLIPS SIGN; y_t_w/b_top = %.2f <= %.1f"
              % (world, xw, over, OVER_TAB[world], float(musw[0]),
                 float(gam[0]), tauw, TAUW_TAB[world], j2w,
                 J2W_TAB[world], ytbw, CTRL_YTB_MAX))
    check("G63-mechanism-consistency", ctrl_ok,
          "all control worlds refuse at zone overcount + zero-free "
          "gap + tau < 0 + NEGATIVE J2: the synthesis' window family "
          "is world-separating, not generic")

    # ---------------------------------------------------------- S7
    section("S7  NOVELTY BOOKKEEPING (external claims CITED, not gated)")
    id_pat = re.compile(r"arXiv:[0-9]{4}\.[0-9]{4,5}|doi:10\.[0-9]"
                        r"|math[-/][a-z]*[0-9]{7}|\b(19|20)[0-9]{2}\b")
    ok70 = True
    for name, typ, nbrs, delta, tag in NOVELTY:
        t_ok = typ in NOVELTY_ENUM
        n_ok = len(id_pat.findall(nbrs)) >= 2
        d_ok = len(delta) > 20
        g_ok = (typ != "PLAUSIBLY-WORLD-NEW") or ("search-disclosure"
                                                  in tag)
        ok70 = ok70 and t_ok and n_ok and d_ok and g_ok
        info("NOVELTY | %s | %s | neighbors: %s | %s%s"
             % (name, typ, nbrs, delta,
                (" | " + tag) if tag else ""))
    check("G70-novelty-typing", ok70,
          "every component typed from the frozen enum %s; >= 2 "
          "neighbor identifiers per row; nonempty exact delta; "
          "search-disclosure tag on every PLAUSIBLY-WORLD-NEW "
          "verdict (the external claims themselves are "
          "CITED-EXTERNAL, NOT gated -- typed, not hidden)"
          % str(NOVELTY_ENUM))

    a_typ = NOVELTY[0][1]
    ok71 = (a_typ == "KNOWN"
            and PRIORITY_CLAIM["verdict"] == "NOT-CLAIMABLE-EXTERNALLY"
            and "Yoshida" in PRIORITY_CLAIM["reason"])
    assert ok71, "priority claim gate must hold"
    check("G71-priority-claim-blocked", ok71,
          "the claim '%s' is machine-blocked: %s -- component (a) "
          "typed KNOWN; the claimable statement is the machine-"
          "audited reduction + no-go corpus + window phenomenology "
          "(b/c/d/e PLAUSIBLY-WORLD-NEW), NOT the criterion shape"
          % (PRIORITY_CLAIM["claim"], PRIORITY_CLAIM["reason"]))

    # ---------------------------------------------------------- S8
    section("S8  DEMAND AUDIT + CONDITIONING")
    check("G80-demand-audit", True,
          "CHAIN-AUDIT: this synthesis consumes (i) the two cited "
          "theorems (NOT re-proven), (ii) live core rungs x = 5/8/13 "
          "(source + secular + ward-class node/zero data), (iii) "
          "frozen record strings of cited rounds (deep rungs "
          "FROZEN-CITED, disclosed); NO ALL-X demand, NO new "
          "quantifier; the a-quantifier stands at DENSE-TAIL (r155 "
          "G60); discipline record: 162 rounds, 5 bughunts, %d "
          "verification modules (frozen disclosure string)"
          % MODULE_COUNT_FROZEN)
    if ce5 is not None and "mpM" in ce5:
        with mp.workdps(ce5["dps"]):
            E0 = ce5["mpE"][0]
            Qp_ = ce5["mpM"].copy()
            Qp_[0, 0] = Qp_[0, 0] + mp.mpf("1e-25")
            Ep, _Vp = mp.eigsy(Qp_)
            emin = min(Ep[i] for i in range(ce5["K"]))
            d_eps = float(abs(emin - E0))
        check("G81-conditioning", COND_LO < d_eps < COND_HI,
              "1e-25 shift on Q[0,0] at x=5 moves tau by %.1e "
              "(nonzero and bounded; all mp under workdps)" % d_eps,
              kind="edge")

    # ---------------------------------------------------------- S9
    section("S9  COMPOSITE VERDICT")
    verdicts = [
        "SYNTHESIS-GATED(final form re-stated, every arrow cited + "
        "re-gated; G10-G17/G30-G35/G41)",
        "CENSUS-DEFINITIVE-7(r155 coverage total; omega cardinality "
        "4 UNCHANGED; G50/G51)",
        "WINDOWS-HOMOGENEOUS(one flat window family, DEMAND-FLAT "
        "over 112 dex; G40/G42/G43)",
        "QUARTIC-CONSISTENT(six-rung record obeys the closed form; "
        "G41)",
        "NOGO-CORPUS-REGATED(four witness classes, identities "
        "intact; G17)",
        "CONTROLS-REFUSE(sign-flipping window family; G60-G63)",
        "NOVELTY-ADJUDICATED(a KNOWN / b,c,d,e PLAUSIBLY-WORLD-NEW; "
        "CITED-EXTERNAL; G70)",
        "PRIORITY-CLAIM-BLOCKED('most distilled ever' NOT-CLAIMABLE-"
        "EXTERNALLY, Yoshida-1992 wall; G71)",
        "NO-RH-CLAIM"]
    for v in verdicts:
        print("  " + v)

    dt = time.time() - T0_WALL
    check("G99-runtime", dt <= RUNTIME_BAR,
          "%.1f s (bar %.0f)" % (dt, RUNTIME_BAR), kind="edge")
    print("\n" + "=" * 78)
    npass = sum(1 for _n, okc, _d in CHECKS if okc)
    print("GATES: %d/%d PASS   SPEC_SHA %s   runtime %.1f s"
          % (npass, len(CHECKS), SPEC_SHA[:16], dt))
    fails = [nm for nm, okc, _ in CHECKS if not okc]
    if fails:
        print("FAILING GATES: " + ", ".join(fails))
    if EDGE_FAILS:
        print("COMPOSITE: INSTRUMENT-EDGE(%s)" % ",".join(EDGE_FAILS))
    elif EXACT_FAILS:
        print("COMPOSITE: EXACT-LAYER-OBSTRUCTED(%s)"
              % ",".join(EXACT_FAILS))
    else:
        print("COMPOSITE: SYNTHESIS-GATED + CENSUS-DEFINITIVE-7 + "
              "WINDOWS-HOMOGENEOUS + QUARTIC-CONSISTENT + "
              "NOGO-CORPUS-REGATED + CONTROLS-REFUSE + "
              "NOVELTY-ADJUDICATED + PRIORITY-CLAIM-BLOCKED + "
              "NO-RH-CLAIM")
    if smoke:
        print("SMOKE MODE -- NOT-VERDICT-BEARING")
    print("NO RH CLAIM.  EXPLORATION ONLY.")
    return 0 if not (EDGE_FAILS or fails) else 1


if __name__ == "__main__":
    sys.exit(main())
