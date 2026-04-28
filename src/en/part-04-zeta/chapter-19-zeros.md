---
difficulty = "★★★"
prerequisites = ["IV-18"]
paths = ["red"]
keywords = ["zeros", "critical strip", "non-trivial zeros", "Hardy", "Selberg", "zero counting"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 19: Zeros of the Zeta Function

> Difficulty: ★★★ | Paths: 🔴 | Prerequisites: Chapter 18

## Two Kinds of Zeros

The zeros of $\zeta(s)$ fall into two categories:

- **Trivial zeros**: located at $s = -2, -4, -6, -8, \ldots$. They arise directly from poles of the Gamma factor in the functional equation. Their positions and multiplicities are completely known and analytically "trivial."
- **Non-trivial zeros**: all remaining zeros. They all lie within the critical strip $0 < \Re(s) < 1$. Chapter 18 explained why they cannot lie outside it.

The Riemann Hypothesis is precisely about the location of the non-trivial zeros: **all non-trivial zeros lie on the critical line $\Re(s) = 1/2$**.

## Symmetries of the Non-trivial Zeros

From the functional equation $\xi(s) = \xi(1-s)$ and Schwarz reflection $\zeta(\bar{s}) = \overline{\zeta(s)}$, non-trivial zeros obey:

- If $\rho$ is a zero, $1 - \rho$ is also a zero (reflection about $\Re = 1/2$)
- If $\rho$ is a zero, $\bar{\rho}$ is also a zero (reflection about the real axis)

Non-trivial zeros thus appear in fours: $\rho$, $\bar{\rho}$, $1-\rho$, $1-\bar{\rho}$. When $\rho$ lies exactly on the critical line, the four merge into two.

## Zero Distribution: The $N(T)$ Function

Let $N(T)$ be the number of non-trivial zeros with imaginary part between $0$ and $T$ (counting multiplicities in the upper half-plane). Riemann gave the asymptotic formula in 1859; von Mangoldt proved it rigorously in 1905:

$$
N(T) = \frac{T}{2\pi} \ln\!\left(\frac{T}{2\pi}\right) - \frac{T}{2\pi} + O(\ln T)
$$

This shows the average density of zeros grows logarithmically with height $T$. The first few non-trivial zeros (computed numerically) are:

$$
\rho_1 \approx \frac{1}{2} + 14.1347i, \quad
\rho_2 \approx \frac{1}{2} + 21.0220i, \quad
\rho_3 \approx \frac{1}{2} + 25.0109i
$$

All have real part $1/2$ — exactly as the Riemann Hypothesis predicts.

## Zeros on the Critical Line

G. H. Hardy (1914) proved a landmark result: $\zeta(s)$ has infinitely many zeros *on* the critical line. While far from "all zeros are on the line," it was the first confirmation that the critical line indeed hosts infinitely many zeros.

**Hardy's Theorem**: $\zeta(1/2 + it) = 0$ for infinitely many $t$.

Atle Selberg (1942) achieved a quantum leap: a **positive proportion** of all non-trivial zeros lie on the critical line.

**Selberg's Theorem**: Let $N_0(T)$ count zeros on the critical line with imaginary part between $0$ and $T$. Then there exists a constant $c > 0$ such that $N_0(T) \geq c\,N(T)$ for all sufficiently large $T$.

The proportion has been improved progressively. The current record (Conrey, 1989) shows: over $40\%$ of non-trivial zeros lie on the critical line.

## The Riemann–von Mangoldt Explicit Formula

Recall the explicit formula previewed in Chapter 15. In terms of $\zeta(s)$'s zeros, the Chebyshev function $\psi(x)$ — hence the prime-counting function $\pi(x)$ — is:

$$
\psi(x) = x - \sum_{\rho} \frac{x^\rho}{\rho} - \ln(2\pi) - \frac{1}{2}\ln(1 - x^{-2})
$$

Each non-trivial zero $\rho = \beta + i\gamma$ contributes an oscillatory term:

$$
-\frac{x^\rho}{\rho} = -\frac{x^\beta}{\rho} \cdot e^{i\gamma \ln x}
$$

The real part $\beta$ controls the **amplitude** of this term; the imaginary part $\gamma$ controls its **oscillation frequency**. Hence:
- If $\beta = 1/2$ (Riemann Hypothesis), each zero contributes an oscillation of amplitude roughly $x^{1/2}$ — the optimal bound
- If any zero had $\beta > 1/2$, the error term in the Prime Number Theorem would be larger than optimal

## The Meaning of the Zeros

Each non-trivial zero is like a note in the symphony of prime numbers. The imaginary part $\gamma$ gives the pitch (frequency); the real part $\beta$ gives the volume (amplitude). The Riemann Hypothesis asserts that all notes have exactly the same volume — $\Re = 1/2$ — so that the prime symphony possesses the most beautiful possible structure.

---

> **Key points**: The zeros of $\zeta(s)$ divide into trivial (negative evens) and non-trivial (within $0 < \Re(s) < 1$). $N(T) \sim \frac{T}{2\pi}\ln(T/2\pi)$ gives the asymptotic zero count. Hardy (1914) proved infinitely many zeros on the critical line; Selberg (1942) proved a positive proportion. The explicit formula expresses $\psi(x)$ as a sum over zeros — each zero contributes an oscillation whose amplitude depends on its real part.

> **See also**: [Chapter 20: Special Values and the Riemann–Siegel Formula](./chapter-20-special-values.md) ★★★
