# Program evolution for the three FREQ propositions

Experiment-only report for `PRIME.RDAGGER.PROGRAM_EVOLUTION.01`.
No RH claim or anti-RH claim. Seed `20260904`.

## Exact proposition statements

Write \(a_k=2^k\), \(r_k=\lfloor\sqrt{k}\rfloor\),
\(m_k=k2^{r_k}-1\), and
\(\Delta_k=\log(a_k)/(m_k+1)=2^{-r_k}\log 2\).
For a native `GridElement` \(f\), let
\[
e_{\rm arch}(k,f)=
\left|\operatorname{archRead}(a_k,m_k,f)-\operatorname{weilArchSide}(f)\right|.
\]

1. **`SelectedArchErrorQuadraticRate`.** For every native \(f\), there is
   \(k_0\) such that, for all \(k\ge k_0\), once the selected mesh covers
   `meshExp(f)` and \(a_k\) covers `elementAnchor(f)`,
   \[
   e_{\rm arch}(k,f)\le
   \operatorname{archRateConst}(f)\Delta_k^2,
   \quad
   \operatorname{archRateConst}(f)=
   (1+\operatorname{supportBound}f)^2
   \left(1+\sum_i|x_i|\right)^2.
   \]

2. **`SelectedPolynomialApproximatesGrid`.** For every \(k>0\) and native
   \(f\) with `meshExp(f) ≤ selectedMesh(k)`, there is
   \(z\in\mathbb R^{\operatorname{cap}(W_k)+1}\) such that
   \[
   \left|\operatorname{fullRead}(a_k,m_k,f)
   -z^\mathsf T A_{\rm cap}(W_k)z\right|
   \le e_{\rm arch}(k,f).
   \]
   This is a scalar read dictionary, not a uniform polynomial approximation.

3. **`frequently_selected_augDualResolvent_ge_half`.** For arbitrarily large
   \(K\), there is \(k\ge K\) and a faithful \(\mu\)-orthonormal transcription
   of the selected real window \(W_k^\mathbb R\) for which
   \[
   R^\dagger(W_k^\mathbb R)-\tfrac12 I\succeq0.
   \]

`selected_polynomial_nonneg_of_cone` is already proved: if the third
finite-window cone holds at \(k\), then
\(z^\mathsf T A_{\rm cap}(W_k)z\ge0\) for every \(z\).

## T1 — archimedean quadratic rate

The evaluator is the corpus implementation in `arch_rate_probe.py`:
`INSTANCE.arch_lags`, `QUAD.acf_of`, `QUAD.to_fun`, and the concrete
u-space integral from `extraction_joint_probe.py`. Six native families were
used: three Gaussian widths, a Legendre window, a DPSS/prolate window, and a
smooth bump. The available distinct selected meshes were \(k=5,9,16\).

Best evolved measured envelope:
\[
e_{\rm arch}(k,f)\le
0.331299232\left(
\|g_f''\|_{1,\mathrm{disc}}+\|g_f\|_{H^2,\mathrm{disc}}
\right)\Delta_k^2.
\]
It had 0/72 sample violations; worst normalized ratio was
0.999999999999. The simpler candidate
\(0.333530945\|g_f''\|_{\infty,\mathrm{disc}}\Delta_k^2\)
also had 0/72 violations.

| family | \(e/\Delta^2\), \(k=5\) | \(k=9\) | \(k=16\) |
|---|---:|---:|---:|
| Gaussian 0.20 | 0.073988 | 0.091775 | 0.097632 |
| Gaussian 0.35 | 0.031432 | 0.036622 | 0.038352 |
| Gaussian 0.50 | 0.018281 | 0.020861 | 0.021692 |
| Legendre window | 0.066923 | 0.082714 | 0.087989 |
| DPSS/prolate | 0.035392 | 0.041422 | 0.043433 |
| smooth bump | 0.023594 | 0.027648 | 0.028997 |

The ratios increase toward family-dependent nonzero limits; the three mesh
levels do not justify a fitted limit, but they are consistent with a
second-order leading term.

**Classification: CLASSICAL-PROVABLE in shape, not proved here.** Composite
tent/trapezoid Euler–Maclaurin gives, cell by cell,
\[
\int_a^b h-\operatorname{Trap}_\Delta(h)
=-\frac{\Delta^2}{12}\bigl(h'(b)-h'(a)\bigr)+O(\Delta^4).
\]
Apply this to the regularized arch integrand, split off the removable
endpoint, sum the cells, and bound the remainder uniformly on the compact
support. The constant \(1/12\) belongs to the smooth integrand estimate; the
fitted constants above are only discrete surrogates and are not theorems.

