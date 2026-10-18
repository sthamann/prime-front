/-
RH/GaborDominance.lean -- r569 canonical isolation-shrink dominance.

CLAIM BOUNDARY.  NO RH CLAIM.  This file does not discharge
`gabor_separationForAllZeros` and does not assert RH or anti-RH.

r566 adjudication: the r562 `Finset (ℝ × ℝ)` configuration space is
the wrong carrier (drops multiplicities; allows γ<0 double-counts of
the FE pair, since Q(σ,−γ)=Q(σ,γ)).  r567 verified the repaired
canonical rule and bound on 119 cells
(`gabor_canonical_dominance_probe`, FILE_SHA c0781a08…).

This module replaces the signed `GaborDominanceBound` by the
canonical weighted form and proves the bricks that are finite
real/complex algebra or elementary analysis.  It does not change
`GaborSeparationPrecheck`, `GaborSeparationForAllZeros`,
`gaborArithmeticFormula`, or `scalingGaborTest`.

Proved, sorry-free (r562–r568):
  (1) truncated theta majorant outside the ε-window;
  (2) quadrupole size Q = 4 Re ĥ_W;
  (3) Q-evenness `Q(σ,−γ)=Q(σ,γ)`;
  (4) phase-coherence: σ′=σ★ and |γ′−γ★| ≤ κ a/σ★, κ<π/2 ⇒
      cos φ₋ ≤ −cos κ;
  (5) plus-lobe majorant on γ′≥0, ω>0, and the geometric bin series;
  (6) isolation-shrink with ω>0, including existence of the
      greatest admissible width (constraints monotone in a);
  (7) host-merge: exact copies contribute m★·(−η·E) on the minus
      lobe (linearity).

r569 rule change: after the largest admissible width is chosen,
the packet width is capped at
`a := min(admissible, a₀)` with
`a₀ = min(A_max, γ★²/512, 1/(8 K_bin²))`.
Every smaller positive width remains admissible (radius monotone
on the canonical strip) and keeps ω>0.  The γ²/512 cap makes
`A₊+2A× < cos(κ)·A₋` uniform in γ>0 (no extra γ★≥1 hypothesis);
the bin cap makes T_far and the plus/cross packing strictly
smaller than η ≥ exp(−π²/1024).  After isolation the peak and
κ windows contain no foreign ordinate, so T_gap = 0 and is
absorbed by T_far (no separate gap summation).

The r569 comparison and negativity theorems live in
`RH.GaborDominanceProof`.  `GaborDominanceBound` itself remains
unasserted: it follows from the one named remainder
`GaborDominanceAssembly` (packing + remainder budget).

Named, unasserted (not `sorry`):
  `GaborDominanceBound` — increment-compliant canonical Z ⇒
    W_honest < 0 under the rule;
  `GaborDominanceAssembly` (in `RH.GaborDominanceProof`) — the
    remaining finite-sum packing plus the elementary remainder
    budget that imply the bound;
  `GaborHonestNegImpliesIsolationArithmeticNeg` and
  `GaborIsolationArithmeticImpliesScalingArithmetic` — the two
    honest translation gaps between W_honest and
    `gaborArithmeticFormula` / `scalingGaborTest`.

`gabor_dominance_implies_separation` is sorry-free logic: the
named bound plus the two bridges imply `GaborSeparationForAllZeros`.

r574: the constant occupancy `K_bin = 43` is a historical special case
(not a theorem about ζ-zeros).  The counting-compatible cap is
`gaborKBinAt γ = 2 C_inner (1+log(γ+3))`, matching
`zeta_unit_increment` / `card_strip_window_le`.
`GaborDominanceBound` (constant compliance) remains; the live
statement is `GaborDominanceBoundLog`.
-/
import RH.GaborInequality
import RH.GaborHatAnalytic
import Mathlib.Analysis.Complex.Trigonometric
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Data.Real.Archimedean
import Mathlib.Topology.Algebra.InfiniteSum.Order
import Mathlib.Topology.Order.IntermediateValue

namespace RH

open scoped Classical
open Set Finset Complex

/-! ## Constants and closed forms -/

/-- r561 bin-card constant `K_bin = 43`.  Historical / constant-compliance
special case, not a theorem about ζ-zeros.  The counting-compatible
cap is `gaborKBinAt`. -/
def gaborKBin : ℕ := 43

/-- r561 lock factor: `a_lock = (σ²/64)/8`. -/
noncomputable def gaborLockFactor : ℝ := 1 / 8

/-- Increment prefactor used by `R_on = 2 C_inc S_cert`.
Equals the Path-A constant in `zeta_unit_increment`. -/
noncomputable def gaborCInc : ℝ :=
  2 * zetaZerosInDiskCardBoundInner

/-- Height-dependent occupancy matching `zeta_unit_increment` and
`card_window_zeros_unit_le`: `N(T+1)−N(T) ≤ 2 C_inner (1+log(T+3))`.
Same formula as `gaborBinCountMajorant k` at `γ = |k|`.
Defined for `γ > -3` (configs use `γ > 0` or `|k|`). -/
noncomputable def gaborKBinAt (γ : ℝ) : ℝ :=
  2 * zetaZerosInDiskCardBoundInner * (1 + Real.log (γ + 3))

/-- Lock width `a_lock = (σ²/64)/8`. -/
noncomputable def gaborALock (sigma : ℝ) : ℝ :=
  gaborScalingA sigma * gaborLockFactor

theorem gaborALock_eq (sigma : ℝ) :
    gaborALock sigma = (sigma ^ 2 / 64) / 8 := by
  unfold gaborALock gaborScalingA gaborLockFactor
  ring

theorem gaborALock_pos {sigma : ℝ} (hs : sigma ≠ 0) :
    0 < gaborALock sigma :=
  mul_pos (gaborScalingA_pos hs) (by norm_num [gaborLockFactor])

/-- Exception-window half-width
`ε(a) = √(2a log max(1/a, 4 K_bin))`.  The sealed probe also floors
the logarithm at 1; that is redundant for `a > 0` because
`4 K_bin = 172 > e`. -/
noncomputable def gaborIsolationEpsilon (a : ℝ) : ℝ :=
  Real.sqrt (2 * a * Real.log (max (1 / a) (4 * (gaborKBin : ℝ))))

/-- Phase-tuned center of the isolation-shrink packet. -/
noncomputable def gaborIsolationOmega (sigma gamma a : ℝ) : ℝ :=
  gamma - Real.pi * a / sigma

/-- Constructive isolation radius `πa/σ + ε(a)`. -/
noncomputable def gaborIsolationRadius (sigma a : ℝ) : ℝ :=
  Real.pi * a / sigma + gaborIsolationEpsilon a

/-- Sealed quadrupole size
`Q(σ′,γ′) = (π/a)[A₊ cos φ₊ + A₋ cos φ₋ + 2 Aₓ cos φₓ]`,
with the r560 *code* convention `A₊ = exp((σ′²-(γ′+ω)²)/(2a))`
paired with `φ₊ = σ′(γ′+ω)/a`.  The probe-header mnemonic
`A± = exp((σ′²-(γ′∓ω)²)/(2a))` swaps the ± labels and is not used. -/
noncomputable def gaborQuadrupole (a omega sigma gamma : ℝ) : ℝ :=
  Real.pi / a *
    (Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) *
        Real.cos (sigma * (gamma + omega) / a) +
      Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a)) *
        Real.cos (sigma * (gamma - omega) / a) +
      2 * Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) *
        Real.cos (sigma * gamma / a))

/-- Reduced-unit prefactor `E = (π/a) exp(σ²/(2a))`. -/
noncomputable def gaborEnhancement (sigma a : ℝ) : ℝ :=
  Real.pi / a * Real.exp (sigma ^ 2 / (2 * a))

/-- Tuned minus-lobe ratio `η = exp(-π² a / (2σ²))`. -/
noncomputable def gaborEtaTune (sigma a : ℝ) : ℝ :=
  Real.exp (-Real.pi ^ 2 * a / (2 * sigma ^ 2))

/-- r560 left-lobe majorant `θ_left`. -/
noncomputable def thetaLeftPos (a omega : ℝ) : ℝ :=
  if omega ≤ 0 ∨ (1 / 2 : ℝ) ≤ Real.exp (-omega / a) then
    thetaLobe a
  else
    Real.exp (-omega ^ 2 / (2 * a)) / (1 - Real.exp (-omega / a))

/-- r560 cross-lobe majorant `θ_cross`.
`θ₃ = Θ_lobe − 2`, so `(1+θ₃)/2 = (Θ_lobe − 1)/2`. -/
noncomputable def thetaCrossPos (a omega : ℝ) : ℝ :=
  Real.exp (-omega ^ 2 / (2 * a)) * (thetaLobe a - 1) / 2

/-- Certified three-lobe bin sum
`S_cert = (π/(4a))[Θ_lobe + θ_left + 2 θ_cross]`. -/
noncomputable def gaborSCert (a omega : ℝ) : ℝ :=
  Real.pi / (4 * a) *
    (thetaLobe a + thetaLeftPos a omega + 2 * thetaCrossPos a omega)

/-- On-line remainder `R_on = 2 C_inc S_cert`. -/
noncomputable def gaborHonestOnlineBudget (a omega Cinc : ℝ) : ℝ :=
  2 * Cinc * gaborSCert a omega

/-- r567 phase-coherence width `κ = 1 < π/2`. -/
def gaborKappa : ℝ := 1

/-- Closed ω>0 cap: `a ≤ γσ/(2π)` ⇒ `πa/σ ≤ γ/2` ⇒ `ω ≥ γ/2 > 0`. -/
noncomputable def gaborOmegaCap (sigma gamma : ℝ) : ℝ :=
  gamma * sigma / (2 * Real.pi)

/-- Largest lock-and-cap width `min(a_lock, γσ/(2π))`. -/
noncomputable def gaborAdmissibleAMax (sigma gamma : ℝ) : ℝ :=
  min (gaborALock sigma) (gaborOmegaCap sigma gamma)

/-- r567 `θ₃ = Θ_lobe − 2`. -/
noncomputable def gaborTheta3 (a : ℝ) : ℝ :=
  thetaLobe a - 2

/-- Minus-lobe phase `φ₋ = σ(γ−ω)/a`. -/
noncomputable def gaborPhiMinus (sigma gamma omega a : ℝ) : ℝ :=
  sigma * (gamma - omega) / a

/-- Canonical weighted configuration: finite support of off-line
representatives `(σ_j, γ_j)` with multiplicity `m_j ∈ ℕ>0`,
`0 < σ_j < 1/2`, `γ_j > 0`.  Not a `Finset` of bare pairs: the
weight is an explicit `ℕ`-valued function, so copies merge rather
than collapse. -/
structure GaborCanonicalConfig where
  pts : Finset (ℝ × ℝ)
  mult : ℝ × ℝ → ℕ
  mult_pos : ∀ q ∈ pts, 0 < mult q
  sigma_off : ∀ q ∈ pts, 0 < q.1 ∧ q.1 < (1 / 2 : ℝ)
  gamma_pos : ∀ q ∈ pts, 0 < q.2

namespace GaborCanonicalConfig

/-- Pairwise distinct ordinates (the shrink well-definedness
hypothesis: `d_min` is then a gap between distinct γ's).
r579: stronger than needed for T_gap = 0.  Isolation only
forbids a foreign σ at the host ordinate; see
`gammaHostIsolated` (defined after the host). -/
def gammaDistinct (Z : GaborCanonicalConfig) : Prop :=
  ∀ q₁ ∈ Z.pts, ∀ q₂ ∈ Z.pts, q₁.2 = q₂.2 → q₁ = q₂

end GaborCanonicalConfig

/-- Honest Weil score `W_honest = Σ_j m_j Q(σ_j,γ_j) + R_on`. -/
noncomputable def gaborHonestWeil (a omega : ℝ) (Z : GaborCanonicalConfig)
    (Cinc : ℝ) : ℝ :=
  Z.pts.sum (fun q => (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
    gaborHonestOnlineBudget a omega Cinc

/-- Plus-lobe term of Q (absolute units). -/
noncomputable def gaborPlusTerm (a omega sigma gamma : ℝ) : ℝ :=
  Real.pi / a *
    (Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) *
      Real.cos (sigma * (gamma + omega) / a))

/-- Minus-lobe term of Q (absolute units). -/
noncomputable def gaborMinusTerm (a omega sigma gamma : ℝ) : ℝ :=
  Real.pi / a *
    (Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a)) *
      Real.cos (sigma * (gamma - omega) / a))

/-- Cross-lobe term of Q (absolute units, without the factor 2). -/
noncomputable def gaborCrossTerm (a omega sigma gamma : ℝ) : ℝ :=
  Real.pi / a *
    (Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) *
      Real.cos (sigma * gamma / a))

theorem gaborQuadrupole_eq_terms (a omega sigma gamma : ℝ) :
    gaborQuadrupole a omega sigma gamma =
      gaborPlusTerm a omega sigma gamma +
        gaborMinusTerm a omega sigma gamma +
          2 * gaborCrossTerm a omega sigma gamma := by
  unfold gaborQuadrupole gaborPlusTerm gaborMinusTerm gaborCrossTerm
  ring

/-- r567 plus-lobe packing
`T₊ = K_bin e^{−ω²/2a} [1/(1−e^{−ω/a}) + (1+θ₃(a))]`. -/
noncomputable def gaborTPlus (a omega : ℝ) : ℝ :=
  (gaborKBin : ℝ) * Real.exp (-omega ^ 2 / (2 * a)) *
    (1 / (1 - Real.exp (-omega / a)) + (1 + gaborTheta3 a))

/-- r567 far-lobe packing
`T_far = K_bin [4 e^{−ε²/2a} + (Θ_lobe−3)]`. -/
noncomputable def gaborTFar (a : ℝ) : ℝ :=
  (gaborKBin : ℝ) *
    (4 * Real.exp (-gaborIsolationEpsilon a ^ 2 / (2 * a)) +
      (thetaLobe a - 3))

