#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""wave_packet_partition_probe -- PRIME.WAVEPACKET.PARTITION.01
(EXPLORATION ONLY, experiments/; direct follow-up to
ENVELOPE-EMPIRICAL-ONLY, 2026-08-08 night).

THE TYPED NEXT OBJECT.  The envelope probe closed the cell
class: every Pruefer cell contains near-diagonal geometric
pairs, pointwise bounds saturate, no cell accounting reaches
below 3.57 (bar 1), and the measured envelope decay is
cancellation-carried.  THE DEMAND: a NON-CELL decomposition
where the diagonal carries the mass and the cancellation
stays INSIDE the blocks -- wave packets on the natural
position-frequency phase space of the odd frame (cos th acts
tridiagonally: generator bandwidth 1, commutator cost O(1)
h-uniform at C_int grade -- the balanced uncertainty scale
s^2 ~ pi/(2 dim) is the packet width both designs use).

THE FORMALIZATION (frozen): canonical TIGHT packet frames on
both node spaces, Psi~ = S^{-1/2} Psi with S the frame
operator; then C^G = Psi~_m B Psi~_p^H with B = Psi~_m^H C^G
Psi~_p and ||C^G|| = ||B||_2 EXACTLY (sanity ward).  The
accounting object is B: diagonal = nearest-packet pairing in
normalized phase-space coordinates; the effective constant is
the Schur bound sqrt(maxrow x maxcol) of |B| -- the honest
number vs the cell frame's 3.57 and vs the certificate bar 1.

DESIGNS (predeclared, source-only):
  (a) RANK-GABOR (measure-adapted; the naive angle lattice
      is structurally killed by node clustering -- the
      folded minus support is patchy, so a uniform angle
      lattice cannot span the clustered node space): the
      position coordinate is the node RANK u_j = (rank(th_j)
      + 1/2)/r (uniform by construction), packets
      psi_{(u0,q)}[j] = exp(-(u_j - u0)^2/(2 su^2))
      e^{2 pi i q u_j}, su = 1/sqrt(2 r), lattice u0 step su
      over (0,1), q step 1/(2 su) over [-r/2, r/2]
      (2x oversampled, N ~ 2 r).
  (b) CHAIN packets: Phi = the orthogonal eigenvector matrix
      of the arm's tridiagonal chain (the exact discrete OP
      transform, columns matched to the deployed nodes);
      psi_{(n0, phi)} = Phi^T-transform of a Gaussian window
      exp(-(n - n0)^2/(2 sig^2)) e^{i n phi}, sig = sqrt(m),
      n0 step sig, phi step pi/sig (N ~ 2 m).
FRAME WARDS: cond(S) <= 1e10 both sides (else the design is
KILLED for that rung, typed); node-eigenvalue match <= 1e-8
for (b); ||B||_2 == ||C^G||_2 to 1e-8 rel (tightness).

TASKS: (2a) the diagonal question under TWO frozen pairings:
D1 the geometric nearest packet in normalized coordinates,
and D2 the EMPIRICAL partner map Q*(P) = argmax_Q |B_PQ|
(share + injectivity + the median coordinate offset -- the
measured pairing law; a near-permutation B with coherent
offsets is the cancellation-respecting structure even if the
naive geometric pairing misses it); plus the row
concentration (mean share of each row's energy in its best
entry); (2b) the off-diagonal envelope in normalized
phase-space distance rho (bins, decay typed); (2c) the
effective Schur constant vs 3.57 and vs 1; (3) the
certificate assembly: E_schur vs the known ||C^G|| =
sqrt(1 - lam1) per rung along ladder + complete-comb deep
holdouts; (4) Epstein/scramble in the same frame.
VERDICT (frozen): PACKETS-CARRY (on every rung the best
design has E_schur <= 1.2 AND [D1 share >= 0.5 OR (D2 share
>= 0.5 AND injectivity >= 0.8)] -- prominent) / PARTITION-
CLASS-CLOSED (every functioning design has E_schur >= 3.5
on every rung -- the atomically-global typing) /
PACKETS-PARTIAL (typed which piece).  NO RH claim; writes
nothing; no .md; no commits.

Run:
    experiments/tfpt-discovery/.venv/bin/python \
        experiments/tfpt-discovery/wave_packet_partition_probe.py
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

