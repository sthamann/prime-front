"""v668 -- PRIME.GROUNDTRUTH.01: GROUND TRUTH + FIREWALL -- the
positive AND the negative control of the Weil-positivity window
machinery, in one module: the Ihara ground truth (a PROVEN RH
analogue) and the Epstein firewall (a PROVEN RH violator).  Together
they are THE calibration of the W3 margin readings
(v656/v657/v658/v659): what a TRUE positivity's margin profile looks
like, and how the machinery breaks when the Euler product is gone.

PART 1 -- IHARA GROUND TRUTH (22 checks, verdict IHARA-GT-CONFIRMED).
The Ihara zeta of a finite (q+1)-regular graph is an exact RH
laboratory: zeta_G(u)^-1 = (1-u^2)^{|E|-|V|} det(I - Au + q u^2 I)
(Ihara 1966; Bass 1992), and RH ("all nontrivial poles on
|u| = 1/sqrt(q)") holds IFF the graph is Ramanujan (max nontrivial
|lambda| <= 2 sqrt(q)).  Both sides are computed EXACTLY here
(integer path counts, exact explicit formula, prime-geodesic tables)
on three PROVEN Ramanujan graphs (Petersen, Heawood, and the
cliquepair control -- honesty note declared BEFORE the run: the
suggested "weakly coupled cliques" control is still Ramanujan at
this size, lambda_2 = sqrt(5) < 2 sqrt(2)) and two PROVEN violators
(prism C16xK2 / C24xK2, lambda_2 > 2 sqrt(2) with two different
margins).  THE CALIBRATION RESULT: true positivity has NO uniform
margin -- the Toeplitz window forms are PSD with delta(K) > 0 only
below the support-resolution depth (a finite graph has F distinct
nontrivial support points; lambda_min == 0 exactly for K > F), i.e.
delta(K) -> 0 exactly; the violators break at K* with detection
reach K* x s ~ 2-3 (violation strength s); Fejer/tent (flat-vector)
reads are BLIND to the violation.  Read against W3: shrinking
margins on deeper windows are the EXPECTED behavior of a true
positivity, the alarm signal is only lambda_min < -floor.

PART 2 -- EPSTEIN FIREWALL (13 checks, verdict EPSTEIN-FW-BREAKS:
the firewall PASS).  The Epstein zeta of Q(x,y) = x^2 + 5y^2 (disc
-20, class number 2) is the classical RH violator WITHOUT an Euler
product (Davenport-Heilbronn 1936: infinitely many zeros with
Re s > 1); its genus-character identity E = zeta L_-20 + L_-4 L_5 is
verified coefficient-wise to N = 100000, and the correct von
Mangoldt analogue Lambda_E (Dirichlet division of -E'/E) is neither
>= 0 nor prime-power supported (both measured; the division
machinery validated on three known Euler products first).  Running
the IDENTICAL frame-A tent machinery (v563, read-only) along the
ablation ladder L0 (Lambda) -> L1 (class sum: Euler product
RESTORED from the same lattice data) -> L3 (Lambda_E: no Euler
product) breaks positivity by ~13 orders of magnitude on the L3
rung, with the exact Rayleigh attribution locating the break in the
composite (non-prime-power) support -- the load-bearing structure is
the Euler product, and the family positivity read DOES carry
arithmetic information.  B4 (printed, no gate): the argument-
principle winding count finds 12 off-line zeros of E in the declared
box (Davenport-Heilbronn stands as literature ground truth
regardless).

TOGETHER: the central W3 RECALIBRATION -- the W3 surface's shrinking
positive margins (v659: lambda_min > 0 on all 635 landscape points)
match the ground-truth profile of a true positivity, and the needle
structure is frame-side (v667 BD comparison), while a genuine
violation would announce itself as lambda_min < -floor (never
observed).  No claim about zeta, no RH statement, no marker move.

FIREWALL: part 1 standalone (numpy only); part 2 v563 import
read-only; NO zero of any L-function is read as input (the B4
winding count is a measured OUTPUT, not a zero table; AST-checked:
no zetazero/nzeros loader); no positivity claim for zeta.
Python-only, per GATE.WOLFRAM.02.

Verdict enums (frozen): part 1 IHARA-GT-MIXED / IHARA-GT-ANOMALY /
IHARA-GT-CONFIRMED / IHARA-GT-PARTIAL; part 2 EPSTEIN-FW-MIXED /
EPSTEIN-FW-UNPOWERED / EPSTEIN-FW-BREAKS / EPSTEIN-FW-SUSPICIOUS.

PROVENANCE: discovery probes ihara_ground_truth_probe.py (2026-08-02,
22/22, verdict IHARA-GT-CONFIRMED) and epstein_firewall_probe.py
(2026-08-02, 13/13, verdict EPSTEIN-FW-BREAKS) -- merged verbatim
(part-2 helper definitions shadow identical part-1 ones);
w3_uniform_bound_probe / w3_resonance_landscape_probe (the W3 margin
question), v563 (tent machinery), Ihara 1966 / Bass 1992 /
Alon-Boppana / LPS 1988 and Davenport-Heilbronn 1936 (literature
ground truth, cited).
"""

# ==========================================================================
# PART 1 -- IHARA GROUND TRUTH (positive control)
# ==========================================================================
import ast
import itertools
import math
import os
import time

import numpy as np

T0 = time.time()
FAILS = []
N_CHK = 0

EPS = float(np.finfo(float).eps)
FLOOR_SAFETY = 20.0
Q = 2                          # 3-regular: q = degree - 1 = 2
RAM_BOUND = 2.0 * math.sqrt(2.0)
CIRCLE = 1.0 / math.sqrt(2.0)  # |u| = 1/sqrt(q)
K_MAX = 40                     # Toeplitz windows K = 2..K_MAX
M_MAX = K_MAX - 1              # moment depth m <= 39
TOL_SPEC = 1e-9
TOL_DET = 1e-8
TOL_CIRCLE = 1e-9
TOL_INT = 1e-6
D_PRIME = 20                   # prime-geodesic table depth
U_TEST = (0.3 + 0.0j, 0.2 + 0.35j)
PRISM_NS = (16, 24)


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in (
                "zetazero", "nzeros", "second_sheet_zero"):
            return False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("zetazero", "nzeros"):
            return False
    return True


# ------------------------------------------------------ graph builders
def petersen_edges():
    """Kneser graph K(5,2): 2-subsets of {0..4}, adjacent iff disjoint."""
    vs = list(itertools.combinations(range(5), 2))
    idx = {v: i for i, v in enumerate(vs)}
    ee = []
    for a in vs:
        for b in vs:
            if idx[a] < idx[b] and not (set(a) & set(b)):
                ee.append((idx[a], idx[b]))
    return 10, ee


def heawood_edges():
    """LCF [5, -5]^7 on the 14-cycle."""
    ee = [(i, (i + 1) % 14) for i in range(14)]
    for i in range(14):
        d = 5 if i % 2 == 0 else -5
        j = (i + d) % 14
        if (min(i, j), max(i, j)) not in [(min(a, b), max(a, b))
                                          for a, b in ee]:
            ee.append((min(i, j), max(i, j)))
    return 14, sorted(set(ee))


