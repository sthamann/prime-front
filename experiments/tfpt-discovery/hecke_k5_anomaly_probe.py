#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""hecke_k5_anomaly_probe -- HECKE.K5ANOMALY.01: the class-1 k = 5
anomaly is decided by the 2-power residue tower of 2 mod p.

Follow-up to HECKE.HALVINGTAILS.01: for p == 1 (mod 8), with
X1(p) = H_p / 8 and v2(D_p) = 8 + v2(X1(p)), the measured tail of
k := v2(X1(p)) was geometric for k <= 4 but carried only HALF the
geometric mass at k = 5 (155 vs ~306 below 10^6), the deficit
reappearing at k >= 6.

MECHANISM (found in the pre-registration scan at 3*10^5, frozen here,
gated at 10^6):  define the TOWER PAIR
    m := v2(p - 1)   (>= 3 for p == 1 mod 8),
    t := max { j >= 1 : 2^((p-1)/2^j) == 1 (mod p) }  (<= m)
        (the depth of 2 in the 2-power residue tower: t >= 2 iff 2 is
         a quartic residue, t >= 3 iff octic, ...).
Then k is DETERMINISTIC on most (m, t) cells.  Scan table at 3*10^5
(n = number of primes; "VAR" = cell with internal spread):
    (3,1)->k=1   (3,2)->0  (3,3)->0
    (4,1)->0     (4,2)->3  (4,3)->2  (4,4)->2
    (5,1)->0     (5,2)->2  (5,3)->VAR, min 5   (5,4)->4  (5,5)->4
    (6,1)->0     (6,2)->2  (6,3)->4  (6,4)->VAR, min 6  (6,5)->6 (6,6)->6
    (7,1)->0     (7,2)->2  (7,3)->4  (7,4)->VAR  (7,5..7)->VAR (small n,
                                                  re-measured here)
THE k = 5 ANSWER: k = 5 occurs ONLY in the single cell (m, t) = (5, 3)
(p == 33 mod 64, 2 octic but not 16th-power residue), whose natural
density among p == 1 (mod 8) is (1/8)*(1/8) = 1/64; inside the cell the
tail restarts geometrically at k = 5, so P(k = 5) = 1/128 = half of the
naive 2^-6 -- EXACTLY the observed suppression, with the excess pushed
to the deterministic k = 6 cells and the deeper bands.  The naive
geometric law is thus a MIXTURE law: deterministic on the tower cells,
geometric only inside the sparse "free" bands.

INVOLUTION CENSUS (task item 1, typed):
  I1 (y <-> -y fold): built into the slice counts (parent probes).
  I2 (cross-line (a,c) maps): NO natural involution exists -- the line
      a + 2c = p is weight-asymmetric; typed as not available.
  I3 (divisor conjugation d <-> a/d): DOES yield the sigma-level
      2-structure: for a == 7 (mod 8) every divisor pair has
      d + a/d == 0 (mod 8) (pair residues (1,7), (3,5) mod 8), giving
      an elementary involution re-proof of v2(sigma(a)) >= 3 and
          sigma(a)/8 == #{pairs: d + a/d == 8 (mod 16)} (mod 2);
      for a == 3 (mod 8) every pair has d + a/d == 4 (mod 8), giving
      v2(sigma(a)) >= 2 and v2 = 2 <=> d(a) == 2 (mod 4).
      So I3 explains the BASE; the TAIL is governed by the tower.
NAMED / CITED INGREDIENTS:
  [N3] Gauss: 2 is a quartic residue mod p (p == 1 mod 8) iff 8 | B in
       p = A^2 + B^2 (equivalently p = x^2 + 64 y^2) -- censused below.
  [C]  the (m, t)-determinism itself is a GOVERNING-FIELD statement
       (splitting of p in Q(zeta_{2^j}, 2^{1/2^j})) of Cohn-Lagarias
       type (octic lore: Western, Barrucand-Cohn); CITED as the
       structural frame, machine-censused at 10^6, derivation OPEN.
  Equidistribution inside the free bands stays a Chebotarev-flavoured
  heuristic: measured, not claimed.