/-- Phase-coherence window
`|σ′(γ′−γ★)/a + π(σ′/σ★−1)| ≤ κ`. -/
def gaborPhaseCoherent (sigma' gamma' sigmaStar gammaStar a : ℝ) : Prop :=
  |sigma' * (gamma' - gammaStar) / a +
      Real.pi * (sigma' / sigmaStar - 1)| ≤ gaborKappa

/-- Exception-window membership `|γ′−ω| ≤ ε(a)`. -/
def gaborInPeakWindow (gamma' omega a : ℝ) : Prop :=
  |gamma' - omega| ≤ gaborIsolationEpsilon a

/-- κ-height window `|γ′−γ★| ≤ κ a/σ★`. -/
def gaborInKappaWindow (gamma' gammaStar sigmaStar a : ℝ) : Prop :=
  |gamma' - gammaStar| ≤ gaborKappa * a / sigmaStar

/-- Gap majorant over non-phase-coherent `σ′<σ★` points in the
peak or κ window. -/
noncomputable def gaborTGap (a : ℝ) (Z : GaborCanonicalConfig)
    (sigmaStar gammaStar omega : ℝ) : ℝ :=
  (Z.pts.filter (fun q =>
      q.1 < sigmaStar ∧
        (gaborInPeakWindow q.2 omega a ∨
          gaborInKappaWindow q.2 gammaStar sigmaStar a) ∧
        ¬ gaborPhaseCoherent q.1 q.2 sigmaStar gammaStar a)).sum
    (fun q =>
      (Z.mult q : ℝ) * Real.exp ((q.1 ^ 2 - sigmaStar ^ 2) / (2 * a)))

/-- Reduced r567 bound
`−η m★ + T₊ + T_gap + T_far + R_on/E`. -/
noncomputable def gaborCanonicalBoundReduced
    (a omega sigmaStar : ℝ) (mStar : ℕ) (Z : GaborCanonicalConfig)
    (gammaStar : ℝ) : ℝ :=
  -gaborEtaTune sigmaStar a * (mStar : ℝ) +
    gaborTPlus a omega +
    gaborTGap a Z sigmaStar gammaStar omega +
    gaborTFar a +
    gaborHonestOnlineBudget a omega gaborCInc /
      gaborEnhancement sigmaStar a

/-- Closed r561 bound in absolute (not reduced) units. -/
noncomputable def gaborDominanceClosedBound
    (sigma a omega Cinc : ℝ) : ℝ :=
  gaborEnhancement sigma a *
      (-gaborEtaTune sigma a +
        (gaborKBin : ℝ) *
          (4 * Real.exp (-gaborIsolationEpsilon a ^ 2 / (2 * a)) +
            (thetaLobe a - 3)) +
        (gaborKBin : ℝ) *
          (thetaLeftPos a omega + 2 * thetaCrossPos a omega)) +
    2 * Cinc * gaborSCert a omega

/-! ## (1) Truncated theta majorant -/

/-- Unit bin `[k,k+1]` lies entirely outside `I_exc = [c−ε, c+ε]`. -/
def binOutsideWindow (c ε : ℝ) (k : ℤ) : Prop :=
  (k : ℝ) + 1 ≤ c - ε ∨ c + ε ≤ (k : ℝ)

lemma binOutsideWindow_dist {c ε : ℝ} {k : ℤ} {t : ℝ}
    (ht : t ∈ Icc (k : ℝ) ((k : ℝ) + 1))
    (hout : binOutsideWindow c ε k) :
    ε ≤ |t - c| := by
  by_cases hε : ε ≤ 0
  · exact hε.trans (abs_nonneg _)
  · have hε0 : 0 < ε := lt_of_not_ge hε
    rcases hout with hL | hR
    · have ht' : t ≤ c - ε := le_trans ht.2 hL
      have hnonpos : t - c ≤ 0 := by linarith [ht', hε0]
      rw [abs_of_nonpos hnonpos]
      linarith [ht']
    · have ht' : c + ε ≤ t := le_trans hR ht.1
      have hnonneg : 0 ≤ t - c := by linarith [ht', hε0]
      rw [abs_of_nonneg hnonneg]
      linarith [ht']

theorem gaussBinMax_of_outside {a c ε : ℝ} (ha : 0 < a) (hε : 0 ≤ ε)
    (k : ℤ) (hout : binOutsideWindow c ε k) :
    gaussBinMax a c k ≤ Real.exp (-ε ^ 2 / (2 * a)) :=
  gaussBinMax_le_exp ha k hε fun _t ht => binOutsideWindow_dist ht hout

private lemma isolation_sum_right_tail_le {a : ℝ} (ha : 0 < a) (n : ℤ)
    (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => n + 2 ≤ k),
        Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
      ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
  set Kr := K.filter (fun k => n + 2 ≤ k)
  let φ : ℤ → ℕ := fun k => Int.toNat (k - n - 2)
  have hφ : ∀ k ∈ Kr, ((k - n - 1 : ℤ) : ℝ) = ((φ k + 1 : ℕ) : ℝ) := by
    intro k hk
    have : n + 2 ≤ k := (mem_filter.mp hk).2
    have hnn : 0 ≤ k - n - 2 := by omega
    have hto : ((k - n - 2).toNat : ℤ) = k - n - 2 :=
      Int.toNat_of_nonneg hnn
    have h1 : (k - n - 1 : ℤ) = (k - n - 2) + 1 := by ring
    have h2 : ((φ k + 1 : ℕ) : ℤ) = (k - n - 2) + 1 := by
      unfold φ
      rw [Nat.cast_add, Nat.cast_one, hto]
    rw [h1, ← h2]
    exact_mod_cast rfl
  have hinj : ∀ k₁ ∈ Kr, ∀ k₂ ∈ Kr, φ k₁ = φ k₂ → k₁ = k₂ := by
    intro k₁ hk₁ k₂ hk₂ hφeq
    have h1 : 0 ≤ k₁ - n - 2 := by
      have : n + 2 ≤ k₁ := (mem_filter.mp hk₁).2
      omega
    have h2 : 0 ≤ k₂ - n - 2 := by
      have : n + 2 ≤ k₂ := (mem_filter.mp hk₂).2
      omega
    have ht1 := Int.toNat_of_nonneg h1
    have ht2 := Int.toNat_of_nonneg h2
    have : k₁ - n - 2 = k₂ - n - 2 := by
      calc
        k₁ - n - 2 = ((k₁ - n - 2).toNat : ℤ) := ht1.symm
        _ = ((k₂ - n - 2).toNat : ℤ) := by exact_mod_cast hφeq
        _ = k₂ - n - 2 := ht2
    omega
  have hsummable := theta_lobe_summable ha
  have himage :
      ∑ k ∈ Kr, Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) =
        ∑ m ∈ Kr.image φ,
          Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    rw [sum_image hinj]
    refine sum_congr rfl fun k hk => ?_
    rw [hφ k hk]
  rw [himage]
  exact hsummable.sum_le_tsum _ (fun _ _ => (Real.exp_pos _).le)

private lemma isolation_sum_left_tail_le {a : ℝ} (ha : 0 < a) (n : ℤ)
    (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => k ≤ n - 2),
        Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) ≤
      ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
  set Kl := K.filter (fun k => k ≤ n - 2)
  let ψ : ℤ → ℕ := fun k => Int.toNat (n - 2 - k)
  have hψ : ∀ k ∈ Kl, ((n - 1 - k : ℤ) : ℝ) = ((ψ k + 1 : ℕ) : ℝ) := by
    intro k hk
    have : k ≤ n - 2 := (mem_filter.mp hk).2
    have hnn : 0 ≤ n - 2 - k := by omega
    have hto : ((n - 2 - k).toNat : ℤ) = n - 2 - k :=
      Int.toNat_of_nonneg hnn
    have h1 : (n - 1 - k : ℤ) = (n - 2 - k) + 1 := by ring
    have h2 : ((ψ k + 1 : ℕ) : ℤ) = (n - 2 - k) + 1 := by
      unfold ψ
      rw [Nat.cast_add, Nat.cast_one, hto]
    rw [h1, ← h2]
    exact_mod_cast rfl
  have hinj : ∀ k₁ ∈ Kl, ∀ k₂ ∈ Kl, ψ k₁ = ψ k₂ → k₁ = k₂ := by
    intro k₁ hk₁ k₂ hk₂ hψeq
    have h1 : 0 ≤ n - 2 - k₁ := by
      have : k₁ ≤ n - 2 := (mem_filter.mp hk₁).2
      omega
    have h2 : 0 ≤ n - 2 - k₂ := by
      have : k₂ ≤ n - 2 := (mem_filter.mp hk₂).2
      omega
    have ht1 := Int.toNat_of_nonneg h1
    have ht2 := Int.toNat_of_nonneg h2
    have : n - 2 - k₁ = n - 2 - k₂ := by
      calc
        n - 2 - k₁ = ((n - 2 - k₁).toNat : ℤ) := ht1.symm
        _ = ((n - 2 - k₂).toNat : ℤ) := by exact_mod_cast hψeq
        _ = n - 2 - k₂ := ht2
    omega
  have hsummable := theta_lobe_summable ha
  have himage :
      ∑ k ∈ Kl, Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) =
        ∑ m ∈ Kl.image ψ,
          Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    rw [sum_image hinj]
    refine sum_congr rfl fun k hk => ?_
    rw [hψ k hk]
  rw [himage]
  exact hsummable.sum_le_tsum _ (fun _ _ => (Real.exp_pos _).le)

lemma gaussBinMax_far_sum_le {a c : ℝ} (ha : 0 < a) (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k =>
        k ≤ Int.floor c - 2 ∨ Int.floor c + 2 ≤ k),
        gaussBinMax a c k ≤ thetaLobe a - 3 := by
  set n := Int.floor c
  set Kf := K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k)
  have hterm : ∀ k ∈ Kf,
      gaussBinMax a c k ≤
        (if n + 2 ≤ k then
            Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) +
          (if k ≤ n - 2 then
              Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) := by
    intro k hk
    have hfar : k ≤ n - 2 ∨ n + 2 ≤ k := (mem_filter.mp hk).2
    rcases hfar with hl | hr
    · have hr : ¬ n + 2 ≤ k := by omega
      have hle := gaussBinMax_le_left (a := a) (c := c) ha (n := n) rfl hl
      simp [hr, hl]
      rw [int_cast_sub_sub'] at hle
      exact hle
    · have hl : ¬ k ≤ n - 2 := by omega
      have hle := gaussBinMax_le_right (a := a) (c := c) ha (n := n) rfl hr
      simp [hr, hl]
      rw [int_cast_sub_sub] at hle
      exact hle
  have hsum := sum_le_sum hterm
  have hsplit :
      ∑ k ∈ Kf,
          ((if n + 2 ≤ k then
              Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) +
            (if k ≤ n - 2 then
                Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0)) =
        ∑ k ∈ Kf, (if n + 2 ≤ k then
            Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) +
          ∑ k ∈ Kf, (if k ≤ n - 2 then
              Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) := by
    simp [sum_add_distrib]
  rw [hsplit] at hsum
  have hright :
      ∑ k ∈ Kf, (if n + 2 ≤ k then
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) ≤
        ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    have : ∑ k ∈ Kf, (if n + 2 ≤ k then
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) =
        ∑ k ∈ Kf.filter (fun k => n + 2 ≤ k),
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)) :=
      (sum_filter (p := fun k => n + 2 ≤ k)
        (f := fun k =>
          Real.exp (-((k - n - 1 : ℤ) : ℝ) ^ 2 / (2 * a)))).symm
    rw [this]
    exact isolation_sum_right_tail_le ha n Kf
  have hleft :
      ∑ k ∈ Kf, (if k ≤ n - 2 then
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) ≤
        ∑' m : ℕ, Real.exp (-((m + 1 : ℕ) : ℝ) ^ 2 / (2 * a)) := by
    have : ∑ k ∈ Kf, (if k ≤ n - 2 then
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) else 0) =
        ∑ k ∈ Kf.filter (fun k => k ≤ n - 2),
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)) :=
      (sum_filter (p := fun k => k ≤ n - 2)
        (f := fun k =>
          Real.exp (-((n - 1 - k : ℤ) : ℝ) ^ 2 / (2 * a)))).symm
    rw [this]
    exact isolation_sum_left_tail_le ha n Kf
  unfold thetaLobe
  linarith [hsum, hright, hleft]

/-- Finite-sum truncated theta bound.  Central bins outside `I_exc`
contribute at most `3 e^{-ε²/2a}`; the r561 form uses the factor 4. -/
theorem truncated_theta_binMax_sum_le {a c ε : ℝ} (ha : 0 < a)
    (hε : 0 ≤ ε) (K : Finset ℤ) :
    ∑ k ∈ K.filter (fun k => binOutsideWindow c ε k), gaussBinMax a c k ≤
      4 * Real.exp (-ε ^ 2 / (2 * a)) + (thetaLobe a - 3) := by
  set n := Int.floor c
  set Ko := K.filter (fun k => binOutsideWindow c ε k)
  let central : Finset ℤ := {n - 1, n, n + 1}
  have hterm : ∀ k ∈ Ko,
      gaussBinMax a c k ≤
        (if k ∈ central then Real.exp (-ε ^ 2 / (2 * a)) else 0) +
          (if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a c k else 0) := by
    intro k hk
    by_cases hcen : k ∈ central
    · have hn2 : ¬ (k ≤ n - 2 ∨ n + 2 ≤ k) := by
        have : k = n - 1 ∨ k = n ∨ k = n + 1 := by
          simpa [central] using hcen
        omega
      simp [hcen, hn2]
      exact gaussBinMax_of_outside ha hε k (mem_filter.mp hk).2
    · have hfar : k ≤ n - 2 ∨ n + 2 ≤ k := by
        have : k ≠ n - 1 ∧ k ≠ n ∧ k ≠ n + 1 := by
          refine ⟨?_, ?_, ?_⟩
          · intro h; exact hcen (by simp [central, h])
          · intro h; exact hcen (by simp [central, h])
          · intro h; exact hcen (by simp [central, h])
        omega
      simp [hcen, hfar]
  have hsum := sum_le_sum hterm
  have hsplit :
      ∑ k ∈ Ko,
          ((if k ∈ central then Real.exp (-ε ^ 2 / (2 * a)) else 0) +
            (if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a c k else 0)) =
        ∑ k ∈ Ko, (if k ∈ central then Real.exp (-ε ^ 2 / (2 * a)) else 0) +
          ∑ k ∈ Ko,
            (if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a c k else 0) := by
    simp [sum_add_distrib]
  rw [hsplit] at hsum
  have hcen :
      ∑ k ∈ Ko, (if k ∈ central then Real.exp (-ε ^ 2 / (2 * a)) else 0) ≤
        3 * Real.exp (-ε ^ 2 / (2 * a)) := by
    have hite :
        ∑ k ∈ Ko, (if k ∈ central then Real.exp (-ε ^ 2 / (2 * a)) else 0) =
          ((Ko.filter (fun k => k ∈ central)).card : ℝ) *
            Real.exp (-ε ^ 2 / (2 * a)) := by
      rw [sum_ite, sum_const, sum_const, nsmul_eq_mul, nsmul_eq_mul,
        mul_zero, add_zero]
    rw [hite]
    have hsub : Ko.filter (fun k => k ∈ central) ⊆ central := by
      intro k hk
      exact (mem_filter.mp hk).2
    have hcard := Nat.cast_le (α := ℝ) |>.mpr
      ((Finset.card_le_card hsub).trans (le_of_eq (central3_card n)))
    exact mul_le_mul_of_nonneg_right hcard (Real.exp_pos _).le
  have hfar :
      ∑ k ∈ Ko,
          (if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a c k else 0) ≤
        thetaLobe a - 3 := by
    have : ∑ k ∈ Ko,
          (if k ≤ n - 2 ∨ n + 2 ≤ k then gaussBinMax a c k else 0) =
        ∑ k ∈ Ko.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k),
          gaussBinMax a c k :=
      (sum_filter (p := fun k => k ≤ n - 2 ∨ n + 2 ≤ k)
        (f := fun k => gaussBinMax a c k)).symm
    rw [this]
    have hsub :
        Ko.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k) ⊆
          K.filter (fun k => k ≤ n - 2 ∨ n + 2 ≤ k) := by
      intro k hk
      have hk' := mem_filter.mp hk
      have hkKo := mem_filter.mp hk'.1
      exact mem_filter.mpr ⟨hkKo.1, hk'.2⟩
    refine (sum_le_sum_of_subset_of_nonneg hsub ?_).trans
      (gaussBinMax_far_sum_le ha K)
    intro k _ _
    exact gaussBinMax_nonneg ha k
  have h3 : (3 : ℝ) * Real.exp (-ε ^ 2 / (2 * a)) ≤
      4 * Real.exp (-ε ^ 2 / (2 * a)) := by
    nlinarith [Real.exp_pos (-ε ^ 2 / (2 * a))]
  linarith [hsum, hcen, hfar, h3]

lemma truncated_theta_indicator_nonneg {a c ε : ℝ} (ha : 0 < a) (k : ℤ) :
    0 ≤ (if binOutsideWindow c ε k then gaussBinMax a c k else 0) := by
  split_ifs
  · exact gaussBinMax_nonneg ha k
  · exact le_rfl

lemma truncated_theta_indicator_le_binMax {a c ε : ℝ} (ha : 0 < a)
    (k : ℤ) :
    (if binOutsideWindow c ε k then gaussBinMax a c k else 0) ≤
      gaussBinMax a c k := by
  split_ifs
  · exact le_rfl
  · exact gaussBinMax_nonneg ha k

lemma truncated_theta_indicator_summable {a c ε : ℝ} (ha : 0 < a) :
    Summable fun k : ℤ =>
      if binOutsideWindow c ε k then gaussBinMax a c k else 0 :=
  Summable.of_nonneg_of_le (fun k => truncated_theta_indicator_nonneg ha k)
    (fun k => truncated_theta_indicator_le_binMax ha k)
    (gaussBinMax_summable ha)

/-- `Σ` over bins outside the ε-window
`≤ 4 e^{-ε²/2a} + (Θ_lobe(a)−3)`. -/
theorem truncated_theta_tsum_le {a c ε : ℝ} (ha : 0 < a) (hε : 0 ≤ ε) :
    (∑' k : ℤ,
      if binOutsideWindow c ε k then gaussBinMax a c k else 0) ≤
      4 * Real.exp (-ε ^ 2 / (2 * a)) + (thetaLobe a - 3) := by
  refine Real.tsum_le_of_sum_le
    (fun k => truncated_theta_indicator_nonneg ha k) fun K => ?_
  have hite :
      ∑ k ∈ K,
          (if binOutsideWindow c ε k then gaussBinMax a c k else 0) =
        ∑ k ∈ K.filter (fun k => binOutsideWindow c ε k),
          gaussBinMax a c k :=
    (sum_filter (p := fun k => binOutsideWindow c ε k)
      (f := fun k => gaussBinMax a c k)).symm
  rw [hite]
  exact truncated_theta_binMax_sum_le ha hε K

/-! ## (2) Q as 4 Re ĥ_W -/

theorem re_ofReal_mul (r : ℝ) (z : ℂ) :
    ((r : ℂ) * z).re = r * z.re := by
  simp [mul_re]

theorem re_ofReal_mul_cexp_I (amp phase : ℝ) :
    (((amp : ℝ) : ℂ) * Complex.exp (Complex.I * (phase : ℂ))).re =
      amp * Real.cos phase := by
  have hmul : Complex.I * (phase : ℂ) = (phase : ℂ) * Complex.I := by
    ring
  have hcos : (Complex.cos (phase : ℂ)).re = Real.cos phase := by
    rw [← ofReal_cos, ofReal_re]
  rw [hmul, Complex.exp_ofReal_mul_I, re_ofReal_mul, add_re, mul_re]
  simp [hcos, I_re, I_im]

theorem re_cexp_I (phase : ℝ) :
    (Complex.exp (Complex.I * (phase : ℂ))).re = Real.cos phase := by
  simpa using re_ofReal_mul_cexp_I (1 : ℝ) phase

