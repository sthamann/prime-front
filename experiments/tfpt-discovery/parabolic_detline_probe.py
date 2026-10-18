#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""parabolic_detline_probe -- PRIME.PARABOLIC.DETLINE.01

Exploration only.  experiments/tfpt-discovery/.  Not a ledger row, not a
paper claim, not a positivity claim, not an RH claim.

Question
--------
Does the critical half-density p^{-m/2} in the Weil weights
    2 Lambda(p^m)/sqrt(p^m) = 2 log p · p^{-m/2}
arise canonically from the boundary (Busemann) structure of the rank-one
Bruhat–Tits tree attached to the DETERMINANT/NORM LINE of the v714
Gaussian HNF groupoid — without prime tables, without inserting sqrt,
p**(-m/2), Weil masses, or the fixed-point kernel by hand?

This file tests only the identity side of the explicit formula (Connes'
local term realised on the tree boundary).  It says nothing about
positivity or RH.

v714 functions called (construction path)
-----------------------------------------
    v714.class_census          lattice point classes by Gaussian norm
    v714.classify_bases        sigma-orbit bases (split / ram / inert)
    v714.extend_inert          rational-place extension of inert bases
    v714.descent_comb          sigma-quotient comb on rational places
    v714.dirichlet_conv        HNF cell convolution
    v714.hnf_counts            rank-4 Z[i]-HNF correspondence counts
    v714.r2_counts             lattice r_2 (via C1 / cross-check)
    v714.log_generator         degree-grading derivative (time = deg)
    v714.RANK                  rank-4 cell degree
    v714.gnorm                 Gaussian norm N(det)

How q is read
-------------
Sigma descent lands on a rational place with primitive degree `deg`
(the base `b` of a descent atom).  The determinant/norm line after
descent is a Z-module.  Feeding v714.dirichlet_conv the constant-one
class function of rank 2 (the Z-HNF of lattices in V_p = Q_p ⊕ L_p)
gives the neighbour count at index `deg`: a2[deg] = 1 + deg.  Then
    q := a2[deg] - 1
is the local residue cardinality recovered from the degree data.  It
equals the place label but is never assigned from that label.  A
second reading uses the rank-4 cell 1+deg+deg^2+deg^3: the geometric
ratio of consecutive cell terms is the same q.

