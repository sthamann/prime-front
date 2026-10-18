#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""hecke_broadcast_probe -- HECKE.ARROW_MESSAGE.01 follow-up (the C2
broadcast test): does the transported Hecke operator on the odd quotient
factor as T-bar_p = M_p (x) I_16, with M_p = [[A_p, B_p], [B_p, A_p]]
the C2 packet matrix (A_n = (sigma3(n) + a_n)/2, B_n = (sigma3(n) -
a_n)/2 = 16 R(n), both nonnegative) and I_16 the identity on
V = L/(1+i)L -- "place 2 is the control plane, odd primes broadcast
over all 16 states"?

PREDECESSOR (this worker, same round): hecke_arrow_ledger_probe.py,
verdict ARROW-LEDGER-STRUCTURED 48/48 -- per-line Kneser label vectors
fall into two types with n_B = (sigma3^2 - a_p^2)/8; odd tower layers
act as degree * id on V (Hecke rigidity); ramified layer = the 15
hyperplanes with 2:1 deck.  ALGEBRA CHECK (task): n_B = (sigma3^2 -
a_p^2)/8 = ((A+B)^2 - (A-B)^2)/8 = 4AB/8 = A_p B_p / 2 -- the special
Kneser lines count the PRODUCT of the two packet multiplicities.

INVESTIGATION RECORD (disclosed; performed BEFORE the freeze):
  * Derivation: on ODD coefficients the v535 oldform coordinates kill
    every basis element except E4 and f8 (E4(q^d), d > 1, and f8(q^2)
    have no odd coefficients), so the mu4 glue census of the odd
    shell-n vectors of E8 is FORCED to
      Theta = (56 s - 4 a, 64 s, 56 s + 4 a, 64 s),   s = sigma3(n),
    i.e. Theta = A_n u + B_n u^{+2} with u = (52, 64, 60, 64) the ROOT
    (shell-1) glue pattern and u^{+2} its glue-torsor 2-shift.  The
    sheet switch is the 2-SHIFT OF THE mu4 TORSOR (the J^2 = -1 clock
    half-turn), and the unit packet is the root census itself.
  * Pilot (p = 3, disclosed): the joint (V-class x mu4-glue) 64-cell
    census of shell 3 equals 12 * tab_1 + 16 * tab_1^{sw} EXACTLY, and
    the V-class totals are uniform 448 = 16 sigma3(3) with empty zero
    class.  The pilot place p = 3 is therefore the SELECTION place;
    the confirmation set is {5, 7, 9, 11, 13} (frozen below).
  * REJECTED candidates (typed honestly, no free keys):
    P1 NS/R glue parity (deg even vs odd): splits 112 s / 128 s --
       NO a_n dependence, cannot carry (A, B).  Measured.
    P2 deg = 0 vs deg = 2: splits (56 s - 4a, 56 s + 4a); proportional
       to (A, B) iff 120 s a = 0 -- exact disproof.  Measured.
    P3c conjugation on tower submodules: at split places conjugation
       swaps the two ideal layers entirely (all-switch, (0, 312) at
       p = 5), at inert places it fixes #P^3(F_p) hyperplanes -- no
       (A, B) proportion.  Structural rejection, no fit attempted.
    P4 "R(p) = number of type-B Kneser Weyl orbits": measured 1, 4, 13
       at p = 3, 5, 7 -- matches R = 1, 4 but FAILS at p = 7 (13 !=
       10): a small-place coincidence, rejected and reported.
  * FROZEN definition (the ONE definition, channel-typed): the C2
    sheet parity is the PACKET decomposition of the odd-shell census
      tab_n = A_n * tab_1 + B_n * tab_1^{sw}        (64 cells)
    where tab_1 is the joint (V-class x glue) root census (the unit
    packet), sw = glue-torsor 2-shift with V-classes UNTOUCHED (the
    broadcast: a sheet switch moves NO V-state), and (A_n, B_n) are
    solved from two census functionals and verified on ALL 64 cells
    (overdetermined 64 : 2).  TYPED [C neu]: this is a CHANNEL
    (packet) decomposition of the arrow census, exact and positive;
    a POINTWISE sheet coloring of individual lattice vectors is NOT
    claimed (that would require unforced choices -- no free keys).

