# Compiler necessity: multiplicative information and TFPT clocks
Claim boundary: experiment-only structural synthesis; no claim for or against RH.

Tags: `[T]` classical theorem, `[I]` inference, `[E]` established corpus statement.

## A. Information-theoretic necessity

### A1. Multiplicative composition forces primes

**Theorem [T].** Let labels lie in \(\mathbb N_{\ge1}\), let independent composition be
\(m\otimes n=mn\), and let a size \(I:\mathbb N_{\ge1}\to\mathbb R\) satisfy
\(I(mn)=I(m)+I(n)\). If size is order-compatible (equivalently, monotone; continuity
after extending from positive rationals also suffices), then
\[
I(n)=c\log n,\qquad c\ge0.
\]
Without the regularity condition arbitrary assignments on primes extend additively, so
the condition is necessary and is not silently omitted.

**Proof.** \(I(1)=0\). For integers \(m,n>1\), choose \(a_k=\lfloor k\log m/\log
n\rfloor\). Then \(n^{a_k}\le m^k<n^{a_k+1}\). Monotonicity and additivity give
\(a_kI(n)\le kI(m)<(a_k+1)I(n)\). Divide by \(k\) and let \(k\to\infty\):
\(I(m)/\log m=I(n)/\log n=c\). Positivity gives \(c\ge0\). ∎

**Atomicity [T].** The fundamental theorem of arithmetic is the monoid isomorphism
\[
\mathbb N^\times\simeq\bigoplus_{p\ {\rm prime}}\mathbb N,\qquad
n\longmapsto(v_p(n))_p.
\]
Thus the non-unit indecomposable labels are exactly the primes. A rational relation
\(\sum_pa_p\log p=0\) clears denominators and exponentiates to equality of two prime
factorisations, so every \(a_p=0\). Hence \(\{\log p\}\) is a basis of the
\(\mathbb Q\)-span of \(\{\log n\}\).

**Statistical mechanics [T].** A bosonic Fock system with one-particle energies
\(E_p=\log p\) has
\[
Z_{\rm bos}(\beta)=\prod_p(1-e^{-\beta E_p})^{-1}
=\prod_p(1-p^{-\beta})^{-1}=\zeta(\beta).
\]
The signed/fermionic Euler product is
\(\prod_p(1-p^{-\beta})=1/\zeta(\beta)=\sum_n\mu(n)n^{-\beta}\).
This is the Julia/primon and Bost--Connes arithmetic-QSM dictionary; it is not an RH
criterion.

**Necessity conclusion [I].** Primes need not be supplied by an oracle once a canonical
integer-labelled multiplicative composition law exists: they are its generators. The
actual TFPT question is whether P1/P2 canonically produce that law on physical states,
with logarithmic information as physical time or energy.

### A2. Where TFPT composes states

The scoped search used the requested composition/state-count/Boltzmann/Dirichlet
patterns in the five physics documents and `verification/v*.py`, excluding named
PRIME/HECKE families; the 60-hit inspection was grouped as follows.

| Site | Composition / weight | A1 law on physical states? |
|---|---|---|
| E8 shell census | \(N(n)=240\sigma_3(n)\), Dirichlet series \(240\zeta(s)\zeta(s-3)\) (`v1018`:21-34) | Multiplicative arithmetic readout, but static and not physical subsystem composition. |
| Gaussian/\(\chi_{-4}\) census | Signed representation counts and character Euler factors | Multiplicative coefficients; no entropy or autonomous clock. |
| Kneser/Hecke | Local \(p\)-neighbour correspondences and \(T_p\); restricted tensor product/Satake structure (`v535`:6-29) | **Yes on the arithmetic side.** No physics-side representation of the norm flow. |
| Thermal/horizon traces | \(\mathrm{Tr}\,e^{-\beta H}\), degeneracies, replica counts | Genuine physics QSM, but labels are energy levels, not canonical \(n\in\mathbb N^\times\); no \(n^{-\beta}\) law found. |
| Tensor products/Fock/Wick | Independent sectors and multiplicative dimensions/state counts | State counts multiply and entropy adds, but no canonical integer label whose multiplication is the TFPT transition law. |
| Spectral zeta/Casimir | Heat-kernel and determinant regularisation | Not an Euler product over arithmetic primes. |
| Finite clocks and scale lattice | Direct products \(Z_5\times Z_6\), additive log scales | Finite rank; not \(\mathbb N^\times\). |
| 4D lattice/QCA | Local tensor products, transfer \(e^{-aH}\), quasilocal limit | Physical composition exists; no norm map, multiplicative site label, or \(n^{-\beta}\) spectrum. |