theorem re_pureGaborHatDelta (a omega : ℝ) (ha : 0 < a) (δ : ℂ) :
    (pureGaborHatDelta a omega δ).re =
      Real.pi / (4 * a) *
        (Real.exp ((δ.re ^ 2 - (δ.im + omega) ^ 2) / (2 * a)) *
            Real.cos (δ.re * (δ.im + omega) / a) +
          Real.exp ((δ.re ^ 2 - (δ.im - omega) ^ 2) / (2 * a)) *
            Real.cos (δ.re * (δ.im - omega) / a) +
          2 * Real.exp ((δ.re ^ 2 - δ.im ^ 2 - omega ^ 2) / (2 * a)) *
            Real.cos (δ.re * δ.im / a)) := by
  simp only [pureGaborHatDelta]
  have h1 : ((δ.re : ℂ) * ((δ.im : ℂ) + (omega : ℂ)) / (a : ℂ)) =
      ((δ.re * (δ.im + omega) / a : ℝ) : ℂ) := by
    push_cast
    rfl
  have h2 : ((δ.re : ℂ) * ((δ.im : ℂ) - (omega : ℂ)) / (a : ℂ)) =
      ((δ.re * (δ.im - omega) / a : ℝ) : ℂ) := by
    push_cast
    rfl
  have h3 : ((δ.re : ℂ) * (δ.im : ℂ) / (a : ℂ)) =
      ((δ.re * δ.im / a : ℝ) : ℂ) := by
    push_cast
    rfl
  rw [h1, h2, h3]
  rw [re_ofReal_mul, add_re, add_re, re_ofReal_mul_cexp_I,
    re_ofReal_mul_cexp_I]
  have hassoc :
      (2 : ℂ) * ((Real.exp ((δ.re ^ 2 - δ.im ^ 2 - omega ^ 2) / (2 * a)) : ℝ) : ℂ) *
          Complex.exp (Complex.I * ((δ.re * δ.im / a : ℝ) : ℂ)) =
        ((2 : ℝ) : ℂ) *
          (((Real.exp ((δ.re ^ 2 - δ.im ^ 2 - omega ^ 2) / (2 * a)) : ℝ) : ℂ) *
            Complex.exp (Complex.I * ((δ.re * δ.im / a : ℝ) : ℂ))) := by
    push_cast
    ring
  rw [hassoc, re_ofReal_mul, re_ofReal_mul_cexp_I]
  ring

theorem gaborQuadrupole_eq_four_re_hat
    (a omega sigma gamma : ℝ) (ha : 0 < a) :
    gaborQuadrupole a omega sigma gamma =
      4 * (gaborHat (pureGaborTest a omega ha)
        ((1 / 2 : ℂ) + (sigma : ℂ) + (gamma : ℂ) * I)).re := by
  have hpure : (pureGaborTest a omega ha).coeffs = ⟨1, 0, 0⟩ := rfl
  rw [gaborHat_of_pure hpure]
  have hδ :
      ((1 / 2 : ℂ) + (sigma : ℂ) + (gamma : ℂ) * I) - (1 / 2 : ℂ) =
        (sigma : ℂ) + (gamma : ℂ) * I := by
    ring
  rw [hδ]
  simp [pureGaborTest]
  rw [re_pureGaborHatDelta a omega ha]
  simp [add_re, mul_re, ofReal_re, ofReal_im, I_re, I_im]
  unfold gaborQuadrupole
  field_simp [ne_of_gt ha]

/-- Q equals four times the real part of the sealed integral
representation of `ĥ_W`. -/
theorem gaborQuadrupole_eq_four_re_integral
    (a omega sigma gamma : ℝ) (ha : 0 < a) :
    gaborQuadrupole a omega sigma gamma =
      4 * (∫ u : ℝ,
        (pureGaborAutocorrelation a omega u : ℂ) *
          Complex.exp (((sigma : ℂ) + (gamma : ℂ) * I) * u)).re := by
  have hhat := gaborQuadrupole_eq_four_re_hat a omega sigma gamma ha
  have hint :=
    pureGaborHat_integral_representation a omega ha
      ((1 / 2 : ℂ) + (sigma : ℂ) + (gamma : ℂ) * I)
  have hδ :
      ((1 / 2 : ℂ) + (sigma : ℂ) + (gamma : ℂ) * I) - (1 / 2 : ℂ) =
        (sigma : ℂ) + (gamma : ℂ) * I := by
    ring
  have hpure : (pureGaborTest a omega ha).coeffs = ⟨1, 0, 0⟩ := rfl
  rw [hhat, gaborHat_of_pure hpure]
  have hre :
      (pureGaborHatDelta a omega
          (((1 / 2 : ℂ) + (sigma : ℂ) + (gamma : ℂ) * I) - (1 / 2 : ℂ))).re =
        (∫ u : ℝ,
          (pureGaborAutocorrelation a omega u : ℂ) *
            Complex.exp (((sigma : ℂ) + (gamma : ℂ) * I) * u)).re := by
    have hint' := hint
    rw [hδ] at hint'
    rw [hint', hδ]
  exact congrArg (fun x => 4 * x) hre

/-! ## (3a) Q-evenness — canonicalisation foundation -/

theorem gaborQuadrupole_even_gamma (a omega sigma gamma : ℝ) :
    gaborQuadrupole a omega sigma (-gamma) =
      gaborQuadrupole a omega sigma gamma := by
  unfold gaborQuadrupole
  have hplus : (-gamma + omega) ^ 2 = (gamma - omega) ^ 2 := by ring
  have hminus : (-gamma - omega) ^ 2 = (gamma + omega) ^ 2 := by ring
  have hsq : (-gamma) ^ 2 = gamma ^ 2 := by ring
  have cplus :
      Real.cos (sigma * (-gamma + omega) / a) =
        Real.cos (sigma * (gamma - omega) / a) := by
    have : sigma * (-gamma + omega) / a =
        -(sigma * (gamma - omega) / a) := by ring
    rw [this, Real.cos_neg]
  have cminus :
      Real.cos (sigma * (-gamma - omega) / a) =
        Real.cos (sigma * (gamma + omega) / a) := by
    have : sigma * (-gamma - omega) / a =
        -(sigma * (gamma + omega) / a) := by ring
    rw [this, Real.cos_neg]
  have ccross :
      Real.cos (sigma * (-gamma) / a) = Real.cos (sigma * gamma / a) := by
    have : sigma * (-gamma) / a = -(sigma * gamma / a) := by ring
    rw [this, Real.cos_neg]
  rw [hplus, hminus, hsq, cplus, cminus, ccross]
  ring

/-! ## (3b) Phase-coherence at the host height -/

theorem gaborKappa_nonneg : 0 ≤ gaborKappa := by
  unfold gaborKappa
  norm_num

theorem gaborKappa_lt_half_pi : gaborKappa < Real.pi / 2 := by
  unfold gaborKappa
  have hπ : (2 : ℝ) < Real.pi := lt_trans (by norm_num) Real.pi_gt_three
  linarith

theorem gaborPhiMinus_eq_pi_add {sigma gamma gamma' a : ℝ}
    (hs : sigma ≠ 0) (ha : a ≠ 0) :
    gaborPhiMinus sigma gamma' (gaborIsolationOmega sigma gamma a) a =
      Real.pi + sigma * (gamma' - gamma) / a := by
  unfold gaborPhiMinus gaborIsolationOmega
  have hσ : (sigma : ℝ) ≠ 0 := hs
  have ha0 : (a : ℝ) ≠ 0 := ha
  field_simp [hσ, ha0]
  ring

theorem gaborPhiMinus_host {sigma gamma a : ℝ}
    (hs : sigma ≠ 0) (ha : a ≠ 0) :
    gaborPhiMinus sigma gamma (gaborIsolationOmega sigma gamma a) a =
      Real.pi := by
  rw [gaborPhiMinus_eq_pi_add hs ha]
  ring

/-- For `σ′=σ★` and `|γ′−γ★| ≤ κ a/σ★` with `0 ≤ κ < π/2`,
the tuned minus-lobe phase satisfies `cos φ₋ ≤ −cos κ`. -/
theorem gabor_phase_coherent_cos {sigma gamma gamma' a κ : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) (hκ0 : 0 ≤ κ) (hκ : κ < Real.pi / 2)
    (hwin : |gamma' - gamma| ≤ κ * a / sigma) :
    Real.cos (gaborPhiMinus sigma gamma'
        (gaborIsolationOmega sigma gamma a) a) ≤ -Real.cos κ := by
  have hφ :=
    gaborPhiMinus_eq_pi_add (sigma := sigma) (gamma := gamma)
      (gamma' := gamma') (a := a) (ne_of_gt hs) (ne_of_gt ha)
  rw [hφ, add_comm, Real.cos_add_pi]
  set θ : ℝ := sigma * (gamma' - gamma) / a
  have hθabs : |θ| ≤ κ := by
    unfold θ
    have ha0 : a ≠ 0 := ne_of_gt ha
    have hs0 : sigma ≠ 0 := ne_of_gt hs
    have : |sigma * (gamma' - gamma) / a| =
        sigma * |gamma' - gamma| / a := by
      rw [abs_div, abs_mul, abs_of_pos hs, abs_of_pos ha]
    rw [this]
    have hden : 0 < a / sigma := div_pos ha hs
    have hmul := mul_le_mul_of_nonneg_left hwin (div_nonneg ha.le hs.le)
    -- |γ'−γ| ≤ κ a/σ  ⇒  σ|γ'−γ|/a ≤ κ
    have hform : sigma * |gamma' - gamma| / a ≤
        sigma * (κ * a / sigma) / a := by
      exact div_le_div_of_nonneg_right
        (mul_le_mul_of_nonneg_left hwin hs.le) ha.le
    refine hform.trans_eq ?_
    field_simp [hs0, ha0]
  have hθle : 0 ≤ |θ| := abs_nonneg _
  have hκpi : κ ≤ Real.pi :=
    hκ.le.trans (div_le_self Real.pi_pos.le (by norm_num))
  have hcos : Real.cos κ ≤ Real.cos |θ| :=
    Real.cos_le_cos_of_nonneg_of_le_pi hθle hκpi hθabs
  have hcosθ : Real.cos θ = Real.cos |θ| := (Real.cos_abs θ).symm
  rw [hcosθ]
  linarith [hcos]

theorem gabor_phase_coherent_cos_kappa {sigma gamma gamma' a : ℝ}
    (hs : 0 < sigma) (ha : 0 < a)
    (hwin : |gamma' - gamma| ≤ gaborKappa * a / sigma) :
    Real.cos (gaborPhiMinus sigma gamma'
        (gaborIsolationOmega sigma gamma a) a) ≤
      -Real.cos gaborKappa :=
  gabor_phase_coherent_cos hs ha gaborKappa_nonneg gaborKappa_lt_half_pi hwin

/-! ## (3c) Plus-lobe majorant on `γ′ ≥ 0`, `ω > 0` -/

theorem gaborEnhancement_pos {sigma a : ℝ} (ha : 0 < a) :
    0 < gaborEnhancement sigma a :=
  mul_pos (div_pos Real.pi_pos ha) (Real.exp_pos _)

theorem gaborPlusAmp_le_exp_neg_omega_sq
    {sigmaStar a omega sigma gamma : ℝ} (ha : 0 < a)
    (hσ0 : 0 ≤ sigma) (hσ : sigma ≤ sigmaStar)
    (hγ : 0 ≤ gamma) (hω : 0 ≤ omega) :
    Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) /
        Real.exp (sigmaStar ^ 2 / (2 * a)) ≤
      Real.exp (-omega ^ 2 / (2 * a)) := by
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hσsq : sigma ^ 2 ≤ sigmaStar ^ 2 :=
    sq_le_sq.mpr (by
      rwa [abs_of_nonneg hσ0, abs_of_nonneg (hσ0.trans hσ)])
  have hγω : omega ^ 2 ≤ (gamma + omega) ^ 2 := by
    nlinarith [mul_nonneg hγ hω, sq_nonneg gamma]
  rw [← Real.exp_sub]
  refine Real.exp_le_exp.mpr ?_
  rw [div_sub_div_same]
  exact div_le_div_of_nonneg_right (by linarith) hden.le

theorem gaborPlusTerm_div_E_le
    {sigmaStar a omega sigma gamma : ℝ} (ha : 0 < a)
    (hσ0 : 0 ≤ sigma) (hσ : sigma ≤ sigmaStar)
    (hγ : 0 ≤ gamma) (hω : 0 ≤ omega) :
    gaborPlusTerm a omega sigma gamma / gaborEnhancement sigmaStar a ≤
      Real.exp (-omega ^ 2 / (2 * a)) := by
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hcos : Real.cos (sigma * (gamma + omega) / a) ≤ 1 := Real.cos_le_one _
  have hamp0 : 0 ≤
      Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) :=
    (Real.exp_pos _).le
  have hπa : 0 ≤ Real.pi / a := div_nonneg Real.pi_pos.le ha.le
  have hred := gaborPlusAmp_le_exp_neg_omega_sq ha hσ0 hσ hγ hω
  have hcancel :
      gaborPlusTerm a omega sigma gamma / gaborEnhancement sigmaStar a =
        (Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) *
            Real.cos (sigma * (gamma + omega) / a)) /
          Real.exp (sigmaStar ^ 2 / (2 * a)) := by
    unfold gaborPlusTerm gaborEnhancement
    field_simp [ha0, Real.pi_pos.ne']
  rw [hcancel]
  have hamp_le :
      Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) *
          Real.cos (sigma * (gamma + omega) / a) ≤
        Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) :=
    mul_le_of_le_one_right hamp0 hcos
  have hdiv :
      (Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) *
          Real.cos (sigma * (gamma + omega) / a)) /
        Real.exp (sigmaStar ^ 2 / (2 * a)) ≤
        Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) /
          Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    div_le_div_of_nonneg_right hamp_le
      (Real.exp_pos (sigmaStar ^ 2 / (2 * a))).le
  exact hdiv.trans hred

theorem gaborKBin_pos : (0 : ℝ) < (gaborKBin : ℝ) := by
  unfold gaborKBin
  norm_num

/-- Stronger plus-lobe comparison: drop the cosine and the
`σ ≤ σ★` Gaussian, without folding `(γ+ω)²` down to `ω²`. -/
theorem gaborPlusTerm_div_E_le_gauss
    {sigmaStar a omega sigma gamma : ℝ} (ha : 0 < a)
    (hσ0 : 0 ≤ sigma) (hσ : sigma ≤ sigmaStar) :
    gaborPlusTerm a omega sigma gamma / gaborEnhancement sigmaStar a ≤
      Real.exp (-(gamma + omega) ^ 2 / (2 * a)) := by
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hcos : Real.cos (sigma * (gamma + omega) / a) ≤ 1 := Real.cos_le_one _
  have hamp0 : 0 ≤
      Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) :=
    (Real.exp_pos _).le
  have hcancel :
      gaborPlusTerm a omega sigma gamma / gaborEnhancement sigmaStar a =
        (Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) *
            Real.cos (sigma * (gamma + omega) / a)) /
          Real.exp (sigmaStar ^ 2 / (2 * a)) := by
    unfold gaborPlusTerm gaborEnhancement
    field_simp [ha0, Real.pi_pos.ne']
  rw [hcancel]
  have hamp_le :
      Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) *
          Real.cos (sigma * (gamma + omega) / a) ≤
        Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) :=
    mul_le_of_le_one_right hamp0 hcos
  have hdiv :
      (Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) *
          Real.cos (sigma * (gamma + omega) / a)) /
        Real.exp (sigmaStar ^ 2 / (2 * a)) ≤
        Real.exp ((sigma ^ 2 - (gamma + omega) ^ 2) / (2 * a)) /
          Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    div_le_div_of_nonneg_right hamp_le
      (Real.exp_pos (sigmaStar ^ 2 / (2 * a))).le
  refine hdiv.trans ?_
  rw [← Real.exp_sub]
  refine Real.exp_le_exp.mpr ?_
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hσsq : sigma ^ 2 ≤ sigmaStar ^ 2 :=
    sq_le_sq.mpr (by
      rwa [abs_of_nonneg hσ0, abs_of_nonneg (hσ0.trans hσ)])
  rw [div_sub_div_same]
  exact div_le_div_of_nonneg_right (by linarith) hden.le

theorem gaborMinusTerm_div_E_le_gauss
    {sigmaStar a omega sigma gamma : ℝ} (ha : 0 < a)
    (hσ0 : 0 ≤ sigma) (hσ : sigma ≤ sigmaStar) :
    gaborMinusTerm a omega sigma gamma / gaborEnhancement sigmaStar a ≤
      Real.exp (-(gamma - omega) ^ 2 / (2 * a)) := by
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hcos : Real.cos (sigma * (gamma - omega) / a) ≤ 1 := Real.cos_le_one _
  have hamp0 : 0 ≤
      Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a)) :=
    (Real.exp_pos _).le
  have hcancel :
      gaborMinusTerm a omega sigma gamma / gaborEnhancement sigmaStar a =
        (Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a)) *
            Real.cos (sigma * (gamma - omega) / a)) /
          Real.exp (sigmaStar ^ 2 / (2 * a)) := by
    unfold gaborMinusTerm gaborEnhancement
    field_simp [ha0, Real.pi_pos.ne']
  rw [hcancel]
  have hamp_le :
      Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a)) *
          Real.cos (sigma * (gamma - omega) / a) ≤
        Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a)) :=
    mul_le_of_le_one_right hamp0 hcos
  have hdiv :
      (Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a)) *
          Real.cos (sigma * (gamma - omega) / a)) /
        Real.exp (sigmaStar ^ 2 / (2 * a)) ≤
        Real.exp ((sigma ^ 2 - (gamma - omega) ^ 2) / (2 * a)) /
          Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    div_le_div_of_nonneg_right hamp_le
      (Real.exp_pos (sigmaStar ^ 2 / (2 * a))).le
  refine hdiv.trans ?_
  rw [← Real.exp_sub]
  refine Real.exp_le_exp.mpr ?_
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hσsq : sigma ^ 2 ≤ sigmaStar ^ 2 :=
    sq_le_sq.mpr (by
      rwa [abs_of_nonneg hσ0, abs_of_nonneg (hσ0.trans hσ)])
  rw [div_sub_div_same]
  exact div_le_div_of_nonneg_right (by linarith) hden.le

