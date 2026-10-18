/-
  SectorPositiveDescent — positive descent with a corner, and the
  honest boundary of the sector floor.
  ================================================================

  The common formal core of the two hardest TFPT fronts (2026-08-07
  strategy table): the G_net continuum limit and the prime-front
  character corner (PRIME.FLOOR.PAIRCORR.01).  Numeric counterparts:
  `experiments/tfpt-discovery/hjelmslev_level2_corner_probe.py`,
  `character_corner_probe.py`, `hjelmslev_position_kraus_probe.py`,
  `paircorr_bridge_map_probe.py`.

  WHAT THIS MODULE PROVES (kernel-checked, no `sorry`, no
  `native_decide`).  The structural half of positive descent with a
  corner, at the finite matrix level (house precedent:
  GramCompactness, PositiveDescentMaster):

    (1) `IsOrthogonalProjection` / `corner` — corner compression
        a ↦ e·a·e by a hermitian idempotent e.  `corner_add`,
        `corner_smul`, `corner_one`, `corner_corner` — the map is
        linear, sends 1 to e and is idempotent (the CP structural
        skeleton, without the Choi apparatus).

    (2) `corner_posSemidef` — compression is completely positive at
        the level that matters here: e·a·e ⪰ 0 for a ⪰ 0
        (congruence, `PosSemidef.conjTranspose_mul_mul_same` with
        eᴴ = e).  `corner_trace_nonneg` / `corner_trace_le` —
        corners of states are states up to normalization:
        0 ≤ tr(e·ρ·e) ≤ tr ρ (the complement 1 − e is again an
        orthogonal projection, `compl_isOrthogonalProjection`, and
        the two corner traces split tr ρ).

    (3) `corner_limit_posSemidef` — limits preserve positivity:
        entrywise limits of corner values of PSD states are PSD.
        This SPECIALIZES `GramCompactness.posSemidef_of_tendsto`
        (imported, not re-proved).

    (4) `DescentTower` / `cornerFamily_compatible` /
        `cornerFamily_positive` — compatible corners under descent:
        for a tower of matrix algebras with unital positive maps
        φ_m and projections e_m satisfying the Hjelmslev-tower
        compatibility φ_m(e_{m+1}·a·e_{m+1}) = e_m·φ_m(a)·e_m (the
        identity whose defect the level-2 corner probe measured as
        identically zero), the corner values of a compatible
        positive family form again a compatible positive family;
        `tower_proj_descent` — the projections themselves descend,
        φ_m(e_{m+1}) = e_m.

    (5) `sector_floor` — the assembly: tower + compatible positive
        families + entrywise convergence of the base corner values
        give a PSD limit corner G with every quadratic-form
        direction nonnegative — PLUS the one named hypothesis
        `identification_positivity` (see below) passed through
        untouched.

  THE HONEST BOUNDARY (the kill criterion — the point of this
  module).  The corner probes proved that structural positivity is
  comb-blind: compression, descent and limits force xᵀGx ≥ 0 for
  every direction x, but they CANNOT see the arithmetic of the
  IDENTIFIED element — the pair-correlation functional whose
  nonnegativity at the limit corner IS the open content of
  PRIME.FLOOR.PAIRCORR.01.  Accordingly `IdentificationPositivity`
  enters `sector_floor` as a NAMED HYPOTHESIS, not a theorem.  The
  final theorem makes the logical geography kernel-checked:

      structural pieces (1)–(4), proven
    + identification_positivity, HYPOTHESIS
    ⇒ the sector floor statement.

  No continuum theorem, no RH statement, no arithmetic
  identification is formalized or claimed here.
-/
import TfptCarrier.GramCompactness

namespace TfptCarrier
namespace SectorPositiveDescent

open Filter Topology Matrix

/-! ### (1) Projections and corner compression -/

section Corner

variable {ι : Type*} [Fintype ι]

/-- An orthogonal projection in a real matrix algebra: a hermitian
idempotent e (e·e = e, eᴴ = e; over ℝ, `ᴴ` is the transpose). -/
structure IsOrthogonalProjection (e : Matrix ι ι ℝ) : Prop where
  idem : e * e = e
  herm : e.IsHermitian