[E] The arithmetic side therefore already carries A1's structure. Its natural
census-QSM partition function is
\[
\sum_{n\ge1}\sigma_3(n)n^{-\beta}=\zeta(\beta)\zeta(\beta-3),
\]
convergent for \(\beta>4\), with the weight-four boundary at \(4\). [I] What is absent
is a physics-derived state space on which the Hecke norm flow is the canonical TFPT
time, rather than a classical arithmetic action attached after the E8 census.

The E8 lattice combines addition (theta/modularity/Poisson summation) and multiplication
(Hecke correspondences), but in the present representation their interaction gives the
known functional equation and Euler product of \(\zeta(s)\zeta(s-3)\). Its zeros are
the zeta zeros and their translate, so this channel is RH-neutral (`prime_story.md`,
Q2; `v535`:41-48). An adele-class construction is stronger because addition, all local
multiplicative places, and the archimedean scaling action act on one quotient.

### A3. Why the prior BC routes died

* `v740` [E/N]: local 55,296-monomial Gram positivity survived. The strong global
  contract failed because adjacent normalised GNS states were not restrictions along
  covariant unital *-embeddings, and the beta-one KMS identity is algebraically
  impossible for bilateral Laurent unitaries:
  \(1=T(u_pu_p^*)=T(u_p^*\sigma_i(u_p))=p^{-1}\)
  (`v740`:31-47,320-377).
* `v741` [E/N]: replacing them by BC Toeplitz isometries repairs the local algebraic
  KMS relation, including finite-box boundary factors. The global covariant UCP window
  errors remain nonmonotone, so no canonical inductive KMS system was obtained
  (`v741`:8-38,412-447).
* This was not primarily a finite-prime or \(\zeta(s-3)\) failure. The decisive failures
  were global covariance/extension and the choice of bilateral versus semigroup
  generators. The E8 census weight shift remains a separate mismatch with the BC
  partition function.

[T/I] \(Z=\zeta(\beta)\zeta(\beta-3)\) is a legitimate arithmetic partition function
of two bosonic prime species with energies \(\log p\) and degeneracies \(1,p^3\), and is
analogous to higher-rank arithmetic QSM. That observation neither constructs the
Connes--Marcolli algebra nor places RH in its KMS phase diagram. Poles/phase transitions
come from real-axis convergence; nontrivial zeros are cancellations of analytic
continuations and are not encoded by positivity of Gibbs weights.

## B. Clock combinations

The exact/numerical audit is
`experiments/tfpt-discovery/clock_combination_spectrum_probe.py` (73/73 checks,
63 singles/pairs/triples, zero survivors).

