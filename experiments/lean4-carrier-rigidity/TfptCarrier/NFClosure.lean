/-
  NFClosure — the round-122 NF-closure kernel and its honesty lock.
  =================================================================

  Lean seam of round 122 (PRIME.RADIUS4.AUBINNITSCHE.01; note
  CDXXIII, contract PRIME.RADIUS4.LEAN.01): the finite determinant
  quotient's contraction kernel, matching the sympy-exact gates of
  `experiments/tfpt-discovery/radius4_an_probe.py` (G10-det-factor,
  G11-contraction, G13-trace-chain) and the round-117 R3a chain of
  `radius4_reduction_probe.py`.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`):

    (1) `contractionKernel_mem_Icc` — THE SCALAR NF KERNEL (probe
        gate G11): for every real eigenvalue μ of a self-adjoint
        block and every a > 0, the mapped value
        aμ²/(a+μ²)² lies in [0, 1/4], exactly because
        (a+μ²)² - 4aμ² = (a-μ²)² ≥ 0.  `eigenvalues_mem_Icc` — the
        same for every member of a finite eigenvalue family: in
        eigenvalue form, the spectrum of B = aM²(a+M²)⁻² lies in
        [0, 1/4].

    (2) `det_factor_vieta` / `det_factor_kernel` — the determinant
        factor (probe gate G10): with z₊ + z₋ = a(2-t) and
        z₊z₋ = a², each eigenvalue contributes
        (μ²+z₊)(μ²+z₋) = (μ²+a)² - taμ² = (μ²+a)²(1 - t·aμ²/(a+μ²)²).

    (3) `sum_pow_le_trace` — THE TRACE INEQUALITY in eigenvalue form
        (round-117 R3a / probe gate G13): for a finite family
        b : ι → ℝ with every b i ∈ [0, 1/4] and k ≥ 1,
        Σ (b i)^k ≤ (1/4)^{k-1} · Σ b i — i.e. Tr B^k ≤ 4^{1-k} Tr B.

    (4) `log_inv_one_sub_le` — the scalar log chain of the
        normal-family bound (probe gate G13, second half):
        log(1/(1-u)) ≤ u/(1-u) for u < 1, from the classical
        log x ≤ x - 1.

    (5) `NFClosureSkeleton` — THE ROUND-122 NF-CLOSURE THEOREM AS A
        TYPED HYPOTHESIS PACKAGE (the SVSkeleton discipline):
        `spectral_map_step` (round-114 block realness + functional
        calculus, cited NOT proven) and
        `vitali_hurwitz_identity_step` (Montel/Vitali normal
        families, Hurwitz, the identity theorem — cited NOT proven)
        are NAMED HYPOTHESES; `nf_implies_rh` composes them;
        `nfSkeleton_inhabited` shows consistency and
        `nfSkeleton_not_unconditional` — THE HONESTY LOCK — shows
        the package alone proves NO RH-shaped statement.

  THE HONEST BOUNDARY.  The kernel-checked content is the finite
  eigenvalue algebra: the scalar contraction, the determinant
  factor, the trace-power inequality and the scalar log bound.  The
  OPERATOR statement 0 ≤ B ≤ 1/4 for B = aM²(a+M²)⁻² needs the
  spectral theorem applied to the round-114 CCM operators — that
  identification (`spectral_map_step`), the convergence hypothesis
  (H-conv), the trace bound (H-trace), the dense-a quantifier and
  the classical Vitali/Hurwitz hull are NAMED HYPOTHESES here, in
  the exact sense of `SVSkeleton`'s discipline: nothing about ζ,
  CCM operators, or normal families is proven.  The module's own
  honesty lock proves no unconditional conclusion can be extracted
  from the packaging.  No RH claim in any direction.
-/
import TfptCarrier.Radius4Algebra
import Mathlib.Analysis.SpecialFunctions.Log.Basic

namespace TfptCarrier
namespace NFClosure

/-! ### (1) The scalar NF kernel -/

/-- The NF contraction kernel: the image of a real eigenvalue μ
under the round-122 map `μ ↦ aμ²/(a+μ²)²` (the eigenvalue form of
B = aM²(a+M²)⁻²).  Definitionally `Radius4Algebra.wOnLine`. -/
noncomputable def contractionKernel (a μ : ℝ) : ℝ :=
  a * μ ^ 2 / (a + μ ^ 2) ^ 2

/-- Dictionary lock: the NF kernel IS the on-line radius-4 rate. -/
theorem contractionKernel_eq_wOnLine (a μ : ℝ) :
    contractionKernel a μ = Radius4Algebra.wOnLine a μ :=
  rfl

/-- **THE SCALAR NF KERNEL BOUND** (probe gate G11): for a > 0 and
every real μ, `aμ²/(a+μ²)² ∈ [0, 1/4]` — real spectrum makes the
determinant-quotient block an automatic 1/4-contraction. -/
theorem contractionKernel_mem_Icc {a : ℝ} (ha : 0 < a) (μ : ℝ) :
    contractionKernel a μ ∈ Set.Icc (0 : ℝ) (1 / 4) :=
  ⟨Radius4Algebra.wOnLine_nonneg ha μ,
   Radius4Algebra.wOnLine_le_quarter ha μ⟩

/-- **The eigenvalue-multiset form** (round 122, requirement (b) at
finite level): every member of a finite real eigenvalue family maps
into [0, 1/4] — in eigenvalue form, spec(B) ⊆ [0, 1/4]. -/
theorem eigenvalues_mem_Icc {ι : Type*} {a : ℝ} (ha : 0 < a)
    (μ : ι → ℝ) (i : ι) :
    contractionKernel a (μ i) ∈ Set.Icc (0 : ℝ) (1 / 4) :=
  contractionKernel_mem_Icc ha (μ i)

/-! ### (2) The determinant factor -/

/-- **The Vieta half of the determinant factor** (probe gate G10):
with z₊ + z₋ = a(2-t) and z₊z₋ = a²,
`(m2+z₊)(m2+z₋) = (m2+a)² - t·a·m2` exactly. -/
theorem det_factor_vieta {a t zp zm : ℝ} (m2 : ℝ)
    (hsum : zp + zm = a * (2 - t)) (hprod : zp * zm = a ^ 2) :
    (m2 + zp) * (m2 + zm) = (m2 + a) ^ 2 - t * a * m2 := by
  have h : (m2 + zp) * (m2 + zm)
      = m2 ^ 2 + (zp + zm) * m2 + zp * zm := by ring
  rw [h, hsum, hprod]
  ring

/-- **The kernel half of the determinant factor** (probe gate G10):
`(μ²+a)²(1 - t·aμ²/(a+μ²)²) = (μ²+a)² - t·a·μ²` — the per-eigenvalue
factor of det(I - tB) in closed form. -/
theorem det_factor_kernel {a : ℝ} (t μ : ℝ) (h : a + μ ^ 2 ≠ 0) :
    (μ ^ 2 + a) ^ 2 * (1 - t * contractionKernel a μ)
      = (μ ^ 2 + a) ^ 2 - t * a * μ ^ 2 := by
  unfold contractionKernel
  field_simp
  ring

/-! ### (3) The trace inequality in eigenvalue form -/

/-- **THE TRACE-POWER INEQUALITY** (round-117 R3a / probe gate G13,
eigenvalue form): if every b i lies in [0, 1/4] then
`Σ (b i)^k ≤ (1/4)^{k-1} · Σ b i` for every k ≥ 1 — i.e.
Tr B^k ≤ 4^{1-k} Tr B for the NF-closure block. -/
theorem sum_pow_le_trace {ι : Type*} [Fintype ι] (b : ι → ℝ)
    (hb : ∀ i, b i ∈ Set.Icc (0 : ℝ) (1 / 4)) {k : ℕ} (hk : 1 ≤ k) :
    ∑ i, b i ^ k ≤ (1 / 4 : ℝ) ^ (k - 1) * ∑ i, b i := by
  rw [Finset.mul_sum]
  refine Finset.sum_le_sum fun i _ => ?_
  obtain ⟨h0, h4⟩ := hb i
  have hk' : k - 1 + 1 = k := Nat.sub_add_cancel hk
  have hpow : b i ^ (k - 1) ≤ (1 / 4 : ℝ) ^ (k - 1) := by
    first
    | exact pow_le_pow_left h0 h4 _
    | exact pow_le_pow_left₀ h0 h4 _
  calc b i ^ k = b i ^ (k - 1 + 1) := by rw [hk']
    _ = b i ^ (k - 1) * b i := pow_succ _ _
    _ ≤ (1 / 4 : ℝ) ^ (k - 1) * b i :=
        mul_le_mul_of_nonneg_right hpow h0

/-! ### (4) The scalar log chain -/

/-- **The scalar log bound of the normal-family estimate** (probe
gate G13, second half): `log(1/(1-u)) ≤ u/(1-u)` for u < 1 — the
per-eigenvalue step of |log det(I-tB)| ≤ Tr B · r/(1-r/4), from the
classical log x ≤ x - 1. -/
theorem log_inv_one_sub_le {u : ℝ} (hu : u < 1) :
    Real.log (1 / (1 - u)) ≤ u / (1 - u) := by
  have h1 : 0 < 1 - u := by linarith
  have h2 : (0 : ℝ) < 1 / (1 - u) := by positivity
  calc Real.log (1 / (1 - u)) ≤ 1 / (1 - u) - 1 :=
        Real.log_le_sub_one_of_pos h2
    _ = u / (1 - u) := by
        field_simp
        ring

/-! ### (5) The NF-closure skeleton and its honesty lock -/

/-- **THE ROUND-122 NF-CLOSURE THEOREM AS A TYPED HYPOTHESIS
PACKAGE** — every field is a NAMED HYPOTHESIS with its citation;
none is proven here (see module docstring).  The five `Prop`
parameters keep the package fully abstract: nothing about ζ, CCM
operators, determinants, or half-planes is smuggled into the
kernel. -/
structure NFClosureSkeleton where
  /-- The round-114 input (cited, NOT proven): the CCM block
  operators M_λ have unconditionally real spectrum (the blockreal
  theorem). -/
  SpectrumReal : Prop
  /-- The operator contraction 0 ≤ B ≤ 1/4 for B = aM²(a+M²)⁻²
  (its EIGENVALUE form is kernel-checked above:
  `contractionKernel_mem_Icc`). -/
  BContraction : Prop
  /-- (H-conv): R_{a,λ}(t) → R_a(t) = Φ(z₊)Φ(z₋)/Φ(a)² pointwise on
  a subinterval of the Euler interval (0, 4-1/a), for every a in a
  dense subset — the round-122 Ω, measured in Lane A, NOT proven. -/
  HConv : Prop
  /-- (H-trace): sup_λ Tr B_{a,λ} < ∞ — the second Ω input. -/
  HTrace : Prop
  /-- The RH-shaped conclusion (opaque — no zeta content in Lean). -/
  RH : Prop
  /-- NAMED HYPOTHESIS 1 (spectral theorem / functional calculus on
  the round-114 realness — cited, NOT proven): real spectrum forces
  the operator contraction whose scalar content is
  `contractionKernel_mem_Icc`. -/
  spectral_map_step : SpectrumReal → BContraction
  /-- NAMED HYPOTHESIS 2 (Montel/VITALI normal families, HURWITZ,
  the identity theorem — cited, NOT proven): the contraction plus
  (H-conv) plus (H-trace) on a dense a-set give the zero-free hull
  and the RH-shaped conclusion. -/
  vitali_hurwitz_identity_step : BContraction → HConv → HTrace → RH

/-- **The composition** — the only theorem the skeleton yields, with
its conditionality fully visible in the type: real spectrum plus
(H-conv) plus (H-trace) plus the two named classical inputs give
the conclusion.  The quantifier structure of the round-122 theorem
is thereby kernel-checked; the analysis is not. -/
theorem nf_implies_rh (S : NFClosureSkeleton) (hreal : S.SpectrumReal)
    (hconv : S.HConv) (htrace : S.HTrace) : S.RH :=
  S.vitali_hurwitz_identity_step (S.spectral_map_step hreal) hconv htrace

/-- Non-vacuity: the package is consistent (inhabited with all nodes
True). -/
theorem nfSkeleton_inhabited : Nonempty NFClosureSkeleton :=
  ⟨{ SpectrumReal := True, BContraction := True, HConv := True,
     HTrace := True, RH := True,
     spectral_map_step := fun h => h,
     vitali_hurwitz_identity_step := fun h _ _ => h }⟩

/-- **THE HONESTY LOCK**: the skeleton proves nothing
unconditionally — there is an instance whose conclusion is False
(all nodes False, implications vacuous).  Any RH-shaped output must
enter through the round-114 realness, (H-conv), (H-trace) and the
named classical hull, never from the packaging. -/
theorem nfSkeleton_not_unconditional :
    ∃ S : NFClosureSkeleton, ¬ S.RH ∧ ¬ S.SpectrumReal ∧ ¬ S.HConv :=
  ⟨{ SpectrumReal := False, BContraction := False, HConv := False,
     HTrace := False, RH := False,
     spectral_map_step := fun h => h,
     vitali_hurwitz_identity_step := fun h _ _ => h },
   fun h => h, fun h => h, fun h => h⟩

end NFClosure
end TfptCarrier
