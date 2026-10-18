# Primes, π, and “reality conformity”

Claim boundary: research documentation only; no claim for or against RH. Tags:
`[T]` classical theorem, `[E]` established corpus statement, `[N]` numerical
measurement, `[I]` interpretation.

## A. Where π sits

### A1. The real place in the explicit formula

Use \(\widehat h(u)=\int_{\mathbb R}h(t)e^{-itu}\,dt\). One standard
Guinand–Weil convention is
\[
\sum_\rho h\!\left(\frac{\rho-\tfrac12}{i}\right)
=h(\tfrac1{2i})+h(-\tfrac1{2i})
+\int_{\mathbb R}\!\left[
 \Re\psi(\tfrac14+\tfrac{it}{2})-\log\pi\right]h(t)\frac{dt}{2\pi}
-\frac1{2\pi}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \{\widehat h(\log n)+\widehat h(-\log n)\}.
\]
The exact placement of \(2\pi\) changes with Fourier convention, not the
finite/infinite-place split. `[T]` The single \(\log\pi\) is from
\(\pi^{-s/2}\); the digamma term is from \(\Gamma(s/2)\); \(dt/(2\pi)\) is the
Plancherel measure. Sources: Weil (1952), Guinand (1948), Edwards (1974).

`[T]` In Tate's thesis, the character \(x\mapsto e^{2\pi i x}\) makes
Lebesgue measure self-dual on \(\mathbb R\), and \(e^{-\pi x^2}\) is
Fourier-self-dual. Its local zeta integral supplies the real-place
\(\Gamma\)-factor. Prime powers \(\log p^k\), weighted by \(\Lambda(p^k)\),
are the finite-place side. Thus “primes ↔ π” has a precise adelic meaning:
finite places balance the real place in an identity.

`[T]` Full Weil positivity on the admissible test class is equivalent to RH.
It can be read as metric domination of the prime contribution by the
archimedean-plus-pole contribution. **Corpus correction:** lemma L* is not
itself the global equivalence. It is the open, finite free-window inequality
\(\int p^2d\nu<\int p^2d\mu\) (`rh/paper/rh_program.tex:774-791`); the corpus
explicitly says extraction to Weil/RH still needs source fidelity, admissible
transport and convergence (`rh/paper/rh_program.tex:1964-2004`). `[E]`

### A2. Classical prime-to-π identities

* `[T]` Euler:
  \(\zeta(2)=\prod_p(1-p^{-2})^{-1}=\pi^2/6\), and
  \(\zeta(2k)\in\pi^{2k}\mathbb Q\).
* `[T]` Leibniz/Euler:
  \(L(1,\chi_{-4})=\prod_p(1-\chi_{-4}(p)/p)^{-1}=\pi/4\).
* `[T]` The class-number formula for \(\mathbb Q(i)\) gives
  \(L(1,\chi_{-4})=2\pi h/(w\sqrt{|d|})=\pi/4\), with
  \(h=1,\ d=-4,\ w=|\mu_4|=4\). The denominator four is literally the
  Gaussian unit group.
* `[T]` \(\sum_{n\le x}r_2(n)\sim\pi x\) (Gauss circle main term);
  Wallis's product and \(\Pr(\gcd(a,b)=1)=1/\zeta(2)=6/\pi^2\) are further
  product/counting appearances of π.

Therefore prime Euler-product data determines π. In particular, a genuine
\(\chi_{-4}\)-signed prime census has value \(\pi/4\) at \(s=1\).

Corpus search: no requested file states \(L(1,\chi_{-4})=\pi/4\), the
\(\mathbb Q(i)\) class-number formula, or the Gauss-circle asymptotic.
`tfpt_1_architecture_e8.tex:4100` mentions \(\pi^2/6\) only as a rejected
numerical coincidence. `[E]` The corpus does contain an exact
\(\chi_{-4}\)/Gaussian split census (`verification/v786_prime_packet480.py:
394-404,555`), while `v537` contains the unrelated level \(32=4\cdot8\)
half-integral bridge (`verification/v537_halfintegral_bridge.py:30,551-554`).
Neither computes the Euler product at \(s=1\). The targeted A2 search found
no `[N]` computation of these identities.

### A3. π in TFPT and the firewall

`[E]/[I]` P1 is declared primitive:
\(c_3=1/(8\pi)\) (`tfpt_1_architecture_e8.tex:160-190`). The corpus then
offers several typed origins/readings:

* one-sided Gauss–Bonnet:
  \(1/(|\mathbb Z_2|\int_{S^2}K\,dA)=1/(2\cdot4\pi)\)
  (`tfpt_1_architecture_e8.tex:1639-1660`);
* four-mark rewrite \(c_3=1/(2\pi d)|_{d=4}\), explicitly **not** a new
  derivation (`tfpt_1_architecture_e8.tex:510-520`);
* lattice/cycle \(8=\operatorname{rank}E_8=\varphi(30)\), plus conditional
  seam–horizon alignment with Einstein/Hawking \(8\pi\)
  (`origin_theory.tex:536-580,650-665`);
* `v53` contains no \(8\pi\) derivation; its docstring derives the integer
  skeleton \(8=5+3\) and \(|\mu_4|=4\)
  (`verification/v53_compiler_core.py:1-29`).

