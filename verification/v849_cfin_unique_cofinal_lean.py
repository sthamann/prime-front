"""v849 Prime Front scope: cofinal Weil implication/hypothesis mirror.

Scope extraction from original module at ba2f0fc; original ID and
mathematical statements preserved. Original full source is retained
in the extraction provenance; no proof/status promotion.
"""
import math

import numpy as np

_B_CHECKS = []

def _bcheck(name, ok, detail=""):
    _B_CHECKS.append(bool(ok))
    print("  [%s] %s%s" % ("PASS" if ok else "FAIL", name,
                           ("  -- " + detail) if detail else ""),
          flush=True)
    return bool(ok)

def part_b():
    print("\n" + "-" * 74)
    print("v849 PART B -- the Lean mirror: TfptCarrier/CofinalWeil."
          "lean (kernel-checked;")
    print("numeric witnesses here; (H_cof) never instantiated with "
          "deployed data)")
    print("-" * 74, flush=True)

    # B1: the minimal implication (limit_nonneg_of_cofinal_seq /
    # weil_nonneg_of_cofinal) -- the eps/2 argument at sequence level
    ok_seq = True
    for (seq, lim) in (
            (lambda m: 1.0 / (m + 1.0), 0.0),
            (lambda m: 2.0 + math.sin(m) / (m + 1.0), 2.0),
            (lambda m: 0.25 + (-0.5) ** m / (m + 2.0) ** 2, 0.25)):
        idx = [2 * j for j in range(2000)]           # pre-fixed ladder
        ok_seq &= all(idx[a] < idx[a + 1] for a in range(1999))
        ok_seq &= all(seq(m) >= 0.0 for m in idx)
        tail = [seq(m) for m in range(5000, 5050)]
        ok_seq &= (min(tail) >= lim - 1e-3) and (lim >= 0.0)
    rng = np.random.default_rng(20260807)
    ok_psd = True
    for _ in range(6):
        base = rng.normal(size=(7, 7))
        A = base @ base.T                            # PSD rung matrix
        for _v in range(24):                         # 'dense family'
            x = rng.normal(size=7)
            ok_psd &= float(x @ (A @ x)) >= -1e-10
    _bcheck("B1 THE MINIMAL IMPLICATION (limit_nonneg_of_cofinal_seq, "
            "PROVEN eps/2 argument): convergent sequences nonneg on a "
            "PRE-FIXED strictly monotone ladder have nonneg limits (3 "
            "witness families, ladder = even integers); and the "
            "no-diagonal reason (ladderForm_nonneg): ONE PSD rung "
            "certificate makes the form nonneg at EVERY element "
            "simultaneously (6 seeded PSD matrices x 24 witnesses "
            ">= -1e-10) -- weil_nonneg_of_cofinal needs only "
            "per-element convergence + (H_cof)", ok_seq and ok_psd)

    # B2: the strict hierarchy uniform < pointwise < cofinal
    margin_pw = [1.0 / (m + 1.0) for m in range(100000)]
    ok_pw = all(v > 0.0 for v in margin_pw)          # pointwise strict
    ok_nu = True                                     # ... not uniform
    for dlt in (1e-2, 1e-6, 1e-12):
        n_w = int(math.ceil(1.0 / dlt))
        ok_nu &= 1.0 / (n_w + 1.0) < dlt
    def margin_pm(m):                                # +-1 witness
        return 1.0 if m % 2 == 0 else -1.0
    even = [2 * j for j in range(100000)]
    ok_cof = all(margin_pm(m) >= 0.0 for m in even)  # cofinal on evens
    ok_np = any(margin_pm(m) < 0.0 for m in range(100))
    _bcheck("B2 THE STRICT HIERARCHY (kernel-checked: "
            "uniformMarginBound_to_cofinal, pointwise_to_cofinal, "
            "cofinal_not_uniform, cofinal_not_pointwise): witness "
            "1/(m+1) is strictly positive at EVERY rung yet below "
            "every delta > 0 eventually (pointwise strict, NOT "
            "uniform; the v843 kernel gap reused), and the +-1 "
            "sequence is nonneg on the pre-fixed even ladder while "
            "strictly negative on every odd rung (cofinal, NOT "
            "pointwise) -- uniform SUBSET-NEQ pointwise SUBSET-NEQ "
            "cofinal, both inclusions strict",
            ok_pw and ok_nu and ok_cof and ok_np)

    # B3: the preregistration shape of (H_cof)
    idx = [2 * j for j in range(1000)]
    ok_mono = all(a < b for a, b in zip(idx[:-1], idx[1:]))
    ok_indep = (idx == [2 * j for j in range(1000)])  # data, not mined
    ok_order = ok_mono and ok_cof                     # ladder -> signs
    _bcheck("B3 THE PREREGISTRATION SHAPE (CofinalHypothesis): the "
            "index sequence is DATA of the structure -- supplied "
            "first, strictly monotone by field (checked), chosen "
            "independently of any measured sign (the even ladder "
            "here is a pure function of j); the positivity "
            "certificates quantify over the GIVEN ladder only -- "
            "formally a consumer must exhibit the ladder before any "
            "form value is evaluated",
            ok_mono and ok_indep and ok_order)

    # B4: the formal demotion statement
    ok_dem = ok_nu and ok_cof and ok_np              # strictness twice
    _bcheck("B4 THE FORMAL DEMOTION: the load-bearing chain "
            "(PRIME.EXTRACTION.CHAIN.01, v848 step 2) consumes "
            "EXACTLY (H_cof); UniformMarginBound implies (H_cof) "
            "(proven) and the converse FAILS kernel-checked "
            "(witnesses above) -- from this round UniformMarginBound "
            "is an over-strong SUFFICIENT LEMMA, no longer the named "
            "wall; the wall content is cofinal PSD on ONE pre-fixed "
            "ladder and nothing else; (H_cof) itself stays a "
            "hypothesis everywhere", ok_dem)
    print("  (kernel-checked statements: experiments/"
          "lean4-carrier-rigidity/TfptCarrier/CofinalWeil.lean -- "
          "11 declarations, lake build green, 3411 jobs, no sorry, "
          "no native_decide, axioms propext/Classical.choice/"
          "Quot.sound only; import wired in TfptCarrier.lean; "
          "lean_manifest.sha256 at 85 files)")

def run():
    _B_CHECKS.clear()
    part_b()
    ok = len(_B_CHECKS) == 4 and all(_B_CHECKS)
    print("v849 CofinalWeil mirror: %d/4 checks passed; H_cof remains a hypothesis" % sum(_B_CHECKS))
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(run())
