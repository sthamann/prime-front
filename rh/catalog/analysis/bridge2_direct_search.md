# Bridge 2 — direct structural search (parent agent, 2026-09-04)

Claim boundary: structural analysis only; no claim for or against RH.
Tags: [T] classical theorem · [E] proved in corpus · [I] inference of this note.

## 1. The three equivalent shapes of bridge 2

Let W be the Weil kernel on the log-scale axis (prime side: archimedean smooth part
minus atoms Λ(n) n^{-1/2} at ±log n). Then the following are equivalent [T]:

(a) Bochner: W is a positive-definite function on R ⇔ Σ_ρ δ(t−γ_ρ) is a positive measure ⇔ RH.
(b) Euclidean/OS: the Wick-rotated kernel is reflection-positive w.r.t. the reflection
    u ↦ −u induced by the functional equation s ↦ 1−s ⇔ it is a Laplace transform of a
    positive measure (Widder/Bernstein) ⇔ the "mass spectrum" {γ_ρ} is real.
(c) Hilbert–Pólya: OS reconstruction yields a Hilbert space and a self-adjoint scale
    Hamiltonian H with spectrum {γ_ρ}.

None of these adds information; they relocate it. The only *mechanism* in mathematics
or physics that yields reflection positivity without assuming it is a construction with a
manifestly positive transfer operator (Markov / Gibbs / conditional expectation), whose
two-point function is then computed and compared with the target kernel. Bridge 2 is
therefore, in its only admissible shape [I]:

> a manifestly positive (Markov) semigroup in log-scale whose reflection symmetry is the
> functional equation and whose *generator itself* — not its analytic continuation —
> carries the zeros.

## 2. TFPT does possess the shape — on the Euler side

[I] Renormalisation-group coarse-graining is a Markov semigroup in log-scale (block
averaging is a unital completely positive map). On the E8 torus R^8/E8 the natural
coarse-grainings are the conditional expectations E_{L'} onto L'-periodic functions for
superlattices L' ⊃ E8 of finite index; RG time is u = log[L':E8]. Dually (E8 self-dual)
superlattices of index n correspond to sublattices of index n, so the census of bridge 1
(`census_qsm_normflow_probe.py`, H = log index) is exactly the RG time of this
semigroup. The Poisson/self-duality L ↔ L*, θ_E8(1/t) = t^4 θ_E8(t), is the reflection
u ↦ −u — i.e. the functional equation. Shape-wise this is a Euclidean scale model with
the right reflection. Bridge 1 is its Euler side.

## 3. What the scale two-point function actually is

On characters e_v(x) = e^{2πi⟨v,x⟩}, v ∈ E8* = E8, each E_{L'} is a projection
(E_{L'} e_v = e_v if v ∈ L'*, else 0). The index-n transfer operator
T_n := Σ_{[L':E8]=n} E_{L'} is diagonal with eigenvalue
#{sublattices L ⊂ E8 of index n with v ∈ L} ∈ N — self-adjoint, so the reflection is a
genuine symmetry of the semigroup [T]. The scale two-point function of the vacuum
character is the sublattice zeta function

    Σ_n a(n) n^{-s} = ζ(s) ζ(s−1) ⋯ ζ(s−7)      (Solomon, r = 8) [T]

(for the Z[i]-module of bridge 1: ζ_{Q(i)}(s)⋯ζ_{Q(i)}(s−3), verified 200/200 [E]).
Coefficients are positive integers ⇒ per-term positive ⇒ BLIND under the positive-cone
lemma (`positive_cone_blindness_probe.py`) [E]. The zeros are zeros of the analytic
continuation. Reflection positivity *on the critical line* for this kernel would mean:
the continued function is a Laplace transform of a positive measure ⇔ its zeros are
real ⇔ RH (de Bruijn–Newman form) [T]. So the RG-Markov structure lands exactly on
the criterion: manifest positivity on the Euler side, restatement on the critical side.

## 4. Consequence: one fact behind all of today's kills [I]

E8 theta/Hecke, census-QSM/Gibbs, Kneser and HNF groupoids, Siegel–Weil, Waldspurger
squares, Cohen seeds, the sublattice RG above — every one of them is the *Euler side* of
the same would-be reflection-positive scale model. Their positivity is per-term and
therefore blind; the critical side is the criterion. No object built from a compact
torus, a finite-type module or a discrete spectrum can escape this: there the arithmetic
L-function is a spectral zeta function and its zeros are continuation artefacts.

## 5. The only remaining idea shape (outside the current corpus) [I]

A *stochastic* (Markov) scale semigroup on the Connes cokernel — the adele class space
modulo the Fourier-invariant part — whose generator is self-adjoint by construction
(positivity of a Markov generator on a probability space) and whose spectrum is the
zeros. Connes' scaling action is unitary, not Markov; a Wick-rotated, stochastic
version would be the RP form of the global trace formula. Whether it exists is RH
content. TFPT can contribute only if its origin story contains (i) an adelic state space
(quotient by K*, self-dual measure) and (ii) a stochastic scale dynamics on it. Today's
evidence: adeles 0 hits, scaling flow 0 hits; r129's self-dual no-go rules out only the
interior Θ+Θ* = I construction, not self-dual Haar measures as such
(`event_log_function.md` §Q2, §Q5; `positivity_origin_search.md` §P2). Independent
confirmation: the origin-layer sweep found 16 positivity structures, of which only the
E8 theta/heat operator carries both archimedean and prime data, with discrete spectrum
and zeros only in the spectral-zeta continuation (`positivity_origin_search.md`).

## 6. Status

Bridge 2: OPEN, with its admissible shape now fixed. Neither a TFPT positivity nor a
new probe is warranted until an object of the shape in §5 exists; every Euler-side test
is predicted to pass trivially and every critical-side test is the criterion.
