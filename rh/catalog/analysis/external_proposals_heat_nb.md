# External proposals: heat-normalized Gabor form and dyadic NB capture

Research documentation only. **No claim for or against RH.** The computations are
experiment-only and do not change the verification ledger.

## Prior corpus contact

- The concept map already contains `nyman-beurling-criterion` (3 attempts),
  `baez-duarte-criterion` (2 attempts), and `nyman-beurling-space`.
- `experiments/tfpt-discovery/baez_duarte_probe.py` measured the classical
  Báez-Duarte ladder through \(N=2048\).
- `experiments/tfpt-discovery/beurling_nyman_gram_probe.py` recorded that
  positive Gram/Schur floors point in the wrong direction for an upper bound on
  the NB distance.
- `r605B/r605C` supplies the exposed-orbit separation architecture.
- `r608` measured the Gabor tropical/source budget and stopped the source-side
  lane as RH-strength cancellation. The normalization below corrects its
  cross-lobe heat residual but does not alter that source-budget verdict.

## Claims audit

| Statement | Verified? | Type |
|---|---:|---|
| The cross term cancels in \(\mathcal H=\sqrt a(2G(a,\omega)-e^{-\omega^2/(2a)}G(a,0))\). | Symbolically exact | THEOREM |
| \(a^{-1/2}e^{-(t-\omega)^2/(2a)}\) satisfies \(\partial_a=\frac12\partial_\omega^2\), also for complex \(t\). | Symbolically exact | THEOREM |
| \(G=[\mathcal H(a,\omega)+e^{-\omega^2/(2a)}\mathcal H(a,0)]/(2\sqrt a)\). | Symbolically exact | THEOREM |
| \(\mathcal H=\pi\sqrt{2\pi}\,(K_a*\operatorname{Re}\mu_\zeta)\). | Exact normalization | RESTATEMENT |
| Criterion A is equivalent to the existing exposed-orbit/Gabor positivity criterion. | Same separating exponential | RESTATEMENT |
| The prime saddle has scale \(\sqrt{2\pi/a}\,e^{1/(8a)}\). | PNT/Laplace calculation; finite sums measured | THEOREM + MEASUREMENT |
| The periodic digamma and Vasyunin Gram formulas agree. | 80-digit checks, max error \(2.64\times10^{-82}\) | THEOREM/check |
| The supplied \(E_N,\eta_k\) table is reproduced. | Yes, through all supplied rows | MEASUREMENT |
| Burnol gives the full constant unconditionally. | No: only the critical-line zero sum is unconditional | CORRECTION |
| Under RH and simple zeros, \(E_N\sim(2+\gamma-\log4\pi)/\log N\). | Conditional literature theorem with an additional zeta-derivative hypothesis | THEOREM (conditional) |
| \(\eta_k\ge c/k\). | Not proved | CONJECTURE |

## A. Heat-normalized Gabor form

Let
\[
 K_a(x)=(2\pi a)^{-1/2}e^{-x^2/(2a)},\qquad
 \mu_\zeta=\sum_\rho m_\rho\delta_{t_\rho},
 \quad t_\rho=\gamma-i(\beta-\tfrac12).
\]
After cancellation and pairing the \(\pm\gamma\) terms,
\[
 \mathcal H(a,\omega)
 =\frac{\pi}{\sqrt a}\operatorname{Re}\sum_\rho m_\rho
 e^{-(t_\rho-\omega)^2/(2a)}
 =\pi\sqrt{2\pi}\,(K_a*\operatorname{Re}\mu_\zeta)(\omega).
\]
Thus the heat equation is the ordinary Gaussian semigroup identity. The
statement \(\mathcal H\ge0\) is the existing Gabor/Weil positivity criterion in
heat coordinates, not an additional positivity source.

### Arithmetic budget

`heat_gabor_restatement_probe.py` exactly sums
\[
B_{\rm prime}(a;X)=\sum_{n\le X}\Lambda(n)n^{-1/2}
e^{-a(\log n)^2/2},\qquad X=2\cdot10^7.
\]

