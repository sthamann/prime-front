/-
  AntiAliasExact — the exact anti-alias quadrature core of the
  handoff frequency Gram.
  ==================================================================

  Machine-checked core of the anti-alias exactness round (intended
  promotion target v760_antialias_exact).  Numeric counterpart:
  experiments/tfpt-discovery/antialias_exact_probe.py (14/14,
  verdict ANTIALIAS-CORRECTED: the sharp minimal uniform frequency
  count for the M-cell Gram construction is Nf = 2M-1, a DOWNWARD
  correction of the deployed-but-not-minimal 2M+1; every deployed
  count stays exact).

  THE SETTING.  The deployed source Gram integrates products
  s(θ)·conj(F_u(θ))·F_v(θ) over the uniform Nf-point frequency grid,
  where s has symbol degree ≤ M-1 and F_u, F_v are lattice Fourier
  transforms of coefficient vectors supported on {0,…,M-1} (spread
  ≤ M-1).  Writing ζ for a primitive Nf-th root of unity, the grid
  node values of every such integrand are ℤ-indexed Laurent
  polynomials in ζ^k, and every identity of the probe reduces to the
  discrete orthogonality of the root-of-unity powers.  Formalized
  here, kernel-checked (no sorry, no native_decide, no decide):

  O (discrete orthogonality, general N over any field):
    * `sum_zpow_eq_card_of_dvd` / `sum_zpow_eq_zero_of_not_dvd` /
      `sum_zpow_ite` — ∑_{k<N} ζ^{mk} = N if N ∣ m, else 0
      (geometric sum against ζ^m ≠ 1).

  Q (the exact quadrature identity, ARBITRARY grid offset):
    * `quadrature_exact` — for ANY coefficient function c : ℤ → K,
      ANY offset w (midpoint AND endpoint grids alike) and total
      degree d < N:  ∑_{k<N} ∑_{|m|≤d} c m · (w·ζ^k)^m = N · c 0.
      This is the statement "the uniform N-grid integrates every
      trigonometric polynomial of degree < N exactly"; the Gram
      budget instance is d = (M-1) + (M-1) = 2M-2.
    * `quadrature_exact_center` — the offset-free special case.

  P (discrete Parseval, the arbitrary-coefficient handoff identity):
    * `discrete_parseval` — for ANY u, v supported on {0,…,M-1} and
      M ≤ N:  ∑_{k<N} (∑_i u i·ζ^{-ik})(∑_j v j·ζ^{jk}) = N·∑ u i·v i
      (over ℂ with |ζ| = 1 the inverse powers ARE the conjugates).

  M (moment reconstruction — exactly what the Gram needs):
    * `moment_reconstruction` — symbol coefficients p on |m| ≤ ds,
      lattice shift |t| ≤ dt, ds + dt < N:
      ∑_{k<N} s(ζ^k)·ζ^{tk} = N · (p(-t) extended by zero) — the
      quadrature reproduces every Toeplitz moment of the Gram.

  W (the sharp threshold, both sides):
    * `alias_witness` / `alias_witness_offset` — frequency N aliases
      onto the constant: ∑_{k<N} ζ^{Nk} = N (≠ 0 = the true moment);
      with offset the alias picks up the factor w^N.
    * `threshold_witness` — at N = ds + dt (ONE below the sharp
      bound ds + dt + 1) the product of the degree-ds symbol mode
      and the degree-dt lattice mode sums to N; `threshold_witness_ne_zero`
      (char 0): the quadrature value N differs from the true moment 0
      — the must-fail witness of the probe.
    * `threshold_witness_exact_above` — the SAME integrand is
      integrated exactly (to 0) by every N > ds + dt: the bound
      ds + dt + 1 is sharp from both sides.

  G (the Gram-budget corollaries, concrete counts):
    * `gram_budget_exact_at_sharp`   — Nf = 2M-1 (the corrected
      minimal count) integrates the full budget d ≤ 2M-2 exactly;
    * `gram_budget_exact_at_deployed` — so does the deployed 2M+1;
    * `below_sharp_fails` — at Nf = 2M-2 the explicit witness
      (symbol mode M-1 × lattice mode M-1) gives a nonzero
      quadrature error (char 0): Nf = 2M-1 is minimal.

  C (the ℂ instance and the midpoint sign):
    * `complex_grid_isPrimitiveRoot` — ζ_N = exp(2πi/N) instantiates
      every theorem above;
    * `midpoint_offset_pow` — the midpoint offset w = exp(πi/N)
      satisfies w^N = -1;
    * `midpoint_alias_sign` — on the midpoint grid the aliased
      frequency-N character sums to -N: the (-1)^r sign in the
      probe's alias formula t_d = ∑_r (-1)^r ŝ(rNf - d).

  HONEST SCOPE.  General-N statements throughout (no concrete-
  instance stand-ins); the core O/Q/P/M/W blocks hold over an
  arbitrary field, the witness non-vanishing needs characteristic
  zero, and the C block is the ℂ instantiation.  NOT formalized
  (probe territory): the Fejér reparametrization p ↦ ŝ (a diagonal
  bijection with weights 1-d/M), the identification of the algebraic
  sums with the analytic integrals over [0,2π), the positive-part
  clip convention, the 24-function battery, and the floating-point
  semantics of the numeric run.

  Standalone module: no imports from other TfptCarrier files (built
  while a concurrent worker may hold the TfptCarrier.lean import
  list).