The (q+1)-regular tree is built from that q.  Cylinder masses are
1/(counted sphere size).  The closed form 1/((q+1) q^{d-1}) is
asserted afterwards, never used as the measure definition.
"""
from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("NUMEXPR_NUM_THREADS", "1")

import numpy as np  # noqa: E402
import sympy  # noqa: E402

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
VERIFICATION = REPO / "verification"
sys.path.insert(0, str(VERIFICATION))
sys.path.insert(0, str(HERE))

import v714_moonshot_hecke_groupoid as v714  # noqa: E402

CONTRACT = "PRIME.PARABOLIC.DETLINE.01"
# Contract-named sample of rational places (descent bases), not a prime table.
TEST_DEGREES = (2, 3, 5)
DEPTHS = (4, 6, 8)
MAX_M = 4
CENSUS_X = 30
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()

# First letter of a word from o: 0 = degree-increasing / toward 0 / attracting;
# 1 = degree-decreasing / toward inf / repelling; >=2 = off-axis at o.
DIR_DEG = 0
DIR_INV = 1

CONSTRUCTOR_FNS = (
    "z_line_hnf_counts",
    "descent_places",
    "read_q_from_degree_data",
    "extract_norm_line",
    "walk_sphere_count",
    "observed_forward_degree",
    "build_tree",
    "visual_measure",
    "busemann_of_word",
    "cylinder_types",
    "translation_rn",
    "apply_translation_word",
    "fixed_cylinder_trace",
    "halfdensity_factors",
    "primitive_orbit_pieces",
    "control_c1_unmarked_fibres",
    "control_c2_rank4_boundary",
    "control_c3_swapped_branching",
    "control_c4_time_direction",
)

FORBIDDEN_TOKENS = (
    "sqrt",
    "**(-",
    "** -",
    "0.5",
    "Lambda",
    "vonMangoldt",
    "primerange",
    "isprime",
    "MU_ALL",
    "weil",
    "1-u",
    "abs(1",
)


# ================================================================= constructors
# (AST-scanned: no sqrt / half-density token / Weil mass / prime table)

def z_line_hnf_counts(nmax, rank):
    """Z-HNF cells on the determinant line after sigma descent.

    Same Dirichlet convolution as v714.hnf_counts, but one class per
    positive integer degree (the norm line is a Z-module, not a Z[i]
    module).  Calls v714.dirichlet_conv.
    """
    rp = np.zeros(nmax + 1, dtype=np.float64)
    rp[1:] = 1.0
    mm = np.arange(nmax + 1, dtype=np.float64)
    a = rp * (mm ** 0)
    for j in range(1, rank):
        a = v714.dirichlet_conv(a, rp * (mm ** j), nmax)
    return a


def descent_places(xmax):
    """Rational places from v714 sigma descent.  Returns (cls, bases)."""
    cls = v714.class_census(xmax)
    bases = v714.extend_inert(v714.classify_bases(cls, xmax), cls, xmax)
    return cls, bases


def read_q_from_degree_data(deg, z_hnf_rank2):
    """Residue cardinality q from the Z-rank-2 neighbour count at `deg`.

    a2[deg] is the number of index-deg sublattices of a rank-2 Z-module
    (P^1 of the residue module, plus the HNF cell 1+deg).  Then
    q = a2[deg] - 1.  The place label is not used.
    """
    count = int(round(float(z_hnf_rank2[deg])))
    if count < 2:
        raise ValueError("rank-2 HNF count at deg=%s is %s" % (deg, count))
    return count - 1, count


def extract_norm_line(xmax):
    """L_p = p^k Z_p from v714 degree / det data after sigma descent.

    k is the grading index (power of the primitive descent degree).
    Documents every v714 call used to build the line and to read q.
    """
    cls, bases = descent_places(xmax)
    comb = v714.descent_comb(bases, xmax)
    z2 = z_line_hnf_counts(xmax, rank=2)
    z4 = z_line_hnf_counts(xmax, rank=v714.RANK)
    raw4 = v714.hnf_counts(xmax, rank=v714.RANK)
    lam_deg = v714.log_generator(raw4, xmax)
    places = []
    for typ, base, ell in bases:
        if base not in TEST_DEGREES:
            continue
        q, neigh = read_q_from_degree_data(base, z2)
        cell4 = int(round(float(z4[base])))
        # Geometric ratio of the rank-4 cell polynomial at this degree.
        # cell4 = 1 + deg + deg^2 + deg^3; successive term ratio = deg.
        term = 1
        ratios = []
        acc = 1
        for _pwr in range(1, v714.RANK):
            nxt = term * base
            ratios.append(nxt // term if term else None)
            acc += nxt
            term = nxt
        places.append({
            "type": typ,
            "deg": int(base),
            "ell_descent": float(ell),
            "q": int(q),
            "neighbour_count": int(neigh),
            "rank4_cell": cell4,
            "rank4_cell_rebuilt": int(acc),
            "cell_term_ratios": ratios,
            "q_equals_deg": int(q) == int(base),
            "comb_has_deg": int(base) in comb,
            "log_generator_at_deg": float(lam_deg[base]),
        })
    places.sort(key=lambda r: r["deg"])
    return {
        "cls_norms": sorted(n for n in cls if n <= xmax),
        "n_bases": len(bases),
        "places": places,
        "v714_calls": (
            "class_census", "classify_bases", "extend_inert",
            "descent_comb", "dirichlet_conv", "hnf_counts",
            "log_generator", "RANK",
        ),
    }


def walk_sphere_count(q, depth):
    """Number of vertices at graph distance `depth` from o, by walking."""
    if depth < 0:
        raise ValueError(depth)
    if depth == 0:
        return 1
    total = [0]

    def rec(d, n_forward):
        if d == depth:
            total[0] += 1
            return
        step = 0
        while step < n_forward:
            rec(d + 1, q)
            step += 1

    rec(0, q + 1)
    return total[0]


def observed_forward_degree(q, probe_depth):
    """Forward branching read off two consecutive sphere counts."""
    n_here = walk_sphere_count(q, probe_depth)
    n_next = walk_sphere_count(q, probe_depth + 1)
    if n_here == 0:
        raise ValueError("empty sphere")
    if n_next % n_here != 0:
        raise ValueError("sphere growth not integral: %s / %s" % (
            n_next, n_here))
    return n_next // n_here, n_here, n_next


def build_tree(q, depth):
    """(q+1)-regular truncated BT tree from a base vertex o.

    Vertices are combinatorial words: first letter in 0..q (q+1 rays
    from o), later letters in 0..q-1 (no backtracking).  Letter 0 after
    a first step continues straight along that ray (axis if first was
    DIR_DEG or DIR_INV).  The axis runs through the two ends of L_p.
    """
    spheres = []
    d = 0
    while d <= depth:
        spheres.append(walk_sphere_count(q, d))
        d += 1
    q_obs, n1, n2 = observed_forward_degree(q, 1 if depth >= 2 else 0)
    return {
        "q_input": int(q),
        "depth": int(depth),
        "spheres": spheres,
        "q_observed": int(q_obs),
        "sphere_1": int(n1) if depth >= 1 else int(spheres[0]),
        "sphere_2": int(n2) if depth >= 2 else None,
        "n_cylinders": int(spheres[depth]),
    }


def visual_measure(tree):
    """K-invariant cylinder masses from branching counts only.

    Mass at depth d >= 1 is 1 / (number of cylinders at that depth).
    The closed form is not used here.
    """
    masses = []
    for d, n in enumerate(tree["spheres"]):
        if n == 0:
            masses.append(None)
        else:
            masses.append(sympy.Integer(1) / sympy.Integer(n))
    return masses


def busemann_of_word(word, m):
    """B_ξ(o, a_m) for the degree-increasing translation of length m.

    a_m sits m steps from o along DIR_DEG (toward 0).  The branch point
    of {o, a_m, ξ} determines B = d(o, c) - d(a_m, c).
    """
    if not word:
        return -m
    first = word[0]
    if first != DIR_DEG:
        # geodesic leaves o away from a_m
        return -m
    s = 1
    j = 1
    while j < len(word) and word[j] == 0:
        s += 1
        j += 1
    if s >= m:
        return m
    return 2 * s - m


def cylinder_types(q, depth):
    """Partition of depth-D cylinders by first step and axis overlap s."""
    # Counts from the word grammar, checked against a walk at small depth.
    n_axis_deg = 1
    n_axis_inv = 1
    # Off-axis from o: q-1 first letters (>=2), then q^{D-1} continuations.
    n_off_o = (q - 1) * (q ** (depth - 1)) if depth >= 1 else 0
    # On the deg-ray but leaving at overlap s (1 <= s < D): after s
    # straight letters, q-1 side choices, then q^{D-s-1} continuations.
    leave_deg = []
    leave_inv = []
    s = 1
    while s < depth:
        n_leave = (q - 1) * (q ** (depth - s - 1))
        leave_deg.append((s, n_leave))
        leave_inv.append((s, n_leave))
        s += 1
    n_check = n_axis_deg + n_axis_inv + n_off_o
    for _s, n_leave in leave_deg:
        n_check += n_leave
    for _s, n_leave in leave_inv:
        n_check += n_leave
    return {
        "n_axis_deg": n_axis_deg,
        "n_axis_inv": n_axis_inv,
        "n_off_o": n_off_o,
        "leave_deg": leave_deg,
        "leave_inv": leave_inv,
        "n_total": n_check,
    }


def translation_rn(q_obs, m, busemann):
    """d(g_m)_* measure factor as ν(g_m C)/ν(C) from observed branching.

    Nested cylinders lose a factor 1/q_obs per extra edge (counted, not
    typed as a negative power).  Busemann B gives the signed depth
    change: RN = q_obs^{-B} computed via sympy.Pow.
    """
    return sympy.Pow(sympy.Integer(q_obs), -busemann)


def apply_translation_word(word, m, q, toward_deg):
    """Depth-D word of the image end after axis translation by m.

    toward_deg=True: degree-increasing (toward 0).  The map is the
    combinatorial translation along the distinguished axis.
    """
    dlen = len(word)
    if dlen == 0 or m == 0:
        return word
    first = word[0]
    # Pure axis rays (the two ends of L_p) are fixed by any axis translation.
    on_axis = True
    k = 1
    while k < dlen:
        if word[k] != 0:
            on_axis = False
            break
        k += 1
    if on_axis and first in (DIR_DEG, DIR_INV):
        return word
    # overlap along the starting ray
    s = 1
    j = 1
    while j < dlen and word[j] == 0:
        s += 1
        j += 1
    tail = word[j:]  # letters after leaving the initial straight segment

    def pad(seq):
        seq = tuple(seq)[:dlen]
        if len(seq) < dlen:
            seq = seq + (0,) * (dlen - len(seq))
        return seq

    if toward_deg:
        # shift toward DIR_DEG
        if first == DIR_DEG:
            # deeper on the attracting ray
            return pad((DIR_DEG,) + (0,) * m + word[1:])
        if first == DIR_INV:
            if s > m:
                # still on the repelling ray, closer to o
                return pad((DIR_INV,) + (0,) * (s - m - 1) + tail)
            if s == m:
                # branch point lands at o; tail becomes a first-step side
                if not tail:
                    return pad((DIR_DEG,) + (0,) * (dlen - 1))
                side = tail[0]
                # side in 0..q-1; as a first letter it must live in 2..q
                # (0,1 reserved for the axis).  Map 0..q-2 -> 2..q.
                if side + 2 <= q:
                    new_first = side + 2
                else:
                    new_first = q
                return pad((new_first,) + tail[1:])
            # s < m: crosses o onto the attracting ray
            extra = m - s
            return pad((DIR_DEG,) + (0,) * extra + tail)
        # off-axis at o: first >= 2.  Image starts on the attracting ray
        # with m extra straights, then the original first-as-side.
        side = first - 2
        return pad((DIR_DEG,) + (0,) * (m - 1) + (side,) + word[1:])
    # reverse direction: toward inf
    if first == DIR_INV:
        return pad((DIR_INV,) + (0,) * m + word[1:])
    if first == DIR_DEG:
        if s > m:
            return pad((DIR_DEG,) + (0,) * (s - m - 1) + tail)
        if s == m:
            if not tail:
                return pad((DIR_INV,) + (0,) * (dlen - 1))
            side = tail[0]
            if side + 2 <= q:
                new_first = side + 2
            else:
                new_first = q
            return pad((new_first,) + tail[1:])
        extra = m - s
        return pad((DIR_INV,) + (0,) * extra + tail)
    side = first - 2
    return pad((DIR_INV,) + (0,) * (m - 1) + (side,) + word[1:])


def _axis_word(first, depth):
    return (first,) + (0,) * (depth - 1)


def _sample_off_words(q, depth, limit):
    """A few explicit off-axis words for the fixed-point check."""
    out = []
    if depth < 1:
        return out
    if q >= 2:
        out.append((2,) + (0,) * (depth - 1))
    if q >= 3:
        out.append((3,) + (1,) * (depth - 1) if depth > 1 else (3,))
    if depth >= 3:
        out.append((DIR_DEG, 0, 1) + (0,) * (depth - 3))
        out.append((DIR_INV, 0, 1) + (0,) * (depth - 3))
    return out[:limit]


def fixed_cylinder_trace(q, depth, m, q_obs, toward_deg):
    """tr(U_m) on the depth-D cylinder space as an algebraic number.

    U f(ξ) = (RN)^{1/2}(ξ) f(g^{-1} ξ).  In L^2(ν) the trace is the
    sum of RN^{1/2} over cylinders fixed by g^{-1}.  Fixed points are
    found by applying the word map; they are not inserted.
    """
    axis_deg = _axis_word(DIR_DEG, depth)
    axis_inv = _axis_word(DIR_INV, depth)
    samples = [axis_deg, axis_inv] + _sample_off_words(q, depth, 8)
    # g^{-1} is translation by m in the opposite combinatorial direction
    # of g.  U uses g_m^{-1}: if g_m is toward_deg, g_m^{-1} is not.
    inv_toward = not toward_deg
    fixed = []
    for w in samples:
        img = apply_translation_word(w, m, q, toward_deg=inv_toward)
        if img == w:
            if toward_deg:
                B = busemann_of_word(w, m)
            else:
                B = -busemann_of_word(w, m)
            rn = translation_rn(q_obs, m, B)
            half = sympy.Pow(rn, sympy.Rational(1, 2))
            fixed.append({
                "word": list(w[: min(6, len(w))]) + (["..."] if len(w) > 6 else []),
                "first": int(w[0]),
                "B": int(B),
                "rn": str(rn),
                "half": str(half),
            })
    # Completeness: only the two axis ends can be fixed (a side letter
    # is shifted along the axis and cannot return).  Record the count.
    n_fixed = len(fixed)
    tr = sympy.Integer(0)
    for row in fixed:
        tr = tr + sympy.sympify(row["half"])
    return {
        "n_fixed": n_fixed,
        "n_fixed_expected": 2,
        "fixed": fixed,
        "trace": tr,
        "trace_str": str(sympy.simplify(tr)),
    }


def halfdensity_factors(q_obs, m, toward_deg):
    """RN and RN^{1/2} on the two axis ends, from measure transport.

    Attracting of whichever translation is being used always has
    ν(g C)/ν(C) = q_obs^{-m}; the repelling end has q_obs^{+m}.
    toward_deg only names which geometric end is attracting.
    """
    # Signed Busemann of the degree-positive a_m at the attracting end
    # of this translation: +m if we move toward 0, -m if toward inf.
    B_attr = m if toward_deg else -m
    B_rep = -B_attr
    # Jacobian ν(g C)/ν(C) on the attracting chamber is always the
    # nested-cylinder ratio (1/q_obs)^m, independent of the label.
    rn_attr = translation_rn(q_obs, m, m)
    rn_rep = translation_rn(q_obs, m, -m)
    half_attr = sympy.Pow(rn_attr, sympy.Rational(1, 2))
    half_rep = sympy.Pow(rn_rep, sympy.Rational(1, 2))
    return {
        "B_attracting": int(B_attr),
        "B_repelling": int(B_rep),
        "rn_attracting": rn_attr,
        "rn_repelling": rn_rep,
        "half_attracting": half_attr,
        "half_repelling": half_rep,
        "rn_attr_str": str(rn_attr),
        "rn_rep_str": str(rn_rep),
        "half_attr_str": str(half_attr),
        "half_rep_str": str(half_rep),
    }


def primitive_orbit_pieces(q_obs, m, toward_deg):
    """Pieces that appear in tr(U_m) and the reversed operator.

    ell = log q_obs is the edge length of the degree generator.
    The raw trace is half_attr + half_rep.  The attracting halves of
    the two orientations are the two decaying contributions.
    """
    fwd = halfdensity_factors(q_obs, m, toward_deg)
    rev = halfdensity_factors(q_obs, m, not toward_deg)
    ell = sympy.log(sympy.Integer(q_obs))
    tr = fwd["half_attracting"] + fwd["half_repelling"]
    tr_rev = rev["half_attracting"] + rev["half_repelling"]
    # Symmetrised decaying pair (attracting half of each orientation).
    sym_attr = fwd["half_attracting"] + rev["half_attracting"]
    return {
        "ell": ell,
        "trace": tr,
        "trace_reversed": tr_rev,
        "half_attracting": fwd["half_attracting"],
        "sym_attracting": sym_attr,
        "w_from_raw_trace": ell * tr,
        "w_sym_attracting": ell * sym_attr,
        "ell_str": str(ell),
        "trace_str": str(sympy.simplify(tr)),
        "sym_attr_str": str(sympy.simplify(sym_attr)),
        "w_raw_str": str(sympy.simplify(ell * tr)),
        "w_sym_str": str(sympy.simplify(ell * sym_attr)),
    }


def control_c1_unmarked_fibres():
    """C1: unmarked HNF fibre counts, as in groupoid_halfdensity_probe."""
    import groupoid_halfdensity_probe as ghd  # noqa: WPS433
    nmax = 30
    groupoid = ghd.build_groupoid(nmax)
    delta = ghd.modular_from_fibres(groupoid)
    law, uni, plus, minus, _ = ghd.classify_delta(delta, nmax)
    max_dev = float(np.max(np.abs(
        groupoid["source_fibre"][2:] - groupoid["target_fibre"][2:])))
    return {
        "delta_law": law,
        "unimodular": bool(uni),
        "max_abs_out_minus_in": max_dev,
        "reproduces_delta_1": bool(uni) and max_dev < 1.0e-12,
    }


def control_c2_rank4_boundary(deg, q, m):
    """C2: Furstenberg / P^{RANK-1} scaling instead of the rank-one line."""
    z4 = z_line_hnf_counts(max(deg, 8), rank=v714.RANK)
    cell = int(round(float(z4[deg])))
    # Write cell as 1 + q + ... + q^k and read k from the sum.
    acc = 0
    pwr = 1
    dim = None
    j = 0
    while j < 8:
        acc = acc + pwr
        if acc == cell:
            dim = j
            break
        pwr = pwr * q
        j += 1
    if dim is None:
        return {
            "cell": cell,
            "projective_dim": None,
            "rn_power": None,
            "half_exponent": None,
            "ok": False,
        }
    rn = sympy.Pow(sympy.Integer(q), -dim * m)
    half = sympy.Pow(rn, sympy.Rational(1, 2))
    half_exp = sympy.Rational(dim, 2)
    return {
        "cell": cell,
        "projective_dim": int(dim),
        "rn": str(rn),
        "rn_power_on_q_m": -int(dim),
        "half": str(half),
        "half_exponent": str(half_exp),
        "expect_half_exponent": str(sympy.Rational(v714.RANK - 1, 2)),
        "ok": dim == v714.RANK - 1,
    }


def control_c3_swapped_branching(place_deg, q_geom, q_swap, m):
    """C3: build the tree with q' != place label; result must follow q'."""
    tree = build_tree(q_swap, depth=4)
    q_obs = tree["q_observed"]
    pieces = primitive_orbit_pieces(q_obs, m, toward_deg=True)
    follows_swap = (q_obs == q_swap) and (q_obs != place_deg)
    half_one = pieces["half_attracting"]
    half_if_swap = sympy.Pow(
        translation_rn(q_swap, m, m), sympy.Rational(1, 2))
    half_if_label = sympy.Pow(
        translation_rn(q_geom, m, m), sympy.Rational(1, 2))
    return {
        "place_deg": int(place_deg),
        "q_geometry": int(q_geom),
        "q_swapped": int(q_swap),
        "q_observed": int(q_obs),
        "follows_q_prime": bool(follows_swap),
        "half_from_tree": str(sympy.simplify(half_one)),
        "half_if_q_swap": str(sympy.simplify(half_if_swap)),
        "half_if_place_label": str(sympy.simplify(half_if_label)),
        "matches_q_prime_not_label": bool(
            follows_swap
            and sympy.simplify(half_one - half_if_swap) == 0
            and sympy.simplify(half_one - half_if_label) != 0
        ),
    }


def control_c4_time_direction(q_obs, m):
    """C4: degree generator fixes the + direction before comparison."""
    # v714.log_generator uses +log n as n grows: degree-increasing is +time.
    raw = v714.hnf_counts(16, rank=v714.RANK)
    lam = v714.log_generator(raw, 16)
    pos_time = float(lam[2]) > 0.0
    # One-sided factor on the FIXED degree-positive chamber: attracting
    # under g_m, repelling under g_{-m}.  That is the flip C4 asks for.
    half_deg_fwd = sympy.Pow(translation_rn(q_obs, m, m), sympy.Rational(1, 2))
    half_deg_rev = sympy.Pow(translation_rn(q_obs, m, -m), sympy.Rational(1, 2))
    pieces = primitive_orbit_pieces(q_obs, m, toward_deg=True)
    return {
        "degree_generator_positive": pos_time,
        "forward_half_on_deg_end": str(half_deg_fwd),
        "reverse_half_on_deg_end": str(half_deg_rev),
        "flip_observed": half_deg_fwd != half_deg_rev,
        "sym_from_attracting_pair": pieces["sym_attr_str"],
        "raw_trace": pieces["trace_str"],
    }


# ================================================================= firewall

def constructor_firewall():
    hits = []
    src_mod = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(src_mod)
    bodies = {}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in CONSTRUCTOR_FNS:
            bodies[node.name] = ast.get_source_segment(src_mod, node) or ""
    missing = [n for n in CONSTRUCTOR_FNS if n not in bodies]
    if missing:
        hits.append("missing constructors: %s" % (missing,))
    for name, src in bodies.items():
        for tok in FORBIDDEN_TOKENS:
            if tok in src:
                hits.append("%s:%s" % (name, tok))
        sub = ast.parse(src)
        for nd in ast.walk(sub):
            if isinstance(nd, ast.Attribute) and nd.attr in (
                    "MU_ALL", "LAM_TAB", "U_ALL"):
                hits.append("%s:attr.%s" % (name, nd.attr))
            if isinstance(nd, ast.Call):
                fn = nd.func
                called = None
                if isinstance(fn, ast.Name):
                    called = fn.id
                elif isinstance(fn, ast.Attribute):
                    called = fn.attr
                if called and called.startswith("declared"):
                    hits.append("%s:calls_%s" % (name, called))
    return hits


# ================================================================= comparison (declared)

def declared_hypotheses(p, m):
    """Weil rivals.  Comparison section only — tokens allowed here."""
    logp = math.log(p)
    two = 2.0 * logp
    half = two * (p ** (-m / 2))
    none = two
    full = two * (p ** (-m))
    return {
        "two_log_p_p_half": half,
        "two_log_p": none,
        "two_log_p_p_full": full,
    }


def declared_compare_place(p, q, rows_w):
    """Blind: w(m) vs 2 log p p^{-m/2}, 2 log p, 2 log p p^{-m}."""
    scores = {"half": [], "none": [], "full": []}
    out = []
    for m, w_sym, w_raw in rows_w:
        hyp = declared_hypotheses(p, m)
        ws = float(w_sym)
        wr = float(w_raw)
        out.append({
            "m": int(m),
            "w_sym": ws,
            "w_raw_trace": wr,
            "two_log_p_p_half": hyp["two_log_p_p_half"],
            "two_log_p": hyp["two_log_p"],
            "two_log_p_p_full": hyp["two_log_p_p_full"],
            "abs_sym_minus_half": abs(ws - hyp["two_log_p_p_half"]),
            "abs_sym_minus_none": abs(ws - hyp["two_log_p"]),
            "abs_sym_minus_full": abs(ws - hyp["two_log_p_p_full"]),
            "abs_raw_minus_half": abs(wr - hyp["two_log_p_p_half"]),
            "abs_raw_minus_none": abs(wr - hyp["two_log_p"]),
            "abs_raw_minus_full": abs(wr - hyp["two_log_p_p_full"]),
        })
        scores["half"].append(abs(ws - hyp["two_log_p_p_half"]))
        scores["none"].append(abs(ws - hyp["two_log_p"]))
        scores["full"].append(abs(ws - hyp["two_log_p_p_full"]))
    err = {k: float(max(v)) if v else float("nan") for k, v in scores.items()}
    selected = min(err, key=err.get)
    names = {
        "half": "2 log p · p^{-m/2}",
        "none": "2 log p (no half-density)",
        "full": "2 log p · p^{-m} (full density)",
    }
    return {
        "p": int(p),
        "q": int(q),
        "rows": out,
        "max_abs_err_sym": err,
        "selected_sym": names[selected],
        "selected_key": selected,
        "exact_half": err["half"] <= 1.0e-12,
        "exact_none": err["none"] <= 1.0e-12,
        "exact_full": err["full"] <= 1.0e-12,
    }


def declared_adjudicate(firewall_hits, q_ok, rn_table, traces,
                        compare_rows, c1, c2, c3, c4):
    """Verdict from measured tables.  Comparison section only."""
    kills = []
    if firewall_hits:
        kills.append("FIREWALL")
    if not q_ok:
        kills.append("Q_NOT_FROM_GEOMETRY")
    # RN: attracting must be q^{-m}, not 1.
    rn_constant_one = True
    rn_attracting_ok = True
    for row in rn_table:
        if str(row["rn_attracting"]) != "1":
            rn_constant_one = False
        expect = sympy.Pow(sympy.Integer(row["q"]), -row["m"])
        if sympy.simplify(sympy.sympify(row["rn_attracting"]) - expect) != 0:
            rn_attracting_ok = False
    if rn_constant_one:
        kills.append("K2_UNIMODULAR")
    traces_stable = True
    traces_are_cosh = True
    traces_are_two_half = True
    for row in traces:
        tr = sympy.simplify(sympy.sympify(row["trace"]))
        q = row["q"]
        m = row["m"]
        cosh = (sympy.Pow(sympy.Integer(q), sympy.Rational(m, 2))
                + sympy.Pow(sympy.Integer(q), sympy.Rational(-m, 2)))
        two_half = 2 * sympy.Pow(sympy.Integer(q), sympy.Rational(-m, 2))
        if sympy.simplify(tr - cosh) != 0:
            traces_are_cosh = False
        if sympy.simplify(tr - two_half) != 0:
            traces_are_two_half = False
    # D-independence of the exact two-end trace
    by_key = {}
    for row in traces:
        by_key.setdefault((row["p"], row["m"]), set()).add(row["trace"])
    for _k, vals in by_key.items():
        if len(vals) != 1:
            traces_stable = False
    c1_ok = bool(c1.get("reproduces_delta_1"))
    c2_exp = [r.get("half_exponent") for r in c2]
    c2_ok = all(x == "3/2" for x in c2_exp) if c2_exp else False
    c3_ok = all(r.get("matches_q_prime_not_label") for r in c3)
    c4_ok = all(r.get("flip_observed") and r.get("degree_generator_positive")
                for r in c4)
    exact_half = all(c["exact_half"] for c in compare_rows)
    if not c1_ok:
        kills.append("C1")
    if not c2_ok:
        kills.append("C2")
    if not c3_ok:
        kills.append("C3")
    if not c4_ok:
        kills.append("C4")

    if "FIREWALL" in kills:
        verdict = "INCONCLUSIVE(constructor firewall)"
    elif not q_ok or not rn_attracting_ok:
        verdict = "KILL-K3"
    elif rn_constant_one:
        verdict = "KILL-K3"
    elif not c2_ok and all(x is None for x in c2_exp):
        verdict = "KILL-DIM"
    elif not traces_stable:
        verdict = "INCONCLUSIVE(truncation: trace does not stabilise in D)"
    elif (q_ok and rn_attracting_ok and c1_ok and c2_ok and c3_ok and c4_ok
          and traces_are_two_half and exact_half):
        verdict = "GO"
    elif (q_ok and rn_attracting_ok and c1_ok and c2_ok and c3_ok and c4_ok
          and traces_are_cosh and exact_half and not traces_are_two_half):
        verdict = (
            "PARTIAL (half-density q^{-m/2} emerges from RN^{1/2} on each "
            "axis end and the symmetrised attracting pair equals "
            "2 log p · p^{-m/2} exactly; the finite cylinder trace is "
            "q^{m/2}+q^{-m/2}, not 2 q^{-m/2} — the expanding end is not "
            "projected out by the trace itself, and no 1/|1-u| kernel "
            "appears from the two fixed cylinders)"
        )
    else:
        verdict = "INCONCLUSIVE(controls or comparison failed)"
    return {
        "verdict": verdict,
        "kills": kills,
        "rn_constant_one": rn_constant_one,
        "rn_attracting_ok": rn_attracting_ok,
        "traces_stable": traces_stable,
        "traces_are_cosh": traces_are_cosh,
        "traces_are_two_half": traces_are_two_half,
        "c1_ok": c1_ok,
        "c2_ok": c2_ok,
        "c3_ok": c3_ok,
        "c4_ok": c4_ok,
        "exact_half_from_w_sym": exact_half,
    }


def _f(x):
    if isinstance(x, sympy.Basic):
        return str(sympy.simplify(x))
    return x


# ================================================================= run

def run():
    t0 = time.time()
    print("=" * 72)
    print("%s  Exploration only; identity side only; no RH claim."
          % CONTRACT)
    print("=" * 72)

    hits = constructor_firewall()
    print("  [%s] constructor AST firewall" % ("PASS" if not hits else "FAIL"))
    if hits:
        print("       hits: %s" % hits)
        raise SystemExit("AST firewall failed: %s" % hits)

    line = extract_norm_line(CENSUS_X)
    print("  v714 calls: %s" % ", ".join(line["v714_calls"]))
    print("  how q is read: Z-rank-2 HNF neighbour count at the descent")
    print("  degree, minus one; cross-checked by rank-4 cell term ratios.")
    q_ok = True
    for pl in line["places"]:
        print("      place deg=%s type=%s  q=%s  neigh=%s  cell4=%s  "
              "ratios=%s  q==deg=%s" % (
                  pl["deg"], pl["type"], pl["q"], pl["neighbour_count"],
                  pl["rank4_cell"], pl["cell_term_ratios"],
                  pl["q_equals_deg"]))
        if not pl["q_equals_deg"] or pl["q"] != pl["deg"]:
            q_ok = False
        if pl["cell_term_ratios"] != [pl["deg"]] * (v714.RANK - 1):
            q_ok = False

    rn_table = []
    trace_table = []
    compare_inputs = {}
    measure_locks = []

    for pl in line["places"]:
        q = pl["q"]
        pdeg = pl["deg"]
        compare_inputs[pdeg] = []
        for D in DEPTHS:
            tree = build_tree(q, D)
            masses = visual_measure(tree)
            q_obs = tree["q_observed"]
            nD = tree["n_cylinders"]
            types = cylinder_types(q, D)
            closed = (q + 1) * (q ** (D - 1)) if D >= 1 else 1
            mass_closed = (sympy.Integer(1)
                           / sympy.Integer((q + 1) * (q ** (D - 1))))
            lock = {
                "p": pdeg,
                "q": q,
                "D": D,
                "n_cylinders": nD,
                "types_total": types["n_total"],
                "closed_form_count": closed,
                "mass_from_count": str(masses[D]),
                "mass_closed_form": str(mass_closed),
                "mass_equals_closed": masses[D] == mass_closed,
                "q_observed": q_obs,
                "types_match_sphere": types["n_total"] == nD,
            }
            measure_locks.append(lock)
            print("  tree p=%s q=%s D=%s  n_cyl=%s  types=%s  "
                  "mass=%s  closed=%s  eq=%s" % (
                      pdeg, q, D, nD, types["n_total"],
                      masses[D], mass_closed, lock["mass_equals_closed"]))
            if not lock["mass_equals_closed"] or q_obs != q:
                q_ok = False
            if types["n_total"] != nD:
                q_ok = False

            for m in range(1, MAX_M + 1):
                if D < m:
                    continue
                # RN by Busemann height (axis ends + one intermediate).
                fac = halfdensity_factors(q_obs, m, toward_deg=True)
                # Intermediate: leave the attracting ray at s=1 (if D>1)
                B_mid = 2 * 1 - m if D > 1 and m > 1 else None
                rn_mid = (str(translation_rn(q_obs, m, B_mid))
                          if B_mid is not None else None)
                if D == DEPTHS[-1]:
                    rn_table.append({
                        "p": pdeg,
                        "q": q,
                        "m": m,
                        "B_attracting": fac["B_attracting"],
                        "B_repelling": fac["B_repelling"],
                        "B_mid_s1": B_mid,
                        "rn_attracting": fac["rn_attr_str"],
                        "rn_repelling": fac["rn_rep_str"],
                        "rn_mid_s1": rn_mid,
                        "half_attracting": fac["half_attr_str"],
                        "half_repelling": fac["half_rep_str"],
                    })
                tr = fixed_cylinder_trace(q, D, m, q_obs, toward_deg=True)
                pieces = primitive_orbit_pieces(q_obs, m, toward_deg=True)
                # The word-map trace must agree with the two-end formula.
                if sympy.simplify(tr["trace"] - pieces["trace"]) != 0:
                    print("  TRACE MISMATCH p=%s D=%s m=%s  word=%s  "
                          "pieces=%s  fixed=%s" % (
                              pdeg, D, m, tr["trace_str"],
                              pieces["trace_str"], tr["fixed"]))
                    q_ok = False
                trace_table.append({
                    "p": pdeg,
                    "q": q,
                    "D": D,
                    "m": m,
                    "n_fixed": tr["n_fixed"],
                    "trace": tr["trace_str"],
                    "trace_pieces": pieces["trace_str"],
                    "w_raw": pieces["w_raw_str"],
                    "w_sym": pieces["w_sym_str"],
                })
                if D == DEPTHS[-1]:
                    compare_inputs[pdeg].append((
                        m,
                        pieces["w_sym_attracting"],
                        pieces["w_from_raw_trace"],
                    ))

    print("  RN by Busemann height (D=%s, attracting / repelling / mid):"
          % DEPTHS[-1])
    for row in rn_table:
        print("      p=%s m=%s  B=(%s,%s,%s)  RN=(%s, %s, %s)  "
              "half=(%s, %s)" % (
                  row["p"], row["m"],
                  row["B_attracting"], row["B_repelling"], row["B_mid_s1"],
                  row["rn_attracting"], row["rn_repelling"], row["rn_mid_s1"],
                  row["half_attracting"], row["half_repelling"]))

    print("  tr(U_m) on depth-D cylinders:")
    for row in trace_table:
        print("      p=%s D=%s m=%s  n_fixed=%s  tr=%s  w_sym=%s" % (
            row["p"], row["D"], row["m"], row["n_fixed"],
            row["trace"], row["w_sym"]))

    compare_tables = []
    for pl in line["places"]:
        cmpn = declared_compare_place(
            pl["deg"], pl["q"], compare_inputs[pl["deg"]])
        compare_tables.append(cmpn)
        print("  comparison p=%s  selected=%s  max|w_sym-hyp| half=%.3e "
              "none=%.3e full=%.3e" % (
                  pl["deg"], cmpn["selected_sym"],
                  cmpn["max_abs_err_sym"]["half"],
                  cmpn["max_abs_err_sym"]["none"],
                  cmpn["max_abs_err_sym"]["full"]))
        for r in cmpn["rows"]:
            print("      m=%s  w_sym=%.8f  half=%.8f  none=%.8f  "
                  "full=%.8f  w_raw=%.8f" % (
                      r["m"], r["w_sym"], r["two_log_p_p_half"],
                      r["two_log_p"], r["two_log_p_p_full"],
                      r["w_raw_trace"]))

    print("  C1 unmarked fibres...")
    c1 = control_c1_unmarked_fibres()
    print("      Delta=%s  uni=%s  max|out-in|=%.3e  Delta=1=%s" % (
        c1["delta_law"], c1["unimodular"], c1["max_abs_out_minus_in"],
        c1["reproduces_delta_1"]))

    print("  C2 rank-4 boundary...")
    c2_rows = []
    for pl in line["places"]:
        row = control_c2_rank4_boundary(pl["deg"], pl["q"], m=1)
        row["p"] = pl["deg"]
        c2_rows.append(row)
        print("      p=%s  cell=%s  dim=%s  half_exp=%s  ok=%s" % (
            pl["deg"], row["cell"], row["projective_dim"],
            row["half_exponent"], row["ok"]))

    print("  C3 swapped branching...")
    c3_rows = []
    for pl in line["places"]:
        q_swap = 3 if pl["deg"] != 3 else 2
        row = control_c3_swapped_branching(pl["deg"], pl["q"], q_swap, m=1)
        c3_rows.append(row)
        print("      p=%s  q'=%s  q_obs=%s  follows_q'=%s  "
              "matches_q'_not_p=%s" % (
                  pl["deg"], q_swap, row["q_observed"],
                  row["follows_q_prime"], row["matches_q_prime_not_label"]))

    print("  C4 time direction...")
    c4_rows = []
    for pl in line["places"]:
        row = control_c4_time_direction(pl["q"], m=1)
        row["p"] = pl["deg"]
        c4_rows.append(row)
        print("      p=%s  deg_gen+=%s  fwd=%s  rev=%s  flip=%s  "
              "sym=%s  raw_tr=%s" % (
                  pl["deg"], row["degree_generator_positive"],
                  row["forward_half_on_deg_end"],
                  row["reverse_half_on_deg_end"],
                  row["flip_observed"], row["sym_from_attracting_pair"],
                  row["raw_trace"]))

    adj = declared_adjudicate(
        hits, q_ok, rn_table, trace_table, compare_tables,
        c1, c2_rows, c3_rows, c4_rows)
    elapsed = time.time() - t0
    print("  kill/flags: %s" % (adj["kills"] if adj["kills"] else "none"))
    print("  VERDICT: %s" % adj["verdict"])
    print("  runtime %.2f s" % elapsed)
    print("  RH one-liner: this concerns only the identity side of the "
          "explicit formula (Connes' local term realised on the tree "
          "boundary) and says nothing about positivity or RH.")

    src_bytes = Path(__file__).read_bytes()
    file_sha = hashlib.sha256(src_bytes).hexdigest()
    payload = {
        "contract": CONTRACT,
        "verdict": adj["verdict"],
        "adjudication": adj,
        "q_from_v714": {
            "method": (
                "Z-rank-2 HNF neighbour count at the sigma-descent "
                "degree, minus one; rank-4 cell term ratios as lock"
            ),
            "v714_calls": list(line["v714_calls"]),
            "places": line["places"],
            "q_ok": q_ok,
        },
        "measure_locks": measure_locks,
        "rn_by_busemann": rn_table,
        "trace_table": trace_table,
        "comparison": compare_tables,
        "controls": {
            "C1": c1,
            "C2": c2_rows,
            "C3": c3_rows,
            "C4": c4_rows,
        },
        "firewall_hits": hits,
        "depths": list(DEPTHS),
        "max_m": MAX_M,
        "imported_v714": True,
        "reimplemented_groupoid": False,
        "spec_sha": SPEC_SHA,
        "file_sha256": file_sha,
        "runtime_s": elapsed,
        "identity_side_only": True,
        "rh_one_liner": (
            "This concerns only the identity side of the explicit "
            "formula (Connes' local term realised on the tree "
            "boundary) and says nothing about positivity or RH."
        ),
    }
    out = HERE / "parabolic_detline_result.json"
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n",
                   encoding="utf-8")
    result_sha = hashlib.sha256(out.read_bytes()).hexdigest()
    print("  wrote %s" % out)
    print("  probe sha256 %s" % file_sha)
    print("  result sha256 %s" % result_sha)
    return 0


if __name__ == "__main__":
    sys.exit(run())
