#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""deep_blind_holdout_probe -- PRIME.PORT.DEEP.HOLDOUT.01
(EXPLORATION ONLY, experiments/; round 63, theorem-engineering on
the RH-side wall: the FIRST BLIND HOLDOUT of the frozen round-63
conjectures on genuinely NEW, DEEPER faithful rungs.  The deployed
v563 pipeline caps faithful rungs at X <= ATOM_MAX = 400000 (the
67-rung registered surface, h 142..1433).  This probe rebuilds the
IDENTICAL pipeline over a ten-times-deeper von Mangoldt table
(TAB_EXT = 4e6), wards the extension byte-exact against the
deployed table, and scores the frozen targets OUT-OF-SAMPLE on the
newly reachable rungs -- no refits, no constant moves, no
exclusions.  2026-08-11.)

WHAT IS BEING SCORED BLIND (all frozen upstream, before any deep
data existed):
 (1) HALFGAP (PRIME.PORT.HALFGAP.01 = CLI): the registered target
     n_h - q_h >= (1/2) mu1(h), mu1(h) = 4 sin^2(pi/(2h+1)); on
     this surface the pivot collapses (K v = m v => n - q = m
     along v, CXLIII ward), so the score is shat_h = m_h/mu1(h)
     >= 1/2 PER RUNG.  The registered no-adjustment clause applies
     verbatim: the constant is EXACTLY 1/2; a miss on any rung is
     a FIRST-CLASS FAIL of the registered conjecture -- it must
     NOT be repaired by adjusting the constant, by reweighting, or
     by excluding rungs; failures are reported per rung; the
     holdout verdict never edits the registration.  The registered
     surface is frozen as the 67-line registry sha256 ae292e55...
     (full hash in REG_SHA below); every scored rung here is
     OUTSIDE that registry.
 (2) HEADFLOOR-O1 + NET TAIL (PRIME.PORT.TAILSIGN.01 = CXLVII):
     on the deployed surface B-covering cuts exist on 67/67
     (n_minB med 17), tail_B <= 0 at the first B-covering cut on
     67/67, tail_A <= 0 at the first A-covering cut on 67/67, and
     head_B(cB) is O(1) vs m (slope +0.113, med 0.388).  Scored
     here: do B-covering cuts exist on the new rungs, does the
     net tail sign persist at the covering cuts (both
     bookkeepings), and does head_B(cB) stay O(1) (typed with the
     TAILSIGN bands PASS |s| <= 0.30 / RELOC s >= 0.70 / AMBIG)?
 (3) B-FLOOR + P_G DOMINANCE, FLOAT LEVEL (PRIME.PORT.BFLOOR.PG.01
     = CXLIV): on the deployed 39-step surface lam_min(B) >= 0.679
     and B >= (1/2) P_G + c_dom I with c_dom > 0 (canonical V4,
     s = 1/2) hold on 39/39.  Scored here on the NEW steps
     (consecutive new-rung pairs, pipeline verbatim): per step
     lam_min(B), float c_G = lam_min(P_G), float c_dom =
     lam_min(B - (1/2) P_G), negidx(B - (1/2) P_G), and c_B =
     (1/2) c_G + c_dom.  Typed BFLOOR-PERSISTS iff min lam_min(B)
     >= MINB_REF (1 - MINB_RTOL) with the deployed constants
     0.679 / 2e-2; DOM-PERSISTS iff negidx = 0 and c_B > 0 on
     every scoreable step.  FLOAT LEVEL DECLARED: no
     exact-rational LDL and no interval enclosure here -- this is
     the float-level persistence measurement only; the certified
     analogue is CXLIV/CXLIX/CLIII machinery and is NOT run at
     depth.
 (4) THE MARGIN LAW (rh_leverage_probe / CXLIII chain): lam_min ~
     h^p with p = -1.93 on the deployed ladder.  Scored here: the
     log-log fit on the deployed 67, on the new rungs alone, and
     combined; typed LAW-CONTINUES iff the combined exponent stays
     in the deployed band EXPO_BAND = [-2.5, -1.5] (halfgap W5
     band, frozen upstream).

HOW THE DEEP RUNGS ARE BUILT (conventions replicated, every copy
documented):
  * table: lam_ext = core.von_mangoldt_table(TAB_EXT) -- the
    DEPLOYED generator itself, called at the deeper cap (the
    v770/v771 "deep-table overlap EXACTLY" pattern); ward W1
    requires lam_ext[:ATOM_MAX+1] == core.LAM_TAB byte-exact,
    ward W2 requires the derived prefix arrays (_NN, U_ALL,
    MU_ALL, G_ALL) to agree bitwise on the deployed range, ward
    W3 requires the Chebyshev envelope kappa on [100, TAB_EXT] to
    stay <= KAPPA_REF + 1e-6 (v770 guard verbatim).
  * zones + frame: exactly core.build_window's conventions on the
    extended arrays -- alpha = U[kz], D = 0.5 G[kz]/NU_MAIN, M =
    ceil(alpha/D - 1e-9) + 1 rounded up to even, h = M/2, atoms =
    all table atoms with u <= 2 alpha + 1e-14, masses mu =
    2 Lambda(n)/sqrt(n).  The zone-horizon guard (ZONE_DEEP /
    NZ_DEEP) is never binding here: faithfulness X = e^{2 alpha}
    <= TAB_EXT caps n_zone at 2000 << the mirrored horizon.
  * faithful NEW rung: ATOM_MAX < X <= TAB_EXT and h in the
    DECLARED band H_HOLD = [128, 2900].  H_MIN = 128 is the
    deployed floor; the ceiling 2900 EXTENDS the deployed HCAP =
    1450 (disclosed AMENDMENT of the reachability frame, frozen
    before scoring; under the deployed HCAP only 3 new rungs
    exist -- the band is widened to make the holdout non-trivial;
    NO scoring rule, bar or constant is touched by this).  Census
    from the pre-freeze sizing run: 28 new rungs, kz 137..332,
    n_zone 641..1951, h 1219..2854, X 4.19e5..3.81e6.
  * per-rung objects: c_at = core.atom_lags_at (tent assembly
    verbatim), c_ar = core.arch_lags, K = core.odd_toeplitz, ONE
    eigh per rung (eigenvalues + eigenvectors -- the registry
    convention; eigvalsh takes a different LAPACK path and moves
    the 12th printed digit, measured in sizing); weights Wv =
    core.lag_weights_from_v(v, h); the head/tail bookkeepings A
    and B verbatim from tail_sign_mechanism_probe (cuts inclusive
    at atom positions, PNT grid NG_SMOOTH = 6000 midpoints); the
    P_G chain verbatim from bfloor_pg_dominance_probe
    (grid_density FFT -> folded_measure -> lanczos_chain(h+1) ->
    eval_chain -> CD-Gram co-block in the r1 Householder frame,
    CORE_J = (2,...,16), steps = consecutive full-core pairs with
    r1 all-PSD).  The deployed step ladder caps H_LADDER_MAX =
    900; the new steps live at h 1219..2854 -- the SAME disclosed
    band amendment as above, machinery untouched.