-/
import Mathlib.RingTheory.RootsOfUnity.PrimitiveRoots
import Mathlib.RingTheory.RootsOfUnity.Complex
import Mathlib.Algebra.Ring.GeomSum
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

set_option maxRecDepth 100000
set_option maxHeartbeats 1000000

open Finset

namespace TfptCarrier.AntiAliasExact

variable {K : Type*} [Field K] {N : ℕ} {ζ : K}

/-! ### O. Discrete orthogonality of the uniform frequency grid -/

/-- Aliased case: if N divides the frequency m, every grid power is 1
and the sum is N (the aliasing mass). -/
theorem sum_zpow_eq_card_of_dvd (hζ : IsPrimitiveRoot ζ N) {m : ℤ}
    (hm : (N : ℤ) ∣ m) :
    ∑ k ∈ range N, ζ ^ (m * (k : ℤ)) = (N : K) := by
  have hone : ζ ^ m = 1 := (hζ.zpow_eq_one_iff_dvd m).mpr hm
  have hterm : ∀ k ∈ range N, ζ ^ (m * (k : ℤ)) = 1 := by
    intro k _
    rw [zpow_mul, hone, one_zpow]
  rw [Finset.sum_congr rfl hterm]
  simp

/-- **Discrete orthogonality**: a frequency m NOT divisible by N sums
to zero over the uniform N-grid — the geometric sum against
ζ^m ≠ 1 with (ζ^m)^N = 1. -/
theorem sum_zpow_eq_zero_of_not_dvd (hζ : IsPrimitiveRoot ζ N) {m : ℤ}
    (hm : ¬ (N : ℤ) ∣ m) :
    ∑ k ∈ range N, ζ ^ (m * (k : ℤ)) = 0 := by
  set z : K := ζ ^ m with hz
  have hne : z ≠ 1 := fun h => hm ((hζ.zpow_eq_one_iff_dvd m).mp h)
  have hzN : z ^ N = 1 := by
    rw [hz, ← zpow_natCast (ζ ^ m) N, ← zpow_mul, mul_comm m (N : ℤ),
      zpow_mul, hζ.zpow_eq_one, one_zpow]
  have hgeom : (∑ k ∈ range N, z ^ k) * (z - 1) = 0 := by
    rw [geom_sum_mul, hzN, sub_self]
  have hsum : ∑ k ∈ range N, z ^ k = 0 := by
    rcases mul_eq_zero.mp hgeom with h | h
    · exact h
    · exact absurd (sub_eq_zero.mp h) hne
  calc ∑ k ∈ range N, ζ ^ (m * (k : ℤ))
      = ∑ k ∈ range N, z ^ k := by
        refine Finset.sum_congr rfl fun k _ => ?_
        rw [hz, ← zpow_natCast (ζ ^ m) k, ← zpow_mul]
    _ = 0 := hsum