THE GATES (frozen):
  G1 UNIT PACKET: shell-1 joint census = 15 x 16 with glue totals
     (52, 64, 60, 64); the 15 per-class glue patterns u_v are NOT all
     equal (so the factorization is class-sensitive and controls can
     fire); the class map used is the verified F2-linearization of the
     v738 quotient (spot-checked against Lmodule.class_of_w).
  G2 BROADCAST FACTORIZATION, per odd shell n in {3, 5, 7, 9, 11, 13}:
     (i) V-uniformity: zero class EMPTY, every nonzero class total
         = 16 sigma3(n)  (the (x) I_16 leg, census side);
     (ii) solve A + B = N/240, A - B = -(Theta_0 - Theta_2)/8, then
         tab_n == A tab_1 + B tab_1^{sw} on ALL 64 cells EXACTLY;
     (iii) A, B >= 0 (positivity) and (A, B) == ((s + a_n)/2,
         (s - a_n)/2) with a_n from the corpus f8 reference (A_P +
         weight-4 multiplicativity a_9 = a_3^2 - 27);
     (iv) B_n == 0 mod 16 arrow-exactly; R(n) = B_n/16 integer.
  G3 MICROSTATES: R(n) = 1, 4, 10, 24, 43, 68 at n = 3..13 == the
     per-class sheet-switch multiplicity / 16 (switch cell = 16 B_n =
     256 R(n) per class); the rejected P4 orbit count is re-measured
     and reported (1, 4, 13).
  G4 TRACE CONSISTENCY: a_n = A_n - B_n and sigma3(n) = A_n + B_n from
     the ledger sums; the Kneser neighbor-sum fits (re-run live at
     p = 3, 5, 7) give b = 2 A_p exactly (the affine T_p coefficient
     IS twice the keep-multiplicity); n_B(p) == A_p B_p / 2 from the
     live line census; the tower I_16 leg re-verified live on the
     norm-9 layer (all 820 submodules, transport = id on all 16
     states).
  C  MUST-FAIL CONTROLS: C1 scrambled parity -- glue 1-shift instead
     of 2-shift AND an LCG permutation of the 15 class patterns: the
     64-cell verification must fail; C2 wrong block size -- the
     maximal power of 2 dividing ALL B_n is EXACTLY 16 (32 fails at
     n = 3, 11; 8 is non-maximal: gcd/16 odd), and block-32 R values
     are non-integer where 16 works; C3 random arrow sets (LCG tables
     with the correct total): V-uniformity and factorization break.

VERDICT ENUM (frozen): BROADCAST-EXACT (T-bar_p = M_p (x) I_16
arrow-exactly on every tested odd shell -- the control-plane /
data-plane protocol is real at arrow level) / BROADCAST-PARTIAL (name
which cells / shells) / BROADCAST-DEAD (no natural parity definition
factorizes -- the reading stays [C], typed).

FENCES: [C neu] semantics typed -- the "control plane / data plane /
broadcast" wording is a READING of an exact finite factorization, not
a physics or semantics claim; no-free-keys discipline: the parity is
the structural packet decomposition above (channel split), pointwise
vector coloring not claimed; ROOTCLASS-MIXED (v775) cited and
unaffected -- no code -> matter assignment anywhere.  Floats only in
the Fincke-Pohst bounds (every vector re-checked in exact integers)
and the entropy readout (measurement).