theorem gaborCrossTerm_div_E_le_gauss
    {sigmaStar a omega sigma gamma : ℝ} (ha : 0 < a)
    (hσ0 : 0 ≤ sigma) (hσ : sigma ≤ sigmaStar) :
    gaborCrossTerm a omega sigma gamma / gaborEnhancement sigmaStar a ≤
      Real.exp (-(gamma ^ 2 + omega ^ 2) / (2 * a)) := by
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hcos : Real.cos (sigma * gamma / a) ≤ 1 := Real.cos_le_one _
  have hamp0 : 0 ≤
      Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) :=
    (Real.exp_pos _).le
  have hcancel :
      gaborCrossTerm a omega sigma gamma / gaborEnhancement sigmaStar a =
        (Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) *
            Real.cos (sigma * gamma / a)) /
          Real.exp (sigmaStar ^ 2 / (2 * a)) := by
    unfold gaborCrossTerm gaborEnhancement
    field_simp [ha0, Real.pi_pos.ne']
  rw [hcancel]
  have hamp_le :
      Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) *
          Real.cos (sigma * gamma / a) ≤
        Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) :=
    mul_le_of_le_one_right hamp0 hcos
  have hdiv :
      (Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) *
          Real.cos (sigma * gamma / a)) /
        Real.exp (sigmaStar ^ 2 / (2 * a)) ≤
        Real.exp ((sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a)) /
          Real.exp (sigmaStar ^ 2 / (2 * a)) :=
    div_le_div_of_nonneg_right hamp_le
      (Real.exp_pos (sigmaStar ^ 2 / (2 * a))).le
  refine hdiv.trans ?_
  rw [← Real.exp_sub]
  refine Real.exp_le_exp.mpr ?_
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hσsq : sigma ^ 2 ≤ sigmaStar ^ 2 :=
    sq_le_sq.mpr (by
      rwa [abs_of_nonneg hσ0, abs_of_nonneg (hσ0.trans hσ)])
  have hident :
      (sigma ^ 2 - gamma ^ 2 - omega ^ 2) / (2 * a) -
          sigmaStar ^ 2 / (2 * a) =
        ((sigma ^ 2 - sigmaStar ^ 2) - (gamma ^ 2 + omega ^ 2)) / (2 * a) := by
    field_simp [ne_of_gt hden]
    ring
  rw [hident]
  exact div_le_div_of_nonneg_right (by linarith) hden.le

theorem gaborCrossTerm_div_E_le_lobe
    {sigmaStar a omega sigma gamma : ℝ} (ha : 0 < a)
    (hσ0 : 0 ≤ sigma) (hσ : sigma ≤ sigmaStar) :
    gaborCrossTerm a omega sigma gamma / gaborEnhancement sigmaStar a ≤
      Real.exp (-omega ^ 2 / (2 * a)) *
        Real.exp (-gamma ^ 2 / (2 * a)) := by
  have h :=
    gaborCrossTerm_div_E_le_gauss (sigmaStar := sigmaStar) (omega := omega)
      (sigma := sigma) (gamma := gamma) ha hσ0 hσ
  refine h.trans_eq ?_
  rw [← Real.exp_add]
  congr 1
  ring

theorem gaborPlusBin_geom {a omega : ℝ} (ha : 0 < a) (hω : 0 < omega)
    (k : ℕ) :
    Real.exp (-((k : ℝ) + omega) ^ 2 / (2 * a)) ≤
      Real.exp (-omega ^ 2 / (2 * a)) *
        (Real.exp (-omega / a)) ^ k := by
  have hsq : ((k : ℝ) + omega) ^ 2 =
      (k : ℝ) ^ 2 + 2 * (k : ℝ) * omega + omega ^ 2 := by ring
  have hden : 0 < 2 * a := mul_pos (by norm_num) ha
  have hk : 0 ≤ (k : ℝ) ^ 2 / (2 * a) :=
    div_nonneg (sq_nonneg _) hden.le
  have hexp : Real.exp (-((k : ℝ) * omega / a)) =
      (Real.exp (-omega / a)) ^ k := by
    rw [show -((k : ℝ) * omega / a) = (k : ℝ) * (-omega / a) by ring,
      Real.exp_nat_mul]
  have hle : -((k : ℝ) + omega) ^ 2 / (2 * a) ≤
      -omega ^ 2 / (2 * a) + -((k : ℝ) * omega / a) := by
    rw [neg_div, neg_div, ← neg_add]
    refine neg_le_neg ?_
    have hident :
        ((k : ℝ) + omega) ^ 2 / (2 * a) =
          (k : ℝ) ^ 2 / (2 * a) + (k : ℝ) * omega / a +
            omega ^ 2 / (2 * a) := by
      rw [hsq]
      field_simp [ne_of_gt hden]
    rw [hident]
    linarith [hk]
  have hmul := Real.exp_le_exp.mpr hle
  rw [Real.exp_add] at hmul
  rwa [hexp] at hmul

theorem gaborPlusGeomSeries {a omega : ℝ} (ha : 0 < a) (hω : 0 < omega) :
    (∑' k : ℕ, (Real.exp (-omega / a)) ^ k) =
      1 / (1 - Real.exp (-omega / a)) := by
  have hξ0 : 0 ≤ Real.exp (-omega / a) := (Real.exp_pos _).le
  have hξ1 : Real.exp (-omega / a) < 1 := by
    rw [Real.exp_lt_one_iff]
    exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hω) ha
  simpa [one_div] using tsum_geometric_of_lt_one hξ0 hξ1

