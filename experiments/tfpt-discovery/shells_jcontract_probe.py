#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""shells_jcontract_probe -- PRIME.SHELLS.JCONTRACT.01
(EXPLORATION ONLY, experiments/tfpt-discovery/; the lead's cheap
multiplicative-shell kill test before any larger RH programme,
2026-08-13).

QUESTION.  Single-prime insertion is not monotone, while the complete
von-Mangoldt comb is positive.  Does the exact rank-two IIKS structure
become J-contractive when the arithmetic source is advanced by complete
multiplicative shells rather than one prime at a time?

THE SHELLS (frozen before measurement).  X = 256, the deployed kz=9
relation-carrier range.  The primes p <= X are sorted in log p and split
into deterministic consecutive blocks of two primes (the final block
may contain one): 27 nonempty logarithmic shells.  Shell S_j contains
the COMPLETE towers {p^k <= X} for its primes.  The relation object at
stage j is
    A_j = {n <= X: every prime factor of n is in shells <= j}.
Thus A_j is divisor closed, A_0={1}, and A_j\A_{j-1} is the new
relation layer.  This is the precise closure rule: the event increment
is a disjoint union of complete prime towers, while every cumulative
relation algebra contains every divisor needed by mu*1=delta and
Lambda=mu*log.  Products that exceed X are the same quotient ideal as
in multiplicative_relation_probe.

THE TRANSFER (amended after smoke 1, source-derived, no fit).  The
FIRST smoke exposed an exact domain fact: independently rebuilt
partial combs are not displacement-rank-two (max s3/s1=3.75e-2), and
the arch-only baseline does not build.  Therefore they cannot define
the requested exact 2x2 shell cocycle.  The fail-first repair keeps the
ONE exact object: each world's COMPLETE deployed kz=9 dressed port.
Its positive/negative folded measures -> deployed h+1 Jacobi chain ->
negative-arm Gram -> bulk Schur complement D_P obey
    [Y,D_P] = f g^T - g f^T
at rank two.  In the predecessor's canonical gauge define
    F_i=(f_i,g_i)^T, G_i=(g_i,-f_i)^T,
    L_i(s,z)=I-s F_i G_i^T/(z-y_i),
    H(s,z)=ordered product_i L_i(s,z).
G_i^T F_i=0 gives det L_i=1 symbolically.  The complete shell step is
    T_j(z)=H(s_j,z) H(s_{j-1},z)^{-1},
where s_j is the cumulative shell load.  Loads are source-only:
sum of the deployed atom masses in each relation-complete shell,
normalized so s_0=0 and s_27=1 (signed for Epstein; the denominator is
warded nonzero).  Thus the path is the canonical radial loading of the
FULL exact displacement generator; complete-shell grouping changes
the nonlinear monodromy quotient but never leaves the exact rank-two
class.  It is not the round-45 TLS fit and does not normalize a result
into contractivity.  The half-plane transfer is
Cayley-conjugated with the deployed K_HD to U_j=K_HD T_j K_DH and
tested in the existing disk Krein metric J=diag(1,-1).

GRID + NUMERICS.  Z = {2i, i, .5i, -1.5+.5i, 1.5+.5i,
.25+.05i}.  Every final 2x2 Hermitian defect
    Delta_j(z)=J-U_j(z)^* J U_j(z)
is classified with a backward rounding enclosure
eta=256 eps max(1,||U||_2^2): PSD only when lambda_min-eta>=0,
NONPSD only when lambda_min+eta<0, otherwise UNRESOLVED.  The enclosure
certifies the final arithmetic on the deployed float IIKS object; it
does not upgrade the upstream float construction to an exact theorem.
For PSD defects R=sqrt(Delta) is built spectrally and R^*R=Delta is
warded.  Rank uses the same eta.  Products are checked both directly
and by
    Delta(AB)=Delta(B)+B^* Delta(A) B.

PROTOCOL.
 S0  Exact relation wards on every A_j and every n<=X:
     divisor closure; mu*1=delta over integers; mu*log=Lambda in the
     exact free log-prime module (Fraction coefficients); true event
     support equals all prime powers <=X and every shell is a complete
     tower union.  AST firewall and symbolic det(L_i)=1.
 S1  Build the four COMPLETE full-comb IIKS states; ward [Y,D_P] rank
     two and off-diagonal IIKS reconstruction.  Ward every source-load
     path: 28 boundaries, s_0=0, s_last=1, nonzero denominator.
 S2  Shell defect census over 27x6 points: PSD/NONPSD/UNRESOLVED and
     ranks 0/1/2; R-factor residual; det(T)=1; every aggregate prefix;
     direct-vs-product and composition-identity wards.
 S3  Single-prime comparison: 54 complete one-prime-tower steps on the
     same path.  The demanded anatomy is FAIL/OSCILLATE: at least one
     certified NONPSD point and not all steps PSD.  Sign changes of the
     minimum defect eigenvalue are reported.
 S4  Relation factorization: (i) det T=1 is tested numerically and
     follows symbolically from G_i^T F_i=0; (ii) the structured
     Delta=R^*R form holds exactly on the certified PSD census only;
     (iii) discriminant zero (the only exact square forced by the
     rank-one nilpotent local relation) is tested on shell transfers.
     A nonzero shell discriminant is reported as NO-ZERO-SQUARE; no
     unsupported claim that an arbitrary sampled complex number is or
     is not a rational-function square is made.
 S5  Controls run through the SAME cumulative shell protocol:
     Epstein x^2+5y^2 (events assigned by largest-prime-factor shell)
     and mass-fixed scramble MUST each have a certified NONPSD shell
     point.  Smooth masses at the true event positions are reported.
 S6  Tau screen (diagnostic only): slope of log|minimum shell defect|
     against log|1-lambda_max(D_P)|; PASS if |slope|<=.30, RELOC if
     slope>=.70, otherwise AMBIG.  Tau never enters a transfer.

