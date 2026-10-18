/-
  WallCertifiedHead — the kernel-certified finite head of the
  prime-front wall ladder (v897), composed into cofinal Weil.
  =================================================================

  Numeric counterpart: verification/v897_certified_interval_ladder.py
  (PRIME.PORT.BALLLADDER.01) — sigma_h > 0 on all 42 reachable rungs
  h = 142..878 of the deployed v563 window ladder, via rigorous
  mpmath.iv interval shifts (15 exact-rational Bareiss certificates at
  h ≤ 300, 27 validated-precision Cholesky certificates at h > 300).

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`, no axioms):

    (1) `certified_head` — POSITIVE DEFINITENESS of the exported
        integer certificate matrices `M = N − shift·1` for the FIRST
        18 RUNGS of the census, ascending h: ALL 15 tier-1 rungs
        (h = 142..291) plus the 3 shallowest tier-2 rungs
        (h = 313, 344, 363) — the same representative-subset economy
        the v897 suite runs.  Each rung is a kernel `decide` on the
        exported exact data (dyadic lag midpoints, rigorous interval
        shift, integer Cholesky witness); the 15 tier-1 entries are
        thereby re-proven INSIDE Lean, and the 3 tier-2 entries are
        proven at a strength (exact integer arithmetic) EXCEEDING
        their Python validated-precision label.

    (2) `wall_certified_head_cofinal_weil` — the composition: these
        18 kernel certificates + the two NAMED hypotheses
        (`HeadEnclosure`: the v897 interval-enclosure identification;
        `TailPositivity`: the 24 deeper reachable rungs h = 364..878
        not kernel-checked here AND the asymptotic tail h → ∞) +
        per-element form convergence  ⇒  the full conclusion of
        `CofinalWeil.cofinal_weil` — the limit functional is
        nonnegative on the dense family.

  THE HONEST BOUNDARY, spelled out:

    * kernel-checked (this file + WallLadder/RungKz*.lean):
      PD of the 18 exported integer matrices — the finite-head
      linear algebra, closed in Lean;
    * NAMED, external (v897 Python interval arithmetic):
      `HeadEnclosure` — that the true analytic wall matrices dominate
      Q⁻¹ times these integer matrices (E1–E4 error accounting);
    * NAMED, open mathematics: `TailPositivity` — the 24 deeper
      reachable rungs (kernel cost grows as h³; they remain certified
      only on the Python side, v897) and the infinite tail, which no
      finite table settles (ExcessSkeleton.pointwise_pos_not_uniform).

  NO RH claim; no marker moves.  The asymptotic tail stays with the
  registered port contracts.
-/
import TfptCarrier.WallCofinalComposition
import TfptCarrier.WallLadder.RungKz18
import TfptCarrier.WallLadder.RungKz23
import TfptCarrier.WallLadder.RungKz12
import TfptCarrier.WallLadder.RungKz13
import TfptCarrier.WallLadder.RungKz20
import TfptCarrier.WallLadder.RungKz9
import TfptCarrier.WallLadder.RungKz14
import TfptCarrier.WallLadder.RungKz22
import TfptCarrier.WallLadder.RungKz15
import TfptCarrier.WallLadder.RungKz33
import TfptCarrier.WallLadder.RungKz29
import TfptCarrier.WallLadder.RungKz32
import TfptCarrier.WallLadder.RungKz39
import TfptCarrier.WallLadder.RungKz46
import TfptCarrier.WallLadder.RungKz27
import TfptCarrier.WallLadder.RungKz19
import TfptCarrier.WallLadder.RungKz25
import TfptCarrier.WallLadder.RungKz59

namespace TfptCarrier
namespace WallLadder

open Matrix Filter Topology CofinalWeil

/-- The FULL 42-rung census of v897 (kz, h), ascending h — frozen
constants from the recorded 2026-08-09 run (BALLLADDER-COMPLETE). -/
def census : List (ℕ × ℕ) :=
  [(18, 142), (23, 149), (12, 151), (13, 168), (20, 170), (9, 184),
   (14, 185), (22, 199), (15, 203), (33, 210), (29, 218), (32, 254),
   (39, 277), (46, 285), (27, 291), (19, 313), (25, 344), (59, 363),
   (26, 364), (21, 371), (55, 388), (60, 388), (16, 434), (44, 436),
   (34, 454), (36, 488), (78, 488), (24, 490), (48, 516), (38, 522),
   (82, 534), (49, 540), (40, 591), (53, 606), (28, 615), (67, 679),
   (30, 700), (31, 722), (43, 839), (50, 841), (64, 859), (52, 878)]

/-- The kernel-checked head data: the first 18 census rungs
(all 15 tier-1 + the 3 shallowest tier-2), ascending h. -/
def checkedData : List RungData :=
  [rungKz18, rungKz23, rungKz12, rungKz13, rungKz20, rungKz9,
   rungKz14, rungKz22, rungKz15, rungKz33, rungKz29, rungKz32,
   rungKz39, rungKz46, rungKz27, rungKz19, rungKz25, rungKz59]

/-- The checked head is exactly the first 18 census rungs (kernel
`decide` on the frozen (kz, h) pairs — a self-consistency ward). -/
theorem checked_is_census_prefix :
    checkedData.map (fun d => (d.kz, d.h)) = census.take 18 := by decide

theorem checkedData_length : checkedData.length = 18 := rfl

theorem census_length : census.length = 42 := by decide

/-- **THE CERTIFIED FINITE HEAD** — every exported certificate matrix
of the checked head is positive definite (18 kernel `decide` runs on
exact integer data; per-rung theorems in WallLadder/RungKz*.lean). -/
theorem certified_head : ∀ d ∈ checkedData, (MmatR d).PosDef := by
  intro d hd
  simp only [checkedData, List.mem_cons, List.not_mem_nil,
    or_false] at hd
  rcases hd with rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl |
    rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl | rfl
  exacts [rungKz18_posDef, rungKz23_posDef, rungKz12_posDef,
    rungKz13_posDef, rungKz20_posDef, rungKz9_posDef, rungKz14_posDef,
    rungKz22_posDef, rungKz15_posDef, rungKz33_posDef, rungKz29_posDef,
    rungKz32_posDef, rungKz39_posDef, rungKz46_posDef, rungKz27_posDef,
    rungKz19_posDef, rungKz25_posDef, rungKz59_posDef]

/-- The PSD form consumed by the composition. -/
theorem certified_head_psd : ∀ d ∈ checkedData, (MmatR d).PosSemidef :=
  fun d hd => (certified_head d hd).posSemidef

section Ladder

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)]

/-- **THE COMPOSED FINITE-HEAD THEOREM** — the certified 18-rung head
plugged into the cofinal Weil implication.  Hypotheses, exhaustively:

  * `idx`, `hmono` — an explicit strictly monotone ladder; binder
    order does not prove its computational provenance;
  * `hbridge` — NAMED: the v897 E1–E4 interval-enclosure
    identification for the 18 checked rungs (external, Python side);
  * `htail` — NAMED: positivity of every rung beyond position 18 —
    the 24 deeper reachable rungs (h = 364..878, certified only on
    the Python side) AND the asymptotic tail h → ∞ (open);
  * `hconv` — per-element form convergence (Piece 2 of the
    extraction chain).

Everything else — the 18 per-rung positivity facts and the whole
composition logic — is kernel-checked.  PREDEFINED/noninterference is
the separate external contract of `CofinalPredefinition`.  NO RH
claim. -/
theorem wall_certified_head_cofinal_weil {V : Type*}
    (A : ∀ m, Matrix (κ m) (κ m) ℝ) (idx : ℕ → ℕ)
    (hmono : StrictMono idx)
    (hbridge : HeadEnclosure A idx checkedData)
    (htail : TailPositivity A idx checkedData.length)
    (sample : ∀ m, V → κ m → ℝ) (QW : V → ℝ)
    (hconv : ∀ v, Tendsto (fun m => ladderForm A sample m v)
      atTop (𝓝 (QW v))) :
    (∀ j v, 0 ≤ ladderForm A sample (idx j) v) ∧
    (∀ v, Tendsto (fun j => ladderForm A sample (idx j) v)
      atTop (𝓝 (QW v))) ∧
    (∀ v, 0 ≤ QW v) :=
  wall_cofinal_weil A idx hmono checkedData certified_head_psd
    hbridge htail sample QW hconv

end Ladder

end WallLadder
end TfptCarrier