Algebraically,
\[
c_3=\frac1{8\pi}=\frac1{32\,L(1,\chi_{-4})}.
\]
The same integer 32 occurs as a level hypothesis in `v537`. `[I]` No targeted
corpus hit links P1 to \(L(1,\chi_{-4})\), the class-number formula, or
Gaussian units as a derivation. This is a **coincidence**, not a mechanism.
The project firewall requires forced identities, not matches mined from a
rich structure (`tfpt_5_redteam.tex:662-689`), and labels post-hoc alternatives
as look-elsewhere traps (`tfpt_5_redteam.tex:576`).

## B. Precise classifications

* **B1 — THEOREM.** Finite and real places agree through the explicit formula.
  This follows from analytic continuation and the functional equation; it is
  not an extra “reality constraint.”
* **B2 — RH_EQUIVALENT, with scope correction.** Full Weil positivity is RH.
  “Every admissible observer sees archimedean/pole dominance” is a valid
  conformity formulation. Corpus L* is only its open finite-window local
  metric reduction, not a proved global synonym.
* **B3 — INTERPRETATION with THEOREM core.** Log scale is a continuous axis;
  prime powers are discrete events on it. Unique factorisation makes the
  primitive \(\log p\) rationally independent: no finite commensurable clock
  realizes them (`tfpt_prime_front.tex:921-951` `[E]`).
* **B4 — THEOREM.** Prime Euler products determine π, as in A2.
* **B5 — FALSE as a known claim / otherwise UNTESTABLE.** No theorem decodes
  primes from decimal digits of π. Normality of π is unproved.

## C. Numerical measurement

The deterministic probe imports the Legendre machinery of
`weil_window_profile_scout.py:146-465`, uses
\(Q=\mathrm{pole}+\mathrm{arch}-\mathrm{prime}\), and references the independent
\(L=0.8\) certificate \(c=1.0276885835726054\times10^{-17}\).

For \(L=0.50,0.65,0.80\), measured even-sector margins are respectively
\(9.3365673259644\times10^{-7}\),
\(3.9470557473553\times10^{-11}\), and
\(1.6429649175891\times10^{-17}\). Since the basis is orthonormal,
\[
\partial_\delta\lambda_{\min}
=-v^TIv=-\frac1{2\pi}\int|\widehat f_{\min}(t)|^2dt=-1.
\]
Hence the positive \(\log\pi\) crossings equal those margins exactly; negative
\(\delta\) increases \(Q\) and has no crossing. The conservative certified
\(L=0.8\) budget is \(1.0276885835726054\times10^{-17}\).

Scaling the Γ/digamma remainder while holding \(-\log\pi I\) fixed gives
projected first-order crossings \(8.4031787651584\times10^{-6}\),
\(2.1019189641437\times10^{-10}\), and
\(7.0083853843393\times10^{-17}\). These are explicitly not full bisections:
repeated arbitrary-precision eigensolves exceeded the runtime budget; the
omitted correction is second order over the reported \(\lambda_2\) gap.

The positive π-term exceeds the margin by \(10^{6.09},10^{10.46},10^{16.84}\).
The decomposition identity residual is at most \(10^{-61}\). A frozen
same-weight log-position scramble raises the \(L=0.5\) margin to
\(1.5927293\times10^{-5}\), but is already indefinite at \(L=0.65,0.8\)
(\(-0.42659,-0.30344\)): sign/order is world-dependent.

For the first \(10^5\) decimal digits, prime-indicator correlation is
\(r=-0.00300484\), permutation \(p=0.33\); two-digit blocks give
\(r=-0.00262089,p=0.406\). Positive control
\(1_{\mathbb P}(n)\) vs \(\Lambda(n)/\log n\):
\(r=0.998926,p=0.002\). `[N]` Null, as expected.

## D. Synthesis

**Satz.** Die Primdaten bestimmen π durch Eulerprodukte; speziell gilt
\(L(1,\chi_{-4})=\pi/4\), und die Vier ist die Einheitengruppe
\(|\mu_4|\) von \(\mathbb Z[i]\). Die explizite Formel ist die Identität
zwischen endlichen Stellen und der reellen Stelle, deren Γ-Faktor,
\(\log\pi\) und selbstduale Gaußfunktion π tragen.

**RH-Sprache.** RH ist äquivalent zur vollen Weil-Positivität: für jede
zulässige Testfunktion muss die archimedisch/polare Seite die Primseite im
quadratischen Formvergleich beherrschen. Das ist ein präziser
„Konformitäts“-Satz. Das corpus-eigene L* ist jedoch nur die offene,
endliche Fensterreduktion; ohne Quelltreue, Transport und Grenzübergang ist
es nicht die globale RH-Äquivalenz.

**Messung und Firewall.** Der Probe quantifiziert, wie winzig die
Fenstermarge gegenüber dem π-Term ist, prüft eine Scramble-Welt und findet
keine Dezimalziffer→Prim-Korrelation. Das misst Konditionierung, keine
Feinabstimmung der physikalischen π: eine Änderung von π zerstört zunächst
die explizite Formel. \(c_3=1/[32L(1,\chi_{-4})]\) bleibt Numerologie, solange
keine corpus-interne Herleitung den P1-Seammechanismus mit der
\(\chi_{-4}\)-Klassenformel verbindet. Der Corpus enthält beide Zutaten
(\(\mu_4\), \(\chi_{-4}\)-Census) getrennt, aber diese Brücke nicht.