FROZEN PROTOCOL:

 W   FIDELITY WARDS (kill -> WARD-BROKEN):
     W1 deep-table overlap: lam_ext[:ATOM_MAX+1] == core.LAM_TAB
        EXACTLY (max abs dev == 0.0);
     W2 prefix arrays bitwise: NN/U/MU prefixes equal, G prefix
        equal on the deployed length - 1;
     W3 extended Chebyshev envelope kappa <= KAPPA_REF + 1e-6;
     W4 CONVENTION REGRESSION (3 deployed rungs REG_KZ = (9, 60,
        121) rebuilt THROUGH THE EXTENDED PIPELINE): frame ties
        (h, M, D, alpha, n_atom) exact; lam_min and the tangent
        scalars (a11, a22, a12, det Ahat of the 2x2 frame-A read)
        agree with the deployed core.build_window output to
        <= REG_WARD = 1e-12 relative (bit-agreement expected);
     W5 REGISTRY REPRODUCTION (deployed pipeline verbatim, kz
        2..150, H_MIN <= h <= HCAP, X <= ATOM_MAX): 67 rungs,
        registry sha256 == REG_SHA (the CLI frozen registry),
        CXLIII band shat min/med/max == 0.502/1.027/2.185 (rtol
        2e-2), margin exponent in EXPO_BAND.
     W6 WARD split exactness on the new rungs: |e_ar + e_t - m|
        and the full-scan identities (head_B + tail_B = m, G +
        tail_A = m) <= SCAN_WARD relative.

 D   THE NEW SURFACE (typed): census of all new rungs (kz,
     n_zone, h, X, atoms); NEW-SURFACE(count, h range); kill K1
     iff count < MIN_NEW = 10.

 H1  HALFGAP BLIND SCORE (typed, never kill; the headline): per
     new rung shat = m/mu1(h), margin = shat - 1/2, PASS iff shat
     >= 1/2; full table printed; typed
     HALFGAP-HOLDOUT-PASS(n/N, min margin, tightest rungs) iff
     all pass, else HALFGAP-HOLDOUT-FAIL(k, list) -- a
     first-class FAIL of the registered conjecture, reported
     plainly, NO adjustment.

 H2  HEADFLOOR + NET-TAIL PERSISTENCE (typed): per new rung the
     first A- and B-covering cuts (cert_A > 0 / cert_B > 0),
     tail_A <= 0 at cA, tail_B <= 0 at cB, n_minB ladder,
     head_B(cB) stats (deployed context: med 0.388), TYPED screen
     jackknife slope of log head_B(cB) vs log m on the new rungs:
     HEADFLOOR-O1(|s| <= 0.30) / HEADFLOOR-RELOC(s >= 0.70) /
     HEADFLOOR-AMBIG.

 H3  B-FLOOR / P_G DOMINANCE, FLOAT (typed): the new-rung gram
     ladder (chain machinery verbatim), steps = consecutive
     full-core pairs (r1 all-PSD, lamS > 0); per step lam_min(B),
     c_G, c_dom = lam_min(B - (1/2) P_G), negidx, c_B; typed
     BFLOOR-PERSISTS(min lam_min(B)) iff min >= MINB_REF (1 -
     MINB_RTOL), else BFLOOR-HOLDOUT-FAIL(min);
     DOM-PERSISTS(n/n, min c_B) iff negidx = 0 and c_B > 0
     everywhere scoreable, else DOM-HOLDOUT-FAIL(k).  Chain-short
     / core-missing rungs are reported and typed as SKIPPED (an
     honest reachability limit, not a pass and not a fail).

 H4  MARGIN-LAW CONTINUATION (typed): jackknife log-log fits of
     m vs h -- deployed 67 / new-only / combined; typed
     LAW-CONTINUES(p_comb) iff p_comb in EXPO_BAND, else
     LAW-BREAKS(p_comb).

 C   CONTROLS (kill -> WARD-BROKEN if silent): on the FIRST new
     rung (by (h, kz); sizing says kz 177, h 1219): C1 scramble
     (seed 1, uniform positions in (0, 2 alpha], SAME masses)
     must break the wall (lam_min < 0, hence shat < 1/2) AND have
     zero covering cuts in both bookkeepings; C2 smooth comb (PNT
     grid masses on the SAME window) must do the same; C3 the
     smooth-world gram chain at that rung must violate the wall
     (neg(A) > 0) or die (chain short / core missing) -- the
     P_G-chain scoring cannot be faked by a prime-free comb.
     DECLARED SKIP: the Epstein x^2+5y^2 control is NOT run at
     depth (its divisor recursion is O(X^2), infeasible at X ~
     8e5); the deployed Epstein control lives at kz 9 inside the
     frozen upstream probes and is not re-run here.  The W4
     3-rung regression doubles as the convention control.

KILLS: K1 (D, MIN_NEW) -> PIPELINE-BROKEN; K2 (W1-W6, C1-C3) ->
WARD-BROKEN.  All H1-H4 outcomes are typed measurements, never
kills: a FAIL label is a first-class reported result.

VERDICT (frozen enum): DEEPHOLDOUT-SCORED with typed sublabels
FIDELITY(overlap, regression, registry sha8),
NEW-SURFACE(count, h range),
HALFGAP-HOLDOUT-PASS(n/N, min margin)/HALFGAP-HOLDOUT-FAIL(k),
HEADFLOOR-HOLDOUT(BCOVER n/N, NETB n/N, NETA n/N, slope label),
BFLOOR-PERSISTS(min)/BFLOOR-HOLDOUT-FAIL(min) +
DOM-PERSISTS(n/n)/DOM-HOLDOUT-FAIL(k) [+ SKIPPED(k)],
LAW-CONTINUES(p)/LAW-BREAKS(p),
CONTROLS-FIRE(k/3); else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: TAB_EXT = 4_000_000; H_HOLD = (128, 2900) (declared
band; HCAP extension disclosed above); MIN_NEW = 10; KZ_SCAN_MAX
= 400; REG_KZ = (9, 60, 121); REG_WARD = 1e-12; REG_SHA =
"ae292e557efa24f13fa1d75823219bcda9a0f6757089fee459e5c652e3458df8"
(the CLI registry, 67 lines "kz:h:shat(%.12e)"); SHAT_REF =
(0.502, 1.027, 2.185), rtol 2e-2; EXPO_BAND = (-2.5, -1.5);
HALF = 1/2 EXACT (registered upstream, NO-ADJUST); SCAN_WARD =
1e-8 (relative; the deployed TAILSIGN bar is 1e-9 at <= 33k
atoms -- one digit of depth allowance for up to 271k atoms,
declared BEFORE the frozen run); NG_SMOOTH = 6000; MINB_REF =
0.679, MINB_RTOL = 2e-2; PG_S = 1/2 (canonical V4, frozen
upstream); CORE_J = (2,...,16); SLOPE_PASS = 0.30, SLOPE_RELOC =
0.70; CTRL scramble seed 1; runtime cap declared: 30 min.