/-- The two orthogonality cases as one closed formula. -/
theorem sum_zpow_ite (hζ : IsPrimitiveRoot ζ N) (m : ℤ) :
    ∑ k ∈ range N, ζ ^ (m * (k : ℤ))
      = if (N : ℤ) ∣ m then (N : K) else 0 := by
  by_cases h : (N : ℤ) ∣ m
  · rw [if_pos h]; exact sum_zpow_eq_card_of_dvd hζ h
  · rw [if_neg h]; exact sum_zpow_eq_zero_of_not_dvd hζ h

/-- Degree arithmetic: a frequency inside the budget |m| ≤ d < N that
is divisible by N must be zero — the no-alias condition. -/
theorem freq_eq_zero_of_dvd {m : ℤ} {d : ℕ} (hdvd : (N : ℤ) ∣ m)
    (hm : m ∈ Icc (-(d : ℤ)) (d : ℤ)) (hd : d < N) : m = 0 := by
  refine Int.eq_zero_of_dvd_of_natAbs_lt_natAbs hdvd ?_
  simp only [Finset.mem_Icc] at hm
  omega

/-! ### Q. The exact quadrature identity (arbitrary grid offset) -/

/-- **Exact quadrature**: the uniform N-point grid with ARBITRARY
offset w (midpoint and endpoint grids alike — the algebraic identity
needs no invertibility of the offset) integrates every trigonometric
polynomial of degree ≤ d < N exactly: for ARBITRARY coefficients
c : ℤ → K the grid sum collapses to N times the constant
coefficient. -/
theorem quadrature_exact (hζ : IsPrimitiveRoot ζ N) (w : K)
    (c : ℤ → K) {d : ℕ} (hd : d < N) :
    ∑ k ∈ range N, ∑ m ∈ Icc (-(d : ℤ)) (d : ℤ),
        c m * (w * ζ ^ (k : ℤ)) ^ m
      = (N : K) * c 0 := by
  rw [Finset.sum_comm]
  have hterm : ∀ m ∈ Icc (-(d : ℤ)) (d : ℤ),
      ∑ k ∈ range N, c m * (w * ζ ^ (k : ℤ)) ^ m
        = if m = 0 then (N : K) * c 0 else 0 := by
    intro m hm
    have hexp : ∀ k ∈ range N,
        c m * (w * ζ ^ (k : ℤ)) ^ m
          = c m * w ^ m * ζ ^ (m * (k : ℤ)) := by
      intro k _
      rw [mul_zpow, ← zpow_mul, mul_comm (k : ℤ) m, mul_assoc]
    rw [Finset.sum_congr rfl hexp, ← Finset.mul_sum, sum_zpow_ite hζ m]
    by_cases h0 : m = 0
    · subst h0
      simp [mul_comm]
    · have hnd : ¬ (N : ℤ) ∣ m := fun hdvd =>
        h0 (freq_eq_zero_of_dvd hdvd hm hd)
      rw [if_neg hnd, if_neg h0, mul_zero]
  rw [Finset.sum_congr rfl hterm,
    Finset.sum_ite_eq' (Icc (-(d : ℤ)) (d : ℤ)) 0
      (fun _ => (N : K) * c 0),
    if_pos (by simp only [Finset.mem_Icc]; omega :
      (0 : ℤ) ∈ Icc (-(d : ℤ)) (d : ℤ))]

