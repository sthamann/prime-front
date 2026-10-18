#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wall_edge_completion_probe -- PRIME.PORT.EDGE.COMPLETION.01
(EXPLORATION ONLY, experiments/; round 60, theorem-engineering on the
RH-side wall: the Gram completion of the signed comb measure fails
EXACTLY at the x = +1 edge (round 59, wall_gram_radau_probe:
lam_min(M1x2) < 0 and lam_min(Mm) < 0 on 42/42 while Mp passes) --
the SAME disease shape the pair kernel had (ONE boundary mode from
an edge convention), which v899 cured by the PERIODIC FULL-WEIGHT
completion.  Does an analogous boundary/edge completion of the
wall's signed moment problem remove the negative Lukacs floors
while preserving the wall identity?  2026-08-10.)

THE OBJECT (round-59 verbatim).  The wall Gram is G_ij =
sqrt(v_i v_j) K_h(y_i, y_j) on the folded NEG family (ys, vs); A =
I - G, tau = 1 - lam_max(G); M0 := I_h - H (H = sum_i v_i p(y_i)
p(y_i)^T) is EXACTLY the moment matrix of the signed comb measure
nu = mu_+ - mu_- in the mu_+-orthonormal chain basis, and
lam_min(M0) = tau.  The Lukacs floors at matched degree are
lam_min(M1x2), lam_min(Mm) ((1-x) localization), lam_min(Mp)
((1+x)); round 59 measured x2:42/42 fail, m:42/42 fail, p:0/42.

THE THREE COMPLETIONS (frozen a priori, increasing ambition; every
one SOURCE-ONLY -- constructed from the comb assembly (c_ar, c_at)
/ the atom table / the positive family; NO tau, NO defect
eigenvector, NO spectral data of A enters any construction):

 (a) EDGE CONVENTION (the literal v899 mirror on the lag assembly).
   The deployed density is the FFT of the whole-sample symmetric
   (DCT-I) extension a = [c_0..c_{M-1}, c_{M-2}..c_1] -- the two
   edge lags c_0, c_{M-1} carry HALF the weight of interior lags,
   exactly the halving that created the pair kernel's one boundary
   tent (v899).  The periodic full-weight completion is closed
   form:
     A1 (deep edge):  dtil_j = d_j + (-1)^j c_{M-1}
     A2 (both edges): dtil_j = d_j + (-1)^j c_{M-1} + c_0
   (e^{-2 pi i j (M-1)/L} = (-1)^j at L = 2M - 2).  WARD two-route:
   closed form == FFT of the doubled-edge lag vector.

 (b) COMB TENT COMPLETION (periodic/reflect completion of the comb
   measure at the deep window edge).  The atom assembly
   atom_lags_at truncates the tent of every atom with u_j >
   (M-1) D at the deep edge (the overhang lag i = M falls off the
   grid) while the u = 0 edge has an explicit mirror.  The
   completion reflects the overhang whole-sample at the deep edge
   (i = M -> M - 2), the SAME reflection rule the extension a
   already encodes.  WARD two-route: modified assembly == deployed
   assembly + closed-form overhang correction on lag M - 2; mass
   ledger exact.

 (c) BOUNDARY ATOM (one-parameter completion).  mu_+' = mu_+ +
   m* delta_{x = +1} with m* >= 0 (source-only positive mass; the
   measure factor (1 - x) kills any such atom inside nu's density
   route, so the atom must be carried by the positive family -- it
   changes the CHAIN BASIS, hence all floors, nontrivially).  Per
   rung: scan the frozen ratio grid m*/m0 in 10^{-12}..10^{-1},
   count sign changes of lam_min(Mm)(m*), bisect the first
   bracket; at the solved m*: ALL three floors, tau', neg(A').
   UNIQUENESS is grid-level (crossing count on the frozen grid,
   said plainly).

WHAT "PRESERVED" MEANS (frozen): each completion changes the
measure, so the wall identity is preserved IN FORM (M0til = I - Htil
= moment matrix of nutil, two-route warded) and the SHIFT is
measured exactly: tau-til ladder, neg(Atil) counts, med/range of
tau-til/tau.  WALL-PRESERVED iff neg(Atil) = 0 on all rungs and
med |tau-til/tau - 1| <= WALL_SHIFT_TOL; WALL-SHIFTED(med) iff
neg(Atil) = 0 everywhere; WALL-BROKEN(count) else.

SUCCESS / FAILURE (frozen): COMPLETION-ACHIEVED(variant) iff some
variant has ALL THREE floors >= -LOC_TOL on ALL truth rungs AND
wall not broken AND the achieved floor's tau-screen is not RELOC
(non-relocating margin: |slope| <= SLOPE_PASS on log|floor| vs log
tau-til, positive-floor subset).  Honest failure = the edge
obstruction is intrinsic; then E4 measures WHERE the needed
negative mass sits: from the minimizing eigenvector e of the base
Mm, q = sum e_k p_k, the negative-side contributions c^-_i =
v_i (1 - y_i) q(y_i)^2 and their cumulative share within x > 1 -
delta for delta in EDGE_DELTAS; typed NEGMASS-EDGE(share at 1e-2)
iff med share >= NEGLOC_BAR, else NEGMASS-BULK.