theorem gaborPlusLobe_majorant {a omega : ℝ} (ha : 0 < a)
    (hω : 0 < omega) :
    (∑' k : ℕ, Real.exp (-((k : ℝ) + omega) ^ 2 / (2 * a))) ≤
      Real.exp (-omega ^ 2 / (2 * a)) / (1 - Real.exp (-omega / a)) := by
  have hξ : Real.exp (-omega / a) < 1 := by
    rw [Real.exp_lt_one_iff]
    exact div_neg_of_neg_of_pos (neg_lt_zero.mpr hω) ha
  have hsummable :
      Summable fun k : ℕ => (Real.exp (-omega / a)) ^ k :=
    summable_geometric_of_lt_one (Real.exp_pos _).le hξ
  have hpos : 0 ≤ Real.exp (-omega ^ 2 / (2 * a)) := (Real.exp_pos _).le
  have hterm : ∀ k : ℕ,
      Real.exp (-((k : ℝ) + omega) ^ 2 / (2 * a)) ≤
        Real.exp (-omega ^ 2 / (2 * a)) * (Real.exp (-omega / a)) ^ k :=
    fun k => gaborPlusBin_geom ha hω k
  have hsum :=
    Summable.tsum_le_tsum hterm
      (Summable.of_nonneg_of_le (fun _ => (Real.exp_pos _).le) hterm
        (hsummable.mul_left _))
      (hsummable.mul_left _)
  refine hsum.trans_eq ?_
  rw [tsum_mul_left, gaborPlusGeomSeries ha hω]
  field_simp

/-! ## (3d) Host-merge: exact copies contribute `m★ · (−η · E)` -/

theorem gaborHostMinusLobe {sigma gamma a : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) :
    Real.exp ((sigma ^ 2 -
        (gamma - gaborIsolationOmega sigma gamma a) ^ 2) / (2 * a)) *
      Real.cos (sigma * (gamma - gaborIsolationOmega sigma gamma a) / a) =
      -gaborEtaTune sigma a * Real.exp (sigma ^ 2 / (2 * a)) := by
  have ha0 : a ≠ 0 := ne_of_gt ha
  have hs0 : sigma ≠ 0 := ne_of_gt hs
  have hφ : sigma * (gamma - gaborIsolationOmega sigma gamma a) / a =
      Real.pi := by
    simpa [gaborPhiMinus] using gaborPhiMinus_host hs0 ha0
  have hdet : gamma - gaborIsolationOmega sigma gamma a =
      Real.pi * a / sigma := by
    unfold gaborIsolationOmega
    ring
  have hcos : Real.cos (sigma * (gamma - gaborIsolationOmega sigma gamma a) / a) =
      -1 := by
    rw [hφ, Real.cos_pi]
  rw [hcos, hdet]
  have hsq : (Real.pi * a / sigma) ^ 2 = Real.pi ^ 2 * a ^ 2 / sigma ^ 2 := by
    field_simp [hs0]
  have hexp :
      Real.exp ((sigma ^ 2 - (Real.pi * a / sigma) ^ 2) / (2 * a)) =
        Real.exp (sigma ^ 2 / (2 * a)) * gaborEtaTune sigma a := by
    unfold gaborEtaTune
    rw [hsq, ← Real.exp_add]
    congr 1
    field_simp [ha0, hs0]
    ring
  rw [hexp]
  ring

theorem gaborHostMerge_minusLobe {sigma gamma a : ℝ} (m : ℕ)
    (hs : 0 < sigma) (ha : 0 < a) :
    (m : ℝ) * gaborMinusTerm a (gaborIsolationOmega sigma gamma a) sigma gamma =
      (m : ℝ) * (-gaborEtaTune sigma a) * gaborEnhancement sigma a := by
  unfold gaborMinusTerm gaborEnhancement
  have h := gaborHostMinusLobe (gamma := gamma) hs ha
  have hmul :
      Real.pi / a *
          (Real.exp ((sigma ^ 2 -
              (gamma - gaborIsolationOmega sigma gamma a) ^ 2) / (2 * a)) *
            Real.cos (sigma *
              (gamma - gaborIsolationOmega sigma gamma a) / a)) =
        Real.pi / a *
          (-gaborEtaTune sigma a * Real.exp (sigma ^ 2 / (2 * a))) := by
    rw [h]
  calc
    (m : ℝ) * (Real.pi / a *
        (Real.exp ((sigma ^ 2 -
            (gamma - gaborIsolationOmega sigma gamma a) ^ 2) / (2 * a)) *
          Real.cos (sigma *
            (gamma - gaborIsolationOmega sigma gamma a) / a)))
        = (m : ℝ) * (Real.pi / a *
            (-gaborEtaTune sigma a * Real.exp (sigma ^ 2 / (2 * a)))) := by
          rw [h]
    _ = (m : ℝ) * (-gaborEtaTune sigma a) *
          (Real.pi / a * Real.exp (sigma ^ 2 / (2 * a))) := by
          ring

theorem gaborHonestWeil_linear (a omega : ℝ) (Z : GaborCanonicalConfig)
    (Cinc : ℝ) :
    gaborHonestWeil a omega Z Cinc =
      Z.pts.sum (fun q =>
          (Z.mult q : ℝ) * gaborQuadrupole a omega q.1 q.2) +
        gaborHonestOnlineBudget a omega Cinc :=
  rfl

/-! ## (3) Isolation-shrink as a function -/

lemma gaborKBin_four : (4 : ℝ) * (gaborKBin : ℝ) = 172 := by
  unfold gaborKBin
  norm_num

lemma log_le_sqrt_of_four_le {x : ℝ} (hx : 4 ≤ x) :
    Real.log x ≤ Real.sqrt x := by
  have hx0 : 0 < x := lt_of_lt_of_le (by norm_num) hx
  have hs : (2 : ℝ) ≤ Real.sqrt x :=
    (Real.le_sqrt (by norm_num : (0 : ℝ) ≤ 2) hx0.le).mpr (by nlinarith [hx])
  have hs0 : 0 < Real.sqrt x := lt_of_lt_of_le (by norm_num) hs
  have hle := Real.add_one_le_exp (Real.sqrt x / 4)
  have hexp : (1 + Real.sqrt x / 4) ^ 2 ≤ Real.exp (Real.sqrt x / 2) := by
    calc
      (1 + Real.sqrt x / 4) ^ 2
          = (Real.sqrt x / 4 + 1) * (Real.sqrt x / 4 + 1) := by ring
      _ ≤ Real.exp (Real.sqrt x / 4) * Real.exp (Real.sqrt x / 4) :=
          mul_le_mul hle hle (by positivity) (Real.exp_pos _).le
      _ = Real.exp (Real.sqrt x / 2) := by
        rw [← Real.exp_add]
        congr 1
        ring
  have hge : Real.sqrt x ≤ (1 + Real.sqrt x / 4) ^ 2 := by
    have hpoly : Real.sqrt x ≤
        1 + Real.sqrt x / 2 + Real.sqrt x ^ 2 / 16 := by
      nlinarith [sq_nonneg (Real.sqrt x - 4)]
    convert hpoly using 1
    ring
  have hge' : Real.sqrt x ≤ Real.exp (Real.sqrt x / 2) := hge.trans hexp
  have hlog_sqrt : Real.log (Real.sqrt x) ≤ Real.sqrt x / 2 := by
    rw [← Real.exp_le_exp, Real.exp_log hs0]
    exact hge'
  have hhalf : Real.log (Real.sqrt x) = Real.log x / 2 := by
    rw [Real.sqrt_eq_rpow, Real.log_rpow hx0]
    ring
  rw [hhalf] at hlog_sqrt
  linarith

lemma isolation_log_arg_eq {a : ℝ} (ha : 0 < a)
    (hle : a ≤ 1 / (4 * (gaborKBin : ℝ))) :
    max (1 / a) (4 * (gaborKBin : ℝ)) = 1 / a := by
  apply max_eq_left
  have hbin : (0 : ℝ) < 4 * (gaborKBin : ℝ) := by
    unfold gaborKBin
    norm_num
  have hmul : a * (4 * (gaborKBin : ℝ)) ≤ 1 := (le_div_iff₀ hbin).mp hle
  exact (le_div_iff₀ ha).mpr (mul_comm a _ ▸ hmul)

/-- Witness integer for a constructive small `a = 1/n`. -/
noncomputable def isolationShrinkWitnessNat (sigma dMin : ℝ) : ℕ :=
  max 173 <|
    max (Nat.ceil (1 / gaborALock sigma)) <|
      max (Nat.ceil ((32 / dMin ^ 2) ^ 2))
        (Nat.ceil (4 * Real.pi / (sigma * dMin)))

lemma isolationShrinkWitnessNat_ge_173 (sigma dMin : ℝ) :
    173 ≤ isolationShrinkWitnessNat sigma dMin :=
  le_max_left _ _

lemma isolationShrinkWitnessNat_ge_ceil_inv (sigma dMin : ℝ) :
    Nat.ceil (1 / gaborALock sigma) ≤ isolationShrinkWitnessNat sigma dMin := by
  unfold isolationShrinkWitnessNat
  exact le_max_of_le_right (le_max_left _ _)

lemma isolationShrinkWitnessNat_ge_ceil_eps (sigma dMin : ℝ) :
    Nat.ceil ((32 / dMin ^ 2) ^ 2) ≤ isolationShrinkWitnessNat sigma dMin := by
  unfold isolationShrinkWitnessNat
  exact le_max_of_le_right (le_max_of_le_right (le_max_left _ _))

lemma isolationShrinkWitnessNat_ge_ceil_pi (sigma dMin : ℝ) :
    Nat.ceil (4 * Real.pi / (sigma * dMin)) ≤
      isolationShrinkWitnessNat sigma dMin := by
  unfold isolationShrinkWitnessNat
  exact le_max_of_le_right (le_max_of_le_right (le_max_right _ _))

lemma isolation_witness_pos (sigma dMin : ℝ) :
    0 < isolationShrinkWitnessNat sigma dMin :=
  lt_of_lt_of_le (by norm_num : (0 : ℕ) < 173)
    (isolationShrinkWitnessNat_ge_173 sigma dMin)

theorem exists_isolationShrink {sigma dMin : ℝ}
    (hs : 0 < sigma) (hd : 0 < dMin) :
    ∃ a : ℝ, 0 < a ∧ a ≤ gaborALock sigma ∧
      gaborIsolationRadius sigma a ≤ dMin / 2 := by
  let n := isolationShrinkWitnessNat sigma dMin
  have hn173 : 173 ≤ n := isolationShrinkWitnessNat_ge_173 sigma dMin
  have hn0 : 0 < n := isolation_witness_pos sigma dMin
  have hnR : (173 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn173
  let a : ℝ := (n : ℝ)⁻¹
  have ha : 0 < a := inv_pos.mpr (Nat.cast_pos.mpr hn0)
  have hA : 0 < gaborALock sigma := gaborALock_pos (ne_of_gt hs)
  have ha_eq : a = 1 / (n : ℝ) := inv_eq_one_div _
  have hlock : a ≤ gaborALock sigma := by
    have hceil : Nat.ceil (1 / gaborALock sigma) ≤ n :=
      isolationShrinkWitnessNat_ge_ceil_inv sigma dMin
    have hx : 1 / gaborALock sigma ≤ (n : ℝ) :=
      (Nat.le_ceil _).trans (by exact_mod_cast hceil)
    rw [ha_eq]
    have hone : (1 : ℝ) ≤ (n : ℝ) * gaborALock sigma :=
      (div_le_iff₀ hA).mp hx
    exact (div_le_iff₀ (Nat.cast_pos.mpr hn0)).mpr (by
      convert hone using 1
      ring)
  refine ⟨a, ha, hlock, ?_⟩
  have hpi : Real.pi * a / sigma ≤ dMin / 4 := by
    have hceil : Nat.ceil (4 * Real.pi / (sigma * dMin)) ≤ n :=
      isolationShrinkWitnessNat_ge_ceil_pi sigma dMin
    have hx : 4 * Real.pi / (sigma * dMin) ≤ (n : ℝ) :=
      (Nat.le_ceil _).trans (by exact_mod_cast hceil)
    have hden : 0 < sigma * dMin := mul_pos hs hd
    have hx' : 4 * Real.pi ≤ (n : ℝ) * (sigma * dMin) :=
      (div_le_iff₀ hden).mp hx
    rw [ha_eq]
    have hform : Real.pi * (1 / (n : ℝ)) / sigma =
        Real.pi / ((n : ℝ) * sigma) := by
      field_simp
    rw [hform, div_le_div_iff₀ (mul_pos (Nat.cast_pos.mpr hn0) hs)
      (by norm_num : (0 : ℝ) < 4)]
    convert hx' using 1 <;> ring
  have hε : gaborIsolationEpsilon a ≤ dMin / 4 := by
    have hle : a ≤ 1 / (4 * (gaborKBin : ℝ)) := by
      have h172 : (172 : ℝ) ≤ (n : ℝ) :=
        le_trans (by norm_num : (172 : ℝ) ≤ 173) hnR
      have hbin : (4 : ℝ) * (gaborKBin : ℝ) = 172 := gaborKBin_four
      rw [ha_eq, hbin, one_div_le_one_div (Nat.cast_pos.mpr hn0) (by norm_num)]
      exact h172
    have hmax := isolation_log_arg_eq ha hle
    have harg : max (1 / a) (4 * (gaborKBin : ℝ)) = (n : ℝ) := by
      rw [hmax, ha_eq, one_div_one_div]
    have hlog : Real.log (max (1 / a) (4 * (gaborKBin : ℝ))) ≤
        Real.sqrt (n : ℝ) := by
      rw [harg]
      exact log_le_sqrt_of_four_le
        (le_trans (by norm_num : (4 : ℝ) ≤ 173) hnR)
    have hlognn : (1 : ℝ) ≤ max (1 / a) (4 * (gaborKBin : ℝ)) :=
      le_trans (by norm_num : (1 : ℝ) ≤ 172)
        (by rw [← gaborKBin_four]; exact le_max_right _ _)
    have hsq : gaborIsolationEpsilon a ^ 2 =
        2 * a * Real.log (max (1 / a) (4 * (gaborKBin : ℝ))) := by
      unfold gaborIsolationEpsilon
      exact Real.sq_sqrt (mul_nonneg (mul_nonneg (by norm_num) ha.le)
        (Real.log_nonneg hlognn))
    have hpos : 0 < Real.sqrt (n : ℝ) :=
      Real.sqrt_pos.mpr (Nat.cast_pos.mpr hn0)
    have hnpos : (0 : ℝ) < n := Nat.cast_pos.mpr hn0
    have hsq' : gaborIsolationEpsilon a ^ 2 ≤ 2 / Real.sqrt (n : ℝ) := by
      rw [hsq]
      have hle' :
          2 * a * Real.log (max (1 / a) (4 * (gaborKBin : ℝ))) ≤
            2 * a * Real.sqrt (n : ℝ) :=
        mul_le_mul_of_nonneg_left hlog (by positivity)
      refine hle'.trans ?_
      rw [ha_eq]
      have heq : 2 * (1 / (n : ℝ)) * Real.sqrt (n : ℝ) =
          2 / Real.sqrt (n : ℝ) := by
        calc
          2 * (1 / (n : ℝ)) * Real.sqrt (n : ℝ)
              = 2 * Real.sqrt (n : ℝ) / (n : ℝ) := by ring
          _ = 2 * Real.sqrt (n : ℝ) /
                (Real.sqrt (n : ℝ) * Real.sqrt (n : ℝ)) := by
              rw [Real.mul_self_sqrt hnpos.le]
          _ = 2 / Real.sqrt (n : ℝ) := by
              field_simp [ne_of_gt hpos]
      exact heq.le
    have hceil : Nat.ceil ((32 / dMin ^ 2) ^ 2) ≤ n :=
      isolationShrinkWitnessNat_ge_ceil_eps sigma dMin
    have hnge : (32 / dMin ^ 2) ^ 2 ≤ (n : ℝ) :=
      (Nat.le_ceil _).trans (by exact_mod_cast hceil)
    have h32 : 0 ≤ 32 / dMin ^ 2 := div_nonneg (by norm_num) (sq_nonneg _)
    have hsqrt : 32 / dMin ^ 2 ≤ Real.sqrt (n : ℝ) :=
      (Real.le_sqrt h32 (Nat.cast_nonneg _)).mpr hnge
    have h2 : 2 / Real.sqrt (n : ℝ) ≤ dMin ^ 2 / 16 := by
      have hprod : 32 ≤ Real.sqrt (n : ℝ) * dMin ^ 2 :=
        (div_le_iff₀ (sq_pos_of_pos hd)).mp hsqrt
      rw [div_le_div_iff₀ hpos (by norm_num : (0 : ℝ) < 16)]
      convert hprod using 1 <;> ring
    have hεsq : gaborIsolationEpsilon a ^ 2 ≤ (dMin / 4) ^ 2 :=
      hsq'.trans (h2.trans_eq (by ring))
    have hε0 : 0 ≤ gaborIsolationEpsilon a := Real.sqrt_nonneg _
    have hd0 : 0 ≤ dMin / 4 := div_nonneg hd.le (by norm_num)
    have habs : |gaborIsolationEpsilon a| ≤ |dMin / 4| :=
      sq_le_sq.mp hεsq
    rwa [abs_of_nonneg hε0, abs_of_nonneg hd0] at habs
  unfold gaborIsolationRadius
  linarith [hpi, hε]

/-! ## (3e) Canonical shrink: ω>0 and greatest admissible width -/

theorem gaborOmegaCap_pos {sigma gamma : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) :
    0 < gaborOmegaCap sigma gamma :=
  div_pos (mul_pos hg hs) (mul_pos (by norm_num) Real.pi_pos)

theorem gaborAdmissibleAMax_pos {sigma gamma : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) :
    0 < gaborAdmissibleAMax sigma gamma :=
  lt_min (gaborALock_pos (ne_of_gt hs)) (gaborOmegaCap_pos hs hg)

/-- Width that forces `R_on/E ≤ O(e^{-256})` via `a ≤ σ²/512` plus
an extra `log(C_inc+1)` factor, without a numeric `C_inc` bound. -/
noncomputable def gaborOnlineSmallnessA (sigma : ℝ) : ℝ :=
  sigma ^ 2 / (2 * (Real.log (gaborCInc + 1) + 256))

/-- r582 ω-dependent online cap: absorbs an extra `log(γ+3)`
against `R_on_log / E`.  Well-defined in `γ` (`ω ≤ γ`). -/
noncomputable def gaborOnlineSmallnessALog (sigma gamma : ℝ) : ℝ :=
  sigma ^ 2 / (2 * (Real.log (gaborCInc + 1) + Real.log (gamma + 3) + 256))

theorem gaborOnlineSmallnessA_pos {sigma : ℝ} (hs : 0 < sigma) :
    0 < gaborOnlineSmallnessA sigma := by
  have hC : 0 < gaborCInc :=
    mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos
  have hlog : 0 ≤ Real.log (gaborCInc + 1) :=
    Real.log_nonneg (by linarith)
  exact div_pos (sq_pos_of_pos hs)
    (mul_pos (by norm_num) (add_pos_of_nonneg_of_pos hlog (by norm_num)))

theorem gaborOnlineSmallnessALog_pos {sigma gamma : ℝ}
    (hs : 0 < sigma) (hg : -2 ≤ gamma) :
    0 < gaborOnlineSmallnessALog sigma gamma := by
  have hC : 0 < gaborCInc :=
    mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos
  have hlogC : 0 ≤ Real.log (gaborCInc + 1) :=
    Real.log_nonneg (by linarith)
  have hlogγ : 0 ≤ Real.log (gamma + 3) :=
    Real.log_nonneg (by linarith)
  exact div_pos (sq_pos_of_pos hs)
    (mul_pos (by norm_num)
      (add_pos_of_nonneg_of_pos (add_nonneg hlogC hlogγ) (by norm_num)))

/-- Plus-lobe analog of `gaborOnlineSmallnessA`: `ω ≥ γ/2` then
`ω²/2a ≥ log(C_inc+1)+256`, so a `C_inner`-prefactor times
`e^{-ω²/2a}` stays `O(e^{-256})`. -/
noncomputable def gaborPlusSmallnessA (gamma : ℝ) : ℝ :=
  gamma ^ 2 / (8 * (Real.log (gaborCInc + 1) + 256))

theorem gaborPlusSmallnessA_pos {gamma : ℝ} (hg : 0 < gamma) :
    0 < gaborPlusSmallnessA gamma := by
  have hC : 0 < gaborCInc :=
    mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos
  have hlog : 0 ≤ Real.log (gaborCInc + 1) :=
    Real.log_nonneg (by linarith)
  exact div_pos (sq_pos_of_pos hg)
    (mul_pos (by norm_num) (add_pos_of_nonneg_of_pos hlog (by norm_num)))

/-- r575 far-tail / far-central cap.  The `max` is the more
restrictive of
* `1/(2a) ≥ γ + log(C_inner+1) + 20` (linear `|ω|` tail),
* `a ≤ 1/(1600 C_inner (γ+10))` (central `|⌊ω⌋|+4` times `e^{-ε²/2a}=a`).
Conservative extra min; the bin-square cap is usually tighter. -/
noncomputable def gaborFarSmallnessA (gamma : ℝ) : ℝ :=
  1 / max (2 * (gamma + Real.log (zetaZerosInDiskCardBoundInner + 1) + 20))
    (1600 * zetaZerosInDiskCardBoundInner * (gamma + 10))

theorem gaborFarSmallnessA_pos {gamma : ℝ} (hg : 0 < gamma) :
    0 < gaborFarSmallnessA gamma := by
  have hC : 0 < zetaZerosInDiskCardBoundInner :=
    zetaZerosInDiskCardBoundInner_pos
  have hlog : 0 ≤ Real.log (zetaZerosInDiskCardBoundInner + 1) :=
    Real.log_nonneg (by linarith [hC])
  have h1 : 0 <
      2 * (gamma + Real.log (zetaZerosInDiskCardBoundInner + 1) + 20) :=
    mul_pos (by norm_num)
      (add_pos_of_pos_of_nonneg (add_pos_of_pos_of_nonneg hg hlog) (by norm_num))
  exact div_pos (by norm_num) (lt_max_of_lt_left h1)

theorem gaborKBinAt_eq (γ : ℝ) :
    gaborKBinAt γ = gaborCInc * (1 + Real.log (γ + 3)) := by
  unfold gaborKBinAt gaborCInc
  ring

theorem gaborKBinAt_pos {γ : ℝ} (hγ : -2 ≤ γ) : 0 < gaborKBinAt γ := by
  have hlog : 0 ≤ Real.log (γ + 3) :=
    Real.log_nonneg (by linarith)
  exact mul_pos (mul_pos (by norm_num) zetaZerosInDiskCardBoundInner_pos)
    (add_pos_of_pos_of_nonneg (by norm_num) hlog)

/-- `log(14/13) ≤ 1/13 < 1/10`, so `C_inner > 20`. -/
lemma zetaZerosInDiskCardBoundInner_gt_twenty :
    (20 : ℝ) < zetaZerosInDiskCardBoundInner := by
  have hden : Real.log (14 / 13 : ℝ) ≤ (1 / 13 : ℝ) := by
    have := Real.log_le_sub_one_of_pos (by norm_num : (0 : ℝ) < 14 / 13)
    have hsub : (14 / 13 : ℝ) - 1 = 1 / 13 := by norm_num
    rwa [hsub] at this
  have hden0 : 0 < Real.log (14 / 13 : ℝ) := Real.log_pos (by norm_num)
  have hnum : (2 : ℝ) <
      Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2 := by
    have h1 : 0 < Real.log jensenSphereMajorantCoeff :=
      Real.log_pos one_lt_jensenSphereMajorantCoeff
    have h2 : 0 < Real.log ‖riemannZeta 2‖ :=
      Real.log_pos one_lt_norm_riemannZeta_two
    linarith
  have hC : zetaZerosInDiskCardBoundInner =
      (Real.log jensenSphereMajorantCoeff + Real.log ‖riemannZeta 2‖ + 2) /
        Real.log (14 / 13 : ℝ) := rfl
  have hlt : (2 : ℝ) / Real.log (14 / 13 : ℝ) >
      (2 : ℝ) / (1 / 10 : ℝ) :=
    div_lt_div_of_pos_left (by norm_num) hden0
      (hden.trans_lt (by norm_num : (1 / 13 : ℝ) < 1 / 10))
  have h20 : (2 : ℝ) / (1 / 10 : ℝ) = 20 := by norm_num
  have hnumle : (2 : ℝ) / Real.log (14 / 13 : ℝ) <
      zetaZerosInDiskCardBoundInner := by
    rw [hC]
    exact div_lt_div_of_pos_right hnum hden0
  linarith [hlt, h20, hnumle]

theorem gaborKBinAt_ge_gaborKBin {γ : ℝ} (hγ : 0 ≤ γ) :
    (gaborKBin : ℝ) ≤ gaborKBinAt γ := by
  have hC : (20 : ℝ) < zetaZerosInDiskCardBoundInner :=
    zetaZerosInDiskCardBoundInner_gt_twenty
  have hlog3 : (1 : ℝ) < Real.log (γ + 3) := by
    have h3 : Real.exp 1 < (3 : ℝ) :=
      (Real.exp_one_lt_d9).trans (by norm_num)
    have hx : Real.exp 1 < γ + 3 := lt_of_lt_of_le h3 (by linarith [hγ])
    exact (Real.lt_log_iff_exp_lt (by linarith [hγ])).mpr hx
  have hprod : (40 : ℝ) * 2 ≤
      2 * zetaZerosInDiskCardBoundInner * (1 + Real.log (γ + 3)) := by
    have h1 : (40 : ℝ) ≤ 2 * zetaZerosInDiskCardBoundInner := by linarith
    have h2 : (2 : ℝ) ≤ 1 + Real.log (γ + 3) := by linarith [hlog3]
    nlinarith [h1, h2, hC, hlog3]
  have h80 : (gaborKBin : ℝ) ≤ (80 : ℝ) := by
    unfold gaborKBin
    norm_num
  exact h80.trans (by
    unfold gaborKBinAt
    linarith [hprod])

/-- r575 smallness cap.  `γ²/512` uniformises the quadrupole sign,
`1/(8 K_binAt(γ)²)` makes far/plus packings smaller than η against
the counting-theorem occupancy, `gaborOnlineSmallnessA` kills `R_on/E`,
`gaborPlusSmallnessA` kills a `C_inner` times `e^{-ω²/2a}`, and
`gaborFarSmallnessA` kills a linear `|ω|` times `C_inner e^{-1/(2a)}`.
The constant `K_bin = 43` bound is a corollary (`gaborSmallnessA_le_binSq`)
because `K_binAt(γ) ≥ 43` for `γ ≥ 0`. -/
noncomputable def gaborSmallnessA (sigma gamma : ℝ) : ℝ :=
  min (gaborAdmissibleAMax sigma gamma)
    (min (gamma ^ 2 / 512)
      (min (1 / (8 * gaborKBinAt gamma ^ 2))
        (min (gaborOnlineSmallnessA sigma)
          (min (gaborPlusSmallnessA gamma)
            (min (gaborFarSmallnessA gamma)
              (gaborOnlineSmallnessALog sigma gamma))))))

theorem gaborSmallnessA_pos {sigma gamma : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) :
    0 < gaborSmallnessA sigma gamma := by
  refine lt_min (gaborAdmissibleAMax_pos hs hg)
    (lt_min ?_ (lt_min ?_ (lt_min ?_ (lt_min ?_ (lt_min ?_ ?_)))))
  · exact div_pos (sq_pos_of_pos hg) (by norm_num)
  · have hK : 0 < gaborKBinAt gamma := gaborKBinAt_pos (by linarith)
    exact div_pos (by norm_num) (mul_pos (by norm_num) (sq_pos_of_pos hK))
  · exact gaborOnlineSmallnessA_pos hs
  · exact gaborPlusSmallnessA_pos hg
  · exact gaborFarSmallnessA_pos hg
  · exact gaborOnlineSmallnessALog_pos hs (by linarith [hg])

theorem gaborSmallnessA_le_AMax (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ gaborAdmissibleAMax sigma gamma :=
  min_le_left _ _

theorem gaborSmallnessA_le_lock (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ gaborALock sigma :=
  (gaborSmallnessA_le_AMax sigma gamma).trans (min_le_left _ _)

theorem gaborSmallnessA_le_omegaCap (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ gaborOmegaCap sigma gamma :=
  (gaborSmallnessA_le_AMax sigma gamma).trans (min_le_right _ _)

theorem gaborSmallnessA_le_gamma_sq (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ gamma ^ 2 / 512 :=
  (min_le_right _ _).trans (min_le_left _ _)

theorem gaborSmallnessA_le_binSqLog (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ 1 / (8 * gaborKBinAt gamma ^ 2) :=
  (min_le_right _ _).trans ((min_le_right _ _).trans (min_le_left _ _))

/-- Historical constant-43 form: `K_binAt(γ) ≥ 43` for `γ ≥ 0`. -/
theorem gaborSmallnessA_le_binSq (sigma gamma : ℝ) (hg : 0 ≤ gamma) :
    gaborSmallnessA sigma gamma ≤ 1 / (8 * (gaborKBin : ℝ) ^ 2) := by
  refine (gaborSmallnessA_le_binSqLog sigma gamma).trans ?_
  have hK : (gaborKBin : ℝ) ≤ gaborKBinAt gamma :=
    gaborKBinAt_ge_gaborKBin hg
  have hK0 : 0 < (gaborKBin : ℝ) := gaborKBin_pos
  have hK1 : 0 < gaborKBinAt gamma := gaborKBinAt_pos (by linarith)
  have hsq : (gaborKBin : ℝ) ^ 2 ≤ gaborKBinAt gamma ^ 2 :=
    sq_le_sq.mpr (by
      rwa [abs_of_nonneg hK0.le, abs_of_nonneg hK1.le])
  have hpos : 0 < 8 * (gaborKBin : ℝ) ^ 2 :=
    mul_pos (by norm_num) (sq_pos_of_pos hK0)
  have hpos' : 0 < 8 * gaborKBinAt gamma ^ 2 :=
    mul_pos (by norm_num) (sq_pos_of_pos hK1)
  exact one_div_le_one_div_of_le hpos (mul_le_mul_of_nonneg_left hsq (by norm_num))

theorem gaborSmallnessA_le_online (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ gaborOnlineSmallnessA sigma :=
  (min_le_right _ _).trans
    ((min_le_right _ _).trans ((min_le_right _ _).trans (min_le_left _ _)))

theorem gaborSmallnessA_le_plus (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ gaborPlusSmallnessA gamma :=
  (min_le_right _ _).trans
    ((min_le_right _ _).trans ((min_le_right _ _).trans
      ((min_le_right _ _).trans (min_le_left _ _))))

theorem gaborSmallnessA_le_far (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ gaborFarSmallnessA gamma :=
  (min_le_right _ _).trans
    ((min_le_right _ _).trans ((min_le_right _ _).trans
      ((min_le_right _ _).trans ((min_le_right _ _).trans (min_le_left _ _)))))

theorem gaborSmallnessA_le_onlineLog (sigma gamma : ℝ) :
    gaborSmallnessA sigma gamma ≤ gaborOnlineSmallnessALog sigma gamma :=
  (min_le_right _ _).trans
    ((min_le_right _ _).trans ((min_le_right _ _).trans
      ((min_le_right _ _).trans ((min_le_right _ _).trans (min_le_right _ _)))))

theorem gaborIsolationOmega_pos_of_cap {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 ≤ a)
    (hcap : a ≤ gaborOmegaCap sigma gamma) :
    gamma / 2 ≤ gaborIsolationOmega sigma gamma a := by
  unfold gaborIsolationOmega
  have hπ : Real.pi * a / sigma ≤ gamma / 2 := by
    have hmul : Real.pi * a ≤ Real.pi * (gamma * sigma / (2 * Real.pi)) :=
      mul_le_mul_of_nonneg_left hcap Real.pi_pos.le
    have hs0 : sigma ≠ 0 := ne_of_gt hs
    have hπ0 : Real.pi ≠ 0 := Real.pi_pos.ne'
    have : Real.pi * (gamma * sigma / (2 * Real.pi)) / sigma = gamma / 2 := by
      field_simp [hs0, hπ0]
    rw [← this]
    exact div_le_div_of_nonneg_right hmul hs.le
  linarith

theorem gaborIsolationOmega_pos {sigma gamma a : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (ha : 0 ≤ a)
    (hcap : a ≤ gaborOmegaCap sigma gamma) :
    0 < gaborIsolationOmega sigma gamma a :=
  lt_of_lt_of_le (half_pos hg) (gaborIsolationOmega_pos_of_cap hs hg ha hcap)

lemma mul_log_inv_mono {x y : ℝ} (hx : 0 < x) (hxy : x ≤ y)
    (hye : y * Real.exp 1 ≤ 1) :
    x * Real.log (1 / x) ≤ y * Real.log (1 / y) := by
  have hy : 0 < y := lt_of_lt_of_le hx hxy
  have hye' : y ≤ 1 / Real.exp 1 :=
    (le_div_iff₀ (Real.exp_pos _)).mpr (mul_comm y (Real.exp 1) ▸ hye)
  have hlogy : 1 ≤ Real.log (1 / y) := by
    rw [Real.le_log_iff_exp_le (div_pos (by norm_num) hy)]
    exact (le_div_iff₀ hy).mpr (mul_comm y (Real.exp 1) ▸ hye)
  have hz : 0 < y / x := div_pos hy hx
  have hlog : Real.log (y / x) ≤ y / x - 1 :=
    Real.log_le_sub_one_of_pos hz
  have hlog' : x * Real.log (y / x) ≤ y - x := by
    have : Real.log (y / x) ≤ (y - x) / x := by
      have : y / x - 1 = (y - x) / x := by field_simp [ne_of_gt hx]
      rwa [this] at hlog
    exact (mul_le_mul_of_nonneg_left this hx.le).trans_eq
      (by field_simp [ne_of_gt hx])
  have hdiff : y * Real.log (1 / y) - x * Real.log (1 / x) =
      (y - x) * Real.log (1 / y) - x * Real.log (y / x) := by
    have : Real.log (1 / x) = Real.log (1 / y) + Real.log (y / x) := by
      rw [Real.log_div (by norm_num : (1 : ℝ) ≠ 0) (ne_of_gt hx),
        Real.log_div (by norm_num : (1 : ℝ) ≠ 0) (ne_of_gt hy),
        Real.log_div (ne_of_gt hy) (ne_of_gt hx)]
      ring
    rw [this]
    ring
  have hpos : 0 ≤ (y - x) * Real.log (1 / y) - x * Real.log (y / x) := by
    have : x * Real.log (y / x) ≤ (y - x) * Real.log (1 / y) :=
      hlog'.trans (le_mul_of_one_le_right (sub_nonneg.mpr hxy) hlogy)
    linarith
  linarith [hdiff, hpos]

lemma gaborIsolationEpsilon_mono_small {a b : ℝ}
    (ha : 0 < a) (hab : a ≤ b)
    (hbC : b ≤ 1 / (4 * (gaborKBin : ℝ))) :
    gaborIsolationEpsilon a ≤ gaborIsolationEpsilon b := by
  have hb : 0 < b := lt_of_lt_of_le ha hab
  have haC : a ≤ 1 / (4 * (gaborKBin : ℝ)) := hab.trans hbC
  have hma := isolation_log_arg_eq ha haC
  have hmb := isolation_log_arg_eq hb hbC
  have h1e : b * Real.exp 1 ≤ 1 := by
    have hexp : Real.exp 1 < 3 :=
      (Real.exp_one_lt_d9).trans (by norm_num)
    have hb' : b ≤ 1 / 172 := by
      simpa [gaborKBin_four] using hbC
    nlinarith [hexp.le, hb']
  have hcmp := mul_log_inv_mono ha hab h1e
  have hεa : gaborIsolationEpsilon a = Real.sqrt (2 * a * Real.log (1 / a)) := by
    unfold gaborIsolationEpsilon
    rw [hma]
  have hεb : gaborIsolationEpsilon b = Real.sqrt (2 * b * Real.log (1 / b)) := by
    unfold gaborIsolationEpsilon
    rw [hmb]
  rw [hεa, hεb]
  have h2 : 2 * a * Real.log (1 / a) ≤ 2 * b * Real.log (1 / b) := by
    have := mul_le_mul_of_nonneg_left hcmp (by norm_num : (0 : ℝ) ≤ 2)
    convert this using 1 <;> ring
  exact Real.sqrt_le_sqrt h2

lemma gaborIsolationRadius_mono_small {sigma a b : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) (hab : a ≤ b)
    (hbC : b ≤ 1 / (4 * (gaborKBin : ℝ))) :
    gaborIsolationRadius sigma a ≤ gaborIsolationRadius sigma b := by
  unfold gaborIsolationRadius
  have hπ : Real.pi * a / sigma ≤ Real.pi * b / sigma :=
    div_le_div_of_nonneg_right
      (mul_le_mul_of_nonneg_left hab Real.pi_pos.le) hs.le
  exact add_le_add hπ (gaborIsolationEpsilon_mono_small ha hab hbC)

lemma gaborIsolationRadius_strictMono_small {sigma a b : ℝ}
    (hs : 0 < sigma) (ha : 0 < a) (hab : a < b)
    (hbC : b ≤ 1 / (4 * (gaborKBin : ℝ))) :
    gaborIsolationRadius sigma a < gaborIsolationRadius sigma b := by
  unfold gaborIsolationRadius
  have hπ : Real.pi * a / sigma < Real.pi * b / sigma :=
    div_lt_div_of_pos_right
      (mul_lt_mul_of_pos_left hab Real.pi_pos) hs
  have hε := gaborIsolationEpsilon_mono_small ha hab.le hbC
  exact add_lt_add_of_lt_of_le hπ hε

/-- Admissible isolation widths: lock, closed ω>0 cap, and the
radius constraint.  No numeric a-floor. -/
def gaborAdmissibleA (sigma gamma dMin a : ℝ) : Prop :=
  0 < a ∧ a ≤ gaborAdmissibleAMax sigma gamma ∧
    gaborIsolationRadius sigma a ≤ dMin / 2

theorem exists_isolationShrink_omega {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) :
    ∃ a : ℝ, gaborAdmissibleA sigma gamma dMin a ∧
      0 < gaborIsolationOmega sigma gamma a := by
  let n0 := isolationShrinkWitnessNat sigma dMin
  let n := max n0 (Nat.ceil (1 / gaborOmegaCap sigma gamma))
  have hn0 : n0 ≤ n := le_max_left _ _
  have hnω : Nat.ceil (1 / gaborOmegaCap sigma gamma) ≤ n := le_max_right _ _
  have hn173 : 173 ≤ n :=
    (isolationShrinkWitnessNat_ge_173 sigma dMin).trans hn0
  have hn0' : 0 < n :=
    lt_of_lt_of_le (by norm_num : (0 : ℕ) < 173) hn173
  have hnR : (173 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn173
  let a : ℝ := (n : ℝ)⁻¹
  have ha : 0 < a := inv_pos.mpr (Nat.cast_pos.mpr hn0')
  have ha_eq : a = 1 / (n : ℝ) := inv_eq_one_div _
  have hA : 0 < gaborALock sigma := gaborALock_pos (ne_of_gt hs)
  have hlock : a ≤ gaborALock sigma := by
    have hceil : Nat.ceil (1 / gaborALock sigma) ≤ n :=
      (isolationShrinkWitnessNat_ge_ceil_inv sigma dMin).trans hn0
    have hx : 1 / gaborALock sigma ≤ (n : ℝ) :=
      (Nat.le_ceil _).trans (by exact_mod_cast hceil)
    rw [ha_eq]
    have hone : (1 : ℝ) ≤ (n : ℝ) * gaborALock sigma :=
      (div_le_iff₀ hA).mp hx
    exact (div_le_iff₀ (Nat.cast_pos.mpr hn0')).mpr (by
      convert hone using 1
      ring)
  have hcap : a ≤ gaborOmegaCap sigma gamma := by
    have hωpos : 0 < gaborOmegaCap sigma gamma := gaborOmegaCap_pos hs hg
    have hx : 1 / gaborOmegaCap sigma gamma ≤ (n : ℝ) :=
      (Nat.le_ceil _).trans (by exact_mod_cast hnω)
    rw [ha_eq]
    have hone : (1 : ℝ) ≤ (n : ℝ) * gaborOmegaCap sigma gamma :=
      (div_le_iff₀ hωpos).mp hx
    exact (div_le_iff₀ (Nat.cast_pos.mpr hn0')).mpr (by
      convert hone using 1
      ring)
  have hAmax : a ≤ gaborAdmissibleAMax sigma gamma :=
    le_min hlock hcap
  have hsmall : a ≤ 1 / (4 * (gaborKBin : ℝ)) := by
    have h172 : (172 : ℝ) ≤ (n : ℝ) :=
      le_trans (by norm_num : (172 : ℝ) ≤ 173) hnR
    have hbin : (4 : ℝ) * (gaborKBin : ℝ) = 172 := gaborKBin_four
    rw [ha_eq, hbin, one_div_le_one_div (Nat.cast_pos.mpr hn0') (by norm_num)]
    exact h172
  have hrad : gaborIsolationRadius sigma a ≤ dMin / 2 := by
    have hpi : Real.pi * a / sigma ≤ dMin / 4 := by
      have hceil : Nat.ceil (4 * Real.pi / (sigma * dMin)) ≤ n :=
        (isolationShrinkWitnessNat_ge_ceil_pi sigma dMin).trans hn0
      have hx : 4 * Real.pi / (sigma * dMin) ≤ (n : ℝ) :=
        (Nat.le_ceil _).trans (by exact_mod_cast hceil)
      have hden : 0 < sigma * dMin := mul_pos hs hd
      have hx' : 4 * Real.pi ≤ (n : ℝ) * (sigma * dMin) :=
        (div_le_iff₀ hden).mp hx
      rw [ha_eq]
      have hform : Real.pi * (1 / (n : ℝ)) / sigma =
          Real.pi / ((n : ℝ) * sigma) := by
        field_simp
      rw [hform, div_le_div_iff₀ (mul_pos (Nat.cast_pos.mpr hn0') hs)
        (by norm_num : (0 : ℝ) < 4)]
      convert hx' using 1 <;> ring
    have hε : gaborIsolationEpsilon a ≤ dMin / 4 := by
      have hmax := isolation_log_arg_eq ha hsmall
      have harg : max (1 / a) (4 * (gaborKBin : ℝ)) = (n : ℝ) := by
        rw [hmax, ha_eq, one_div_one_div]
      have hlog : Real.log (max (1 / a) (4 * (gaborKBin : ℝ))) ≤
          Real.sqrt (n : ℝ) := by
        rw [harg]
        exact log_le_sqrt_of_four_le
          (le_trans (by norm_num : (4 : ℝ) ≤ 173) hnR)
      have hlognn : (1 : ℝ) ≤ max (1 / a) (4 * (gaborKBin : ℝ)) :=
        le_trans (by norm_num : (1 : ℝ) ≤ 172)
          (by rw [← gaborKBin_four]; exact le_max_right _ _)
      have hsq : gaborIsolationEpsilon a ^ 2 =
          2 * a * Real.log (max (1 / a) (4 * (gaborKBin : ℝ))) := by
        unfold gaborIsolationEpsilon
        exact Real.sq_sqrt (mul_nonneg (mul_nonneg (by norm_num) ha.le)
          (Real.log_nonneg hlognn))
      have hpos : 0 < Real.sqrt (n : ℝ) :=
        Real.sqrt_pos.mpr (Nat.cast_pos.mpr hn0')
      have hnpos : (0 : ℝ) < n := Nat.cast_pos.mpr hn0'
      have hsq' : gaborIsolationEpsilon a ^ 2 ≤ 2 / Real.sqrt (n : ℝ) := by
        rw [hsq]
        have hle' :
            2 * a * Real.log (max (1 / a) (4 * (gaborKBin : ℝ))) ≤
              2 * a * Real.sqrt (n : ℝ) :=
          mul_le_mul_of_nonneg_left hlog (by positivity)
        refine hle'.trans ?_
        rw [ha_eq]
        have heq : 2 * (1 / (n : ℝ)) * Real.sqrt (n : ℝ) =
            2 / Real.sqrt (n : ℝ) := by
          calc
            2 * (1 / (n : ℝ)) * Real.sqrt (n : ℝ)
                = 2 * Real.sqrt (n : ℝ) / (n : ℝ) := by ring
            _ = 2 * Real.sqrt (n : ℝ) /
                  (Real.sqrt (n : ℝ) * Real.sqrt (n : ℝ)) := by
                rw [Real.mul_self_sqrt hnpos.le]
            _ = 2 / Real.sqrt (n : ℝ) := by
                field_simp [ne_of_gt hpos]
        exact heq.le
      have hceil : Nat.ceil ((32 / dMin ^ 2) ^ 2) ≤ n :=
        (isolationShrinkWitnessNat_ge_ceil_eps sigma dMin).trans hn0
      have hnge : (32 / dMin ^ 2) ^ 2 ≤ (n : ℝ) :=
        (Nat.le_ceil _).trans (by exact_mod_cast hceil)
      have h32 : 0 ≤ 32 / dMin ^ 2 := div_nonneg (by norm_num) (sq_nonneg _)
      have hsqrt : 32 / dMin ^ 2 ≤ Real.sqrt (n : ℝ) :=
        (Real.le_sqrt h32 (Nat.cast_nonneg _)).mpr hnge
      have h2 : 2 / Real.sqrt (n : ℝ) ≤ dMin ^ 2 / 16 := by
        have hprod : 32 ≤ Real.sqrt (n : ℝ) * dMin ^ 2 :=
          (div_le_iff₀ (sq_pos_of_pos hd)).mp hsqrt
        rw [div_le_div_iff₀ hpos (by norm_num : (0 : ℝ) < 16)]
        convert hprod using 1 <;> ring
      have hεsq : gaborIsolationEpsilon a ^ 2 ≤ (dMin / 4) ^ 2 :=
        hsq'.trans (h2.trans_eq (by ring))
      have hε0 : 0 ≤ gaborIsolationEpsilon a := Real.sqrt_nonneg _
      have hd0 : 0 ≤ dMin / 4 := div_nonneg hd.le (by norm_num)
      have habs : |gaborIsolationEpsilon a| ≤ |dMin / 4| :=
        sq_le_sq.mp hεsq
      rwa [abs_of_nonneg hε0, abs_of_nonneg hd0] at habs
    unfold gaborIsolationRadius
    linarith [hpi, hε]
  refine ⟨a, ⟨ha, hAmax, hrad⟩, ?_⟩
  exact gaborIsolationOmega_pos hs hg ha.le hcap

lemma gaborALock_lt_inv_bin {sigma : ℝ}
    (hs0 : 0 ≤ sigma) (hs : sigma < 1 / 2) :
    gaborALock sigma < 1 / (4 * (gaborKBin : ℝ)) := by
  have hsq : sigma ^ 2 ≤ (1 / 2 : ℝ) ^ 2 := by nlinarith
  have hlock : gaborALock sigma = (sigma ^ 2 / 64) / 8 := gaborALock_eq sigma
  have hC : (4 : ℝ) * (gaborKBin : ℝ) = 172 := gaborKBin_four
  have hle : gaborALock sigma ≤ 1 / 2048 := by
    rw [hlock]
    nlinarith [hsq]
  have hlt : (1 / 2048 : ℝ) < 1 / 172 := by norm_num
  rw [hC]
  exact hle.trans_lt hlt

lemma continuousOn_gaborIsolationEpsilon_small {a0 A : ℝ}
    (ha0 : 0 < a0) (hA : a0 ≤ A)
    (hAC : A ≤ 1 / (4 * (gaborKBin : ℝ))) :
    ContinuousOn gaborIsolationEpsilon (Set.Icc a0 A) := by
  have hpos : ∀ a ∈ Set.Icc a0 A, 0 < a :=
    fun a ha => lt_of_lt_of_le ha0 ha.1
  have hsmall : ∀ a ∈ Set.Icc a0 A,
      max (1 / a) (4 * (gaborKBin : ℝ)) = 1 / a :=
    fun a ha => isolation_log_arg_eq (hpos a ha) (ha.2.trans hAC)
  have hfun :
      EqOn gaborIsolationEpsilon
        (fun a : ℝ => Real.sqrt (2 * a * Real.log (1 / a)))
        (Set.Icc a0 A) := by
    intro a ha
    unfold gaborIsolationEpsilon
    rw [hsmall a ha]
  have hmul : ContinuousOn
      (fun a : ℝ => 2 * a * Real.log (1 / a)) (Set.Icc a0 A) := by
    have h2 : ContinuousOn (fun _ : ℝ => (2 : ℝ)) (Set.Icc a0 A) :=
      continuousOn_const
    have hid : ContinuousOn (fun a : ℝ => a) (Set.Icc a0 A) :=
      continuousOn_id
    have hlog : ContinuousOn (fun a : ℝ => Real.log (1 / a))
        (Set.Icc a0 A) :=
      Real.continuousOn_log.comp
        ((continuousOn_const (c := (1 : ℝ))).div hid fun a ha =>
          (hpos a ha).ne')
        fun a ha =>
          (div_pos (by norm_num : (0 : ℝ) < 1) (hpos a ha)).ne'
    exact (h2.mul hid).mul hlog
  have hcont : ContinuousOn
      (fun a : ℝ => Real.sqrt (2 * a * Real.log (1 / a)))
      (Set.Icc a0 A) :=
    Continuous.comp_continuousOn Real.continuous_sqrt hmul
  exact hcont.congr hfun

lemma continuousOn_gaborIsolationRadius_small {sigma a0 A : ℝ}
    (hs : 0 < sigma) (ha0 : 0 < a0) (hA : a0 ≤ A)
    (hAC : A ≤ 1 / (4 * (gaborKBin : ℝ))) :
    ContinuousOn (gaborIsolationRadius sigma) (Set.Icc a0 A) := by
  unfold gaborIsolationRadius
  refine ContinuousOn.add ?_
    (continuousOn_gaborIsolationEpsilon_small ha0 hA hAC)
  exact (continuousOn_const.mul continuousOn_id).div continuousOn_const
    fun _ _ => ne_of_gt hs

/-- On the canonical strip `0 < σ < 1/2` the admissible set is a
closed initial segment of `(0, A_max]` and therefore has a greatest
element.  Constraints are monotone in `a`; there is no numeric floor. -/
theorem exists_greatest_isolationShrink {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hs1 : sigma < 1 / 2) (hg : 0 < gamma)
    (hd : 0 < dMin) :
    ∃ a, IsGreatest {a | gaborAdmissibleA sigma gamma dMin a} a := by
  set A := gaborAdmissibleAMax sigma gamma
  have hApos : 0 < A := gaborAdmissibleAMax_pos hs hg
  have hAC : A ≤ 1 / (4 * (gaborKBin : ℝ)) :=
    (min_le_left _ _).trans (gaborALock_lt_inv_bin hs.le hs1).le
  obtain ⟨a0, ha0, hω0⟩ := exists_isolationShrink_omega hs hg hd
  have ha0A : a0 ≤ A := ha0.2.1
  by_cases hAdm : gaborIsolationRadius sigma A ≤ dMin / 2
  · refine ⟨A, ?_⟩
    constructor
    · exact ⟨hApos, le_rfl, hAdm⟩
    · intro a ha
      exact ha.2.1
  · have hcont :=
      continuousOn_gaborIsolationRadius_small (sigma := sigma) hs
        ha0.1 ha0A hAC
    have hle : a0 ≤ A := ha0A
    have hleft : gaborIsolationRadius sigma a0 ≤ dMin / 2 := ha0.2.2
    have hright : dMin / 2 < gaborIsolationRadius sigma A := lt_of_not_ge hAdm
    have hivt :
        ∃ a ∈ Set.Icc a0 A,
          gaborIsolationRadius sigma a = dMin / 2 := by
      have himg :=
        intermediate_value_Icc hle hcont
      have hmem :
          dMin / 2 ∈ Set.Icc (gaborIsolationRadius sigma a0)
            (gaborIsolationRadius sigma A) :=
        ⟨hleft, hright.le⟩
      exact himg hmem
    obtain ⟨aStar, haI, hradEq⟩ := hivt
    refine ⟨aStar, ?_⟩
    constructor
    · exact ⟨lt_of_lt_of_le ha0.1 haI.1, haI.2, hradEq.le⟩
    · intro a ha
      have haA : a ≤ A := ha.2.1
      have haC : a ≤ 1 / (4 * (gaborKBin : ℝ)) := haA.trans hAC
      by_contra hgt
      have hlt : aStar < a := lt_of_not_ge hgt
      have hapos : 0 < a := ha.1
      have hmono :=
        gaborIsolationRadius_strictMono_small (sigma := sigma) hs
          (lt_of_lt_of_le ha0.1 haI.1) hlt haC
      have : dMin / 2 < gaborIsolationRadius sigma a := by
        rw [← hradEq]
        exact hmono
      exact (not_lt_of_ge ha.2.2) this

/-- Isolation-shrink map `(σ★,γ★,d_min) ↦ (a,ω)` with `ω>0`.
Noncomputable choice of an admissible width; on the canonical strip
the greatest admissible width exists separately. -/
noncomputable def isolationShrink (sigma gamma dMin : ℝ)
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) : ℝ × ℝ :=
  let a := Classical.choose (exists_isolationShrink_omega hs hg hd)
  (a, gaborIsolationOmega sigma gamma a)

/-- `d_min = +∞` rule: `a = min(a_lock, γσ/(2π))`. -/
noncomputable def isolationShrinkTop (sigma gamma : ℝ)
    (hs : 0 < sigma) (hg : 0 < gamma) : ℝ × ℝ :=
  (gaborAdmissibleAMax sigma gamma,
    gaborIsolationOmega sigma gamma (gaborAdmissibleAMax sigma gamma))

theorem isolationShrink_spec {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) :
    gaborAdmissibleA sigma gamma dMin
        (isolationShrink sigma gamma dMin hs hg hd).1 ∧
      0 < gaborIsolationOmega sigma gamma
        (isolationShrink sigma gamma dMin hs hg hd).1 ∧
      (isolationShrink sigma gamma dMin hs hg hd).2 =
        gaborIsolationOmega sigma gamma
          (isolationShrink sigma gamma dMin hs hg hd).1 := by
  let a := Classical.choose (exists_isolationShrink_omega hs hg hd)
  have h := Classical.choose_spec (exists_isolationShrink_omega hs hg hd)
  refine ⟨h.1, h.2, ?_⟩
  simp [isolationShrink]

theorem isolationShrink_a_pos {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) :
    0 < (isolationShrink sigma gamma dMin hs hg hd).1 :=
  (isolationShrink_spec hs hg hd).1.1

theorem isolationShrinkTop_a_pos {sigma gamma : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) :
    0 < (isolationShrinkTop sigma gamma hs hg).1 := by
  simpa [isolationShrinkTop] using gaborAdmissibleAMax_pos hs hg

theorem isolationShrink_omega_pos {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) :
    0 < (isolationShrink sigma gamma dMin hs hg hd).2 := by
  have h := isolationShrink_spec hs hg hd
  rw [h.2.2]
  exact h.2.1

/-- The exception window `I_exc = [ω−ε, ω+ε]` contains no foreign
ordinate at gap `≥ d_min`. -/
theorem isolationShrink_exceptionWindow_empty {sigma gamma dMin : ℝ}
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) {gamma' : ℝ}
    (hgap : dMin ≤ |gamma' - gamma|) :
    gaborIsolationEpsilon (isolationShrink sigma gamma dMin hs hg hd).1 ≤
      |gamma' - (isolationShrink sigma gamma dMin hs hg hd).2| := by
  have hspec := isolationShrink_spec hs hg hd
  set a := (isolationShrink sigma gamma dMin hs hg hd).1
  set omega := (isolationShrink sigma gamma dMin hs hg hd).2
  have hω : omega = gamma - Real.pi * a / sigma := by
    simpa [gaborIsolationOmega] using hspec.2.2
  have hrad : Real.pi * a / sigma + gaborIsolationEpsilon a ≤ dMin / 2 := by
    simpa [gaborIsolationRadius, a] using hspec.1.2.2
  have hdet : |omega - gamma| = Real.pi * a / sigma := by
    rw [hω]
    have hpi : 0 ≤ Real.pi * a / sigma :=
      div_nonneg (mul_nonneg Real.pi_pos.le hspec.1.1.le) hs.le
    rw [abs_of_nonpos (by linarith [hpi])]
    ring
  have : dMin - Real.pi * a / sigma ≤ |gamma' - omega| := by
    have htri : |gamma' - gamma| ≤ |gamma' - omega| + |omega - gamma| :=
      abs_sub_le gamma' omega gamma
    linarith [hgap, hdet, htri]
  have hεle : gaborIsolationEpsilon a ≤ dMin - Real.pi * a / sigma := by
    linarith [hrad]
  exact hεle.trans this

/-- Isolation-shrink packet. -/
noncomputable def isolationGaborTest (sigma gamma dMin : ℝ)
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) : GaborWeilTest :=
  let aw := isolationShrink sigma gamma dMin hs hg hd
  pureGaborTest aw.1 aw.2 (isolationShrink_a_pos hs hg hd)

theorem isolationGaborTest_coeffs (sigma gamma dMin : ℝ)
    (hs : 0 < sigma) (hg : 0 < gamma) (hd : 0 < dMin) :
    (isolationGaborTest sigma gamma dMin hs hg hd).coeffs = ⟨1, 0, 0⟩ :=
  rfl

/-! ## Host / increment bookkeeping (multiplicity-aware) -/

/-- Historical constant occupancy: at most `K_bin = 43` of multiplicity
in every unit ordinate bin.  Not a theorem about ζ-zeros. -/
def GaborConfigIncrementCompliant (Z : GaborCanonicalConfig) : Prop :=
  ∀ k : ℤ,
    (Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)).sum
      (fun q => (Z.mult q : ℝ)) ≤ gaborKBin

/-- Counting-theorem occupancy: unit bin `(k, k+1]` carries at most
`gaborKBinAt |k| = 2 C_inner (1+log(|k|+3))`, matching
`gaborBinCountMajorant` / `card_strip_window_le` / `zeta_unit_increment`. -/
def GaborConfigIncrementCompliantLog (Z : GaborCanonicalConfig) : Prop :=
  ∀ k : ℤ,
    (Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)).sum
      (fun q => (Z.mult q : ℝ)) ≤ gaborKBinAt (|k| : ℝ)

noncomputable def gaborHostSigma (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) : ℝ :=
  Z.pts.sup' hZ (fun q => q.1)

lemma gaborHostLayer_nonempty (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (Z.pts.filter (fun q => q.1 = gaborHostSigma Z hZ)).Nonempty := by
  obtain ⟨q, hq, hqeq⟩ := Finset.exists_mem_eq_sup' hZ (fun q => q.1)
  refine ⟨q, ?_⟩
  refine mem_filter.mpr ⟨hq, ?_⟩
  simpa [gaborHostSigma] using hqeq.symm

/-- Lexicographic host: max `σ`, then min `γ>0`. -/
noncomputable def gaborHostGamma (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) : ℝ :=
  (Z.pts.filter (fun q => q.1 = gaborHostSigma Z hZ)).inf'
    (gaborHostLayer_nonempty Z hZ) (fun q => q.2)

theorem gaborHost_mem (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty) :
    (gaborHostSigma Z hZ, gaborHostGamma Z hZ) ∈ Z.pts := by
  obtain ⟨q, hq, hqσ⟩ := Finset.exists_mem_eq_sup' hZ (fun q => q.1)
  have hqσ' : q.1 = gaborHostSigma Z hZ := by
    simpa [gaborHostSigma] using hqσ.symm
  have hlayer := gaborHostLayer_nonempty Z hZ
  obtain ⟨p, hp, hpγ⟩ :=
    Finset.exists_mem_eq_inf' hlayer (fun q => q.2)
  have hpσ : p.1 = gaborHostSigma Z hZ := (mem_filter.mp hp).2
  have hppts : p ∈ Z.pts := (mem_filter.mp hp).1
  have : p = (gaborHostSigma Z hZ, gaborHostGamma Z hZ) := by
    apply Prod.ext
    · exact hpσ
    · simpa [gaborHostGamma] using hpγ.symm
  rwa [← this]

noncomputable def gaborHostMult (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) : ℕ :=
  Z.mult (gaborHostSigma Z hZ, gaborHostGamma Z hZ)

theorem gaborHostSigma_pos (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    0 < gaborHostSigma Z hZ :=
  (Z.sigma_off _ (gaborHost_mem Z hZ)).1

theorem gaborHostSigma_lt_half (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    gaborHostSigma Z hZ < 1 / 2 :=
  (Z.sigma_off _ (gaborHost_mem Z hZ)).2

theorem gaborHostGamma_pos (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    0 < gaborHostGamma Z hZ :=
  Z.gamma_pos _ (gaborHost_mem Z hZ)

theorem gaborHostMult_pos (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    0 < gaborHostMult Z hZ :=
  Z.mult_pos _ (gaborHost_mem Z hZ)

/-- Weakest host-window hypothesis used by T_gap / peak emptiness:
the only catalog point on the host ordinate is the host itself.
Implied by `gammaDistinct`; not implied by increment compliance
(two off-line FE-orbits can share an ordinate and differ in σ).
Bin majorants already sum every point, so global injectivity of
`γ` is not needed for packing. -/
def GaborCanonicalConfig.gammaHostIsolated (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) : Prop :=
  ∀ q ∈ Z.pts, q.2 = gaborHostGamma Z hZ →
    q = (gaborHostSigma Z hZ, gaborHostGamma Z hZ)

theorem gammaDistinct_hostIsolated (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) (h : Z.gammaDistinct) :
    Z.gammaHostIsolated hZ :=
  fun q hq heq =>
    h q hq (gaborHostSigma Z hZ, gaborHostGamma Z hZ)
      (gaborHost_mem Z hZ) heq

/-- Minimal foreign-ordinate gap.  Empty foreign set is the `+∞`
case of the rule (handled by `isolationShrinkTop`).  The dummy `1`
is never fed to the shrink when the foreign set is empty. -/
noncomputable def gaborForeignDMin (Z : GaborCanonicalConfig)
    (gammaStar : ℝ) : ℝ :=
  if h : (Z.pts.filter (fun q => q.2 ≠ gammaStar)).Nonempty then
    (Z.pts.filter (fun q => q.2 ≠ gammaStar)).inf' h
      (fun q => |q.2 - gammaStar|)
  else 1

theorem gaborForeignDMin_pos (Z : GaborCanonicalConfig) (gammaStar : ℝ) :
    0 < gaborForeignDMin Z gammaStar := by
  unfold gaborForeignDMin
  split_ifs with h
  · have hnle :
        ¬ ((Z.pts.filter (fun q => q.2 ≠ gammaStar)).inf' h
            (fun q => |q.2 - gammaStar|) ≤ 0) := by
      rw [Finset.inf'_le_iff]
      rintro ⟨q, hq, hle⟩
      exact (not_le_of_gt
        (abs_pos.mpr (sub_ne_zero.mpr (mem_filter.mp hq).2))) hle
    exact lt_of_not_ge hnle
  · norm_num

/-- Uncapped isolation-shrink pair (largest / any admissible width). -/
noncomputable def isolationShrinkOfConfigRaw (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) : ℝ × ℝ :=
  let σ := gaborHostSigma Z hZ
  let γ := gaborHostGamma Z hZ
  if h : (Z.pts.filter (fun q => q.2 ≠ γ)).Nonempty then
    isolationShrink σ γ (gaborForeignDMin Z γ)
      (gaborHostSigma_pos Z hZ) (gaborHostGamma_pos Z hZ)
      (gaborForeignDMin_pos Z γ)
  else
    isolationShrinkTop σ γ (gaborHostSigma_pos Z hZ)
      (gaborHostGamma_pos Z hZ)

/-- Named constructive rule on a nonempty canonical catalog.
r569: the raw admissible width is capped at `gaborSmallnessA`
(every smaller positive width stays admissible and keeps ω>0). -/
noncomputable def isolationShrinkOfConfig (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) : ℝ × ℝ :=
  let σ := gaborHostSigma Z hZ
  let γ := gaborHostGamma Z hZ
  let a := min (isolationShrinkOfConfigRaw Z hZ).1 (gaborSmallnessA σ γ)
  (a, gaborIsolationOmega σ γ a)

theorem isolationShrinkOfConfigRaw_a_pos (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    0 < (isolationShrinkOfConfigRaw Z hZ).1 := by
  dsimp [isolationShrinkOfConfigRaw]
  split_ifs
  · apply isolationShrink_a_pos
  · apply isolationShrinkTop_a_pos

theorem isolationShrinkOfConfig_a_eq (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 =
      min (isolationShrinkOfConfigRaw Z hZ).1
        (gaborSmallnessA (gaborHostSigma Z hZ) (gaborHostGamma Z hZ)) :=
  rfl

theorem isolationShrinkOfConfig_omega_eq (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).2 =
      gaborIsolationOmega (gaborHostSigma Z hZ) (gaborHostGamma Z hZ)
        (isolationShrinkOfConfig Z hZ).1 :=
  rfl

theorem isolationShrinkOfConfig_a_pos (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    0 < (isolationShrinkOfConfig Z hZ).1 := by
  rw [isolationShrinkOfConfig_a_eq]
  exact lt_min (isolationShrinkOfConfigRaw_a_pos Z hZ)
    (gaborSmallnessA_pos (gaborHostSigma_pos Z hZ)
      (gaborHostGamma_pos Z hZ))

theorem isolationShrinkOfConfig_a_le_smallness (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    (isolationShrinkOfConfig Z hZ).1 ≤
      gaborSmallnessA (gaborHostSigma Z hZ) (gaborHostGamma Z hZ) := by
  rw [isolationShrinkOfConfig_a_eq]
  exact min_le_right _ _

theorem isolationShrinkOfConfig_omega_pos (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) :
    0 < (isolationShrinkOfConfig Z hZ).2 := by
  rw [isolationShrinkOfConfig_omega_eq]
  exact gaborIsolationOmega_pos (gaborHostSigma_pos Z hZ)
    (gaborHostGamma_pos Z hZ) (isolationShrinkOfConfig_a_pos Z hZ).le
    ((isolationShrinkOfConfig_a_le_smallness Z hZ).trans
      (gaborSmallnessA_le_omegaCap _ _))

noncomputable def isolationGaborTestOfConfig (Z : GaborCanonicalConfig)
    (hZ : Z.pts.Nonempty) : GaborWeilTest :=
  let aw := isolationShrinkOfConfig Z hZ
  pureGaborTest aw.1 aw.2 (isolationShrinkOfConfig_a_pos Z hZ)

/-! ## (4) Canonical dominance scaffold and honest bridges -/

/-- r569 canonical dominance (historical constant occupancy).
Every `K_bin = 43`-compliant catalog has `W_honest < 0`.
Discharged by `gabor_dominanceBound_holds`.  Special case of
`GaborDominanceBoundLog` once `Compliant → CompliantLog`. -/
def GaborDominanceBound : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    GaborConfigIncrementCompliant Z →
    Z.gammaDistinct →
    gaborHonestWeil (isolationShrinkOfConfig Z hZ).1
      (isolationShrinkOfConfig Z hZ).2 Z gaborCInc < 0

/-- r574 counting-compatible dominance: every catalog whose unit-bin
masses obey the Path-A increment `gaborKBinAt |k|` has `W_honest < 0`
for the isolation-shrink packet (smallness uses `K_binAt(γ★)`).
The constant on-line remainder `R_on = 2 C_inc S_cert` is a
historical proxy (r575).  The majorant-compatible remainder is
`gaborHonestOnlineBudgetLog` / `GaborDominanceBoundLog2`. -/
def GaborDominanceBoundLog : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    GaborConfigIncrementCompliantLog Z →
    Z.gammaDistinct →
    gaborHonestWeil (isolationShrinkOfConfig Z hZ).1
      (isolationShrinkOfConfig Z hZ).2 Z gaborCInc < 0

/-- Bridge (i), NOT an identity.

`W_honest = Σ_j m_j Q + R_on` is a finite quadrupole-plus-online
majorant.  `gaborArithmeticFormula` of the isolation packet is the
classical three-channel form `Arch − Prime_comb + Re ĥ_W(0)`.

L2-Adjudikation r589: RH-Kern.  The implication hides the full
off-line tail control (r549 mechanism `exp((σ′²−σ²)/2a)`); it is
not a finite identity. -/
def GaborHonestNegImpliesIsolationArithmeticNeg : Prop :=
  ∀ (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
    gaborHonestWeil (isolationShrinkOfConfig Z hZ).1
        (isolationShrinkOfConfig Z hZ).2 Z gaborCInc < 0 →
    gaborArithmeticFormula (isolationGaborTestOfConfig Z hZ) < 0

/-- Bridge (ii), NOT an identity.

The isolation packet uses `a ≤ min(a_lock, γσ/(2π))`.  The live
`GaborSeparationForAllZeros` target uses `scalingGaborTest` with
`a = σ²/64`.  The first conjunct identifies a canonical host
`(|β−1/2|, |γ|)` with the scaling test at the raw ordinate; the
second is the real-ordinate gap (`ω>0` isolation is undefined at
`γ = 0`).

L2-Adjudikation r589: kein Monotonie-Transfer.
Isolation `a ≤ σ²/512` does not yield Scaling `a = σ²/64`. -/
def GaborIsolationArithmeticImpliesScalingArithmetic : Prop :=
  (∀ (beta gamma : ℝ) (hcrit : beta ≠ 1 / 2)
      (Z : GaborCanonicalConfig) (hZ : Z.pts.Nonempty),
      gaborHostSigma Z hZ = |beta - 1 / 2| →
      gaborHostGamma Z hZ = |gamma| →
      gaborArithmeticFormula (isolationGaborTestOfConfig Z hZ) < 0 →
        gaborArithmeticFormula (scalingGaborTest beta gamma hcrit) < 0) ∧
    (∀ (beta : ℝ) (hcrit : beta ≠ 1 / 2),
      gaborArithmeticFormula (scalingGaborTest beta 0 hcrit) < 0)

noncomputable def gaborSingletonConfig (sigma gamma : ℝ)
    (hs0 : 0 < sigma) (hs1 : sigma < 1 / 2) (hg : 0 < gamma) :
    GaborCanonicalConfig where
  pts := {(sigma, gamma)}
  mult := fun _ => 1
  mult_pos := by
    intro q hq
    simp at hq
    norm_num
  sigma_off := by
    intro q hq
    have : q = (sigma, gamma) := by simpa using hq
    cases this
    exact ⟨hs0, hs1⟩
  gamma_pos := by
    intro q hq
    have : q = (sigma, gamma) := by simpa using hq
    cases this
    exact hg

lemma singleton_incrementCompliant (sigma gamma : ℝ)
    (hs0 : 0 < sigma) (hs1 : sigma < 1 / 2) (hg : 0 < gamma) :
    GaborConfigIncrementCompliant
      (gaborSingletonConfig sigma gamma hs0 hs1 hg) := by
  intro k
  set Z := gaborSingletonConfig sigma gamma hs0 hs1 hg
  have hle :
      (Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)).sum
        (fun q => (Z.mult q : ℝ)) ≤ 1 := by
    have hsub :=
      (Finset.sum_le_sum_of_subset_of_nonneg
        (s := Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1))
        (t := Z.pts) (f := fun q => (Z.mult q : ℝ))
        (Finset.filter_subset _ Z.pts)
        (fun _ _ _ => Nat.cast_nonneg _))
    simpa [Z, gaborSingletonConfig] using hsub
  exact hle.trans (by norm_num [gaborKBin] : (1 : ℝ) ≤ (gaborKBin : ℝ))

lemma singleton_incrementCompliantLog (sigma gamma : ℝ)
    (hs0 : 0 < sigma) (hs1 : sigma < 1 / 2) (hg : 0 < gamma) :
    GaborConfigIncrementCompliantLog
      (gaborSingletonConfig sigma gamma hs0 hs1 hg) := by
  intro k
  set Z := gaborSingletonConfig sigma gamma hs0 hs1 hg
  have hle :
      (Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1)).sum
        (fun q => (Z.mult q : ℝ)) ≤ 1 := by
    have hsub :=
      (Finset.sum_le_sum_of_subset_of_nonneg
        (s := Z.pts.filter (fun q => (k : ℝ) < q.2 ∧ q.2 ≤ (k : ℝ) + 1))
        (t := Z.pts) (f := fun q => (Z.mult q : ℝ))
        (Finset.filter_subset _ Z.pts)
        (fun _ _ _ => Nat.cast_nonneg _))
    simpa [Z, gaborSingletonConfig] using hsub
  have hK : (1 : ℝ) ≤ gaborKBinAt (|k| : ℝ) := by
    have h43 : (gaborKBin : ℝ) ≤ gaborKBinAt (|k| : ℝ) :=
      gaborKBinAt_ge_gaborKBin (abs_nonneg _)
    exact (by norm_num [gaborKBin] : (1 : ℝ) ≤ (gaborKBin : ℝ)).trans h43
  exact hle.trans hK

lemma singleton_gammaDistinct (sigma gamma : ℝ)
    (hs0 : 0 < sigma) (hs1 : sigma < 1 / 2) (hg : 0 < gamma) :
    (gaborSingletonConfig sigma gamma hs0 hs1 hg).gammaDistinct := by
  intro q₁ hq₁ q₂ hq₂ _
  have h1 : q₁ = (sigma, gamma) := by
    simpa [gaborSingletonConfig] using hq₁
  have h2 : q₂ = (sigma, gamma) := by
    simpa [gaborSingletonConfig] using hq₂
  rw [h1, h2]

lemma singleton_gammaHostIsolated (sigma gamma : ℝ)
    (hs0 : 0 < sigma) (hs1 : sigma < 1 / 2) (hg : 0 < gamma) :
    (gaborSingletonConfig sigma gamma hs0 hs1 hg).gammaHostIsolated
      (by simp [gaborSingletonConfig]) :=
  gammaDistinct_hostIsolated _
    (by simp [gaborSingletonConfig])
    (singleton_gammaDistinct sigma gamma hs0 hs1 hg)

lemma singleton_hostSigma (sigma gamma : ℝ)
    (hs0 : 0 < sigma) (hs1 : sigma < 1 / 2) (hg : 0 < gamma) :
    gaborHostSigma (gaborSingletonConfig sigma gamma hs0 hs1 hg)
      (by simp [gaborSingletonConfig]) = sigma := by
  simp [gaborHostSigma, gaborSingletonConfig]

lemma singleton_hostGamma (sigma gamma : ℝ)
    (hs0 : 0 < sigma) (hs1 : sigma < 1 / 2) (hg : 0 < gamma) :
    gaborHostGamma (gaborSingletonConfig sigma gamma hs0 hs1 hg)
      (by simp [gaborSingletonConfig]) = gamma := by
  unfold gaborHostGamma
  have hσ := singleton_hostSigma sigma gamma hs0 hs1 hg
  apply le_antisymm
  · have hmem : (sigma, gamma) ∈
        (gaborSingletonConfig sigma gamma hs0 hs1 hg).pts.filter
          (fun q => q.1 =
            gaborHostSigma (gaborSingletonConfig sigma gamma hs0 hs1 hg)
              (by simp [gaborSingletonConfig])) := by
      refine mem_filter.mpr ⟨by simp [gaborSingletonConfig], ?_⟩
      simp [hσ]
    have hle := Finset.inf'_le (fun q => q.2) hmem
    convert hle using 2
  · rw [Finset.le_inf'_iff]
    intro q hq
    have : q = (sigma, gamma) := by
      simpa [gaborSingletonConfig] using (mem_filter.mp hq).1
    simp [this]

lemma nontrivialZero_re_mem_Ioo_of_im_ne {s : ℂ}
    (hs : IsNontrivialRiemannZetaZero s) (him : s.im ≠ 0) :
    s.re ∈ Set.Ioo (0 : ℝ) 1 := by
  constructor
  · by_contra h
    have hre : s.re ≤ 0 := le_of_not_gt h
    rcases lt_or_eq_of_le hre with hlt | heq
    · exact him (riemannZeta_eq_zero_im_eq_zero_of_re_lt_zero hlt hs.1)
    · exact (riemannZeta_ne_zero_of_re_eq_zero heq) hs.1
  · by_contra h
    exact riemannZeta_ne_zero_of_one_le_re (le_of_not_gt h) hs.1

lemma abs_re_sub_half_lt_half {s : ℂ}
    (hs : IsNontrivialRiemannZetaZero s) (him : s.im ≠ 0) :
    |s.re - 1 / 2| < 1 / 2 := by
  have h := nontrivialZero_re_mem_Ioo_of_im_ne hs him
  rw [abs_sub_lt_iff]
  constructor <;> linarith [h.1, h.2]

/-- Sorry-free logical wrapper: dominance plus the two named
translation bridges imply the live `∀`-zeros arithmetic inequality.
The bridges are hypotheses because `W_honest` is not
`gaborArithmeticFormula` and the isolation packet is not
`scalingGaborTest`. -/
theorem gabor_dominance_implies_separation
    (hdom : GaborDominanceBound)
    (hhonest : GaborHonestNegImpliesIsolationArithmeticNeg)
    (hscale : GaborIsolationArithmeticImpliesScalingArithmetic) :
    GaborSeparationForAllZeros := by
  intro s hsz hcrit
  set sigma : ℝ := |s.re - 1 / 2|
  have hs : 0 < sigma := abs_pos.mpr (sub_ne_zero.mpr hcrit)
  by_cases him : s.im = 0
  · simpa [him] using hscale.2 s.re hcrit
  · have hs1 : sigma < 1 / 2 := abs_re_sub_half_lt_half hsz him
    have hg : 0 < |s.im| := abs_pos.mpr him
    let Z := gaborSingletonConfig sigma |s.im| hs hs1 hg
    have hZ : Z.pts.Nonempty := by
      simp [Z, gaborSingletonConfig]
    have hW :=
      hdom Z hZ (singleton_incrementCompliant sigma |s.im| hs hs1 hg)
        (singleton_gammaDistinct sigma |s.im| hs hs1 hg)
    have harith := hhonest Z hZ hW
    refine hscale.1 s.re s.im hcrit Z hZ ?_ ?_ harith
    · convert singleton_hostSigma sigma |s.im| hs hs1 hg
    · convert singleton_hostGamma sigma |s.im| hs hs1 hg

/-- Constant occupancy is stronger than the counting-theorem cap:
`K_bin = 43 ≤ gaborKBinAt |k|` for every bin. -/
theorem incrementCompliant_implies_log
    {Z : GaborCanonicalConfig} (h : GaborConfigIncrementCompliant Z) :
    GaborConfigIncrementCompliantLog Z := by
  intro k
  exact (h k).trans (gaborKBinAt_ge_gaborKBin (abs_nonneg _))

theorem gabor_dominanceLog_implies_separation
    (hdom : GaborDominanceBoundLog)
    (hhonest : GaborHonestNegImpliesIsolationArithmeticNeg)
    (hscale : GaborIsolationArithmeticImpliesScalingArithmetic) :
    GaborSeparationForAllZeros := by
  intro s hsz hcrit
  set sigma : ℝ := |s.re - 1 / 2|
  have hs : 0 < sigma := abs_pos.mpr (sub_ne_zero.mpr hcrit)
  by_cases him : s.im = 0
  · simpa [him] using hscale.2 s.re hcrit
  · have hs1 : sigma < 1 / 2 := abs_re_sub_half_lt_half hsz him
    have hg : 0 < |s.im| := abs_pos.mpr him
    let Z := gaborSingletonConfig sigma |s.im| hs hs1 hg
    have hZ : Z.pts.Nonempty := by
      simp [Z, gaborSingletonConfig]
    have hW :=
      hdom Z hZ (singleton_incrementCompliantLog sigma |s.im| hs hs1 hg)
        (singleton_gammaDistinct sigma |s.im| hs hs1 hg)
    have harith := hhonest Z hZ hW
    refine hscale.1 s.re s.im hcrit Z hZ ?_ ?_ harith
    · convert singleton_hostSigma sigma |s.im| hs hs1 hg
    · convert singleton_hostGamma sigma |s.im| hs hs1 hg

#print axioms gaussBinMax_of_outside
#print axioms truncated_theta_binMax_sum_le
#print axioms truncated_theta_tsum_le
#print axioms re_ofReal_mul_cexp_I
#print axioms re_pureGaborHatDelta
#print axioms gaborQuadrupole_eq_four_re_hat
#print axioms gaborQuadrupole_eq_four_re_integral
#print axioms gaborQuadrupole_even_gamma
#print axioms gabor_phase_coherent_cos
#print axioms gaborPlusAmp_le_exp_neg_omega_sq
#print axioms gaborPlusLobe_majorant
#print axioms gaborHostMerge_minusLobe
#print axioms exists_isolationShrink
#print axioms exists_isolationShrink_omega
#print axioms exists_greatest_isolationShrink
#print axioms isolationShrink_spec
#print axioms isolationShrink_exceptionWindow_empty
#print axioms gaborForeignDMin_pos
#print axioms gammaDistinct_hostIsolated
#print axioms gabor_dominance_implies_separation
#print axioms gaborKBinAt_pos
#print axioms gaborKBinAt_ge_gaborKBin
#print axioms incrementCompliant_implies_log
#print axioms singleton_incrementCompliantLog
#print axioms singleton_gammaHostIsolated
#print axioms gabor_dominanceLog_implies_separation

end RH
