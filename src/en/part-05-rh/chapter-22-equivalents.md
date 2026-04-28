---
difficulty = "★★★"
prerequisites = ["V-21"]
paths = ["red"]
keywords = ["equivalent formulations", "Weil explicit formula", "Li criterion", "Hilbert-Pólya", "operator theory"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 22: Equivalent Formulations

> Difficulty: ★★★ | Paths: 🔴 | Prerequisites: Chapter 21

## The Many Faces of the Riemann Hypothesis

One of the RH's great fascinations is that it can be equivalently restated in the language of multiple, seemingly unrelated mathematical domains. No two equivalent formulations look "the same" — their equivalence itself reflects some deep underlying structure.

## Prime Distribution Equivalence

The most fundamental equivalence (Chapter 21):

**RH** $\iff$ $\pi(x) = \operatorname{Li}(x) + O(\sqrt{x} \ln x)$

More precisely, RH is equivalent to the statement that for every $\varepsilon > 0$:

$$
|\pi(x) - \operatorname{Li}(x)| < \frac{1}{8\pi} \sqrt{x} \ln x \quad \text{for all } x \geq 2657
$$

## Mertens Function Equivalence

The Mertens function $M(x) = \sum_{n \leq x} \mu(n)$ is intimately linked to RH. In 1897, Mertens himself conjectured $|M(x)| < \sqrt{x}$ — a statement that would imply RH. In 1985, Odlyzko and te Riele disproved Mertens' conjecture in its strong form, though the counterexamples occur at astronomically large $x$.

The exact equivalence: RH $\iff$ $M(x) = O(x^{1/2 + \varepsilon})$ for every $\varepsilon > 0$.

## The Li Criterion (1997)

Define $\lambda_n = \sum_{\rho} [1 - (1 - 1/\rho)^n]$, summing over non-trivial zeros of $\zeta(s)$. The Chinese mathematician Xian-Jin Li proved in 1997:

**RH** $\iff$ $\lambda_n \geq 0$ for all positive integers $n$

The elegance of the Li criterion lies in transforming a statement about the real parts of complex numbers into a statement about the non-negativity of a real sequence.

## The Hilbert–Pólya Conjecture

In the early twentieth century, Hilbert and Pólya independently suggested: find a self-adjoint (Hermitian) operator $H$ on a Hilbert space whose spectrum (eigenvalues) corresponds to the non-trivial zeros of $\zeta(s)$. Since eigenvalues of self-adjoint operators are real, this would prove RH.

This conjecture is the genesis of the "physical proof" approach to RH. In quantum mechanics, observables are represented by self-adjoint operators, and their spectra (energy levels) are real. Finding such an operator $H$ would interpret $\zeta$ zeros as the energy levels of some quantum system.

## The Connection to Random Matrix Theory

In 1972, Hugh Montgomery and Freeman Dyson met over tea at the Institute for Advanced Study and made a stunning discovery: the pair correlation of $\zeta$ zeros matches exactly the eigenvalue pair correlation of random Hermitian matrices (the Gaussian Unitary Ensemble, or GUE).

This connection (explored fully in Chapter 29) strongly supports the Hilbert–Pólya conjecture: if the GUE connection is more than coincidence, there exists an operator whose eigenvalues behave like $\zeta$ zeros — and that operator would be self-adjoint.

## Weil's Explicit Formula

André Weil (1952) formulated a general explicit formula relating primes, $\zeta$ zeros, and test functions in the language of distributions:

$$
\sum_{\rho} \hat{h}(\rho) = h(0) + h(1) - \sum_{p} \sum_{k=1}^{\infty} \frac{\ln p}{p^{k/2}} \left[h(k \ln p) + h(-k \ln p)\right]
$$

where $\hat{h}$ is the Mellin transform of the test function $h$.

Weil's formula reveals: **RH is equivalent to the non-negativity of a certain positive-definite functional**. This observation connects RH to Connes' noncommutative geometry approach (Chapter 25).

## A Map of Equivalent Forms

| Domain | Equivalence | Keywords |
|--------|-------------|----------|
| Prime distribution | Optimal error bound | $\pi(x) - \operatorname{Li}(x)$ |
| Möbius function | Growth of $M(x)$ | $O(x^{1/2+\varepsilon})$ |
| Functional analysis | Hilbert–Pólya | Self-adjoint operator |
| Algebraic number theory | Generalized RH | L-functions |
| Integral theory | Li criterion | $\lambda_n \geq 0$ |
| Random matrices | GUE statistics | Zero spacings |

All these equivalences tell the same story: **RH is not merely a claim about the zeros of $\zeta(s)$ — it is a deep unifying principle connecting primes, operators, matrices, and quantum chaos.**

---

> **Key points**: RH has multiple equivalent formulations spanning prime distribution, Möbius function growth, Li's criterion, the Hilbert–Pólya operator conjecture, and Weil's explicit formula. The Hilbert–Pólya conjecture links RH to the spectrum of a self-adjoint operator, inspiring a physical approach. The Montgomery–Dyson tea-time encounter revealed a deep connection between $\zeta$ zero spacings and random matrix eigenvalues. RH is a unifying principle across multiple mathematical domains.

> **See also**: [Chapter 23: Zero-Free Regions](./chapter-23-zero-free-regions.md) ★★★