FIREWALL: experiments/ probe; ONE new file; writes nothing; no
verification/, paper, ledger, changelog or website surface touched;
no prime table / zeta symbols (AST-enforced; sigma3 by trial-division
divisor sum on the six declared odd shells, a_n frozen corpus f8
values); no v563 window surface.  Machinery read-only from v738 /
v535 / hecke_arrow_ledger_probe (certified sibling).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/hecke_broadcast_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from collections import Counter
from fractions import Fraction as Fr

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v738_hecke_mod_ramified as ram              # noqa: E402
import v535_hecke_from_geometry as kg              # noqa: E402
import hecke_arrow_ledger_probe as hal             # noqa: E402

FROZEN_SPEC = """\
HECKE.ARROW_MESSAGE.01 / C2-broadcast spec v1 (frozen 2026-08-05, after
the disclosed p=3 pilot, before the confirmation runs)
Shells: odd n in {3,5,7,9,11,13} (primes + composite 9; deeper-if-cheap
  clause exercised at 11, 13).  Arrow set per shell: ALL E8 vectors of
  norm 2n (Fincke-Pohst, exact integer recheck), labeled by (V-class in
  the v738 frame via the verified F2-linearization, mu4 glue deg via
  the v535 DVEC pairing, orientation calibrated to the shell-1 head
  (52,64,60,64)).
Frozen parity: the packet decomposition tab_n = A_n tab_1 + B_n
  tab_1^{sw}, sw = glue-torsor 2-shift, V-classes untouched; (A,B)
  solved from (N/240, -(Theta0-Theta2)/8) and verified on all 64 cells;
  channel-typed, no pointwise coloring claimed.
Gates G1-G4 and controls C1-C3 as in the module docstring.  Corpus
  references: a_p from v535 A_P {3:-4,5:-2,7:24,11:-44,13:22}, a_9 =
  a_3^2 - 27 = -11 (weight-4 multiplicativity); predicted R series
  1,4,10,24,43,68.  Rejected parity candidates P1/P2/P3c/P4 typed in
  the docstring; P4 measured (1,4,13) fails at p=7.
Verdict enum: BROADCAST-EXACT / BROADCAST-PARTIAL / BROADCAST-DEAD.
LCG seed 20260805.  Runtime cap ~20 min.
"""

SHELLS = (3, 5, 7, 9, 11, 13)
KNESER_PLACES = (3, 5, 7)
R_EXPECT = {3: 1, 5: 4, 7: 10, 9: 24, 11: 43, 13: 68}
A9 = (-4) ** 2 - 27                                 # a_9 = a_3^2 - 3^3

BANNED_IDS = ("sympy", "isprime", "primerange", "nextprime", "prevprime",
              "primepi", "zetazero", "zetas", "mpz_zeta")
FORBIDDEN_SURFACE = ("U_ALL", "MU_ALL", "LAM_TAB", "G_ALL", "NU_MAIN",
                     "ATOM_MAX", "atoms_in", "atom_lags_at", "arch_lags",
                     "frame_a_zones", "build_window", "odd_toeplitz",
                     "_NN")

CHECKS = []
GATE_FAIL = []
CONTROL_FIRED = {}
T0 = time.time()

_LCG = [20260805]


def lcg(n):
    _LCG[0] = (1103515245 * _LCG[0] + 12345) % (1 << 31)
    return _LCG[0] % n


def check(name, ok, detail="", gate=None):
    CHECKS.append((name, bool(ok)))
    if gate and not ok:
        GATE_FAIL.append(gate)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def sigma3_odd(n):
    """divisor cube sum by trial division (declared odd shells only --
    no prime table)."""
    return sum(d ** 3 for d in range(1, n + 1) if n % d == 0)


A_N = dict(kg.A_P)
A_N[9] = A9