ANTI-CIRCULARITY (frozen): the constant 1/2, the HEADFLOOR bands,
the B-floor class 0.679 and the dominance shape s = 1/2 are all
frozen UPSTREAM in the registered probes, before any deep data;
nothing here is fit to the new rungs; mu1 is pure geometry; the
new rungs are scored and never feed back into any registered
object; the holdout verdict never edits the registration.

PRE-FREEZE SIZING DISCLOSURE (2026-08-11, before the spec was
frozen): a sizing run built the extended table (overlap dev 0.0),
counted the band census (28 rungs; 3 under the deployed HCAP;
list frozen into this spec), timed the deep pipeline (deepest
eigh 1.3 s, deepest Lanczos 8.0 s), and -- unavoidably, since the
timing ran the rung end-to-end -- SAW TWO HOLDOUT VALUES before
freezing: kz 177/h 1219 shat 1.3048 and kz 222/h 2854 shat
0.7232 (both above 1/2).  Disclosed in full: the scoring constant
was frozen upstream (CLI) and cannot move, no bar/band/enum of
this spec was chosen after seeing them (the band H_HOLD and all
wards were fixed by the census geometry and the deployed
constants), and the remaining 26 rungs were NOT computed before
the freeze.  The sizing run also recomputed the deployed registry
sha (eigh path) = REG_SHA, confirming the CLI prefix ae292e55.

SMOKE-RUN DISCLOSURE (2026-08-11, before freezing): one smoke run
(DEEPHOLD_SMOKE=1, the 2 shallowest new rungs end-to-end, 14/14,
16.5 s) measured: wards W1-W6 green (overlap 0.0, prefix bitwise,
kappa within guard, W4 regression max rel dev 0.0e+00 BIT-EXACT
on all 3 rungs, registry sha == REG_SHA, scan ward 2.7e-14 <<
1e-8); smoke rungs kz 177/h 1219 shat 1.3047882108 PASS and kz
243/h 1292 shat 1.2442150312 PASS (two further holdout values
seen, the declared purpose of the smoke); both A- and B-covered
(n_minA 9/13, n_minB 41/59), tail_A <= 0 at cA and tail_B <= 0
at cB on 2/2, head_B(cB) 0.4004/0.2579 (deployed med 0.388); the
HEADFLOOR screen is VACUOUS at n = 2 (jackknife R^2 nan -- the
typed label resolves only on the full census); 1 smoke step:
lam_min(B) 3.9638, c_G 0.9551, c_dom +3.4638, negidx 0, c_B
3.9414; combined law p = -1.926; controls: scramble lam_min
-9.1e+02, smooth -9.6e+00, both with zero A/B coverage, smooth
gram chain neg(A) = 13 -- all three fire.  NO bar, band, count,
rule or enum was moved after the smoke.

SPEC v1 (2026-08-11, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v1: (i)
one eigh per rung (eigenvalues + vectors), registry format
"%d:%d:%.12e"; (ii) covering cuts inclusive at atom positions
(u_n <= u_c); first covering cut = argmax(cert > 0); (iii)
jackknife = full leave-one-out, CI +- 2SE; (iv) the head_B(cB)
screen reads the positive-cert subset; (v) steps sorted by
(h, kz), consecutive pairs, r1 must be full-core all-PSD with
lamS > 0; (vi) negidx = count of eigenvalues < 0 (float sign, no
tolerance); (vii) scramble = rng.default_rng(1).uniform(0,
2 alpha, ka), sorted, same masses.

HONEST LIMITS (frozen): all new-rung objects are FLOAT-LEVEL --
no interval rollout, no exact-rational certificates at depth (the
CLIII interval machinery is not rerun here; its band ends at h ~
900); the H band extension beyond the deployed HCAP is a declared
reachability amendment, not a convention change; the Epstein
control is skipped at depth (declared above); the P_G-chain
step ladder extends H_LADDER_MAX = 900 by the same declared
amendment; a PASS census on 28 rungs proves nothing about deeper
h, ideal objects, or any tail statement.  NO RH claim.  No
marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime; the extended table comes from the deployed sieve
generator, not an oracle); v563 READ-ONLY; RNG only inside the
declared scramble control; stdout only.

Sources (read-only): v563_paper2_readouts (table generator, tent
assembly, arch lags, odd Toeplitz, frame conventions);
halfgap_registration_probe (CLI: registered target + holdout
protocol + registry sha); tail_sign_mechanism_probe (CXLVII:
bookkeepings + HEADFLOOR bands); bfloor_pg_dominance_probe
(CXLIV: gram/chain/P_G machinery + B-floor constants);
rh_leverage_probe (margin-law fit); v770_qf_spectral_bundle
(deep-table overlap ward pattern).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/deep_blind_holdout_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..",
                                       "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import v563_paper2_readouts as core        # noqa: E402  (READ-ONLY)

TAB_EXT = 4_000_000
H_HOLD = (128, 2900)
MIN_NEW = 10
KZ_SCAN_MAX = 400
REG_KZ = (9, 60, 121)
REG_WARD = 1e-12
REG_SHA = ("ae292e557efa24f13fa1d75823219bcda9a0f6757089fee459e"
           "5c652e3458df8")
SHAT_REF = (0.502, 1.027, 2.185)
SHAT_RTOL = 2e-2
EXPO_BAND = (-2.5, -1.5)
HALF = Fraction(1, 2)
SCAN_WARD = 1e-8
NG_SMOOTH = 6000
MINB_REF = 0.679
MINB_RTOL = 2e-2
PG_S = 0.5
CORE_J = (2, 4, 6, 8, 10, 12, 14, 16)
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
SCRAMBLE_SEED = 1
SMOKE = os.environ.get("DEEPHOLD_SMOKE", "") == "1"
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