/-- Corner compression by e: a ↦ e·a·e. -/
def corner (e a : Matrix ι ι ℝ) : Matrix ι ι ℝ :=
  e * a * e

/-- Compression is additive. -/
theorem corner_add (e a b : Matrix ι ι ℝ) :
    corner e (a + b) = corner e a + corner e b := by
  simp [corner, Matrix.mul_add, Matrix.add_mul]

/-- Compression is homogeneous (with `corner_add`: linear). -/
theorem corner_smul (e : Matrix ι ι ℝ) (c : ℝ) (a : Matrix ι ι ℝ) :
    corner e (c • a) = c • corner e a := by
  simp [corner, Matrix.mul_smul, Matrix.smul_mul]

/-- Compression sends the unit to the projection: e·1·e = e. -/
theorem corner_one [DecidableEq ι] {e : Matrix ι ι ℝ}
    (he : IsOrthogonalProjection e) : corner e 1 = e := by
  simp [corner, he.idem]

/-- Compression is idempotent: compressing a corner changes nothing. -/
theorem corner_corner {e : Matrix ι ι ℝ} (he : IsOrthogonalProjection e)
    (a : Matrix ι ι ℝ) : corner e (corner e a) = corner e a := by
  simp only [corner, ← mul_assoc]
  rw [he.idem, mul_assoc (e * a), he.idem]

/-! ### (2) Compression is positive; corners of states are states
up to normalization -/

/-- **Corner compression preserves PSD** (the CP inequality at the
matrix level): e·a·e ⪰ 0 for a ⪰ 0 — congruence by e with eᴴ = e. -/
theorem corner_posSemidef {e a : Matrix ι ι ℝ}
    (he : IsOrthogonalProjection e) (ha : a.PosSemidef) :
    (corner e a).PosSemidef := by
  have h := ha.conjTranspose_mul_mul_same e
  rw [he.herm.eq] at h
  exact h

/-- Corner states have nonnegative normalization: 0 ≤ tr(e·ρ·e). -/
theorem corner_trace_nonneg {e a : Matrix ι ι ℝ}
    (he : IsOrthogonalProjection e) (ha : a.PosSemidef) :
    0 ≤ (corner e a).trace :=
  (corner_posSemidef he ha).trace_nonneg

/-- The corner trace collapses to tr(e·a) (cyclicity + e·e = e). -/
theorem corner_trace_eq {e : Matrix ι ι ℝ}
    (he : IsOrthogonalProjection e) (a : Matrix ι ι ℝ) :
    (corner e a).trace = (e * a).trace := by
  simp only [corner]
  rw [Matrix.trace_mul_cycle, he.idem]

/-- The complement 1 − e of an orthogonal projection is again an
orthogonal projection. -/
theorem compl_isOrthogonalProjection [DecidableEq ι] {e : Matrix ι ι ℝ}
    (he : IsOrthogonalProjection e) : IsOrthogonalProjection (1 - e) := by
  constructor
  · have h : (1 - e) * (1 - e) = 1 - e - e + e * e := by noncomm_ring
    rw [h, he.idem]
    abel
  · exact Matrix.isHermitian_one.sub he.herm

/-- **Corners of states are states up to normalization**: the corner
trace never exceeds the state trace — the complementary corner
carries the (nonnegative) rest: tr(e·ρ·e) + tr((1−e)·ρ·(1−e)) = tr ρ. -/
theorem corner_trace_le [DecidableEq ι] {e a : Matrix ι ι ℝ}
    (he : IsOrthogonalProjection e) (ha : a.PosSemidef) :
    (corner e a).trace ≤ a.trace := by
  have hsum : (corner e a).trace + (corner (1 - e) a).trace = a.trace := by
    rw [corner_trace_eq he, corner_trace_eq (compl_isOrthogonalProjection he),
      ← Matrix.trace_add, ← Matrix.add_mul]
    norm_num
  have hrest := corner_trace_nonneg (compl_isOrthogonalProjection he) ha
  linarith

/-! ### (3) Limits preserve positivity (GramCompactness, specialized) -/

