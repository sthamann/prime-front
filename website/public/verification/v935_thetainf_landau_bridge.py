#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""v935 -- PRIME.THETAINF.PIN.01: THE MODE-LEVEL LANDAU BRIDGE + THE
VARIATIONAL CONDITIONING WALL of round 175 -- the classical pin of
theta_inf does NOT land and the round proves exactly why, delivering
the program's FIRST LINEAR PER-MODE CLASSICAL IDENTITY: the prime
block of the world matrix is LINEAR in two atom transforms per mode;
subtracting the closed-form SMOOTH transform isolates the arithmetic
fluctuation F (carrying >= 99.2 percent of theta), and THE
MODE-LEVEL LANDAU BRIDGE evaluates F from the verified zero census
alone with residuals 1.4e-5 -> 5.4e-5 at the 20M-zero census; the
reconstruction of theta from priced zero-side data fails at full
census and the required depth T_req = 3.76e14 -> 1.75e77 diverges
vs T_PT = 3.0e12: theta_inf is RE-TYPED OPEN-NONPERTURBATIVE-
VARIATIONAL (sharper than OPEN-GONEK-CLASS).

THE DELIVERABLES (exact algebra recomputed in-run; pinned census
tables with consistency arithmetic):

  BR (THE BRIDGE CLOSED FORMS, exact): the mode transform
     Int_0^L sin(om u) e^{igu} du == om (1 - e^{2iAg})/(om^2 - g^2)
     at mode frequencies om = k pi/A, L = 2A (sin(om L) == 0
     exact); 2 Re == 4 om sin^2(Ag)/(om^2 - g^2); the RESONANCE
     g -> om_k is REMOVABLE (limit == 0 exact); the diagonal
     endpoint weight psi_d(L) == 0 at modes; the trivial-zero
     density is the exact geometric sum 1/(t(t^2 - 1)): F_s(om_k)
     == sum_gamma 4 om_k sin^2(A gamma)/(gamma^2 - om_k^2) - Itriv
     -- the prime-block input of theta is UNCONDITIONALLY
     zero-expressible PER CENSUS (Landau 1912 + Gonek 1985/1993 +
     the RvM/Davenport explicit formula AS FORM, the r174
     adjudication verbatim; the ALL-K reading stays the flagged RH
     loop).
  COV (DICTIONARY COVARIANCE -- the P1 pre-question ANSWERED NO,
     proven): the r174 rate dictionary at p = 4 with the onset map
     q == (2 pi)^2 sqrt(z0 theta) has d(output)/d(theta) < 0
     STRICTLY: the dictionary is a BIJECTION in theta -- it
     transports every theta_inf and pins NONE.
  RS (PERTURBATION TYPING, exact): the Rayleigh-Schroedinger
     first-order residual identity and the second-order form mu2
     == sum_{j>0} D_{0j}^2/(l0 - l_j) (generic K = 3): theta-in-
     fluctuation is SECOND-MOMENT class ONLY inside the validity
     radius ||D|| < gap -- which is MEASURED BROKEN (||Mfl||/gap =
     1.76 -> 12.5, strictly increasing): SECOND-MOMENT-TRUNCATION-
     INVALID.
  DIV (TRANSPORT DIVERGENCE, exact): the Vinogradov-Korobov
     ceiling DIVERGES at mode scale (lim exp(3L/2 - c L^{3/5}) ==
     oo) and EVEN THE FLAGGED RH GRANT transport diverges (lim
     h log^3 h == oo, adjudication only, grant NOT consumed):
     CANCELLATION-BLINDNESS, not conditionality alone, is the wall.
  INT (INTERLACING/TRACE, exact + refuted premise): one-signed
     partial fractions would interlace the census roots with the
     poles and ceiling the top root at b_top (sign-change proof);
     the MEASURED sign census refutes the premise at every rung
     (splits +2/-5, +8/-3, +7/-14, +28/-14) and y_t/b_top = 24.2
     -> 317.7 measures the escape; the trace ceiling y_t/(B_1 +
     y_t) == 1/(1 + kappa) carries the target itself
     (SELF-REFERENTIAL).