def ols_line(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    vx = float(np.var(x))
    if vx == 0.0:
        return float(np.mean(y)), 0.0, float("nan")
    b = float(np.cov(x, y, bias=True)[0, 1] / vx)
    a = float(np.mean(y) - b * np.mean(x))
    ss = float(np.sum((y - a - b * x) ** 2))
    st = float(np.sum((y - np.mean(y)) ** 2))
    return a, b, (1.0 - ss / st if st > 0 else float("nan"))


def jack_slope(x, y):
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    _a, b, r2 = ols_line(x, y)
    n = len(x)
    bb = []
    for i in range(n):
        m = np.ones(n, bool)
        m[i] = False
        bb.append(ols_line(x[m], y[m])[1])
    bb = np.array(bb)
    se = math.sqrt((n - 1) / n * float(np.sum((bb - bb.mean())
                                              ** 2)))
    return b, se, r2


def mu1_of(h):
    return 4.0 * math.sin(math.pi / (2.0 * h + 1.0)) ** 2


def q_read(W, u, D, M):
    """tail_sign_mechanism_probe verbatim."""
    u = np.asarray(u, float)
    i0 = np.floor(u / D).astype(int)
    f = u / D - i0
    val = np.zeros_like(u)
    ok0 = (i0 >= 0) & (i0 < M)
    val[ok0] += (1.0 - f[ok0]) * W[i0[ok0]]
    ok1 = (i0 + 1 >= 0) & (i0 + 1 < M)
    val[ok1] += f[ok1] * W[i0[ok1] + 1]
    refl = u < D
    val[refl] += (1.0 - u[refl] / D) * W[0]
    return -0.5 * val


def smooth_comb(alpha, ng=NG_SMOOTH):
    ug = (np.arange(ng) + 0.5) * (2.0 * alpha / ng)
    mg = 2.0 * np.exp(ug / 2.0) * (2.0 * alpha / ng)
    return ug, mg


# ------------- P_G chain machinery (bfloor_pg_dominance verbatim)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


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


def householder_frame(v):
    n = len(v)
    v = v / float(np.linalg.norm(v))
    e1 = np.zeros(n)
    e1[0] = 1.0
    u = e1 - v
    nu = float(np.linalg.norm(u))
    if nu < 1e-14:
        return np.eye(n)
    u = u / nu
    Q = np.eye(n) - 2.0 * np.outer(u, u)
    if float(Q[:, 0] @ v) < 0:
        Q = -Q
    return Q


# ---------------- the extended surface (frame conventions verbatim)
EXT = {}


def build_ext_tables():
    lam_ext = core.von_mangoldt_table(TAB_EXT)
    NN = np.nonzero(lam_ext > 0.0)[0]
    EXT["lam"] = lam_ext
    EXT["NN"] = NN
    EXT["U"] = np.log(NN.astype(float))
    EXT["MU"] = 2.0 * lam_ext[NN] / np.sqrt(NN.astype(float))
    EXT["G"] = np.diff(EXT["U"])
    return lam_ext


def ext_frame(kz):
    """core.build_window frame conventions on the extended arrays."""
    alpha = float(EXT["U"][kz])
    D_k = 0.5 * float(EXT["G"][kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    hz = Mz // 2
    ka = int(np.searchsorted(EXT["U"], 2.0 * alpha + 1.0e-14,
                             side="right"))
    return alpha, Mz, hz, ka


def ext_rung(kz, positions=None, masses=None):
    """One extended-pipeline rung: eigh + both tail bookkeepings
    (tail_sign_mechanism_probe build_rung, re-hosted on the
    extended arrays; identical formulas)."""
    alpha, M, h, ka = ext_frame(kz)
    uu = EXT["U"][:ka].copy() if positions is None else positions
    mm = EXT["MU"][:ka].copy() if masses is None else masses
    c_at, D = core.atom_lags_at(alpha, M, uu, mm)
    c_at = np.asarray(c_at, float)
    c_ar = np.asarray(core.arch_lags(M, D), float)
    Kt = core.odd_toeplitz(c_ar + c_at, M)
    w, V = np.linalg.eigh(Kt)
    v = V[:, 0]
    del Kt, V
    row = dict(kz=kz, nz=int(EXT["NN"][kz]), alpha=alpha, h=h,
               M=M, D=D, ka=ka, X=math.exp(2.0 * alpha),
               m=float(w[0]), mu1=mu1_of(h), uu=uu)
    Wv = core.lag_weights_from_v(v, h)
    e_ar = float(c_ar @ Wv)
    e_t = float(c_at @ Wv)
    ug, mg = smooth_comb(alpha)
    c_sm = np.asarray(core.atom_lags_at(alpha, M, ug, mg)[0],
                      float)
    e_s = float(c_sm @ Wv)
    qa = mm * q_read(Wv, uu, D, M)
    qg = mg * q_read(Wv, ug, D, M)
    lift = e_t - e_s
    demand = -(e_ar + e_s)
    cq = np.cumsum(qa)
    idxg = np.searchsorted(ug, uu, side="right")
    cg_all = np.concatenate([[0.0], np.cumsum(qg)])
    head_err = cq - cg_all[idxg]
    G = head_err - demand
    tail_A = lift - head_err
    cert_A = G - np.abs(tail_A)
    head_B = e_ar + cq
    tail_B = float(qa.sum()) - cq
    cert_B = head_B - np.abs(tail_B)
    row.update(e_ar=e_ar, e_t=e_t, e_s=e_s, lift=lift,
               demand=demand, cert_A=cert_A, tail_A=tail_A,
               head_B=head_B, tail_B=tail_B, cert_B=cert_B,
               c_at=c_at, c_ar=c_ar,
               dev_id=abs((e_ar + e_t) - row["m"])
               / max(1.0, abs(e_t)),
               dev_scan=max(
                   float(np.max(np.abs((head_B + tail_B)
                                       - row["m"]))),
                   float(np.max(np.abs((G + tail_A)
                                       - row["m"]))))
               / max(1.0, abs(e_t)))
    return row


def ext_gram(kz, c_lags=None, keep_chain=True):
    """bfloor_pg_dominance gram_anatomy verbatim, on the extended
    frame; c_lags = precomputed c_ar + c_at (or a control's)."""
    alpha, M, h, ka = ext_frame(kz)
    if c_lags is None:
        c_at, D = core.atom_lags_at(alpha, M, EXT["U"][:ka],
                                    EXT["MU"][:ka])
        c_ar = np.asarray(core.arch_lags(M, D), float)
        c_lags = c_ar + np.asarray(c_at, float)
    d = grid_density(c_lags)
    L = 2 * M - 2
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, uf_n = folded_measure(d, L, -1.0)
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0):
        return None
    Pn = eval_chain(al, be, m0, ys, h)
    G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
    G = 0.5 * (G + G.T)
    n = G.shape[0]
    A = np.eye(n) - G
    evA = np.linalg.eigvalsh(A)
    out = dict(kz=kz, h=h, n=n, alpha=alpha, M=M)
    out["tau"] = float(evA[0])
    out["negA"] = int(np.sum(evA < 0.0))
    if keep_chain:
        out["chain"] = (al, be, m0)
    idx = {int(j): k for k, j in enumerate(uf_n)}
    out["core_ok"] = all(j in idx for j in CORE_J)
    if not out["core_ok"]:
        return out
    ic = np.array([idx[j] for j in CORE_J], dtype=int)
    icset = set(ic.tolist())
    ib = np.array([k for k in range(n) if k not in icset],
                  dtype=int)
    B = A[np.ix_(ic, ic)]
    Xc = A[np.ix_(ic, ib)]
    R = A[np.ix_(ib, ib)]
    evR = np.linalg.eigvalsh(R)
    out["negR"] = int(np.sum(evR < 0.0))
    Z = np.linalg.solve(R, Xc.T)
    Y = Xc @ Z
    Y = 0.5 * (Y + Y.T)
    S = B - Y
    S = 0.5 * (S + S.T)
    evS = np.linalg.eigvalsh(S)
    out["S"] = S
    out["lamS"] = float(evS[0])
    out["negS"] = int(np.sum(evS < 0.0))
    if keep_chain:
        out["y_core"] = np.array([ys[idx[j]] for j in CORE_J])
        out["v_core"] = np.array([vs[idx[j]] for j in CORE_J])
    return out


def build_pg_step(r1, r2):
    """One step of the P_G chain (bfloor E-block verbatim, s from
    PG_S): frame from r1's soft direction, B = 7x7 co-block of
    Q^T (S_2/tau_1) Q, P_G from r2's own chain at r2's core
    nodes."""
    wS, VS = np.linalg.eigh(r1["S"])
    Q = householder_frame(VS[:, 0])
    Mt = Q.T @ (r2["S"] / r1["tau"]) @ Q
    Mt = 0.5 * (Mt + Mt.T)
    B = Mt[1:, 1:]
    al, be, m0 = r2["chain"]
    Pc = eval_chain(al, be, m0, r2["y_core"], r2["h"])
    Gc = (np.sqrt(r2["v_core"])[:, None] * (Pc @ Pc.T)
          * np.sqrt(r2["v_core"])[None, :])
    Gc = 0.5 * (Gc + Gc.T)
    PG = (Q.T @ Gc @ Q)[1:, 1:]
    PG = 0.5 * (PG + PG.T)
    minB = float(np.linalg.eigvalsh(B)[0])
    cg = float(np.linalg.eigvalsh(PG)[0])
    Dm = B - PG_S * PG
    Dm = 0.5 * (Dm + Dm.T)
    evd = np.linalg.eigvalsh(Dm)
    return dict(kz=r2["kz"], h=r2["h"], minB=minB, cg=cg,
                cdom=float(evd[0]), negD=int(np.sum(evd < 0.0)),
                cb=PG_S * cg + float(evd[0]), tau=r1["tau"])


def deployed_registry():
    """halfgap_registration_probe W-block verbatim (deployed
    pipeline): the 67-rung faithful ladder + registry sha."""
    rungs = []
    for kz in range(2, 151):
        try:
            rr = core.build_window(kz)
        except Exception:
            continue
        if not (core.H_MIN <= rr["h"] <= core.HCAP):
            continue
        if rr["X"] > core.ATOM_MAX:
            continue
        alpha, M, D, h = rr["alpha"], rr["M"], rr["D"], rr["h"]
        uu = np.asarray(rr["uu"], float)
        mu = 2.0 * np.asarray(rr["lam"], float)
        c_at = np.asarray(core.atom_lags_at(alpha, M, uu, mu)[0],
                          float)
        c_ar = np.asarray(core.arch_lags(M, D), float)
        Kt = core.odd_toeplitz(c_ar + c_at, M)
        w, V = np.linalg.eigh(Kt)
        rungs.append(dict(kz=kz, h=h, m=float(w[0]),
                          shat=float(w[0]) / mu1_of(h)))
        del Kt, V
    rungs.sort(key=lambda r: (r["h"], r["kz"]))
    lines = "\n".join("%d:%d:%.12e" % (r["kz"], r["h"], r["shat"])
                      for r in rungs)
    return rungs, hashlib.sha256(lines.encode("utf-8")).hexdigest()


def first_cut(nn_atoms, cert):
    cov = cert > 0.0
    if not bool(np.any(cov)):
        return -1, -1
    i0 = int(np.argmax(cov))
    return i0, int(nn_atoms[i0])


def main():
    section("PRIME.PORT.DEEP.HOLDOUT.01 -- blind holdout deepening:"
            " the frozen round-63 targets scored out-of-sample on "
            "the 4e6-table rungs (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves; no refits -- the "
          "constant 1/2, the HEADFLOOR bands, the 0.679 class and "
          "s = 1/2 are frozen upstream.")
    if SMOKE:
        print("    *** SMOKE MODE: 2 shallowest new rungs only ***")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- fidelity wards: the extension IS the deployed "
            "pipeline")
    lam_ext = build_ext_tables()
    dev = float(np.max(np.abs(lam_ext[:core.ATOM_MAX + 1]
                              - core.LAM_TAB)))
    check("W1 deep-table overlap: extended von Mangoldt table == "
          "deployed core table on [0, %d] EXACTLY (max abs dev "
          "%.1e)" % (core.ATOM_MAX, dev), dev == 0.0, kill="K2")
    nP = len(core.U_ALL)
    ok_pref = (np.array_equal(EXT["NN"][:nP], core._NN)
               and np.array_equal(EXT["U"][:nP], core.U_ALL)
               and np.array_equal(EXT["MU"][:nP], core.MU_ALL)
               and np.array_equal(EXT["G"][:nP - 1],
                                  core.G_ALL[:nP - 1]))
    check("W2 prefix arrays bitwise: NN/U/MU on %d entries, G on "
          "%d" % (nP, nP - 1), ok_pref, kill="K2")
    psi = np.cumsum(lam_ext[EXT["NN"]])
    nnf = EXT["NN"].astype(float)
    keep = nnf >= core.KAPPA_X0
    kappa = float(np.max(np.abs(psi[keep] - nnf[keep])
                         / nnf[keep]))
    check("W3 extended Chebyshev envelope: kappa = %.6f <= %.6f "
          "+ 1e-6 on [%d, %d]"
          % (kappa, core.KAPPA_REF, int(core.KAPPA_X0), TAB_EXT),
          kappa <= core.KAPPA_REF + 1e-6, kill="K2")

    # W4: convention regression through the extended pipeline
    dev_reg = 0.0
    reg_rows = []
    for kz in REG_KZ:
        rr = core.build_window(kz)
        alpha, M, h = rr["alpha"], rr["M"], rr["h"]
        uu_d = np.asarray(rr["uu"], float)
        mu_d = 2.0 * np.asarray(rr["lam"], float)
        c_at_d = np.asarray(core.atom_lags_at(alpha, M, uu_d,
                                              mu_d)[0], float)
        c_ar_d = np.asarray(core.arch_lags(M, rr["D"]), float)
        lam_d = float(np.linalg.eigh(
            core.odd_toeplitz(c_ar_d + c_at_d, M))[0][0])
        a_e, M_e, h_e, ka_e = ext_frame(kz)
        ok_frame = (a_e == alpha and M_e == M and h_e == h
                    and ka_e == rr["n_atom"])
        c_at_e, D_e = core.atom_lags_at(a_e, M_e, EXT["U"][:ka_e],
                                        EXT["MU"][:ka_e])
        c_at_e = np.asarray(c_at_e, float)
        c_ar_e = np.asarray(core.arch_lags(M_e, D_e), float)
        lam_e = float(np.linalg.eigh(
            core.odd_toeplitz(c_ar_e + c_at_e, M_e))[0][0])
        # tangent scalars through the extended pipeline
        Tb = core.parity_basis(h_e, 2)
        t1, t2 = Tb[0].copy(), Tb[1].copy()
        W11 = core.lag_weights_from_v(t1, h_e)
        W22 = core.lag_weights_from_v(t2, h_e)
        Wpp = core.lag_weights_from_v(t1 + t2, h_e)
        W12 = 0.5 * (Wpp - W11 - W22)
        B2 = np.array([[float(c_ar_e @ W11), float(c_ar_e @ W12)],
                       [float(c_ar_e @ W12),
                        float(c_ar_e @ W22)]])
        lamw = 0.5 * EXT["MU"][:ka_e]
        Xn = np.empty((ka_e, 3))
        for i in range(ka_e):
            Xn[i, 0] = core.spline_project(W11, EXT["U"][i], D_e,
                                           M_e)
            Xn[i, 1] = core.spline_project(W22, EXT["U"][i], D_e,
                                           M_e)
            Xn[i, 2] = core.spline_project(W12, EXT["U"][i], D_e,
                                           M_e)
        S2 = np.array([[float(lamw @ Xn[:, 0]),
                        float(lamw @ Xn[:, 2])],
                       [float(lamw @ Xn[:, 2]),
                        float(lamw @ Xn[:, 1])]])
        Ah = B2 - S2
        det_e = float(np.linalg.det(Ah))
        devs = [abs(lam_e - lam_d) / max(abs(lam_d), 1e-300),
                abs(Ah[0, 0] - rr["a11"]) / max(abs(rr["a11"]),
                                                1e-300),
                abs(Ah[1, 1] - rr["a22"]) / max(abs(rr["a22"]),
                                                1e-300),
                abs(Ah[0, 1] - rr["a12"]) / max(abs(rr["a12"]),
                                                1e-300),
                abs(det_e - rr["det"]) / max(abs(rr["det"]),
                                             1e-300)]
        dev_reg = max(dev_reg, max(devs))
        reg_rows.append((kz, h, ok_frame, max(devs)))
        print("    kz %3d h %4d: frame tie %s; lam_min dev %.1e; "
              "tangent scalars (a11, a22, a12, det) max dev %.1e"
              % (kz, h, ok_frame, devs[0], max(devs[1:])),
              flush=True)
    check("W4 CONVENTION REGRESSION: 3 deployed rungs rebuilt "
          "through the extended pipeline; frame ties exact, max "
          "rel dev %.2e <= %.0e (bit-agreement expected)"
          % (dev_reg, REG_WARD),
          all(o for _k, _h, o, _d in reg_rows)
          and dev_reg <= REG_WARD, kill="K2")

    # W5: the deployed registry reproduced verbatim
    reg_rungs, reg_sha = deployed_registry()
    shat_d = np.array([r["shat"] for r in reg_rungs])
    trio = (float(shat_d.min()), float(np.median(shat_d)),
            float(shat_d.max()))
    ok_band = all(abs(a / b - 1.0) <= SHAT_RTOL
                  for a, b in zip(trio, SHAT_REF))
    m_d = np.array([r["m"] for r in reg_rungs])
    h_d = np.array([float(r["h"]) for r in reg_rungs])
    p_dep, se_dep, r2_dep = jack_slope(np.log(h_d), np.log(m_d))
    check("W5 REGISTRY REPRODUCTION: %d rungs, sha256 %s.. == "
          "ae292e55.. (%s); band %.3f/%.3f/%.3f == "
          "0.502/1.027/2.185; exponent %+.3f in [%.1f, %.1f]  "
          "[%.1f s]"
          % (len(reg_rungs), reg_sha[:8],
             "MATCH" if reg_sha == REG_SHA else "MISMATCH",
             trio[0], trio[1], trio[2], p_dep, EXPO_BAND[0],
             EXPO_BAND[1], time.time() - T0),
          len(reg_rungs) == 67 and reg_sha == REG_SHA and ok_band
          and EXPO_BAND[0] <= p_dep <= EXPO_BAND[1], kill="K2")
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ D
    section("D -- the new surface: faithful rungs with ATOM_MAX < "
            "X <= %d, h in [%d, %d]" % (TAB_EXT, H_HOLD[0],
                                        H_HOLD[1]))
    new_kz = []
    for kz in range(2, min(KZ_SCAN_MAX, len(EXT["NN"]) - 2)):
        alpha = float(EXT["U"][kz])
        X = math.exp(2.0 * alpha)
        if X > TAB_EXT:
            break
        if X <= core.ATOM_MAX:
            continue
        _a, _M, h, _ka = ext_frame(kz)
        if not (H_HOLD[0] <= h <= H_HOLD[1]):
            continue
        new_kz.append(kz)
    rows = []
    order = sorted(new_kz, key=lambda k: (ext_frame(k)[2], k))
    if SMOKE:
        order = order[:2]
    for kz in order:
        r = ext_rung(kz)
        rows.append(r)
        print("    NEW kz %3d n_zone %5d h %5d X %.4g atoms %6d  "
              "[%.1f s]" % (r["kz"], r["nz"], r["h"], r["X"],
                            r["ka"], time.time() - T0), flush=True)
    N = len(rows)
    check("D1 new-surface census: %d new rungs (>= %d), h %d..%d, "
          "every one OUTSIDE the ae292e55 registry (kz range "
          "%d..%d disjoint from the 67 registered kz <= 136)"
          % (N, MIN_NEW if not SMOKE else 2, rows[0]["h"],
             rows[-1]["h"], min(r["kz"] for r in rows),
             max(r["kz"] for r in rows)),
          N >= (MIN_NEW if not SMOKE else 2), kill="K1")
    if KILLS:
        return finish({})
    dev_id = max(r["dev_id"] for r in rows)
    dev_sc = max(r["dev_scan"] for r in rows)
    check("W6 WARD split exactness on the new rungs: |e_ar + e_t "
          "- m| rel %.2e, full scans (head_B + tail_B = m, G + "
          "tail_A = m) rel %.2e <= %.0e"
          % (dev_id, dev_sc, SCAN_WARD),
          max(dev_id, dev_sc) <= SCAN_WARD, kill="K2")
    if KILLS:
        return finish({})

    # ----------------------------------------------------------- H1
    section("H1 -- THE BLIND HALFGAP SCORE: shat >= 1/2 per rung "
            "(constant EXACTLY 1/2, NO-ADJUST, frozen upstream)")
    c_half = float(HALF)
    print("    kz   n_zone  h     alpha     m            mu1      "
          "    shat          margin      score")
    fails = []
    for r in rows:
        s = r["m"] / r["mu1"]
        r["shat"] = s
        ok = s >= c_half
        if not ok:
            fails.append(r)
        print("    %-4d %-6d %-5d %.4f  %.6e %.6e %.10f %+.6e  %s"
              % (r["kz"], r["nz"], r["h"], r["alpha"], r["m"],
                 r["mu1"], s, s - c_half,
                 "PASS" if ok else "FAIL"), flush=True)
    margins = np.array([r["shat"] - c_half for r in rows])
    o3 = np.argsort(margins)[:3]
    tight = ", ".join("kz%d/h%d %+.2e"
                      % (rows[i]["kz"], rows[i]["h"], margins[i])
                      for i in o3)
    print("\n    margins: min/med/max %+.4f/%+.4f/%+.4f; tightest:"
          " %s" % (float(margins.min()), float(np.median(margins)),
                   float(margins.max()), tight))
    if fails:
        h1 = ("HALFGAP-HOLDOUT-FAIL(%d/%d: %s) -- a FIRST-CLASS "
              "FAIL of the registered conjecture; the "
              "no-adjustment clause applies (no repair, no "
              "exclusion, no constant move)"
              % (len(fails), N,
                 ", ".join("kz%d/h%d shat %.6f" %
                           (r["kz"], r["h"], r["shat"])
                           for r in fails)))
    else:
        h1 = ("HALFGAP-HOLDOUT-PASS(%d/%d, min margin %+.4e at "
              "kz%d/h%d)" % (N, N, float(margins.min()),
                             rows[int(np.argmin(margins))]["kz"],
                             rows[int(np.argmin(margins))]["h"]))
    check("H1 typed: %s" % h1, True)

    # ----------------------------------------------------------- H2
    section("H2 -- HEADFLOOR + NET-TAIL persistence at depth")
    print("    kz   h     n_minA  tailA@cA    n_minB  tailB@cB    "
          "headB@cB")
    kA = kB = nBcov = nAcov = 0
    hBc, nB_min = [], []
    for r in rows:
        nn_at = np.round(np.exp(r["uu"])).astype(np.int64)
        iA, nA = first_cut(nn_at, r["cert_A"])
        iB, nB = first_cut(nn_at, r["cert_B"])
        tAc = float(r["tail_A"][iA]) if iA >= 0 else float("nan")
        tBc = float(r["tail_B"][iB]) if iB >= 0 else float("nan")
        hBv = float(r["head_B"][iB]) if iB >= 0 else float("nan")
        nAcov += iA >= 0
        nBcov += iB >= 0
        kA += (iA >= 0 and tAc <= 0.0)
        kB += (iB >= 0 and tBc <= 0.0)
        nB_min.append(nB)
        hBc.append(hBv)
        print("    %-4d %-5d %-7d %+.3e  %-7d %+.3e  %+.4f"
              % (r["kz"], r["h"], nA, tAc, nB, tBc, hBv),
              flush=True)
    hBc = np.array(hBc)
    okB = np.array([n > 0 for n in nB_min])
    mm = np.array([r["m"] for r in rows])
    print("\n    B-cover exists on %d/%d (n_minB med %s, deployed "
          "med 17); A-cover on %d/%d; head_B(cB) min/med/max "
          "%.4f/%.4f/%.4f (deployed med 0.388)"
          % (nBcov, N,
             int(np.median(np.array(nB_min)[okB])) if okB.any()
             else "-", nAcov, N,
             float(np.nanmin(hBc)) if okB.any() else float("nan"),
             float(np.nanmedian(hBc)), float(np.nanmax(hBc))))
    pos = okB & (hBc > 0)
    if int(np.sum(pos)) >= 3:
        slC, seC, r2C = jack_slope(np.log(mm[pos]),
                                   np.log(hBc[pos]))
    else:
        slC = seC = r2C = float("nan")
    print("    TYPED screen log head_B(cB) vs log m on the new "
          "rungs: slope %+.3f +- 2SE %.3f (R^2 %.2f); deployed "
          "+0.113" % (slC, 2 * seC, r2C))
    if not np.isfinite(slC):
        hd = "HEADFLOOR-VACUOUS(pos=%d)" % int(np.sum(pos))
    elif abs(slC) <= SLOPE_PASS:
        hd = "HEADFLOOR-O1(slope=%+.3f)" % slC
    elif slC >= SLOPE_RELOC:
        hd = "HEADFLOOR-RELOC(slope=%+.3f)" % slC
    else:
        hd = "HEADFLOOR-AMBIG(slope=%+.3f)" % slC
    h2 = ("BCOVER(%d/%d) + NETB(%d/%d@cB) + NETA(%d/%d@cA) + %s"
          % (nBcov, N, kB, N, kA, N, hd))
    check("H2 typed: %s" % h2, True)

    # ----------------------------------------------------------- H3
    section("H3 -- B-floor + (1/2) P_G dominance on the NEW steps "
            "(float level, declared)")
    grams = []
    for r in rows:
        g = ext_gram(r["kz"])
        tag = ("chain-short" if g is None else
               "core-missing" if not g["core_ok"] else
               "negA=%d" % g["negA"] if g["negA"] > 0 else "ok")
        print("    gram kz %3d h %5d: %s%s  [%.1f s]"
              % (r["kz"], r["h"], tag,
                 ("" if g is None or not g.get("core_ok") else
                  "  tau %.3e n %d" % (g["tau"], g["n"])),
                 time.time() - T0), flush=True)
        grams.append(g)
    usable = [g for g in grams if isinstance(g, dict)
              and g.get("core_ok")]
    n_skip = len(grams) - len(usable)
    usable.sort(key=lambda g: (g["h"], g["kz"]))
    steps = []
    for g1, g2 in zip(usable, usable[1:]):
        if g1["negA"] > 0 or g1["negS"] > 0 or g1["lamS"] <= 0.0:
            continue
        steps.append(build_pg_step(g1, g2))
    print("\n    %d/%d rungs usable (%d skipped: honest "
          "reachability limit), %d steps"
          % (len(usable), len(grams), n_skip, len(steps)))
    print("    kz(r2) h     lam_min(B)  c_G        c_dom       "
          "negidx  c_B")
    for s in steps:
        print("    %-6d %-5d %.6f    %.6f   %+.6f   %-6d  %.6f"
              % (s["kz"], s["h"], s["minB"], s["cg"], s["cdom"],
                 s["negD"], s["cb"]), flush=True)
    if steps:
        minB_new = float(np.min([s["minB"] for s in steps]))
        n_dom = sum(1 for s in steps if s["negD"] == 0
                    and s["cb"] > 0)
        cb_min = float(np.min([s["cb"] for s in steps]))
        bar = MINB_REF * (1.0 - MINB_RTOL)
        if minB_new >= bar:
            h3a = ("BFLOOR-PERSISTS(min lam_min(B) = %.4f >= "
                   "%.4f)" % (minB_new, bar))
        else:
            h3a = ("BFLOOR-HOLDOUT-FAIL(min lam_min(B) = %.4f < "
                   "%.4f at kz%d/h%d) -- first-class, reported, "
                   "not repaired"
                   % (minB_new, bar,
                      min(steps, key=lambda s: s["minB"])["kz"],
                      min(steps, key=lambda s: s["minB"])["h"]))
        if n_dom == len(steps):
            h3b = ("DOM-PERSISTS(%d/%d, min c_B = %.4f)"
                   % (n_dom, len(steps), cb_min))
        else:
            h3b = ("DOM-HOLDOUT-FAIL(%d/%d) -- first-class, "
                   "reported, not repaired"
                   % (len(steps) - n_dom, len(steps)))
    else:
        h3a = "BFLOOR-VACUOUS(no steps)"
        h3b = "DOM-VACUOUS(no steps)"
    h3 = "%s + %s + SKIPPED(%d)" % (h3a, h3b, n_skip)
    check("H3 typed: %s (FLOAT LEVEL: no exact-rational LDL, no "
          "interval enclosure at depth)" % h3, True)

    # ----------------------------------------------------------- H4
    section("H4 -- the margin law lam_min ~ h^p across the depth "
            "extension")
    hh_n = np.array([float(r["h"]) for r in rows])
    p_new, se_new, r2_new = jack_slope(np.log(hh_n), np.log(mm))
    h_all = np.concatenate([h_d, hh_n])
    m_all = np.concatenate([m_d, mm])
    p_all, se_all, r2_all = jack_slope(np.log(h_all),
                                       np.log(m_all))
    print("    deployed 67: p = %+.4f +- %.4f (R^2 %.3f)"
          % (p_dep, 2 * se_dep, r2_dep))
    print("    new %d:      p = %+.4f +- %.4f (R^2 %.3f)"
          % (N, p_new, 2 * se_new, r2_new))
    print("    combined %d: p = %+.4f +- %.4f (R^2 %.3f)"
          % (len(h_all), p_all, 2 * se_all, r2_all))
    if EXPO_BAND[0] <= p_all <= EXPO_BAND[1]:
        h4 = "LAW-CONTINUES(p_comb = %+.3f, p_new = %+.3f)" % (
            p_all, p_new)
    else:
        h4 = "LAW-BREAKS(p_comb = %+.3f outside [%.1f, %.1f])" % (
            p_all, EXPO_BAND[0], EXPO_BAND[1])
    check("H4 typed: %s" % h4, True)

    # ------------------------------------------------------------ C
    section("C -- controls on the first new rung (kz %d, h %d)"
            % (rows[0]["kz"], rows[0]["h"]))
    kz0 = rows[0]["kz"]
    alpha0, M0, h0, ka0 = ext_frame(kz0)
    rng = np.random.default_rng(SCRAMBLE_SEED)
    uu_s = np.sort(rng.uniform(0.0, 2.0 * alpha0, size=ka0))
    r_scr = ext_rung(kz0, positions=uu_s,
                     masses=EXT["MU"][:ka0].copy())
    ug0, mg0 = smooth_comb(alpha0)
    r_smo = ext_rung(kz0, positions=ug0, masses=mg0)
    fired = 0
    for name, rc in (("scramble", r_scr), ("smooth", r_smo)):
        ncA = int(np.sum(rc["cert_A"] > 0))
        ncB = int(np.sum(rc["cert_B"] > 0))
        f = rc["m"] < 0 and ncA == 0 and ncB == 0
        fired += f
        print("    %-9s: lam_min %+.3e  shat %+.3e  covering cuts "
              "A/B %d/%d -> %s"
              % (name, rc["m"], rc["m"] / rc["mu1"], ncA, ncB,
                 "FIRES" if f else "SILENT"), flush=True)
    check("C1/C2 WARD scramble + smooth break the wall AND have "
          "zero coverage in both bookkeepings", fired == 2,
          kill="K2")
    c_at_s, D0 = core.atom_lags_at(alpha0, M0, ug0, mg0)
    c_sm_lags = (np.asarray(core.arch_lags(M0, D0), float)
                 + np.asarray(c_at_s, float))
    g_sm = ext_gram(kz0, c_lags=c_sm_lags)
    if g_sm is None:
        c3 = "smooth gram chain dies (chain short) -> fires"
        ok3 = True
    elif not g_sm.get("core_ok"):
        c3 = "smooth gram core missing -> fires"
        ok3 = True
    else:
        ok3 = g_sm["negA"] > 0
        c3 = ("smooth gram neg(A) = %d -> %s"
              % (g_sm["negA"], "FIRES" if ok3 else "SILENT"))
    check("C3 WARD the prime-free comb cannot fake the P_G-chain "
          "surface: %s" % c3, ok3, kill="K2")
    print("    DECLARED SKIP: Epstein control not run at depth "
          "(O(X^2) divisor recursion infeasible at X ~ 8e5); it "
          "lives at kz 9 in the frozen upstream probes.")

    return finish(dict(h1=h1, h2=h2, h3=h3, h4=h4,
                       fid="FIDELITY(overlap 0.0, regression "
                           "%.1e, registry %s)"
                           % (dev_reg, reg_sha[:8]),
                       surf="NEW-SURFACE(%d, h %d..%d)"
                            % (N, rows[0]["h"], rows[-1]["h"])))


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("DEEPHOLDOUT-SCORED / %(fid)s / %(surf)s / "
                   "%(h1)s / %(h2)s / %(h3)s / %(h4)s" % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): this is the first genuine OUT-OF-SAMPLE
  test of the round-63 registered objects -- the constant 1/2, the
  HEADFLOOR bands, the 0.679 class and s = 1/2 were all frozen
  before any rung beyond X = 4e5 existed.  All deep objects are
  FLOAT-LEVEL (no interval rollout, no exact-rational certificates
  at depth); the h band beyond HCAP and the Epstein skip are
  declared amendments of REACHABILITY, not of any scoring rule.  A
  PASS census on 28 rungs proves nothing about deeper h, the ideal
  objects, or any tail statement; a FAIL is a first-class result
  and is never repaired.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