# ==================================================================== G0
def g0_firewall():
    section("G0 -- SHA-frozen spec + AST firewall + environment")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    tree = ast.parse(src)
    bad, leaks = [], []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            mods = [al.name for al in node.names]
            if isinstance(node, ast.ImportFrom) and node.module:
                mods.append(node.module)
            for m in mods:
                if any(b in m for b in BANNED_IDS):
                    bad.append(m)
            continue
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
        if name in FORBIDDEN_SURFACE:
            leaks.append(name)
    check("G0.1 no prime-table / zeta symbols in this file", not bad,
          "found %s" % bad if bad else "clean")
    check("G0.2 no v563 window surface (AST-enforced)", not leaks,
          "leaks %s" % leaks if leaks else "clean")
    print("    python %s, numpy %s" % (sys.version.split()[0],
                                       np.__version__))


# ==================================================================== frame
G8 = kg.G
DVEC = np.asarray(kg.DVEC, dtype=np.int64)
BE = kg.BE_np.astype(np.int64)
CHOL_U = np.linalg.cholesky(G8.astype(np.float64)).T


def enum_shell(n):
    """all E8 coeff vectors c with c G c / 2 == n (exact recheck)."""
    out = []
    x = [0] * 8
    eps = 1e-7
    U = CHOL_U

    def go(k, right):
        if k < 0:
            c = np.array(x, dtype=np.int64)
            if int(c @ G8 @ c) == 2 * n:
                out.append(c.copy())
            return
        s = 0.0
        for j in range(k + 1, 8):
            s += U[k, j] * x[j]
        ukk = U[k, k]
        thr = math.sqrt(max(0.0, right))
        lo = math.ceil((-thr - s) / ukk - eps)
        hi = math.floor((thr - s) / ukk + eps)
        for xk in range(lo, hi + 1):
            x[k] = xk
            t = ukk * xk + s
            go(k - 1, right - t * t)
        x[k] = 0

    go(7, 2.0 * n + eps)
    return np.stack(out)


def s1_frame():
    section("G1 -- the unit packet: joint (V-class x glue) root census")
    L = ram.Lmodule()
    # F2-linearization of the v738 class map on coeff vectors
    Kcols = []
    for i in range(8):
        amb = tuple(int(v) for v in BE[:, i])
        Kcols.append(L.class_of_w(amb))
    Kmat = np.array(Kcols, dtype=np.int64).T          # 4 x 8

    def joint(C):
        cls = (C % 2) @ Kmat.T % 2
        cidx = cls @ np.array([1, 2, 4, 8])
        deg = (C @ DVEC) % 4
        tab = np.zeros((16, 4), dtype=np.int64)
        np.add.at(tab, (cidx, deg), 1)
        return tab

    R1 = enum_shell(1)
    tab1 = joint(R1)
    # spot-check the linearized class map against Lmodule.class_of_w
    ok_lin = True
    for _ in range(60):
        c = R1[lcg(len(R1))]
        direct = L.class_of_w(tuple(int(v) for v in (BE @ c)))
        linz = tuple(int(b) for b in ((c % 2) @ Kmat.T % 2))
        ok_lin &= (direct == linz)
    glue1 = tab1.sum(axis=0)
    cls1 = sorted(tab1.sum(axis=1).tolist())
    patterns = {tuple(tab1[i]) for i in range(16) if tab1[i].sum()}
    check("G1.1 shell 1: 240 roots, class totals 15 x 16 (zero empty), "
          "glue head %s == (52, 64, 60, 64) (orientation calibrated); "
          "class map linearization verified (60 samples)"
          % (glue1.tolist(),),
          len(R1) == 240 and cls1 == [0] + [16] * 15
          and glue1.tolist() == [52, 64, 60, 64] and ok_lin, gate="G1")
    check("G1.2 the 15 per-class glue patterns u_v are NOT all equal "
          "(%d distinct) -- the factorization is class-sensitive"
          % len(patterns), len(patterns) >= 2, gate="G1")
    print("    unit packet tab_1 (rows = V-class bits, cols = glue "
          "deg 0..3):")
    for i in range(16):
        if tab1[i].sum():
            print("      class %s : %s"
                  % (tuple((i >> k) & 1 for k in range(4)),
                     tab1[i].tolist()))
    return dict(joint=joint, tab1=tab1)