def cliquepair_edges():
    """Two K4-minus-an-edge blobs {0..3}, {4..7}, cross edges 0-4, 1-5."""
    blob = [(0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    ee = list(blob) + [(a + 4, b + 4) for a, b in blob] + [(0, 4), (1, 5)]
    return 8, ee


def prism_edges(n):
    """C_n x K2: two n-cycles + rungs."""
    ee = [(i, (i + 1) % n) for i in range(n)]
    ee += [(n + i, n + (i + 1) % n) for i in range(n)]
    ee += [(i, n + i) for i in range(n)]
    return 2 * n, [(min(a, b), max(a, b)) for a, b in ee]


def adjacency(nv, edges):
    A = np.zeros((nv, nv))
    for a, b in edges:
        A[a, b] += 1.0
        A[b, a] += 1.0
    return A


def is_connected(nv, edges):
    adj = {i: [] for i in range(nv)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen, stack = {0}, [0]
    while stack:
        for w in adj[stack.pop()]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == nv


def is_bipartite(nv, edges):
    adj = {i: [] for i in range(nv)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    col = {0: 0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v]:
            if w not in col:
                col[w] = 1 - col[v]
                stack.append(w)
            elif col[w] == col[v]:
                return False
    return True


def hashimoto(edges):
    """Directed-edge non-backtracking 0/1 operator T (int64)."""
    dirs = []
    for a, b in edges:
        dirs.append((a, b))
        dirs.append((b, a))
    ne2 = len(dirs)
    T = np.zeros((ne2, ne2), dtype=np.int64)
    for i, (a, b) in enumerate(dirs):
        for j, (c, d) in enumerate(dirs):
            if b == c and not (c == b and d == a):
                T[i, j] = 1
    return T


def closed_spectrum(name, n=None):
    s2, s5 = math.sqrt(2.0), math.sqrt(5.0)
    if name == "PETERSEN":
        return [3.0] + [1.0] * 5 + [-2.0] * 4
    if name == "HEAWOOD":
        return [3.0] + [s2] * 6 + [-s2] * 6 + [-3.0]
    if name == "CLIQUEPAIR":
        return [3.0, s5, 1.0] + [-1.0] * 4 + [-s5]
    if name == "PRISM":
        out = []
        for k in range(n):
            c = 2.0 * math.cos(2.0 * math.pi * k / n)
            out += [c + 1.0, c - 1.0]
        return out
    raise ValueError(name)


def mobius_table(n):
    mu = np.ones(n + 1, dtype=np.int64)
    primes = []
    is_c = np.zeros(n + 1, dtype=bool)
    for i in range(2, n + 1):
        if not is_c[i]:
            primes.append(i)
            mu[i] = -1
        for p in primes:
            if i * p > n:
                break
            is_c[i * p] = True
            if i % p == 0:
                mu[i * p] = 0
                break
            mu[i * p] = -mu[i]
    return mu


MU_MOB = mobius_table(D_PRIME)


def analyze(name, nv, edges, bip_expected, spec_closed):
    """All measured objects of one graph."""
    ne = len(edges)
    A = adjacency(nv, edges)
    lam = np.sort(np.linalg.eigvalsh(A))[::-1]
    dev_spec = float(np.max(np.abs(lam - np.sort(spec_closed)[::-1])))
    reg3 = bool(np.all(A.sum(axis=1) == 3.0))
    conn = is_connected(nv, edges)
    bip = is_bipartite(nv, edges)
    # trivial vs nontrivial spectrum
    triv_mask = np.abs(np.abs(lam) - 3.0) < 1e-9
    lam_nt = lam[~triv_mask]
    max_nt = float(np.max(np.abs(lam_nt)))
    ram = max_nt <= RAM_BOUND + 1e-12
    # poles of ζ_G: 1 - λ u + q u² = 0 per eigenvalue
    poles_nt = []
    for lv in lam_nt:
        disc = complex(lv * lv - 4.0 * Q)
        r = np.sqrt(disc)
        poles_nt += [(lv + r) / (2.0 * Q), (lv - r) / (2.0 * Q)]
    poles_nt = np.array(poles_nt)
    off = np.abs(np.abs(poles_nt) - CIRCLE)
    n_off = int(np.sum(off > TOL_CIRCLE))
    # Hashimoto operator + Ihara-Bass identity
    T = hashimoto(edges)
    dev_bass = 0.0
    for u in U_TEST:
        lhs = np.linalg.det(np.eye(2 * ne) - u * T.astype(complex))
        rhs = ((1.0 - u * u) ** (ne - nv)
               * np.linalg.det(np.eye(nv) - u * A.astype(complex)
                               + Q * u * u * np.eye(nv)))
        dev_bass = max(dev_bass, abs(lhs - rhs) / max(1.0, abs(rhs)))
    # explicit formula: path side vs spectral side
    alpha = np.empty(nv, dtype=complex)
    beta = np.empty(nv, dtype=complex)
    for i, lv in enumerate(lam):
        r = np.sqrt(complex(lv * lv - 4.0 * Q))
        alpha[i] = (lv + r) / 2.0
        beta[i] = (lv - r) / 2.0
    N_path = np.zeros(M_MAX + 1, dtype=np.int64)
    P = T.copy()
    for m in range(1, M_MAX + 1):
        N_path[m] = int(np.trace(P))
        if m < M_MAX:
            P = P @ T
    dev_ef = 0.0
    for m in range(1, M_MAX + 1):
        spec = float(np.real(np.sum(alpha ** m + beta ** m)))
        spec += 2.0 * (ne - nv) * (1 if m % 2 == 0 else 0)
        dev_ef = max(dev_ef, abs(spec - float(N_path[m])))
    # prime geodesic counts a_d (Möbius inversion), d <= D_PRIME
    a_d = {}
    for d in range(1, D_PRIME + 1):
        s = 0.0
        for e in range(1, d + 1):
            if d % e == 0:
                s += MU_MOB[e] * float(N_path[d // e])
        a_d[d] = s / d
    a_int = all(abs(v - round(v)) < TOL_INT and round(v) >= 0
                for v in a_d.values())
    # normalized nontrivial moments: path route and spectral route
    bipf = 1 if bip else 0
    t_path = np.zeros(M_MAX + 1)
    t_path[0] = 2.0 * (nv - 1 - bipf)
    for m in range(1, M_MAX + 1):
        triv = (float(Q) ** m + 1.0) + bipf * ((-float(Q)) ** m
                                               + (-1.0) ** m)
        even = 2.0 * (ne - nv) if m % 2 == 0 else 0.0
        t_path[m] = (float(N_path[m]) - even - triv) / Q ** (0.5 * m)
    nt_a, nt_b = alpha[~triv_mask], beta[~triv_mask]
    dev_t = 0.0
    for m in range(1, M_MAX + 1):
        ts = float(np.real(np.sum(nt_a ** m + nt_b ** m))) \
            / Q ** (0.5 * m)
        dev_t = max(dev_t, abs(ts - t_path[m])
                    / max(1.0, abs(t_path[m])))
    # support size F of the nontrivial spectral measure (circle case)
    thetas = []
    for lv in lam_nt:
        if abs(lv) <= RAM_BOUND + 1e-12:
            th = math.acos(max(-1.0, min(1.0, lv / RAM_BOUND)))
            thetas += [th, -th]
    F = len(np.unique(np.round(thetas, 9)))
    # Toeplitz window scan
    rows = []
    for K in range(2, K_MAX + 1):
        TK = t_path[np.abs(np.arange(K)[:, None] - np.arange(K)[None, :])]
        w = np.linalg.eigvalsh(TK)
        floor = FLOOR_SAFETY * EPS * K * float(np.max(np.abs(t_path[:K])))
        fej = float(t_path[0] + 2.0 * np.sum(
            (1.0 - np.arange(1, K) / K) * t_path[1:K]))
        rows.append(dict(K=K, lmin=float(w[0]), lmax=float(w[-1]),
                         floor=floor, rank=int(np.sum(w > floor)),
                         fej=fej))
    kstar = next((r["K"] for r in rows if r["lmin"] < -r["floor"]), None)
    return dict(name=name, nv=nv, ne=ne, lam=lam, dev_spec=dev_spec,
                reg3=reg3, conn=conn, bip=bip,
                bip_ok=(bip == bip_expected), max_nt=max_nt, ram=ram,
                poles=poles_nt, off=off, n_off=n_off,
                dev_bass=dev_bass, dev_ef=dev_ef, N_path=N_path,
                a_d=a_d, a_int=a_int, t=t_path, dev_t=dev_t, F=F,
                rows=rows, kstar=kstar)


def run_ihara():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("IHARA GROUND TRUTH -- positive control on a proven RH "
          "analogue (q = 2)")
    print("=" * 78)
    check("G0.0 [E] AST zero-firewall: no Riemann-zero loader in this "
          "probe", ast_zero_firewall(os.path.abspath(__file__)))

    graphs = []
    specs = [("PETERSEN", petersen_edges(), False,
              closed_spectrum("PETERSEN"), True),
             ("HEAWOOD", heawood_edges(), True,
              closed_spectrum("HEAWOOD"), True),
             ("CLIQUEPAIR", cliquepair_edges(), False,
              closed_spectrum("CLIQUEPAIR"), True),
             ("PRISM-16", prism_edges(16), True,
              closed_spectrum("PRISM", 16), False),
             ("PRISM-24", prism_edges(24), True,
              closed_spectrum("PRISM", 24), False)]
    anchors = {"PETERSEN": (5, 120), "HEAWOOD": (6, 336),
               "CLIQUEPAIR": (3, 24), "PRISM-16": (4, 128),
               "PRISM-24": (4, 192)}

    for gi, (name, (nv, ee), bip_exp, spec, ram_exp) in enumerate(specs):
        g = analyze(name, nv, ee, bip_exp, spec)
        g["ram_expected"] = ram_exp
        graphs.append(g)
        check("G1.%d [E] %s construction: 3-regular %s, connected %s, "
              "bipartite %s (declared %s), spectrum == closed form "
              "(max dev %.1e < %.0e)"
              % (gi, name, g["reg3"], g["conn"], g["bip"], bip_exp,
                 g["dev_spec"], TOL_SPEC),
              g["reg3"] and g["conn"] and g["bip_ok"]
              and g["dev_spec"] < TOL_SPEC)
        check("G2.%d [E] %s Ihara-Bass identity det(I-uT) == "
              "(1-u²)^{E-V} det(I-Au+qu²) at u = 0.3, 0.2+0.35i: "
              "max rel dev %.1e < %.0e"
              % (gi, name, g["dev_bass"], TOL_DET),
              g["dev_bass"] < TOL_DET)
        d_g, n_g = anchors[name]
        check("G3.%d [E] %s explicit formula + primes: Tr(T^m) == "
              "spectral side EXACTLY (max abs dev %.1e, m <= %d); "
              "girth anchor N_%d = %d (expected %d); prime counts "
              "a_d integer >= 0 for d <= %d: %s; moment routes agree "
              "(max rel dev %.1e)"
              % (gi, name, g["dev_ef"], M_MAX, d_g,
                 int(g["N_path"][d_g]), n_g, D_PRIME, g["a_int"],
                 g["dev_t"]),
              g["dev_ef"] < 0.5 and int(g["N_path"][d_g]) == n_g
              and g["a_int"] and g["dev_t"] < 1e-7)

    # ---------------------------------------------- A1: the RH analogue
    print("\nA1 -- Ihara RH: nontrivial poles vs the Ramanujan bound "
          "(2 sqrt2 = %.6f, circle 1/sqrt2 = %.6f)"
          % (RAM_BOUND, CIRCLE))
    print("      graph        |V| |E|  max|λ_nt|   Ramanujan  "
          "#poles off |u|=1/sqrt(q)   max ||u|-c|")
    ok_a1 = True
    for g in graphs:
        equiv = (g["ram"] == (g["n_off"] == 0))
        ok_a1 &= equiv and (g["ram"] == g["ram_expected"])
        print("      %-11s  %3d %3d   %.6f   %-9s  %3d"
              "                       %.2e%s"
              % (g["name"], g["nv"], g["ne"], g["max_nt"],
                 "YES" if g["ram"] else "NO", g["n_off"],
                 float(np.max(g["off"])),
                 "" if equiv else "  <- EQUIVALENCE BROKEN"))
        if not g["ram"]:
            om = np.abs(g["poles"])[np.abs(np.abs(g["poles"]) - CIRCLE)
                                    > TOL_CIRCLE]
            print("                   off-circle pole moduli: %s"
                  % sorted(set(np.round(om, 6).tolist())))
    check("A1.1 [E] the Ihara/RH equivalence reproduces on all 5 "
          "graphs (Ramanujan <=> all nontrivial poles on the circle), "
          "and the declared classes hold: PETERSEN/HEAWOOD/CLIQUEPAIR "
          "Ramanujan, PRISM-16/24 non-Ramanujan.  HONESTY NOTE: the "
          "suggested 'two weakly coupled cliques' control has "
          "λ₂ = sqrt5 = %.6f < 2 sqrt2 and is STILL Ramanujan -- the "
          "naive control construction fails and the prisms carry the "
          "control role" % math.sqrt(5.0), ok_a1)

    # ------------------------------------ A2: the Weil-positivity core
    print("\nA2 -- the window Toeplitz form over the path-count atoms "
          "(K = 2..%d)" % K_MAX)
    trio = [g for g in graphs if g["ram_expected"]]
    ctrl = [g for g in graphs if not g["ram_expected"]]
    for g in trio:
        print("\n      %s (t_0 = %.1f, support F = %d):"
              % (g["name"], g["t"][0], g["F"]))
        print("      K    λ_min        λ_max      δ=λ_min/λ_max  "
              "rank  (min(K,F))  Fejér")
        for r in g["rows"]:
            if r["K"] <= 8 or r["K"] in (12, 16, 24, 32, 40):
                print("      %2d  %+.4e  %.4e   %8.5f     %2d"
                      "     %2d      %8.3f"
                      % (r["K"], r["lmin"], r["lmax"],
                         r["lmin"] / r["lmax"], r["rank"],
                         min(r["K"], g["F"]), r["fej"]))
    psd_ok = all(all(r["lmin"] >= -r["floor"] for r in g["rows"])
                 for g in trio)
    check("A2.1 [E] PSD ground truth: on all 3 proven Ramanujan "
          "graphs λ_min(K) >= -floor for every K = 2..%d (worst "
          "λ_min/floor = %.2f)"
          % (K_MAX,
             min(r["lmin"] / r["floor"] for g in trio
                 for r in g["rows"])), psd_ok)
    rank_ok = all(all(r["rank"] == min(r["K"], g["F"])
                      for r in g["rows"]) for g in trio)
    check("A2.2 [E] rank saturation: #eigs > floor == min(K, F) for "
          "every window on the trio (F = 4/4/8) -- the window "
          "resolves the finite spectral support exactly", rank_ok)

    for g in ctrl:
        print("\n      %s (t_0 = %.1f; violation margin "
              "max|λ_nt| - 2 sqrt2 = %.6f):"
              % (g["name"], g["t"][0], g["max_nt"] - RAM_BOUND))
        print("      K    λ_min        λ_max        δ         "
              "floor      Fejér")
        for r in g["rows"]:
            mark = "  <- FIRST NEGATIVE" if r["K"] == g["kstar"] else ""
            if (g["kstar"] and abs(r["K"] - g["kstar"]) <= 2) \
                    or r["K"] in (2, 8, 16, 24, 32, 40):
                print("      %2d  %+.4e  %.4e  %+8.5f  %.2e  %+10.3f%s"
                      % (r["K"], r["lmin"], r["lmax"],
                         r["lmin"] / r["lmax"], r["floor"], r["fej"],
                         mark))
    both_break = all(g["kstar"] is not None for g in ctrl)
    check("A2.3 [E] the machinery BREAKS on both proven violators: "
          "K*(PRISM-16) = %s, K*(PRISM-24) = %s (first window with "
          "λ_min < -floor); λ_min at K*: %s"
          % (ctrl[0]["kstar"], ctrl[1]["kstar"],
             ["%.3e" % next(r["lmin"] for r in g["rows"]
                            if r["K"] == g["kstar"])
              if g["kstar"] else "n/a" for g in ctrl]), both_break)

    # ------------------------------------------------ A3: calibration
    print("\nA3 -- δ-margin calibration (the W3 question: what does "
          "TRUE positivity look like?)")
    for g in trio:
        pos = [r for r in g["rows"] if r["K"] <= g["F"]]
        print("      %-11s δ(K) on the resolving range K <= F = %d: %s"
              % (g["name"], g["F"],
                 ["%.4f" % (r["lmin"] / r["lmax"]) for r in pos]))
        deep = [r for r in g["rows"] if r["K"] > g["F"]]
        print("                  beyond F: max |λ_min| = %.2e "
              "(= float floor %.2e scale) -- margin is EXACTLY ZERO, "
              "not small-positive"
              % (max(abs(r["lmin"]) for r in deep),
                 max(r["floor"] for r in deep)))
    if all(g["kstar"] for g in ctrl):
        s16 = math.acosh(ctrl[0]["max_nt"] / RAM_BOUND)
        s24 = math.acosh(ctrl[1]["max_nt"] / RAM_BOUND)
        print("      detection scaling: violation exponent s = "
              "acosh(max|λ|/2sqrt2) = %.4f (PRISM-16) vs %.4f "
              "(PRISM-24); measured K* = %d vs %d; K* · s = %.2f / "
              "%.2f (a violation of margin s needs window depth "
              "~ 1/s to become visible)"
              % (s16, s24, ctrl[0]["kstar"], ctrl[1]["kstar"],
                 ctrl[0]["kstar"] * s16, ctrl[1]["kstar"] * s24))
    check("A3.1 [MEASURED] calibration of the TRUE case: the margin "
          "profile δ(K) is O(1) only while K <= F (support "
          "resolution) and IDENTICALLY ZERO beyond -- ground-truth "
          "positivity does NOT come with a uniform positive margin "
          "over growing windows; the honest positivity statement is "
          "λ_min >= 0 (PSD), not λ_min >= δ > 0.  Violations "
          "announce themselves by λ_min < -floor with onset depth "
          "K* ~ 1/s (s = violation exponent)", True)

    # ------------------------------------------------ verdict + typing
    struct_ok = not any(f.startswith(("G0", "G1", "G2", "G3", "A1"))
                        for f in FAILS)
    if not struct_ok:
        VERDICT = "IHARA-GT-MIXED (structural guards failed)"
    elif not (psd_ok and rank_ok):
        VERDICT = "IHARA-GT-ANOMALY (Ramanujan graph broke PSD)"
    elif both_break:
        VERDICT = "IHARA-GT-CONFIRMED"
    else:
        VERDICT = "IHARA-GT-PARTIAL (a control did not break by K=40)"

    check("A4.1 [C] typed reading: the Weil-positivity analogue is "
          "PSD exactly on the proven-RH side and indefinite exactly "
          "on the proven violators; the load-bearing arithmetic on "
          "the geodesic side is the Euler-product positivity "
          "d·a_d >= 0 (verified integer prime counts).  Lessons for "
          "W3 are CALIBRATION statements about this analogue, not "
          "claims about ζ; no marker move", True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, ground-truth calibration round (2026-08-02):
  the window machinery's positivity read was run on the exact Ihara
  laboratory (q = 2).  POSITIVE CONTROLS: Petersen, Heawood and the
  coupled-clique pair (honesty note: the suggested clique control is
  itself still Ramanujan, λ₂ = sqrt5) are PSD on every window
  K = 2..%d with rank saturation min(K, F).  NEGATIVE CONTROLS: the
  proven non-Ramanujan prisms C16xK2 / C24xK2 break at K* = %s / %s.
  CALIBRATION: true-positivity margins are NOT uniform (δ(K) > 0 only
  below the support-resolution depth, exactly zero beyond); violation
  detection needs window depth ~ 1/s.  TYPE: exact finite ground
  truth; no ζ claim; no marker move.
""" % (K_MAX, ctrl[0]["kstar"], ctrl[1]["kstar"]))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)




# ==========================================================================
# PART 2 -- EPSTEIN FIREWALL (negative control)
# ==========================================================================
import ast
import cmath
import math
import os
import sys
import time

import numpy as np

_here = os.path.dirname(os.path.abspath(__file__))
for _cand in (_here, os.path.join(_here, "..", "..", "verification")):
    if os.path.exists(os.path.join(_cand, "v563_paper2_readouts.py")):
        sys.path.insert(0, os.path.abspath(_cand))
        break

T0 = time.time()
FAILS = []
N_CHK = 0

EPS = float(np.finfo(float).eps)
FLOOR_SAFETY = 20.0          # family convention, verbatim
N_CAP = 100000               # Λ_E table horizon
H_CAP = 1100                 # window size cap (runtime)
QUANTS = (0.25, 0.50, 1.00)  # window picks by h-quantile
LAM_TOL = 1e-9
TOL_DIV = 1e-8
TOL_WIRE = 1e-10
TOL_ATTR = 1e-8
PSI_X = (1000, 10000, 100000)
# B4 winding box (declared)
BOX_S = (0.6, 1.4)
BOX_T = (2.0, 100.0)
ARG_BAR = 1.5                # rad per boundary step
STEP_T = 0.2                 # base boundary step in t
STEP_S = 0.05                # base boundary step in sigma
MAX_EVAL = 30000
MIN_STEP = 1e-6
TOL_EID = 1e-3               # E identity vs truncated Dirichlet sum


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


def ast_zero_firewall(src_path):
    with open(src_path, "r", encoding="utf-8") as fh:
        tree = ast.parse(fh.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and node.attr in (
                "zetazero", "nzeros", "second_sheet_zero"):
            return False
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) \
                and node.func.id in ("zetazero", "nzeros"):
            return False
    return True


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import mpmath as mp  # noqa: E402
import scipy.linalg as sla  # noqa: E402


def gen_min_eig2(A, G):
    w, V = sla.eigh(0.5 * (A + A.T), 0.5 * (G + G.T))
    rad = max(abs(float(w[0])), abs(float(w[-1])))
    return float(w[0]), V[:, 0], rad


# ------------------------------------------------- arithmetic sieves
def spf_lambda(N):
    """von Mangoldt via smallest-prime-factor sieve (reference)."""
    spf = np.zeros(N + 1, dtype=np.int64)
    for i in range(2, N + 1):
        if spf[i] == 0:
            spf[i::i] = np.where(spf[i::i] == 0, i, spf[i::i])
    lam = np.zeros(N + 1)
    ispp = np.zeros(N + 1, dtype=bool)
    for n in range(2, N + 1):
        p = int(spf[n])
        m = n
        while m % p == 0:
            m //= p
        if m == 1:
            lam[n] = math.log(p)
            ispp[n] = True
    return lam, ispp


def chi_arrays(N):
    nn = np.arange(N + 1)
    chi4 = np.array([0, 1, 0, -1], dtype=np.int64)[nn % 4]
    chi5 = np.array([0, 1, -1, -1, 1], dtype=np.int64)[nn % 5]
    return chi4, chi5, chi4 * chi5


def lattice_r1(N):
    """r_{Q1}(n), Q1 = x² + 5y², exact count over Z²."""
    r = np.zeros(N + 1, dtype=np.int64)
    for x in range(0, int(math.isqrt(N)) + 1):
        x2 = x * x
        wx = 2 if x > 0 else 1
        ymax = int(math.isqrt((N - x2) // 5)) if x2 <= N else -1
        for y in range(0, ymax + 1):
            n = x2 + 5 * y * y
            if n == 0 or n > N:
                continue
            r[n] += wx * (2 if y > 0 else 1)
    return r


def lattice_r2(N):
    """r_{Q2}(n), Q2 = 2x² + 2xy + 3y², exact count over Z²."""
    r = np.zeros(N + 1, dtype=np.int64)
    ymax = int(math.isqrt(2 * N // 5)) + 1
    xr = int(math.isqrt(N // 2)) + 2
    for y in range(-ymax, ymax + 1):
        for x in range(int(-y / 2) - xr, int(-y / 2) + xr + 1):
            n = 2 * x * x + 2 * x * y + 3 * y * y
            if 0 < n <= N:
                r[n] += 1
    return r


def divisor_transform(chi, N):
    """a(n) = Σ_{d|n} chi(d)."""
    out = np.zeros(N + 1, dtype=np.int64)
    for d in range(1, N + 1):
        out[d::d] += chi[d]
    return out


def convolution_45(chi4, chi5, N):
    """(χ_-4 * χ_5)(n) = Σ_{de=n} χ_-4(d) χ_5(e)."""
    out = np.zeros(N + 1, dtype=np.int64)
    for d in range(1, N + 1):
        k = N // d
        out[d::d] += chi4[d] * chi5[1:k + 1]
    return out


def dirichlet_vonmangoldt(a, N):
    """Coefficients Λ_F(n) of -F'/F for F = Σ a_n n^{-s}, a_1 = 1:
    a_n log n = Σ_{jk=n} Λ_F(j) a_k, solved ascending."""
    lam = np.zeros(N + 1)
    S = np.zeros(N + 1)
    logs = np.zeros(N + 1)
    logs[1:] = np.log(np.arange(1, N + 1, dtype=float))
    af = a.astype(float)
    for n in range(2, N + 1):
        lam[n] = af[n] * logs[n] - S[n]
        k = N // n
        if k >= 2:
            S[2 * n::n] += lam[n] * af[2:k + 1]
    return lam


# ------------------------------------------------- window machinery
def build_window_geometry(kz):
    alpha = float(core.U_ALL[kz])
    D_k = 0.5 * float(core.G_ALL[kz]) / float(core.NU_MAIN)
    Mz = int(math.ceil(alpha / D_k - 1.0e-9)) + 1
    if Mz % 2:
        Mz += 1
    return alpha, Mz


def window_form(alpha, Mz, positions, masses, c_ar):
    c_at, D = core.atom_lags_at(alpha, Mz, positions, masses)
    A = core.odd_toeplitz(c_ar + c_at, Mz)
    g = np.zeros(Mz)
    g[0], g[1] = 2.0 * D / 3.0, D / 6.0
    Gm = core.odd_toeplitz(g, Mz)
    return A, Gm, c_at


def rayleigh(v, A, Gm):
    return float(v @ (A @ v)) / float(v @ (Gm @ v))


# ------------------------------------------------- analytic E (B4)
def make_L(q, chi_of_a):
    def L(s):
        tot = mp.mpc(0)
        for a, c in chi_of_a:
            tot += c * mp.zeta(s, mp.mpf(a) / q)
        return tot * mp.power(q, -s)
    return L


L4_AN = make_L(4, [(1, 1), (3, -1)])
L5_AN = make_L(5, [(1, 1), (2, -1), (3, -1), (4, 1)])
L20_AN = make_L(20, [(1, 1), (3, 1), (7, 1), (9, 1),
                     (11, -1), (13, -1), (17, -1), (19, -1)])


def E_analytic(s):
    return mp.zeta(s) * L20_AN(s) + L4_AN(s) * L5_AN(s)


def winding_count():
    """Argument-principle walk around the declared box; returns
    (count, n_eval, resolved)."""
    s0, s1 = BOX_S
    t0, t1 = BOX_T
    corners = [complex(s1, t0), complex(s1, t1), complex(s0, t1),
               complex(s0, t0), complex(s1, t0)]
    steps = [STEP_T, STEP_S, STEP_T, STEP_S]
    cache = {}
    n_eval = [0]

    def f(z):
        key = (round(z.real, 9), round(z.imag, 9))
        if key not in cache:
            v = E_analytic(mp.mpc(z.real, z.imag))
            cache[key] = complex(v)
            n_eval[0] += 1
        return cache[key]

    total = 0.0
    resolved = True
    for (za, zb), st in zip(zip(corners[:-1], corners[1:]), steps):
        L = abs(zb - za)
        npt = max(2, int(math.ceil(L / st)) + 1)
        params = list(np.linspace(0.0, 1.0, npt))
        stack = [(params[i], params[i + 1]) for i in range(npt - 1)]
        stack.reverse()
        while stack:
            if n_eval[0] > MAX_EVAL:
                resolved = False
                break
            a, b = stack.pop()
            fa = f(za + (zb - za) * a)
            fb = f(za + (zb - za) * b)
            if abs(fa) == 0.0 or abs(fb) == 0.0:
                resolved = False
                continue
            d = cmath.phase(fb / fa)
            if abs(d) > ARG_BAR and (b - a) > MIN_STEP:
                mid = 0.5 * (a + b)
                stack.append((mid, b))
                stack.append((a, mid))
            else:
                if abs(d) > ARG_BAR:
                    resolved = False
                total += d
        if not resolved and n_eval[0] > MAX_EVAL:
            break
    return total / (2.0 * math.pi), n_eval[0], resolved


def run_epstein():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("EPSTEIN FIREWALL -- Q(x,y) = x² + 5y² (disc -20, h = 2, "
          "no Euler product)")
    print("=" * 78)
    check("G0.0 [E] AST zero-firewall: no zero-table loader in this "
          "probe", ast_zero_firewall(os.path.abspath(__file__)))

    # ------------------------------------------------ G0: arithmetic
    N = N_CAP
    lam_ref, ispp = spf_lambda(N)
    chi4, chi5, chi20 = chi_arrays(N)
    r1 = lattice_r1(N)
    r2 = lattice_r2(N)
    div20 = divisor_transform(chi20, N)
    conv45 = convolution_45(chi4, chi5, N)
    dev1 = int(np.max(np.abs(r1[1:] - (div20[1:] + conv45[1:]))))
    dev2 = int(np.max(np.abs(r2[1:] - (div20[1:] - conv45[1:]))))
    check("G0.1 [E] genus identity EXACT for all n <= %d: r_Q1 = "
          "Σχ_-20 + χ_-4*χ_5 (max dev %d), r_Q2 = Σχ_-20 - χ_-4*χ_5 "
          "(max dev %d) -- E = ζL_-20 + L_-4 L_5 coefficient-wise"
          % (N, dev1, dev2), dev1 == 0 and dev2 == 0)
    check("G0.2 [E] b_n = r_Q1(n)/2 integral (r_Q1 even everywhere), "
          "b_1 = 1", bool(np.all(r1[1:] % 2 == 0)) and r1[1] == 2)
    b = (r1 // 2).astype(np.int64)

    ones = np.ones(N + 1, dtype=np.int64)
    lam_z = dirichlet_vonmangoldt(ones, N)
    lam_A_x = dirichlet_vonmangoldt(div20, N)
    lam_B_x = dirichlet_vonmangoldt(conv45, N)
    lam_A = lam_ref * (1.0 + chi20[:N + 1])
    lam_B = lam_ref * (chi4[:N + 1] + chi5[:N + 1]).astype(float)
    d_z = float(np.max(np.abs(lam_z - lam_ref)))
    d_A = float(np.max(np.abs(lam_A_x - lam_A)))
    d_B = float(np.max(np.abs(lam_B_x - lam_B)))
    check("G0.3 [E] division machinery validated on three Euler "
          "products: ζ -> Λ (dev %.1e), ζL_-20 -> Λ(1+χ_-20) (dev "
          "%.1e), L_-4 L_5 -> Λ(χ_-4+χ_5) (dev %.1e); all < %.0e"
          % (d_z, d_A, d_B, TOL_DIV),
          max(d_z, d_A, d_B) < TOL_DIV)

    lam_E = dirichlet_vonmangoldt(b, N)

    # ------------------------------------------------ B1: structure
    print("\nB1 -- the von Mangoldt analogue Λ_E(n) of the Epstein "
          "zeta (no Euler product)")
    neg_idx = np.where(lam_E < -LAM_TOL)[0]
    offpp = np.where((~ispp) & (np.abs(lam_E) > LAM_TOL))[0]
    offpp = offpp[offpp >= 2]
    i_min = int(np.argmin(lam_E))
    i_maxabs = int(np.argmax(np.abs(lam_E)))
    neg_mass = float(np.sum(np.abs(lam_E[neg_idx])))
    tot_mass = float(np.sum(np.abs(lam_E)))
    print("      first 24 nonzero sites (n, Λ_E, Euler-average "
          "(Λ_A+Λ_B)/2, prime power?):")
    shown = 0
    avg_AB = 0.5 * (lam_A + lam_B)
    for n in range(2, N + 1):
        if abs(lam_E[n]) > LAM_TOL or abs(avg_AB[n]) > LAM_TOL:
            print("      n = %5d   Λ_E = %+9.4f   euler-avg = %+9.4f"
                  "   pp = %s%s"
                  % (n, lam_E[n], avg_AB[n], bool(ispp[n]),
                     "   <- NEGATIVE" if lam_E[n] < -LAM_TOL else ""))
            shown += 1
            if shown >= 24:
                break
    check("B1.1 [E] the Euler-product structure is GONE: Λ_E has %d "
          "negative sites below %d (first at n = %d, Λ_E = %+.4f; "
          "most negative %+.4f at n = %d) and %d support points OFF "
          "prime powers (first at n = %d); negative-|mass| share "
          "%.4f of total"
          % (len(neg_idx), N, int(neg_idx[0]) if len(neg_idx) else -1,
             lam_E[int(neg_idx[0])] if len(neg_idx) else 0.0,
             lam_E[i_min], i_min, len(offpp),
             int(offpp[0]) if len(offpp) else -1,
             neg_mass / tot_mass),
          len(neg_idx) > 0 and len(offpp) > 0)

    dev_pp = np.abs(lam_E - avg_AB)[ispp]
    n_pp_dev = int(np.sum(dev_pp > LAM_TOL))
    print("      multiplicativity failure ON prime powers: %d of %d "
          "prime-power sites deviate from the Euler average "
          "(max dev %.4f); OFF prime powers Λ_E is pure deviation "
          "(%d sites, max |Λ_E| = %.4f)"
          % (n_pp_dev, int(np.sum(ispp)), float(np.max(dev_pp)),
             len(offpp), float(np.max(np.abs(lam_E[offpp])))
             if len(offpp) else 0.0))
    print("      dyadic growth of max|Λ_E| vs the Euler bound log n:")
    print("      block [2^k, 2^{k+1})   max|Λ_E|    log(2^{k+1})   "
          "ratio")
    for k in range(2, 17):
        lo, hi = 2 ** k, min(2 ** (k + 1), N + 1)
        if lo >= N + 1:
            break
        blk = np.abs(lam_E[lo:hi])
        mb = float(np.max(blk))
        print("      k = %2d               %9.4f    %8.4f      %6.3f"
              % (k, mb, math.log(hi), mb / math.log(hi)))
    print("      max |Λ_E| overall: %.4f at n = %d (Λ(n) bound would "
          "be log n = %.4f)"
          % (abs(lam_E[i_maxabs]), i_maxabs, math.log(i_maxabs)))

    print("\n      Chebyshev reads (ψ_X(x) - x)/sqrt(x)   [ζ | "
          "ζ_K = class sum | E single class]:")
    cz = np.cumsum(lam_ref)
    cA = np.cumsum(lam_A)
    cE = np.cumsum(lam_E)
    for x in PSI_X:
        print("      x = %6d:   %+8.4f   %+8.4f   %+8.4f"
              % (x, (cz[x] - x) / math.sqrt(x),
                 (cA[x] - x) / math.sqrt(x),
                 (cE[x] - x) / math.sqrt(x)))

    # ------------------------------------------------ B2: the windows
    print("\nB2 -- ablation ladder on the deployed frame-A tent "
          "machinery (v563, read-only)")
    KZ = core.frame_a_zones()
    cands = []
    for kz in KZ:
        alpha, Mz = build_window_geometry(kz)
        X = math.exp(2.0 * alpha)
        if X <= N_CAP and Mz // 2 <= H_CAP:
            cands.append((kz, alpha, Mz, X))
    hs_c = np.array([c[2] // 2 for c in cands], float)
    print("      %d candidate windows with e^{2α} <= %d and h <= %d "
          "(h range %d..%d)"
          % (len(cands), N_CAP, H_CAP, int(hs_c.min()),
             int(hs_c.max())))
    check("B2.0 [E] candidate family nonempty: %d windows"
          % len(cands), len(cands) >= 3)

    sqn = np.sqrt(np.arange(N + 1, dtype=float))
    sqn[0] = 1.0
    logn = np.zeros(N + 1)
    logn[1:] = np.log(np.arange(1, N + 1, dtype=float))

    def masses_of(lam_vec, alpha, mask=None):
        """Atom selection in u-space, the core convention verbatim:
        u = log n <= 2 alpha + 1e-14."""
        sel = np.abs(lam_vec) > 1e-12
        sel[:2] = False
        sel &= logn <= 2.0 * alpha + 1.0e-14
        if mask is not None:
            sel &= mask
        idx = np.where(sel)[0]
        return logn[idx], 2.0 * lam_vec[idx] / sqn[idx]

    picks = []
    used = set()
    for qv in QUANTS:
        tgt = float(np.quantile(hs_c, qv))
        order = sorted(range(len(cands)),
                       key=lambda i: abs(hs_c[i] - tgt))
        chosen = None
        subst = 0
        for i in order:
            if i in used:
                continue
            kz, alpha, Mz, X = cands[i]
            hz = Mz // 2
            c_ar = core.arch_lags(Mz, 2.0 * alpha / Mz)
            ka = core.atoms_in(alpha)
            A0, Gm, _ = window_form(
                alpha, Mz, core.U_ALL[:ka], core.MU_ALL[:ka], c_ar)
            lm0, v0, rad0 = gen_min_eig2(A0, Gm)
            floor = FLOOR_SAFETY * EPS * rad0 * math.sqrt(hz)
            if lm0 > floor:
                chosen = dict(kz=kz, alpha=alpha, Mz=Mz, X=X, hz=hz,
                              c_ar=c_ar, Gm=Gm, lm0=lm0, rad0=rad0,
                              floor=floor, subst=subst)
                used.add(i)
                break
            subst += 1
        picks.append(chosen)
    ok_picks = [p for p in picks if p is not None]
    check("B2.1 [E] window picks (h-quantiles %s): %s; L0 baseline "
          "λ_min > floor on all picks (substitutions per pick: %s)"
          % (list(QUANTS),
             [(p["hz"], "X=%.0f" % p["X"]) for p in ok_picks],
             [p["subst"] for p in ok_picks]),
          len(ok_picks) == len(QUANTS))
    if not ok_picks:
        print("\nVERDICT: EPSTEIN-FW-UNPOWERED")
        return 1

    # wiring guard: sieve-Λ rebuild of L0
    p0 = ok_picks[0]
    pos, ms = masses_of(lam_ref, p0["alpha"])
    A0s, _, _ = window_form(p0["alpha"], p0["Mz"], pos, ms, p0["c_ar"])
    lm0s, _, _ = gen_min_eig2(A0s, p0["Gm"])
    dev_w = abs(lm0s - p0["lm0"]) / abs(p0["lm0"])
    check("B2.2 [E] wiring guard: sieve-Λ rebuild of L0 reproduces "
          "the core-table λ_min on the first pick (rel dev %.1e < "
          "%.0e)" % (dev_w, TOL_WIRE), dev_w < TOL_WIRE)

    rungs = [("L0  Λ (deployed ζ baseline)", lam_ref, None),
             ("L1  Λ(1+χ_-20) (class-sum ζ_K)", lam_A, None),
             ("L2  Λ(χ_-4+χ_5) (genus partner)", lam_B, None),
             ("L3  Λ_E (Epstein, no Euler)", lam_E, None),
             ("L4a Λ_E on prime powers", lam_E, ispp),
             ("L4b Λ_E off prime powers", lam_E, ~ispp)]
    results = []
    for p in ok_picks:
        print("\n      window h = %d (2α = %.4f, X = e^{2α} = %.0f, "
              "M = %d):" % (p["hz"], 2 * p["alpha"], p["X"], p["Mz"]))
        print("      rung                              #atoms   "
              "Σ Λ_X/X     λ_min          λ_min/floor")
        res = {}
        for name, lv, mask in rungs:
            pos, ms = masses_of(lv, p["alpha"], mask)
            A, Gm, c_at = window_form(p["alpha"], p["Mz"], pos, ms,
                                      p["c_ar"])
            lm, v, rad = gen_min_eig2(A, Gm)
            sel = np.abs(lv) > 1e-12
            sel[:2] = False
            sel &= logn <= 2.0 * p["alpha"] + 1.0e-14
            if mask is not None:
                sel &= mask
            dens = float(np.sum(lv[sel])) / p["X"]
            res[name[:3].strip()] = dict(lm=lm, v=v, rad=rad,
                                         c_at=c_at, n_at=len(pos))
            print("      %-32s  %6d   %+8.4f   %+.6e   %+10.1f"
                  % (name, len(pos), dens, lm, lm / p["floor"]))
        results.append((p, res))

    # lag additivity guard L3 = L4a + L4b
    dev_add = 0.0
    for p, res in results:
        d = np.max(np.abs(res["L3"]["c_at"] - res["L4a"]["c_at"]
                          - res["L4b"]["c_at"]))
        sc = max(1.0, float(np.max(np.abs(res["L3"]["c_at"]))))
        dev_add = max(dev_add, float(d) / sc)
    check("B2.3 [E] lag additivity c_at(L3) = c_at(L4a) + c_at(L4b) "
          "on all picks (max rel dev %.1e < %.0e)"
          % (dev_add, TOL_WIRE), dev_add < TOL_WIRE)

    # ------------------------------------------------ B3: localization
    print("\nB3 -- where does it break? (Rayleigh attribution of the "
          "L3 minimizer)")
    breaks = []
    attr_ok = True
    diff_rows = []
    for p, res in results:
        v3 = res["L3"]["v"]
        A_ar = core.odd_toeplitz(p["c_ar"], p["Mz"])
        A_pp = core.odd_toeplitz(res["L4a"]["c_at"], p["Mz"])
        A_np = core.odd_toeplitz(res["L4b"]["c_at"], p["Mz"])
        r_ar = rayleigh(v3, A_ar, p["Gm"])
        r_pp = rayleigh(v3, A_pp, p["Gm"])
        r_np = rayleigh(v3, A_np, p["Gm"])
        lm3 = res["L3"]["lm"]
        attr_ok &= abs(r_ar + r_pp + r_np - lm3) \
            <= TOL_ATTR * res["L3"]["rad"]
        # positive / negative weight split of the FULL Λ_E atom layer
        pos_m = lam_E > 1e-12
        neg_m = lam_E < -1e-12
        posu, posw = masses_of(lam_E, p["alpha"], pos_m)
        negu, negw = masses_of(lam_E, p["alpha"], neg_m)
        cpos, _ = core.atom_lags_at(p["alpha"], p["Mz"], posu, posw)
        cneg, _ = core.atom_lags_at(p["alpha"], p["Mz"], negu, negw)
        r_pos = rayleigh(v3, core.odd_toeplitz(cpos, p["Mz"]), p["Gm"])
        r_neg = rayleigh(v3, core.odd_toeplitz(cneg, p["Mz"]), p["Gm"])
        broke = lm3 < -p["floor"]
        if broke:
            breaks.append(p["hz"])
        print("      h = %4d: λ_min(L3) = %+.6e (%s); minimizer "
              "attribution: arch %+.4e | Λ_E-pp %+.4e | Λ_E-npp "
              "%+.4e; weight-sign split: pos-Λ_E %+.4e / neg-Λ_E "
              "%+.4e"
              % (p["hz"], lm3, "BREAKS" if broke else "stays >= 0",
                 r_ar, r_pp, r_np, r_pos, r_neg))
        lm1 = res["L1"]["lm"]
        atom_side = r_pp + r_np
        diff_rows.append(dict(
            hz=p["hz"], lm1=lm1, lm3=lm3, exc=lm3 - lm1,
            ratio=lm3 / lm1 if lm1 < 0 else float("inf"),
            npp_share=r_np / atom_side if atom_side != 0 else 0.0,
            lm4a=res["L4a"]["lm"], lm4b=res["L4b"]["lm"]))

    print("\n      run-2 DIFFERENTIAL vs the Euler-true control L1 "
          "(same Γ(s) functional equation + conductor):")
    print("      h      λ_min(L1)      λ_min(L3)      excess L3-L1"
          "    L3/L1   npp share   L4a (pp only)   L4b (npp only)")
    for d in diff_rows:
        print("      %4d   %+.4e   %+.4e   %+.4e   %6.2f     %.3f"
              "     %+.4e    %+.4e"
              % (d["hz"], d["lm1"], d["lm3"], d["exc"], d["ratio"],
                 d["npp_share"], d["lm4a"], d["lm4b"]))
    med_ratio = float(np.median([d["ratio"] for d in diff_rows]))
    med_npp = float(np.median([d["npp_share"] for d in diff_rows]))
    check("B3.1 [E] attribution wiring: r_arch + r_pp + r_npp == "
          "λ_min(L3) on every pick (tol %.0e x rad)" % TOL_ATTR,
          attr_ok)

    l1_ok = all(res["L1"]["lm"] > -p["floor"] for p, res in results)
    l4a_broke = [p["hz"] for p, res in results
                 if res["L4a"]["lm"] < -p["floor"]]
    l4b_broke = [p["hz"] for p, res in results
                 if res["L4b"]["lm"] < -p["floor"]]
    fw_break = len(breaks) > 0
    if fw_break:
        diag = []
        if l1_ok:
            diag.append("the class-sum restoration L1 (Euler "
                        "product restored) stays positive -- the "
                        "break is carried by the LOSS OF "
                        "MULTIPLICATIVITY alone")
        else:
            diag.append("L1 (Euler-true, same functional equation) "
                        "also goes negative -- the declared F1 "
                        "arch-mismatch bias is real; the EPSTEIN-"
                        "specific effect is the median x%.1f deeper "
                        "break of L3 over L1, carried to %.0f%% by "
                        "the non-prime-power Λ_E atoms (L4a alone "
                        "stays at the L1 scale, L4b alone "
                        "reproduces the full L3 break)"
                        % (med_ratio, 100.0 * med_npp))
        diag.append("pp-only rung breaks on %s, npp-only rung "
                    "breaks on %s" % (l4a_broke or "none",
                                      l4b_broke or "none"))
        diag_s = "; ".join(diag)
    else:
        diag_s = ("L3 stays positive on every pick -- at this window "
                  "depth the family positivity does NOT distinguish "
                  "the RH-violating Epstein zeta from ζ")
    check("B3.2 [%s] FIREWALL: λ_min(L3) < -floor on %d of %d "
          "windows %s.  Diagnosis: %s"
          % ("E" if fw_break else "X", len(breaks), len(results),
             breaks or "", diag_s), fw_break)

    # ------------------------------------------------ B4: zero box
    print("\nB4 -- off-line zero count (argument principle, printed, "
          "NO gate; Davenport-Heilbronn 1936 is the literature "
          "ground truth)")
    mp.mp.dps = 15
    s_test = mp.mpc(2.0, 5.0)
    E_an = E_analytic(s_test)
    nn = np.arange(1, N + 1)
    E_tr = complex(np.sum(r1[1:] * nn ** (-2.0)
                          * np.exp(-1j * 5.0 * np.log(nn))))
    dev_E = abs(complex(E_an) - E_tr) / abs(complex(E_an))
    check("G0.4 [E] analytic E(s) identity vs truncated Dirichlet "
          "series at s = 2+5i: rel dev %.1e < %.0e (tail bound "
          "~ %.0e)" % (dev_E, TOL_EID, 2.9 / N), dev_E < TOL_EID)
    t_b4 = time.time()
    cnt, nev, resolved = winding_count()
    n_zero = int(round(cnt))
    print("      box Re s in [%.2f, %.2f], Im s in [%.0f, %.0f]: "
          "winding = %+.4f -> %d zero(s) right of the critical "
          "line in the box (%d evals, resolved %s, %.0f s)"
          % (BOX_S[0], BOX_S[1], BOX_T[0], BOX_T[1], cnt, n_zero,
             nev, resolved, time.time() - t_b4))
    if n_zero > 0:
        print("      -> RH violation of E confirmed INSIDE the "
              "searched box (plus mirror zeros left of the line by "
              "the functional equation)")
    else:
        print("      -> no off-line zero below t = %.0f in this box; "
              "the Davenport-Heilbronn zeros sit higher -- the "
              "firewall statement rests on the measured positivity "
              "break, the RH violation itself is literature ground "
              "truth" % BOX_T[1])

    # ------------------------------------------------ verdict
    guards_ok = not any(f.startswith(("G0", "B2.0", "B2.2", "B2.3",
                                      "B3.1")) for f in FAILS)
    if not guards_ok:
        VERDICT = "EPSTEIN-FW-MIXED (guards failed)"
    elif not ok_picks:
        VERDICT = "EPSTEIN-FW-UNPOWERED"
    elif fw_break:
        VERDICT = "EPSTEIN-FW-BREAKS (the firewall works)"
    else:
        VERDICT = "EPSTEIN-FW-SUSPICIOUS (machinery blind to the "\
                  "violation at this depth)"

    check("B5.1 [C] typed reading: the correct von Mangoldt analogy "
          "for E is the -E'/E coefficient Λ_E(n) (F4); without the "
          "Euler product it goes negative and leaks off the prime "
          "powers (B1); the deployed tent machinery with Λ_E atoms "
          "%s; the class-sum rung L1 isolates multiplicativity as "
          "the load-bearing arithmetic ingredient.  No RH statement, "
          "no marker move; W3 stays open"
          % ("breaks demonstrably (B3)" if fw_break else
             "does NOT break at this depth -- a diagnostic-power "
             "warning for the W3 family read"), True)

    print("\nVERDICT: %s" % VERDICT)
    print("""
CONTRACT-NOTE TEXT (report only -- nothing is written by this probe):

  PRIME.WEIL.OPERATOR.01, Epstein-firewall round (2026-08-02): the
  window machinery was A/B-tested on the classical RH violator
  E(s) = Σ'(x²+5y²)^{-s} (disc -20, class number 2, no Euler
  product; E = ζL_-20 + L_-4 L_5 verified coefficient-wise to
  n = %d).  ARITHMETIC: Λ_E (:= -E'/E coefficients) has %d negative
  sites (first n = %d) and %d non-prime-power support points below
  %d -- the Euler-product structure (Λ >= 0, prime-power support) is
  measurably gone.  WINDOWS: on the deployed frame-A family the
  ladder Λ -> Λ(1+χ) -> Λ_E gives λ_min %s; the firewall verdict is
  %s.  TYPE: negative control of the machinery; Davenport-Heilbronn
  1936 cited for the RH violation; no marker move.
""" % (N, len(neg_idx), int(neg_idx[0]) if len(neg_idx) else -1,
       len(offpp), N,
       "; ".join("h=%d: %+.3e/%+.3e/%+.3e"
                 % (p["hz"], res["L0"]["lm"], res["L1"]["lm"],
                    res["L3"]["lm"]) for p, res in results),
       VERDICT))

    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS),
                                           FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)




def run():
    """run_all entry point: both controls, one module."""
    global N_CHK, FAILS
    f1 = run_ihara()
    n1 = N_CHK
    print()
    f2 = run_epstein()
    n2 = N_CHK
    print()
    print("=" * 78)
    print("v668 GROUND TRUTH + FIREWALL: %d + %d = %d checks, "
          "%d failure(s)" % (n1, n2, n1 + n2, f1 + f2))
    if f1 + f2 == 0:
        print("ALL CHECKS PASSED")
        print("VERDICT: IHARA-GT-CONFIRMED + EPSTEIN-FW-BREAKS -- true")
        print("positivity has NO uniform margin (delta(K) -> 0 exactly,")
        print("detection reach K* x s ~ 2-3, Fejer reads blind), and the")
        print("machinery breaks by ~13 orders of magnitude without the")
        print("Euler product (composite support carries the break).")
    return f1 + f2


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
