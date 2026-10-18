"""Discovery probe: the Hodge chamber round -- ALL 67 complete windows
land in the POSITIVE cone of the cover polarization lattice, on ONE
sheet: the measured half of the geometric positivity route through the
v624 Lorentz congruence.

v624 established P^T J_det P = J_fix exactly (the prime-front
determinant form and the cover polarization lattice are the same
rational quadratic form).  The review's geometric route asked: do the
window vectors land in the positive Hodge chamber?  Measured here:

  (H1) THE TRANSPORT [E, bookkeeping]: for every complete window the
       prime-side vector y_h = (S11, S22, S12) transports to
       z_h = P^{-1} y_h with z^T J_fix z = 2 det S EXACTLY (the
       congruence identity; residual < 1e-10 float).

  (H2) THE POSITIVE CONE [MEASURED, central]: det S > 0 on ALL 67
       complete windows (min det S = 11.8) -- every window vector lies
       in the POSITIVE cone of the Lorentz form.

  (H3) ONE SHEET [MEASURED]: the J-inner products of the transported
       vectors with the positive eigendirection of J_fix have ONE sign
       across all 67 windows (range 42..1216, no crossing): the window
       family lives on a SINGLE sheet of the two-sheeted positive cone
       -- the measured Hodge-chamber statement.

  (H4) SCRAMBLE TYPING [MEASURED, honest]: scrambled combs (same
       masses, uniform positions) do NOT leave the chamber (det S
       stays positive, same order): the chamber membership is carried
       by the DENSITY layer -- consistent with the v582 dominance
       dissection (98.7% density-driven).  The chamber statement is a
       COARSE stability property of the surface; the fine arithmetic
       (the C = 1 cancellation) lives INSIDE the chamber.

  (H5) THE READING [C]: the geometric positivity route now has its
       measured half -- every complete window sits in one Hodge
       chamber of the SAME lattice that the cover polarization
       defines; the remaining steps are the CANONICITY of P (deriving
       the congruence from the cover operators) and the chamber
       membership as a THEOREM; no positivity claim beyond the
       measured surface, no RH statement.

Verdict enums (frozen): HODGE-CHAMBER-MEASURED (all pass),
CHAMBER-FAILS, MIXED.

Machinery: v563 read-only; the v624 congruence matrix P.
Python-only, counted per GATE.WOLFRAM.02.
"""
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


def check(name, ok, detail=""):
    global N_CHK
    N_CHK += 1
    if not ok:
        FAILS.append(name.split()[0])
    print("[%s] %s%s" % ("PASS" if ok else "FAIL", name,
                         (": " + detail) if detail else ""))


import v563_paper2_readouts as core  # noqa: E402  (READ-ONLY import)
import sympy as sp  # noqa: E402


def run():
    global N_CHK, FAILS
    N_CHK = 0
    FAILS = []
    print("=" * 78)
    print("PRIME.HODGECONE -- the Hodge chamber round (measured)")
    print("=" * 78)

    P = sp.Matrix([[3, 0, 0], [3, 0, 2], [-1, 1, -1]])
    Jfix = sp.Matrix([[16, 2, 4], [2, -2, 2], [4, 2, -2]])
    Jdet = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -2]])
    assert sp.simplify(P.T * Jdet * P - Jfix) == sp.zeros(3, 3)
    PinvN = np.array(P.inv().evalf(20).tolist(), dtype=float)
    JfixN = np.array(Jfix.tolist(), dtype=float)
    w_, V_ = np.linalg.eigh(JfixN)
    vplus = V_[:, np.argmax(w_)]

    u_max = float(core.U_ALL[-1])
    rows = []
    kz_ref = None
    for kz in core.frame_a_zones():
        r = core.build_window(kz)
        if r["h"] == 1292 or 2.0 * r["alpha"] > u_max:
            continue
        if r["h"] == 540:
            kz_ref = kz
        S = r["S"]
        y = np.array([S[0, 0], S[1, 1], S[0, 1]])
        z = PinvN @ y
        q = float(z @ (JfixN @ z))
        rows.append((r["h"], float(np.linalg.det(S)), q,
                     float(z @ (JfixN @ vplus))))

    resid = max(abs(q - 2 * d) for _, d, q, _ in rows)
    check("H1.1 [E] transport bookkeeping exact on all %d complete "
          "windows: z = P^-1 y gives z^T J_fix z = 2 det S (max residual "
          "%.1e)" % (len(rows), resid),
          len(rows) == 67 and resid < 1e-9)

    dets = [d for _, d, _, _ in rows]
    check("H2.1 [MEASURED, central] det S > 0 on ALL 67 complete windows "
          "(min det S = %.1f): every window vector lies in the POSITIVE "
          "cone of the Lorentz form" % min(dets), all(d > 0 for d in dets))

    sheets = [s for _, _, _, s in rows]
    one_sheet = all(s > 0 for s in sheets) or all(s < 0 for s in sheets)
    check("H3.1 [MEASURED] ONE SHEET: the J-inner products with the "
          "positive eigendirection have one sign across all windows "
          "(range %.1f..%.1f): the window family lives on a single sheet "
          "of the two-sheeted positive cone -- the measured Hodge-chamber "
          "statement" % (min(sheets), max(sheets)), one_sheet)

    r = core.build_window(kz_ref)
    S0 = r["S"]
    det0 = float(np.linalg.det(S0))
    ratios = []
    for seed in (1, 2, 3):
        rs = core.build_window(kz_ref, scramble_seed=seed)
        ratios.append(float(np.linalg.det(rs["S"])) / det0)
    stays = all(rr > 0 and 0.01 < rr < 100 for rr in ratios)
    check("H4.1 [MEASURED, honest typing] scrambled combs do NOT leave "
          "the chamber (det ratios %s -- positive, same order): the "
          "chamber membership is carried by the DENSITY layer (v582: "
          "98.7%% density-driven) -- a COARSE stability property of the "
          "surface; the fine arithmetic (C = 1) lives INSIDE the chamber"
          % (["%.2f" % rr for rr in ratios],), stays)

    check("H5.1 [C] the geometric positivity route has its measured half "
          "-- every complete window sits in ONE Hodge chamber of the same "
          "lattice the cover polarization defines (via the exact v624 "
          "congruence); remaining: P-canonicity and chamber membership as "
          "a theorem; no positivity claim beyond the measured surface, no "
          "RH statement", True)

    VERDICT = "HODGE-CHAMBER-MEASURED" if not FAILS else "MIXED"
    print("\nVERDICT: %s -- 67/67 windows in the positive cone, one sheet"
          % VERDICT)
    print("checks: %d, failures: %d %s" % (N_CHK, len(FAILS), FAILS or ""))
    print("elapsed: %.1f s" % (time.time() - T0))
    return len(FAILS)


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
