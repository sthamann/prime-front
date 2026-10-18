#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""chiral_phase_probe -- E8.DIVISOR210.CHIRAL_PHASE.01: deciding
the family-cycle chirality of the 210 register by the phase
readout, blind.

EXPLORATION ONLY (experiments/): no ledger row, no paper edit, no
.md, nothing outside experiments/.  NO RH claim.  Frozen (spec +
sha256) before running.

THE FREEDOM TO DECIDE (divisor210_canonicity_probe, read-only,
verdict DIVISOR210-GAUGE-FAMILY(2)): after the Euler pin and the
ramification anchor filter, exactly TWO gauge classes survive --
(F1,F2,F3,A) -> (3,5,7,2) [chi+] and (3,7,5,2) [chi-]: the CYCLIC
ORIENTATION of {3,5,7} along the family cycle sigma.  The phase
readout (weyl_readout_repair_probe, readout C: total phase
variation -- orientation-sensitive, strongly discriminating) is
the candidate decider.

FROZEN PROTOCOL (2026-08-08, frozen + SHA-hashed before first
run; ALL decision rules frozen here, BEFORE any evaluation):

 S1  CENSUS REGRESSION (bit model; the heavy lattice/refinement
     regressions live in the canonicity probe, cited): sigma
     (f1,f2,f3,a) -> (f3,f1,f2,a); q* = wt(iota)/2 mod 2 (the
     v845 lift identity, cited); unique anchor (sigma-fixed,
     q*=1) = A; admissible bases 6 ordered / 2 axis sets, weld-
     compatible 3 / 1; R3 (anchor -> 2) survivors modulo the
     weld gauge C3 = <sigma> (G3 from the canonicity run, cited)
     = EXACTLY the two classes chi+ = (3,5,7,2), chi- =
     (3,7,5,2).  Any fail => CENSUS-BROKEN.

 S2  READOUT REGRESSIONS (dw/wr read-only): the v1 extremal ref
     s_min(kz9, a, r2) = 8.68463e-01 +- 1e-5; Herglotz Im m > 0
     and passivity |r| < 1 on ZFIX, the spectral grid and the
     phase window; my inline total-phase-variation == the repair
     probe's readouts()["s_C"] to 1e-12 (the readout is the
     deployed one).  Any fail => READOUT-BROKEN.

 S3  THE BLINDNESS WARD (structural, must FIRE): the sigma-LESS
     chirality machines U0_chi(tau) = WH diag(i^wt)
     diag(d_chi^{-i tau/2}) are exactly conjugate under the bit
     transposition Pi = (F2 <-> F3), which fixes the vacuum port
     and the parity readout w2 -- so the loaded scalar transfer
     is IDENTICAL for chi+ and chi- (matrix ward <= 1e-13;
     loaded scalars <= 1e-12 on the whole phase window).  ANY
     phase readout that does not couple the family-cycle letter
     sigma to the weights is PROVABLY chirality-blind; the
     decider below therefore wires sigma in.  (Also typed: the
     fixed-sector divisors 1, 2, 105, 210 are chirality-equal.)

 S4  THE DECIDER (frozen decision rules):
     D1 REGISTER ORIENTATION FUNCTIONAL (exact): for each of the
        4 free 3-orbits O with root v0 = min(O) and x_k =
        log d_chi(sigma^k v0), X1(O) = sum_k x_k om^k with om =
        e^{2 pi i/3}; Phi_reg(chi) = sum_O Im(X1^3).  WARDS:
        antisymmetry Phi_reg(chi+) = -Phi_reg(chi-) (rel 1e-12);
        re-rooting (v0 -> sigma v0) invariance (the C3 gauge).
     D2 KMS-ORIENTATION CRITERION (frozen): the deployed modular
        phases are e^{-i w tau/2} with tau >= 0 on the dual grid
        (redheffer design (b)); the KMS-compatible chirality :=
        the one with Phi_reg(chi) > 0 (positive spectral winding
        of the log-weights along the cycle, om = e^{+2 pi i/3}
        paired with tau >= 0).  TYPED HONESTLY: this pairing of
        two sign conventions is a CONVENTION BRIDGE unless the
        machine leg (D3) independently selects the same
        chirality; D2 alone cannot decide.
     D3 MACHINE LEG (the sigma-wired loaded phase readout): the
        chirality machine U_chi(tau) = WH diag(i^wt) P_sigma
        diag(d_chi^{-i tau/2}) (P_sigma = the deployed family
        cycle on labels; the ONLY difference between chi+ and
        chi- is the weight assignment); port = vacuum slot
        (U[0,0] = 1/4, warded); load = the deployed divisor
        tower (kz 9, variant a, dw read-only), r(i y) on the
        frozen window y in YPH (33 points), coupling tau_j = y_j
        (frozen); f_j = w2' Vt_chi(r_j, tau_j) w2;
        Phi_mach(chi, load) = sum_j arg(f_{j+1}/f_j) (signed
        winding), V(chi, load) = sum_j |arg(f_{j+1}/f_j)| (total
        variation).  Loads: truth, Epstein (kn.lambda_eps),
        scramble (frozen LCG seed 12345, dw convention).
        FROZEN DECISION: the machine SEES the chirality iff
        |Phi_mach(chi+) - Phi_mach(chi-)| >= 1e-3 rad on truth;
        disc_ok(chi) iff V(chi, eps)/V(chi, truth) outside
        [1/1.5, 1.5] AND V(chi, scr)/V(chi, truth) outside
        [1/1.5, 1.5]; the machine DECIDES iff exactly one
        chirality has disc_ok; then winner_mach = that
        chirality.
 S5  SCRAMBLED-REGISTER CONTROL (must fire): LCG-permute the 12
     moved divisor values (seed 12345): the lattice
     multiplicativity d(v XOR w) = d(v) d(w) on disjoint
     supports BREAKS (count > 0 violated pairs), and the machine
     readout moves (rel >= 1e-6) -- the decider consumes the
     register structure, not just 12 numbers.

 S6  VERDICT (frozen precedence): CENSUS-BROKEN / READOUT-BROKEN
     / WARD-DEAD (S3 or S5 fails to fire) / then:
     - machine decides AND winner_mach == KMS winner (D2) ->
       CHIRALITY-DECIDED (named winner; criterion: machine
       discrimination + KMS orientation agree);
     - machine decides AND winner_mach != KMS winner ->
       CHIRALITY-INCONSISTENT (typed);
     - machine does not decide (both disc_ok, or neither, or
       the machine does not even see the chirality) ->
       CHIRALITY-DEGENERATE (the freedom is real gauge at the
       deployed-machine level; D2 alone is a convention bridge,
       typed, NOT a decision).