FROZEN PROTOCOL (pipeline verbatim from wall_gram_radau_probe =
v900 chain; ONE Gram per rung; window memoization; big arrays kept
per rung for the variant rebuilds, dropped at the end):

 W   PIPELINE + REPRODUCTION (kill -> PIPELINE-BROKEN /
     WARD-BROKEN): W1 42 rungs, chains complete, tau finite; W2
     WARD truth wall holds (neg(A) = 0 via the factor-Gram tie,
     dense-warded on the N_SPOT = 2 shallowest rungs at
     SPOT_WARD); W3 WARD two-route M0 (pipeline I - H vs direct
     signed quadrature) rel <= M0_WARD on every rung; W4
     REPRODUCTION of the round-59 floor ledger: fail counts
     (x2, m, p) == (42, 42, 0) at LOC_TOL (kill -> WARD-BROKEN).

 E1  VARIANT (a): wards A1/A2 two-route <= EDGE_WARD; full floor +
     tau-til ladder per sub-variant; typed A1-/A2-<FIXES |
     FAILS(x2,m,p)>-WALL<PRESERVED | SHIFTED(med) | BROKEN(n)>.

 E2  VARIANT (b): ward support of the correction (last SUPP_LAGS
     lags) + exact mass ledger <= REFL_WARD; overhang census (how
     many atoms, what mass); same floor + wall ladder and typing.

 E3  VARIANT (c): grid scan + bisection (BISECT_IT) on lam_min(Mm)
     per rung; light-route spot ward vs the full pack on the
     shallowest rung <= LIGHT_WARD; typed ATOM-<ZEROES(n,
     crossings) | NONE>: n = rungs with a grid bracket, med
     m*/m0, med tau'/tau, the OTHER floors at m* (counts), and
     the m*-vs-tau screen slope (is the needed mass tau-coupled?).

 E4  THE NEGATIVE-MASS SEAT (always measured, base family):
     share(delta) ladder med over rungs, peak fold position; typed
     NEGMASS-EDGE(share)/NEGMASS-BULK at NEGLOC_BAR.

 C   CONTROLS (kill -> WARD-BROKEN if silent): C1 smooth world:
     neg(A) > 0 on >= 1 rung AND the x2 floor < 0 on all smooth
     rungs (round-59 LOCWALL-SEEN reproduced); C2 Epstein x^2+5y^2
     comb + scramble (seed 1) at kz 9 fire (neg(A) > 0 or chain
     death); C3 COMPLETION MUST NOT CERTIFY THE SCRAMBLE: every
     variant (a1, a2, b, c at the median solved ratio) applied to
     the scramble comb leaves neg(Atil) > 0 or a floor < -LOC_TOL;
     C4 v899 MECHANISM REGRESSION under this implementation: on
     the deployed kz-9 density, the half-weight edge reading leaks
     EXACTLY chat_j = Wc_j - (T0 + (-1)^j T1)/(2L) (rel <=
     V899_WARD) with a POSITIVE negative index, and the periodic
     full-weight reading returns Wc >= 0 exactly (negative index
     0, dev <= V899_WARD) -- the v899 kill reproduced
     mechanism-level (disclosed: not the round-50 kernel census).

KILLS: K1 pipeline (W1) -> PIPELINE-BROKEN; K2 identity /
reproduction / control wards (W2-W4, E-wards, C1-C4) ->
WARD-BROKEN.  All E-typed outcomes are measurements, never kills.

VERDICT (frozen enum): EDGECOMPL-MEASURED with typed sublabels
BASE-REPRO(x2,m,p), A1-.../A2-.../B-... (as above),
ATOM-ZEROES(n)/ATOM-NONE, COMPLETION-ACHIEVED(variant)/
EDGE-OBSTRUCTION-INTRINSIC, NEGMASS-EDGE(share)/NEGMASS-BULK,
V899REG-OK; else PIPELINE-BROKEN / WARD-BROKEN.

FROZEN BARS: H_LADDER_MAX = 900; N_RUNGS_EXP = 42; LOC_TOL =
1e-10; M0_WARD = 1e-8; SPOT_WARD = 1e-10; N_SPOT = 2; EDGE_WARD =
1e-10; REFL_WARD = 1e-10; SUPP_LAGS = 4; LIGHT_WARD = 1e-8;
MSTAR_LOG_GRID = (-12, -10, -8, -7, -6, -5, -4, -3, -2, -1) on
m*/m0; BISECT_IT = 12; WALL_SHIFT_TOL = 0.05; SLOPE_PASS = 0.30;
SLOPE_RELOC = 0.70; EDGE_DELTAS = (1e-4, 1e-3, 1e-2, 1e-1);
NEGLOC_BAR = 0.90 (at delta = 1e-2); V899_WARD = 1e-10; V899_DUST
= 1e-12 (x max|Wc|); CTRL_KZ = 9; scramble seed 1.