import v563_paper2_readouts as core            # noqa: E402  (READ-ONLY)
import gauss_node_unitary_probe as gnu         # noqa: E402  (READ-ONLY)
import pruefer_compensation_probe as ppc       # noqa: E402  (READ-ONLY)
import cotlar_v2_complete_comb_probe as cv2    # noqa: E402  (READ-ONLY)
import envelope_derivation_gap_probe as edg    # noqa: E402  (READ-ONLY)

FROZEN_SPEC = """\
PRIME.WAVEPACKET.PARTITION.01 spec v1 (2026-08-08, frozen
before run).  SAMPLE (frozen): kz (9, 13, 26, 40, 64, 90,
142, 243); 142/243 with the v2 COMPLETE comb.  OBJECT: C^G =
Dm-weighted U from gauss_objects (node coordinates); ward
|sigma_max(C^G)^2 - (1 - lam1(Delta))| <= 1e-8 rel.  DESIGNS
(a) RANK-GABOR: position = node rank u_j (uniform), su =
1/sqrt(2 r), lattice (u0: step su in (0,1); q: step
1/(2 su) in [-r/2, r/2]) and (b) chain packets sig =
sqrt(m), lattice (n0: step sig in (0, m); phi: step pi/sig
in (-pi, pi)) -- docstring formulas verbatim; packets of raw
norm < 1e-8 dropped (typed count); canonical tight frames
via S^{-1/2}.  FRAME KILL: lam_min(S) <= 0 or cond(S) > 1e10
on either side.  Normalized packet coords: (u0, q/r) resp
(n0/m, phi/(2 pi)).  READOUTS per rung x design: N_m, N_p,
cond_m, cond_p; ||B||_2 vs ||C^G|| (tightness ward 1e-8
rel); E_schur = sqrt(max row l1 x max col l1 of |B|); E_row
= max row l1; D1 diag: Q*(P) = nearest plus packet in
normalized coords -- max_P |B|, Frobenius share; D2 diag:
Q*(P) = argmax_Q |B_PQ| -- Frobenius share, injectivity
fraction, median |offset| in both coords (the measured
pairing law); row concentration = mean_P max_Q |B_PQ|^2 /
sum_Q |B_PQ|^2; envelope: max |B| in normalized-rho bins
(0, .02, .05, .1, .2, .4, .7, 1, 1.5+); decay = env(last
nonempty)/env(0).  DECISION (frozen): PACKETS-CARRY iff the
best design on every rung has E_schur <= 1.2 AND [D1 share
>= 0.5 OR (D2 share >= 0.5 AND injectivity >= 0.8)];
PARTITION-CLASS-CLOSED iff every non-killed design on every
rung has E_schur >= 3.5; else PACKETS-PARTIAL (typed).
DISCRIMINATION (kz 9, design a): Epstein and scramble must
move (E_schur rel >= 0.25 or diag share abs >= 0.25) --
else typed failure.  CONTROLS: envelope-probe regressions at
kz 9 (CD identity residual <= 1e-8, C_int within 1e-3 rel of
1.412); frame wards; certified budgets (runtime + peak N).
NO RH claim; writes nothing."""

SAMPLE = (9, 13, 26, 40, 64, 90, 142, 243)
DEEP = (142, 243)
RHO_BINS = (0.0, 0.02, 0.05, 0.10, 0.20, 0.40, 0.70,
            1.00, 1.50)
COND_KILL = 1e10
DIAG_BAR = 0.5
SCHUR_CARRY = 1.2
SCHUR_CLOSED = 3.5
CTRL_MOVE = 0.25
C_INT_REF = 1.412
BANNED_IDS = ("zetazero", "nzeros", "primerange", "isprime",
              "primepi", "nextprime", "prevprime")

CHECKS = []
FAILS = []
T0 = time.time()


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    if not ok:
        FAILS.append(name.split()[0])
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


# ------------------------------------------------ packet frames
def tighten(Psi):
    """Canonical tight frame; returns (Psi_tight, cond) or
    (None, cond) on frame kill."""
    S = Psi @ Psi.conj().T
    S = 0.5 * (S + S.conj().T)
    w, V = np.linalg.eigh(S)
    if w[0] <= 0.0 or w[-1] / w[0] > COND_KILL:
        return None, float(w[-1] / max(w[0], 1e-300))
    Si = (V * (w ** -0.5)) @ V.conj().T
    return Si @ Psi, float(w[-1] / w[0])


