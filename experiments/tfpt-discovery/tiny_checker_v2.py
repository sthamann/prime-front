#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""tiny_checker_v2 -- independent auditor of the PRIME.COFINAL.PACKAGE.01
theorem package (cofinal_package.json).  EXPLORATION ONLY, no RH claim.
Version 2: repairs the six T2f defects confirmed by the CCCXXXIII
adversarial audit (chain_adversary_probe.py) against tiny_checker.py.
The original is FROZEN (the package pins checker.file/lines, the builder
gates it, the audit ran it unmodified), so v2 lives alongside it.
Repairs: (B1) moment/coefficient length mismatch is a hard refusal (no
silent zip truncation); (B2) the declared bound must be nonnegative;
(B3) an empty moment census is refused; (B4) the Part-1 statement set
and the full certificate census are anchored against fixed constants
frozen in THIS file (no self-referential hash passes); (B5) structural
shape pins per census tier (8x8 M, 10 moments, 9/6x6/5x5 certificates;
global tier G0 = deg+2, G1 = deg+1); (B6) coverage must be CONTIGUOUS
(zero gaps) or it is refused; (B7) the anchored certificate digests
include the SHAPE in the hashed payload (no cross-shape collision).
KNOWS NO MATRIX THEORY.  Verifies ONLY (a) exact rational polynomial
identities (expansion over Fractions), (b) elimination reconstruction
G == sum_k d_k v_k v_k^T, pivots d_k > 0, (c) rank-form reconstruction
with c_r > 0, (d) sign/order comparisons, (e) sha256 integrity against
the frozen anchors.  AXIOM SURFACE (all it trusts): python stdlib
integer/Fraction arithmetic, the package file and the two anchor
constants below.  DOCUMENTED LIMIT (CCCXXXIII NON_VACUITY): the entry
data (M, moments, bound, rho) are anchored to NOTHING outside the
package file -- a sub-radius entry edit (relative size below the cell's
exact robustness radius t_crit, tightest cell 3.293e-15 = 15 float64
ulp) passes this checker with all derived fields recomputed; only the
ladder rebuild certifies entry provenance.  Checker-pass is certificate
integrity, NOT entry-data certification.  Fail-fast: exit 1 at the
FIRST failing check, naming it.  Usage: python tiny_checker_v2.py
<package.json>
"""
import hashlib
import json
import sys
from fractions import Fraction
from itertools import zip_longest

FR0, FR1 = Fraction(0), Fraction(1)
rq = Fraction

# frozen anchors, computed ONCE from the genuine CCCIX package
# (cofinal_package.json, 4 statements; 5 global + 151 cell + 7
# extension certificates) -- see cert_sha for the anchored payload.
ANCHOR_PART1 = "912df6a9bbe40a59"
ANCHOR_CERTS = "f68041ce1288f800"
CELL_SHAPE = (8, 10, 9, 6, 5)   # dim M, len moments, len c, dim G0, G1

def fail(msg):
    print("FAIL  %s" % msg)
    sys.exit(1)

def sha16(txt):
    return hashlib.sha256(txt.encode("utf-8")).hexdigest()[:16]

def padd(pa, pb):
    return [u + v for u, v in zip_longest(pa, pb, fillvalue=FR0)]

def peq(pa, pb):
    return all(u == v for u, v in zip_longest(pa, pb, fillvalue=FR0))

def pmul(pa, pb):
    out = [FR0] * (len(pa) + len(pb) - 1)
    for i, u in enumerate(pa):
        for j, v in enumerate(pb):
            out[i + j] += u * v
    return out

def gram_poly(gm):
    out = [FR0] * (2 * len(gm) - 1)
    for i, row in enumerate(gm):
        for j, v in enumerate(row):
            out[i + j] += v
    return out

def rebuild_eq(pairs, gm):
    dim = len(gm)
    acc = [[FR0] * dim for _ in range(dim)]
    for cf, vec in pairs:
        if cf <= 0 or len(vec) != dim:
            return False
        for i in range(dim):
            if vec[i]:
                for j in range(dim):
                    acc[i][j] += cf * vec[i] * vec[j]
    return acc == gm

def pd_ldl(gm):
    dim = len(gm)
    wrk = [row[:] for row in gm]
    cols = []
    for k in range(dim):
        piv = wrk[k][k]
        if piv <= 0:
            return False
        vec = [FR0] * dim
        vec[k] = FR1
        for i in range(k + 1, dim):
            vec[i] = wrk[i][k] / piv
        cols.append((piv, vec))
        for i in range(k + 1, dim):
            if vec[i]:
                for j in range(k + 1, dim):
                    wrk[i][j] -= vec[i] * piv * vec[j]
    return rebuild_eq(cols, gm)

def square(tag, name, gm):
    if not gm or any(len(row) != len(gm) for row in gm):
        fail(tag + ": " + name + " is not square")

def cert_sha(beta, lce, cxs, gm0, gm1):
    """v2 (B7): the SHAPE (len c / dim G0 / dim G1) prefixes the
    payload, so certificates of different shape cannot collide."""
    return sha16("|".join(
        ["%d/%d/%d" % (len(cxs), len(gm0), len(gm1)),
         str(beta), str(lce)] + [str(v) for v in cxs]
        + [str(v) for row in gm0 for v in row]
        + [str(v) for row in gm1 for v in row]))

def legacy_sha(beta, lce, cxs, gm0, gm1):
    """The package's stored per-certificate hash field predates the
    shape separation; it is re-checked as a TRANSCRIPTION ward only.
    Integrity lives in the shape-aware census anchor."""
    return sha16("|".join(
        [str(beta), str(lce)] + [str(v) for v in cxs]
        + [str(v) for row in gm0 for v in row]
        + [str(v) for row in gm1 for v in row]))

def check_cert(tag, cert, shape):
    beta, lce = rq(cert["beta"]), rq(cert["L"])
    if not (beta > 0 and lce > beta):
        fail(tag + ": interval sign/order")
    cxs = [rq(v) for v in cert["p_coeffs_x"]]
    gm0 = [[rq(v) for v in row] for row in cert["G0"]]
    gm1 = [[rq(v) for v in row] for row in cert["G1"]]
    square(tag, "G0", gm0)
    square(tag, "G1", gm1)
    if shape is not None:                              # cell tier (B5)
        if (len(cxs), len(gm0), len(gm1)) != shape:
            fail(tag + ": certificate shape %d/%d/%d != pinned %d/%d/%d"
                 % ((len(cxs), len(gm0), len(gm1)) + shape))
    elif not (len(gm0) == len(cxs) + 1 and len(gm1) == len(cxs)):
        fail(tag + ": global certificate shape %d/%d/%d breaks the "
             "G0 = deg+2, G1 = deg+1 tier rule"
             % (len(cxs), len(gm0), len(gm1)))
    for name, gm, key in (("G0", gm0, "G0_rank"), ("G1", gm1, "G1_rank")):
        rank = cert.get(key)
        if rank is not None:
            prs = [(rq(cf), [rq(v) for v in vec]) for cf, vec in rank]
            if not rebuild_eq(prs, gm):
                fail(tag + ": " + name + " rank reconstruction/sign")
        elif not pd_ldl(gm):
            fail(tag + ": " + name + " elimination pivot")
    lhs = padd(pmul([FR0, FR1], cxs), [-FR1])
    rhs = padd(gram_poly(gm0),
               pmul([-beta * lce, beta + lce, -FR1], gram_poly(gm1)))
    if not peq(lhs, rhs):
        fail(tag + ": SOS identity residual nonzero")
    if legacy_sha(beta, lce, cxs, gm0, gm1) != cert["hash"]:
        fail(tag + ": certificate hash")
    return beta, lce, cxs, cert_sha(beta, lce, cxs, gm0, gm1)

def moments(bvec, blk, kmax):
    cur, out = bvec[:], []
    for _k in range(kmax + 1):
        out.append(sum(u * v for u, v in zip(bvec, cur)))
        cur = [sum(row[j] * cur[j] for j in range(len(cur))) for row in blk]
    return out

def check_cell(tag, cell, eta):
    mat = [[rq(v) for v in row] for row in cell["M"]]
    dim = len(mat)
    square(tag, "M", mat)
    if dim != CELL_SHAPE[0]:                                     # B5
        fail(tag + ": M is %dx%d, census tier requires %dx%d"
             % (dim, dim, CELL_SHAPE[0], CELL_SHAPE[0]))
    if not cell["moments"]:                                      # B3
        fail(tag + ": empty moment census refused")
    if len(cell["moments"]) != CELL_SHAPE[1]:                    # B5
        fail(tag + ": moment census length %d != pinned %d"
             % (len(cell["moments"]), CELL_SHAPE[1]))
    if any(mat[i][j] != mat[j][i] for i in range(dim) for j in range(dim)):
        fail(tag + ": M not symmetric")
    piv = mat[0][0]
    if not (piv > 0 and piv == rq(cell["n"])):
        fail(tag + ": pivot n sign/match")
    bvec = [mat[i][0] for i in range(1, dim)]
    blk = [row[1:] for row in mat[1:]]
    nus = moments(bvec, blk, len(cell["moments"]) - 1)
    if nus != [rq(v) for v in cell["moments"]]:
        fail(tag + ": moments nu_k = b^T B^k b mismatch")
    cfl, cce = rq(cell["region"]["floor"]), rq(cell["region"]["ceiling"])
    if not (0 < cfl < cce):
        fail(tag + ": floor/ceiling sign/order")
    dco = len(blk)
    if not pd_ldl([[blk[i][j] - (cfl if i == j else FR0)
                    for j in range(dco)] for i in range(dco)]):
        fail(tag + ": floor pivots (B - c I)")
    if not pd_ldl([[(cce if i == j else FR0) - blk[i][j]
                    for j in range(dco)] for i in range(dco)]):
        fail(tag + ": ceiling pivots (L I - B)")
    beta, lce, cxs, dig = check_cert(tag + " cert", cell["certificate"],
                                     CELL_SHAPE[2:])
    if not (beta <= cfl and lce >= cce):
        fail(tag + ": certificate domain does not cover the cell")
    if len(nus) < len(cxs):                                      # B1
        fail(tag + ": moment census (%d) shorter than certificate "
             "coefficients (%d) -- refusing truncated bound"
             % (len(nus), len(cxs)))
    bound = sum(c * v for c, v in zip(cxs, nus)) / piv
    if bound != rq(cell["bound"]):
        fail(tag + ": stored bound mismatch")
    if bound < FR0:                                              # B2
        fail(tag + ": declared bound %s is negative -- not the "
             "nonnegative certificate quantity" % cell["bound"])
    if bound > FR1 - eta:
        fail(tag + ": census bound > 1 - eta")
    den = sum(abs(c) * v for c, v in zip(cxs, nus))
    rho = ((FR1 - eta) - bound) * piv / den if den > 0 else FR0
    if rho != rq(cell["rho"]):
        fail(tag + ": stored moment-box radius rho mismatch")
    return dig

def check_coverage(cov, cells):
    ivals = sorted((rq(c["region"]["floor"]),
                    rq(c["region"]["ceiling"])) for c in cells)
    merged = []
    for lo, hi in ivals:
        if merged and lo <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], hi)
        else:
            merged.append([lo, hi])
    if [[str(a), str(b)] for a, b in merged] != cov["union_segments"]:
        fail("coverage: union segments mismatch")
    if [str(merged[0][0]), str(merged[-1][1])] != cov["covering_interval"]:
        fail("coverage: covering interval mismatch")
    if [[str(merged[i][1]), str(merged[i + 1][0])]
            for i in range(len(merged) - 1)] != cov["gaps"]:
        fail("coverage: gap list mismatch")
    if len(merged) != 1:                                         # B6
        fail("coverage: census union is NOT contiguous (%d segments, "
             "%d gaps) -- refusing" % (len(merged), len(merged) - 1))
    if sha16(cov["verdict"]) != cov["verdict_sha"]:
        fail("coverage: verdict hash")

def main():
    if len(sys.argv) != 2:
        fail("usage: tiny_checker_v2.py <package.json>")
    pkg = json.load(open(sys.argv[1], encoding="utf-8"))
    eta = rq(pkg["eta"])
    if not (0 < eta < 1):
        fail("eta out of range")
    stmts = pkg["part1_relation"]["statements"]
    for st in stmts:
        if sha16(st["text"]) != st["hash"]:
            fail("statement hash: %s" % st["id"])
    if sha16("|".join(st["hash"] for st in stmts)) != ANCHOR_PART1:  # B4
        fail("part1 anchor: statement set does not match the frozen "
             "CCCIX package constant %s -- a rewritten statement with "
             "a recomputed self-hash is refused" % ANCHOR_PART1)
    digests = []
    glob = pkg["part2_positivity"]["global_certificates"]
    for key in sorted(glob):
        digests.append("g%s:%s"
                       % (key, check_cert("global-%s" % key, glob[key],
                                          None)[3]))
    cells = pkg["part2_positivity"]["cells"]
    ext = pkg["part2_positivity"]["extension_cells"]
    if not cells:                                                # B3
        fail("empty cell census refused")
    for grp, pre, lst in (("cell", "c", cells), ("ext", "x", ext)):
        for cell in lst:
            digests.append(pre + ":" + check_cell(
                "%s %s" % (grp, cell["id"]), cell, eta))
    check_coverage(pkg["part3_coverage"], cells)
    if sha16("|".join(digests)) != ANCHOR_CERTS:                 # B4/B7
        fail("certificate census anchor: %d shape-aware digests do not "
             "match the frozen CCCIX constant %s -- this is not the "
             "anchored package" % (len(digests), ANCHOR_CERTS))
    cnt = (len(stmts), len(glob), len(cells), len(ext))
    print("CHECKER CENSUS: statements %d/%d, global %d/%d, cells %d/%d,"
          " extension %d/%d, coverage CONTIGUOUS, anchors %s/%s OK"
          " -- ALL PASS"
          % (tuple(v for c in cnt for v in (c, c))
             + (ANCHOR_PART1, ANCHOR_CERTS)))
    print("NOTE: entry data (M, moments, bound, rho) carry NO external"
          " anchor; a sub-radius entry edit (below the cell's exact"
          " robustness radius t_crit, tightest cell 3.293e-15 = 15"
          " float64 ulp; blind band [0, t_crit)) passes this checker."
          " Checker-pass certifies the package's internal certificates"
          " and coverage transcription, NOT entry-data provenance;"
          " only the ladder rebuild ties M to the wall (CCCXXXIII).")
    sys.exit(0)

if __name__ == "__main__":
    main()