SMOKE-RUN DISCLOSURE (2026-08-10, before freezing): TWO smoke
runs.  Smoke 1 (19 checks passed, then a MECHANICAL crash in the
C4 call -- a stray broadcast expression, no content; fixed) and
one spec defect exposed: the original (c)-grid m*/m0 in
1e-12..1e-1 measured ALL-NEGATIVE signs of lam_min(Mm)(m*) on
42/42 rungs (no bracket anywhere).  AMENDMENT 1 (disclosed): the
C4 argument bug was fixed (pure mechanics).  AMENDMENT 2
(disclosed): the grid was EXTENDED UPWARD to 1e-12..1e+2 x m0 and
a no-bracket diagnostic print was added (top-grid floor ratio) --
this only STRENGTHENS a NONE claim; no bar, band, count, enum or
typed rule was moved; fail-first preserved.  Smoke 2 (20/20, 39.8
s) MEASURED, recorded as the honest context the frozen run must
confirm: (a) the lag-edge convention completions FAIL: A1 (deep
edge full weight) leaves the fail counts EXACTLY at base (x2:42,
m:42, p:0) with the min floor WORSENED to -1.63e-01 and the wall
preserved (med shift 8.2e-03, neg = 0 everywhere) -- the DCT-I
lag halving is NOT the seat of the wall's edge disease (unlike
the pair kernel's); A2 (both edges) inflates the wall scale by
med tau'/tau = 3.9e+04 (the c_0 halving is a HUGE convention
choice) and STILL fails the floors on 40/42 -- the obstruction
survives even a 4-orders-of-magnitude slack wall; (b) the comb
tent completion is REAL (796 overhang atoms, med mass share
1.5e-03 of the comb) and BREAKS the wall on 9/42 rungs
(neg(Atil) > 0, tau' down to -1.3e+06 x tau) while fixing NO
floor (42, 42, 0): the deployed deep-edge tent truncation is
LOAD-BEARING for wall positivity, not an innocent convention;
(c) the boundary atom at x = +1 NEVER zeroes the (1-x) floor:
no sign change on any rung over 14 decades m*/m0 in
1e-12..1e+2; the floor improves monotonically toward zero but
saturates at med 9.4% of its base value at the top mass (range
[0.2%, 19%]) -- the atom-at-the-point completion asymptotes
strictly below zero; (d) THE SEAT (E4): the needed negative mass
IS edge-localized but as a BAND, not a point: cumulative
negative-side share within x > 1 - delta med 0.006 / 0.249 /
0.942 / 0.996 at delta = 1e-4/1e-3/1e-2/1e-1 (NEGMASS-EDGE(0.94)
at the 0.90 bar), peak contribution at x med 0.99811 (fold index
med 16 of the circle) -- an O(1e-2)-wide x-band near +1, which is
exactly why one boundary atom at the point x = +1 cannot complete
the cone; (e) v899 mechanism regression OK (leak dev 2.3e-16,
negative index 349 > 0; periodic kill dev 2.3e-16, negative index
0; T1 = +14.3); controls all fire (smooth neg(A) > 0 with x2 < 0
on 42/42; Epstein neg(A) = 55, scramble neg(A) = 37; no
completion certifies the scramble -- worst variant leaves neg =
7..37 and floors down to -1.8e+07).  Headline at smoke:
EDGE-OBSTRUCTION-INTRINSIC.  Fail-first preserved: nothing was
weakened; all typed outcomes are measurements over exact-warded
rebuilds.

SPEC v2 (2026-08-10, frozen + SHA-hashed before the frozen run):
everything above.  Mechanical concretizations frozen with v2: (i)
window memoization per (kz, seed); (ii) floors at size h - 1
(degree budget 2h - 2), verbatim wall_gram_radau_probe; (iii) the
light scan route builds the chain at length h - 1 (nested Lanczos;
spot-warded); (iv) OLS population statistics as v900; screens read
the positive subset with excluded counts printed; (v) neg(A) and
tau via the factor-Gram tie eig(A) = {1 - eig(H)} u {1}^(n-h)
(dense-warded, N_SPOT); (vi) the (c)-scan bisects on log10(m*/m0).

NO-GO COMPLIANCE (frozen): no certified-bound retry on raw B (not
touched here), no rank-1 approximation of the core update, no
plain Herglotz certificate; no fit where an identity is claimed
(all identities are exact wards; trends are typed measurements).

NO RH claim: a successful completion would say the deployed signed
comb measure is, at matched finite degree per rung, the shadow of
a nonnegative measure after an explicit source-only boundary
completion -- a reformulation surface, not a bound and not a tail
theorem; failure localizes the obstruction.  Nothing here proves
tau_h > 0 beyond the deployed census.  No marker moves.

FIREWALL: no zeros, no prime oracles (AST scan; banned ids
zetazero / nzeros / primerange / isprime / primepi / nextprime /
prevprime); v563 READ-ONLY; RNG only inside the declared scramble
control; stdout only.

Sources (read-only): v563_paper2_readouts; wall machinery verbatim
from wall_gram_radau_probe.py (round 59) = v900 chain; the v899
periodic full-weight mechanism (verification/v899, READ-ONLY
reference for the closed form); Lukacs representation (classical).

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wall_edge_completion_probe.py
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

H_LADDER_MAX = 900
N_RUNGS_EXP = 42
LOC_TOL = 1e-10
M0_WARD = 1e-8
SPOT_WARD = 1e-10
N_SPOT = 2
EDGE_WARD = 1e-10
REFL_WARD = 1e-10
SUPP_LAGS = 4
LIGHT_WARD = 1e-8
MSTAR_LOG_GRID = (-12.0, -10.0, -8.0, -7.0, -6.0, -5.0, -4.0,
                  -3.0, -2.0, -1.0, 0.0, 1.0, 2.0)
BISECT_IT = 12
WALL_SHIFT_TOL = 0.05
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
EDGE_DELTAS = (1e-4, 1e-3, 1e-2, 1e-1)
NEGLOC_BAR = 0.90
V899_WARD = 1e-10
V899_DUST = 1e-12
CTRL_KZ = 9
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


# --------------- pipeline, verbatim (wall_gram_radau_probe chain)
def grid_density(c):
    c = np.asarray(c, float)
    a = np.concatenate([c, c[-2:0:-1]])
    d = np.fft.fft(a)
    assert float(np.max(np.abs(d.imag))) <= 1e-9 * max(
        1.0, float(np.max(np.abs(d.real))))
    return d.real


def cell_widths(uu):
    du = np.zeros(len(uu))
    du[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    du[0] = uu[1] - uu[0]
    du[-1] = uu[-1] - uu[-2]
    return du


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


def lambda_eps(N):
    """Epstein x^2+5y^2 comb (port_schur_reduction verbatim)."""
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


_WIN_CACHE = {}


def window_of(kz, scramble_seed=None):
    key = (kz, scramble_seed)
    if key not in _WIN_CACHE:
        rr = core.build_window(kz, scramble_seed=scramble_seed)
        _WIN_CACHE[key] = dict(
            h=rr["h"], M=rr["M"], D=rr["D"], alpha=rr["alpha"],
            n_atom=rr["n_atom"],
            uu=np.asarray(rr["uu"], float).copy(),
            lam=np.asarray(rr["lam"], float).copy(),
            c_ar=np.asarray(core.arch_lags(rr["M"], rr["D"]),
                            float))
    return _WIN_CACHE[key]


def ladder_zones():
    out = []
    for kz in core.frame_a_zones():
        D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
        M_k = int(math.ceil(float(core.U_ALL[kz]) / D_k - 1.0e-9)) + 1
        if M_k % 2:
            M_k += 1
        if M_k // 2 <= H_LADDER_MAX:
            out.append(kz)
    return out


def smooth_masses(uu):
    return 2.0 * np.exp(uu / 2.0) * cell_widths(uu)


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


# ------------------------------ the assemblies (base + variants)
def base_assembly(kz, world_fn=None, scramble_seed=None, comb=None):
    """Deployed lag assembly c = c_ar + c_at and its density d."""
    rr = window_of(kz, scramble_seed=scramble_seed)
    M, D, alpha, h = rr["M"], rr["D"], rr["alpha"], rr["h"]
    uu = rr["uu"]
    mm = 2.0 * rr["lam"]
    if world_fn is not None:
        uu, mm = world_fn(uu, mm)
    if comb is not None:
        uu, mm = comb
    c_at, _ = core.atom_lags_at(alpha, M, uu, mm)
    c = rr["c_ar"] + np.asarray(c_at, float)
    d = grid_density(c)
    return dict(kz=kz, h=h, M=M, D=D, alpha=float(alpha),
                L=2 * M - 2, uu=np.asarray(uu, float),
                mm=np.asarray(mm, float), c=c, d=d)


def atom_lags_reflected(alpha, M, positions, masses):
    """Variant (b): atom_lags_at with the deep-edge overhang
    REFLECTED whole-sample (i = M -> M - 2) instead of truncated.
    Returns (c, overhang_mass, n_overhang)."""
    D = 2.0 * alpha / M
    c = np.zeros(M)
    over = 0.0
    nov = 0
    for u_j, mu_j in zip(positions, masses):
        i0 = int(math.floor(u_j / D))
        hit = False
        for i in range(max(0, i0 - 2), i0 + 3):
            v = 1.0 - abs(i * D - u_j) / D
            if v > 0.0:
                if i < M:
                    c[i] -= mu_j * 0.5 * v
                else:
                    ir = 2 * (M - 1) - i
                    if 0 <= ir < M:
                        c[ir] -= mu_j * 0.5 * v
                    over += mu_j * 0.5 * v
                    hit = True
        if hit:
            nov += 1
        if u_j < D:
            for i in range(0, min(M, int(math.floor(
                    (D - u_j) / D)) + 2)):
                v = 1.0 - (i * D + u_j) / D
                if v > 0.0:
                    c[i] -= mu_j * 0.5 * v
    return c, over, nov


def floors_pack(xs, ws, ys, vs, h, want_evec=False):
    """Chain + M0 two-route + the three Lukacs floors + tau/neg
    via the factor-Gram tie.  None if the chain dies."""
    al, be, m0, steps = lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or (len(be) and np.any(be <= 0)):
        return None
    Px = eval_chain(al, be, m0, xs, h)
    Pn = eval_chain(al, be, m0, ys, h)
    H = (Pn * vs[:, None]).T @ Pn
    H = 0.5 * (H + H.T)
    M0a = np.eye(h) - H
    Gp = (Px * ws[:, None]).T @ Px
    M0b = 0.5 * (Gp + Gp.T) - H
    dev = (float(np.linalg.norm(M0a - M0b))
           / max(float(np.linalg.norm(M0a)), 1e-300))
    evH = np.linalg.eigvalsh(H)
    out = dict(dev=dev, tau=float(1.0 - evH[-1]),
               negA=int(np.sum(evH > 1.0)), m0=m0)
    hm = h - 1
    Pxm, Pnm = Px[:, :hm], Pn[:, :hm]
    for tag, gx, gy in (("x2", 1.0 - xs ** 2, 1.0 - ys ** 2),
                        ("m", 1.0 - xs, 1.0 - ys),
                        ("p", 1.0 + xs, 1.0 + ys)):
        Mloc = ((Pxm * (ws * gx)[:, None]).T @ Pxm
                - (Pnm * (vs * gy)[:, None]).T @ Pnm)
        Mloc = 0.5 * (Mloc + Mloc.T)
        if tag == "m" and want_evec:
            w_, V_ = np.linalg.eigh(Mloc)
            out["lam_m"] = float(w_[0])
            out["evec_m"] = V_[:, 0]
            out["Pxm"], out["Pnm"] = Pxm, Pnm
        else:
            out["lam_" + tag] = float(np.linalg.eigvalsh(Mloc)[0])
    return out


def floor_m_light(xs, ws, ys, vs, h):
    """The (1-x) floor via the nested chain at length h - 1
    (the scan route; spot-warded against floors_pack)."""
    hm = h - 1
    al, be, m0, steps = lanczos_chain(xs, ws, hm)
    if steps < hm or (len(be) and np.any(be <= 0)):
        return None
    Pxm = eval_chain(al, be, m0, xs, hm)
    Pnm = eval_chain(al, be, m0, ys, hm)
    Mloc = ((Pxm * (ws * (1.0 - xs))[:, None]).T @ Pxm
            - (Pnm * (vs * (1.0 - ys))[:, None]).T @ Pnm)
    Mloc = 0.5 * (Mloc + Mloc.T)
    return float(np.linalg.eigvalsh(Mloc)[0])


def measure_of(d, L):
    xs, ws, _ = folded_measure(d, L, +1.0)
    ys, vs, ufn = folded_measure(d, L, -1.0)
    return xs, ws, ys, vs, ufn


def variant_ladder(name, packs):
    """Summarize a variant's floor + wall ladder; returns the typed
    label pieces.  packs: list of (rung, pack-or-None)."""
    ok = [(r, p) for r, p in packs if p is not None]
    dead = len(packs) - len(ok)
    n_x2 = sum(1 for _r, p in ok if p["lam_x2"] < -LOC_TOL)
    n_m = sum(1 for _r, p in ok if p["lam_m"] < -LOC_TOL)
    n_p = sum(1 for _r, p in ok if p["lam_p"] < -LOC_TOL)
    negs = sum(1 for _r, p in ok if p["negA"] > 0)
    rat = np.array([p["tau"] / r["tau"] for r, p in ok])
    minfl = min(min(p["lam_x2"], p["lam_m"], p["lam_p"])
                for _r, p in ok) if ok else float("nan")
    if negs == 0 and float(np.median(np.abs(rat - 1.0))) \
            <= WALL_SHIFT_TOL:
        wall = "WALL-PRESERVED(med-shift=%.1e)" % float(
            np.median(np.abs(rat - 1.0)))
    elif negs == 0:
        wall = "WALL-SHIFTED(med tau'/tau=%.3f)" % float(
            np.median(rat))
    else:
        wall = "WALL-BROKEN(%d)" % negs
    if n_x2 == 0 and n_m == 0 and n_p == 0 and dead == 0:
        lab = "%s-FIXES" % name
    else:
        lab = "%s-FAILS(x2:%d, m:%d, p:%d%s)" % (
            name, n_x2, n_m, n_p,
            ", dead:%d" % dead if dead else "")
    print("    %s: fail counts x2:%d m:%d p:%d (dead %d); min "
          "floor %.3e; tau'/tau med %.5f range [%.4f, %.4f]; "
          "neg(Atil)>0 on %d -> %s / %s"
          % (name, n_x2, n_m, n_p, dead, minfl,
             float(np.median(rat)), float(np.min(rat)),
             float(np.max(rat)), negs, lab, wall), flush=True)
    return lab, wall, (n_x2 == 0 and n_m == 0 and n_p == 0
                       and dead == 0 and negs == 0), ok


def v899_mechanism(d):
    """C4: the closed-form half-weight leak + the periodic
    full-weight kill, on the deployed density magnitudes."""
    L = len(d)
    M = L // 2 + 1
    Wc = np.abs(np.asarray(d, float))
    sgn = (-1.0) ** np.arange(L)
    T0m = float(np.sum(Wc))
    T1m = float(sgn @ Wc)
    P = np.fft.ifft(Wc).real
    v = P[:M].copy()
    v[0] *= 0.5
    v[M - 1] *= 0.5
    bv = np.concatenate([v, v[M - 2:0:-1]])
    chat = np.fft.fft(bv).real
    closed = Wc - (T0m + sgn * T1m) / (2.0 * L)
    scale = float(np.max(Wc))
    dev_leak = float(np.max(np.abs(chat - closed))) / scale
    dust = V899_DUST * scale
    n_leak = int(np.sum(chat < -dust))
    cfix = np.fft.fft(np.concatenate([P[:M], P[M - 2:0:-1]])).real
    dev_fix = float(np.max(np.abs(cfix - Wc))) / scale
    n_fix = int(np.sum(cfix < -dust))
    return dict(T0=T0m, T1=T1m, dev_leak=dev_leak, n_leak=n_leak,
                dev_fix=dev_fix, n_fix=n_fix)


def main():
    section("PRIME.PORT.EDGE.COMPLETION.01 -- boundary/edge "
            "completion of the wall's signed moment problem "
            "(EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s"
          % hashlib.sha256(__doc__.encode("utf-8")).hexdigest())
    print("    NO RH claim; no marker moves.")
    print("\nS0 -- firewall")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))

    # ------------------------------------------------------------ W
    section("W -- the truth ladder: base assembly, floors, "
            "reproduction")
    zones = ladder_zones()
    check("W1 frozen rung count %d" % N_RUNGS_EXP,
          len(zones) == N_RUNGS_EXP, "found %d" % len(zones),
          kill="K1")
    truth = []
    for kz in zones:
        r = base_assembly(kz)
        xs, ws, ys, vs, _uf = measure_of(r["d"], r["L"])
        p = floors_pack(xs, ws, ys, vs, r["h"], want_evec=True)
        if p is None:
            print("    kz %-3d: CHAIN SHORT" % kz, flush=True)
            truth.append(None)
            continue
        r["fam"] = (xs, ws, ys, vs)
        r.update(tau=p["tau"], negA=p["negA"], pack=p)
        truth.append(r)
    ok_chain = all(r is not None for r in truth)
    check("W1b all chains complete", ok_chain, kill="K1")
    if not ok_chain:
        return finish({})
    truth.sort(key=lambda r: (r["h"], r["kz"]))
    check("W1c all tau finite",
          all(np.isfinite(r["tau"]) for r in truth), kill="K1")
    check("W2a WARD truth wall holds (neg(A) = 0 via factor-Gram "
          "tie on all rungs)",
          all(r["negA"] == 0 for r in truth), kill="K2")
    dev_sp = 0.0
    for r in truth[:N_SPOT]:
        xs, ws, ys, vs = r["fam"]
        al, be, m0, _ = lanczos_chain(xs, ws, r["h"] + 1)
        Pn = eval_chain(al, be, m0, ys, r["h"])
        G = np.sqrt(vs)[:, None] * (Pn @ Pn.T) * np.sqrt(vs)[None, :]
        lamA = float(np.linalg.eigvalsh(
            np.eye(G.shape[0]) - 0.5 * (G + G.T))[0])
        dev_sp = max(dev_sp, abs(lamA - r["tau"]))
    check("W2b SPOT WARD dense lam_min(A) == 1 - lam_max(H) on %d "
          "shallowest rungs: max dev %.2e <= %.0e"
          % (N_SPOT, dev_sp, SPOT_WARD), dev_sp <= SPOT_WARD,
          kill="K2")
    dev0 = max(r["pack"]["dev"] for r in truth)
    check("W3 WARD two-route M0 (I - H vs direct signed "
          "quadrature): max rel dev %.2e <= %.0e" % (dev0, M0_WARD),
          dev0 <= M0_WARD, kill="K2")
    b_x2 = sum(1 for r in truth if r["pack"]["lam_x2"] < -LOC_TOL)
    b_m = sum(1 for r in truth if r["pack"]["lam_m"] < -LOC_TOL)
    b_p = sum(1 for r in truth if r["pack"]["lam_p"] < -LOC_TOL)
    med_ratio = float(np.median(
        [r["pack"]["lam_m"] / r["tau"] for r in truth]))
    check("W4 REPRODUCTION round-59 floor ledger: fail counts "
          "(x2, m, p) = (%d, %d, %d) == (42, 42, 0); med "
          "lam_m/tau %.1f" % (b_x2, b_m, b_p, med_ratio),
          (b_x2, b_m, b_p) == (42, 42, 0), kill="K2")
    print("    h range %d..%d  [%.1f s]"
          % (truth[0]["h"], truth[-1]["h"], time.time() - T0))
    if KILLS:
        return finish({})

    # ------------------------------------------------------------ E1
    section("E1 -- variant (a): full-weight lag-edge convention "
            "(the v899 mirror on the DCT-I lag assembly)")
    dev_a = 0.0
    packs_a1, packs_a2 = [], []
    for r in truth:
        M, L = r["M"], r["L"]
        sgn = (-1.0) ** np.arange(L)
        d_a1 = r["d"] + sgn * r["c"][M - 1]
        d_a2 = d_a1 + r["c"][0]
        c2 = r["c"].copy()
        c2[M - 1] *= 2.0
        dev_a = max(dev_a, float(np.max(np.abs(
            grid_density(c2) - d_a1))) / max(
            float(np.max(np.abs(r["d"]))), 1e-300))
        c3 = c2.copy()
        c3[0] *= 2.0
        dev_a = max(dev_a, float(np.max(np.abs(
            grid_density(c3) - d_a2))) / max(
            float(np.max(np.abs(r["d"]))), 1e-300))
        for dd, store in ((d_a1, packs_a1), (d_a2, packs_a2)):
            xs, ws, ys, vs, _ = measure_of(dd, L)
            store.append((r, floors_pack(xs, ws, ys, vs, r["h"])))
    check("E1.a WARD two-route (closed form == FFT of doubled-edge "
          "lags): max rel dev %.2e <= %.0e" % (dev_a, EDGE_WARD),
          dev_a <= EDGE_WARD, kill="K2")
    print("    kz   h    tau        lam_m(A1)  lam_x2(A1) "
          "tau'/tau   lam_m(A2)")
    for (r, p1), (_r2, p2) in zip(packs_a1, packs_a2):
        print("    %-4d %-4d %.3e  %s  %s"
              % (r["kz"], r["h"], r["tau"],
                 ("%+.3e %+.3e %8.5f " % (p1["lam_m"], p1["lam_x2"],
                  p1["tau"] / r["tau"])) if p1 else "CHAIN-DEAD",
                 ("%+.3e" % p2["lam_m"]) if p2 else "CHAIN-DEAD"),
              flush=True)
    lab_a1, wall_a1, ok_a1, _ = variant_ladder("A1", packs_a1)
    lab_a2, wall_a2, ok_a2, _ = variant_ladder("A2", packs_a2)
    check("E1.b typed: %s / %s ; %s / %s"
          % (lab_a1, wall_a1, lab_a2, wall_a2), True)

    # ------------------------------------------------------------ E2
    section("E2 -- variant (b): comb tent completion at the deep "
            "window edge (reflect the truncated overhang)")
    dev_b = 0.0
    packs_b = []
    n_over_tot = 0
    shares = []
    for r in truth:
        cb, over, nov = atom_lags_reflected(
            r["alpha"], r["M"], r["uu"], r["mm"])
        cav, _ = core.atom_lags_at(r["alpha"], r["M"], r["uu"],
                                   r["mm"])
        dc = cb - np.asarray(cav, float)
        supp_bad = int(np.sum(np.abs(dc[:r["M"] - SUPP_LAGS])
                              > 1e-300))
        mass_dev = abs(float(np.sum(dc)) + over) / max(over, 1e-300)
        dev_b = max(dev_b, float(supp_bad), mass_dev
                    if over > 0 else 0.0)
        n_over_tot += nov
        shares.append(over / max(float(np.sum(np.abs(r["mm"]))),
                                 1e-300))
        rr = window_of(r["kz"])
        d_b = grid_density(rr["c_ar"] + cb)
        xs, ws, ys, vs, _ = measure_of(d_b, r["L"])
        packs_b.append((r, floors_pack(xs, ws, ys, vs, r["h"])))
    check("E2.a WARD correction support (last %d lags) + exact "
          "mass ledger: max dev %.2e <= %.0e; overhang atoms "
          "total %d, mass share med %.1e"
          % (SUPP_LAGS, dev_b, REFL_WARD, n_over_tot,
             float(np.median(shares))), dev_b <= REFL_WARD,
          kill="K2")
    lab_b, wall_b, ok_b, _ = variant_ladder("B", packs_b)
    check("E2.b typed: %s / %s" % (lab_b, wall_b), True)

    # ------------------------------------------------------------ E3
    section("E3 -- variant (c): the boundary atom at x = +1 "
            "(one-parameter completion, solved on the (1-x) floor)")
    r0 = truth[0]
    xs, ws, ys, vs = r0["fam"]
    fl_l = floor_m_light(xs, ws, ys, vs, r0["h"])
    dev_l = abs(fl_l - r0["pack"]["lam_m"]) / max(
        abs(r0["pack"]["lam_m"]), 1e-300)
    check("E3.a SPOT WARD light (h-1 chain) vs pack route on the "
          "shallowest rung: rel dev %.2e <= %.0e"
          % (dev_l, LIGHT_WARD), dev_l <= LIGHT_WARD, kill="K2")
    print("    kz   h    tau        m*/m0      cross  lam_m(m*)   "
          "lam_x2(m*)  lam_p(m*)   tau'/tau")
    sol = []
    for r in truth:
        xs, ws, ys, vs = r["fam"]
        h = r["h"]
        m0 = r["pack"]["m0"]

        def f(lr):
            xs2 = np.append(xs, 1.0)
            ws2 = np.append(ws, (10.0 ** lr) * m0)
            v = floor_m_light(xs2, ws2, ys, vs, h)
            return v if v is not None else float("nan")

        vals = [f(lr) for lr in MSTAR_LOG_GRID]
        sgns = [np.sign(v) if np.isfinite(v) else 0.0 for v in vals]
        r["scan_top"] = (vals[-1] / r["pack"]["lam_m"]
                         if np.isfinite(vals[-1]) else float("nan"))
        r["scan_best"] = (float(np.nanmax(vals))
                          / abs(r["pack"]["lam_m"]))
        crossings = []
        for i in range(1, len(vals)):
            if sgns[i - 1] < 0.0 <= sgns[i]:
                crossings.append(i)
        entry = dict(r=r, ncross=len(crossings))
        if crossings:
            i = crossings[0]
            lo, hi = MSTAR_LOG_GRID[i - 1], MSTAR_LOG_GRID[i]
            for _ in range(BISECT_IT):
                mid = 0.5 * (lo + hi)
                if f(mid) < 0.0:
                    lo = mid
                else:
                    hi = mid
            lr_star = 0.5 * (lo + hi)
            xs2 = np.append(xs, 1.0)
            ws2 = np.append(ws, (10.0 ** lr_star) * m0)
            pk = floors_pack(xs2, ws2, ys, vs, h)
            entry.update(lr=lr_star, ratio=10.0 ** lr_star, pack=pk)
            print("    %-4d %-4d %.3e  %.3e  %d      %s"
                  % (r["kz"], r["h"], r["tau"], 10.0 ** lr_star,
                     len(crossings),
                     ("%+.3e  %+.3e  %+.3e  %8.5f"
                      % (pk["lam_m"], pk["lam_x2"], pk["lam_p"],
                         pk["tau"] / r["tau"])) if pk else
                     "CHAIN-DEAD"), flush=True)
        else:
            print("    %-4d %-4d %.3e  NO GRID BRACKET (signs %s)"
                  % (r["kz"], r["h"], r["tau"],
                     "".join("+" if s > 0 else "-" for s in sgns)),
                  flush=True)
        sol.append(entry)
    got = [e for e in sol if e.get("pack")]
    n_got = len(got)
    n_uni = sum(1 for e in sol if e["ncross"] == 1)
    if n_got:
        ratios = np.array([e["ratio"] for e in got])
        taus_ = np.array([e["r"]["tau"] for e in got])
        shift = np.array([e["pack"]["tau"] / e["r"]["tau"]
                          for e in got])
        negs_c = sum(1 for e in got if e["pack"]["negA"] > 0)
        c_x2 = sum(1 for e in got
                   if e["pack"]["lam_x2"] < -LOC_TOL)
        c_p = sum(1 for e in got if e["pack"]["lam_p"] < -LOC_TOL)
        _a, sl_ms, r2_ms = ols_line(np.log(taus_), np.log(ratios))
        med_x2r = float(np.median(
            [e["pack"]["lam_x2"] / e["pack"]["tau"] for e in got]))
        print("\n    solved on %d/%d rungs (grid-unique on %d); "
              "med m*/m0 %.2e; m*-vs-tau screen slope %+.3f (R^2 "
              "%.3f); tau'/tau med %.5f min %.5f; at m*: x2 < 0 "
              "on %d, p < 0 on %d, neg(A') > 0 on %d; med "
              "lam_x2/tau' %.1f"
              % (n_got, len(sol), n_uni,
                 float(np.median(ratios)), sl_ms, r2_ms,
                 float(np.median(shift)), float(np.min(shift)),
                 c_x2, c_p, negs_c, med_x2r))
        e3 = ("ATOM-ZEROES(%d/%d, unique-grid:%d, med-ratio=%.1e, "
              "slope=%+.2f)" % (n_got, len(sol), n_uni,
                                float(np.median(ratios)), sl_ms))
        ok_c = (n_got == len(sol) and c_x2 == 0 and c_p == 0
                and negs_c == 0)
    else:
        tops = np.array([e2["r"]["scan_top"] for e2 in sol
                         if np.isfinite(e2["r"].get(
                             "scan_top", float("nan")))])
        bests = np.array([e2["r"]["scan_best"] for e2 in sol
                          if np.isfinite(e2["r"].get(
                              "scan_best", float("nan")))])
        print("\n    DIAGNOSTIC (no bracket anywhere): lam_m at "
              "the TOP grid mass / base lam_m med %.3f (range "
              "[%.2f, %.2f]); best grid value / |base| med %+.3f "
              "(all < 0 <=> the floor never reaches zero)"
              % (float(np.median(tops)), float(np.min(tops)),
                 float(np.max(tops)),
                 float(np.median(bests))))
        e3 = "ATOM-NONE(grid 1e-12..1e+2 x m0, all floors < 0)"
        ok_c = False
        sl_ms = float("nan")
    check("E3.b typed: %s (the m*-vs-tau slope reads whether the "
          "needed edge mass is tau-coupled)" % e3, True)

    # ------------------------------------------------------------ E4
    section("E4 -- WHERE the needed negative mass sits (base Mm "
            "minimizing eigenvector)")
    shares_d = {dl: [] for dl in EDGE_DELTAS}
    peaks_x, peaks_u = [], []
    for r in truth:
        p = r["pack"]
        xs, ws, ys, vs = r["fam"]
        e = p["evec_m"]
        qn = p["Pnm"] @ e
        cn = vs * (1.0 - ys) * qn ** 2
        tot = float(np.sum(cn))
        for dl in EDGE_DELTAS:
            shares_d[dl].append(float(np.sum(cn[ys > 1.0 - dl]))
                                / max(tot, 1e-300))
        ip = int(np.argmax(cn))
        peaks_x.append(float(ys[ip]))
        peaks_u.append(float(np.arccos(np.clip(ys[ip], -1, 1))
                             * r["L"] / (2.0 * math.pi)))
    med_sh = {dl: float(np.median(shares_d[dl]))
              for dl in EDGE_DELTAS}
    print("    negative-side share within x > 1 - delta (med over "
          "rungs): " + "  ".join("%.0e: %.3f" % (dl, med_sh[dl])
                                 for dl in EDGE_DELTAS))
    print("    peak contribution: x med %.5f, fold index med %.1f"
          % (float(np.median(peaks_x)), float(np.median(peaks_u))))
    if med_sh[1e-2] >= NEGLOC_BAR:
        e4 = "NEGMASS-EDGE(share@1e-2=%.2f)" % med_sh[1e-2]
    else:
        e4 = "NEGMASS-BULK(share@1e-2=%.2f)" % med_sh[1e-2]
    check("E4.1 typed: %s (bar %.2f)" % (e4, NEGLOC_BAR), True)

    # ------------------------------------------------------------ C
    section("C -- controls")
    n_viol = 0
    n_x2neg = 0
    n_smdone = 0
    for kz in zones:
        rs = base_assembly(kz, world_fn=lambda uu, mm:
                           (uu, smooth_masses(uu)))
        xs, ws, ys, vs, _ = measure_of(rs["d"], rs["L"])
        ps = floors_pack(xs, ws, ys, vs, rs["h"])
        if ps is None:
            continue
        n_smdone += 1
        if ps["negA"] > 0:
            n_viol += 1
        if ps["lam_x2"] < -LOC_TOL:
            n_x2neg += 1
    check("C1 WARD smooth world violates (neg(A) > 0 on %d/%d) "
          "and LOCWALL reproduced (x2 < 0 on %d/%d)"
          % (n_viol, n_smdone, n_x2neg, n_smdone),
          n_viol > 0 and n_x2neg == n_smdone, kill="K2")
    rr9 = window_of(CTRL_KZ)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE_ = lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE_) > 1e-12)[0]
    rE = base_assembly(CTRL_KZ, comb=(np.log(nn.astype(float)),
                                      2.0 * lamE_[nn]
                                      / np.sqrt(nn.astype(float))))
    xsE, wsE, ysE, vsE, _ = measure_of(rE["d"], rE["L"])
    pE = floors_pack(xsE, wsE, ysE, vsE, rE["h"])
    rS = base_assembly(CTRL_KZ, scramble_seed=1)
    xsS, wsS, ysS, vsS, _ = measure_of(rS["d"], rS["L"])
    pS = floors_pack(xsS, wsS, ysS, vsS, rS["h"])
    fE = (pE is None) or pE["negA"] > 0
    fS = (pS is None) or pS["negA"] > 0
    print("    Epstein  : %s" % ("chain dies -> fires" if pE is None
                                 else "neg(A) %d" % pE["negA"]))
    print("    scramble : %s" % ("chain dies -> fires" if pS is None
                                 else "neg(A) %d" % pS["negA"]))
    check("C2 WARD both controls fire", fE and fS, kill="K2")
    # C3: no completion may certify the scramble
    still = []
    M9, L9 = rS["M"], rS["L"]
    sgn9 = (-1.0) ** np.arange(L9)
    d_v = {"a1": rS["d"] + sgn9 * rS["c"][M9 - 1]}
    d_v["a2"] = d_v["a1"] + rS["c"][0]
    cb9, _o9, _n9 = atom_lags_reflected(rS["alpha"], M9, rS["uu"],
                                        rS["mm"])
    d_v["b"] = grid_density(window_of(CTRL_KZ, scramble_seed=1
                                      )["c_ar"] + cb9)
    med_lr = (float(np.median([e["lr"] for e in got]))
              if n_got else -8.0)
    for nm, dd in d_v.items():
        xs2, ws2, ys2, vs2, _ = measure_of(dd, L9)
        pv = floors_pack(xs2, ws2, ys2, vs2, rS["h"])
        certified = (pv is not None and pv["negA"] == 0
                     and min(pv["lam_x2"], pv["lam_m"], pv["lam_p"])
                     >= -LOC_TOL)
        still.append(not certified)
        print("    scramble + %-2s: %s" % (nm, "chain dies" if pv is
              None else "neg %d, min floor %+.1e"
              % (pv["negA"], min(pv["lam_x2"], pv["lam_m"],
                                 pv["lam_p"]))))
    xs2 = np.append(xsS, 1.0)
    ws2 = np.append(wsS, (10.0 ** med_lr)
                    * (pS["m0"] if pS else 1.0))
    pv = floors_pack(xs2, ws2, ysS, vsS, rS["h"])
    certified = (pv is not None and pv["negA"] == 0
                 and min(pv["lam_x2"], pv["lam_m"], pv["lam_p"])
                 >= -LOC_TOL)
    still.append(not certified)
    print("    scramble + c : %s" % ("chain dies" if pv is None
          else "neg %d, min floor %+.1e"
          % (pv["negA"], min(pv["lam_x2"], pv["lam_m"],
                             pv["lam_p"]))))
    check("C3 WARD no completion certifies the scramble (all %d "
          "variants leave it broken)" % len(still), all(still),
          kill="K2")
    reg = v899_mechanism(base_assembly(CTRL_KZ)["d"])
    print("    v899 mechanism: T0 %.3e T1 %+.3e; leak dev %.1e, "
          "neg index %d; periodic fix dev %.1e, neg index %d"
          % (reg["T0"], reg["T1"], reg["dev_leak"], reg["n_leak"],
             reg["dev_fix"], reg["n_fix"]))
    reg_ok = (reg["dev_leak"] <= V899_WARD and reg["n_leak"] > 0
              and reg["dev_fix"] <= V899_WARD and reg["n_fix"] == 0)
    check("C4 WARD v899 mechanism regression (closed-form leak "
          "fires, periodic full-weight kill exact)", reg_ok,
          kill="K2")

    achieved = None
    for nm, okv in (("A1", ok_a1), ("A2", ok_a2), ("B", ok_b),
                    ("C-ATOM", ok_c)):
        if okv:
            achieved = nm
            break
    labels = dict(a1=lab_a1, a2=lab_a2, b=lab_b, e3=e3, e4=e4,
                  final=("COMPLETION-ACHIEVED(%s)" % achieved
                         if achieved else
                         "EDGE-OBSTRUCTION-INTRINSIC"))
    check("V0 typed headline: %s" % labels["final"], True)
    return finish(labels)