/-- The offset-free (endpoint-grid) special case w = 1. -/
theorem quadrature_exact_center (hζ : IsPrimitiveRoot ζ N)
    (c : ℤ → K) {d : ℕ} (hd : d < N) :
    ∑ k ∈ range N, ∑ m ∈ Icc (-(d : ℤ)) (d : ℤ),
        c m * (ζ ^ (k : ℤ)) ^ m
      = (N : K) * c 0 := by
  simpa using quadrature_exact hζ (1 : K) c hd

/-! ### P. Discrete Parseval for arbitrary coefficient vectors -/

/-- **Discrete Parseval**: for ARBITRARY coefficient vectors u, v
supported on the M-cell lattice {0,…,M-1} and any count N ≥ M, the
grid inner product of the lattice Fourier transforms equals N times
the lattice inner product.  (Over ℂ with |ζ| = 1 the inverse powers
ζ^{-ik} are exactly the conjugated transform values.) -/
theorem discrete_parseval (hζ : IsPrimitiveRoot ζ N) (hN : N ≠ 0)
    (u v : ℕ → K) {M : ℕ} (hMN : M ≤ N) :
    ∑ k ∈ range N,
        (∑ i ∈ range M, u i * ζ ^ (-(i : ℤ) * (k : ℤ)))
      * (∑ j ∈ range M, v j * ζ ^ ((j : ℤ) * (k : ℤ)))
      = (N : K) * ∑ i ∈ range M, u i * v i := by
  have hz : ζ ≠ 0 := hζ.ne_zero hN
  have hexpand : ∀ k ∈ range N,
      (∑ i ∈ range M, u i * ζ ^ (-(i : ℤ) * (k : ℤ)))
        * (∑ j ∈ range M, v j * ζ ^ ((j : ℤ) * (k : ℤ)))
      = ∑ i ∈ range M, ∑ j ∈ range M,
          u i * v j * ζ ^ (((j : ℤ) - (i : ℤ)) * (k : ℤ)) := by
    intro k _
    rw [Finset.sum_mul_sum]
    refine Finset.sum_congr rfl fun i _ =>
      Finset.sum_congr rfl fun j _ => ?_
    rw [mul_mul_mul_comm, ← zpow_add₀ hz]
    congr 1
    ring_nf
  rw [Finset.sum_congr rfl hexpand, Finset.sum_comm]
  have hinner : ∀ i ∈ range M,
      (∑ k ∈ range N, ∑ j ∈ range M,
          u i * v j * ζ ^ (((j : ℤ) - (i : ℤ)) * (k : ℤ)))
        = (N : K) * (u i * v i) := by
    intro i hi
    rw [Finset.sum_comm]
    have hcell : ∀ j ∈ range M,
        ∑ k ∈ range N, u i * v j * ζ ^ (((j : ℤ) - (i : ℤ)) * (k : ℤ))
          = if j = i then (N : K) * (u i * v i) else 0 := by
      intro j hj
      rw [← Finset.mul_sum, sum_zpow_ite hζ ((j : ℤ) - (i : ℤ))]
      by_cases hij : j = i
      · subst hij
        simp [mul_comm]
      · have hnd : ¬ (N : ℤ) ∣ ((j : ℤ) - (i : ℤ)) := by
          intro hdvd
          have hzero : (j : ℤ) - (i : ℤ) = 0 :=
            Int.eq_zero_of_dvd_of_natAbs_lt_natAbs hdvd (by
              simp only [Finset.mem_range] at hi hj
              omega)
          exact hij (by omega)
        rw [if_neg hnd, if_neg hij, mul_zero]
    rw [Finset.sum_congr rfl hcell,
      Finset.sum_ite_eq' (range M) i
        (fun _ => (N : K) * (u i * v i)),
      if_pos hi]
  rw [Finset.sum_congr rfl hinner, ← Finset.mul_sum]

/-! ### M. Exact reconstruction of the Gram moments -/

