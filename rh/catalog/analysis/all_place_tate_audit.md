# All-place Tate audit: Calabi--Yau, finite carriers and the remaining RH bridge

**As of:** 2026-09-05. **Repository tip audited:**
106f27b08b096a3af9a8769a0b39c3eee3274c36 (origin/main at audit start).

**Claim boundary:** this note contains exact identities, a finite-carrier no-go and a
correction of record. It does **not** prove RH. The all-place intersection identity and
its independent positivity theorem remain open.

## 1. Result

The level-8 rigid Calabi--Yau route does isolate the Riemann zeta factor exactly, but it
does not transport the Calabi--Yau, \(E_8/H_8\), code or finite quantum information into
that factor. The canonical projection lands on the universal Tate line
\(\mathbf Q(0)\), which contains none of those data. To the extent that projective
representation data survive in \(\operatorname{End}(V)\), they lie in the adjoint
complement; scalar-twist, sign and concrete-realization data can be lost altogether.

A second, independent obstruction is dimensional. Conditional on the external strict
window floor reported in Zhu's v2 preprint, one fixed finite-dimensional Hodge, Rosati,
code or quantum carrier cannot represent the full window Weil form as an exact linear
pullback: an infinite-dimensional source mapped into a fixed finite-dimensional target
has a kernel, while a strictly positive quadratic form does not.

Therefore the specific exact-linear pullback route studied here needs an
infinite-dimensional carrier, an unbounded compatible family or a direct-limit object.
This no-go does not exclude nonlinear procedures, growing finite discretizations or
finite proxies for approximation. A proof through the stated geometric route must still
put every finite prime, the archimedean place, the pole terms and an independent global
polarization on one common correspondence space; a single fixed finite proxy or a bare
Euler product is not that exact object.

The executable regression is
verification/v1021_all_place_tate_rank_audit.py. Its expected verdict is:

    TATE_FACTOR_EXACT; FIXED_FINITE_CARRIER_NO_GO;
    RANKIN_EXPONENT_DROP_FALSIFIED; ALL_PLACE_INTERSECTION_OPEN
    CLAIM_BOUNDARY: NO_RH_PROOF

## 2. Exact Tate factor in the rigid \(f_8\) channel

Let \(X/\mathbf Q\) be a rigid level-8 Calabi--Yau threefold whose middle cohomology
corresponds to

\[
f_8(\tau)=\eta(2\tau)^4\eta(4\tau)^4,
\qquad V=H^3_{\mathrm{et}}(X,\mathbf Q_\ell).
\]

At a good prime, write

\[
\alpha_p+\beta_p=a_p,
\qquad \alpha_p\beta_p=p^3.
\]

Then

\[
V\otimes V=\operatorname{Sym}^2V\oplus\wedge^2V,
\qquad \wedge^2V\simeq\mathbf Q_\ell(-3),
\]

and, after the unitary shift \(u=s-3\),

\[
\operatorname{End}(V)
\simeq \mathbf Q_\ell(0)\oplus\operatorname{Ad}^0(V),
\qquad
L(\operatorname{End}V,u)=\zeta(u)L(\operatorname{Ad}^0V,u).
\]

The canonical projector is

\[
e_T(A)=\frac{\operatorname{tr}(A)}2 I.
\]

It is idempotent, conjugation-equivariant and self-adjoint for the induced
Hilbert--Schmidt form. This is the exact part of the route.

At a good prime the coefficient of the degree-one term of the symmetric-square factor
is

\[
\alpha_p^2+\alpha_p\beta_p+\beta_p^2=a_p^2-p^3.
\]

The earlier label \(a_p^2-2p^3\) names only
\(\alpha_p^2+\beta_p^2\); it omits the middle eigenvalue
\(\alpha_p\beta_p=p^3\). The executable probe and the current record use the corrected
coefficient.

### The bad place \(p=2\)

It is invalid to infer the invariants of a tensor product by tensoring the invariant
subspaces. Even when \(V^{I_2}=0\), the identity endomorphism is fixed by inertia under
conjugation and has zero monodromy. The Tate line therefore contributes

\[
L_2(\mathbf Q(0),u)=(1-2^{-u})^{-1}.
\]

The full ramified adjoint factor is not reconstructed by v1021; the module certifies the
unavoidable scalar Tate factor and keeps the remaining local calculation explicit.

### The archimedean place and pole normalization

With

\[
\Gamma_{\mathbf R}(s)=\pi^{-s/2}\Gamma(s/2),
\qquad
\Gamma_{\mathbf C}(s)=\Gamma_{\mathbf R}(s)\Gamma_{\mathbf R}(s+1),
\]

the factorization is compatible with

