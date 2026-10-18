# Positivity in TFPT's origin layer

Structural search only; no claim for or against RH. Status shorthand: `[E]` exact/classical or machine-checked within the stated finite model, `[N]` numerical/certified finite evidence, `[P]` premise/conditional/open contract.

## Scope and filter

The origin section tree is: integer skeleton (`origin_theory.tex:85`), three routes to 8 (`:534`), Coxeter rotation (`:642`), gapped fixed point (`:669`), common alpha/horizon/Lambda readout (`:984`), cyclic interpretation (`:1026`), falsifiers (`:1101`), seam/horizon statement (`:1166`), consequences (`:1455`), closure program (`:1504`), and honest status (`:1632`).

The controlling filter is `positive_cone_blindness_result.json`: positive measures, coefficient squares, SOS, per-term positivity, and positive diagonal GNS norms are unchanged when the negative/archimedean channel is rescaled. In its exact toy, the blind data are identical on both sides of \(t_*=9/2\), while \(M_\mu-tM_\nu\) changes from positive definite to indefinite. Only a **METRIC** comparison of both channels or **OPERATOR** positivity with an independently derived explicit-formula bridge can decide the target.

## P1 — Inventory

| # | Structure and source | Positive object; provenance/status | Class; data carried | Bridge-2 result |
|---|---|---|---|---|
| 1 | \(c_3=1/(8\pi)\), `origin_theory.tex:1188-1196` | Positive inverse one-sided \(S^2\) curvature coefficient; P1/geometric alignment `[E]/[P]` | BLIND; arch only | Scalar sign, no \(\mu\)-vs-\(\nu\) comparison |
| 2 | Positive anti-degrees, `introduction.tex:196-210` | Three positive integers summing to 4; BG/MS typing `[E]/[P]` | BLIND/LOCAL; neither | Finite partition cone |
| 3 | \(E_8\) Gram/Cartan/Type-II norm, `tfpt_1_architecture_e8.tex:440-450` | Positive-definite even unimodular lattice/Hermitian Gram `[E]` | BLIND/LOCAL; prime census | Positive shell counts, no arch defect |
| 4 | Hodge/Riemann candidates, `tfpt_1:278-290,3500-3520,5488-5493` | Cover Riemann-bilinear route, finite Hodge tables and cusp Hodge metric; identifications `[P]` | BLIND/LOCAL; arch | No Kähler positivity theorem specifically at \(\tau=i\); no prime action |
| 5 | RP covariance and OS/GNS norm, `origin:1747-1758`, `v446:17-43` | Reflection form/covariance/GNS metric; finite Gaussian `[E/N]`, continuum/raw state `[P]` | OPERATOR/LOCAL; arch | Genuine positivity, no prime data |
| 6 | OS transfer \(\Lambda=e^{-h}\), `v446:20-39,91-139` | Positive contraction, spectrum in \((0,1]\) `[E]/[P]` | OPERATOR/LOCAL; arch | No arithmetic scale or Weil measure |
| 7 | Modular \(K=\log((1-C)C^{-1})\), `origin:1770-1781`, `v446:31-43` | Self-adjoint free modular generator in positive GNS space `[E]/[P]` | OPERATOR/LOCAL; arch | Best self-adjoint seed; covariance has no canonical \(n,p\) labels |
| 8 | Perron fixed point, `origin:669-690,755-767` | Positive leading vector and gap of primitive transport `[E]/[P]` | OPERATOR/LOCAL; neither | Spectrum \(\{1,(2/3)^6,(1/3)^6\}\), not zero spectrum |
| 9 | CPTP/Stinespring QCA, `origin:770-796`, `v984:1-43` | Complete positivity downstairs; exact unitary upstairs `[E]/[P]` | OPERATOR/LOCAL; neither | Hilbert space is system qutrit \(\otimes\) a stream of record qutrits; no arch/prime data |
| 10 | Weak-collision/GKSL split, `v999:1-23` | CPTP flow, GNS-symmetric dissipator, Hamiltonian split `[E/N]/[P]` | OPERATOR/LOCAL; neither | No multiplicative arithmetic action |
| 11 | Quasilocal \(H_\Lambda,\tau_t\), `tfpt_4:809-824`, `v1013:11-37` | Hermitian local \(H\), positive \(e^{-aH}\), unitary dynamics, LR bound `[E/N]/[P]` | OPERATOR; arch | Strong physical seed, but no Hecke/norm flow |
| 12 | KMS/Gibbs/horizon trace, `origin:800-817`, `tfpt_4:700-717` | Positive thermal state and Boltzmann weights `[E/N]/[P]` | BLIND; arch | Partition-function positivity does not control continued zeros |
| 13 | Heat kernel/\(\zeta\)-determinant, `tfpt_1:3870-3913` | Positive heat semigroup before analytic continuation; regularized determinant `[E]/[P]` | OPERATOR; arch | Compact discrete spectrum; continuation zeros are not eigenvalues |
| 14 | Replica/area/Gaussian horizon sector, `origin:1250-1267,1428-1445`, `horizon:560-620` | Entropy coefficient, Gaussian norm, gapped area law `[E]/[P]` | BLIND/LOCAL; arch | No prime channel |
| 15 | \(E_8\)-theta heat trace, `v1018:27-46`, `v535:1-48` | Positive torus heat semigroup and shell trace `[E]` | OPERATOR; **arch+prime** | Unique meeting point, but discrete-spectrum neutral |
| 16 | Kernel-Loewner/window floor, `tfpt_4:960-974` | Smallest eigenvalue of assembled signed kernel `[N]` | METRIC/LOCAL; cited scope arch only | Filter-sensitive, but prime term is empty in certified scope |
| 17 | Seam-bit RP blindness/straddle toy, `introduction:226-244`, `tfpt_1:246-251,1486-1488` | Free RP is side-blind; positive interacting toy selector `[E]/[P]` | BLIND/LOCAL; arch | Selects a seam bit, not \(\mu/\nu\) |
| 18 | Admissible OS measure, `origin:1813-1818,1901-1907` | PSD transfer, tight measure, \(H_{\rm OS}=-\log T\ge0\), inherited many-body gap `[E]/[P]` | OPERATOR/LOCAL; arch | No arithmetic action or Weil trace |
| 19 | Finite Weil/GNS family metric, `tfpt_1:2116-2149`, `v539:6-10` | GNS metric and finite \(Q_{\rm fam}\) containing prime+arch channels `[E]/[P]` | METRIC/LOCAL; **arch+prime** | \(Q_{\rm fam}\ne Q_\zeta\); doubling/Plancherel obstructions |
| 20 | Matching-ledger positivity, `tfpt_1:2207-2246`, `v541` | Per-term finite Weil-ledger decomposition `[E]/[P]` | BLIND/LOCAL; **arch+prime** | Retired by positive-cone blindness; global signed comparison open |

