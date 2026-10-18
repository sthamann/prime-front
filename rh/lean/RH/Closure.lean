/-
RH/Closure.lean -- THE RECONSTRUCTION THEOREM (wave 10 / r305, reviewer
plan section 3): the master positivity is finite algebra over the two
true holes.

WHAT THIS FILE PROVES.  The r273 master theorem
`augmented_prefix_positive` (formerly the single open `sorry` of
RH/Window.lean) is NOT an independent arithmetic axiom: it is a finite
matrix-algebra corollary of exactly two window statements,

  * `LStar w`            -- the wave-6 canonical form (r283/v963): the
                            archimedean channel is strictly
                            mu-subordinate on the free polynomial
                            window (open as `lstar_subordination`,
                            RH/Window.lean),
  * `TerminalPositive w` -- the r258/r260 terminal statement: positive
                            budget normalization and the terminal
                            cross-ratio inequality `q_N < 1` (open as
                            `terminal_positive_main` below; its
                            pair-coordinate refinement is
                            `pair_margin_main`, RH/PairBound.lean).

The reconstruction chain (`lstar_terminal_implies_master`, PROVED):
  1. L* makes every Hankel block through the half-filling cap positive
     definite (`lstar_implies_hankel_posDef`, RH/Window.lean, wave 6).
  2. TerminalPositive gives the terminal Schur margin
     `D_cap = B(1 - q) > 0` (`terminal_margin_pos_of_terminal` below;
     pure ordered-field algebra, cf. `terminal_equiv` in
     RH/Recursion.lean).
  3. `H_cap PosDef` + `det A_cap = D_cap * det H_cap > 0` make the full
     bordered matrix `A_cap` positive definite
     (`posDef_fromBlocks_border`, RH/Inertia.lean wave-10 layer -- the
     Schur-complement step of the reviewer plan).
  4. Every `A_n` with `n <= cap` is a principal submatrix of `A_cap`
     (border column included), hence positive definite
     (`posDef_submatrix_of_injective`).  NOTE on fidelity to the
     reviewer's Riccati route: the backward drain sum
     `D_n = D_N + sum rho_k >= D_N > 0` (v959 S0.1 drain, exact in
     RH/Recursion.lean `drain`/`telescope`) is exactly the
     Schur-complement monotonicity of nested principal minors; the
     principal-submatrix restriction used here is the same finite
     algebra in matrix coordinates -- no extra input is consumed.

CONSEQUENCES (all PROVED, formerly conditioned on the master `sorry`):
  * `augmented_prefix_positive` -- the master theorem, a corollary of
    the two true holes;
  * `prefix_chain_positive_main` (former edge B), `terminal_margin_
    positive_main`, `terminal_crossratio_main` (former edge A).
C1 MOVE (the reviewer final-domain contract): the two true holes and
the master corollaries now live in RH/Canonical.lean, retyped onto the
canonical construction (`CanonicalWindow` in place of the opaque
`MainWindow`; the budget half of the terminal statement is PROVED
there, the open conjunct is `terminal_q_canonical`).  This file keeps
the two predicates (`LStar`, `TerminalPositive`) and the sorry-free
reconstruction theorem they feed.

THE TWO TRUE HOLES after C1: `lstar_canonical` and
`terminal_q_canonical` (both RH/Canonical.lean); the r263 dictionary
`Z^2/m = q_N` connecting the terminal statement to the pair
coordinates is formalized there as the ONE named lemma
`pair_terminal_dictionary` (measured 42/42, transcription-blocked).

Claim boundary: research documentation.  NOT evidence for or against
the Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Basic
import RH.Window
import RH.Inertia

namespace RH

open Matrix VonMangoldtWindow

/-! ## The two window predicates -/

/-- **Lemma L* as a predicate** (the wave-6 canonical form, r283/v963):
the archimedean/smooth channel `nu` is strictly `mu`-subordinate on the
free polynomial window.  This is verbatim the statement of
`lstar_subordination` (RH/Window.lean); packaging it as a `Prop` lets
the reconstruction theorem consume it as one named hypothesis. -/
def LStar (w : VonMangoldtWindow) : Prop :=
  ∀ p : Polynomial ℝ, p ≠ 0 → p.natDegree < w.cap →
    w.nuSq p < w.muSq p

/-- **The terminal statement as a predicate** (r258 TERMINAL_Q_LAW /
r260 terminal reduction): positive budget normalization `B > 0` and the
terminal cross-ratio inequality `q_N < 1`.

FIDELITY to the machine-checked r258/r260 semantics: `w.q` is the
determinant form `(B - D_cap)/B` of RH/Window.lean, which by
`D_eq_schur` equals the bordered Schur ratio `u^T H^{-1} u / B` -- the
exact-rational TERMINAL_Q_LAW object of r258 (42/42 rungs, min margin
0.0139); by the v959 S0.3 budget telescope (`telescope` /
`terminal_reduction` in RH/Recursion.lean, TELESCOPE_EXACT r258) the
positivity `D_N = B(1 - q_N) > 0` is equivalent to `q_N < 1` GIVEN the
budget normalization `B > 0` -- and `B > 0` is itself part of the
measured r243 budget form `B = S_{N-2} + 5/7` (a sum of nonnegative
drain increments `rho_k = F_k^2/h_k >= 0` on the wall plus the positive
floor `5/7`), so carrying it inside the predicate imports no content
beyond r243/r258.  Without it `q < 1` carries no sign information --
the two conjuncts together are exactly the terminal gate
`terminal_equiv` (RH/Recursion.lean) consumes. -/
def TerminalPositive (w : VonMangoldtWindow) : Prop :=
  0 < ((w.B : ℚ) : ℝ) ∧ w.q < 1