/-- **Moment reconstruction**: the Gram construction needs exactly the
moments ∑_k s(node_k)·ζ^{tk} for lattice shifts |t| ≤ dt of the
degree-ds symbol s.  For every count N > ds + dt the quadrature
returns N times the true Toeplitz moment p(-t) (extended by zero) —
for ARBITRARY symbol coefficients p : ℤ → K. -/
theorem moment_reconstruction (hζ : IsPrimitiveRoot ζ N)
    (p : ℤ → K) {ds dt : ℕ} (t : ℤ) (ht : t.natAbs ≤ dt)
    (hd : ds + dt < N) :
    ∑ k ∈ range N,
        (∑ m ∈ Icc (-(ds : ℤ)) (ds : ℤ), p m * ζ ^ (m * (k : ℤ)))
      * ζ ^ (t * (k : ℤ))
      = (N : K)
        * (if -t ∈ Icc (-(ds : ℤ)) (ds : ℤ) then p (-t) else 0) := by
  have hz : ζ ≠ 0 := hζ.ne_zero (by omega)
  have hexpand : ∀ k ∈ range N,
      (∑ m ∈ Icc (-(ds : ℤ)) (ds : ℤ), p m * ζ ^ (m * (k : ℤ)))
        * ζ ^ (t * (k : ℤ))
      = ∑ m ∈ Icc (-(ds : ℤ)) (ds : ℤ),
          p m * ζ ^ ((m + t) * (k : ℤ)) := by
    intro k _
    rw [Finset.sum_mul]
    refine Finset.sum_congr rfl fun m _ => ?_
    rw [mul_assoc, ← zpow_add₀ hz]
    congr 1
    ring_nf
  rw [Finset.sum_congr rfl hexpand, Finset.sum_comm]
  have hcell : ∀ m ∈ Icc (-(ds : ℤ)) (ds : ℤ),
      ∑ k ∈ range N, p m * ζ ^ ((m + t) * (k : ℤ))
        = if m = -t then p m * (N : K) else 0 := by
    intro m hmem
    rw [← Finset.mul_sum, sum_zpow_ite hζ (m + t)]
    by_cases hmt : m = -t
    · subst hmt
      simp
    · have hnd : ¬ (N : ℤ) ∣ (m + t) := by
        intro hdvd
        have hzero : m + t = 0 :=
          Int.eq_zero_of_dvd_of_natAbs_lt_natAbs hdvd (by
            simp only [Finset.mem_Icc] at hmem
            omega)
        exact hmt (by omega)
      rw [if_neg hnd, if_neg hmt, mul_zero]
  rw [Finset.sum_congr rfl hcell,
    Finset.sum_ite_eq' (Icc (-(ds : ℤ)) (ds : ℤ)) (-t)
      (fun m => p m * (N : K))]
  by_cases hmem : -t ∈ Icc (-(ds : ℤ)) (ds : ℤ)
  · rw [if_pos hmem, if_pos hmem, mul_comm]
  · rw [if_neg hmem, if_neg hmem, mul_zero]

/-! ### W. The sharp threshold: witnesses on both sides -/

/-- Frequency N aliases onto the constant: the uniform N-grid sums the
frequency-N character to N — while its true moment is 0. -/
theorem alias_witness (hζ : IsPrimitiveRoot ζ N) :
    ∑ k ∈ range N, ζ ^ ((N : ℤ) * (k : ℤ)) = (N : K) :=
  sum_zpow_eq_card_of_dvd hζ dvd_rfl

/-- The offset version: the aliased frequency-N character picks up the
factor w^N (for the midpoint grid this is the sign -1, see
`midpoint_alias_sign`). -/
theorem alias_witness_offset (hζ : IsPrimitiveRoot ζ N) (w : K) :
    ∑ k ∈ range N, (w * ζ ^ (k : ℤ)) ^ (N : ℤ)
      = (N : K) * w ^ (N : ℤ) := by
  have hterm : ∀ k ∈ range N,
      (w * ζ ^ (k : ℤ)) ^ (N : ℤ)
        = w ^ (N : ℤ) * ζ ^ ((N : ℤ) * (k : ℤ)) := by
    intro k _
    rw [mul_zpow, ← zpow_mul, mul_comm (k : ℤ) (N : ℤ)]
  rw [Finset.sum_congr rfl hterm, ← Finset.mul_sum, alias_witness hζ,
    mul_comm]