The “topological fixed point” is not a separate self-adjoint operator. Operationally it is the stationary vector \(Tm=m\) of the finite primitive transport, with convergence rate \((2/3)^6\) (`origin_theory.tex:669-767`); other uses include RG and the scalar Ward root. Its linearization is a finite contraction/Jacobian. No origin statement identifies it as a canonical self-adjoint generator carrying the arithmetic explicit formula.

P1 does not encode Hilbert positivity. It fixes a positive orientation/normalization
\[
c_3^{-1}=|\mathbb Z_2|\int_{S^2}K\,dA=2\cdot4\pi,
\]
then aligns it with gravitational and thermal coefficients. The curvature integral is topological; no signed prime measure occurs.

The requested Kähler/Hodge check is negative in the strict sense: the origin/architecture source contains Hodge tables, a conditional Riemann-bilinear route on \(y^3=x^4-1\), and an open cusp-Hodge/residue-metric identification, but no theorem that a Kähler polarization at the \(\tau=i\) \(E_8\) seam supplies the required arithmetic positive form.

The origin also records an explicit non-positivity warning (`origin_theory.tex:1914-1928`): the bare conformal mode has wrong-sign kinetic coefficient \(-3/2\). GHP/entire-form-factor treatments are conditional repairs, not an additional positive bridge.

## P2 — The meeting point

For the self-dual \(E_8\) lattice,
\[
\theta_{E_8}(it)=\sum_{v\in E_8}e^{-\pi t|v|^2}=E_4(it),\qquad
\int_0^\infty(\theta_{E_8}(it)-1)t^{s-1}dt
=\pi^{-s}\Gamma(s)\,240\zeta(s)\zeta(s-3),
\]
first in the convergence domain, then by meromorphic continuation. Thus \(L^2(\mathbb R^8/E_8)\) is the sole **origin-derived geometric operator space** carrying the archimedean Gaussian/\(\pi,\Gamma\) side and the lattice/Hecke census side. The finite \(Q_{\rm fam}\) and matching-ledger objects in rows 19–20 also assemble both channels, but they are downstream explicit-formula analysis surfaces, not an origin mechanism or common physical/arithmetic state space.