/-- the terminal statement yields a positive terminal Schur margin:
`D_cap = B(1 - q) > 0`.  Pure ordered-field algebra (the reviewer's
step 2). -/
theorem terminal_margin_pos_of_terminal (w : VonMangoldtWindow)
    (hT : TerminalPositive w) : 0 < w.D w.cap := by
  obtain ⟨hB, hq⟩ := hT
  rw [VonMangoldtWindow.q, div_lt_one hB] at hq
  linarith

/-! ## The reconstruction theorem -/

/-- the augmented matrix `A_n` is a principal submatrix of the terminal
augmented matrix `A_cap` (Hankel rows `0..n-1` plus the border
row/column).  Pure index bookkeeping. -/
theorem A_eq_submatrix_A_cap (w : VonMangoldtWindow) {n : ℕ}
    (hn : n ≤ w.cap) :
    w.A n = (w.A w.cap).submatrix
      (Sum.map (Fin.castLE hn) id) (Sum.map (Fin.castLE hn) id) := by
  ext (i | ⟨⟩) (k | ⟨⟩) <;> rfl

/-- **THE RECONSTRUCTION THEOREM** (wave 10 / r305; reviewer plan
section 3).  L* and the terminal statement imply the full master
positivity: every augmented matrix `A_{w,n} = [[H_n, u_n], [u_n^T, B]]`
through the half-filling cap is positive definite.

Proof skeleton (five lines, all PROVED ingredients):
  1. L* => `H_cap` PosDef            (`lstar_implies_hankel_posDef`),
  2. Terminal => `D_cap > 0`         (`terminal_margin_pos_of_terminal`),
  3. `det A_cap = D_cap * det H_cap > 0`  (definition of `D`),
  4. Schur bordering => `A_cap` PosDef    (`posDef_fromBlocks_border`),
  5. principal-submatrix restriction => `A_n` PosDef for all `n <= cap`
     (`posDef_submatrix_of_injective`; = the backward Riccati drain
     `D_n = D_N + sum rho_k` in matrix coordinates).  NO RH CLAIM. -/
theorem lstar_terminal_implies_master (w : VonMangoldtWindow)
    (hL : LStar w) (hTerminal : TerminalPositive w) :
    ∀ n ≤ w.cap, (w.A n).PosDef := by
  have hH : (w.hankel w.cap).PosDef := by
    rcases Nat.eq_zero_or_pos w.cap with h0 | hpos
    · rw [h0]
      exact posDef_of_isEmpty _
    · exact lstar_implies_hankel_posDef w hL w.cap le_rfl hpos
  have hD : 0 < w.D w.cap := terminal_margin_pos_of_terminal w hTerminal
  have hdetA : 0 < (w.A w.cap).det := by
    have hdh : 0 < (w.hankel w.cap).det := hH.det_pos
    have hsplit : (w.A w.cap).det = w.D w.cap * (w.hankel w.cap).det := by
      rw [VonMangoldtWindow.D, div_mul_cancel₀ _ hdh.ne']
    rw [hsplit]
    exact mul_pos hD hdh
  have hAeq : w.A w.cap = Matrix.fromBlocks (w.hankel w.cap)
      (fun i (_ : Unit) => w.borderVec w.cap i)
      (fun (_ : Unit) k => w.borderVec w.cap k)
      (fun _ _ => ((w.B : ℚ) : ℝ)) := rfl
  have hAcap : (w.A w.cap).PosDef := by
    rw [hAeq]
    exact posDef_fromBlocks_border hH (by rw [← hAeq]; exact hdetA)
  intro n hn
  rw [A_eq_submatrix_A_cap w hn]
  exact posDef_submatrix_of_injective hAcap
    ((Fin.castLE_injective hn).sumMap Function.injective_id)

/-! ## The terminal hole and the master corollaries -- C1 MOVE

The second true hole formerly carried here as `terminal_positive_main
: MainWindow w → TerminalPositive w` is RETYPED onto the canonical
construction (RH/Canonical.lean): the budget half `0 < B` is PROVED
there (`canonical_budget_pos` -- B-fidelity + the named completion's
`budget_pos`), and the genuinely open conjunct is the sharpened hole
`terminal_q_canonical : CanonicalWindow w → w.q < 1`;
`terminal_canonical` re-assembles the verbatim `TerminalPositive`
conclusion.  The master theorem `augmented_prefix_positive` and its
corollaries (`prefix_chain_positive_main`,
`terminal_margin_positive_main`, `terminal_crossratio_main`) moved
with it, statements verbatim modulo the `MainWindow → CanonicalWindow`
domain retype, proofs verbatim through `lstar_terminal_implies_master`
above.  The r263 pair-coordinate connection is formalized there as the
ONE named dictionary lemma `pair_terminal_dictionary`; the former
duplicate sorry `pair_margin_main` is retired (see
RH/PairBound.lean). -/

end RH