/-- **The must-fail witness**: at N = ds + dt — one below the sharp
bound ds + dt + 1 — the product of the degree-ds symbol mode and the
degree-dt lattice mode aliases onto the constant and sums to N. -/
theorem threshold_witness (hζ : IsPrimitiveRoot ζ N) {ds dt : ℕ}
    (hsum : ds + dt = N) (hpos : 0 < N) :
    ∑ k ∈ range N, ζ ^ ((ds : ℤ) * (k : ℤ)) * ζ ^ ((dt : ℤ) * (k : ℤ))
      = (N : K) := by
  have hz : ζ ≠ 0 := hζ.ne_zero (by omega)
  have hterm : ∀ k ∈ range N,
      ζ ^ ((ds : ℤ) * (k : ℤ)) * ζ ^ ((dt : ℤ) * (k : ℤ))
        = ζ ^ ((N : ℤ) * (k : ℤ)) := by
    intro k _
    rw [← zpow_add₀ hz]
    congr 1
    rw [← add_mul]
    congr 1
    exact_mod_cast hsum
  rw [Finset.sum_congr rfl hterm, alias_witness hζ]

/-- In characteristic zero the witness FIRES: the quadrature value N
differs from the true moment 0 — exactness fails at N = ds + dt. -/
theorem threshold_witness_ne_zero [CharZero K]
    (hζ : IsPrimitiveRoot ζ N) {ds dt : ℕ}
    (hsum : ds + dt = N) (hpos : 0 < N) :
    ∑ k ∈ range N, ζ ^ ((ds : ℤ) * (k : ℤ)) * ζ ^ ((dt : ℤ) * (k : ℤ))
      ≠ 0 := by
  rw [threshold_witness hζ hsum hpos]
  exact_mod_cast hpos.ne'

/-- The SAME witness integrand is integrated exactly (to its true
moment 0) by EVERY count N > ds + dt: the bound ds + dt + 1 is sharp
from both sides. -/
theorem threshold_witness_exact_above (hζ : IsPrimitiveRoot ζ N)
    {ds dt : ℕ} (hgt : ds + dt < N) (hdt : 0 < ds + dt) :
    ∑ k ∈ range N, ζ ^ ((ds : ℤ) * (k : ℤ)) * ζ ^ ((dt : ℤ) * (k : ℤ))
      = 0 := by
  have hz : ζ ≠ 0 := hζ.ne_zero (by omega)
  have hterm : ∀ k ∈ range N,
      ζ ^ ((ds : ℤ) * (k : ℤ)) * ζ ^ ((dt : ℤ) * (k : ℤ))
        = ζ ^ (((ds : ℤ) + (dt : ℤ)) * (k : ℤ)) := by
    intro k _
    rw [← zpow_add₀ hz]
    congr 1
    ring
  rw [Finset.sum_congr rfl hterm]
  refine sum_zpow_eq_zero_of_not_dvd hζ ?_
  intro hdvd
  have hzero : (ds : ℤ) + (dt : ℤ) = 0 :=
    Int.eq_zero_of_dvd_of_natAbs_lt_natAbs hdvd (by omega)
  omega

/-! ### G. The Gram-budget corollaries (concrete counts) -/