VERDICT (frozen enum).
 JCONTRACT-SIGNAL iff all true shell points and all aggregate prefixes
 are certified PSD, the single-prime path fails/oscillates, Epstein and
 scramble each break J-contractivity, and all algebra/pipeline wards
 pass.  JCONTRACT-DEAD(reason) if a true shell is certified NONPSD, the
 single-prime path is wholly J-contractive, or either mandatory control
 stays wholly J-contractive.  JCONTRACT-MIXED(anatomy) covers only
 unresolved/mixed true or control censuses without a DEAD trigger.
 Pipeline/algebra ward failure is typed PIPELINE-BROKEN/WARD-BROKEN,
 not converted into a physics verdict.

ANTI-CIRCULARITY.  Shells and radial loads use only integer
factorization, deployed source labels and deployed atom masses; no
defect, wall margin, eigenvalue or control result chooses a boundary
or load.  T_j is a quotient on the independently built COMPLETE IIKS
object; no per-shell fit and no J-projection occurs.  Tau is
report-only.  Epstein/scramble rules and all bars are frozen.

FIREWALL.  No zeros, no prime oracle, no RH claim, no marker move.
v563 is READ-ONLY through the predecessor module.  RNG occurs only in
core.build_window(..., scramble_seed=1).  Stdout only.

SMOKE DISCLOSURE 1 (2026-08-13, summarized before this amendment):
17 checks, 10 pass / 7 fail, 0.3 s.  Arithmetic/shell wards passed
(54 primes, 27 shells, 70 prime powers).  Every arch-only baseline
failed (8/9 states built), and partial-comb ports were not rank two
(max s3/s1 3.75e-2; reconstruction 3.40e-2), so no defect was read and
the smoke typed PIPELINE-BROKEN.  Fail-first amendment: replace the
invalid partial-comb rebuild by the radial loading H(s,z) of each
world's one COMPLETE exact IIKS generator, with shell loads fixed by
source masses.  No measured defect, control result, bar or verdict
informed the repair.  SPEC remains unfrozen pending smoke 2.

SMOKE DISCLOSURE 2 (2026-08-13, summarized before freezing): the
amended radial-loading smoke passed 18/18 in 0.1 s, but exposed
float64 cancellation in the scramble quotient (det dev 288, direct
20.1, composition 820); truth itself was stable and already NONPSD
24/24.  A numerical-only repair evaluates every 2x2 monodromy,
quotient, defect and composition identity at 90 decimal digits while
retaining the same deployed float IIKS inputs.  Smoke 3 then passed
18/18 in 1.1 s: rank/reconstruction 8.72e-15/1.24e-13; truth
PSD/NONPSD/UNRESOLVED 0/24/0, Epstein 3/15/6, scramble 0/24/0,
smooth 0/24/0, single-prime 0/36/0; scramble det/direct/composition
1.91e-73/3.64e-74/1.59e-73; truth 1.47e-90/4.73e-91/4.39e-91;
tau slope 2.017 (RELOC).  No construction, bar, rule or enum changed
after smoke 3.  SPEC v2 is now frozen for the full run.

Run smoke:
  JCONTRACT_SMOKE=1 experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/shells_jcontract_probe.py