With \(x=\log t\), \(dt/t=dx\), so Mellin transform on a vertical line is Fourier transform in \(x\). The generator \(-i\,d/dx\) on \(L^2(\mathbb R,dx)\) is self-adjoint with continuous spectrum \(\mathbb R\). But \(\theta-1\) is one generalized vector/distribution: its Mellin transform is a matrix coefficient, not the generator's eigenvalue list. Zeros of \(\zeta(s)\zeta(s-3)\) are zeros of that continued coefficient; poles/resonances likewise require continuation. They are not eigenvalues of the dilation generator or of the compact torus Laplacian.

A Connes-type quotient would instead use the noncompact adele-class space \(\mathbb A_K/K^\times\): the field's multiplicative group acts on the additive adeles, producing the scaling/orbit trace. For \(K=\mathbb Q(i)\), \(O_K^\times=\mu_4\) and Gaussian primes enter \(K^\times\). TFPT's \(\mu_4\) mark exactly matches the unit group, but the origin layer does not construct \(\mathbb A_K/K^\times\), its action, or Tate's self-dual measure.

Exact scoped word counts:

| File | self-dual | Poisson summation | adele | idele | Tate |
|---|---:|---:|---:|---:|---:|
| `origin_theory.tex` | 0 | 0 | 0 | 0 | 0 |
| `tfpt_1_architecture_e8.tex` | 4 | 0 | 0 | 0 | 2 |
| `tfpt_prime_front.tex` | 14 | 1 | 0 | 0 | 5 |

The architecture hits are code/lattice self-duality or imported Tate cells, not an origin axiom for an adelic quotient/self-dual Haar measure.

### r129, precisely

Commit `d58cb7e3` (“discovery freeze round 129 … self-dual construction round”) proves an **interior** no-go: if bounded \(\Theta+\Theta^*=I\), then with \(S=\Theta-\tfrac12\),
\[
W=\Theta\Theta^*=\tfrac14+SS^*\ge\tfrac14.
\]
Hence normalized moments cannot reproduce the certified falling source diagonals. Matched off-line blocks can be exactly self-dual while on-line zeros cannot: this interior condition selects violations, not RH. The catalog groups it as `r116-r129`, `failure_class=NOT_APPLICABLE`. It is **not** a no-go for self-dual Haar measure or all adelic models: finite-window Krein/CMV completions are exactly self-dual; the RH-priced step is the all-window \(L\to\infty\) quantifier.

## P3 — Operator candidates and the joint-spectrum check

| Operator | Spectrum | Hecke relation | Could its measure be \(\tilde\mu=\mu-\nu\)? |
|---|---|---|---|
| QCA collision unitary | finite discrete phases | none | No joint data |
| modular \(K\) | finite in verified models; continuum unknown | commutes with \(\mu_4\), not Hecke | No explicit-formula identification |
| \(H_\Lambda\) / OS Hamiltonian | finite-volume discrete; infinite unknown | none | No arithmetic labels |
| fixed-point linearization | finite contraction spectrum | none | Not canonical self-adjoint arithmetic dynamics |
| \(E_8\)-torus \(\Delta\) | discrete, nonnegative, compact resolvent | shell/theta Hecke only | Spectral zeta is neutral |
| \(e^{-t\Delta}\) | positive discrete contraction | arithmetic after shell trace | Same neutrality |
| log-dilation \(-i\partial_{\log t}\) | continuous \(\mathbb R\) | none in TFPT | Missing \(K^\times\) quotient and prime trace |

For \(|v|^2=2n\), \(\Delta e_v=4\pi^2|v|^2e_v=8\pi^2n\,e_v\), and the first multiplicities are
\[
(n,N(n))=(1,240),(2,2160),(3,6720),(4,17520),(5,30240).
\]
Therefore
\[
\zeta_\Delta(s)=\sum_{v\ne0}(4\pi^2|v|^2)^{-s}
=240(8\pi^2)^{-s}\zeta(s)\zeta(s-3).
\]
This reproduces the Eisenstein series and nothing about zero location.

Precision correction: `v535` proves Kneser/modular Hecke correspondences on lattice/theta channels and \(E_4\) as an Eisenstein eigenform. It does **not** prove that every \(T_p\) is characterwise diagonal on the fixed torus \(L^2\). Thus the supported “joint spectrum” is shell/theta-level: Laplace shell \(n\), multiplicity \(240\sigma_3(n)\), Hecke eigenvalue \(1+p^3\) on \(E_4\). The nontrivial zeros remain analytic-continuation zeros, not joint eigenvalues.

