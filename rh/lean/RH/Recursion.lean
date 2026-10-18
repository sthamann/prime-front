/-
RH/Recursion.lean -- the PROVED core identities of the coupled-tau lane.

Provenance: rounds r256-r263.
  * Riccati drain + bilinear identity + telescope + terminal reduction:
    ledger PRIME.PORT.RHP.COUPLEDTAU.TERMINAL.01 [E], module
    verification/v959_coupledtau_terminal_dictionary.py, section S0
    (S0.1 drain, S0.2 bilinear form, S0.3 terminal consequence gate);
    discovery probes coupledtau_probe.py (r257, SPEC_SHA 73d8247f6de36a2b)
    and budget_anatomy_probe.py (r258, SPEC_SHA 28026ae6b0750098).
  * Two-branch trivial direction: round r263 (note DXCIV), probe
    cancellation_adjudication_probe.py (SPEC_SHA 151a9176...),
    TWO_BRANCH_DECOMPOSITION_EXACT -- the cheap branch g_w >= 0 closes
    the target by the triangle inequality alone (no cancellation).

Every theorem in this file is proved (no `sorry`).  The proofs are pure
(ordered-)field algebra, exactly the class the corpus certifies with
sympy-symbolic + exact-rational gates.

Claim boundary: research documentation.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import RH.Basic
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace RH

namespace ChainData

variable {K : Type*} [Field K] (d : ChainData K)

/-- **The bilinear tau form** (v959 S0.2): the Wronskian-type identity
`tauAug_n tau_{n+1} - tauAug_{n+1} tau_n = (c_n F_n)^2 tau_n^2`.
Pure ring algebra -- the right side is a manifest square, so the fiber
increment is a positive tau cross-ratio wherever `tau_n tau_{n+1} > 0`. -/
theorem bilinear (n : ℕ) :
    d.tauAug n * d.tau (n + 1) - d.tauAug (n + 1) * d.tau n
      = (d.c n * d.F n) ^ 2 * (d.tau n) ^ 2 := by
  simp only [tau_succ, tauAug_succ, a, b]
  ring

/-- **The Riccati drain** (v959 S0.1): the coupled two-term recursion implies
`D_{n+1} = D_n - rho_n`, under the division prerequisites `c_n, h_n != 0`
(hence `a_n != 0`) and `tau_n != 0`. -/
theorem drain (n : ℕ) (hc : d.c n ≠ 0) (hh : d.h n ≠ 0)
    (ht : d.tau n ≠ 0) :
    d.D (n + 1) = d.D n - d.rho n := by
  have ha : d.a n ≠ 0 := by
    simp only [a]; exact mul_ne_zero (pow_ne_zero 2 hc) hh
  simp only [D, tau_succ, tauAug_succ, a, b, rho] at *
  field_simp
  ring

/-- **The budget telescope** (v959 S0.3 / r258 TELESCOPE_EXACT):
on a regular window, `D_N = B - S_N` -- the entire spend is the exact
Schur telescope of the drain.  Induction on the drain law. -/
theorem telescope {N : ℕ} (hreg : d.Regular N) :
    d.D N = d.B - d.S N := by
  induction N with
  | zero => simp [D, S]
  | succ n ih =>
      have hreg' : d.Regular n := fun k hk => hreg k (Nat.lt_succ_of_lt hk)
      have hn : n < n + 1 := Nat.lt_succ_self n
      obtain ⟨hc, hh⟩ := hreg n hn
      have ht : d.tau n ≠ 0 := d.tau_ne_zero hreg n (Nat.le_of_lt hn)
      rw [d.drain n hc hh ht, ih hreg', S_succ]
      ring

/-- **The terminal reduction** (v959 S0.3): with the r243 budget form
`B = S_N + m` (in the corpus `m = 5/7` and `N` is the last free index),
the terminal margin collapses to one scalar: `D_{N+1} = m - rho_N`. -/
theorem terminal_reduction {N : ℕ} (m : K) (hreg : d.Regular (N + 1))
    (hB : d.B = d.S N + m) :
    d.D (N + 1) = m - d.rho N := by
  rw [d.telescope hreg, hB, S_succ]
  ring

end ChainData

section OrderedField

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- **The terminal consequence gate** (v959 S0.3): for a positive terminal
budget `m > 0`, `margin = m - r > 0` iff `q = r / m < 1` -- the entire
fiber positivity is ONE terminal inequality. -/
theorem terminal_equiv {m r : K} (hm : 0 < m) :
    0 < m - r ↔ r / m < 1 := by
  rw [div_lt_one hm]
  constructor <;> intro h <;> linarith

/-- **The two-branch trivial direction, non-strict** (r263): if the triangle
certificate `|Z| <= U` holds and the branch scalar `g = M - U` is
nonnegative (`U <= M`), then `q = Z^2 / M^2 <= 1`.  Triangle inequality
alone -- no cancellation consumed. -/
theorem two_branch_cheap {Z U M : K} (hM : 0 < M)
    (htri : |Z| ≤ U) (hg : U ≤ M) :
    Z ^ 2 / M ^ 2 ≤ 1 := by
  rw [div_le_one (by positivity)]
  have hZM : |Z| ≤ M := le_trans htri hg
  calc Z ^ 2 = |Z| ^ 2 := (sq_abs Z).symm
    _ ≤ M ^ 2 := by nlinarith [abs_nonneg Z]

/-- **The two-branch trivial direction, strict** (r263): with strict slack
`U < M` (the measured cheap branch `g_w > 0`) the target is closed
strictly: `q = Z^2 / M^2 < 1`. -/
theorem two_branch_cheap_strict {Z U M : K} (hM : 0 < M)
    (htri : |Z| ≤ U) (hg : U < M) :
    Z ^ 2 / M ^ 2 < 1 := by
  rw [div_lt_one (by positivity)]
  have hZM : |Z| < M := lt_of_le_of_lt htri hg
  calc Z ^ 2 = |Z| ^ 2 := (sq_abs Z).symm
    _ < M ^ 2 := by nlinarith [abs_nonneg Z]

/-- Corollary shape used at the terminal degree: `q_N = rho_{N-1} / m`
with `rho = F^2 / h`, `h > 0`, `m > 0`: the exception-branch requirement
`|Z| < sqrt(m)` in the scale-free form `Z^2 < m` gives `q_N < 1` where
`Z^2 = h * rho` normalizes the readout (`Z = r_{N-1}` in r263 notation,
`Z^2 / m = q_N`). -/
theorem exception_scalar_closes {Z m : K} (hm : 0 < m) (hZ : Z ^ 2 < m) :
    Z ^ 2 / m < 1 := (div_lt_one hm).mpr hZ

end OrderedField

end RH