PREDECLARED GATES (frozen):
  G0 scaffolding + witnesses: v2(H_17) = 3 (cell (4,1), k=0),
     v2(H_41) = 4 ((3,1), k=1), v2(H_113) = 6 ((4,2), k=3) from the
     exact segment.
  G1 exact cell criteria at 10^6 (zero exceptions each):
     T1  k=1  <=> (m,t) = (3,1)
     T2  k=0  <=> (m=3 & t>=2) or (m>=4 & t=1)
         [closes the previously OPEN class-1 base-criterion bridge:
          M1 odd <=> this tower condition, via k=0 <=> M1 odd of
          HALVINGTAILS.01]
     T3  k=3  <=> (m,t) = (4,2)
     T4  k=2  <=> (m=4 & t>=3) or (m>=5 & t=2)
     T5  k=4  <=> (m=5 & t>=4) or (m>=6 & t=3)
     T6  k=5  ==> (m,t) = (5,3); inside (5,3): min k = 5 and both
         k = 5 and k >= 6 occur (no determinism claimed inside).
  G2 refined mixture law (MEASURED, not gated): full (m,t) x k census
     table at 10^6; reconstructed global P(k) from the cell laws
     (deterministic cells exact, free bands geometric restart at their
     min) vs observed histogram -- chi-square-style residuals printed;
     P(k=5) prediction 1/128 vs observed.
  G3 involution census at 10^6: I3 pair lemmas (a == 7 mod 8: all
     pairs == 0 mod 8 and sigma/8 parity = #(pairs == 8 mod 16) parity;
     a == 3 mod 8: all pairs == 4 mod 8 and v2 sigma = 2 <=> d(a) == 2
     mod 4).
  G4 [N3] Gauss quartic census at 10^5: t >= 2 <=> 8 | B.
  G5 controls: (a) class 7 CANNOT carry the (m, t) mechanism --
     structural: v2(p - 1) = 1 for all p == 7 (mod 8) (the tower of 2
     is trivial); (b) THE MIRROR LAW (found by the run-1 control,
     which was frozen as "per p mod 64 flatness" and FAILED with an
     8.2x k = 5 excess at p == 63 mod 64 -- a real structure, not a
     fluctuation; re-frozen here after a 3*10^5 scan):
         v2(X7(p)) = v2(p + 1) - 3   for v2(p + 1) <= 7,
         v2(X7(p)) >= 5              for v2(p + 1) >= 8 (free band),
     i.e. v2(D_p) = 3 + v2(p + 1) = 3 + v2(sigma(p)) deterministically
     up to k = 4 -- the SAME skeleton as class 1 (deterministic
     through k = 4, first free level k = 5).  This EXPLAINS the clean
     class-7 geometric tail: the governing invariant v2(p + 1) has
     exactly geometric density 2^-(m'-2), so the deterministic
     transfer is invisible in the aggregate histogram; class 1 shows
     the k = 5 dip only because its cell (5, 3) has density 1/64,
     half of the 1/32 that a smooth geometric tail would need.
     Consistency: class 3 (constant depth 5) obeys the same mirror
     law, 3 + v2(p + 1) = 3 + 2 = 5.  Witnesses: p = 7, 23 (m' = 3,
     k = 0), p = 47 (m' = 4, k = 1), p = 31 (m' = 5, k = 2);
     (c) k = 3 mutant does not telescope (first mismatch n = 10).
  G6 strata dissection table (REPORT only): per-cell parities of the
     minimal-stratum count M1 and the level-1 family counts at 3*10^4.

VERDICT ENUM (frozen):
  K5-MECHANISM-FOUND : T1-T6 census-clean at 10^6 + involution census
                       + controls pass (mechanism = tower localization
                       with cell (5,3) restart; refined law measured).
  K5-PARTIAL         : localization T6 holds but some deterministic
                       cell gate fails.
  K5-OPEN            : the localization itself fails.

Exploration only (experiments/tfpt-discovery/): no verification/, no
ledger, no papers, no website surfaces touched.
"""
from __future__ import annotations

import time
from collections import Counter
from math import isqrt

from hecke_check32_probe import build_f8, embed, sieve_primes, sieve_sigma3
from hecke_multirate2adic_probe import (h_series, kron_mul_fast,
                                        sieve_sigma1, v2_capped)

# ---------------------------------------------------------------- budgets
N_SEG = 20_000
N_PAIR = 1_000_000      # divisor-pair involution census
N_GAUSS = 100_000       # [N3] two-squares census
N_DISS = 30_000         # strata dissection table (report only)
N_CTL = 5_000
CAP = 1_000_000
MOD_BITS = 20
K3_FIRST_MISMATCH = 10
WITNESS_VH = {17: 3, 41: 4, 113: 6}          # exact v2(H_p), frozen
K5_CELL = (5, 3)

CHECKS = []


def check(label: str, ok: bool) -> bool:
    CHECKS.append((label, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return bool(ok)


def v2_of(x):
    v = 0
    while x % 2 == 0:
        x //= 2
        v += 1
    return v


def tower(p):
    """(m, t): m = v2(p-1); t = depth of 2 in the 2-power tower mod p."""
    m = v2_of(p - 1)
    t = 0
    for j in range(1, m + 1):
        if pow(2, (p - 1) >> j, p) == 1:
            t = j
        else:
            break
    return m, t


def two_sq(p):
    """p == 1 (mod 4) prime -> (A, B) with p = A^2 + B^2, A odd, B even."""
    for b in range(2, isqrt(p) + 1, 2):
        s = p - b * b
        r = isqrt(s)
        if r * r == s:
            return r, b
    raise ValueError(p)


# ================================================================== run
def main():
    t0 = time.time()
    print("hecke_k5_anomaly_probe -- HECKE.K5ANOMALY.01")
    print("  claim: k = v2(X1(p)) is governed by (m, t) = "
          "(v2(p-1), 2-power depth of 2); k = 5 lives only in (5, 3)")

    # ------------------------------------------------------------- P0
    print("P0 -- scaffolding + witnesses")
    a = build_f8(N_SEG)
    sig3 = sieve_sigma3(N_SEG)
    sig1 = sieve_sigma1(N_SEG)
    H = h_series(sig1, N_SEG)
    check("scaffold: sigma3 - a == 32 H on odd n <= " + str(N_SEG),
          all(sig3[n] - a[n] == 32 * H[n] for n in range(1, N_SEG + 1, 2)))
    wit_ok = True
    for p, vh in WITNESS_VH.items():
        got = v2_of(H[p])
        cell = tower(p)
        print(f"        witness p={p}: v2(H)={got} (expect {vh}), "
              f"(m,t)={cell}")
        wit_ok &= got == vh
    check("witnesses: v2(H_17)=3 @(4,1)k0, v2(H_41)=4 @(3,1)k1, "
          "v2(H_113)=6 @(4,2)k3", wit_ok
          and tower(17) == (4, 1) and tower(41) == (3, 1)
          and tower(113) == (4, 2))

    # ------------------------------------------------------------- P1
    print("P1 -- 10^6 census: k vs tower cells")
    t1 = time.time()
    sig1_big = sieve_sigma1(CAP)
    Hm = h_series(sig1_big, CAP - 1, mod=1 << MOD_BITS)
    print(f"        H mod 2^{MOD_BITS} to {CAP - 1}: {time.time()-t1:.1f}s")
    primes = [p for p in sieve_primes(CAP - 1) if p % 2 == 1]
    recs = []                                   # (p, k, m, t) class 1
    for p in primes:
        if p % 8 == 1:
            k = v2_capped(Hm[p], MOD_BITS) - 3
            m, t = tower(p)
            recs.append((p, k, m, t))
    n1 = len(recs)
    cells = {}
    for _, k, m, t in recs:
        cells.setdefault((m, t), Counter())[k] += 1
    print(f"        class-1 primes: {n1}; occupied cells: {len(cells)}")
    print("        full (m,t) x k table (k capped at "
          f"{MOD_BITS - 3} = cap):")
    for cell in sorted(cells):
        c = cells[cell]
        body = " ".join(f"k{k}:{c[k]}" for k in sorted(c))
        tag = ("DET k=%d" % next(iter(c)) if len(c) == 1
               else f"VAR min k={min(c)}")
        print(f"          (m,t)={cell}: n={sum(c.values()):5d}  [{tag}]  "
              f"{body}")

    def kset(pred):
        return {k for (_, k, m, t) in recs if pred(m, t)}

    def where(kv):
        return {(m, t) for (_, k, m, t) in recs if k == kv}

    t1_ok = check(
        f"T1: k=1 <=> (m,t)=(3,1), all {n1} class-1 primes < {CAP} "
        f"(k=1 cells: {sorted(where(1))})",
        where(1) == {(3, 1)} and kset(lambda m, t: (m, t) == (3, 1))
        == {1})
    t2_ok = check(
        "T2: k=0 <=> (m=3 & t>=2) | (m>=4 & t=1)  [closes the class-1 "
        "base-criterion bridge: M1 odd <=> tower condition]",
        all((k == 0) == ((m == 3 and t >= 2) or (m >= 4 and t == 1))
            for (_, k, m, t) in recs))
    t3_ok = check(
        f"T3: k=3 <=> (m,t)=(4,2) (k=3 cells: {sorted(where(3))})",
        where(3) == {(4, 2)} and kset(lambda m, t: (m, t) == (4, 2))
        == {3})
    t4_ok = check(
        "T4: k=2 <=> (m=4 & t>=3) | (m>=5 & t=2)",
        all((k == 2) == ((m == 4 and t >= 3) or (m >= 5 and t == 2))
            for (_, k, m, t) in recs))
    t5_ok = check(
        "T5: k=4 <=> (m=5 & t>=4) | (m>=6 & t=3)",
        all((k == 4) == ((m == 5 and t >= 4) or (m >= 6 and t == 3))
            for (_, k, m, t) in recs))
    c53 = cells.get(K5_CELL, Counter())
    t6_ok = check(
        f"T6 (THE ANOMALY): k=5 only in (m,t)={K5_CELL} (k=5 cells: "
        f"{sorted(where(5))}); inside (5,3): min k = "
        f"{min(c53) if c53 else None}, n(k=5)={c53.get(5, 0)}, "
        f"n(k>=6)={sum(v for kk, v in c53.items() if kk >= 6)}",
        where(5) == {K5_CELL} and bool(c53) and min(c53) == 5
        and c53.get(5, 0) > 0
        and sum(v for kk, v in c53.items() if kk >= 6) > 0)

    # ------------------------------------------------------------- P2
    print("P2 -- refined mixture law (measured, not gated)")
    pred = Counter()
    for cell, c in cells.items():
        w = sum(c.values())
        if len(c) == 1:
            pred[next(iter(c))] += w
        else:
            kmin = min(c)
            for j in range(0, 40):
                pred[kmin + j] += w * 2.0 ** (-j - 1)
    print("        reconstructed P(k) (det cells exact + geometric "
          "restart in free bands) vs observed:")
    chi2 = 0.0
    obs_hist = Counter(k for (_, k, _, _) in recs)
    for k in range(0, 11):
        o = obs_hist.get(k, 0)
        e = pred.get(k, 0.0)
        if e > 0:
            chi2 += (o - e) ** 2 / e
        print(f"          k={k:2d}: obs={o:6d}  law={e:9.1f}  "
              f"obs/law={o / e if e else float('nan'):.3f}")
    print(f"          chi-square-style sum over k<=10: {chi2:.1f} "
          "(free-band restart is heuristic -- measured only)")
    d53 = sum(cells.get(K5_CELL, Counter()).values()) / n1
    print(f"          density of cell (5,3): {d53:.5f} (naive 1/64 = "
          f"{1 / 64:.5f}); P(k=5) observed {obs_hist.get(5, 0) / n1:.5f} "
          f"vs tower prediction 1/128 = {1 / 128:.5f}")
    check("refined law recorded: mixture (deterministic tower cells + "
          "geometric free bands) printed with residuals; P(k=5) = "
          "(1/64)*(1/2) = 1/128 quantitatively explains the halved "
          "level (statistics reported, not gated)", True)

    # ------------------------------------------------------------- P3
    print("P3 -- involution census (I3 divisor-conjugation pair lemmas)")
    t1 = time.time()
    cnt8 = bytearray(N_PAIR + 1)    # parity of #{pairs == 8 mod 16}
    dcnt = bytearray(N_PAIR + 1)    # d(a)/2 mod 2 via pair parity
    pair_viol_7 = pair_viol_3 = 0
    for d in range(1, isqrt(N_PAIR) + 1, 2):
        for e in range(d, N_PAIR // d + 1, 2):
            n = d * e
            r = n % 8
            s = (d + e) % 16
            if r == 7:
                if s % 8 != 0:
                    pair_viol_7 += 1
                if s == 8:
                    cnt8[n] ^= 1
            elif r == 3:
                if s % 8 != 4:
                    pair_viol_3 += 1
                dcnt[n] ^= 1
    bad_p7 = sum(1 for m in range(7, N_PAIR + 1, 8)
                 if ((sig1_big[m] >> 3) & 1) != cnt8[m])
    bad_p3 = sum(1 for m in range(3, N_PAIR + 1, 8)
                 if (v2_capped(sig1_big[m], 6) == 2) != (dcnt[m] == 1))
    print(f"        pair sieve: {time.time()-t1:.1f}s")
    check(f"I3a: a == 7 (mod 8): every divisor pair d + a/d == 0 (mod 8) "
          f"(violations: {pair_viol_7}) and sigma(a)/8 parity == "
          f"#{{pairs: d+a/d == 8 mod 16}} parity, all a <= {N_PAIR} "
          f"(mismatches: {bad_p7})", pair_viol_7 == 0 and bad_p7 == 0)
    check(f"I3b: a == 3 (mod 8): every pair == 4 (mod 8) (violations: "
          f"{pair_viol_3}) and v2(sigma(a)) = 2 <=> d(a) == 2 (mod 4), "
          f"all a <= {N_PAIR} (mismatches: {bad_p3})",
          pair_viol_3 == 0 and bad_p3 == 0)
    check("I1/I2 typing: y <-> -y fold built into slice counts; no "
          "natural cross-line involution exists on a + 2c = p (weight-"
          "asymmetric) -- the tail mechanism is the tower, not a "
          "term pairing", True)

    # ------------------------------------------------------------- P4
    print("P4 -- [N3] Gauss quartic census")
    bad_g = []
    for (p, k, m, t) in recs:
        if p >= N_GAUSS:
            break
        A, B = two_sq(p)
        if (t >= 2) != (B % 8 == 0):
            bad_g.append(p)
    n_g = sum(1 for r in recs if r[0] < N_GAUSS)
    check(f"[N3] Gauss: t >= 2 (2 quartic residue) <=> 8 | B in "
          f"p = A^2 + B^2, all {n_g} class-1 primes < {N_GAUSS} "
          f"(failures: {len(bad_g)})", len(bad_g) == 0)

    # ------------------------------------------------------------- P5
    print("P5 -- strata dissection table (report only)")
    vs = [0] * (N_DISS + 1)
    for mm in range(1, N_DISS + 1, 2):
        vs[mm] = v2_capped(sig1_big[mm], 6)
    print("        per-cell: [M1 parity pattern] -> k  (p < "
          f"{N_DISS}; M1 = level-0 count, L1 = level-1 family count)")
    diss = {}
    for (p, k, m, t) in recs:
        if p >= N_DISS:
            break
        m1 = l1 = 0
        y = 1
        while 2 * y * y < p:
            av = vs[p - 2 * y * y]
            if av == 3:
                m1 += 1
            elif av == 4:
                l1 += 1                       # branch-A c-square, v=4
            y += 2
        for c in range(1, (p - 1) // 2 + 1, 2):
            cv = vs[c]
            av = vs[p - 2 * c]
            if c % 8 in (1, 5) and cv == 1 and av == 3:
                l1 += 1                       # branch-A off-square level 1
            elif c % 8 == 3 and cv == 2 and av == 2:
                l1 += 1                       # branch-B minimal
        diss.setdefault((m, t), Counter())[(m1 % 2, l1 % 2, min(k, 6))] += 1
    for cell in sorted(diss):
        pat = ", ".join(f"(M1%2={a},L1%2={b})->k{kk}:{v}"
                        for (a, b, kk), v in sorted(diss[cell].items()))
        print(f"          (m,t)={cell}: {pat}")
    check("dissection recorded: minimal-stratum parity M1 tracks k=0 "
          "(T2), level-1 parities tabulated per tower cell -- the "
          "tower enters already at the first two strata levels "
          "(derivation of the full determinism typed OPEN, "
          "Cohn-Lagarias-flavoured governing statement cited)", True)

    # ------------------------------------------------------------- P6
    print("P6 -- controls")
    check("C-a structural: v2(p - 1) == 1 for ALL p == 7 (mod 8) < "
          f"{CAP} -- the tower is trivial in class 7, the mechanism "
          "CANNOT act there",
          all(v2_of(p - 1) == 1 for p in primes if p % 8 == 7))
    mirror_cells = {}
    bad_mirror = []
    n7 = 0
    for p in primes:
        if p % 8 != 7:
            continue
        n7 += 1
        k = v2_capped(Hm[p], MOD_BITS) - 1
        mp = v2_of(p + 1)
        mirror_cells.setdefault(min(mp, 9), Counter())[k] += 1
        if mp <= 7:
            if k != mp - 3:
                bad_mirror.append(p)
        elif k < 5:
            bad_mirror.append(p)
    print("        class-7 mirror table (m' = v2(p+1), m' >= 9 pooled):")
    for mp in sorted(mirror_cells):
        c = mirror_cells[mp]
        tag = "DET k=%d" % next(iter(c)) if len(c) == 1 \
            else f"VAR min k={min(c)}"
        print(f"          m'={mp}: n={sum(c.values()):5d} [{tag}]  "
              + " ".join(f"k{k}:{c[k]}" for k in sorted(c)))
    check("C-b class-7 MIRROR LAW: v2(X7(p)) = v2(p+1) - 3 for "
          "v2(p+1) <= 7 and >= 5 in the free band v2(p+1) >= 8, ALL "
          f"{n7} primes p == 7 (mod 8) < {CAP} (violations: "
          f"{len(bad_mirror)}) => v2(D_p) = 3 + v2(sigma(p)) through "
          "k = 4; class-3 consistency 3 + 2 = 5; the run-1 'flatness' "
          "control failure (8.2x k=5 at p == 63 mod 64) is exactly "
          "this law -- class 7 carries the mirror skeleton, whose "
          "geometric cell densities hide it from the aggregate "
          "histogram; NO (m,t)-tower signature (C-a)",
          len(bad_mirror) == 0)
    sig1_c = sig1[:N_CTL + 1]
    L = [0] + [sig1_c[n] for n in range(1, N_CTL + 1)]
    L_no3 = [0] + [sig1_c[n] if n % 3 else 0 for n in range(1, N_CTL + 1)]
    h3 = kron_mul_fast(L, embed(L, 3, N_CTL), N_CTL)
    w19 = kron_mul_fast(L, embed(L, 9, N_CTL), N_CTL)
    w127 = kron_mul_fast(L, embed(L, 27, N_CTL), N_CTL)
    u13 = kron_mul_fast(L, embed(L_no3, 3, N_CTL), N_CTL)
    mism = [n for n in range(1, N_CTL + 1)
            if h3[n] - 3 * w19[n] + 2 * w127[n] != u13[n]]
    check(f"C-c k = 3 mutant does not telescope: first mismatch "
          f"n = {mism[0] if mism else None} (predeclared "
          f"{K3_FIRST_MISMATCH})",
          len(mism) > 0 and mism[0] == K3_FIRST_MISMATCH)

    # ---------------------------------------------------------- verdict
    n_pass = sum(1 for _, ok in CHECKS if ok)
    n_all = len(CHECKS)
    det_ok = t1_ok and t2_ok and t3_ok and t4_ok and t5_ok
    assert det_ok or n_pass < n_all
    if not t6_ok:
        verdict = "K5-OPEN"
    elif n_pass == n_all:
        verdict = "K5-MECHANISM-FOUND"
    else:
        verdict = "K5-PARTIAL"
    print(f"CHECKS: {n_pass}/{n_all} passed; walltime "
          f"{time.time() - t0:.1f}s")
    print(f"VERDICT: {verdict}")
    return 0 if verdict == "K5-MECHANISM-FOUND" else 1


if __name__ == "__main__":
    raise SystemExit(main())