def gabor_frame(th, r):
    """Design (a): rank-Gabor packets (position = node
    rank, uniform by construction)."""
    u = (np.argsort(np.argsort(th)).astype(float) + 0.5) / r
    su = 1.0 / math.sqrt(2.0 * r)
    u0s = np.arange(su / 2.0, 1.0, su)
    dq = 1.0 / (2.0 * su)
    qs = np.arange(-r / 2.0, r / 2.0 + 1e-9, dq)
    packets, meta = [], []
    for u0 in u0s:
        g = np.exp(-(u - u0) ** 2 / (2.0 * su * su))
        ng = float(np.linalg.norm(g))
        if ng < 1e-8:
            continue
        for q in qs:
            v = g * np.exp(2j * math.pi * q * u)
            packets.append(v / ng)
            meta.append((u0, q / r))
    Psi = np.array(packets).T
    return Psi, np.array(meta)


def chain_matrix(al, be, th):
    """Eigenvector matrix of the tridiagonal chain, columns
    matched to the deployed node ordering.  Returns (Phi,
    match_err); Phi[j, n] = orthonormal OP transform."""
    m = len(al)
    J = np.diag(al)
    if m > 1:
        J += np.diag(be[:m - 1], 1) + np.diag(be[:m - 1], -1)
    evs, V = np.linalg.eigh(J)
    x = np.cos(th)
    order = np.argsort(np.argsort(x))
    err = float(np.max(np.abs(evs[order] - x)))
    return V[:, order].T, err


def chain_frame(al, be, th):
    """Design (b): Gaussian windows in the chain index,
    transported by the exact OP transform."""
    Phi, err = chain_matrix(al, be, th)
    m = Phi.shape[1]
    sig = math.sqrt(float(m))
    n0s = np.arange(sig / 2.0, m, sig)
    dph = math.pi / sig
    phs = np.arange(-math.pi, math.pi - 1e-9, dph)
    nn = np.arange(m, dtype=float)
    packets, meta = [], []
    for n0 in n0s:
        g = np.exp(-(nn - n0) ** 2 / (2.0 * sig * sig))
        ng = float(np.linalg.norm(g))
        if ng < 1e-8:
            continue
        for ph in phs:
            c = g * np.exp(1j * nn * ph)
            packets.append(Phi @ (c / ng))
            meta.append((n0 / m, ph / (2.0 * math.pi)))
    Psi = np.array(packets).T
    return Psi, np.array(meta), err


def block_readout(CG, Pm, mm, Pp, mp):
    """B = Pm^H C Pp + the frozen readouts."""
    B = Pm.conj().T @ CG @ Pp
    aB = np.abs(B)
    nB = float(np.linalg.svd(B, compute_uv=False)[0])
    rowl1 = np.sum(aB, axis=1)
    coll1 = np.sum(aB, axis=0)
    E_schur = math.sqrt(float(np.max(rowl1))
                        * float(np.max(coll1)))
    E_row = float(np.max(rowl1))
    fro2 = max(float(np.sum(aB ** 2)), 1e-300)
    # D1: nearest-packet diagonal (normalized coords)
    d2 = ((mm[:, 0][:, None] - mp[:, 0][None, :]) ** 2
          + (mm[:, 1][:, None] - mp[:, 1][None, :]) ** 2)
    qstar = np.argmin(d2, axis=1)
    diag = aB[np.arange(aB.shape[0]), qstar]
    dshare = float(np.sum(diag ** 2)) / fro2
    offrow = rowl1 - diag
    worst = int(np.argmax(rowl1))
    ratio_worst = float(offrow[worst]) \
        / max(float(diag[worst]), 1e-300)
    # D2: the empirical partner map (the measured pairing)
    qbest = np.argmax(aB, axis=1)
    dbest = aB[np.arange(aB.shape[0]), qbest]
    dshare2 = float(np.sum(dbest ** 2)) / fro2
    inj = float(len(np.unique(qbest))) / len(qbest)
    off_pos = float(np.median(np.abs(
        mm[:, 0] - mp[qbest, 0])))
    off_frq = float(np.median(np.abs(
        mm[:, 1] - mp[qbest, 1])))
    row2 = np.sum(aB ** 2, axis=1)
    conc = float(np.mean(dbest ** 2
                         / np.maximum(row2, 1e-300)))
    # envelope in normalized phase-space distance
    rho = np.sqrt(d2)
    env = []
    for k in range(len(RHO_BINS) - 1):
        m_ = (rho >= RHO_BINS[k]) & (rho < RHO_BINS[k + 1])
        env.append(float(np.max(aB[m_])) if np.any(m_)
                   else float("nan"))
    m_ = rho >= RHO_BINS[-1]
    env.append(float(np.max(aB[m_])) if np.any(m_)
               else float("nan"))
    fin = [e for e in env if math.isfinite(e)]
    decay = (fin[-1] / fin[0]) if len(fin) >= 2 else 1.0
    return dict(nB=nB, E_schur=E_schur, E_row=E_row,
                dmax=float(np.max(diag)), dshare=dshare,
                ratio_worst=ratio_worst, dshare2=dshare2,
                inj=inj, off=(off_pos, off_frq), conc=conc,
                env=env, decay=decay,
                Nm=Pm.shape[1], Np=Pp.shape[1])