| \(a\) | exact partial \(B\) | PNT saddle | \(e^{1/\sqrt a}\) | \(\log(\mathrm{PNT}/\mathrm{slack})\) | PNT tail after \(X\) |
|---:|---:|---:|---:|---:|---:|
| 1/4 | 6.28702320666 | 8.26546270824 | 7.38905609893 | 0.112086 | \(6.53\times10^{-14}\) |
| 1/8 | 17.0801282518 | 19.2721163788 | 16.9188286786 | 0.130232 | \(2.96\times10^{-6}\) |
| 1/16 | 70.6972910416 | 74.0864677617 | 54.5981500331 | 0.305233 | \(1.38\times10^{-2}\) |
| 1/32 | 428.739250714 | 774.181610229 | 286.246763854 | 0.994952 | \(4.43\times10^{-1}\) |

The requested \(10^{-12}\)-relative exact tail is feasible at this cap only for
\(a=1/4\). At \(a=1/32\), the Gaussian PNT tail estimate requires
\(\log X\approx55.79\), far outside the two-minute finite-sieve contract.
Accordingly the other entries are explicitly typed **exact partial sums**.

At \(a=1/4,\omega=0\), the corpus normalization gives pole
41.4368850548, exact-partial prime term 31.5184602662, and archimedean term
\(-9.91842478862\), leaving \(2.70\times10^{-12}\). The first-zero-pair
zero-side sanity magnitude is \(7.32\times10^{-173}\). This zero datum is used
only to display cancellation depth. It shows why a finite source evaluation
cannot certify the tiny full form: pole, prime, and archimedean terms must
cancel far beyond their individual precision.

An off-line displacement \(\sigma\) contributes \(e^{\sigma^2/(2a)}\), with
\(\sigma^2\le1/4\), while the prime saddle reaches \(e^{1/(8a)}\). Criterion A
therefore asks for cancellation of \(a^{-1}\)-exponential source terms down to
\(e^{1/\sqrt a}\) precision. This is the same zero-free content exposed by
`r605`/`r608`, not a reduction in hardness. **Verdict A: RESTATED.**

## B. Dyadic Nyman--Beurling capture

For \(r_n(x)=\{1/(nx)\}-n^{-1}\{1/x\}\),
\(\langle1,r_n\rangle=\log(n)/n\). The periodic digamma sum for
\(\langle r_m,r_n\rangle\) agrees with the BBLS/Vasyunin cotangent formula.
Moreover \(u_n=2r_{2n}-r_n\) is the stated odd-block indicator and
\(\langle1,u_n\rangle=\|u_n\|^2=\log2/n\).

| \(N\) | \(E_N\) | \(\eta_k\) | \(k\eta_k\) | condition number |
|---:|---:|---:|---:|---:|
| 8 | 0.024244525307 | 0.0639854156 | 0.1919562468 | \(5.37\times10^1\) |
| 16 | 0.017936267020 | 0.1007401959 | 0.4029607835 | \(3.08\times10^2\) |
| 32 | 0.014077011415 | 0.1200395213 | 0.6001976066 | \(1.74\times10^3\) |
| 64 | 0.011392474680 | 0.1152003874 | 0.6912023245 | \(8.08\times10^3\) |
| 128 | 0.009670345448 | 0.1252601699 | 0.8768211893 | \(3.82\times10^4\) |
| 256 | 0.008242256028 | 0.0906767057 | 0.7254136455 | \(1.67\times10^5\) |
| 512 | 0.007393375337 | 0.1104454847 | 0.9940093619 | \(7.24\times10^5\) |