Lean still needs: integrability and endpoint regularity of
`weilArchUIntegrand`; a composite trapezoid/tent error lemma (or
Euler–Maclaurin with an explicit remainder); bounds translating the native
piecewise-linear autocorrelation into the existing `archRateConst`; and the
identification of `productionArchLagNear/Far` with the quadrature cells.
Likely Mathlib ingredients are `intervalIntegral`, Taylor remainder lemmas,
bounded variation/absolute continuity, and finite-sum integral splitting.

## T2 — polynomial approximation

Chebyshev programs of degree \(n=\operatorname{cap}(W_k)-1\) were fitted at
\(k=5,9,16\). The best empirical norm envelope was
\[
E_n(g_f)\le
0.982464733\,\|g_f''\|_{\infty,\mathrm{disc}}/n^2.
\]
This has the shape of the second-order Jackson theorem
\(E_n(g)\le C\,\omega(g'',1/n)/n^2\), with Bernstein polynomials providing
the standard constructive approximation route.

**Classification: INCONCLUSIVE, not CLASSICAL-PROVABLE as stated.** Jackson's
1912 theorem controls \(\|g-p_n\|_\infty\). The Lean proposition instead
requires one scalar identity involving the window-dependent quadratic form
\(z^\mathsf T A_{\rm cap}z\), with tolerance exactly
\(e_{\rm arch}(k,f)\). No measured norm estimate supplies the missing
whitening, border coordinate, pole correction, or read dictionary.
Moreover native autocorrelations are piecewise linear, so a literal
\(\|g''\|_\infty\) is only a discrete surrogate.

A valid Lean proof would need a constructive map from native tent
coefficients to the polynomial coefficient-plus-border vector \(z\), a
proved bound transporting Jackson error through every arch/comb/pole read,
and a final constant no larger than `selectedArchError`. Likely Mathlib
ingredients are polynomial density/Weierstrass, Chebyshev or Bernstein
approximation, modulus of continuity, and finite-dimensional quadratic-form
continuity. Those ingredients do not currently prove the stated tolerance.

## T3 — spectral FREQ and hardest windows

The full-cap object was reconstructed from `cofinal_family_probe.py` and
`deep_builder_probe.py`. With \(G^\dagger=\begin{psmallmatrix}E&v\\v^T&\gamma
\end{psmallmatrix}\), the measured margin is
\[
\lambda_{\min}(R^\dagger-\tfrac12I)
=\frac1{1+\lambda_{\max}(G^\dagger)}-\frac12.
\]

| \(k\) | \(\Delta_k\) | prime powers | margin |
|---:|---:|---:|---:|
| 5 | 0.173287 | 18 | 2.21356e-2 |
| 7 | 0.173287 | 44 | 2.50051e-3 |
| 9 | 0.0866434 | 117 | 1.90370e-4 |
| 10 | 0.0866434 | 198 | 9.39510e-5 |
| 12 | 0.0866434 | 604 | 1.99752e-5 |
| 14 | 0.0866434 | 1961 | 5.38208e-6 |
| 16 | 0.0433217 | 6635 | 1.15514e-6 |

All 12 windows \(k=5,\ldots,16\) were good. The evolved rule `return True`
therefore scored 100% on held-out \(k=\{7,10,13,16\}\), but the 1,000-fold
permutation-null baseline was also 100%. There is no classification signal.

**Empirical selection-rule conjecture:** on the tested selected family,
the margin stays positive while decaying toward zero. This is only a finite
census. It neither establishes infinitely many good \(k\) nor distinguishes
a feature-based rule from the constant predictor.

Hardest-window Galerkin programs reused the converged Legendre evaluator in
`weil_window_profile_scout.py`:

| \(L\) | degree | evolved infimum | scout \(\lambda_*(L)\) |
|---:|---:|---:|---:|
| 0.50 | 80 | 9.33657e-7 | 9.33657e-7 |
| 0.65 | 80 | 3.94706e-11 | 3.94706e-11 |
| 0.80 | 100 | 1.64243e-17 | 1.64243e-17 |
| 1.00 | 120 | 5.75860e-30 | 5.75860e-30 |

No value was below the \(-10^{-11}\) correctness tolerance.
**Classification: RH-HARD.**

## Bottom line

The run classified T1 as a classical analytic target with a concrete proof
plan, but produced no Lean proof. T2 did not reduce to Jackson/Bernstein;
its exact scalar channel remains open. T3 remains the FREQ spectral kernel.
Thus the honest classification count is **3 open Props before → 2 after
classification**, not the requested target of 1.

The two remaining statements say: (i) every native test read must be
represented by the positive polynomial channel to within exactly the arch
error, and (ii) arbitrarily far out, another selected full-cap window must
have augmented dual resolvent at least one half.

Budget: estimated API cost `$0.001723`; actual `$0` because the environment
key was absent. Runtime `0.633 s`; 92 programs logged. No limit fired.