/-- **Limits of corner states are PSD**: if the corner values
e·ρ_n·e of PSD states converge entrywise, the limit is PSD.
Specialization of `GramCompactness.posSemidef_of_tendsto` (imported,
not re-proved) through `corner_posSemidef`. -/
theorem corner_limit_posSemidef {e : Matrix ι ι ℝ}
    (he : IsOrthogonalProjection e) (ρ : ℕ → Matrix ι ι ℝ)
    (hρ : ∀ n, (ρ n).PosSemidef) (G : Matrix ι ι ℝ)
    (hlim : ∀ i j,
      Tendsto (fun n => corner e (ρ n) i j) atTop (𝓝 (G i j))) :
    G.PosSemidef :=
  GramCompactness.posSemidef_of_tendsto (fun n => corner e (ρ n)) G
    (fun n => corner_posSemidef he (hρ n)) hlim

end Corner

/-! ### (4) Compatible corners under descent (the Hjelmslev tower) -/

section Tower

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)] [∀ m, DecidableEq (κ m)]

/-- A descent tower of matrix algebras: transition maps φ_m from
level m+1 to level m that are positive (PSD → PSD) and unital, and
orthogonal projections e_m satisfying the corner compatibility
φ_m(e_{m+1}·a·e_{m+1}) = e_m·φ_m(a)·e_m — the identity whose defect
the Hjelmslev level-2 corner probe measured as identically zero. -/
structure DescentTower (κ : ℕ → Type*) [∀ m, Fintype (κ m)]
    [∀ m, DecidableEq (κ m)] where
  /-- The transition map from level m+1 down to level m. -/
  φ : ∀ m, Matrix (κ (m + 1)) (κ (m + 1)) ℝ → Matrix (κ m) (κ m) ℝ
  /-- The corner projection at each level. -/
  e : ∀ m, Matrix (κ m) (κ m) ℝ
  /-- Each e_m is an orthogonal projection. -/
  proj : ∀ m, IsOrthogonalProjection (e m)
  /-- Each transition is positive: PSD is preserved. -/
  pos : ∀ m a, a.PosSemidef → (φ m a).PosSemidef
  /-- Each transition is unital. -/
  unital : ∀ m, φ m 1 = 1
  /-- The corner compatibility (Hjelmslev tower, defect = 0). -/
  compat : ∀ m a, φ m (corner (e (m + 1)) a) = corner (e m) (φ m a)

/-- A family of matrices, one per level, compatible under descent. -/
def IsCompatibleFamily (T : DescentTower κ)
    (ρ : ∀ m, Matrix (κ m) (κ m) ℝ) : Prop :=
  ∀ m, T.φ m (ρ (m + 1)) = ρ m

/-- A family of matrices, one per level, all PSD. -/
def IsPositiveFamily (ρ : ∀ m, Matrix (κ m) (κ m) ℝ) : Prop :=
  ∀ m, (ρ m).PosSemidef

/-- The corner values of a family along the tower projections. -/
def cornerFamily (T : DescentTower κ)
    (ρ : ∀ m, Matrix (κ m) (κ m) ℝ) : ∀ m, Matrix (κ m) (κ m) ℝ :=
  fun m => corner (T.e m) (ρ m)

/-- The projections themselves descend: φ_m(e_{m+1}) = e_m —
compatibility at a = 1, unitality, and e·1·e = e. -/
theorem tower_proj_descent (T : DescentTower κ) (m : ℕ) :
    T.φ m (T.e (m + 1)) = T.e m := by
  have h := T.compat m 1
  rwa [corner_one (T.proj (m + 1)), T.unital m, corner_one (T.proj m)] at h

/-- **Corner values of a compatible family are compatible**: the
corner compatibility transports descent through the compression. -/
theorem cornerFamily_compatible (T : DescentTower κ)
    {ρ : ∀ m, Matrix (κ m) (κ m) ℝ} (h : IsCompatibleFamily T ρ) :
    IsCompatibleFamily T (cornerFamily T ρ) := by
  intro m
  show T.φ m (corner (T.e (m + 1)) (ρ (m + 1))) = corner (T.e m) (ρ m)
  rw [T.compat m, h m]