Sources (read-only): divisor210_canonicity_probe (census, cited
counts), divisor_weyl_port_probe (towers, closure blocks, v1
refs), weyl_readout_repair_probe (Load, readouts, YPH, ZFIX),
redheffer_colligation_probe (walsh16, hamw),
krein_normalform_probe (lambda_eps), v845 register conventions.
NO RH claim; report only.

ADDENDUM v2 (typed after run 1; run-1 numbers unchanged, no
decision bar moved -- the amendment REPAIRS a mis-calibrated ward
and TYPES two structural findings the run produced):
 (1) MEASURED STRUCTURAL FACT: Phi_reg vanishes IDENTICALLY (both
     chiralities, to 1e-15).  Mechanism, verified exactly: the
     Moebius complement d -> 210/d pairs the four free orbits
     (weight-1 <-> weight-2 at fixed anchor bit) with REVERSED
     cycle orientation, so X1(O')^3 = -X1(O)^3 per pair and the
     orbit sum cancels for EVERY multiplicative weight
     assignment.  The register carries no intrinsic scalar
     orientation of this type; the D2 KMS criterion is therefore
     VACUOUS (winner undefined), typed.  The v1 antisymmetry
     ward divided by |Phi_reg| ~ 1e-15 and failed on float noise
     although antisymmetry holds trivially; v2 wards: absolute
     antisymmetry |Phi+ + Phi-| <= 1e-12, re-rooting invariance
     absolute <= 1e-12, and the NEW exact complement-cancellation
     ward |X1(O)^3 + X1(O')^3| <= 1e-12 per pair.
 (2) MEASURED STRUCTURAL FACT: the sigma-wired QUADRATIC readout
     is also chirality-blind (|dPhi| ~ 1e-15): w2' M w2 =
     w2' M^T w2 sees only the symmetric part of the machine, and
     cycle reversal is exactly transposition up to the
     Pi-conjugation that fixes port and readout (U_-^sigma =
     Pi (sigma^{-1}-machine) Pi^T, and the transposed machine
     has blocks (A^T, C^T, B^T) whose closure scalar under ONE
     readout vector is identical).  v2 adds the ward for this
     equality and a REPORT-ONLY diagnostic: the asymmetric
     two-vector readout w2' Vt w1 (r2 left, r1 right, both
     deployed) -- measured for chirality response and typed, NOT
     verdict-bearing (post-run diagnostic).
 (3) Verdict logic under a vacuous D2: CHIRALITY-DECIDED would
     require the machine leg to decide alone (named as machine-
     only); with D3 measured blind the verdict is
     CHIRALITY-DEGENERATE either way.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/chiral_phase_probe.py
"""

import ast
import hashlib
import itertools
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

import v563_paper2_readouts as core            # noqa: E402 (READ-ONLY)
import krein_normalform_probe as kn            # noqa: E402 (READ-ONLY)
import redheffer_colligation_probe as rc       # noqa: E402 (READ-ONLY)
import divisor_weyl_port_probe as dw           # noqa: E402 (READ-ONLY)
import weyl_readout_repair_probe as wr         # noqa: E402 (READ-ONLY)

T0 = time.time()
CHECKS = []
KILLS = []

V1_SMIN_REF = 8.68463e-01
SEE_BAR = 1e-3
DISC_FACTOR = 1.5
LCG_SEED = 12345
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")


def check(name, ok, detail="", kill=None):
    CHECKS.append((name, bool(ok)))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n== %s ==  (t=%.1fs)" % (title, time.time() - T0),
          flush=True)


def ast_scan():
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(src)):
        nm = None
        if isinstance(node, ast.Name):
            nm = node.id
        elif isinstance(node, ast.Attribute):
            nm = node.attr
        if nm and nm.lower() in BANNED_IDS:
            bad.append(nm)
    return bad


print("E8.DIVISOR210.CHIRAL_PHASE.01 -- the chirality decider, "
      "blind protocol")
print("FROZEN_SPEC SHA-256: %s"
      % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
print("\nS0 -- firewall")
check("S0.1 AST firewall clean (no zero/prime oracles)",
      not ast_scan())

# ======================================================================
section("S1: census regression -- the two gauge classes")
# ======================================================================
W16 = [tuple(b) for b in itertools.product((0, 1), repeat=4)]
WIDX = {w: i for i, w in enumerate(W16)}
Z4 = (0, 0, 0, 0)


def sig_bits(v):
    return (v[2], v[0], v[1], v[3])


def x2(u, w):
    return tuple((a + b) % 2 for a, b in zip(u, w))


def qstar(v):
    f1, f2, f3, a = v
    io = (f1, f2, f3, a, (f1 + f2 + f3 + a) % 2)
    return (sum(io) // 2) % 2


GJI = [[0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 0]]


def hb(v, w):
    return sum(v[i] * GJI[i][j] * w[j] for i in range(4)
               for j in range(4)) % 2


anchors = [w for w in W16 if w != Z4 and sig_bits(w) == w
           and qstar(w) == 1]
A_BIT = (0, 0, 0, 1)
check("S1.1 unique anchor (sigma-fixed, q* = 1): %s == [(0,0,0,1)]"
      % anchors, anchors == [A_BIT], kill="CENSUS-BROKEN")

FREE12 = [w for w in W16 if w != Z4 and sig_bits(w) != w]
ADM = []
for X1 in FREE12:
    X2b, X3b = sig_bits(X1), sig_bits(sig_bits(X1))
    span3 = set()
    for e in itertools.product((0, 1), repeat=3):
        vv = Z4
        for c, xx in zip(e, (X1, X2b, X3b)):
            if c:
                vv = x2(vv, xx)
        span3.add(vv)
    if len(span3) != 8 or A_BIT in span3:
        continue
    bb = (X1, X2b, X3b, A_BIT)
    if [[hb(u, w) for w in bb] for u in bb] != GJI:
        continue
    if qstar(x2(x2(X1, X2b), X3b)) != 0:
        continue
    ADM.append(bb)


def coords_map(bb):
    out = {}
    for e in itertools.product((0, 1), repeat=4):
        vv = Z4
        for c, xx in zip(e, bb):
            if c:
                vv = x2(vv, xx)
        out[vv] = e
    return out


WELD = [bb for bb in ADM
        if all(sum(coords_map(bb)[w]) == sum(w) for w in W16)]
check("S1.2 admissible bases %d ordered / %d sets; weld-compatible "
      "%d / %d (canonicity-run counts 6/2 and 3/1)"
      % (len(ADM), len({frozenset(b) for b in ADM}), len(WELD),
         len({frozenset(b) for b in WELD})),
      len(ADM) == 6 and len(WELD) == 3, kill="CENSUS-BROKEN")

QUAD = (2, 3, 5, 7)
idents = {}
for bb in WELD:
    cm = coords_map(bb)
    for assign in itertools.permutations(QUAD):
        if assign[3] != 2:                     # R3 anchor filter
            continue
        phi = tuple((assign[0] ** cm[w][0]) * (assign[1] ** cm[w][1])
                    * (assign[2] ** cm[w][2]) * (assign[3] ** cm[w][3])
                    for w in W16)
        idents.setdefault(phi, assign)
SIGP16 = [WIDX[sig_bits(w)] for w in W16]
classes = []
seen = set()
for phi in sorted(idents):
    if phi in seen:
        continue
    cls = {phi}
    cur = phi
    for _ in range(2):
        cur = tuple(cur[SIGP16[i]] for i in range(16))
        cls.add(cur)
    seen |= cls
    classes.append(sorted(cls)[0])
def canon3(t3):
    k = t3.index(3)
    return t3[k:] + t3[:k]


assigns = sorted(canon3(idents[c][:3]) for c in classes)
check("S1.3 R3 survivors modulo C3 = EXACTLY 2 classes, family "
      "cycles (canonical rotation) %s == [(3,5,7), (3,7,5)] (the "
      "chirality pair)"
      % (assigns,), len(classes) == 2
      and assigns == [(3, 5, 7), (3, 7, 5)], kill="CENSUS-BROKEN")

CHI = {"chi+": {"F1": 3, "F2": 5, "F3": 7, "A": 2},
       "chi-": {"F1": 3, "F2": 7, "F3": 5, "A": 2}}


def dval(cls, w):
    return (cls["F1"] ** w[0]) * (cls["F2"] ** w[1]) \
        * (cls["F3"] ** w[2]) * (cls["A"] ** w[3])


fixed_nz = [w for w in W16 if w != Z4 and sig_bits(w) == w]
check("S1.4 fixed-sector divisors chirality-EQUAL: %s (plus "
      "vacuum 1) -- any fixed-sector functional is chirality-"
      "blind, typed"
      % sorted(dval(CHI["chi+"], w) for w in fixed_nz),
      all(dval(CHI["chi+"], w) == dval(CHI["chi-"], w)
          for w in fixed_nz))

# ======================================================================
section("S2: readout regressions (dw + wr read-only)")
# ======================================================================
VA, VB, VC, D0 = dw.closure_blocks()
w2 = dw.readout_vec("r2")
rr9 = core.build_window(9)
N9 = int(math.exp(2.0 * rr9["alpha"]))
lam9 = dw.mangoldt(N9)
Ha = dw.build_H(N9, lam9, "a")
LOAD = wr.Load(*dw.weyl_data(Ha))
mv1 = LOAD.m(dw.zgrid())
_, outs1, _ = dw.loaded_scalars(mv1, VA, VB, VC, D0)
s_v1 = float(np.min(1.0 - np.abs(outs1["r2"]) ** 2))
check("S2.1 v1 regression: extremal s(kz9, a, r2) = %.6e == "
      "%.6e +- 1e-5" % (s_v1, V1_SMIN_REF),
      abs(s_v1 - V1_SMIN_REF) <= 1e-5, kill="READOUT-BROKEN")
ok_hz = True
for zg in (wr.ZFIX, LOAD.ev + 1j * wr.EPS_B, 1j * wr.YPH):
    mv = LOAD.m(zg)
    ok_hz &= bool(np.all(mv.imag > 0)) and bool(
        np.all(np.abs((mv - 1j) / (mv + 1j)) < 1.0))
check("S2.2 Herglotz + passivity on ZFIX, spectral grid and the "
      "phase window", ok_hz, kill="READOUT-BROKEN")
rd = wr.readouts(LOAD, VA, VB, VC, D0, w2)
rph = LOAD.r(1j * wr.YPH)
sC_inline = float(np.sum(np.abs(np.angle(rph[1:] / rph[:-1]))))
check("S2.3 inline total-phase-variation == wr.readouts s_C "
      "(%.6e vs %.6e, diff %.1e)"
      % (sC_inline, rd["s_C"], abs(sC_inline - rd["s_C"])),
      abs(sC_inline - rd["s_C"]) <= 1e-12, kill="READOUT-BROKEN")

# ======================================================================
section("S3: the blindness ward -- sigma-less machines are "
        "chirality-blind (structural)")
# ======================================================================
WH = rc.walsh16()
WELD16 = np.diag([1j ** rc.hamw(S) for S in range(16)])


def sig_int(S):
    f1, f2, f3, a = S & 1, (S >> 1) & 1, (S >> 2) & 1, (S >> 3) & 1
    return f3 + 2 * f1 + 4 * f2 + 8 * a


def pi_int(S):
    f1, f2, f3, a = S & 1, (S >> 1) & 1, (S >> 2) & 1, (S >> 3) & 1
    return f1 + 2 * f3 + 4 * f2 + 8 * a


P_SIG = np.zeros((16, 16))
P_PI = np.zeros((16, 16))
for S in range(16):
    P_SIG[sig_int(S), S] = 1.0
    P_PI[pi_int(S), S] = 1.0


def dvec(chi):
    cls = CHI[chi]
    return np.array([dval(cls, ((S & 1), (S >> 1) & 1,
                                (S >> 2) & 1, (S >> 3) & 1))
                     for S in range(16)], float)


D_P, D_M = dvec("chi+"), dvec("chi-")


def machine(chi, tau, with_sigma):
    ph = np.diag(np.exp(-0.5j * np.log(dvec(chi)) * tau))
    U = WH @ WELD16 @ ((P_SIG @ ph) if with_sigma else ph)
    return U


def loaded_f(chi, rvals, taus, with_sigma):
    out = []
    for r_, t_ in zip(rvals, taus):
        U = machine(chi, t_, with_sigma)
        A, B, C = U[1:, 1:], U[1:, 0], U[0, 1:]
        Dv = U[0, 0]
        Vt = A + (r_ / (1.0 - Dv * r_)) * np.outer(B, C)
        out.append(complex(w2.conj() @ Vt @ w2))
    return np.array(out)


taus = np.asarray(wr.YPH, float)
r_truth = LOAD.r(1j * wr.YPH)
conj_dev = max(float(np.max(np.abs(
    machine("chi-", t, False)
    - P_PI @ machine("chi+", t, False) @ P_PI.T)))
    for t in (taus[0], taus[16], taus[-1]))
f0p = loaded_f("chi+", r_truth, taus, False)
f0m = loaded_f("chi-", r_truth, taus, False)
blind_dev = float(np.max(np.abs(f0p - f0m)))
u_test = machine("chi+", taus[0], True)
check("S3.1 WARD FIRES: U0_- == Pi U0_+ Pi^T (max dev %.1e <= "
      "1e-13); sigma-less loaded scalars IDENTICAL for chi+/chi- "
      "(max dev %.1e <= 1e-12) -- any phase readout without the "
      "sigma letter is PROVABLY chirality-blind"
      % (conj_dev, blind_dev),
      conj_dev <= 1e-13 and blind_dev <= 1e-12, kill="WARD-DEAD")
check("S3.2 the sigma-wired machine is unitary with port "
      "U[0,0] = 1/4 (dev %.1e; closure well-posed)"
      % abs(u_test[0, 0] - 0.25),
      float(np.max(np.abs(u_test.conj().T @ u_test
                          - np.eye(16)))) <= 1e-12
      and abs(u_test[0, 0] - 0.25) <= 1e-14)

# ======================================================================
section("S4: the decider (frozen rules, evaluated only now)")
# ======================================================================
om = np.exp(2j * math.pi / 3.0)
orb_roots = sorted({min(frozenset({w, sig_bits(w),
                                   sig_bits(sig_bits(w))}))
                    for w in FREE12})


def x1cube(dmapper, v0):
    xs = [math.log(dmapper(v0)),
          math.log(dmapper(sig_bits(v0))),
          math.log(dmapper(sig_bits(sig_bits(v0))))]
    return (xs[0] + xs[1] * om + xs[2] * om ** 2) ** 3


def phi_reg(dmapper, roots=None):
    return float(sum(x1cube(dmapper, v0)
                     for v0 in (roots or orb_roots)).imag)


phi_p = phi_reg(lambda w: dval(CHI["chi+"], w))
phi_m = phi_reg(lambda w: dval(CHI["chi-"], w))
reroot = phi_reg(lambda w: dval(CHI["chi+"], w),
                 roots=[sig_bits(v) for v in orb_roots])
check("S4.1 D1 wards (v2, absolute): antisymmetry "
      "|Phi_reg(chi+) + Phi_reg(chi-)| = %.1e <= 1e-12; "
      "re-rooting invariance (dev %.1e)"
      % (abs(phi_p + phi_m), abs(reroot - phi_p)),
      abs(phi_p + phi_m) <= 1e-12
      and abs(reroot - phi_p) <= 1e-12)
# v2 ward: the Moebius-complement pairing cancels per orbit pair
dmap_p = lambda w: dval(CHI["chi+"], w)               # noqa: E731
comp_dev = 0.0
for v0 in orb_roots:
    vc = x2((1, 1, 1, 1), v0)                          # d -> 210/d
    comp_dev = max(comp_dev, abs(complex(
        x1cube(dmap_p, v0) + x1cube(dmap_p, vc))))
check("S4.1b v2 STRUCTURAL WARD: the Moebius complement d -> "
      "210/d pairs the 4 orbits with reversed orientation, "
      "X1(O)^3 + X1(O')^3 = 0 per pair (max dev %.1e) -- "
      "Phi_reg == 0 IDENTICALLY for every multiplicative weight "
      "assignment: the register carries no intrinsic scalar "
      "orientation of this type" % comp_dev, comp_dev <= 1e-12)
kms_winner = None
if abs(phi_p) > 1e-12:
    kms_winner = "chi+" if phi_p > 0 else "chi-"
print("    D2 KMS-orientation criterion: Phi_reg(chi+) = %+.2e, "
      "Phi_reg(chi-) = %+.2e -> %s"
      % (phi_p, phi_m,
         ("KMS-compatible chirality = %s (convention bridge "
          "unless D3 agrees)" % kms_winner) if kms_winner else
         "VACUOUS (Phi_reg == 0 identically; no KMS winner, "
         "typed v2)"))

# D3: loads
lamE = kn.lambda_eps(N9)[:N9 + 1]


def lcg_perm(n, seed):
    s = seed
    idx = list(range(2, n + 1))
    for i in range(len(idx) - 1, 0, -1):
        s = (1103515245 * s + 12345) % (1 << 31)
        j = s % (i + 1)
        idx[i], idx[j] = idx[j], idx[i]
    return idx


lamS = np.zeros(N9 + 1)
lamS[2:] = lam9[lcg_perm(N9, LCG_SEED)]
loads = {"truth": LOAD}
for nm, lm in (("eps", lamE), ("scr", lamS)):
    H_ = dw.build_H(N9, lm, "a")
    loads[nm] = wr.Load(*dw.weyl_data(H_))
PHI = {}
VV = {}
for lnm, ld in loads.items():
    rv = ld.r(1j * wr.YPH)
    for chi in ("chi+", "chi-"):
        f = loaded_f(chi, rv, taus, True)
        dphi = np.angle(f[1:] / f[:-1])
        PHI[(chi, lnm)] = float(np.sum(dphi))
        VV[(chi, lnm)] = float(np.sum(np.abs(dphi)))
print("    load     Phi(chi+)   Phi(chi-)   V(chi+)   V(chi-)")
for lnm in ("truth", "eps", "scr"):
    print("    %-7s %+.5f   %+.5f   %.5f   %.5f"
          % (lnm, PHI[("chi+", lnm)], PHI[("chi-", lnm)],
             VV[("chi+", lnm)], VV[("chi-", lnm)]))
delta_see = abs(PHI[("chi+", "truth")] - PHI[("chi-", "truth")])
sees = delta_see >= SEE_BAR
disc_ok = {}
for chi in ("chi+", "chi-"):
    vt = VV[(chi, "truth")]
    rE = VV[(chi, "eps")] / max(vt, 1e-300)
    rS = VV[(chi, "scr")] / max(vt, 1e-300)
    disc_ok[chi] = (not (1.0 / DISC_FACTOR <= rE <= DISC_FACTOR)) \
        and (not (1.0 / DISC_FACTOR <= rS <= DISC_FACTOR))
    print("    disc(%s): V_eps/V_truth = %.3f, V_scr/V_truth = "
          "%.3f -> discrimination %s"
          % (chi, rE, rS, "PRESERVED" if disc_ok[chi]
             else "LOST/INSIDE the 1.5x window"))
decides = sees and (disc_ok["chi+"] != disc_ok["chi-"])
mach_winner = None
if decides:
    mach_winner = "chi+" if disc_ok["chi+"] else "chi-"
check("S4.2 D3 measured: |Phi(chi+) - Phi(chi-)| = %.3e on truth "
      "(sees the chirality: %s, bar 1e-3); machine decides "
      "(exactly one disc_ok): %s%s"
      % (delta_see, sees, decides,
         ("; winner " + mach_winner) if mach_winner else ""),
      True)
# v2 ward: WHY the quadratic readout is blind -- transpose
# symmetry (w2' M w2 = w2' M^T w2; cycle reversal = transposition
# up to the Pi-conjugation fixing port and readout)
check("S4.3 v2 STRUCTURAL WARD: sigma-wired QUADRATIC readout "
      "chirality-equal to machine precision (max dev %.1e <= "
      "1e-12) -- the symmetric form w2' Vt w2 cannot see the "
      "cycle orientation (transposition kills it); an "
      "orientation-sensitive readout needs an ASYMMETRIC pairing"
      % delta_see, delta_see <= 1e-12)
# v2 REPORT-ONLY diagnostic: asymmetric two-vector readout
w1v = dw.readout_vec("r1")


def loaded_f_asym(chi, rvals, tvals):
    out = []
    for r_, t_ in zip(rvals, tvals):
        U = machine(chi, t_, True)
        A, B, C = U[1:, 1:], U[1:, 0], U[0, 1:]
        Dv = U[0, 0]
        Vt = A + (r_ / (1.0 - Dv * r_)) * np.outer(B, C)
        out.append(complex(w2.conj() @ Vt @ w1v))
    return np.array(out)


fa_p = loaded_f_asym("chi+", r_truth, taus)
fa_m = loaded_f_asym("chi-", r_truth, taus)
phi_ap = float(np.sum(np.angle(fa_p[1:] / fa_p[:-1])))
phi_am = float(np.sum(np.angle(fa_m[1:] / fa_m[:-1])))
print("    v2 DIAGNOSTIC (report-only, NOT verdict-bearing): "
      "asymmetric readout w2' Vt w1: Phi(chi+) = %+.5f, "
      "Phi(chi-) = %+.5f, |dPhi| = %.3e -- the asymmetric "
      "pairing %s the chirality"
      % (phi_ap, phi_am, abs(phi_ap - phi_am),
         "SEES" if abs(phi_ap - phi_am) >= 1e-3 else
         "still does not see"))

# ======================================================================
section("S5: scrambled-register control")
# ======================================================================
mv_labels = sorted(FREE12)
mv_vals = [dval(CHI["chi+"], w) for w in mv_labels]
pidx = lcg_perm(len(mv_vals), LCG_SEED)     # perm of 2..12 indices
perm_vals = list(mv_vals)
ordr = [i - 2 for i in pidx] + [len(mv_vals) - 1]
perm_vals = [mv_vals[i] for i in ordr]
scr_map = dict(zip(mv_labels, perm_vals))


def d_scr(w):
    if w in scr_map:
        return scr_map[w]
    return dval(CHI["chi+"], w)


viol = 0
for u, v in itertools.combinations([w for w in W16 if w != Z4], 2):
    if all(a * b == 0 for a, b in zip(u, v)):
        if d_scr(x2(u, v)) != d_scr(u) * d_scr(v):
            viol += 1
D_SCRV = np.array([d_scr(((S & 1), (S >> 1) & 1, (S >> 2) & 1,
                          (S >> 3) & 1)) for S in range(16)],
                  float)


def loaded_f_weights(dw16, rvals, tvals):
    out = []
    for r_, t_ in zip(rvals, tvals):
        ph = np.diag(np.exp(-0.5j * np.log(dw16) * t_))
        U = WH @ WELD16 @ P_SIG @ ph
        A, B, C = U[1:, 1:], U[1:, 0], U[0, 1:]
        Dv = U[0, 0]
        Vt = A + (r_ / (1.0 - Dv * r_)) * np.outer(B, C)
        out.append(complex(w2.conj() @ Vt @ w2))
    return np.array(out)


f_scrreg = loaded_f_weights(D_SCRV, r_truth, taus)
f_true = loaded_f("chi+", r_truth, taus, True)
move = float(np.linalg.norm(f_scrreg - f_true)
             / np.linalg.norm(f_true))
check("S5.1 CONTROL FIRES: scrambled register weights violate "
      "lattice multiplicativity on %d disjoint pairs (> 0) AND "
      "move the machine readout (rel %.3e >= 1e-6) -- the "
      "decider consumes the register structure"
      % (viol, move), viol > 0 and move >= 1e-6,
      kill="WARD-DEAD")

# ======================================================================
section("S6: verdict (frozen precedence)")
# ======================================================================
if KILLS:
    verdict = KILLS[0]
elif decides and kms_winner is None:
    verdict = ("CHIRALITY-DECIDED (%s; criterion: machine "
               "discrimination alone, D2 vacuous -- typed v2)"
               % mach_winner)
elif decides and mach_winner == kms_winner:
    verdict = ("CHIRALITY-DECIDED (%s = family cycle %s; "
               "criterion: machine discrimination + KMS "
               "orientation agree)"
               % (mach_winner,
                  "(3,5,7)" if mach_winner == "chi+"
                  else "(3,7,5)"))
elif decides:
    verdict = "CHIRALITY-INCONSISTENT"
else:
    verdict = "CHIRALITY-DEGENERATE"
n_pass = sum(1 for _, ok in CHECKS if ok)
print("\n" + "=" * 70)
print("CHECKS: %d/%d passed" % (n_pass, len(CHECKS)))
if n_pass != len(CHECKS):
    print("FAILED: %s" % [nm for nm, ok in CHECKS if not ok])
print("VERDICT: %s" % verdict)
print("=" * 70)
print("""
HONEST CONSEQUENCE (measured):
 * The census freedom is exactly the two classes (3,5,7) vs
   (3,7,5) on the family cycle (S1, regression).
 * STRUCTURAL FACT (S3): every phase readout that does not couple
   the family-cycle letter to the divisor weights is PROVABLY
   chirality-blind (bit-transposition conjugation fixing port and
   readout).  The deployed weyl/phase chain is of that type: the
   chirality cannot be decided by the deployed readouts as they
   stand.
 * D1/D2 (v2 finding): the register orientation functional
   vanishes IDENTICALLY -- the Moebius complement d -> 210/d
   pairs the orbits with reversed orientation (exact ward) --
   so the KMS-orientation criterion is VACUOUS: the register's
   multiplicative weight structure carries NO intrinsic scalar
   orientation.  KMS winner: %s.
 * D3 (sigma-wired machine, blind protocol): sees chirality =
   %s (|dPhi| = %.3e, quadratic readout provably orientation-
   dead by transpose symmetry, v2 ward), decides = %s;
   asymmetric-readout diagnostic |dPhi| = %.3e (report-only).
If the verdict is CHIRALITY-DEGENERATE: the residual Z2 of the
210 register is REAL GAUGE at the deployed-machine level -- the
canonicity verdict DIVISOR210-GAUGE-FAMILY(2) stands and is not
upgraded.  NO RH claim.""" % (kms_winner, sees, delta_see,
                              decides, abs(phi_ap - phi_am)))
print("runtime: %.1f s" % (time.time() - T0))
sys.exit(0 if n_pass == len(CHECKS) else 1)