def finish(labels):
    section("V -- FROZEN VERDICT")
    n_pass = sum(1 for _n, okk in CHECKS if okk)
    n_tot = len(CHECKS)
    if KILLS:
        VERDICT = {"K1": "PIPELINE-BROKEN",
                   "K2": "WARD-BROKEN"}[KILLS[0]]
        print("\n  VERDICT: %s" % VERDICT)
    else:
        VERDICT = ("EDGECOMPL-MEASURED / %(a1)s / %(a2)s / %(b)s / "
                   "%(e3)s / %(e4)s / %(final)s / V899REG-OK"
                   % labels)
        print("\n  VERDICT: %s" % VERDICT)
    print("""
  HONEST FRAME (as frozen): a successful completion is a
  reformulation surface -- the deployed signed comb measure would
  be, at matched finite degree per rung, the shadow of a
  nonnegative measure after an explicit source-only boundary
  completion.  It is NOT a bound, NOT a tail theorem, and proves
  nothing beyond the deployed rungs.  A tau-coupled solved mass
  (slope ~ 1+) is a relocation-type object, not an O(1)
  completion.  NO RH claim.  No marker moves.""")
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed"
          % (time.time() - T0, n_tot, n_tot - n_pass))
    return 0 if n_pass == n_tot else 1


if __name__ == "__main__":
    raise SystemExit(main())