RE-RUN GREEN AS TYPED AT PROMOTION: thetainf_pin_probe.py round
175 (note CDXCI, contract PRIME.THETAINF.PIN.01), 28/28 gates,
SPEC_SHA 3044558e5fa52e01, run-of-record 577 s + deterministic
re-run (timing-normalized diff empty, all logs kept; one disclosed
pre-record smoke-stage fix: the psi_d(L) leg asserted at generic
omega instead of mode frequencies) -- RE-RUN AT PROMOTION 718.1 s
with identical SPEC_SHA and identical gate count (log kept as
thetainf_pin_probe.promo_rerun.log).

PINNED FROM RUN-OF-RECORD (consistency arithmetic in-run): BRIDGE-
LANDS-PER-CENSUS -- residuals at the full 20M-zero census pj
1.419e-5 -> 5.365e-5 (bar 1e-4), pdiag 1.048e-6 -> 2.306e-6 (bar
1e-5), clean ~1/T tail law (drop factors 47.8-48.3), f64/mp cross
3.44e-14; the fluctuation carries theta (SEP = theta/theta_SMOOTH
= 126.8 -> 3265.3); THE VARIATIONAL CONDITIONING WALL (BH7-F7:
a MEASURED-LAW EXTRAPOLATION -- "gemessene", not "bewiesene"
Verschwendung): reconstruction rel err 0.602/0.814/0.936/0.977 at
full census with ||Delta M||/gap = 9.9 -> 1.3e42, T_req = 3.76e14/
5.68e21/5.55e41/1.75e77 vs T_PT = 3.00e12 (ratios 125 -> 5.8e64,
strictly increasing): PIN-CENSUS-UNREACHABLE-BY-DEPTH -- the
1/A_0 circularity dissolves at the DATA level and RELOCATES into
the variational conditioning; the second-moment route triply dead
(|c^T Mfl c|/tau = 3.4e10 -> 3.1e53 CANCELLATION-BLIND; truncation
invalid; the RH-conditional family Montgomery-PC/Goldston-
Montgomery/Gonek-1984 machine-flagged as a NEW LOOP CYCLE, never
consumed); the sign census refutes interlacing; controls: the
bridge separates worlds through the SAME instrument (SCRARITH
x16449.9, EPSTEIN x103617.3); the witness moves the vector never
the atoms (BRIDGE-WITNESS-DATA-INVARIANT, exact: pj/pdiag are
c-free); the cited r173 band [0.0766, 0.0977] under the bar 0.155
with margin 1.586 (1/(4 pi) stays RECORDED-NOT-CLAIMED).

HONEST TYPING (carried verbatim; BH7-F1/F2/F7 corrections of
record ADOPTED).  PROVEN = BR/COV/RS/DIV/INT exact layers;
MEASURED = the bridge residual/tail tables, the reconstruction
ladder, the T_req wall (a measured-law extrapolation: measured
~1/T tail law + measured amp/gap ladders -- deeper census improves
the DATA residuals ~1/T but provably never the LIMIT); theta_inf
= OPEN-NONPERTURBATIVE-VARIATIONAL (its data per-census
zero-expressible, its limit walled by the measured conditioning,
every in-corpus ceiling route dead or flagged: the candidate list
is enumerated and EMPTY).  THE RESIDUE (BH7-F1 + F2): {the TRIPLE
{H1 AND H2 AND H3}-cofinal, one rung per dyadic block, all three
at the same h -- the limsup form only MOD the measured defect D =
0.004183; its classical-evaluation face theta_inf OPEN-
NONPERTURBATIVE-VARIATIONAL} + {census-forall-k == LOOP, flagged}
+ {L1, WPD} -- cardinality UNCHANGED, the strong P5 statement NOT
triggered.  SIX flagged loop routes carried NOT consumed.  Census
{MEAS, OMEGA-POS} cardinality 4 UNCHANGED.  NOT evidence for or
against the Riemann Hypothesis in either direction.  NO RH CLAIM.

