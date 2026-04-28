---
difficulty = "★★"
prerequisites = ["II-06"]
paths = ["blue", "red"]
keywords = ["infinite product", "Euler product", "Weierstrass factorization", "convergence"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 11: Infinite Products

> Difficulty: ★★ | Paths: 🟡🔴 | Prerequisites: Chapter 6

## Infinity Through Multiplication

We have become comfortable with infinite series — adding infinitely many numbers. An **infinite product** multiplies infinitely many numbers:

$$
P = \prod_{n=1}^{\infty} a_n = a_1 \cdot a_2 \cdot a_3 \cdot \cdots
$$

Convergence is defined through **partial products**:

$$
P_N = \prod_{n=1}^{N} a_n, \qquad \prod_{n=1}^{\infty} a_n = \lim_{N \to \infty} P_N
$$

As with series, there is a subtle convention: **if the limit is $0$, we say the product diverges to zero.** This preserves the algebraic property that a product is zero only if a factor is zero — products like $\prod (1 - \frac{1}{n})$ tend to zero but no individual factor is zero.

### Convergence Criterion

Writing each factor as $a_n = 1 + u_n$, the product $\prod (1 + u_n)$ converges (to a non-zero limit) if and only if $\sum |u_n|$ converges. This simple test is usually sufficient:

- $\prod_{n=2}^{\infty} \left(1 - \frac{1}{n^2}\right) = \frac{1}{2}$ (converges)
- $\prod_{n=2}^{\infty} \left(1 - \frac{1}{n}\right)$ diverges to zero

## The Euler Product: The Central Identity of the Zeta Function

In 1737, Euler discovered one of the most stunning identities in analysis — a formula linking an infinite sum over *all integers* to an infinite product over *all primes*:

$$
\sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}} \qquad (\operatorname{Re}(s) > 1)
$$

The left side is $\zeta(s)$ as a series — the sum of reciprocal $s$-th powers of all positive integers. The right side is an infinite product over primes $p = 2, 3, 5, 7, 11, \ldots$. This identity connects **addition** (sum over integers) with **multiplication** (product over primes) in a profoundly deep way.

### Proof Sketch

Expand each factor $(1 - p^{-s})^{-1}$ as a geometric series:

$$
\frac{1}{1 - p^{-s}} = 1 + p^{-s} + p^{-2s} + p^{-3s} + \cdots
$$

When you multiply these expansions over all primes, the Fundamental Theorem of Arithmetic (unique prime factorization of integers) guarantees that every term $n^{-s}$ appears exactly once. The product therefore equals $\sum_{n=1}^{\infty} n^{-s} = \zeta(s)$.

The Euler product is the cornerstone of analytic number theory. It shows that all information about the distribution of primes is encoded in the analytic properties of $\zeta(s)$ — particularly in the location of its zeros.

## An Immediate Corollary: Infinitude of Primes (Analytic Proof)

As $s \to 1^+$, the series $\sum n^{-s}$ diverges (it approaches the harmonic series), so the product $\prod (1 - p^{-s})^{-1}$ must diverge. If there were only finitely many primes, this product would be finite — contradiction. Therefore, there are infinitely many primes.

This argument differs fundamentally from Euclid's classical proof. It uses analytic methods (divergence), making it a paradigm of analytic number theory.

## Regularizing Divergent Products

Sometimes a divergent product can be given a meaningful "value." For $\prod_p (1 - p^{-1})^{-1}$ (as $s \to 1^+$), the precise rate of divergence is given by Mertens' theorem:

$$
\prod_{p \leq x} \left(1 - \frac{1}{p}\right) \sim \frac{e^{-\gamma}}{\ln x}
$$

where $\gamma \approx 0.5772$ is the Euler-Mascheroni constant — the same constant that appears in the Laurent expansion of $\zeta(s)$ at $s=1$.

## General Infinite Products: The Weierstrass Factorization

A deep theorem in complex analysis is the **Weierstrass factorization theorem**: every entire function (a function holomorphic on the whole complex plane) can be expressed as an infinite product determined by its zeros. For example, the product representation of sine:

$$
\sin(\pi z) = \pi z \prod_{n=1}^{\infty} \left(1 - \frac{z^2}{n^2}\right)
$$

Comparing this product with the Taylor expansion $\sin(\pi z) = \pi z - \frac{(\pi z)^3}{6} + \cdots$, Euler derived $\zeta(2) = \pi^2/6$. Riemann used essentially the same technique — product representations involving the Gamma function and the zeta function — in his derivation of the functional equation.

## Connection to the Riemann Hypothesis

The Euler product converges only for $\operatorname{Re}(s) > 1$. But through **analytic continuation** (Chapter 17), $\zeta(s)$ is extended to the entire complex plane. In the critical strip $0 < \operatorname{Re}(s) < 1$, the behavior of $\zeta(s)$ is governed by its zeros — zeros that are linked, through the Euler product, to the distribution of primes.

This is the essence of Riemann's 1859 paper: **study the analytic properties and zero locations of $\zeta(s)$ in the complex plane, to obtain the most precise possible information about prime numbers.**

---

> **Key points**: Infinite products converge when the corresponding series of $|u_n|$ converges. Euler's product $\zeta(s) = \prod_p (1-p^{-s})^{-1}$ connects addition (the series over integers) to multiplication (the product over primes) and is the foundation of analytic number theory. The Weierstrass factorization theorem represents entire functions via their zeros — a technique central to the functional equation of $\zeta(s)$.

> **Continue to**: [Part III: Analytic Number Theory Foundations](../part-03-analytic-nt/chapter-12-prime-history.md) ★
