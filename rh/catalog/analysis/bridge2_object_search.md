# Bridge 2 object search (2026-09-04)

Claim boundary: literature/corpus synthesis and finite-window analysis only. No
claim for or against RH. `[T]` classical/published theorem, `[E]` certified
corpus statement, `[O]` open, `[I]` inference of this note.

## Target and filter

The target is not merely a positive Euler product or a self-adjoint operator
whose determinant is later continued. It is a reflection-positive Euclidean
scale model whose OS generator itself carries the zeta ordinates, or an
independently derived metric inequality (L*) comparing the full archimedean and
prime channels. The positive-cone result excludes per-term, square, SOS and
positive-measure certificates; metric/operator positivity remains admissible
(`positive_cone_blindness_result.json`).

## S1. Literature

| work | object | positivity: assumed or derived | unconditional part | stopping point / relation to target |
|---|---|---|---|---|
| Connes, *Selecta Math.* 5 (1999), 29–106, DOI `10.1007/s000290050042` | scaling action on the adele-class space; zeros as absorption spectrum, off-line zeros as resonances | Hilbert-space scaling is derived; the global trace/positivity needed to force only critical spectrum is not | noncommutative trace-formula framework and spectral interpretation | closest global state space, but no Markov/OS construction deriving global Weil positivity |
| Meyer, *Duke Math. J.* 127 (2005), 519–595, DOI `10.1215/S0012-7094-04-12734-4`; arXiv:`math/0412277` | nuclear Fréchet/virtual idele-class representation with all L-function zeros in its spectrum | no positivity bias in the global space | spectral/character realization of all zeros and poles | not a Hilbert-space self-adjoint generator; deliberately no RH implication |
| Connes–Consani, arXiv:`2006.13771`, DOI `10.1007/s00029-021-00689-4`; Connes–Consani, arXiv:`2310.18423` | compressed scaling action, Sonin/prolate spaces, archimedean then semi-local Weil forms | archimedean-place positivity is derived from a Hilbert-space trace; global/semi-local positivity is not | conceptual archimedean positivity and semi-local operator stage | finite-place coupling is still the criterion; no stochastic generator with proven zeta spectrum |
| Connes–Consani–Moscovici, arXiv:`2511.22755`, DOI `10.4171/ELM/37/3`; Connes–van Suijlekom, arXiv:`2511.23257` | self-adjoint finite rank-one perturbations of the log-scaling spectral triple | finite self-adjointness is derived (Carathéodory–Fejér/operator theory) | finite operators; spectra numerically track low zeta ordinates | convergence of spectra or regularized determinants to the zeta object is open; the finite generator is not yet proved to carry the zeros |
| Suzuki, arXiv:`2206.03682`, DOI `10.1112/jlms.12785`; arXiv:`2209.04658` | screw kernel \(K_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)\), helical embedding, Krein canonical system | global \(K_g\succeq0\) / positive Hamiltonian is equivalent to RH, not derived | explicit \(g\); trace class on every finite interval; unconditionally \(\Psi(t)>0\) on \(0<t<t_0\) for some \(t_0>\log2\), and \(K_g\) is positive definite on \((-a,a)\) for some \(a_0>0\) | forward problem remains: construct the positive Hamiltonian globally from the explicit prime/archimedean data |
| Suzuki, arXiv:`2606.09096` | localized Weil form \(Q_W^a\), canonical self-adjoint \(A_a\), Friedrichs realization, finite-interval differential extensions | \(A_a\) is self-adjoint and lower-bounded unconditionally; positivity is proved only for small \(a\) | explicit \(A_a\); continuity of its lowest eigenvalue; finite-interval self-adjoint extensions with real spectra | the proposed \(a\to\infty\) convergence to \(z^2\xi/\xi'\) is a conjecture; these real finite spectra are not yet zeta zeros |
| de Branges (1986–1994); Conrey–Li, arXiv:`math/9812166`, DOI `10.1155/S1073792800000489`; Lagarias, *JNT* 2006 context | de Branges entire-function spaces and shift positivity | the shift positivity is an extra sufficient hypothesis | de Branges implication theorems | Conrey–Li exhibit failure for \(E(z)=\xi(1-iz)\): \(\Re\langle F,F(\cdot+i)\rangle>0\) fails (already at the 34th zeta zero); a natural operator positivity can be strictly stronger than RH |
| Burnol, arXiv:`math/9902080`, arXiv:`math/0101068`, DOI `10.1515/FORUM.2004.16.6.789` | local conductor operator \(\log|x|+\mathcal F^{-1}\log|y|\mathcal F\), co-Poisson and Sonine/de Branges spaces | local self-adjoint/symmetric Fourier structure is constructed | local explicit-formula terms; vectors indexed by zeros in Sonine spaces; small-support Weil checks | zeros label vectors/functional data, not the point spectrum of one proved global positive generator |
| Yoshida (1992); Bombieri (2000), *Rend. Lincei* 11, 183–233; Li, DOI `10.1006/jnth.1997.2137`; Maślanka arXiv:`math/0402168` | localized Weil quadratic form, variational operator and Li coefficients | small-support Weil positivity is derived; all-\(n\) Li positivity is equivalent to RH | \(Q_W>0\) for \(\operatorname{supp}f\subset[-L,L]\) when \(2L\le\log2\); finite reduction/minimizers; finite Li tables reach thousands, not a theorem near \(10^5\) | both all-window and all-\(n\) positivity are criteria; no growing structural lower bound |
| Deninger program; Álvarez López–Kordyukov et al., arXiv:`2402.06671`; Leichtnam, arXiv:`2508.15971` | foliated flow/Lefschetz trace and would-be arithmetic cohomology | Hodge-index positivity is available for genuine geometric foliations, but the arithmetic object is not constructed | trace formulas for specified foliated flows; structural comparison with adelic spaces | the required arithmetic foliation/cohomology and polarization remain open |
| Bender–Brody–Müller, DOI `10.1103/PhysRevLett.118.130201`; Bellissard arXiv:`1704.02644`; arXiv:`2607.19067` | non-Hermitian \(xp\)-type operator with zeta boundary condition and candidate metric | quasi-Hermiticity/metric completion is required, not established in the needed space | formal eigen-equation and boundary encoding | standard metric completion has missing candidate eigenstates; no accepted Hilbert–Pólya operator |
| Bost–Connes, *Selecta Math.* 1 (1995), 411–457, DOI `10.1007/BF01589495` | \(C^*\)-dynamical/KMS system with Hamiltonian \(\log N\) and partition function \(\zeta(\beta)\) | Gibbs/KMS positivity and the phase transition are derived | arithmetic quantum statistical system and symmetry breaking at \(\beta=1\) | Euler-side thermodynamics only: the generator has log-integer spectrum, not zeta ordinates; no Weil/OS positivity mechanism |

Searches for “reflection positivity/OS/Markov semigroup + Riemann zeros”
found no peer-reviewed construction of the fixed target shape. The evolving
arXiv:`2408.15135` builds an intertwining metric whose positivity is explicitly
an operator version of Weil positivity (and versions assume simplicity), hence
is a criterion. The Zenodo deposit DOI `10.5281/zenodo.15880788` claims a complete
OS proof but is not an accepted/refereed RH proof and supplies no independently
validated replacement for the missing positivity step.

## S2. Corpus contact

| corpus object | exact contact | status relative to target |
|---|---|---|
| W1, `notes/arxiv_w1_note` and `v630`–`v643` | identifies the TFPT window measure and odd Galerkin form with Suzuki's \(B_a=D^*G_aD\), including pole, smooth and prime-atom conventions; `v643` reports 11/11 | `[E]` finite identification only; no positivity statement |
| W2, `v644` and the W3-note addendum | FEM \(H^1/L^2\) rates 1/2 and Rayleigh–Ritz slices; Fejér density identity and smoothed floor \(c_0=0.306\) are established | formal Mosco/norm-resolvent bridge and the pointwise frame-level bound remain open in the note's decomposition |
| W3, `notes/arxiv_w3_note` / `v677` | positivity of a deployed finite family is an off-line-zero detector with resolved band \(\gamma\le\pi/D\), subject to a strength floor | uniform W3 (`PRIME.UNIFPOS.01`) over every window is exactly the conjectural wall; the note explicitly says “there is no ladder underneath” |
| W4 | transfer from the finite families to all Weil test functions | `[O]`; requires W2, control in \(a\), and uniformity |
| `v955`–`v963` | RHP/IIKS/tau dictionaries reduce a signed finite-window moment problem to quasi-definiteness | they do not construct Suzuki's continuous canonical-system Hamiltonian |
| L*, `v963`, `rh_program.tex:733–791` | \(\int p^2d\nu<\int p^2d\mu\) for every \(0\ne p\), \(\deg p<N_w\), equivalently \(\lambda_{\max}(E_{N_w})<1\) | `[O]`; this is the corpus metric inequality and the closest finite analogue of screw-kernel positivity |
| `v980` | exact margin/cancellation identities around L* | finite algebra plus measured laws; no bound proving L* |
| `v981` | Borodin particle–hole duality gives \(L^*\Longleftrightarrow R>\frac12I\) | exact reparametrization, explicitly not a proof |
| `v982` | completed Dirichlet-\(L\) archimedean frame and finite 126-window census | shows frame portability, not a global canonical Hamiltonian or GRH statement |
| Lean FREQ/Gabor routes | fixed-\(k\) inequality is proved; augmented-dual-resolvent, selected-grid approximation and quadratic arch-error rate remain propositions/open; countable Gabor criterion is equivalent to RH | formalizes the reduction/criterion boundary; it does not derive the missing uniform estimate |

Thus no corpus object is the positive global canonical Hamiltonian. W1 is the
operator-form dictionary; W2 is domain/limit control; W3 is the uniform
positivity wall; W4 is global transfer. In the separate finite-moment language,
L* is the load-bearing metric gap.

## S3. Construction attempt

### (i) Explicit screw function

With \(\psi=\Gamma'/\Gamma\) and
\(\Phi(z,s,a)=\sum_{m\ge0}(m+a)^{-s}z^m\), Suzuki uses
\[
\begin{aligned}
g(t)={}&-4(e^{|t|/2}+e^{-|t|/2}-2)
+\sum_{n\le e^{|t|}}\frac{\Lambda(n)}{\sqrt n}(|t|-\log n)\\
&-\frac{|t|}{2}\{\psi(1/4)-\log\pi\}
-\frac14\{\Phi(1,2,1/4)-e^{-|t|/2}\Phi(e^{-2|t|},2,1/4)\}.
\end{aligned}
\]
Write this literally as \(g=g_{\rm arch}+g_{\rm prime}\), where the
displayed ramp sum is \(g_{\rm prime}\). The full kernel is
\(K_g(t,u)=g(t-u)-g(t)-g(-u)+g(0)\).

### (ii) Metric identity — and the failed decomposition

`[T]` \(K_g\succeq0\) iff \(g\) is a screw function iff there is a
stationary-increment helical map \(x:\mathbb R\to\mathcal H\) with
\[
\langle x(t)-x(0),x(u)-x(0)\rangle=K_g(t,u),\qquad
\|x(t)-x(0)\|^2=-2g(t).
\]
This is the Schoenberg/Krein metric form (up to the displayed factor 2), and
for this \(g\) it is equivalent to RH.

The proposed stronger split “prime part is conditionally negative definite,
archimedean part positive” is **false as stated**. For one symmetric prime atom
\(\delta_a+\delta_{-a}\), the translation-form Fourier multiplier is
\(2\cos(a\xi)\), which changes sign. A positive comb in log-position is not a
positive quadratic convolution operator. Consequently neither component is
semidefinite term-by-term; only the assembled metric can be positive. The W1
identity \(c_{\rm gal}=\mathrm{pole}-\langle\mathcal W,K_d\rangle\) and the
positive-cone blindness result enforce exactly this distinction. L* is an
analogous assembled two-measure comparison, not a proof that raw archimedean
and prime pieces are separately positive/negative operators.

### (iii) Unconditional range and corpus range

The classical explicit range is \(2L\le\log2\), i.e.
\(L\le0.34657359\) for \(\operatorname{supp}f\subset[-L,L]\)
(Yoshida; reinterpreted by Connes–Consani). The corpus-associated preprint
arXiv:`2608.24827` certifies directly from the geometric/prime side
\[
Q(f)\ge8.9\times10^{-18}\|f\|_2^2\quad
(\operatorname{supp}f\subset[-0.8,0.8]),
\]
with a certified upper bound \(2.27\times10^{-17}\). This is 2.3 times the
classical autocorrelation-support range. Since \(2L=1.6\), the prime powers
with \(\log n<1.6\) are \(n=2,3,4\): it is not a “prime 2 only” window.
This is a real finite, RH-neutral partial theorem, but it already exists; no
new probe is created here.

### (iv) Verified zeros are not the mechanism

Platt–Trudgian proved all zeros through
\(H=3\,000\,175\,332\,800\) lie on the line (arXiv:`2004.09765`,
DOI `10.1112/blms.12460`). That theorem does **not** imply positivity on a
whole compact time window. If \(f\) has compact log-support, Paley–Wiener says
\(\widehat f\) is entire of exponential type, not supported in
\([-H,H]\); hypothetical off-line zeros above \(H\) still contribute. Exact
simultaneous compact support and frequency support is impossible for nonzero
\(f\).

Hence there is no finite relation \(T=T(L)\) for the full
\(L^2[-L,L]\) class. The uncertainty scale \(\pi/L\) is only a resolution
scale (at \(L=0.8\), about \(3.93\)), not a spectral cutoff. For a *finite
Galerkin grid* of spacing \(D\), the corpus W3 detector has a genuine alias
band \(\gamma\lesssim\pi/D\); beyond it one needs an explicit tail/operator
bound. The repository does recognize verified-zero inputs in other probes,
but the \(L=0.8\) certificate is independently assembled from primes,
digamma and rigorous matrix/tail bounds. Its truth is not merely inherited
from the Platt–Trudgian height.

### (v) Outcome

No new inequality follows from the screw decomposition. The exact obstruction
is sharper than “positivity above a height is unknown”:

1. the raw prime/archimedean split is not a difference of two semidefinite
   convolution forms;
2. compact-window test functions see all zero heights;
3. finite verified zeros help only after a uniform tail theorem for the
   chosen function class, while uniform W3/W4 or L* is precisely the missing
   operator/metric estimate.

E8 heat-kernel positivity, census-QSM Gibbs positivity and the Gaussian
Fourier fixed point do not supply that estimate; they remain on the blind
Euler side. The observed \(\pi\)-shift sensitivity \(\delta^*=\lambda_{\min}\)
is a conditioning identity at a certified finite window, not a growing-window
lower-bound mechanism.

## S4. Verdict

Es gibt mehrere Objekte nahe an der Zielform: Connes/Meyer liefern den
adelischen Skalierungsraum und eine spektrale Realisierung; Suzuki liefert die
exakte Schraubenfunktion, lokalisierte selbstadjungierte Operatoren und die
kanonische-System-Sprache; Connes–Consani–Moscovici liefern endliche
selbstadjungierte Skalierungsoperatoren mit numerisch passendem Spektrum.
Überall stoppt der Beweis aber am globalen Positivitäts- oder
Konvergenzschritt. Kein akzeptiertes Resultat konstruiert heute einen
Markov/OS-Generator, dessen Spektrum nachweislich genau die Zeta-Ordinaten ist.

Conrey–Li ist eine wichtige Warnung: die natürliche de-Branges-
Verschiebungspositivität scheitert bereits für den zu \(\xi\) gehörenden Raum.
Operatorpositivität kann also echt stärker als RH sein; der Hilbertraum und
die Metrik dürfen nicht nachträglich so gewählt werden, dass Selbstadjungiertheit
die gewünschte Aussage bereits voraussetzt.

Im Corpus ist W1 geschlossen (Suzuki-Identifikation). W2 kontrolliert
Diskretisierung/Domäne und ist nur teilweise geschlossen; uniformes W3 ist die
Positivitätswand, W4 der globale Transfer. In der endlichen Momentensprache ist
L* genau die offene metrische Aussage. Der Konstruktionsversuch erzeugt keinen
neuen Satz: die gewünschte semidefinite Arch-minus-Prim-Zerlegung existiert
nicht, und verifizierte Nullstellen bis \(3\cdot10^{12}\) schneiden kompakt
getragene Tests nicht spektral ab.

**Status Bridge 2: OPEN.** Ein nicht-restatierender nächster Schritt ist eng:
für die bereits konstruierten selbstadjungierten Operatoren
\(D_{\log}^{(\lambda,N)}\) oder Suzukis \(D_{a,\theta}\) eine
geometrisch-prime-seitige, uniform-in-scale resolvent/determinant convergence
with explicit tail norm zu beweisen. Ohne eine solche Normabschätzung wäre ein
weiterer Fenster- oder Euler-Positivitätstest nur eine Wiederholung von W3/L*.