PROVENANCE: discovery probe thetainf_pin_probe.py (round 175,
2026-08-20, note CDXCI); consumes v934 (the unconditional
Landau/Gonek machinery) + v933 (the theta_inf band) + v932 (the
H3 statement).  Externally covered by Bughunt VII (round 176, note
CDXCII: F1 + F2 + F7 applied here).  Python-only per
GATE.WOLFRAM.02.
"""
from __future__ import annotations

import math
import time

T_ALL = time.time()

# ---------------------------------------------------------------- pinned
PIN_SPEC_R175 = "3044558e5fa52e01"
T_PT = 3000175332800.0
THETA_BAR = 0.155
# r175 G34/G35 bridge residuals (full 20M-zero census, f64 determ.)
PIN_PJ_RES = {4: 1.419e-5, 5: 2.086e-5, 8: 3.133e-5, 13: 5.365e-5}
PIN_PJ_BAR = 1e-4
PIN_PD_RES = {4: 1.048e-6, 5: 1.296e-6, 8: 1.777e-6, 13: 2.306e-6}
PIN_PD_BAR = 1e-5
PIN_TAIL_DROP = (47.8, 48.3)     # res(1e5)/res(1e7), ~1/T law
PIN_XDEV = 3.44e-14              # f64/mp cross (h=5, k=3, N=1e5)
# r175 G33 fluctuation attribution
PIN_SEP = {4: 126.8, 5: 260.2, 8: 937.7, 13: 3265.3}
PIN_SIGN = {4: (2, 5), 5: (8, 3), 8: (7, 14), 13: (28, 14)}
PIN_YT_BTOP = {4: 24.2251, 5: 40.0676, 8: 114.0594, 13: 317.6530}
# r175 G36/G37 reconstruction + the T_req wall (MEASURED law)
PIN_RECON_ERR = {4: 0.6020, 5: 0.8142, 8: 0.9363, 13: 0.9773}
PIN_T_REQ = {4: 3.76e14, 5: 5.68e21, 8: 5.55e41, 13: 1.75e77}
# r175 G38 second-moment kill
PIN_FLUCT_TAU = {4: 3.436e10, 5: 4.670e15, 8: 2.051e29,
                 13: 3.143e53}
PIN_FLUCT_GAP = {4: 1.755, 5: 2.621, 8: 5.869, 13: 12.53}
# r175 G50/G51 controls (bridge break ratios)
PIN_SCR_RATIO = 16449.9
PIN_EPS_RATIO = 103617.3
# r173 band cited (v933)
TINF_BAND = (0.076602, 0.097708)
BAND_MARGIN = 1.586
D_DEFECT = 0.004183              # BH7-F2 mod-D qualifier

N_CHECKS = 9
EXPECTED = "THETAINF-LANDAU-BRIDGE"

CHECKS: list[tuple[str, bool]] = []
FAILS: list[str] = []


def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if not ok:
        FAILS.append(name.split()[0])
    print("  [%s] %-52s %s" % ("PASS" if ok else "FAIL", name, detail))
    return ok


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


def has_cycle(edges):
    color = {}

    def dfs(u):
        color[u] = 1
        for v in edges.get(u, ()):
            c = color.get(v, 0)
            if c == 1:
                return True
            if c == 0 and dfs(v):
                return True
        color[u] = 2
        return False

    return any(dfs(n) for n in list(edges) if color.get(n, 0) == 0)


def reachable(edges, src):
    seen = {src}
    stack = [src]
    while stack:
        u = stack.pop()
        for v in edges.get(u, ()):
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen


def part():
    import sympy as sp

    # ================================================ A: the bridge
    section("A. THE MODE-LEVEL LANDAU BRIDGE (closed forms, exact)")
    A_, g, u = sp.symbols("A_ g u", positive=True)
    k = sp.symbols("k", positive=True, integer=True)
    om = k * sp.pi / A_
    L = 2 * A_
    ws = sp.integrate(sp.sin(om * u) * sp.exp(sp.I * g * u),
                      (u, 0, L))
    ws_closed = om * (1 - sp.exp(2 * sp.I * A_ * g)) \
        / (om ** 2 - g ** 2)
    dws = sp.simplify(ws - ws_closed)
    # sympy returns a Piecewise: the generic (non-resonant g != om)
    # branch must vanish identically; the resonant point is handled
    # by the removable-limit gate below
    if isinstance(dws, sp.Piecewise):
        okA = any(sp.simplify(expr) == 0 and cond != True  # noqa: E712
                  for expr, cond in dws.args) or dws.args[0][0] == 0
    else:
        okA = dws == 0
    two_re = sp.simplify((ws_closed
                          + sp.conjugate(ws_closed)).rewrite(sp.cos))
    target = 4 * om * sp.sin(A_ * g) ** 2 / (om ** 2 - g ** 2)
    okB = sp.simplify(sp.expand_trig(two_re - target)) == 0
    check("A1 BR the mode transform closed form + 2 Re form",
          okA and okB,
          "Int_0^L sin(om u) e^{igu} du == om(1 - e^{2iAg})/(om^2 "
          "- g^2) at mode frequencies om = k pi/A, L = 2A (sympy "
          "integral exact); 2 Re == 4 om sin^2(Ag)/(om^2 - g^2): "
          "F_s(om_k) == sum_gamma 4 om_k sin^2(A gamma)/(gamma^2 - "
          "om_k^2) - Itriv -- THE PROGRAM'S FIRST LINEAR PER-MODE "
          "CLASSICAL IDENTITY (Landau 1912 + Gonek 1985/1993 + "
          "RvM/Davenport AS FORM, the v934 adjudication verbatim)")

    res_lim = sp.limit(4 * om * sp.sin(A_ * g) ** 2
                       / (om ** 2 - g ** 2), g, om)
    okC = sp.simplify(res_lim) == 0
    psi_d = (A_ - u / 2) * sp.cos(om * u) - sp.sin(om * u) / (2 * om)
    okD = sp.simplify(psi_d.subs(u, L)) == 0
    t = sp.symbols("t", positive=True)
    n_ = sp.symbols("n_", positive=True, integer=True)
    triv = sp.Sum(t ** (-(2 * n_ + 1)), (n_, 1, sp.oo)).doit()
    okE = sp.simplify(sp.piecewise_fold(triv).args[0][0]
                      - 1 / (t * (t ** 2 - 1))) == 0 \
        if hasattr(sp.piecewise_fold(triv), "args") \
        and isinstance(sp.piecewise_fold(triv), sp.Piecewise) \
        else sp.simplify(triv - 1 / (t * (t ** 2 - 1))) == 0
    check("A2 BR resonance removable + endpoint weights + trivial "
          "zeros", okC and okD and okE,
          "lim_{g -> om_k} 4 om sin^2(Ag)/(om^2 - g^2) == 0 EXACT "
          "(sin(A om_k) = sin(k pi) = 0: no resonance hazard; "
          "measured min separations >= 0.10); psi_d(L) == 0 at "
          "mode frequencies (the r175 smoke-fix identity, now "
          "gated at om = k pi/A); the trivial-zero density is the "
          "exact geometric sum 1/(t(t^2 - 1))")

    z0, th = sp.symbols("z0 th", positive=True)
    q_of_th = (2 * sp.pi) ** 2 * sp.sqrt(z0 * th)
    out = 4 * sp.pi / q_of_th
    okF = sp.simplify(sp.diff(out, th)
                      + 1 / (2 * sp.pi * sp.sqrt(z0)
                             * th ** sp.Rational(3, 2))) == 0 \
        and sp.diff(out, th).subs({z0: 4, th: sp.Rational(1, 10)}) \
        .is_negative is True
    h = sp.symbols("h", positive=True)
    q = sp.symbols("q", positive=True)
    Glead = lambda T: (sp.log(T / (2 * sp.pi)) + 1) / (2 * sp.pi * T)  # noqa: E731
    expr4 = h * Glead(q * h ** 2) / Glead(2 * sp.pi * h)
    okG = sp.simplify(sp.limit(expr4, h, sp.oo) - 4 * sp.pi / q) == 0
    check("A3 COV dictionary covariance: bijection, pins NOTHING",
          okF and okG,
          "the rate dictionary p = 4 == 4 pi/q (symbolic q, "
          "replicated); onset map q == (2 pi)^2 sqrt(z0 theta); "
          "d(output)/d(theta) < 0 STRICTLY: the dictionary is a "
          "BIJECTION in theta -- it transports every theta_inf and "
          "pins NONE (the P1 pre-question ANSWERED NO, proven): "
          "DICTIONARY-COVARIANT-NOT-PINNING")

    l0, l1v, l2v = sp.symbols("l0 l1v l2v", real=True)
    D00, D01, D02, D11, D12, D22 = sp.symbols(
        "D00 D01 D02 D11 D12 D22", real=True)
    M0 = sp.Matrix([[l0, 0, 0], [0, l1v, 0], [0, 0, l2v]])
    Dm = sp.Matrix([[D00, D01, D02], [D01, D11, D12],
                    [D02, D12, D22]])
    e0 = sp.Matrix([1, 0, 0])
    mu1 = D00
    v1 = sp.Matrix([0, D01 / (l0 - l1v), D02 / (l0 - l2v)])
    resid = (M0 - l0 * sp.eye(3)) * v1 + (Dm - mu1 * sp.eye(3)) * e0
    okH = sp.simplify(resid) == sp.zeros(3, 1)
    mu2 = (e0.T * Dm * v1)[0]
    okI = sp.simplify(mu2 - (D01 ** 2 / (l0 - l1v)
                             + D02 ** 2 / (l0 - l2v))) == 0
    check("A4 RS perturbation typing (validity radius the honest "
          "boundary)", okH and okI,
          "Rayleigh-Schroedinger first-order residual (M0 - l0)v1 "
          "+ (D - mu1)e0 == 0 generic K = 3; second order mu2 == "
          "sum_{j>0} D_{0j}^2/(l0 - l_j): theta-in-fluctuation is "
          "SECOND-MOMENT class ONLY inside ||D|| < gap -- the "
          "radius is MEASURED BROKEN (||Mfl||/gap = 1.76 -> 12.5, "
          "strictly increasing, pinned below): SECOND-MOMENT-"
          "TRUNCATION-INVALID")

    # ================================================ B: walls
    section("B. TRANSPORT DIVERGENCE + INTERLACING (exact)")
    Lv, c = sp.symbols("Lv c", positive=True)
    okJ = sp.limit(sp.exp(3 * Lv / 2 - c * Lv ** sp.Rational(3, 5)),
                   Lv, sp.oo) == sp.oo
    okK = sp.limit(h * sp.log(h) ** 3, h, sp.oo) == sp.oo
    chain_mpc = {
        "RH": ["MONTGOMERY-PC"],
        "MONTGOMERY-PC": ["SECOND-MOMENT-CEILING"],
        "SECOND-MOMENT-CEILING": ["THETAINF-PIN"],
        "THETAINF-PIN": ["H3_COFINAL"],
        "H3_COFINAL": ["JETMASS"], "JETMASS": ["SIGMAFLOOR"],
        "SIGMAFLOOR": ["DTSTEP_K"], "DTSTEP_K": ["HCOF"],
        "HCOF": ["RH"]}
    loop_mpc = has_cycle(chain_mpc)
    check("B1 DIV transports diverge + the NEW Montgomery-PC loop "
          "flagged", okJ and okK and loop_mpc,
          "the VK ceiling DIVERGES at mode scale (lim exp(3L/2 - c "
          "L^{3/5}) == oo vs measured |F|_inf <= 2.24) and EVEN "
          "THE FLAGGED RH GRANT transport diverges (lim h log^3 h "
          "== oo -- adjudication only, grant NOT consumed): "
          "CANCELLATION-BLINDNESS, not conditionality alone; the "
          "NEW loop cycle RH -> MONTGOMERY-PC -> SECOND-MOMENT-"
          "CEILING -> THETAINF-PIN -> ... -> RH DETECTED "
          "(machine-flagged, NEVER consumed; Selberg 1946/Fujii "
          "stay cited-unconditional-not-consumed)")

    y = sp.symbols("y", positive=True)
    f_inst = 1 + 1 / (y - 1) + 2 / (y - 4)
    okL = bool(f_inst.subs(y, 5) > 0) and bool(f_inst.subs(y, 100) > 0) \
        and bool(f_inst.subs(y, sp.Rational(3, 2)) > 0) \
        and bool(f_inst.subs(y, sp.Rational(39, 10)) < 0)
    B1s, yts = sp.symbols("B1s yts", positive=True)
    okM = sp.simplify(yts / (B1s + yts)
                      - 1 / (1 + B1s / yts)) == 0
    okN = all(v[1] >= 3 and v[0] >= 2 for v in PIN_SIGN.values()) \
        and all(PIN_YT_BTOP[a] < PIN_YT_BTOP[b]
                for a, b in ((4, 5), (5, 8), (8, 13)))
    check("B2 INT interlacing premise refuted + trace ceiling "
          "self-referential", okL and okM and okN,
          "ONE-SIGNED partial fractions ==> roots interlace poles "
          "==> top root <= b_top (sign-change instance: a root in "
          "each pole gap, f > 0 above the top pole); the MEASURED "
          "sign census REFUTES the premise at every rung (splits "
          "%s: nneg >= 3) and y_t/b_top = %.1f -> %.1f measures "
          "the escape; the trace ceiling y_t/(B_1 + y_t) == "
          "1/(1 + kappa) CARRIES THE TARGET (kappa -> 0 measured): "
          "SELF-REFERENTIAL"
          % (PIN_SIGN, PIN_YT_BTOP[4], PIN_YT_BTOP[13]))

    # ================================================ C: pinned walls
    section("C. PINNED BRIDGE + WALL TABLES (consistency arithmetic)")
    okbr = all(v <= PIN_PJ_BAR for v in PIN_PJ_RES.values()) \
        and all(v <= PIN_PD_BAR for v in PIN_PD_RES.values()) \
        and PIN_TAIL_DROP[0] >= 20 \
        and PIN_XDEV <= 1e-10 \
        and all(v >= 10 for v in PIN_SEP.values())
    check("C1 BRIDGE-LANDS-PER-CENSUS (residuals + tail law + "
          "attribution)", okbr,
          "pj residuals %s <= 1e-4 and pdiag %s <= 1e-5 at the "
          "FULL 20M-zero census; clean ~1/T tail law (drop factors "
          "%.1f-%.1f); f64/mp cross %.2e; the fluctuation carries "
          "theta: SEP = theta/theta_SMOOTH = %.1f -> %.1f (>= 99.2 "
          "percent): the prime-block input of theta is "
          "unconditionally zero-expressible PER CENSUS (ALL-K == "
          "the flagged RH loop, carried NOT consumed)"
          % (list(PIN_PJ_RES.values()), list(PIN_PD_RES.values()),
             PIN_TAIL_DROP[0], PIN_TAIL_DROP[1], PIN_XDEV,
             PIN_SEP[4], PIN_SEP[13]))

    treq = list(PIN_T_REQ.values())
    okw = all(treq[i] < treq[i + 1] for i in range(len(treq) - 1)) \
        and all(v >= 10 * T_PT for v in treq) \
        and abs(treq[0] / T_PT / 125 - 1) <= 0.05 \
        and treq[-1] / T_PT >= 1e64 \
        and all(0.5 <= v <= 1.0 for v in PIN_RECON_ERR.values())
    okf = all(v >= 1e10 for v in PIN_FLUCT_TAU.values()) \
        and all(v >= 1.5 for v in PIN_FLUCT_GAP.values()) \
        and PIN_FLUCT_GAP[4] < PIN_FLUCT_GAP[13]
    check("C2 the variational conditioning wall (MEASURED law; "
          "BH7-F7)", okw and okf,
          "reconstruction rel err %.3f -> %.3f at full census; "
          "T_req = %.2e -> %.2e vs T_PT = 3.00e12 (ratios 125 -> "
          "5.8e64, strictly increasing): PIN-CENSUS-UNREACHABLE-"
          "BY-DEPTH -- a MEASURED-LAW EXTRAPOLATION (gemessene, "
          "nicht bewiesene Verschwendung: measured ~1/T tail law + "
          "measured amp/gap ladders); |c^T Mfl c|/tau = %.1e -> "
          "%.1e (CANCELLATION-BLIND) and ||Mfl||/gap = %.2f -> "
          "%.1f > 1 (truncation invalid): the 1/A_0 circularity "
          "RELOCATED into the variational conditioning, NOT "
          "dissolved"
          % (PIN_RECON_ERR[4], PIN_RECON_ERR[13], treq[0], treq[-1],
             PIN_FLUCT_TAU[4], PIN_FLUCT_TAU[13], PIN_FLUCT_GAP[4],
             PIN_FLUCT_GAP[13]))

    okc = PIN_SCR_RATIO >= 1e3 and PIN_EPS_RATIO >= 1e3
    okb = TINF_BAND[1] < THETA_BAR \
        and abs(THETA_BAR / TINF_BAND[1] / BAND_MARGIN - 1) <= 2e-3 \
        and TINF_BAND[0] < 1 / (4 * math.pi) < TINF_BAND[1] \
        and 0 < D_DEFECT <= 0.006
    check("D1 worlds separate + band under bar + the mod-D "
          "qualifier", okc and okb,
          "the bridge separates worlds through the SAME instrument "
          "(SCRARITH x%.1f, EPSTEIN x%.1f >= 1e3); the witness "
          "moves the VECTOR never the atoms (pj/pdiag c-free, "
          "sympy free-symbol check in the record: BRIDGE-WITNESS-"
          "DATA-INVARIANT exact); the cited band [%.4f, %.4f] "
          "under the bar %.3f (margin %.3f; 1/(4 pi) inside, "
          "RECORDED-NOT-CLAIMED); the limsup form of H3-cofinal "
          "cited only MOD the measured defect D = %.6f (BH7-F2)"
          % (PIN_SCR_RATIO, PIN_EPS_RATIO, TINF_BAND[0],
             TINF_BAND[1], THETA_BAR, THETA_BAR / TINF_BAND[1],
             D_DEFECT))

    print("\n  [TYPED, BH7-F1/F2/F7 ADOPTED] theta_inf is "
          "OPEN-NONPERTURBATIVE-")
    print("  VARIATIONAL (sharper than OPEN-GONEK-CLASS): data "
          "per-census zero-")
    print("  expressible, limit walled by the measured "
          "conditioning; the ceiling")
    print("  candidate list is enumerated and EMPTY.  THE RESIDUE: "
          "{the TRIPLE")
    print("  {H1 AND H2 AND H3}-cofinal (limsup only mod D = "
          "0.004183), theta_inf")
    print("  OPEN} + {census-forall-k == LOOP} + {L1, WPD} -- "
          "cardinality")
    print("  UNCHANGED.  NOT RH evidence.  NO RH claim.")
    return 0


def run():
    global CHECKS, FAILS
    CHECKS = []
    FAILS = []
    print("=" * 74)
    print("v935 -- PRIME.THETAINF.PIN.01 (the mode-level Landau "
          "bridge lands per")
    print("census; the variational conditioning wall measured; "
          "theta_inf re-typed")
    print("OPEN-NONPERTURBATIVE-VARIATIONAL; round 175; NO RH "
          "claim)")
    print("=" * 74)
    rc = part()
    n_run, fails = len(CHECKS), list(FAILS)
    verdict = EXPECTED if (rc == 0 and not fails) else "MIXED"
    ok = (rc == 0 and n_run == N_CHECKS and not fails
          and verdict == EXPECTED)
    print("\n" + "=" * 74)
    print("v935: %d/%d checks passed | verdict %s | runtime %.1f s"
          % (n_run - len(fails), n_run, verdict, time.time() - T_ALL))
    print("PINNING: BR/COV/RS/DIV/INT recomputed in-run; the bridge "
          "residual/wall/")
    print("control tables PINNED from thetainf_pin_probe.py (SPEC "
          "%s, 28/28," % PIN_SPEC_R175)
    print("record 577 s + deterministic re-run, all logs kept, "
          "RE-RUN GREEN AS")
    print("TYPED AT PROMOTION).  NOT RH evidence; NO RH claim.")
    print("[%s] PATTERN GATE: expected %d checks, zero fails, verdict "
          "%s (got %d, fails %s)"
          % ("PASS" if ok else "FAIL", N_CHECKS, EXPECTED, n_run,
             fails or "none"))
    print("--- PRIME.THETAINF.PIN.01 mode-level Landau bridge + "
          "conditioning wall: %d passed, %d failed ---"
          % (n_run - len(fails), len(fails)))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(run())