General obstruction: compact/finite TFPT spaces have discrete spectra, while their \(L\)-functions arise as heat traces or spectral zeta functions. Their continued zeros are analytic artifacts of those transforms. Zeros-as-spectrum requires a noncompact Connes/Berry-Keating-type scaling space, a domain/self-adjoint extension, and a prime explicit-formula trace. `event_log_function.md:53-77,146-161` finds no arithmetic scaling action and no canonical emergent-time self-adjoint generator.

## P4 — Minimal missing structures

1. **Adele-class host (not sufficient):** derive \(L^2(\mathbb A_{\mathbb Q(i)}/\mathbb Q(i)^\times)\), self-dual measure, and multiplicative scaling from P1/P2. Seed: \(\mu_4=O_{\mathbb Q(i)}^\times\), Gaussian \(E_8\), Hecke census. Absent: quotient, \(K^\times\) action, measure axiom. Even a pass gives the trace formula; positivity remains open.
2. **Hilbert–Pólya operator (sufficient):** derive a self-adjoint \(A\) and canonical vector/domain whose spectral measure or trace identity is the signed Weil object. Seed: modular \(K\), \(H_\Lambda\), OS/GNS. Absent: prime action and explicit-formula identification.
3. **Compiler metric inequality (sufficient):** derive \(\int p^2d\nu<\int p^2d\mu\) from an independent variational principle. Seed: entanglement equilibrium and gap-dominance are only analogies. No origin functional compares these two arithmetic measures.

Assuming positivity of an arithmetic generator after defining it through the Weil form is circular: it assumes the decisive metric/sign condition. The generator, domain, Hilbert metric, arithmetic action, and trace identification must be independently derived.

No frozen contract is written: the theta/heat object carries both data types and is OPERATOR-class, but fails the explicit-formula identification test by discrete-spectrum neutrality.

## P5 — Verdict (Deutsch, ≤350 Wörter)

TFPTs Ursprung enthält echte Positivität, aber keine derzeit tragfähige Brücke 2.

**Rang 1: \(E_8\)-Theta/Heat/Laplacian — OPERATOR, archimedisch + primärithmetisch.** Das ist der einzige natürliche Treffpunkt: Gaußkern, \(\pi,\Gamma\), \(E_8\)-Schalen und Hecke liegen zusammen. Er scheitert jedoch exakt an **discrete-spectrum neutrality**: Das kompakte Torusspektrum ist \(8\pi^2n>0\); \(\zeta(s)\zeta(s-3)\) ist seine analytisch fortgesetzte Spektral-Zeta. Deren Nullstellen sind keine Eigenwerte.

**Rang 2: modularer Generator \(K\), OS-Transfer und quasilokales \(H_\Lambda\) — OPERATOR.** Sie liefern positive Hilberträume, Selbstadjungiertheit/Unitärität und teils Lieb–Robinson-Dynamik. Ihnen fehlen aber Prime/Hecke-Daten, eine multiplikative Skalenwirkung und die explizite-Formel-Identifikation.

**Rang 3: QCA/Stinespring und Perron-Fixpunkt — OPERATOR/LOCAL.** Die diskrete Dilatation lebt auf Qutrit plus Record-Anzillen; der Fixpunkt ist der dominante Vektor einer endlichen Kontraktion. Beide sind endlich und arithmetisch blind.

**Rang 4: \(E_8\)-Gram/Hodge, RP-Kegel, Gibbs/KMS, Replica-/Horizont- und positive Koeffizienten — BLIND oder LOCAL.** Sie beweisen Norm-, Kegel-, Entropie- oder Termpositivität, lesen aber das entscheidende Verhältnis \(\nu/\mu\) nicht. Gibbs-Positivität der parallelen Census-QSM-Brücke hilft daher nicht.

Ein Seed existiert: \(\mu_4=O_{\mathbb Q(i)}^\times\), Gaussian-\(E_8\), Theta/Hecke sowie physikalische selbstadjungierte Operatoren. Nicht vorhanden ist **ein gemeinsamer Raum** mit archimedischer und primärer Wirkung.

Nötig wäre entweder (a) ein unabhängig hergeleiteter Hilbert–Pólya-Operator mit Weil-Spektralmaß oder (b) eine Compiler-Variation, die direkt „archimedisch \(\ge\) prim“ beweist. Ein adelischer Quotient mit selbstdualem Maß würde nur die Spurformel liefern und wäre allein nicht hinreichend. Ehrlicher Stand: **kein Ursprungselement passiert beide Tests; Brücke 2 bleibt offen.**
