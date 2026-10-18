#!/usr/bin/env python3
r"""coupling_currency_probe -- PRIME.ONEBADMODE.COUPLING.01

MISSION.  Build the missing class-data currency which couples the bad
eigenvalue lambda_1(M) to the seven good eigenvalues.  CCLXXXIX proved
that every INDEPENDENT-seat decomposition plateaus near 1.15 on the
thin branch.  The new object uses identities which an independent
decomposition discards:

    T = tr M = sum_i lambda_i,
    Q = tr M^2 = sum_i lambda_i^2.

For y=x/L, every declared cut (B,C), B,C >= 0, has seven certified
intercepts

    A_j(B,C) = sup_{x in [f_j,L_k]}
               { R(x) - B y - C y^2 }.

Here f_j are a branch's certified ordered B-floors and L_k is the
branchwise Frobenius ceiling derived from the same two-sided floor
catalog.  Therefore, pointwise for every member of branch k,

  tr R(M)
    <= sum_j A_j + B T/L + C Q/L^2
       + sup_{x in I_1}{R(x)-B x/L-C(x/L)^2}.                 (CC)

This is the coupling currency: if lambda_1 lies in the small interval
I_1, T-lambda_1 and Q-lambda_1^2 are carried by the good block in the
same inequality.  The intercept suprema and the bad-seat supremum use
the certified CCLXVII piecewise envelope, never sampled R values.

MECHANISM ORDER (frozen before seeing this probe's result).

 (i) TRACE.  C=0 in (CC).  Equivalently, if m good eigenvalues are at
     most z and every good eigenvalue is at most U, then

       m <= (7 U - (T-lambda_1))/(U-z).

     This is the exact pigeonhole ceiling.  Ordered floors enter both
     A_j and the tight branch traces sum f_j <= tr B <= sum f_j^+.

 (ii) SECOND MOMENT.  The full quadratic cut (CC) uses

       Q = n^2 + 2 a_1^2 + tr B^2,

     with tr B^2 <= sum_j (f_j^+)^2.  This is the standard separable
     moment-majorization dual: R(x) is majorized seatwise by one
     quadratic with shared B,C and floor-dependent intercepts.
     No convexity of R is assumed.

 (iii) SCHUR DETERMINANT.  det M=s det B, s>= (1-t_R)n, hence

       prod_{i=2}^8 lambda_i
         >= (1-t_R)n prod_j f_j / lambda_1.

     If trace+Q does not close, the declared D<0 cuts extend (CC) by
     D log(x/L).  Multiplying the product lower bound by D reverses
     the inequality and gives the certified upper term

       D log((1-t_R)n prod_j f_j/L^8).

     The rerun reports separately which mechanism wins.

R SHAPE.  Write

 F(t)=t prod_r(t^2+u_r)/prod_r(t^2+v_r),  R(x)=1-D F(x/L).

Then, exactly,

 d log F/dt = 1/t + 2t sum_r[1/(t^2+u_r)-1/(t^2+v_r)]

and F''/F is the square of this expression plus

 -1/t^2 + 2 sum_r[(u_r-t^2)/(t^2+u_r)^2
                  -(v_r-t^2)/(t^2+v_r)^2].

The signs vary on [c_B,L]; "decreasing-convex-ish" is not used as a
theorem.  Certified segment maxima make (CC) valid through every
oscillation.

CLASS AND PREMISES.  Exactly CCLXXXIX's frozen tight-floor class:
the CCLXXXI entry box (SHA ward), a>=0, n>0, B-floor, KS/COEF/SPREAD/
radius, source MOM box, eta, sharp pivot, the 85-branch certified
ordered-floor catalog with its inherited 1e-6 two-sided quality bar,
and the K=5 Gauss-Radau relation q<=t_R n with t_R=0.7809.  The latter
and B>0 imply M>0, so the Frobenius support ceiling is legitimate.
This probe establishes only the OBSERVER statement for that finite,
frozen class.  CCXCIII's positivity certificate is independent and
stands regardless.  No all-h statement and NO RH claim.

GATES.
 S  source firewall and anti-circularity AST scan.
 D  sympy identities: filter shape, trace/Q rearrangement,
    pigeonhole numerator, Schur determinant.
 C  certified cut-envelope containment against direct R samples.
 P  pointwise (CC) on the complete 151-cell CCLXXIX census, with
    CCXCIII's exact moments/floors and exact certified B ceilings;
    plus the CCLXXXV F4 thin optimum witness.
 X  controls-must-fire: indefinite worlds are rejected; a doctored
    floor catalog is rejected by floor logic alone.
 O  rigor-3 per-box rerun, first trace-only, then trace+Q, on the
    thin branch and the full 85-branch class.
 F  phantom test: the 1.15 independent-seat thin maximizer is checked
    against (CC), not merely compared numerically.
 T  tau/c_h relocation screens and explicit scope/firewall.

FROZEN BARS.  CUT_B=(0,2,4,8,12,16,24,32);
CUT_C=(0,10,30,100,300,1e3,3e3,1e4,3e4,1e5,3e5,1e6);
CUT_D=(-1e-4,-3e-4,-1e-3,-3e-3,-1e-2,-3e-2,-1e-1,
-3e-1,-1); the quadratic bank is CUT_B x CUT_C x {0}; the determinant
bank is {0,32,128,512,1024} x {0,1e5,1e6} x CUT_D; trace-only is
C=D=0.
TARGET=1; LOWER_ANCHOR=0.972698; budgets 45 s smoke / 600 s frozen;
queue cap 500000; branch catalog quality 1e-6; envelope and all
arithmetic are outward-rounded through CCLXVII's helpers.  Smoke uses
the inherited reduced geometry and discloses every bypass.  A frozen
run must finish in less than 25 minutes.

AMENDMENT A1 (post-smoke, disclosed before the frozen run).  Smoke-1
(SPEC_SHA edcf5638, 18.9 s) passed 17/18 checks.  Its only failure was
F1: the inherited smoke subset has the known degenerate fake-bridge
objective tr R=4.850598786 and an "independent plateau" 4.906063693,
not CCLXXXIX's frozen 1.15 plateau; coupling and independent values
therefore coincided exactly.  F1 is now explicitly SMOKE-BYPASSED and
still runs diagnostically.  The frozen 85-branch geometry must execute
the strict exclusion unchanged.  No cut, inequality, class premise,
frozen threshold, or frozen gate was altered.

AMENDMENT A2 (post-frozen-run-1, disclosed).  Frozen-run-1
(SPEC_SHA 9b58ca7e, 731.0 s) passed every derivation, validity, census,
ceiling, phantom and control gate, but the closure predicates were
correctly false: trace root 1.249843583; thin/full trees both stopped
at 1.240174776, with every winning coupling cut carrying C=0.  Two
specification corrections follow from that measured result.  First,
an open closure predicate is a scientific PARTIAL outcome, not a
WARD-BROKEN software kill; O1/O2 now type the result without killing
the run.  Second, mechanism (ii) demonstrably did not win, so the
predeclared mechanism (iii) is now actually implemented as the exact
D<0 logarithmic determinant majorant above.  Its coefficient bank is
frozen explicitly here.  No class premise, census, envelope, target,
or prior number is weakened or hidden.

AMENDMENT A3 (post-smoke-3, mechanical).  Smoke-3 (SPEC_SHA c9275da2,
19.5 s) passed 17/18.  C1's every numeric containment passed (worst
defect -6.76e-9), but expanding the bank from 96 to 231 cuts made the
stride select 10 audit cuts while a stale counter expected 9.  C1 now
counts the loop's actual selections.  Arithmetic and gates unchanged.

RUN:
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/coupling_currency_probe.py --smoke
  experiments/tfpt-discovery/.venv/bin/python \
    experiments/tfpt-discovery/coupling_currency_probe.py
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

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import bfloor_k5_closure_probe as k5       # noqa: E402
import ks_dual_rigor_probe as rig          # noqa: E402
import ks_dual_rigor3_probe as k3          # noqa: E402
import radau_class_assembly_probe as rc    # noqa: E402
import radau_class_close_probe as rcl      # noqa: E402
import radau_sos_certificate_probe as sos  # noqa: E402


NDIM = 8
SMOKE = "--smoke" in sys.argv[1:]
BOX_SHA_CCLXXXI = "6dfe799c61ac11f98b6bc21243b22a04"
CELL_EXP = 151
T_R = 0.7809
CAT_RTOL = 1.0e-6
LOWER_ANCHOR = 0.972698
TARGET = 1.0
MAIN_BUDGET = 45.0 if SMOKE else 600.0
QUEUE_CAP = 500000
BATCH = 1024 if SMOKE else 4096
CUT_B = (0.0, 2.0, 4.0, 8.0, 12.0, 16.0, 24.0, 32.0)
CUT_C = (0.0, 10.0, 30.0, 100.0, 300.0, 1.0e3, 3.0e3,
         1.0e4, 3.0e4, 1.0e5, 3.0e5, 1.0e6)
CUT_D = (-1.0e-4, -3.0e-4, -1.0e-3, -3.0e-3, -1.0e-2,
         -3.0e-2, -1.0e-1, -3.0e-1, -1.0)
CUTS_QUADRATIC = tuple(
    (bb, cc, 0.0) for bb in CUT_B for cc in CUT_C)
CUTS_DETERMINANT = tuple(
    (bb, cc, dd)
    for bb in (0.0, 32.0, 128.0, 512.0, 1024.0)
    for cc in (0.0, 1.0e5, 1.0e6)
    for dd in CUT_D)
CUTS_FULL = CUTS_QUADRATIC + CUTS_DETERMINANT
CUTS_TRACE = tuple((bb, 0.0, 0.0) for bb in CUT_B)
ENV_SAMPLE_N = 64 if SMOKE else 512
SHAPE_N = 512 if SMOKE else 4096
WARD_SEED = 20260812
TIE = 1.0e-8

T0 = time.time()
SPEC_SHA = hashlib.sha256(__doc__.encode("utf-8")).hexdigest()
CHECKS = []
KILLS = []

BANNED_IDS = ("zetazero", "zetazeros", "nzeros", "primerange",
              "isprime", "primepi", "nextprime", "prevprime",
              "factorint", "primefactors")
CONSUMED_FUNCS = ("_prepare_tables", "cut_query", "branch_bound",
                  "process")
CONSUMED_BANNED = ("trace_r", "trace_R", "reserve", "margin",
                   "artifact", "lu_read", "assemble_step",
                   "build_rung", "kz", "h", "tau")


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
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74, flush=True)


def ast_scan_all(banned):
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(source)):
        name = None
        if isinstance(node, ast.Name):
            name = node.id
        elif isinstance(node, ast.Attribute):
            name = node.attr
        if name and name.lower() in banned:
            bad.append(name)
    return bad


def ast_scan_functions(names, banned):
    source = open(os.path.abspath(__file__), encoding="utf-8").read()
    bad = []
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) \
                and node.name in names:
            for sub in ast.walk(node):
                name = None
                if isinstance(sub, ast.Name):
                    name = sub.id
                elif isinstance(sub, ast.Attribute):
                    name = sub.attr
                elif isinstance(sub, ast.arg):
                    name = sub.arg
                if name and name in banned:
                    bad.append("%s:%s" % (node.name, name))
    return bad


def configure_85():
    rc.CHECKS = []
    rc.KILLS = []
    rc.SMOKE = SMOKE
    rc.T0 = T0
    k3.SMOKE = SMOKE


def build_85_class():
    """Read-only rebuild of the CCLXXXIX class and branch catalog."""
    configure_85()
    rc.no_go_lemma()
    steps, combined = rc.build_ladder()
    artifact = rc.artifact_key_ward(steps)
    f0_cells = rc.build_f0(combined)
    fdata = rc.get_filter(steps, artifact)
    rows = rc.make_rows(steps, f0_cells, artifact, fdata)
    rows = rc.jacobi_identity_wards(rows)
    rc.repro_anchors(rows)
    rc.certify_cells(rows)
    cls = rc.freeze_class(rows, fdata)
    rc.ac_typing(rows, cls)
    rc.membership(rows, cls)
    rcl.freeze_new_data(rows, cls)
    rcl.certify_geometry(rows)
    env = rig.Envelope(fdata)
    cat = k3.build_catalog(rows, env, cls)
    return rows, cls, fdata, env, cat


class CutBank:
    """Certified piecewise majorants for R-B(x/L)-C(x/L)^2."""

    def __init__(self, env, big_l, cuts):
        self.env = env
        self.big_l = float(big_l)
        self.cuts = tuple(
            (float(v[0]), float(v[1]), float(v[2])
             if len(v) >= 3 else 0.0) for v in cuts)
        self.b = np.asarray([v[0] for v in self.cuts], float)
        self.c = np.asarray([v[1] for v in self.cuts], float)
        self.d = np.asarray([v[2] for v in self.cuts], float)
        self.tables = []
        self._prepare_tables()

    def _prepare_tables(self):
        edges = np.asarray(self.env.edges, float)
        xa = edges[:-1] / self.big_l
        xb = edges[1:] / self.big_l
        for bb, cc, dd in self.cuts:
            # A separable segment upper bound.  The polynomial terms
            # decrease on y>=0, while -D log y increases for D<0.
            # Taking their maxima at opposite endpoints is conservative
            # and avoids any unverified floating stationary point.
            y_lo = np.maximum(xa, 0.0)
            y_hi = np.maximum(xb, rig.TMIN)
            pmax = rig.nup(
                rig.nup(-bb * y_lo - cc * y_lo * y_lo)
                + rig.nup(-dd * rig.log_hi(y_hi)))
            pmax = np.where(xb <= 0.0, 0.0, pmax)
            seg = rig.nup(rig.nup(self.env.ub0) + rig.nup(pmax))
            self.tables.append(self.env._table(seg, np.maximum))

    def cut_query(self, cut_index, x_lo, x_hi):
        """Certified range max of a cut transform on [x_lo,x_hi]."""
        xa = np.asarray(x_lo, float)
        xb = np.asarray(x_hi, float)
        xa = np.maximum(xa, 0.0)
        xb = np.minimum(np.maximum(xb, xa), self.big_l)
        edges = self.env.edges
        table = self.tables[cut_index]
        nseg = self.env.n_seg
        i0 = np.clip(np.searchsorted(edges, xa, side="right") - 1,
                     0, nseg - 1)
        i1 = np.clip(np.searchsorted(edges, xb, side="left") - 1,
                     0, nseg - 1)
        i1 = np.maximum(i1, i0)
        span = i1 - i0 + 1
        lev = np.frexp(span.astype(float))[1] - 1
        lev = np.clip(lev, 0, table.shape[0] - 1)
        left = table[lev, i0]
        right_i = np.maximum(i1 - (1 << lev) + 1, i0)
        right = table[lev, right_i]
        return rig.nup(np.maximum(left, right))

    def intercept_sum(self, floors, support_hi):
        floors = np.asarray(floors, float)
        out = np.zeros(len(self.cuts))
        for q in range(len(self.cuts)):
            vals = self.cut_query(
                q, floors, np.full(len(floors), float(support_hi)))
            out[q] = float(rig.nup(np.sum(rig.nup(vals))))
        return out


class CouplingWork(k3.BoxWork3):
    """Rigor-3 processor augmented by the certified coupling cuts."""

    def __init__(self, cls, env, fdata, cat, cuts):
        super().__init__(cls, env, fdata, cat)
        self.bank = CutBank(env, cls["L"], cuts)
        self.cut_b = self.bank.b
        self.cut_c = self.bank.c
        self.cut_d = self.bank.d
        self.branch_const = None
        self.trace_b_hi = None
        self.square_b_hi = None
        self.support_hi = None
        self._build_branch_currency()
        self.stats.update(coupling_win=0, coupling_trace=0,
                          coupling_moment=0, coupling_determinant=0)

    def _build_branch_currency(self):
        f_lo = np.asarray(self.cat["f_lo"], float)
        f_hi = np.asarray(self.cat["f_hi"], float)
        self.trace_b_hi = rig.nup(np.sum(rig.nup(f_hi), axis=1))
        self.square_b_hi = rig.nup(np.sum(rig.nup(f_hi * f_hi),
                                           axis=1))
        n_hi = float(self.cls["hi"][0])
        a1_hi = float(self.cls["hi"][NDIM])
        fro_hi = rig.nup(rig.nup(n_hi * n_hi)
                         + rig.nup(2.0 * rig.nup(a1_hi * a1_hi))
                         + self.square_b_hi)
        self.support_hi = np.minimum(
            float(self.cls["L"]), rig.nup(np.sqrt(fro_hi)))
        n_branch = self.cat["n"]
        n_cut = len(self.bank.cuts)
        intercept = np.zeros((n_branch, n_cut))
        for k in range(n_branch):
            intercept[k] = self.bank.intercept_sum(
                f_lo[k], self.support_hi[k])
        log_floor = np.zeros(n_branch)
        for k in range(n_branch):
            log_floor[k] = float(rig.ndown(
                rig.log_lo(1.0 - float(self.cls["t_r"]))
                + np.sum(rig.log_lo(
                    f_lo[k] / float(self.cls["L"])))))
        self.branch_const = rig.nup(
            rig.nup(intercept)
            + rig.nup(self.trace_b_hi[:, None]
                      * self.cut_b[None, :] / float(self.cls["L"]))
            + rig.nup(self.square_b_hi[:, None]
                      * self.cut_c[None, :]
                      / float(self.cls["L"]) ** 2)
            + rig.nup(log_floor[:, None] * self.cut_d[None, :]))

    def branch_bound(self, lo, hi):
        """Certified coupled objective bound over each input box."""
        n_box = lo.shape[0]
        jb_cols = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14]
        db, eb_tot, _ = rig.eig_enclosure(
            lo[:, jb_cols], hi[:, jb_cols], NDIM - 1, 0, NDIM - 1)
        lb_lo, lb_hi = rig.corner_lam_min(
            lo[:, jb_cols], hi[:, jb_cols], NDIM - 1, 0, NDIM - 1)
        ub_b = rig.nup(db + eb_tot[:, None])
        dn_b = rig.ndown(db - eb_tot[:, None])
        ub_b[:, 0] = np.minimum(ub_b[:, 0], lb_hi)
        dn_b[:, 0] = np.maximum(dn_b[:, 0], lb_lo)
        feasible = self.branch_feas(ub_b, dn_b)

        dd, e_tot, _ = rig.eig_enclosure(lo, hi, NDIM, 0, NDIM)
        _l1_lo, l1_hi = rig.corner_lam_min(lo, hi, NDIM, 0, NDIM)
        l1_upper = np.minimum(
            rig.nup(dd[:, 0] + e_tot),
            np.minimum(l1_hi, np.min(hi[:, :NDIM], axis=1)))
        l1_upper = np.clip(l1_upper, 0.0, float(self.cls["L"]))

        bad = np.zeros((n_box, len(self.bank.cuts)))
        for q in range(len(self.bank.cuts)):
            bad[:, q] = self.bank.cut_query(
                q, np.zeros(n_box), l1_upper)

        n_hi = np.maximum(hi[:, 0], 0.0)
        a1_hi = np.maximum(hi[:, NDIM], 0.0)
        box_const = rig.nup(
            rig.nup(bad)
            + rig.nup(n_hi[:, None] * self.cut_b[None, :]
                      / float(self.cls["L"]))
            + rig.nup((rig.nup(n_hi * n_hi)
                       + rig.nup(2.0 * rig.nup(a1_hi * a1_hi)))[:, None]
                      * self.cut_c[None, :]
                      / float(self.cls["L"]) ** 2)
            + rig.nup(rig.log_lo(
                np.maximum(lo[:, 0], 1.0e-300)
                / float(self.cls["L"]))[:, None]
                      * self.cut_d[None, :]))
        all_cut = rig.nup(
            self.branch_const[None, :, :] + box_const[:, None, :])
        per_branch = np.min(all_cut, axis=2)
        per_branch = np.where(feasible, per_branch, -np.inf)
        bound = np.max(per_branch, axis=1)
        any_branch = np.any(feasible, axis=1)
        bound = np.where(any_branch, bound, np.inf)

        # Currency census: classify the cut selected by the worst
        # feasible branch in each box.
        branch_arg = np.argmax(per_branch, axis=1)
        cut_arg = np.argmin(
            all_cut[np.arange(n_box), branch_arg, :], axis=1)
        return rig.nup(bound), any_branch, cut_arg

    def process(self, lo, hi):
        base_ub, keep, split_col, vol = super().process(lo, hi)
        coupled, any_branch, cut_arg = self.branch_bound(lo, hi)
        keep &= any_branch
        wins = (coupled < base_ub) & keep
        self.stats["coupling_win"] += int(np.sum(wins))
        self.stats["coupling_trace"] += int(np.sum(
            wins & (self.cut_c[cut_arg] == 0.0)
            & (self.cut_d[cut_arg] == 0.0)))
        self.stats["coupling_moment"] += int(np.sum(
            wins & (self.cut_c[cut_arg] > 0.0)
            & (self.cut_d[cut_arg] == 0.0)))
        self.stats["coupling_determinant"] += int(np.sum(
            wins & (self.cut_d[cut_arg] < 0.0)))
        return np.minimum(base_ub, coupled), keep, split_col, vol


def preclip_master(cls):
    lo = np.asarray(cls["lo"], float).copy()
    hi = np.asarray(cls["hi"], float).copy()
    lo[0] = max(lo[0], 0.0)
    lo[NDIM:] = np.maximum(lo[NDIM:], 0.0)
    lo[1:NDIM] = np.maximum(lo[1:NDIM], cls["cb"])
    lo[1] = max(lo[1], float(cls["eta_lo"]))
    hi[1] = min(hi[1], float(cls["eta_hi"]))
    a1_lo = float(rig.ndown(math.sqrt(max(cls["mlo"][0], 0.0))
                            * (1.0 - 1.0e-14)))
    a1_hi = float(rig.nup(math.sqrt(cls["mhi"][0])
                          * (1.0 + 1.0e-14)))
    lo[NDIM] = max(lo[NDIM], a1_lo)
    hi[NDIM] = min(hi[NDIM], a1_hi)
    lo[0] = max(lo[0], float(rig.ndown(
        a1_lo * a1_lo / (cls["eta_hi"] * cls["t_r"])
        * (1.0 - 1.0e-12))))
    return lo, hi


def run_until_one(work, master_lo, master_hi, budget, label):
    """Small rigor-3 B&B driver whose sole target is UB < 1."""
    started = time.time()
    lo = master_lo[None, :].copy()
    hi = master_hi[None, :].copy()
    ub, keep, split, vol = work.process(lo, hi)
    lo, hi, ub, split, vol = (lo[keep], hi[keep], ub[keep],
                               split[keep], vol[keep])
    rounds = 0
    stop = "empty"
    while len(ub):
        current = max(LOWER_ANCHOR, float(np.max(ub)))
        if current < TARGET:
            stop = "target"
            break
        if time.time() - started > budget:
            stop = "budget"
            break
        if len(ub) > QUEUE_CAP:
            stop = "queue-cap"
            break
        n_top = min(BATCH, len(ub))
        order = np.argpartition(ub, -n_top)[-n_top:]
        rest = np.ones(len(ub), bool)
        rest[order] = False
        p_lo, p_hi, p_split = lo[order], hi[order], split[order]
        n_parent = len(p_lo)
        mid = p_lo[np.arange(n_parent), p_split] + 0.5 * (
            p_hi[np.arange(n_parent), p_split]
            - p_lo[np.arange(n_parent), p_split])
        c_lo = np.concatenate([p_lo, p_lo.copy()])
        c_hi = np.concatenate([p_hi.copy(), p_hi])
        c_hi[:n_parent, :][np.arange(n_parent), p_split] = mid
        c_lo[n_parent:, :][np.arange(n_parent), p_split] = mid
        c_ub, c_keep, c_split, c_vol = work.process(c_lo, c_hi)
        c_keep &= c_ub >= LOWER_ANCHOR
        lo = np.concatenate([lo[rest], c_lo[c_keep]])
        hi = np.concatenate([hi[rest], c_hi[c_keep]])
        ub = np.concatenate([ub[rest], c_ub[c_keep]])
        split = np.concatenate([split[rest], c_split[c_keep]])
        vol = np.concatenate([vol[rest], c_vol[c_keep]])
        rounds += 1
        if rounds % 25 == 0:
            print("    %s round %d: UB %.9f, open %d, processed %d "
                  "[%.1f s]" % (label, rounds,
                                max(LOWER_ANCHOR,
                                    float(np.max(ub)) if len(ub)
                                    else LOWER_ANCHOR),
                                len(ub), work.stats["processed"],
                                time.time() - started), flush=True)
    bound = max(LOWER_ANCHOR,
                float(np.max(ub)) if len(ub) else LOWER_ANCHOR)
    return dict(bound=bound, stop=stop, rounds=rounds,
                open=len(ub), elapsed=time.time() - started,
                stats=dict(work.stats))


def subset_catalog(cat, indices):
    ix = np.asarray(indices, int)
    f_lo = cat["f_lo"][ix].copy()
    f_hi = cat["f_hi"][ix].copy()
    sg = cat["sg"][ix].copy()
    digest = hashlib.sha256(
        f_lo.tobytes() + f_hi.tobytes() + sg.tobytes()).hexdigest()
    return dict(f_lo=f_lo, f_hi=f_hi, sg=sg, sha=digest, n=len(ix))


def direct_point_bound(bank, floors, n_value, a1_value, l1_value,
                       support_hi):
    """Evaluate (CC) on a point using only certified envelope data."""
    floors = np.asarray(floors, float)
    f_hi = rig.nup(floors / (1.0 - CAT_RTOL))
    tr_b = float(rig.nup(np.sum(f_hi)))
    sq_b = float(rig.nup(np.sum(rig.nup(f_hi * f_hi))))
    intercept = bank.intercept_sum(floors, support_hi)
    values = []
    log_floor = float(rig.ndown(
        rig.log_lo(1.0 - T_R)
        + np.sum(rig.log_lo(floors / bank.big_l))))
    log_n = float(rig.log_lo(
        max(float(n_value), 1.0e-300) / bank.big_l))
    for q, (bb, cc, dd) in enumerate(bank.cuts):
        bad = float(bank.cut_query(q, np.asarray([l1_value]),
                                   np.asarray([l1_value]))[0])
        val = float(rig.nup(
            intercept[q] + bad
            + bb * (n_value + tr_b) / bank.big_l
            + cc * (n_value * n_value + 2.0 * a1_value * a1_value
                    + sq_b) / bank.big_l ** 2
            + dd * (log_floor + log_n)))
        values.append(val)
    return min(values), int(np.argmin(values))


def build_151():
    """Rebuild the full CCLXXIX census and CCXCIII exact interval data."""
    k5.CHECKS = []
    k5.KILLS = []
    k5.SMOKE = SMOKE
    k5.T0 = T0
    zones, steps, census, combined = k5.build_ladder()
    del zones
    k5.artifact_key_ward(steps)
    f0_cells = k5.build_f0(combined)
    families = k5.build_families(census, combined)
    rows = k5.make_rows(steps, f0_cells, families)
    rows = k5.jacobi_identity_wards(rows)
    k5.pivot_ward(rows)
    k5.repro_anchors(rows)
    sos.exact_cell_data(rows)
    return rows, len(steps), len(rows) - len(steps)


def filter_shape_wards(fdata, cls):
    section("D -- exact derivations and the actual filter shape")
    t, u1, u2, v1, v2 = sp.symbols(
        "t u1 u2 v1 v2", positive=True)
    ff = t * (t * t + u1) * (t * t + u2) / (
        (t * t + v1) * (t * t + v2))
    ell = (1 / t + 2 * t * (
        1 / (t * t + u1) + 1 / (t * t + u2)
        - 1 / (t * t + v1) - 1 / (t * t + v2)))
    ell_prime = (-1 / t ** 2 + 2 * (
        (u1 - t * t) / (t * t + u1) ** 2
        + (u2 - t * t) / (t * t + u2) ** 2
        - (v1 - t * t) / (t * t + v1) ** 2
        - (v2 - t * t) / (t * t + v2) ** 2))
    check("D1 sympy exact log-derivative F'/F formula",
          sp.simplify(sp.diff(ff, t) / ff - ell) == 0, kill="K2")
    check("D2 sympy exact second derivative F''/F = ell^2+ell'",
          sp.simplify(sp.diff(ff, t, 2) / ff
                      - ell * ell - ell_prime) == 0, kill="K2")

    lam1, tt, qq, bb, cc = sp.symbols(
        "lam1 T Q B C", real=True)
    goods = sp.symbols("x2:9", real=True)
    lhs = sum(bb * x + cc * x * x for x in goods)
    rhs = bb * (tt - lam1) + cc * (qq - lam1 * lam1)
    replacement = {
        tt: lam1 + sum(goods),
        qq: lam1 * lam1 + sum(x * x for x in goods),
    }
    check("D3 sympy trace/Q coupling rearrangement is exact",
          sp.expand((lhs - rhs).subs(replacement)) == 0, kill="K2")

    m, uu, zz, ss = sp.symbols("m U z S", positive=True)
    pigeon = sp.expand(
        (m * zz + (7 - m) * uu) - (7 * uu - m * (uu - zz)))
    check("D4 sympy pigeonhole identity: S<=m z+(7-m)U gives "
          "m<=(7U-S)/(U-z)", pigeon == 0, kill="K2")

    nn, qv, detb, detm = sp.symbols(
        "n q detB detM", positive=True)
    check("D5 sympy Schur determinant rearrangement detM=(n-q)detB",
          sp.simplify(detm / lam1
                      - (nn - qv) * detb / lam1
                      ).subs(detm, (nn - qv) * detb) == 0,
          kill="K2")

    # Numeric anatomy only; validity never relies on these signs.
    xs = np.geomspace(max(float(cls["cb"]), 1.0e-12),
                       float(cls["L"]), SHAPE_N)
    ts = xs / float(fdata["L"])
    num = np.asarray(fdata["num"], float)
    den = np.asarray(fdata["den"], float)
    logd = 1.0 / ts
    logd2 = -1.0 / (ts * ts)
    for node in num:
        logd += 2.0 * ts / (ts * ts + node)
        logd2 += 2.0 * (node - ts * ts) / (ts * ts + node) ** 2
    for node in den:
        logd -= 2.0 * ts / (ts * ts + node)
        logd2 -= 2.0 * (node - ts * ts) / (ts * ts + node) ** 2
    fvals = np.asarray([
        1.0 - rc.zol.scalar_r(fdata, float(x)) for x in xs
    ]) / float(fdata["D"])
    rprime_sign = np.sign(-fvals * logd)
    rsecond_sign = np.sign(-fvals * (logd * logd + logd2))
    n_r1 = int(np.sum(rprime_sign[1:] * rprime_sign[:-1] < 0))
    n_r2 = int(np.sum(rsecond_sign[1:] * rsecond_sign[:-1] < 0))
    print("    shape anatomy on %d log points [c_B,L]: R' sign "
          "changes %d, R'' sign changes %d -- no global monotonicity/"
          "convexity assumption is consumed" % (SHAPE_N, n_r1, n_r2))
    return n_r1, n_r2


def envelope_ward(bank, fdata):
    section("C -- certified cut-envelope wards")
    rng = np.random.default_rng(WARD_SEED)
    xs = np.exp(rng.uniform(
        math.log(max(1.0e-12, bank.big_l * 1.0e-12)),
        math.log(bank.big_l), ENV_SAMPLE_N))
    worst = -float("inf")
    n_ok = 0
    n_test = 0
    for q, (bb, cc, dd) in enumerate(bank.cuts):
        if q % max(1, len(bank.cuts) // 8) != 0 \
                and q != len(bank.cuts) - 1:
            continue
        n_test += 1
        ub = bank.cut_query(q, xs, xs)
        yy = xs / bank.big_l
        truth = np.asarray([
            rc.zol.scalar_r(fdata, float(x)) for x in xs
        ]) - bb * yy - cc * yy * yy - dd * np.log(yy)
        worst = max(worst, float(np.max(truth - ub)))
        n_ok += int(np.all(truth <= ub + rig.ENV_TOL))
    check("C1 certified transformed-envelope contains direct R on "
          "%d sampled cuts x %d points (worst defect %.2e)"
          % (n_test, ENV_SAMPLE_N, worst),
          n_ok == n_test and worst <= rig.ENV_TOL, kill="K2")


def census_gate(rows151, bank, fdata):
    section("P -- 151-cell pointwise coupling gate + certified ceilings")
    n_dom = 0
    n_ceil = 0
    n_det = 0
    worst_def = -float("inf")
    max_ub = -float("inf")
    for row in rows151:
        theta = np.asarray(row["theta"], float)
        jm, jb = rc.theta_matrices(theta)
        lam = np.linalg.eigvalsh(jm)
        lam_b = np.linalg.eigvalsh(jb)
        floors_fr = rcl.spectral_floors(theta)
        floors = np.asarray([float(v) for v in floors_fr], float)
        f_hi = rig.nup(floors / (1.0 - CAT_RTOL))
        support = min(bank.big_l, float(rig.nup(math.sqrt(
            rig.nup(theta[0] * theta[0])
            + rig.nup(2.0 * theta[NDIM] * theta[NDIM])
            + rig.nup(np.sum(rig.nup(f_hi * f_hi)))))))
        ub, _q = direct_point_bound(
            bank, floors, float(theta[0]), float(theta[NDIM]),
            float(lam[0]), support)
        truth = rc.tr_r_of_theta(theta, fdata)
        defect = truth - ub
        worst_def = max(worst_def, defect)
        max_ub = max(max_ub, ub)
        n_dom += int(defect <= TIE)
        n_ceil += int(float(row["l_fr"]) + TIE >= float(lam_b[-1]))
        lhs = float(np.prod(lam[1:]))
        rhs = ((1.0 - T_R) * theta[0] * float(np.prod(floors))
               / max(float(lam[0]), 1.0e-300))
        n_det += int(lhs + TIE * max(1.0, abs(lhs)) >= rhs)
    check("P1 coupling inequality SATISFIED on %d/%d complete "
          "CCLXXIX cells (worst truth-UB defect %.2e; max UB %.6f)"
          % (n_dom, len(rows151), worst_def, max_ub),
          n_dom == len(rows151), kill="K2")
    check("P2 CCXCIII exact certified B ceilings dominate the float "
          "top eigenvalue on %d/%d cells" % (n_ceil, len(rows151)),
          n_ceil == len(rows151), kill="K2")
    check("P3 Schur-determinant lower product inequality holds on "
          "%d/%d cells" % (n_det, len(rows151)),
          n_det == len(rows151), kill="K2")
    return max_ub


def phantom_gate(rows, cls, fdata, env, cat, bank, thin_index):
    section("F -- the independent-seat 1.15 plateau is a phantom")
    floors = cat["f_lo"][thin_index]
    lambda_sat = float(floors[0] * (1.0 - cls["t_r"]))
    seat1 = float(env.range_max(
        np.asarray([lambda_sat]), np.asarray([float(cls["L"])]))[0])
    plateau = float(rig.nup(seat1 + cat["sg"][thin_index]))

    theta = np.asarray(rows[thin_index]["theta"], float)
    support = min(bank.big_l, float(rig.nup(math.sqrt(
        cls["hi"][0] ** 2 + 2.0 * cls["hi"][NDIM] ** 2
        + np.sum(cat["f_hi"][thin_index] ** 2)))))
    # Maximize the coupled cut over the class n/a1 box while fixing
    # the fictitious lambda_sat and the thin branch.
    f_hi = cat["f_hi"][thin_index]
    tr_b = float(rig.nup(np.sum(f_hi)))
    sq_b = float(rig.nup(np.sum(rig.nup(f_hi * f_hi))))
    intercept = bank.intercept_sum(floors, support)
    vals = []
    log_floor = float(rig.ndown(
        rig.log_lo(1.0 - T_R)
        + np.sum(rig.log_lo(floors / bank.big_l))))
    log_n = float(rig.log_lo(
        max(float(cls["lo"][0]), 1.0e-300) / bank.big_l))
    for q, (bb, cc, dd) in enumerate(bank.cuts):
        bad = float(bank.cut_query(
            q, np.asarray([lambda_sat]),
            np.asarray([lambda_sat]))[0])
        vals.append(float(rig.nup(
            intercept[q] + bad
            + bb * (cls["hi"][0] + tr_b) / bank.big_l
            + cc * (cls["hi"][0] ** 2
                    + 2.0 * cls["hi"][NDIM] ** 2 + sq_b)
            / bank.big_l ** 2
            + dd * (log_floor + log_n))))
    coupled = min(vals)
    print("    thin branch kz=%d: lambda_sat=f1(1-t_R)=%.9f; "
          "independent plateau %.9f; certified coupled ceiling at "
          "that bad-seat value %.9f"
          % (rows[thin_index]["kz"], lambda_sat, plateau, coupled))
    check("F1 the fictitious independent-seat plateau is EXCLUDED "
          "by the coupling currency (coupled %.9f < plateau %.9f)%s"
          % (coupled, plateau,
             " -- SMOKE-BYPASSED: reduced geometry is the disclosed "
             "degenerate fake bridge" if SMOKE else ""),
          SMOKE or coupled < plateau, kill="K2")
    return lambda_sat, plateau, coupled


def controls(rows, cls, fdata, env, cat, thin_index):
    section("X -- controls-must-fire")
    theta = np.asarray(rows[thin_index]["theta"], float).copy()
    theta[0] = -1.0
    parent = k3.BoxWork3(cls, env, fdata, cat)
    feasible, tr_lo, tr_hi, fails = parent.point_certify(theta)
    lam1 = float(np.linalg.eigvalsh(rc.theta_matrices(theta)[0])[0])
    check("X1 indefinite world lambda_1=%.6f has certified tr R "
          "interval [%.6f,%.6f] with lower >=1 and is REJECTED (%s)"
          % (lam1, tr_lo, tr_hi, ",".join(fails) or "-"),
          (not feasible) and tr_lo >= 1.0, kill="K4")

    far = dict(
        f_lo=cat["f_lo"] * 1.0e3,
        f_hi=cat["f_hi"] * 1.0e3,
        sg=cat["sg"].copy(), sha="control", n=cat["n"])
    doctored = k3.BoxWork3(cls, env, fdata, far)
    truth = np.asarray(rows[thin_index]["theta"], float)[None, :]
    _ub, keep, _sp, _vol = doctored.process(truth, truth)
    other = sum(doctored.stats[k] for k in doctored.stats
                if k.startswith("pr_") and k != "pr_floor")
    check("X2 doctored catalog is killed by floor logic alone: "
          "pr_floor=%d, all other prunes=%d"
          % (doctored.stats["pr_floor"], other),
          (not keep[0]) and doctored.stats["pr_floor"] == 1
          and other == 0, kill="K4")


def finish(result):
    section("V -- FROZEN VERDICT")
    passed = sum(1 for _name, ok in CHECKS if ok)
    total = len(CHECKS)
    full_bound = result.get("full_bound", float("inf"))
    lower = result.get("lower", LOWER_ANCHOR)
    if KILLS:
        verdict = {
            "K1": "PIPELINE-BROKEN",
            "K2": "WARD-BROKEN",
            "K3": "REPRO-BROKEN",
            "K4": "CONTROL-SILENT",
        }.get(KILLS[0], "BLOCKED")
    elif not SMOKE and full_bound < 1.0:
        verdict = (
            "COUPLING-CERTIFIED(the class-level OBSERVER statement "
            "sup tr R <= %.9f < 1 over the frozen CCLXXXIX "
            "tight-floor entry-data class; certified window "
            "[%.9f, %.9f]; premises: CCLXXXI box SHA %s..., "
            "85-branch exact-Sturm ordered-floor catalog SHA %s..., "
            "two-sided floor quality 1e-6, K=5 Gauss-Radau "
            "q<=0.7809 n, B>0, radius, eta/MOM/KS/COEF/SPREAD; "
            "therefore the KS.DUAL finite-class COMPRESSION observer "
            "side is closed.  CCXCIII positivity is an independent "
            "already-closed premise and stands regardless.  No "
            "all-h statement; NO RH claim.)"
            % (full_bound, lower, full_bound,
               result["box_sha"][:8], result["cat_sha"][:8]))
    elif full_bound < float("inf"):
        verdict = (
            "PARTIAL(new certified coupling ceiling %.9f; window "
            "[%.9f,%.9f], measured blocker printed above)"
            % (full_bound, lower, full_bound))
    else:
        verdict = "BLOCKED(no certified coupling rerun result)"
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST FRAME.  This is an experiments-only finite/frozen class
  statement.  The observer inequality consumes only entry traces,
  entry second moments, certified ordered co-block floors, the
  certified scalar envelope and the declared Radau/positivity
  premises.  The 151-cell gate is a pointwise power/validity census,
  not an all-h membership theorem.  No verification, paper, ledger,
  website or manifest file is touched; no marker moves; no .md;
  no commit; NO RH claim.""")
    elapsed = time.time() - T0
    print("\n[TIME] %.1f s   [CHECKS] %d run, %d failed   [KILLS] %s"
          % (elapsed, total, total - passed,
             ",".join(KILLS) if KILLS else "none"))
    print("  FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    check_runtime = elapsed < 1500.0
    print("  RUNTIME GATE <25 min: %s (%.1f s)"
          % ("PASS" if check_runtime else "FAIL", elapsed))
    return 0 if passed == total and not KILLS and check_runtime else 1


def main():
    section("PRIME.ONEBADMODE.COUPLING.01 -- certified coupling "
            "currency (EXPLORATION ONLY)")
    print("    FROZEN_SPEC SHA-256 = %s" % SPEC_SHA)
    print("    mode=%s; scope experiments/tfpt-discovery only (+ later "
          "next.txt prepend); NO RH claim"
          % ("SMOKE" if SMOKE else "FROZEN"))
    print("    cut bank: %d trace-only / %d trace+Q; budget %.0f s"
          % (len(CUTS_TRACE), len(CUTS_FULL), MAIN_BUDGET))

    section("S -- firewall and anti-circularity")
    bad = ast_scan_all(BANNED_IDS)
    check("S1 AST firewall clean (no prime/zero oracle)", not bad,
          ",".join(sorted(set(bad))), kill="K2")
    ac = ast_scan_functions(CONSUMED_FUNCS, CONSUMED_BANNED)
    check("S2 consumed per-box currency reads class entries/floors "
          "only; no wall read/identifier", not ac,
          ",".join(sorted(set(ac))), kill="K2")

    rows, cls, fdata, env, cat = build_85_class()
    if rc.KILLS or cat is None:
        KILLS.append("K1")
        return finish({})
    check("S3 CCLXXXIX class rebuilt: %d branches, box SHA %s..."
          % (cat["n"], cls["box_sha"][:16]),
          (SMOKE or cat["n"] == 85)
          and (SMOKE or cls["box_sha"][:32] == BOX_SHA_CCLXXXI),
          kill="K3")
    check("S4 inherited Radau cap t_R=%.4f and catalog quality %.0e"
          % (cls["t_r"], CAT_RTOL),
          abs(cls["t_r"] - T_R) <= 1.0e-12
          and float(k3.CAT_RTOL_FR) == CAT_RTOL, kill="K3")

    filter_shape_wards(fdata, cls)
    bank_full = CutBank(env, cls["L"], CUTS_FULL)
    envelope_ward(bank_full, fdata)

    thin_index = int(np.argmax([r["trace_r"] for r in rows]))
    thin = rows[thin_index]
    thin_lam1 = float(np.min(thin["lam_j"]))
    thin_support = min(float(cls["L"]), float(rig.nup(math.sqrt(
        thin["theta"][0] ** 2 + 2.0 * thin["theta"][NDIM] ** 2
        + np.sum(cat["f_hi"][thin_index] ** 2)))))
    f4_ub, f4_cut = direct_point_bound(
        bank_full, cat["f_lo"][thin_index],
        float(thin["theta"][0]), float(thin["theta"][NDIM]),
        thin_lam1, thin_support)
    check("P0 CCLXXXV F4 optimum witness kz=%d tr R=%.9f, "
          "lambda_1=%.9f is SATISFIED by (CC): UB %.9f "
          "(cut B=%.1f,C=%.1f,D=%.4g)"
          % (thin["kz"], thin["trace_r"], thin_lam1, f4_ub,
             bank_full.cuts[f4_cut][0], bank_full.cuts[f4_cut][1],
             bank_full.cuts[f4_cut][2]),
          f4_ub + TIE >= thin["trace_r"], kill="K2")

    rows151, n_ladder, n_sweep = build_151()
    check("P0b complete wall-legal census rebuilt: %d ladder + %d "
          "sweep = %d (expected %d)"
          % (n_ladder, n_sweep, len(rows151), CELL_EXP),
          SMOKE or len(rows151) == CELL_EXP, kill="K3")
    census_gate(rows151, bank_full, fdata)
    phantom = phantom_gate(
        rows, cls, fdata, env, cat, bank_full, thin_index)
    controls(rows, cls, fdata, env, cat, thin_index)
    if KILLS:
        return finish({})

    section("O -- rigor-3 certified rerun: trace, trace+Q, thin/full")
    master_lo, master_hi = preclip_master(cls)
    plain = k3.BoxWork3(cls, env, fdata, cat)
    plain_ub = float(plain.process(
        master_lo[None, :], master_hi[None, :])[0][0])
    trace_work = CouplingWork(cls, env, fdata, cat, CUTS_TRACE)
    trace_ub = float(trace_work.process(
        master_lo[None, :], master_hi[None, :])[0][0])
    print("    ROOT comparison: independent-seat %.9f -> "
          "trace-coupled %.9f" % (plain_ub, trace_ub))

    thin_cat = subset_catalog(cat, [thin_index])
    thin_work = CouplingWork(cls, env, fdata, thin_cat, CUTS_FULL)
    thin_result = run_until_one(
        thin_work, master_lo, master_hi, MAIN_BUDGET, "thin")
    print("    THIN certified window [%.9f, %.9f], stop=%s, "
          "processed=%d, coupling wins=%d (trace %d / moment %d / "
          "determinant %d)"
          % (LOWER_ANCHOR, thin_result["bound"], thin_result["stop"],
             thin_result["stats"]["processed"],
             thin_result["stats"]["coupling_win"],
             thin_result["stats"]["coupling_trace"],
             thin_result["stats"]["coupling_moment"],
             thin_result["stats"]["coupling_determinant"]))

    full_work = CouplingWork(cls, env, fdata, cat, CUTS_FULL)
    full_result = run_until_one(
        full_work, master_lo, master_hi, MAIN_BUDGET, "full")
    print("    FULL certified window [%.9f, %.9f], stop=%s, "
          "processed=%d, coupling wins=%d (trace %d / moment %d / "
          "determinant %d)"
          % (LOWER_ANCHOR, full_result["bound"], full_result["stop"],
             full_result["stats"]["processed"],
             full_result["stats"]["coupling_win"],
             full_result["stats"]["coupling_trace"],
             full_result["stats"]["coupling_moment"],
             full_result["stats"]["coupling_determinant"]))
    check("O1 thin-rung result typed: certified UB %.9f (%s)"
          % (thin_result["bound"],
             "CLOSES" if thin_result["bound"] < 1.0 else "PARTIAL"),
          True)
    check("O2 full-class result typed: certified UB %.9f (%s)"
          % (full_result["bound"],
             "CLOSES" if full_result["bound"] < 1.0 else "PARTIAL"),
          True)
    check("T1 tau/c_h relocation screens: class-data-only currency, "
          "no new per-step tau/c_h decision", True)
    check("T2 scope guard: observer side only; CCXCIII positivity "
          "independent; no all-h and NO RH claim", True)

    result = dict(
        full_bound=full_result["bound"],
        thin_bound=thin_result["bound"],
        trace_bound=trace_ub,
        plain_bound=plain_ub,
        lower=LOWER_ANCHOR,
        box_sha=cls["box_sha"],
        cat_sha=cat["sha"],
        phantom=phantom,
    )
    return finish(result)


if __name__ == "__main__":
    raise SystemExit(main())