# ==================================================================== S2
def s2_parity_record(fr):
    section("S2 -- parity investigation record (rejected candidates "
            "measured; frozen definition stated)")
    tab1 = fr["tab1"]
    R3 = enum_shell(3)
    tab3 = fr["joint"](R3)
    th = tab3.sum(axis=0)
    s3, a3 = sigma3_odd(3), A_N[3]
    # P1: NS/R glue parity (deg even vs odd) -- no a_n dependence
    ns, rr = int(th[0] + th[2]), int(th[1] + th[3])
    check("S2.1 P1 REJECTED (measured): glue-parity split at n = 3 is "
          "(112 s, 128 s) = (%d, %d) -- carries NO a_n dependence, "
          "cannot be the C2" % (ns, rr),
          ns == 112 * s3 and rr == 128 * s3)
    # P2: deg 0 vs deg 2
    prop = (Fr(int(th[0]), int(th[2]))
            == Fr(s3 + a3, s3 - a3))
    check("S2.2 P2 REJECTED (measured): (Theta_0, Theta_2) = (%d, %d) "
          "= (56 s - 4a, 56 s + 4a); proportional to (A, B) iff "
          "120 s a = 0 -- fails (%s)"
          % (int(th[0]), int(th[2]), not prop),
          th[0] == 56 * s3 - 4 * a3 and th[2] == 56 * s3 + 4 * a3
          and not prop)
    print("    P3c conjugation-on-tower REJECTED (structural): at the "
          "split place p = 5\n    conjugation swaps the two ideal "
          "layers entirely -- all-switch (0, 312),\n    never "
          "(A, B) = (62, 64); at inert places it fixes #P^3(F_p) "
          "hyperplanes.\n    P4 (type-B Weyl orbit count) measured in "
          "G3 below: (1, 4, 13) -- fails at p = 7.")
    print("    FROZEN (channel-typed, no pointwise coloring): "
          "tab_n = A_n tab_1 + B_n tab_1^{sw},\n    sw = glue-torsor "
          "2-shift (J^2 half-turn), V-classes untouched.")
    return tab3