Run frozen:
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/shells_jcontract_probe.py
"""

import ast
import hashlib
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
import sympy as sp
from mpmath import mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_VERIFY = os.path.abspath(os.path.join(_HERE, "..", "..", "verification"))
sys.path.insert(0, _HERE)
sys.path.insert(0, _VERIFY)

import port_riemann_hilbert_setup_probe as iiks  # noqa: E402
import v563_paper2_readouts as core              # noqa: E402  (READ-ONLY)


SPEC_FROZEN = True
FROZEN_SPEC = r"""PRIME.SHELLS.JCONTRACT.01 spec v2, 2026-08-13,
fail-first amendment after smoke 1: partial combs are not rank-two;
use the complete-world exact generator with source-mass radial loading.
KZ=9; X=256; sorted primes are consecutive log-shells of two primes,
giving 27 shells; cumulative A_j is the X-truncated integer algebra
generated by all primes through shell j.  True shell events are all
complete p-power towers.  Per world build ONE complete dressed port.
Shell load c_j=sum deployed atom masses in shell / total mass (signed
for Epstein), s_j=sum_{k<=j}c_k, ward s0=0/slast=1/nonzero total.
Transfer = relative radial bare-IIKS monodromy
H(s_j)H(s_{j-1})^{-1}, L_i(s)=I-sF_iG_i^T/(z-y_i), canonical
predecessor gauge, ascending y order, no fit and no J-projection. Cayley
K_HD=[[-1,i],[1,i]], J=diag(1,-1).  Z grid=(2i,i,.5i,-1.5+.5i,
1.5+.5i,.25+.05i).  Defect enclosure eta=256 eps
max(1,||U||_2^2); PSD iff lmin-eta>=0, NONPSD iff lmin+eta<0.
All 2x2 arithmetic is evaluated at MP_DPS=90 from the unchanged
deployed float IIKS inputs; the eta disclosure remains an upstream
float-object enclosure, not an exact-theorem upgrade.
IIKS rank bar 1e-10; reconstruction bar 1e-8; det bar 2e-7;
product/composition bar 2e-7; R factor bar 2e-7.  Controls:
Epstein x^2+5y^2 and core scramble seed 1 must each contain a
certified NONPSD shell-grid point; smooth mass world report-only.
Single-prime path is the 54 complete prime towers and must contain
NONPSD.  Signal/dead/mixed rules are exactly those in the module
docstring.  Tau screen bands .30/.70, diagnostic only.  Smoke uses
first 8 shells, first 3 z points, first 12 prime towers, and all four
worlds; smoke never emits the frozen verdict.  Runtime cap 25 min.
No zeros, no RH claim, stdout only."""

KZ = 9
XMAX = 256
PRIMES_PER_SHELL = 2
Z_GRID = (2j, 1j, 0.5j, -1.5 + 0.5j, 1.5 + 0.5j, 0.25 + 0.05j)
IIKS_RANK_BAR = 1.0e-10
IIKS_REC_BAR = 1.0e-8
DET_BAR = 2.0e-7
ALG_BAR = 2.0e-7
R_FACTOR_BAR = 2.0e-7
ROUND_FACTOR = 256.0
SLOPE_PASS = 0.30
SLOPE_RELOC = 0.70
SCRAMBLE_SEED = 1
RUNTIME_CAP = 25.0 * 60.0
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

K_HD = np.array([[-1.0, 1j], [1.0, 1j]], dtype=complex)
K_DH = np.linalg.inv(K_HD)
J2 = np.diag([1.0, -1.0]).astype(complex)
MP_DPS = 90

CHECKS = []
KILLS = []
T0 = time.time()


def check(name, ok, detail="", kill=None):
    ok = bool(ok)
    CHECKS.append((name, ok))
    if kill and not ok:
        KILLS.append(kill)
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           (" -- " + detail) if detail else ""),
          flush=True)
    return ok


def section(title):
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76, flush=True)


def ast_firewall():
    with open(os.path.abspath(__file__), encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    bad = []
    for node in ast.walk(tree):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in BANNED_IDS:
            bad.append(name)
    return bad


def own_primes(limit):
    sieve = [True] * (limit + 1)
    sieve[:2] = [False, False]
    for p in range(2, int(math.isqrt(limit)) + 1):
        if sieve[p]:
            for n in range(p * p, limit + 1, p):
                sieve[n] = False
    return [p for p in range(2, limit + 1) if sieve[p]]


def smallest_prime_factors(limit):
    spf = list(range(limit + 1))
    if limit >= 1:
        spf[1] = 1
    for p in range(2, int(math.isqrt(limit)) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


SPF = smallest_prime_factors(XMAX)


def factor_exp(n):
    out = {}
    while n > 1:
        p = SPF[n]
        out[p] = out.get(p, 0) + 1
        n //= p
    return out


def divisors(n):
    out = [1]
    for p, exponent in factor_exp(n).items():
        old = list(out)
        power = 1
        for _ in range(exponent):
            power *= p
            out += [d * power for d in old]
    return sorted(out)


def largest_prime_factor(n):
    fs = factor_exp(n)
    return max(fs) if fs else 1


def mobius_sieve(limit):
    mu = [1] * (limit + 1)
    mu[0] = 0
    primes = own_primes(limit)
    for p in primes:
        for n in range(p, limit + 1, p):
            mu[n] *= -1
        p2 = p * p
        for n in range(p2, limit + 1, p2):
            mu[n] = 0
    return mu


MU = mobius_sieve(XMAX)
PRIMES = own_primes(XMAX)
SHELL_PRIMES = tuple(tuple(PRIMES[k:k + PRIMES_PER_SHELL])
                     for k in range(0, len(PRIMES), PRIMES_PER_SHELL))
SHELL_CUTS = tuple(block[-1] for block in SHELL_PRIMES)


def is_prime_power(n):
    fs = factor_exp(n)
    return len(fs) == 1


def lambda_module(n):
    fs = factor_exp(n)
    if len(fs) == 1:
        return {next(iter(fs)): Fraction(1)}
    return {}


def log_module(n):
    return {p: Fraction(e) for p, e in factor_exp(n).items()}


def module_add(dst, src, scalar=1):
    for p, value in src.items():
        dst[p] = dst.get(p, Fraction(0)) + scalar * value
        if dst[p] == 0:
            del dst[p]


def relation_wards(shell_count):
    mu_one = True
    mu_log = True
    for n in range(1, XMAX + 1):
        ds = divisors(n)
        mu_one &= sum(MU[d] for d in ds) == (1 if n == 1 else 0)
        acc = {}
        for d in ds:
            module_add(acc, log_module(n // d), MU[d])
        mu_log &= acc == lambda_module(n)

    closure = True
    nested = True
    previous = {1}
    for cut in SHELL_CUTS[:shell_count]:
        current = {n for n in range(1, XMAX + 1)
                   if largest_prime_factor(n) <= cut}
        nested &= previous <= current
        for n in current:
            closure &= all(d in current for d in divisors(n))
        previous = current
    return mu_one, mu_log, closure, nested


def event_shell_index(n):
    pmax = largest_prime_factor(n)
    for j, cut in enumerate(SHELL_CUTS):
        if pmax <= cut:
            return j
    raise AssertionError("event outside shell range")


def exact_shell_support():
    events = {n for n in range(2, XMAX + 1) if is_prime_power(n)}
    union = set()
    complete = True
    for block in SHELL_PRIMES:
        shell = {p ** k for p in block
                 for k in range(1, 64) if p ** k <= XMAX}
        union |= shell
        for n in shell:
            complete &= all((d == 1 or d in shell) for d in divisors(n))
    return events, union, complete


def lambda_epstein(limit):
    radius = int(math.isqrt(limit)) + 1
    reps = np.zeros(limit + 1)
    for x in range(-radius, radius + 1):
        for y in range(-radius, radius + 1):
            n = x * x + 5 * y * y
            if 1 <= n <= limit:
                reps[n] += 1.0
    coeff = reps / 2.0
    lam = np.zeros(limit + 1)
    for n in range(2, limit + 1):
        value = coeff[n] * math.log(n)
        for d in range(2, n):
            if n % d == 0:
                value -= lam[d] * coeff[n // d]
        lam[n] = value
    return lam


def cell_widths(uu):
    uu = np.asarray(uu, float)
    widths = np.zeros(len(uu))
    widths[1:-1] = 0.5 * (uu[2:] - uu[:-2])
    widths[0] = uu[1] - uu[0]
    widths[-1] = uu[-1] - uu[-2]
    return widths


def smooth_masses(uu):
    return 2.0 * np.exp(np.asarray(uu, float) / 2.0) * cell_widths(uu)


def rounded_labels(uu):
    labels = np.rint(np.exp(np.asarray(uu, float))).astype(int)
    err = float(np.max(np.abs(np.asarray(uu, float) - np.log(labels))))
    return labels, err


def canonical_generators(commutator):
    f, g, sv = iiks.antisym_generators(commutator)
    anchor = 0
    radius = math.hypot(float(f[anchor]), float(g[anchor]))
    if radius <= 1e-300:
        raise np.linalg.LinAlgError("zero generator anchor")
    cosine = float(f[anchor]) / radius
    sine = float(g[anchor]) / radius
    return cosine * f + sine * g, -sine * f + cosine * g, sv


def build_iiks_model(rr, uu, mm):
    h = int(rr["h"])
    M = int(rr["M"])
    D = float(rr["D"])
    alpha = float(rr["alpha"])
    c_arch = np.asarray(core.arch_lags(M, D), float)
    if len(uu):
        c_atom, _ = core.atom_lags_at(alpha, M, np.asarray(uu, float),
                                      np.asarray(mm, float))
        c_atom = np.asarray(c_atom, float)
    else:
        c_atom = np.zeros_like(c_arch)
    density = iiks.grid_density(c_arch + c_atom)
    length = 2 * M - 2
    xs, ws, _ = iiks.folded_measure(density, length, +1.0)
    ys, vs, folded_negative = iiks.folded_measure(
        density, length, -1.0)
    al, be, m0, steps = iiks.lanczos_chain(xs, ws, h + 1)
    if steps < h + 1 or np.any(be <= 0.0):
        return None
    polynomials = iiks.eval_chain(al, be, m0, ys, h)
    gram = (np.sqrt(vs)[:, None] * (polynomials @ polynomials.T)
            * np.sqrt(vs)[None, :])
    gram = 0.5 * (gram + gram.T)
    tau_nodes = (2.0 * math.pi * folded_negative / length) / D
    port = tau_nodes <= float(np.max(tau_nodes)) / 10.0
    ip, ib = np.where(port)[0], np.where(~port)[0]
    if len(ip) < 4 or len(ib) < 1:
        return None
    pblock = gram[np.ix_(ip, ip)]
    cross = gram[np.ix_(ip, ib)]
    bulk = gram[np.ix_(ib, ib)]
    dp = pblock + cross @ np.linalg.solve(np.eye(len(ib)) - bulk,
                                          cross.T)
    dp = 0.5 * (dp + dp.T)
    yport = ys[ip]
    ydiag = np.diag(yport)
    comm = ydiag @ dp - dp @ ydiag
    f, g, sv = canonical_generators(comm)
    rec = iiks.integrable_offdiag(f, g, yport)
    dp0 = dp.copy()
    np.fill_diagonal(dp0, 0.0)
    rec_rel = float(np.linalg.norm(rec - dp0)
                    / max(np.linalg.norm(dp0), 1e-300))
    rank_ratio = float(sv[2] / sv[0]) if len(sv) > 2 else 0.0
    return {
        "f": f,
        "g": g,
        "y": yport,
        "rank_ratio": rank_ratio,
        "rec_rel": rec_rel,
        "lam_dp": float(np.linalg.eigvalsh(dp)[-1]),
        "tau": 1.0 - float(np.linalg.eigvalsh(dp)[-1]),
        "lam_gram": float(np.linalg.eigvalsh(gram)[-1]),
        "nport": len(ip),
    }


def mp_matrix(rows):
    return mp.matrix([[mp.mpc(value.real, value.imag)
                       if isinstance(value, complex) else mp.mpf(value)
                       for value in row] for row in rows])


def adjoint(matrix):
    return matrix.transpose_conj()


def matrix_norm(matrix):
    return mp.sqrt(sum(abs(matrix[i, j]) ** 2
                       for i in range(matrix.rows)
                       for j in range(matrix.cols)))


def hermitian_eigs_mp(matrix):
    hermitian = (matrix + adjoint(matrix)) / 2
    a = mp.re(hermitian[0, 0])
    d = mp.re(hermitian[1, 1])
    off = hermitian[0, 1]
    radius = mp.sqrt(((a - d) / 2) ** 2 + abs(off) ** 2)
    center = (a + d) / 2
    return center - radius, center + radius


def monodromy(model, z, scale):
    transfer = mp.eye(2)
    zmp = mp.mpc(float(z.real), float(z.imag))
    smp = mp.mpf(float(scale))
    order = np.argsort(model["y"])
    for idx in order:
        f = mp.mpf(float(model["f"][idx]))
        g = mp.mpf(float(model["g"][idx]))
        denominator = zmp - mp.mpf(float(model["y"][idx]))
        residue = mp.matrix([[f * g, -f * f],
                             [g * g, -g * f]])
        local = mp.eye(2) - smp * residue / denominator
        transfer = local @ transfer
    return transfer


def inv2(matrix):
    determinant = mp.det(matrix)
    return mp.matrix([[matrix[1, 1], -matrix[0, 1]],
                      [-matrix[1, 0], matrix[0, 0]]]) / determinant


def disk_step(model, previous_scale, current_scale, z):
    halfplane = (monodromy(model, z, current_scale)
                 @ inv2(monodromy(model, z, previous_scale)))
    khd = mp_matrix([[-1.0, 1j], [1.0, 1j]])
    kdh = khd ** -1
    return khd @ halfplane @ kdh


def defect_read(transfer):
    jmetric = mp.matrix([[1, 0], [0, -1]])
    defect = jmetric - adjoint(transfer) @ jmetric @ transfer
    defect = (defect + adjoint(defect)) / 2
    eig_lo, eig_hi = hermitian_eigs_mp(defect)
    gram_eigs = hermitian_eigs_mp(adjoint(transfer) @ transfer)
    norm_squared = max(mp.mpf(0), gram_eigs[1])
    eta = (mp.mpf(ROUND_FACTOR) * mp.mpf(np.finfo(float).eps)
           * max(mp.mpf(1), norm_squared))
    if eig_lo - eta >= 0:
        status = "PSD"
    elif eig_lo + eta < 0:
        status = "NONPSD"
    else:
        status = "UNRESOLVED"
    rank = (int(eig_lo > eta) + int(eig_hi > eta)
            if status == "PSD" else None)
    rres = None
    if status == "PSD":
        determinant_defect = max(mp.mpf(0), mp.re(mp.det(defect)))
        root_det = mp.sqrt(determinant_defect)
        denominator = mp.sqrt(max(
            mp.mpf(0), mp.re(defect[0, 0] + defect[1, 1])
            + 2 * root_det))
        if denominator == 0:
            root = mp.zeros(2)
        else:
            root = (defect + root_det * mp.eye(2)) / denominator
        rres = float(matrix_norm(adjoint(root) @ root - defect)
                     / max(mp.mpf(1), matrix_norm(defect)))
    khd = mp_matrix([[-1.0, 1j], [1.0, 1j]])
    halfplane = (khd ** -1) @ transfer @ khd
    determinant = mp.det(halfplane)
    discriminant = (halfplane[0, 0] + halfplane[1, 1]) ** 2 \
        - 4 * determinant
    return {
        "defect": defect,
        "eigs": (eig_lo, eig_hi),
        "eta": float(eta),
        "status": status,
        "rank": rank,
        "rres": rres,
        "detdev": float(abs(determinant - 1)),
        "discriminant": discriminant,
        "norm_squared": norm_squared,
    }


def source_path(world, shell_count, prime_mode=False):
    labels = world["labels"]
    mm = world["mm"]
    if prime_mode:
        cuts = PRIMES[:shell_count]
    else:
        cuts = SHELL_CUTS[:shell_count]
    total = float(np.sum(mm))
    if abs(total) <= 1e-14 * max(1.0, float(np.sum(np.abs(mm)))):
        return None, total
    scales = [0.0]
    for cut in cuts:
        mask = np.array([largest_prime_factor(int(n)) <= cut
                         for n in labels], dtype=bool)
        scales.append(float(np.sum(mm[mask])) / total)
    return np.asarray(scales, float), total


def census(name, model, scales, z_grid):
    rows = []
    aggregate = {z: mp.eye(2) for z in z_grid}
    direct_dev = 0.0
    comp_dev = 0.0
    prefix_nonpsd = 0
    status_counts = {"PSD": 0, "NONPSD": 0, "UNRESOLVED": 0}
    rank_counts = {0: 0, 1: 0, 2: 0}
    detdev = 0.0
    rres = 0.0
    disc_zero = 0
    model_deaths = int(model is None or scales is None)
    if model_deaths:
        return {
            "name": name,
            "model_deaths": model_deaths,
            "rows": [],
            "status_counts": status_counts,
            "rank_counts": rank_counts,
            "step_all_psd": 0,
            "nsteps": max(0, len(scales) - 1) if scales is not None else 0,
            "prefix_nonpsd": 0,
            "direct_dev": float("inf"),
            "comp_dev": float("inf"),
            "detdev": float("inf"),
            "rres": float("inf"),
            "disc_zero": 0,
            "sign_changes": 0,
            "minima": [],
        }

    minima = []
    step_all_psd = 0
    for step_index, (previous_scale, current_scale) in enumerate(
            zip(scales[:-1], scales[1:]), 1):
        step_statuses = []
        step_minimum = float("inf")
        for z in z_grid:
            transfer = disk_step(model, previous_scale, current_scale, z)
            read = defect_read(transfer)
            status_counts[read["status"]] += 1
            step_statuses.append(read["status"])
            step_minimum = min(step_minimum, float(read["eigs"][0]))
            if read["rank"] is not None:
                rank_counts[read["rank"]] += 1
            detdev = max(detdev, float(read["detdev"]))
            if read["rres"] is not None:
                rres = max(rres, float(read["rres"]))
            if abs(read["discriminant"]) <= mp.mpf(read["eta"]):
                disc_zero += 1

            old_aggregate = aggregate[z]
            jmetric = mp.matrix([[1, 0], [0, -1]])
            old_defect = (jmetric
                          - adjoint(old_aggregate) @ jmetric @ old_aggregate)
            step_defect = read["defect"]
            aggregate[z] = transfer @ old_aggregate
            new_defect = (jmetric
                          - adjoint(aggregate[z]) @ jmetric @ aggregate[z])
            composed = (old_defect + adjoint(old_aggregate)
                        @ step_defect @ old_aggregate)
            comp_dev = max(
                comp_dev,
                float(matrix_norm(new_defect - composed)
                      / max(mp.mpf(1), matrix_norm(new_defect))))
            direct = disk_step(model, scales[0], current_scale, z)
            direct_dev = max(
                direct_dev,
                float(matrix_norm(aggregate[z] - direct)
                      / max(mp.mpf(1), matrix_norm(direct))))
            prefix_read = defect_read(aggregate[z])
            prefix_nonpsd += prefix_read["status"] == "NONPSD"
        step_all_psd += all(status == "PSD" for status in step_statuses)
        minima.append(step_minimum)
        rows.append((step_index, step_statuses, step_minimum,
                     1.0 - current_scale * model["lam_dp"],
                     model["nport"]))

    signs = [0 if abs(value) <= 1e-14 else (1 if value > 0 else -1)
             for value in minima]
    nonzero_signs = [value for value in signs if value]
    sign_changes = sum(a != b for a, b in zip(
        nonzero_signs[:-1], nonzero_signs[1:]))
    return {
        "name": name,
        "model_deaths": 0,
        "rows": rows,
        "status_counts": status_counts,
        "rank_counts": rank_counts,
        "step_all_psd": step_all_psd,
        "nsteps": len(scales) - 1,
        "prefix_nonpsd": prefix_nonpsd,
        "direct_dev": direct_dev,
        "comp_dev": comp_dev,
        "detdev": detdev,
        "rres": rres,
        "disc_zero": disc_zero,
        "sign_changes": sign_changes,
        "minima": minima,
    }


def print_census(result, nz):
    print("    %-13s steps %2d | all-z PSD %2d | points PSD/NON/UNR "
          "%3d/%3d/%3d | ranks 0/1/2 %3d/%3d/%3d"
          % (result["name"], result["nsteps"], result["step_all_psd"],
             result["status_counts"]["PSD"],
             result["status_counts"]["NONPSD"],
             result["status_counts"]["UNRESOLVED"],
             result["rank_counts"][0], result["rank_counts"][1],
             result["rank_counts"][2]))
    print("      model deaths %d | aggregate NONPSD points %d/%d | "
          "det max %.2e | R residual %.2e | direct %.2e | comp %.2e"
          % (result["model_deaths"], result["prefix_nonpsd"],
             result["nsteps"] * nz, result["detdev"], result["rres"],
             result["direct_dev"], result["comp_dev"]))
    print("      discriminant zero-square points %d/%d | minimum-eigenvalue "
          "sign changes %d"
          % (result["disc_zero"], result["nsteps"] * nz,
             result["sign_changes"]))


def tau_screen(rows):
    x, y = [], []
    for _index, _statuses, minimum, tau, _nport in rows:
        if abs(minimum) > 1e-14 and abs(tau) > 1e-14:
            x.append(math.log(abs(tau)))
            y.append(math.log(abs(minimum)))
    if len(x) < 3 or float(np.std(x)) <= 1e-14:
        return float("nan"), "TAU-AMBIG"
    slope = float(np.polyfit(np.asarray(x), np.asarray(y), 1)[0])
    label = ("TAU-PASS" if abs(slope) <= SLOPE_PASS else
             "TAU-RELOC" if slope >= SLOPE_RELOC else "TAU-AMBIG")
    return slope, label


def symbolic_local_ward():
    f, g, y, z = sp.symbols("f g y z")
    source = sp.Matrix([f, g])
    dual = sp.Matrix([[g, -f]])
    local = sp.eye(2) - source * dual / (z - y)
    determinant = sp.factor(local.det())
    discriminant = sp.factor(sp.trace(local) ** 2 - 4 * local.det())
    nilpotence = sp.simplify((dual * source)[0])
    return determinant, discriminant, nilpotence


def main():
    mp.dps = MP_DPS
    smoke = os.environ.get("JCONTRACT_SMOKE", "0") == "1"
    if not SPEC_FROZEN and not smoke:
        print("REFUSED: SPEC is not frozen; run JCONTRACT_SMOKE=1 first.")
        return 2
    shell_count = 8 if smoke else len(SHELL_PRIMES)
    z_grid = Z_GRID[:3] if smoke else Z_GRID
    prime_count = 12 if smoke else len(PRIMES)

    section("PRIME.SHELLS.JCONTRACT.01 -- multiplicative-shell kill test")
    print("    mode = %s | SPEC_FROZEN = %s | SPEC_SHA = %s"
          % ("SMOKE" if smoke else "FROZEN", SPEC_FROZEN,
             hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()))
    print("    NO RH claim; experiment-only; stdout only.")

    section("S0 -- firewall, exact relation algebra, shell construction")
    check("S0.1 AST firewall clean", not ast_firewall(), kill="K2")
    mu_one, mu_log, closure, nested = relation_wards(shell_count)
    check("S0.2 [EXACT] mu*1=delta for all n<=%d" % XMAX,
          mu_one, kill="K2")
    check("S0.3 [EXACT] mu*log=Lambda in free log-prime module "
          "for all n<=%d" % XMAX, mu_log, kill="K2")
    check("S0.4 cumulative A_j divisor-closed and nested on %d "
          "shell stages" % shell_count, closure and nested, kill="K2")
    expected_events, shell_union, complete = exact_shell_support()
    check("S0.5 true event support is exactly all %d prime powers "
          "<=%d; every shell is complete under non-unit divisors"
          % (len(expected_events), XMAX),
          expected_events == shell_union and complete, kill="K2")
    det_symbolic, disc_symbolic, nil_symbolic = symbolic_local_ward()
    check("S0.6 [SYMBOLIC] G^T F=%s, det L(z)=%s, local "
          "discriminant=%s=0^2"
          % (nil_symbolic, det_symbolic, disc_symbolic),
          nil_symbolic == 0 and det_symbolic == 1
          and disc_symbolic == 0, kill="K2")
    print("    %d primes -> %d shells; active %d; blocks: %s"
          % (len(PRIMES), len(SHELL_PRIMES), shell_count,
             " ".join("%d-%d" % (block[0], block[-1])
                      for block in SHELL_PRIMES[:shell_count])))

    rr_true = core.build_window(KZ)
    labels_true, label_err = rounded_labels(rr_true["uu"])
    support_true = set(int(n) for n in labels_true)
    check("S0.7 deployed kz=%d labels are exact integer logs "
          "(max dev %.1e) and support is the %d prime powers <=%d"
          % (KZ, label_err, len(expected_events), XMAX),
          label_err <= 2e-12 and support_true == expected_events,
          kill="K1")

    uu_true = np.asarray(rr_true["uu"], float)
    mm_true = 2.0 * np.asarray(rr_true["lam"], float)
    rr_scramble = core.build_window(KZ, scramble_seed=SCRAMBLE_SEED)
    uu_scramble = np.asarray(rr_scramble["uu"], float)
    mm_scramble = 2.0 * np.asarray(rr_scramble["lam"], float)
    check("S0.8 mass-fixed scramble preserves event count and masses",
          len(uu_scramble) == len(labels_true)
          and np.allclose(mm_scramble, mm_true, rtol=0.0, atol=0.0),
          kill="K1")

    epstein_lambda = lambda_epstein(XMAX)
    epstein_labels = np.nonzero(np.abs(epstein_lambda) > 1e-12)[0]
    epstein_uu = np.log(epstein_labels.astype(float))
    epstein_mm = (2.0 * epstein_lambda[epstein_labels]
                  / np.sqrt(epstein_labels.astype(float)))
    worlds = {
        "truth": {
            "labels": labels_true, "uu": uu_true, "mm": mm_true,
        },
        "Epstein": {
            "labels": epstein_labels, "uu": epstein_uu,
            "mm": epstein_mm,
        },
        "scramble": {
            "labels": labels_true, "uu": uu_scramble,
            "mm": mm_scramble,
        },
        "smooth": {
            "labels": labels_true, "uu": uu_true,
            "mm": smooth_masses(uu_true),
        },
    }

    section("S1 -- complete-world IIKS states and source-load paths")
    models_by_world = {}
    paths_by_world = {}
    max_rank = 0.0
    max_rec = 0.0
    for name, world in worlds.items():
        model = build_iiks_model(rr_true, world["uu"], world["mm"])
        scales, total_mass = source_path(world, shell_count)
        models_by_world[name] = model
        paths_by_world[name] = scales
        if model is not None:
            max_rank = max(max_rank, model["rank_ratio"])
            max_rec = max(max_rec, model["rec_rel"])
        print("    %-9s: full model %s; port nodes %s; total mass "
              "%+.6e; path endpoint %s"
              % (name, "BUILT" if model is not None else "DEAD",
                 str(model["nport"]) if model is not None else "none",
                 total_mass,
                 ("%.9f" % scales[-1]) if scales is not None else "none"))
    check("S1.1 all four complete-world IIKS states built",
          all(model is not None for model in models_by_world.values()),
          kill="K1")
    path_wards = all(
        path is not None and abs(path[0]) <= 1e-15
        and np.all(np.isfinite(path))
        for path in paths_by_world.values())
    endpoint_ward = (smoke or all(
        abs(path[-1] - 1.0) <= 1e-12
        for path in paths_by_world.values() if path is not None))
    check("S1.2 source paths finite with s0=0%s"
          % (" (smoke endpoints are partial)"
             if smoke else " and s_last=1"),
          path_wards and endpoint_ward, kill="K1")
    check("S1.3 IIKS rank/reconstruction wards on every complete state: "
          "max s3/s1 %.2e <= %.0e; rec %.2e <= %.0e"
          % (max_rank, IIKS_RANK_BAR, max_rec, IIKS_REC_BAR),
          max_rank <= IIKS_RANK_BAR and max_rec <= IIKS_REC_BAR,
          kill="K1")

    section("S2/S5 -- shell defects, products, and controls")
    results = {}
    for name in ("truth", "Epstein", "scramble", "smooth"):
        results[name] = census(name, models_by_world[name],
                               paths_by_world[name], z_grid)
        print_census(results[name], len(z_grid))
    truth = results["truth"]
    check("S2.1 det(T)=1 census max dev %.2e <= %.0e"
          % (truth["detdev"], DET_BAR),
          truth["detdev"] <= DET_BAR, kill="K2")
    check("S2.2 product telescoping %.2e and defect-composition "
          "identity %.2e <= %.0e"
          % (truth["direct_dev"], truth["comp_dev"], ALG_BAR),
          truth["direct_dev"] <= ALG_BAR
          and truth["comp_dev"] <= ALG_BAR, kill="K2")
    check("S2.3 R^*R reconstruction on certified PSD points: "
          "max residual %.2e <= %.0e"
          % (truth["rres"], R_FACTOR_BAR),
          truth["rres"] <= R_FACTOR_BAR, kill="K2")
    mandatory_controls_built = all(
        results[name]["model_deaths"] == 0
        for name in ("Epstein", "scramble"))
    check("S5.1 mandatory controls delivered per-shell censuses "
          "(no frame-death substitute)", mandatory_controls_built)

    section("S3 -- single-prime complete-tower comparison")
    prime_path, _prime_total = source_path(
        worlds["truth"], prime_count, prime_mode=True)
    prime_result = census("single-prime", models_by_world["truth"],
                          prime_path, z_grid)
    print_census(prime_result, len(z_grid))
    single_fails = prime_result["status_counts"]["NONPSD"] > 0
    check("S3.1 single-prime path FAIL/OSCILLATE: certified NONPSD "
          "points %d, sign changes %d"
          % (prime_result["status_counts"]["NONPSD"],
             prime_result["sign_changes"]), single_fails)

    section("S4 -- relation factorization census")
    total_truth_points = truth["nsteps"] * len(z_grid)
    print("    FORM 1 det(T)=1: SYMBOLICALLY YES locally and numerically "
          "max shell dev %.2e (world-blind IIKS relation)."
          % truth["detdev"])
    print("    FORM 2 T*JT=J-Delta, Delta=R*R: holds on %d/%d certified "
          "PSD shell points; rank census %s."
          % (truth["status_counts"]["PSD"], total_truth_points,
             truth["rank_counts"]))
    print("    FORM 3 discriminant certified zero-square: local IIKS "
          "factor YES (0^2); complete shell %d/%d points."
          % (truth["disc_zero"], total_truth_points))
    if truth["disc_zero"] < total_truth_points:
        print("      complete-shell result: NO-ZERO-SQUARE.  A general "
              "rational-square claim is UNRESOLVED, not inferred from "
              "sampled complex values.")
    check("S4.1 all three requested factor forms tested and typed", True)

    section("S6 -- tau screen (diagnostic only)")
    slope, screen = tau_screen(truth["rows"])
    print("    shell min-defect vs wall tau=1-lambda_max(D_P): slope %s "
          "-> %s (tau never enters T)"
          % ("%.3f" % slope if np.isfinite(slope) else "n/a", screen))
    check("S6.1 tau screen reported", True)

    true_nonpsd = truth["status_counts"]["NONPSD"] > 0
    true_all_shell = truth["step_all_psd"] == truth["nsteps"]
    aggregate_all = truth["prefix_nonpsd"] == 0
    epstein_breaks = results["Epstein"]["status_counts"]["NONPSD"] > 0
    scramble_breaks = results["scramble"]["status_counts"]["NONPSD"] > 0

    section("V -- verdict")
    if KILLS:
        verdict = ("PIPELINE-BROKEN" if KILLS[0] == "K1"
                   else "WARD-BROKEN")
    elif smoke:
        verdict = "SMOKE-ONLY / NO-FROZEN-VERDICT"
    elif true_nonpsd:
        verdict = "JCONTRACT-DEAD(TRUE-SHELL-NONPSD)"
    elif not single_fails:
        verdict = "JCONTRACT-DEAD(SINGLE-PRIME-ALSO-CONTRACTIVE)"
    elif not epstein_breaks:
        verdict = "JCONTRACT-DEAD(EPSTEIN-CONTROL-SILENT)"
    elif not scramble_breaks:
        verdict = "JCONTRACT-DEAD(SCRAMBLE-CONTROL-SILENT)"
    elif (true_all_shell and aggregate_all and epstein_breaks
          and scramble_breaks):
        verdict = "JCONTRACT-SIGNAL"
    else:
        verdict = "JCONTRACT-MIXED(UNRESOLVED-DEFECTS)"
    print("    THE VERDICT: %s" % verdict)
    print("    truth all-shell PSD %d/%d; aggregate NONPSD %d; "
          "single-prime NONPSD %d; Epstein/scramble NONPSD %d/%d"
          % (truth["step_all_psd"], truth["nsteps"],
             truth["prefix_nonpsd"],
             prime_result["status_counts"]["NONPSD"],
             results["Epstein"]["status_counts"]["NONPSD"],
             results["scramble"]["status_counts"]["NONPSD"]))
    print("    Smooth world (report-only): PSD/NONPSD/UNRESOLVED "
          "%d/%d/%d."
          % (results["smooth"]["status_counts"]["PSD"],
             results["smooth"]["status_counts"]["NONPSD"],
             results["smooth"]["status_counts"]["UNRESOLVED"]))
    print("    Scope: experiments/tfpt-discovery probe only; no "
          "verification/paper/ledger/website/manifest change; NO RH claim.")

    elapsed = time.time() - T0
    passed = sum(ok for _name, ok in CHECKS)
    print("\n[TIME] %.1f s / cap %.0f s  [CHECKS] %d run, %d failed"
          % (elapsed, RUNTIME_CAP, len(CHECKS), len(CHECKS) - passed))
    if not smoke:
        check("V.RUNTIME frozen run below 25 min", elapsed < RUNTIME_CAP)
    return 0 if all(ok for _name, ok in CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