| Clock/object | Rank / spectrum | Log-rational? | Primitive content | Verdict |
|---|---|---|---|---|
| \(Z_4,Z_5,Z_6\), Coxeter 30 | rank 1 over \(\mathbb Q\), rational multiples of \(\pi\) | No | one commensurable period each | K1 |
| Any finite direct product | rank 1 in the common \(\pi\)-direction | No | finite/commensurable | K1 |
| Resummed \(N=3,4,5,6,8,16,30,240\) | ranks \(2,2,3,3,4,6,10,52\) | Yes: \(6\log(N/(N-n))\) | primes in numerator/denominator valuations; depends on \(N\) | K2 |
| All-\(N\) resummed tower | countable rank; \(6\log\mathbb Q_{>1}\) | Yes | \(6\log p\), but infinitely many labels before reduction | K2+K3 |
| Modular \(K\), seeded v446 covariance | 28 generic float eigenvalues | No canonical rational labelling | no integer or denominator-\(\le1000\) ratio; PSLQ unconfirmable from float64 | K1 |
| Koide Möbius flow | rank 1, \(6\log(3/2)\) | Yes | one rational direction | K2 |
| `F_transfer` | hyperbolic/parabolic/identity classes; no common discrete spectrum | No | continuous \(\log\mu\), not integer monoid | K1 |
| Scale lattice | formal rank 3: \(\alpha^{-1},L_0,\log(8\pi)\) | No | three corpus scales | K1 |
| QCA/4D Hamiltonian | generator exists, arithmetic spectrum unspecified | Unknown | no multiplicative label | K3 |

For fixed \(N\), the raw resummed spectrum never contains \(\log n\) for \(n>1\)
because of the factor six; after normalisation it contains only those integer ratios
accidentally represented by \(N/(N-n)\). Over every \(N\), any reduced \(a/b>1\)
occurs by \(N=a,n=a-b\), while \((a,b)\mapsto(ka,kb)\) gives infinite multiplicity.
The limit is canonical as the set \(\log\mathbb Q_{>1}\), but not as a multiplicity-one
state spectrum and not as a TFPT-derived integer monoid.

### B3. Modular-clock result

For v446, \(C=(I+e^h)^{-1}\), hence \((1-C)C^{-1}=e^h\) and
\(\operatorname{spec}K=\operatorname{spec}h\). The tested \(h\) is a seeded random
positive block-diagonal matrix, not a lattice-labelled covariance. Across sizes
\(4,8,16\), none of 28 ratios was integral or had a denominator-\(\le1000\) rational
fit at \(10^{-12}\). A decimal PSLQ relation cannot be confirmed because the source is
float64. No canonical reparametrisation by \(n\) exists in the corpus: B3 is killed.

### B4. Koide, QCA, and 4D

The Koide vector field has fixed points \(q=2,5\); its time-one multipliers are
\((2/3)^6=64/729\) and \(729/64\), so the translation length is
\(6\log(3/2)\), neither an integer multiplier nor a prime (`v723`:111-139).

[E] The QCA collision band realises reduced \(B^n\) exactly, while continuous
Hamiltonian/OS legs and branch selection were open in `v984`:37-43. `v999`:1-23
subsequently completed the finite/kernel continuous-time ladder but left the
thermodynamic field limit open. `v1013`:11-36 proves a Hamiltonian-class quasilocal
thermodynamic dynamics and Lieb--Robinson bound; it explicitly leaves the gap,
IR universality/common light cone, and continuum open. None of these steps introduces
an arithmetic dilation action or multiplicative integer label. They can provide a
self-adjoint physical generator and inner product, but not its prime spectrum.

## C. Candidate constructions and kill decisions