/-- **Corner values of a positive family are positive**: compression
preserves PSD level by level. -/
theorem cornerFamily_positive (T : DescentTower κ)
    {ρ : ∀ m, Matrix (κ m) (κ m) ℝ} (h : IsPositiveFamily ρ) :
    IsPositiveFamily (cornerFamily T ρ) :=
  fun m => corner_posSemidef (T.proj m) (h m)

/-- Descent preserves positive families rung by rung (field `pos`
consumed once, so the hypothesis is load-bearing, not decorative). -/
theorem descend_positive (T : DescentTower κ)
    {ρ : ∀ m, Matrix (κ m) (κ m) ℝ} (h : IsPositiveFamily ρ) (m : ℕ) :
    (T.φ m (ρ (m + 1))).PosSemidef :=
  T.pos m (ρ (m + 1)) (h (m + 1))

end Tower

/-! ### (5) The honest boundary and the sector floor -/

section Floor

variable {ι : Type*} [Fintype ι]

/-- **THE HONEST BOUNDARY** (the kill criterion of this module).
`IdentificationPositivity identified G` says: the given functional —
the IDENTIFIED element, i.e. the pair-correlation floor functional
of PRIME.FLOOR.PAIRCORR.01 — is nonnegative at the limit corner G.

This is a NAMED HYPOTHESIS, deliberately NOT a theorem.  The corner
probes (`hjelmslev_level2_corner_probe.py`,
`character_corner_probe.py`, `paircorr_bridge_map_probe.py`) proved
that structural positivity is comb-blind: compression, descent and
limits force xᵀGx ≥ 0 in every direction, but the value of the
identified functional is NOT of that quadratic form — its
nonnegativity is exactly the open arithmetic content.  Any future
closure of the prime front must discharge THIS hypothesis; nothing
in this module (or in any structural extension of it) can. -/
def IdentificationPositivity (identified : Matrix ι ι ℝ → ℝ)
    (G : Matrix ι ι ℝ) : Prop :=
  0 ≤ identified G

variable {κ : ℕ → Type*} [∀ m, Fintype (κ m)] [∀ m, DecidableEq (κ m)]

/-- **THE SECTOR FLOOR** — the module's final theorem, with the
logical geography kernel-checked.  Given a descent tower, a sequence
of compatible positive families, and entrywise convergence of the
base-level corner values to G, then:

  * PROVEN (structural): every corner family is again compatible
    and positive; the limit corner G is PSD; every quadratic-form
    direction of G is nonnegative;
  * HYPOTHESIS (named, not proven): `identification_positivity` —
    the identified functional is nonnegative at G.  It is passed
    through untouched; it is the single non-structural input.

Structural pieces + the one named hypothesis ⇒ the floor statement. -/
theorem sector_floor (T : DescentTower κ)
    (ρ : ℕ → ∀ m, Matrix (κ m) (κ m) ℝ)
    (hcompat : ∀ n, IsCompatibleFamily T (ρ n))
    (hpos : ∀ n, IsPositiveFamily (ρ n))
    (G : Matrix (κ 0) (κ 0) ℝ)
    (hlim : ∀ i j,
      Tendsto (fun n => corner (T.e 0) (ρ n 0) i j) atTop (𝓝 (G i j)))
    (identified : Matrix (κ 0) (κ 0) ℝ → ℝ)
    (identification_positivity : IdentificationPositivity identified G) :
    (∀ n, IsCompatibleFamily T (cornerFamily T (ρ n))) ∧
    (∀ n, IsPositiveFamily (cornerFamily T (ρ n))) ∧
    G.PosSemidef ∧ (∀ x, 0 ≤ x ⬝ᵥ (G *ᵥ x)) ∧ 0 ≤ identified G := by
  have hG : G.PosSemidef :=
    corner_limit_posSemidef (T.proj 0) (fun n => ρ n 0)
      (fun n => hpos n 0) G hlim
  refine ⟨fun n => cornerFamily_compatible T (hcompat n),
    fun n => cornerFamily_positive T (hpos n), hG, fun x => ?_,
    identification_positivity⟩
  have h := hG.dotProduct_mulVec_nonneg x
  rwa [star_trivial] at h

end Floor

end SectorPositiveDescent
end TfptCarrier