The mean of \(E_N\log N\) over the last three rows is 0.046249285476,
1.001253 times
\[
C_{\rm BD}=2+\gamma-\log(4\pi)=0.046191417932.
\]
Burnol's unconditional statement is the safer
\[
\liminf E_N\log N\ge
\sum_{\Re\rho=1/2}\frac{m(\rho)^2}{|\rho|^2}.
\]
Only under RH and simple zeros does this sum become \(C_{\rm BD}\). Bettin,
Conrey and Farmer obtain the expected asymptotic under RH plus a growth
condition on \(1/\zeta'(\rho)\).

The block conjecture is not literally just the Báez-Duarte rate conjecture:
it additionally says that a specified dyadic subspace captures a harmonic
fraction of the residual. It implies a polynomial decay in \(k=\log_2N\), and
therefore RH, but no such lower bound is proved. The finite sequence
\(k\eta_k\) oscillates \(0.192,\ldots,0.994\). **Verdict B: MEASURED.**

Proving \(\eta_k\ge c/k\) would require a uniform lower bound for the
projection of the residual \(R_N\) onto the residualized dyadic block span.
Equivalently, one must control the Schur complement built from the explicit
Vasyunin Gram matrix and prevent the residual/block correlations from
collapsing as conditioning worsens.

## Literature placement

- L. Báez-Duarte, “A strengthening of the Nyman-Beurling criterion,”
  *Rend. Lincei Mat. Appl.* 14 (2003), 5–11:
  <https://eudml.org/doc/252348>.
- J.-F. Burnol, “A lower bound in an approximation problem involving the
  zeros of the Riemann zeta function,” *Adv. Math.* 170 (2002), 56–70:
  <https://doi.org/10.1006/aima.2001.2066>.
- S. Bettin, J. B. Conrey, D. W. Farmer, “An optimal choice of Dirichlet
  polynomials for the Nyman-Beurling criterion”:
  <https://doi.org/10.1134/S0081543813030036>.
- B. Landreau, F. Richard, “Le critère de Beurling et Nyman ... aspects
  numériques,” *Experimental Mathematics* 11 (2002), 349–360:
  <https://projecteuclid.org/euclid.em/1057777427>.
- V. I. Vasyunin, “On a biorthogonal system related to the Riemann
  hypothesis,” *Algebra i Analiz* 7 (1995), 118–135; later cotangent-form
  context: <https://arxiv.org/abs/1111.0931>.
- No searched source used the exact block \(u_n=2r_{2n}-r_n\). This is an
  absence-of-hit report, not a novelty or priority claim.
- Gaussian testing is a standard smooth explicit-formula operation; the local
  corpus instances are `weil_gabor_explicit_formula_probe.py`, `r605`, and
  `r608`.

## Deutsches Urteil (unter 200 Wörter)

Beide Vorschläge liefern vor allem klarere Koordinaten, keine neue Information
in Richtung RH. Vorschlag A entfernt tatsächlich ein Artefakt aus `r608`: Nach
der richtigen Linearkombination verschwindet der Kreuzterm exakt, und
\(\mathcal H\) ist schlicht die Gauß-geglättete reelle Nullstellenverteilung
mit dem Faktor \(\pi\sqrt{2\pi}\). Damit wird die Wärmegleichung transparent.
Die Schwierigkeit bleibt jedoch unverändert: Auf der Primseite müssen
Terme der Größe \(\exp(1/(8a))\) bis auf eine wesentlich kleinere Skala
\(\exp(1/\sqrt a)\) auslöschen. Das ist genau die Nullstellenfreiheit in
anderer Darstellung.

Vorschlag B ist mathematisch besser als Forschungsvertrag geeignet. Die
Größen sind rein arithmetisch, die Geometrie ist positiv, die Gram-Matrix ist
explizit, und die Zahlen reproduzieren sich. Trotzdem impliziert jede
harmonische Untergrenze \(\eta_k\ge c/k\) bereits \(E_N\to0\) und damit RH.
Sie ist also kein leichter Zwischensatz. Empfehlung: als eingefrorenen,
experimentellen Vertrag aufnehmen, ausdrücklich als offene stärkere
Block-Capture-Vermutung. Der konkrete Beweisbedarf ist eine uniforme
Projektionsuntergrenze für den Residualvektor gegen den dyadischen Block über
die Vasyunin-Schurstruktur.
