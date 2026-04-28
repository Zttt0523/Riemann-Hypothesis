---
difficulty = "★★"
prerequisites = ["III-13", "III-14"]
paths = ["green", "blue", "red"]
keywords = ["prime number theorem", "PNT", "Chebyshev", "Hadamard", "de la Vallée Poussin", "psi"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 15: The Prime Number Theorem

> Difficulty: ★★ | Paths: 🟢🟡🔴 | Prerequisites: Chapters 13, 14

## Statement of the Prime Number Theorem

The **Prime Number Theorem** (PNT) is the crowning achievement of nineteenth-century analytic number theory — and, before the Riemann Hypothesis, the greatest result in the field.

Let $\pi(x)$ denote the number of primes not exceeding $x$:

$$
\pi(x) = \#\{p \leq x : p \text{ is prime}\}
$$

> **Prime Number Theorem**:
> $$
> \pi(x) \sim \frac{x}{\ln x} \qquad (x \to \infty)
> $$
> That is, $\lim_{x \to \infty} \frac{\pi(x)}{x / \ln x} = 1$.

A more refined version uses the **logarithmic integral**:

$$
\operatorname{Li}(x) = \int_2^x \frac{dt}{\ln t}
$$

$\operatorname{Li}(x)$ is a better approximation than $x/\ln x$, and PNT is equivalently expressed as $\pi(x) \sim \operatorname{Li}(x)$.

## From Gauss to Chebyshev

Gauss and Legendre conjectured the PNT in the late eighteenth century, but neither could prove it. The first substantial progress came from Pafnuty Chebyshev around 1850, who showed that *if* the limit $\lim_{x \to \infty} \frac{\pi(x)}{x/\ln x}$ exists, then it must be $1$.

Chebyshev also proved bounds: $\pi(x)$ is sandwiched between constant multiples of $x/\ln x$. He introduced the **Chebyshev functions** that became standard technical tools:

$$
\vartheta(x) = \sum_{p \leq x} \ln p, \qquad \psi(x) = \sum_{p^k \leq x} \ln p = \sum_{n \leq x} \Lambda(n)
$$

PNT is equivalent to the statement that $\psi(x) \sim x$.

## Two Key Lemmas

The 1896 proofs of PNT rest on two facts about $\zeta(s)$.

**Lemma 1**: $\zeta(s)$ has no zeros on the line $\operatorname{Re}(s) = 1$.

That is, $\zeta(1 + it) \neq 0$ for all real $t$. This is the crucial technical heart of the PNT.

**Lemma 2**: $\zeta(s)$ has a simple pole at $s = 1$ with residue $1$. In a neighborhood of $s = 1$:

$$
\zeta(s) \sim \frac{1}{s-1}
$$

The first fact is number-theoretic — it prevents the prime distribution from having a systematic bias. The second fact is analytic — it determines the "leading term" of the prime distribution.

## Proof Strategy

Using Perron's formula (Chapter 14), $\psi(x)$ is expressed as a complex integral:

$$
\psi(x) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \left(-\frac{\zeta'(s)}{\zeta(s)}\right) \frac{x^s}{s} \, ds, \quad c > 1
$$

Shift the integration contour leftward. As it moves, contributions arise from:

1. The pole of $-\zeta'(s)/\zeta(s)$ at $s = 1$ (from $\zeta(s)$'s simple pole), with residue $1$, contributing the main term $x$
2. The pole at $s = 0$, contributing a constant
3. **Each non-trivial zero $\rho$ of $\zeta(s)$**, contributing an oscillatory term $\frac{x^\rho}{\rho}$
4. **Trivial zeros** ($s = -2, -4, -6, \ldots$), contributing negligible small terms

The result is **Riemann's explicit formula**:

$$
\psi(x) = x - \sum_{\rho} \frac{x^\rho}{\rho} - \ln(2\pi) - \frac{1}{2}\ln(1 - x^{-2})
$$

## What Prevents a Stronger Conclusion?

Hadamard and de la Vallée Poussin used only the fact that $\zeta(1+it) \neq 0$, not the full Riemann Hypothesis (which asserts that only zeros with $\operatorname{Re}(s) = 1/2$ matter).

Because $\zeta(1+it) \neq 0$ is a weaker statement, the error bound is weaker: $\pi(x) = \operatorname{Li}(x) + O(x e^{-c\sqrt{\ln x}})$.

If the Riemann Hypothesis were true, the error term would sharpen dramatically: $\pi(x) = \operatorname{Li}(x) + O(\sqrt{x} \ln x)$. And conversely — **the Riemann Hypothesis is equivalent to the error term in the Prime Number Theorem being $O(x^{1/2+\varepsilon})$**.

## The Significance of PNT

The proof of the Prime Number Theorem was one of the great achievements of nineteenth-century mathematics. It demonstrated that:

1. Analytic methods (complex analysis) can solve purely discrete problems in number theory
2. Riemann's intuition — studying primes via complex functions — was a stroke of profound genius
3. The zeros of $\zeta(s)$ precisely govern the fine structure of the prime distribution

But PNT also reveals *why* the Riemann Hypothesis matters. PNT answers: "Roughly how many primes are there?" The Riemann Hypothesis would answer: "Precisely how are the primes distributed?"

---

> **Key points**: The Prime Number Theorem $\pi(x) \sim x/\ln x$ was proved independently by Hadamard and de la Vallée Poussin in 1896. The key technical step is showing $\zeta(s) \neq 0$ on $\operatorname{Re}(s) = 1$. Perron's formula and the Chebyshev function $\psi(x)$ are the central technical tools. PNT gives a "first-order" approximation; the Riemann Hypothesis is equivalent to the sharpest possible error bound $O(x^{1/2+\varepsilon})$.

> **Continue to**: [Part IV: The Riemann Zeta Function](../part-04-zeta/chapter-16-zeta-definition.md) ★★
