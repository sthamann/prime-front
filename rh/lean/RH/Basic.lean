/-
RH/Basic.lean -- abstract chain data of the coupled-tau lane.

Provenance: rounds r256-r259, ledger PRIME.PORT.RHP.COUPLEDTAU.TERMINAL.01
[E], module verification/v959_coupledtau_terminal_dictionary.py (section S0),
discovery probe experiments/tfpt-discovery/coupledtau_probe.py (r257,
SPEC_SHA 73d8247f6de36a2b).

The chain data of one window are sequences over an arbitrary field K:
  c n  -- exact Chebyshev leading coefficients (c_n = (2/rh)^n in the corpus)
  h n  -- the base chain (monic norm squares of the signed defect measure)
  F n  -- the border Cauchy readouts
  B    -- the budget scalar (r243 form: B = S_{N-2} + 5/7)
from which the derived objects are
  a n   = c_n^2 h_n            (the base coefficient; its sign IS the world
                                pivot sign)
  b n   = -(c_n F_n)^2         (a manifest negative square -- source-sign-pure
                                in every world)
  rho n = F_n^2 / h_n          (the Riccati drain increment)
  tau / tauAug                 (the coupled two-term recursion)
  D n   = tauAug n / tau n     (the indivisible full-source object)
  S n   = sum_{k<n} rho k      (the running budget spend).

Seed convention: the corpus seeds tau_1 = h_0, tau^aug_1 = h_0 B - F_0^2
(with c_0 = 1).  Here we seed one step earlier, tau 0 = 1 and tauAug 0 = B,
so that the uniform recursion reproduces the corpus seeds at n = 1 whenever
c 0 = 1.  All identities below are index-uniform and do not depend on this
convention.

Claim boundary: research documentation.  NOT evidence for or against the
Riemann Hypothesis in either direction.  NO RH CLAIM.
-/
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset

namespace RH

/-- The abstract chain data of one window of the coupled-tau lane
(v959 S0.1).  `K` is any field; the corpus instantiates exact rationals. -/
structure ChainData (K : Type*) [Field K] where
  /-- exact Chebyshev leading coefficients `c_n`. -/
  c : ℕ → K
  /-- the base chain `h_n` (monic norm squares). -/
  h : ℕ → K
  /-- the border Cauchy readouts `F_n`. -/
  F : ℕ → K
  /-- the budget scalar `B`. -/
  B : K

namespace ChainData

variable {K : Type*} [Field K] (d : ChainData K)

/-- `a_n = c_n^2 h_n` -- the base coefficient of the coupled recursion. -/
def a (n : ℕ) : K := (d.c n) ^ 2 * d.h n

/-- `b_n = -(c_n F_n)^2` -- a manifest negative square (source-sign-pure). -/
def b (n : ℕ) : K := -((d.c n) * (d.F n)) ^ 2

/-- `rho_n = F_n^2 / h_n` -- the Riccati drain increment. -/
def rho (n : ℕ) : K := (d.F n) ^ 2 / d.h n

/-- the tau chain: `tau_0 = 1`, `tau_{n+1} = a_n tau_n` (v959 S0.1). -/
def tau : ℕ → K
  | 0 => 1
  | n + 1 => d.a n * tau n

/-- the augmented tau chain: `tauAug_0 = B`,
`tauAug_{n+1} = a_n tauAug_n + b_n tau_n` (v959 S0.1). -/
def tauAug : ℕ → K
  | 0 => d.B
  | n + 1 => d.a n * tauAug n + d.b n * tau d n

/-- `D_n = tauAug_n / tau_n` -- the indivisible full-source object
(the fiber margin lives at `D_N`). -/
def D (n : ℕ) : K := d.tauAug n / d.tau n

/-- `S_n = sum_{k<n} rho_k` -- the running budget spend. -/
def S (n : ℕ) : K := ∑ k ∈ Finset.range n, d.rho k

@[simp] theorem tau_zero : d.tau 0 = 1 := by simp [tau]
@[simp] theorem tauAug_zero : d.tauAug 0 = d.B := by simp [tauAug]
@[simp] theorem S_zero : d.S 0 = 0 := by simp [S]

theorem tau_succ (n : ℕ) : d.tau (n + 1) = d.a n * d.tau n := by
  simp [tau]
theorem tauAug_succ (n : ℕ) :
    d.tauAug (n + 1) = d.a n * d.tauAug n + d.b n * d.tau n := by
  simp [tauAug]

theorem S_succ (n : ℕ) : d.S (n + 1) = d.S n + d.rho n :=
  Finset.sum_range_succ _ n

/-- A window is *regular* through degree `N` when no coefficient or base
value vanishes there (the division prerequisites of the drain law).  On the
measured windows this holds by construction for `c` and is the wall
statement for `h`. -/
def Regular (N : ℕ) : Prop :=
  ∀ k < N, d.c k ≠ 0 ∧ d.h k ≠ 0

theorem a_ne_zero {N k : ℕ} (hreg : d.Regular N) (hk : k < N) :
    d.a k ≠ 0 := by
  obtain ⟨hc, hh⟩ := hreg k hk
  simp only [a]
  exact mul_ne_zero (pow_ne_zero 2 hc) hh

/-- The tau chain never vanishes on a regular window. -/
theorem tau_ne_zero {N : ℕ} (hreg : d.Regular N) :
    ∀ n ≤ N, d.tau n ≠ 0 := by
  intro n
  induction n with
  | zero => intro _; simp
  | succ m ih =>
      intro hm
      have hmN : m < N := Nat.lt_of_succ_le hm
      have h1 : d.tau m ≠ 0 := ih (Nat.le_of_lt hmN)
      have h2 : d.a m ≠ 0 := d.a_ne_zero hreg hmN
      rw [tau_succ]
      exact mul_ne_zero h2 h1

end ChainData

end RH