/-- The corrected SHARP count Nf = 2M-1 integrates the full Gram
budget — symbol degree (M-1) + lattice spread (M-1) = 2M-2 — exactly,
for arbitrary coefficients and arbitrary grid offset. -/
theorem gram_budget_exact_at_sharp {M : ℕ} (hM : 0 < M)
    (hζ : IsPrimitiveRoot ζ (2 * M - 1)) (w : K)
    (c : ℤ → K) {d : ℕ} (hd : d ≤ 2 * M - 2) :
    ∑ k ∈ range (2 * M - 1), ∑ m ∈ Icc (-(d : ℤ)) (d : ℤ),
        c m * (w * ζ ^ (k : ℤ)) ^ m
      = ((2 * M - 1 : ℕ) : K) * c 0 :=
  quadrature_exact hζ w c (by omega)

/-- The DEPLOYED count Nf = 2M+1 integrates the same budget exactly —
sufficient, but by `below_sharp_fails` not minimal. -/
theorem gram_budget_exact_at_deployed {M : ℕ} (hM : 0 < M)
    (hζ : IsPrimitiveRoot ζ (2 * M + 1)) (w : K)
    (c : ℤ → K) {d : ℕ} (hd : d ≤ 2 * M - 2) :
    ∑ k ∈ range (2 * M + 1), ∑ m ∈ Icc (-(d : ℤ)) (d : ℤ),
        c m * (w * ζ ^ (k : ℤ)) ^ m
      = ((2 * M + 1 : ℕ) : K) * c 0 :=
  quadrature_exact hζ w c (by omega)

/-- **Minimality of 2M-1**: at Nf = 2M-2 the explicit witness — the
degree-(M-1) symbol mode times the degree-(M-1) lattice mode, i.e.
the probe's p = M·e_{M-1}, u = e_0, v = e_{M-1} — has a NONZERO
quadrature error in characteristic zero. -/
theorem below_sharp_fails [CharZero K] {M : ℕ} (hM : 2 ≤ M)
    (hζ : IsPrimitiveRoot ζ (2 * M - 2)) :
    ∑ k ∈ range (2 * M - 2),
        ζ ^ (((M - 1 : ℕ) : ℤ) * (k : ℤ))
      * ζ ^ (((M - 1 : ℕ) : ℤ) * (k : ℤ)) ≠ 0 :=
  threshold_witness_ne_zero hζ (by omega) (by omega)

/-! ### C. The ℂ instance and the midpoint sign -/

/-- The concrete frequency grid generator ζ_N = exp(2πi/N)
instantiates every theorem above. -/
theorem complex_grid_isPrimitiveRoot (N : ℕ) (hN : N ≠ 0) :
    IsPrimitiveRoot (Complex.exp (2 * Real.pi * Complex.I / N)) N :=
  Complex.isPrimitiveRoot_exp N hN

/-- The midpoint offset w = exp(πi/N) satisfies w^N = -1. -/
theorem midpoint_offset_pow {N : ℕ} (hN : N ≠ 0) :
    (Complex.exp (Real.pi * Complex.I / N)) ^ N = -1 := by
  rw [← Complex.exp_nat_mul]
  have hcast : (N : ℂ) ≠ 0 := Nat.cast_ne_zero.mpr hN
  rw [show (N : ℂ) * (Real.pi * Complex.I / N) = Real.pi * Complex.I by
    field_simp]
  exact Complex.exp_pi_mul_I

/-- On the MIDPOINT grid (the probe's theta_k = 2π(k+1/2)/N) the
aliased frequency-N character sums to -N: the (-1)^r sign in the
probe's alias formula. -/
theorem midpoint_alias_sign {N : ℕ} (hN : N ≠ 0) {ζ : ℂ}
    (hζ : IsPrimitiveRoot ζ N) :
    ∑ k ∈ range N,
        (Complex.exp (Real.pi * Complex.I / N) * ζ ^ (k : ℤ)) ^ (N : ℤ)
      = -(N : ℂ) := by
  rw [alias_witness_offset hζ (Complex.exp (Real.pi * Complex.I / N)),
    zpow_natCast, midpoint_offset_pow hN]
  ring

end TfptCarrier.AntiAliasExact