def rung_packets(kz, **kw):
    """Both designs on one rung; returns per-design readouts
    or typed kills."""
    dc, err = ppc.deployed_cells(kz, **kw)
    if dc is None:
        return None, err
    b, go = dc["b"], dc["go"]
    CG = go["Dm"][:, None] * go["U"]
    nC = float(np.linalg.svd(CG, compute_uv=False)[0])
    lam1 = float(np.linalg.eigvalsh(b["Delta"])[0])
    id_ok = abs(nC ** 2 - (1.0 - lam1)) \
        <= 1e-8 * max(1.0, nC ** 2)
    out = dict(kz=kz, h=b["h"], nC=nC, lam1=lam1,
               id_ok=id_ok, designs={})
    thm, thp = go["thm"], go["thp"]
    ch = dc["chains"]
    # design (a)
    Pm_raw, mm = gabor_frame(thm, len(thm))
    Pp_raw, mp = gabor_frame(thp, len(thp))
    Pm, cm = tighten(Pm_raw)
    Pp, cp = tighten(Pp_raw)
    if Pm is None or Pp is None:
        out["designs"]["gabor"] = dict(
            kill="frame (cond %.1e/%.1e)" % (cm, cp))
    else:
        rd = block_readout(CG, Pm, mm, Pp, mp)
        rd.update(cond=(cm, cp))
        out["designs"]["gabor"] = rd
    # design (b)
    Pm_raw, mm, em = chain_frame(ch["alm"], ch["bem"], thm)
    Pp_raw, mp, ep = chain_frame(ch["alp"], ch["bep"], thp)
    if max(em, ep) > 1e-8:
        out["designs"]["chain"] = dict(
            kill="node match (%.1e/%.1e)" % (em, ep))
    else:
        Pm, cm = tighten(Pm_raw)
        Pp, cp = tighten(Pp_raw)
        if Pm is None or Pp is None:
            out["designs"]["chain"] = dict(
                kill="frame (cond %.1e/%.1e)" % (cm, cp))
        else:
            rd = block_readout(CG, Pm, mm, Pp, mp)
            rd.update(cond=(cm, cp))
            out["designs"]["chain"] = rd
    return out, None


def show(kz, h, name, rd):
    if "kill" in rd:
        print("    kz %-4d h %-4d [%s]: KILLED -- %s"
              % (kz, h, name, rd["kill"]), flush=True)
        return
    es = " ".join(("%.3f" % e) if math.isfinite(e) else "--"
                  for e in rd["env"])
    print("    kz %-4d h %-4d [%-5s N %4d/%4d cond "
          "%.1e/%.1e]: ||B|| %.6f | E_schur %.3f E_row %.3f"
          % (kz, h, name, rd["Nm"], rd["Np"], rd["cond"][0],
             rd["cond"][1], rd["nB"], rd["E_schur"],
             rd["E_row"]), flush=True)
    print("      D1 diag: max %.3f share %.3f (worst "
          "off/diag %.2f) | D2 partner: share %.3f inj "
          "%.2f offset (%.3f, %.3f) | row conc %.3f"
          % (rd["dmax"], rd["dshare"], rd["ratio_worst"],
             rd["dshare2"], rd["inj"], rd["off"][0],
             rd["off"][1], rd["conc"]), flush=True)
    print("      env %s | decay %.4f" % (es, rd["decay"]),
          flush=True)