\[
\Gamma_{\infty,\operatorname{End}}(u)
=\Gamma_{\mathbf C}(u)\Gamma_{\mathbf C}(u+3),
\]

\[
\Gamma_{\infty,\operatorname{Tate}}(u)=\Gamma_{\mathbf R}(u),
\qquad
\Gamma_{\infty,\operatorname{Ad}}(u)
=\Gamma_{\mathbf R}(u+1)\Gamma_{\mathbf C}(u+3).
\]

If

\[
\xi(u)=\tfrac12u(u-1)\Gamma_{\mathbf R}(u)\zeta(u),
\]

then the completed Tate factor is \(2\xi(u)/(u(u-1))\), not simply
\(\xi(u)\). A relative determinant or trace formula must retain the pole normalization.

## 3. Tate information-loss theorem

The image of \(e_T\) is the scalar line \(\mathbf Q_\ell I\). It is the same line for
every two-dimensional representation. Consequently, any construction that first
projects to this line and subsequently uses only functorial data of the image cannot
recover \(a_p(f_8)\), level 8, the chosen Calabi--Yau geometry or the \(E_8/H_8\)
realization from that image. Projective information that survives passage to
\(\operatorname{End}(V)\) lies in \(\operatorname{Ad}^0(V)\); scalar twists, signs and
realization data need not survive in \(\operatorname{End}(V)\) at all.

For a hypothetical global operator \(\Theta\), this gives a dichotomy:

1. If \([\Theta,e_T]=0\), the Tate block is independent and its desired
   self-adjointness or positivity is the original Hilbert--Polya/Weil problem for zeta.
2. If \([\Theta,e_T]\ne0\), the compressed determinant does not factor automatically;
   a new global Schur-complement or determinant identity is required.
3. Positivity of the entire endomorphism block would also control the adjoint
   \(L\)-function and is a stronger, presently unavailable input.

The Tate projection is therefore an exact factor identification, not a positivity
mechanism.

## 4. Fixed finite-carrier no-go

Let \(\mathcal H_L\) be an infinite-dimensional space of Weil test functions supported
in a compact window. Suppose a linear compiler into a fixed finite-dimensional carrier
\(E\), followed by a positive form \(R\), represented the Weil form:

\[
C:\mathcal H_L\to E,
\qquad Q_\zeta(f,g)=R(Cf,Cg).
\]

Rank--nullity gives a nonzero \(f\in\ker C\). Then the displayed representation forces
\(Q_\zeta(f)=0\). This contradicts any strict lower bound
\(Q_\zeta(f)\ge c_L\lVert f\rVert_2^2\) with \(c_L>0\).

Zhu's v2 preprint supplies such an external certified strict-positivity premise on
\([-0.8,0.8]\). The repository does not re-prove that premise; conditional on it, the
linear-algebra consequence is immediate:

> No linear pullback of a positive form from one fixed finite-dimensional
> \(E_8\)-, \(H_8\)-, Calabi--Yau \(H^3\)-, \(\operatorname{End}(H^3)\)- or finite quantum
> carrier can equal the complete Weil form on that window.

For \(\operatorname{End}(H^3)\), the target dimension is four, so five independent source
directions suffice. For the scalar Tate line, two suffice. This does not exclude
nonlinear methods, growing finite families, direct limits, finite discretizations or an
infinite adelic, automorphic or operator-algebraic realization. It proves only that one
fixed finite carrier cannot provide the stated exact linear pullback on the full
strictly positive window space.

## 5. Quantum, code and geometric variants

The following variants do not evade the two obstructions:

- finite code-zeta, MacWilliams and self-duality tests provide finite functional
  equations, but do not construct the all-place Weil pairing;
- positive Gibbs/KMS states live in the half-plane where the zeta partition function is
  a genuine trace; analytic continuation to the critical strip is not a positive Gibbs
  state;
- UCP, GNS, OS and Schur-complement constructions preserve supplied positivity but do
  not create the signed prime--archimedean alignment missing from the source;
- a connected metric graph with lengths \(\log p\) normally creates mixed
  \(\log(pq)\) walks, absent as independent primitive orbits in the zeta explicit formula;
- finite self-adjoint zeta approximants require a proved infinite spectral or
  determinant limit before they can yield a global statement;
- ordinary Hodge/Rosati positivity acts on a fixed cohomological carrier and does not by
  itself assemble all prime powers, the gamma term and the pole in one global pairing.

The strongest surviving TFPT quantum shape is an infinite, compatible
Petz--Watatani--Tate network of conditional expectations. Its finite Stinespring
shadows are meaningful, but the compatible normal limit and its identification with the
critical Weil form are precisely the missing all-place theorem, not consequences of
finite complete positivity.

## 6. Correction of record: historical Rankin miniature

The historical probe claimed that nonnegative coefficients and a summatory main growth