# ==================================================================== G2
def g2_factorization(fr, tab3):
    section("G2 -- the broadcast factorization on the odd shells "
            "(64 cells each, overdetermined)")
    tab1 = fr["tab1"]
    sw = tab1[:, [2, 3, 0, 1]]
    results = {}
    ok_all = True
    for n in SHELLS:
        t0 = time.time()
        tab = tab3 if n == 3 else fr["joint"](enum_shell(n))
        N = int(tab.sum())
        s = sigma3_odd(n)
        a_ref = A_N[n]
        th = tab.sum(axis=0)
        # V-uniformity
        cls_tot = tab.sum(axis=1)
        ok_uni = (cls_tot[0] == 0
                  and all(int(cls_tot[i]) == 16 * s for i in range(16)
                          if i != 0))
        # solve (A, B) from two census functionals
        okAB = (N % 240 == 0 and (int(th[0]) - int(th[2])) % 8 == 0)
        A2 = N // 240 - (int(th[0]) - int(th[2])) // 8   # 2A
        okAB &= (A2 % 2 == 0)
        A = A2 // 2
        B = N // 240 - A
        pred = A * tab1 + B * sw
        ok_cells = np.array_equal(tab, pred)
        ok_ref = (A >= 0 and B >= 0 and A - B == a_ref
                  and A + B == s
                  and A == (s + a_ref) // 2 and B == (s - a_ref) // 2)
        ok_div = (B % 16 == 0)
        results[n] = dict(A=A, B=B, s=s, N=N, R=B // 16, tab=tab)
        ok = ok_uni and okAB and ok_cells and ok_ref and ok_div
        ok_all &= ok
        check("G2.n=%d: N = %d = 240 sigma3; V-uniform 16 s = %d per "
              "nonzero class, zero empty (%s); tab == %d tab_1 + %d "
              "tab_1^{sw} on ALL 64 cells (%s); (A, B) = ((s%+d)/2, "
              "(s%+d)/2) nonneg (%s); B = %d == 0 mod 16 (%s)"
              % (n, N, 16 * s, ok_uni, A, B, ok_cells, a_ref, -a_ref,
                 ok_ref, B, ok_div), ok,
              "%.1f s" % (time.time() - t0), gate="G2.n=%d" % n)
    return results, ok_all


# ==================================================================== G3
def g3_microstates(results, Mint):
    section("G3 -- the R(n) microstate cross-check")
    ok_R = all(results[n]["R"] == R_EXPECT[n] for n in SHELLS)
    check("G3.1 R(n) = B_n/16 = %s == predicted series %s (8-mode "
          "triangular-number system values); per-class sheet-switch "
          "cell = 16 B_n = 256 R(n)"
          % ([results[n]["R"] for n in SHELLS],
             [R_EXPECT[n] for n in SHELLS]), ok_R, gate="G3")

    # the rejected P4 candidate, measured live (typed report)
    p4 = {}
    ok_lines = True
    for p in KNESER_PLACES:
        orbs, nlines = kg.orbit_reps(p, Mint % p)
        nb_orb = 0
        nb_lines = 0
        for g, osz in orbs:
            vadj = kg.adjust_isotropic_lift(
                np.asarray(g, dtype=np.int64), p)
            vec4, _r, _t = hal.marked_census_line(vadj, p)
            if vec4 == [84, 64, 28, 64]:
                nb_orb += 1
                nb_lines += osz
        p4[p] = (nb_orb, nb_lines)
        ok_lines &= (nb_lines
                     == results[p]["A"] * results[p]["B"] // 2)
    check("G3.2 P4 typed: type-B Weyl orbit counts (p = 3, 5, 7) = "
          "(%d, %d, %d) -- matches R at 3, 5, FAILS at 7 (13 != 10): "
          "small-place coincidence, NOT the microstate count; the "
          "type-B LINE counts equal A_p B_p / 2 at all three places "
          "(%s)" % (p4[3][0], p4[5][0], p4[7][0], ok_lines),
          p4[3][0] == 1 and p4[5][0] == 4 and p4[7][0] == 13
          and ok_lines, gate="G3")
    return p4


# ==================================================================== G4
def g4_trace(results, Mint):
    section("G4 -- trace consistency: a_n, sigma3, b = 2 A_p, "
            "n_B = A B / 2, the tower I_16 leg")
    ok_tr = all(results[n]["A"] - results[n]["B"] == A_N[n]
                and results[n]["A"] + results[n]["B"]
                == results[n]["s"] for n in SHELLS)
    check("G4.1 a_n = A_n - B_n and sigma3(n) = A_n + B_n on every "
          "shell: a = %s" % {n: results[n]["A"] - results[n]["B"]
                             for n in SHELLS}, ok_tr, gate="G4")

    Th = hal.build_thetas()
    ok_b = True
    ok_nb = True
    for p in KNESER_PLACES:
        orbs, nlines = kg.orbit_reps(p, Mint % p)
        S1 = [0, 0, 0, 0]
        n_B = 0
        for g, osz in orbs:
            vadj = kg.adjust_isotropic_lift(
                np.asarray(g, dtype=np.int64), p)
            vec4, _r, _t = hal.marked_census_line(vadj, p)
            for j in range(4):
                S1[j] += osz * vec4[j]
            if vec4 == [84, 64, 28, 64]:
                n_B += osz
        a_fit, b_fit, okfit = hal.fit_ab(Th, p, S1)
        A, B = results[p]["A"], results[p]["B"]
        ok_b &= (okfit and b_fit == 2 * A
                 and a_fit + b_fit * kg.sigma3(p) == nlines)
        ok_nb &= (n_B == A * B // 2)
        print("    p = %d: Kneser fit (a, b) = (%s, %s); b == 2 A_p = "
              "%d (%s); n_B = %d == A B / 2 = %d (%s)"
              % (p, a_fit, b_fit, 2 * A, b_fit == 2 * A, n_B,
                 A * B // 2, n_B == A * B // 2))
    check("G4.2 the affine Kneser T_p coefficient is TWICE the keep "
          "multiplicity: b = 2 A_p at p = 3, 5, 7 (live)", ok_b,
          gate="G4")
    check("G4.3 the special-line census counts the packet product: "
          "n_B = A_p B_p / 2 at p = 3, 5, 7 (live re-derivation of "
          "the sibling probe's identity)", ok_nb, gate="G4")

    # the (x) I_16 tower leg, re-verified live on the norm-9 layer
    ly9 = ram.Layer("(3)", (3, 0))
    res = hal.odd_layer_scan(ly9)
    check("G4.4 tower I_16 leg (live): norm-9 layer, ALL 820 "
          "submodules, iota-bar invertible, transport == "
          "iota-bar^{-1} on all 16 states (odd arrows move NO "
          "V-state; sibling probe: same for norms 5, 13, 49)",
          not res["viol"] and res["n_rank4"] == 820, gate="G4")
    return ok_tr and ok_b and ok_nb


# ==================================================================== C
def c_controls(fr, results):
    section("C -- must-fail controls")
    tab1 = fr["tab1"]
    sw1 = tab1[:, [1, 2, 3, 0]]                    # WRONG: 1-shift
    sw2 = tab1[:, [2, 3, 0, 1]]
    n = 3
    tab = results[n]["tab"]
    A, B = results[n]["A"], results[n]["B"]
    bad1 = np.array_equal(tab, A * tab1 + B * sw1)
    # LCG permutation of the 15 nonzero class patterns
    idx = [i for i in range(16) if tab1[i].sum()]
    perm = idx[:]
    for i in range(len(perm) - 1, 0, -1):
        j = lcg(i + 1)
        perm[i], perm[j] = perm[j], perm[i]
    tab1p = tab1.copy()
    for src, dst in zip(idx, perm):
        tab1p[dst] = tab1[src]
    bad2 = np.array_equal(tab, A * tab1p + B * tab1p[:, [2, 3, 0, 1]])
    fired1 = (not bad1) and (not bad2)
    CONTROL_FIRED["C1"] = fired1
    check("C1 scrambled parity: glue 1-shift fails the 64-cell "
          "verification (%s) and an LCG permutation of the 15 class "
          "patterns fails it too (%s)" % (not bad1, not bad2), fired1)

    Bs = [results[m]["B"] for m in SHELLS]
    g = 0
    for b in Bs:
        g = math.gcd(g, b)
    pow2 = g & (-g)
    n32 = [m for m in SHELLS if results[m]["B"] % 32 != 0]
    fired2 = (pow2 == 16 and all(b % 16 == 0 for b in Bs)
              and len(n32) >= 1)
    CONTROL_FIRED["C2"] = fired2
    check("C2 wrong block size: 2-content of gcd(B_n) = %d == 16 "
          "EXACTLY (gcd = %d); block 32 fails at n = %s; block 8 is "
          "non-maximal (gcd/16 = %d odd)"
          % (pow2, g, n32, g // 16), fired2)

    # C3 random arrow sets with the correct total
    N = int(tab.sum())
    rnd = np.zeros((16, 4), dtype=np.int64)
    for _ in range(N // 64):
        rnd[lcg(16), lcg(4)] += 64
    cls_tot = rnd.sum(axis=1)
    s = results[n]["s"]
    uni_bad = not (cls_tot[0] == 0
                   and all(int(cls_tot[i]) == 16 * s
                           for i in range(1, 16)))
    fac_bad = not np.array_equal(rnd, A * tab1 + B * sw2)
    fired3 = uni_bad and fac_bad
    CONTROL_FIRED["C3"] = fired3
    check("C3 random arrow sets (LCG, same total %d): V-uniformity "
          "breaks (%s) and the factorization breaks (%s)"
          % (N, uni_bad, fac_bad), fired3)


# ==================================================================== M
def m_entropy(results):
    section("M -- measurement: the sheet bit above the trace (frozen "
            "Shannon estimator; NO semantic claim)")
    for n in SHELLS:
        A, B, s = results[n]["A"], results[n]["B"], results[n]["s"]
        pA, pB = A / s, B / s
        h = -(pA * math.log2(pA) + pB * math.log2(pB))
        print("    n = %2d: packet mixture (A, B) = (%4d, %4d): sheet "
              "bit H = %.4f bits per packet event (trace a_n keeps "
              "only A - B)" % (n, A, B, h))
    print("    typed: bits of a channel mixture, not a decoded "
          "message (no free keys);\n    ROOTCLASS-MIXED (v775) fence "
          "respected -- no matter assignment.")


# ================================================================ verdict
def verdict():
    section("VERDICT")
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    n_all = len(CHECKS)
    print("%d/%d checks passed" % (n_pass, n_all))
    controls_ok = all(CONTROL_FIRED.get(c, False)
                      for c in ("C1", "C2", "C3"))
    if not GATE_FAIL and controls_ok and n_pass == n_all:
        v = "BROADCAST-EXACT"
    elif any(g.startswith("G2") for g in GATE_FAIL) and \
            len([g for g in GATE_FAIL if g.startswith("G2")]) \
            == len(SHELLS):
        v = "BROADCAST-DEAD"
    else:
        v = "BROADCAST-PARTIAL (%s%s)" % (
            ",".join(sorted(set(GATE_FAIL))) if GATE_FAIL
            else "non-gate check",
            "" if controls_ok else "; control void")
    print("VERDICT: %s" % v)
    if v == "BROADCAST-EXACT":
        print("""
HECKE.ARROW_MESSAGE.01 / C2-BROADCAST: BROADCAST-EXACT -- on every
tested odd shell n in {3, 5, 7, 9, 11, 13} the joint (V-class x glue)
arrow census factorizes EXACTLY as

    tab_n = A_n * tab_1 + B_n * tab_1^{sw},   sw = glue 2-shift,

i.e. T-bar_n = M_n (x) I_16 with M_n = [[A_n, B_n], [B_n, A_n]]: the
odd-shell arrows are sigma3(n) full 16-state copies of the unit root
packet -- A_n sheet-keep copies and B_n sheet-switch copies -- with
V-classes untouched by the switch (the broadcast), B_n = 16 R(n)
arrow-exactly (R = 1, 4, 10, 24, 43, 68), the trace a_n = A_n - B_n,
the Kneser affine coefficient b = 2 A_p, the special-line census
n_B = A_p B_p / 2, and the tower I_16 leg live (odd arrows move no
V-state).  The C2 parity is the packet/channel decomposition (typed:
no pointwise vector coloring claimed); "control plane at place 2 /
odd-prime broadcast" stays a [C neu] READING of this exact finite
factorization.""")
    print("total runtime %.1f s" % (time.time() - T0))
    return v


def main():
    print("=" * 74)
    print("HECKE.ARROW_MESSAGE.01 follow-up -- the C2 broadcast "
          "factorization test")
    print("=" * 74)
    g0_firewall()
    fr = s1_frame()
    tab3 = s2_parity_record(fr)
    results, _ok2 = g2_factorization(fr, tab3)
    hal.DVEC_ARR = DVEC
    Mint = hal.weyl_int_mats()
    g3_microstates(results, Mint)
    g4_trace(results, Mint)
    c_controls(fr, results)
    m_entropy(results)
    v = verdict()
    n_pass = sum(1 for _n, ok in CHECKS if ok)
    return 0 if (n_pass == len(CHECKS) and v == "BROADCAST-EXACT") \
        else 1


if __name__ == "__main__":
    sys.exit(main())