# ================================================================= main
def main():
    section("PRIME.WAVEPACKET.PARTITION.01 -- the coherent-"
            "state partition of the contractor (EXPLORATION "
            "ONLY)")
    sha = hashlib.sha256(FROZEN_SPEC.encode("utf-8")).hexdigest()
    print("    FROZEN_SPEC SHA-256 = %s" % sha)
    print("    NO RH claim.")
    print("\nS0 -- firewall + inherited contracts + "
          "regressions")
    check("S0.1 AST firewall clean", not ast_scan(BANNED_IDS))
    shas = [hashlib.sha256(m.FROZEN_SPEC.encode()).hexdigest()
            for m in (ppc, cv2, edg)]
    check("S0.2 [CONTRACT CHAIN] v1 %s... v2 %s... envelope "
          "%s..." % tuple(s[:8] for s in shas),
          shas[0].startswith("4621b899")
          and shas[1].startswith("5fd6bf61")
          and shas[2].startswith("27d9f0a3"))
    cv2.U_EXT, cv2.MU_EXT = cv2.build_ext_table()
    dc9, _ = edg.get_dc(9)
    cs9 = edg.census(dc9)
    aa9 = edg.analytic_envelope(dc9, cs9)
    check("S0.3 [ENVELOPE REGRESSION] CD identity residual "
          "%.1e <= 1e-8 and C_int %.4f within 1e-3 rel of "
          "%.3f" % (aa9["idres"], aa9["C_int"], C_INT_REF),
          aa9["idres"] <= 1e-8
          and abs(aa9["C_int"] - C_INT_REF) / C_INT_REF
          <= 1e-3)

    # ---------------- the main table
    section("TASK 1+2 -- packet frames + the block structure "
            "of C^G  (env bins: rho = %s)"
            % (RHO_BINS,))
    res = {}
    id_all, tight_all = True, True
    for kz in SAMPLE:
        kw = dict(comb=cv2.comb_ext(kz)) if kz in DEEP \
            else {}
        out, err = rung_packets(kz, **kw)
        if out is None:
            print("    kz %d: %s" % (kz, err))
            continue
        res[kz] = out
        id_all &= out["id_ok"]
        print("    kz %-4d: ||C^G|| = %.8f  (1 - lam1 = "
              "%.8f)%s" % (kz, out["nC"],
                           math.sqrt(max(0.0,
                                         1.0 - out["lam1"])),
                           "  [COMPLETE comb]"
                           if kz in DEEP else ""))
        for name, rd in out["designs"].items():
            show(kz, out["h"], name, rd)
            if "kill" not in rd:
                tight_all &= abs(rd["nB"] - out["nC"]) \
                    <= 1e-8 * max(1.0, out["nC"])
    check("P.1 [GAUGE IDENTITY] sigma_max(C^G)^2 == 1 - "
          "lam1(Delta) on every rung", id_all)
    check("P.2 [TIGHTNESS] ||B||_2 == ||C^G||_2 (1e-8 rel) "
          "for every non-killed design", tight_all)

    # ---------------- task 3: the certificate assembly
    section("TASK 3 -- the certificate assembly (E_schur vs "
            "the known norm, per rung)")
    best = {}
    for kz in res:
        live = {n: r for n, r in res[kz]["designs"].items()
                if "kill" not in r}
        if not live:
            continue
        bn = min(live, key=lambda n: live[n]["E_schur"])
        best[kz] = (bn, live[bn])
        print("    kz %-4d h %-4d: best design %-5s  "
              "E_schur %.3f  vs ||C^G|| %.6f  (gap ratio "
              "%.2f; cell-class best was 3.57)"
              % (kz, res[kz]["h"], bn,
                 live[bn]["E_schur"], res[kz]["nC"],
                 live[bn]["E_schur"] / res[kz]["nC"]))
    hh = np.log([float(res[kz]["h"]) for kz in best])
    ee = np.log([best[kz][1]["E_schur"] for kz in best])
    slope = float(np.polyfit(hh, ee, 1)[0])
    print("    E_schur log-log slope vs h: %+.3f "
          "(decaying toward 1 would need < 0)" % slope)

    # ---------------- task 4: discrimination
    section("TASK 4 -- Epstein / scramble in the same "
            "packet frame (kz 9, design a)")
    t9 = res[9]["designs"]["gabor"]
    rr9 = core.build_window(9)
    N_E = int(math.floor(math.exp(2.0 * rr9["alpha"]))) + 1
    lamE = gnu.lambda_eps(N_E)
    nn = np.nonzero(np.abs(lamE) > 1e-12)[0]
    ctrl_ok = True
    for nmc, kw in (("Epstein", dict(comb=(
            np.log(nn.astype(float)),
            2.0 * lamE[nn] / np.sqrt(nn.astype(float))))),
            ("scramble", dict(scramble_seed=1))):
        out, err = rung_packets(9, **kw)
        if out is None:
            print("    %-8s: %s (typed break)" % (nmc, err))
            continue
        rd = out["designs"]["gabor"]
        if "kill" in rd:
            print("    %-8s: %s (typed break)"
                  % (nmc, rd["kill"]))
            continue
        dE = abs(rd["E_schur"] - t9["E_schur"]) \
            / t9["E_schur"]
        dD = abs(rd["dshare"] - t9["dshare"])
        moved = dE >= CTRL_MOVE or dD >= CTRL_MOVE
        ctrl_ok &= moved
        print("    %-8s: E_schur %.3f (truth %.3f, rel "
              "%.2f) diag share %.3f (truth %.3f, abs "
              "%.2f) -> %s"
              % (nmc, rd["E_schur"], t9["E_schur"], dE,
                 rd["dshare"], t9["dshare"], dD,
                 "moves" if moved else "BLIND"))
    check("D.1 [DISCRIMINATION] the packet structure moves "
          "under Epstein/scramble", ctrl_ok)

    # ---------------- verdict
    section("V -- FROZEN VERDICT + honest consequence")
    def diag_ok(rd):
        return (rd["dshare"] >= DIAG_BAR
                or (rd["dshare2"] >= DIAG_BAR
                    and rd["inj"] >= 0.8))

    carry = all(diag_ok(r[1])
                and r[1]["E_schur"] <= SCHUR_CARRY
                for r in best.values()) and len(best) > 0
    closed = all(
        all(rd["E_schur"] >= SCHUR_CLOSED
            for rd in res[kz]["designs"].values()
            if "kill" not in rd)
        for kz in res) and len(res) > 0
    if carry:
        verdict = "PACKETS-CARRY"
    elif closed:
        verdict = "PARTITION-CLASS-CLOSED"
    else:
        dmin = min(r[1]["dshare"] for r in best.values())
        d2mn = min(r[1]["dshare2"] for r in best.values())
        imin = min(r[1]["inj"] for r in best.values())
        cmin = min(r[1]["conc"] for r in best.values())
        emin = min(r[1]["E_schur"] for r in best.values())
        emax = max(r[1]["E_schur"] for r in best.values())
        pieces = []
        pieces.append("diagonal %s (D1 min %.3f, D2 min "
                      "%.3f inj %.2f, conc %.3f; bar %.1f)"
                      % ("carries" if (dmin >= DIAG_BAR
                                       or (d2mn >= DIAG_BAR
                                           and imin >= 0.8))
                         else "does NOT carry", dmin, d2mn,
                         imin, cmin, DIAG_BAR))
        pieces.append("E_schur in [%.2f, %.2f] (carry bar "
                      "%.1f, closed bar %.1f)"
                      % (emin, emax, SCHUR_CARRY,
                         SCHUR_CLOSED))
        verdict = "PACKETS-PARTIAL (%s)" % "; ".join(pieces)
    print("\n  VERDICT: %s" % verdict)
    print("""
  HONEST CONSEQUENCE: the packet frame is the first
  decomposition tested against the cancellation finding of
  the envelope probe.  The numbers above are the honest
  comparison: cell class >= 3.57 everywhere (closed); the
  packet class delivers the E_schur column, the diagonal
  shares, and the phase-space envelope per rung -- whatever
  the enum says, the certificate shape requires E_schur ~ 1
  with an h-decaying excess, and the assembly table plus the
  slope above is the measured status of that demand.  NO RH
  claim.""")
    npass = sum(1 for _n, ok in CHECKS if ok)
    print("\n[TIME] %.1f min   [CHECKS] %d run, %d failed%s"
          % ((time.time() - T0) / 60.0, len(CHECKS),
             len(FAILS),
             ("  " + ",".join(FAILS)) if FAILS else ""))
    return 0 if npass == len(CHECKS) else 1


if __name__ == "__main__":
    raise SystemExit(main())