\[
A(X)=\sum_{n\le X} b_n=O(X^q)
\]

imply \(b_n=O(n^{q-1+\varepsilon})\). They do not. The direct consequence is only
\(b_n\le A(n)=O(n^q)\). The probe then fitted
\(K=\max_{n\le N}b_n/n^{q-1+\varepsilon}\) and tested the same inequality on the same
window, making that gate tautological.

An exact counterexample preserving both the main asymptotic and the pole is

\[
b_n=4n^3+\mathbf 1_{n=32^m}n^{18/5}.
\]

Its partial sums equal \(X^2(X+1)^2+O(X^{18/5})\sim X^4\), while

\[
\sum_{n\ge1}\frac{b_n}{n^s}
=4\zeta(s-3)+\frac{2^{18-5s}}{1-2^{18-5s}}.
\]

The spike series is analytic at \(s=4\) and equals \(1/3\) there, so the simple pole is
unchanged. Nevertheless, along \(n=32^m\),
\(b_n/n^{31/10}\ge n^{1/2}\to\infty\). The same construction with baseline
\(12n^{11}\) and spike exponent \(58/5\) corrects the Ramanujan-tau paragraph.

Rankin's actual 1939 argument uses a quantitative error term in a Rankin--Selberg
summatory asymptotic and differences that error. A pole plus positivity alone is not
that argument and does not give the claimed Deligne-strength exponent. The corrected
probe retains its valid Hecke, Jacobi, local-factor and finite regression checks, and
ends with RANKIN-EXPONENT-DROP-FALSIFIED; FINITE-IDENTITIES-SURVIVE.

## 7. Exact contract for a complete solution

A geometric proof route is complete only after all seven statements below are supplied
without using RH, a zero oracle or a metric defined from the desired answer.

| Gate | Required theorem | Current state |
|---|---|---|
| A1 | A global absolute curve with every finite place, infinity, scaling/Frobenius action and an explicit treatment of \(2\). | Carrier candidates exist; no complete TFPT realization. |
| A2 | A well-defined square with an all-place Arakelov/height intersection product. | Open. |
| A3 | A linear, continuous and injective map \(f\mapsto D_f\) from a dense Weil test class to primitive or degree-zero correspondences. | Open; in this exact-linear formulation its image must be infinite-dimensional or realized as an unbounded compatible/direct-limit family. |
| A4 | Exact local-to-global identity: all \(p^k\) terms with \((\log p)p^{-k/2}\), the gamma/\(\log\pi\) term and the pole terms arise from the same pairing. | Open; scalar local normalization is fixed by v1021. |
| A5 | A global polarization/Hodge-index inequality on the whole image, proved independently of zeta zeros. | Open. |
| A6 | Density, closure and convergence transferring the identity and sign to the full Weil class. | TFPT form convergence is available; the required positivity premise remains open. |
| A7 | A regularized determinant/trace identity retaining \(u(u-1)/2\), conductors, epsilon factors, \(p=2\) and infinity. | Local Tate bookkeeping exact; global identity open. |

A1--A7 would yield

\[
Q_\zeta(f)=-\langle D_f,D_f\rangle_{\mathrm{Ar}}\ge0,
\]

and hence RH by Weil's criterion. The first genuinely new missing statement is the
**Tate--Weil realization theorem**: construct the zero-independent family \(D_f\) and
prove that its full all-place intersection pairing is the polarized Weil form. The
second is the absolute Hodge-index theorem on that image.

## 8. Reproduction and sources

Run from the repository root:

    python3 -B verification/v1021_all_place_tate_rank_audit.py
    python3 -B experiments/tfpt-discovery/rankin_positivity_miniature_probe.py

Primary references used to type the external premises and geometry:

- Cynk--Meyer, *Modular Calabi--Yau threefolds of level eight*,
  arXiv:math/0504070.
- Rankin, *Contributions to the theory of Ramanujan's function tau(n) and similar
  arithmetical functions. II*, Proc. Cambridge Philos. Soc. 35 (1939),
  DOI:10.1017/S0305004100021101.
- Yuan--Zhang, *The arithmetic Hodge index theorem for adelic line bundles I*,
  arXiv:1304.3538.
- Connes--Consani, *The Absolute Twistor Line and the Geometry of the compactified
  Spec Z*, arXiv:2609.00299.
- Zhu, *Weil positivity in compact windows*, arXiv:2608.24827v2.
- André Weil, *Sur les “formules explicites” de la théorie des nombres premiers*,
  Commun. Sém. Math. Univ. Lund, Tome supplémentaire (1952), 252--265, for the
  positivity criterion.

The exact algebra and counterexample are re-derived in v1021; external theorems are
identified as premises and are not presented as machine-proved by the repository.
