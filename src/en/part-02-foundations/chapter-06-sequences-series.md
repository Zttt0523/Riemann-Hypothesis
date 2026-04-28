---
difficulty = "★"
prerequisites = ["II-05"]
paths = ["green", "blue", "red"]
keywords = ["series", "convergence", "geometric series", "p-series", "zeta function"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 6: Sequences and Series

> Difficulty: ★ | Paths: 🟢🟡🔴 | Prerequisites: Chapter 5

## What Is a Series?

A **series** is the sum of infinitely many numbers:

$$
S = a_1 + a_2 + a_3 + \cdots = \sum_{n=1}^{\infty} a_n
$$

What does it mean to add infinitely many things? Chapter 5's concept of the limit provides the answer: define the **partial sums** $S_N = \sum_{n=1}^{N} a_n$ and examine their limit:

$$
\sum_{n=1}^{\infty} a_n = \lim_{N \to \infty} S_N = \lim_{N \to \infty} \sum_{n=1}^{N} a_n
$$

If this limit exists and is finite, the series **converges**; otherwise it **diverges**.

## The Geometric Series

The most fundamental convergent series is the **geometric series**, in which each term is multiplied by a constant ratio $r$:

$$
\sum_{n=0}^{\infty} r^n = 1 + r + r^2 + r^3 + \cdots
$$

The partial sum has the closed form $S_N = \frac{1 - r^{N+1}}{1 - r}$ (for $r \neq 1$). Hence:

$$
\sum_{n=0}^{\infty} r^n = \frac{1}{1 - r} \quad\text{if and only if}\quad |r| < 1
$$

For $|r| \geq 1$, the series diverges.

**Examples**: $\sum_{n=0}^{\infty} \frac{1}{2^n} = 2$ (the mathematical resolution of Zeno's paradox); $\sum_{n=0}^{\infty} \frac{1}{3^n} = \frac{3}{2}$.

## $p$-Series and the First Encounter with $\zeta$

The most important type of series in number theory is the **$p$-series**:

$$
\sum_{n=1}^{\infty} \frac{1}{n^s}
$$

where $s$ is a real number. The convergence of this series depends on $s$:

- **$s > 1$**: The series converges. For $s=2$, Euler (1734) proved $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$ — the famous Basel problem.
- **$s \leq 1$**: The series diverges. At $s=1$, this is the harmonic series.

This series is the original definition of the Riemann zeta function:

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (s > 1)
$$

When $s$ is a real number greater than $1$, $\zeta(s)$ is a finite value. But this is only the beginning — later, we will extend $s$ into the complex domain.

### The Basel Problem

Euler's solution of $\zeta(2) = \pi^2/6$ is a milestone in the history of analysis. Comparing the infinite product expansion of $\frac{\sin x}{x}$ with its Taylor series:

$$
\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \cdots = \prod_{n=1}^{\infty} \left(1 - \frac{x^2}{n^2 \pi^2}\right)
$$

and matching the $x^2$ coefficients yields $\frac{1}{6} = \sum \frac{1}{n^2 \pi^2}$, hence $\zeta(2) = \frac{\pi^2}{6}$.

This elegant technique was later generalized by Riemann to connect the zeta function with the product over primes — the Euler product.

## Convergence Tests

For a general series $\sum a_n$, how do we determine convergence?

### The Comparison Test

If $0 \leq a_n \leq b_n$ for all sufficiently large $n$, then:
- $\sum b_n$ converges $\Rightarrow$ $\sum a_n$ converges
- $\sum a_n$ diverges $\Rightarrow$ $\sum b_n$ diverges

### The Integral Test

If $f(x)$ is positive and decreasing, then $\sum_{n=1}^{\infty} f(n)$ and $\int_1^{\infty} f(x)\,dx$ converge or diverge together.

This gives an elegant proof of the $p$-series convergence criterion: $\int_1^{\infty} x^{-s}\,dx$ converges precisely when $s > 1$.

### The Ratio Test

Compute $\rho = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|$:
- $\rho < 1$: absolute convergence
- $\rho > 1$: divergence
- $\rho = 1$: inconclusive

## Absolute vs. Conditional Convergence

A crucial distinction:

- **Absolute convergence**: $\sum |a_n|$ converges. The series is unconditionally well-behaved; rearranging terms does not change its sum.
- **Conditional convergence**: $\sum a_n$ converges but $\sum |a_n|$ diverges. The alternating harmonic series $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots = \ln 2$ is a classic example.

Remarkably, Riemann himself proved that the terms of any conditionally convergent series can be rearranged to sum to *any* real number — the **Riemann rearrangement theorem**.

## Connection to the Riemann Zeta Function

The $p$-series $\sum n^{-s}$ is the starting point for $\zeta(s)$. In the real domain $s > 1$, the properties of $\zeta(s)$ are relatively straightforward. The real magic begins in Part IV — when we extend $s$ to the complex plane and deploy the full power of complex analysis. The deep secrets of the primes begin to emerge.

But first, we need the machinery: continuity (Chapter 7), calculus (Chapters 8-9), and the theory of complex numbers (Chapter 10).

---

> **Key points**: A series converges when its sequence of partial sums approaches a finite limit. The geometric series and $p$-series are the two most fundamental types. The $p$-series is $\zeta(s)$ in its original real-variable definition. Convergence tests — comparison, integral, ratio — are the practical tools for analyzing series behavior.

> **See also**: [Chapter 7: Functions and Continuity](./chapter-07-functions-continuity.md) ★