| Candidate | Canonical now / addition required | F1 / F2 | Bridge 2 | Decision |
|---|---|---|---|---|
| Census-QSM Hecke norm flow \(\sigma_t(T_p)=p^{it}T_p\) | E8 marked Hecke module is canonical; must derive this norm flow from TFPT OS/transfer time | borderline / pass if norms arise functorially, fail if assigned | Natural Hecke Hilbert spaces exist, but no TFPT-selected positive representation or RH positivity | **Worth one frozen contract** |
| Modular clock with log-\(n\) spectrum | Modular formula canonical; requires a derived covariance \(c_n=1/(1+n)\) and canonical labels | pass / currently fail | Self-adjoint \(K\) and GNS metric would be genuine | Weed out now: v446 covariance is generic |
| Resummed-clock tower | Formula canonical at \(N_{\rm fam}=3\); all-\(N\) tower is not | pass / fail | Diagonal real spectrum, but no canonical multiplicity/limit Hilbert space | Weed out K2+K3 |
| 4D lattice with multiplicative site labels | Local \(H,T,\tau_t\) canonical; arithmetic labels absent | pass / fail | Best physical self-adjointness, no prime spectrum | Weed out until labels are derived |
| Extend three-scale lattice by all prime scales | Existing three generators canonical; infinite extension unsupported | fail / fail | Formal diagonal operator only | Weed out as oracle insertion |
| E8 addition + Hecke as mini adele-class space | Both operations canonical separately; needs one quotient/representation and archimedean norm flow | borderline / pass | No independent positive arithmetic generator; current factor is neutral | Fold into census-QSM contract, not a second contract |

Frozen-contract pass condition: construct, from P1/P2 and the marked E8 module, a
physics-selected representation of the Hecke algebra whose modular/transfer flow equals
the norm flow, with no prime list, and prove the local flows glue. Kill on an assigned
\(p^{it}\), a standard BC system merely renamed, failure of global covariance as in
`v740/v741`, or multiplicity not fixed by the corpus. Even a pass closes only bridge 1;
bridge 2 still needs independent self-adjoint/metric positivity not equivalent to Weil.

## D. Verdict (Deutsch; no RH claim)

[T] Präzise bewiesen ist jetzt die Notwendigkeit: Sobald unabhängige Zustände durch
Multiplikation natürlicher Labels komponieren und Information monoton additiv ist,
gilt \(I(n)=c\log n\). Die unzerlegbaren Generatoren dieses Monoids sind genau die
Primzahlen; \(\{\log p\}\) ist die rationale Basis aller \(\log n\). Primzahlen wären
also kein Orakel, **falls** TFPT ein kanonisches physikalisches
\(\mathbb N^\times\)-Kompositionsgesetz besitzt.

[E/I] TFPT besitzt dieses Gesetz bereits auf der arithmetischen Seite:
E8-Theta, Kneser/Hecke und der Census liefern
\(\sum\sigma_3(n)n^{-\beta}=\zeta(\beta)\zeta(\beta-3)\). Es fehlt die Ableitung
derselben Normwirkung als physikalische Zeit/Energie aus P1/P2. Die vorhandene
Addition-plus-Hecke-Struktur reproduziert den bekannten, RH-neutralen
\(\zeta(s)\zeta(s-3)\)-Faktor; sie erzeugt keine neue Nullstelleninformation.

Der Clock-Probe bestand 73/73 Tests, klassifizierte 63 Einzel-, Paar- und
Dreifachkombinationen und fand keinen BC-Kandidaten. Endliche Uhren bleiben
kommensurabel. Der Resummations-Turm erreicht zwar \(6\log\mathbb Q_{>1}\), aber nur
mit \(N\)-abhängigen beziehungsweise unendlich vielfachen Labels. Der reale v446-
Modularclock hat kein kanonisches ganzzahliges Spektrum. Koide liefert nur
\(6\log(3/2)\).

Koide, QCA und die 4D-Hamilton-Dynamik sind für echte Zeitentwicklung wichtig:
insbesondere existieren lokale Selbstadjungiertheit, unitäre Dilatation und
quasilokale Thermodynamik. Sie liefern aber weder eine arithmetische Skalenwirkung
noch primitive Perioden \(\log p\).

Ehrlicher Stand: Brücke 1 ist offen; nur ein enger Census-QSM/Hecke-Normfluss-Vertrag
ist einen weiteren eingefrorenen Test wert. Brücke 2 ist ebenfalls offen. Die
4D-Schicht kann ihren Hilbertraum liefern, aber nicht ohne zusätzliches Theorem die
benötigte arithmetische Positivität; die Weil-Bedingung umzubenennen wäre zirkulär.
