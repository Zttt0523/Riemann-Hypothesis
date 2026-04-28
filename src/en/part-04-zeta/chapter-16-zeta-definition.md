---
difficulty = "★★"
prerequisites = ["III-14"]
paths = ["blue", "red"]
keywords = ["zeta function", "Dirichlet series", "Euler product", "integral representation", "Mellin"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 16: Definition and Elementary Properties of $\zeta(s)$

> Difficulty: ★★ | Paths: 🟡🔴 | Prerequisites: Chapter 14

## Definition

The Riemann zeta function is defined initially as a Dirichlet series (Chapter 14):

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (\Re(s) > 1)
$$

When $s$ is a real number $> 1$, this is the familiar $p$-series (Chapter 6). When $s$ is complex — Riemann's first key insight in 1859 — $n^{-s} = e^{-s\ln n}$, and $\zeta(s)$ becomes a function of a complex variable.

## Convergence

The series defining $\zeta(s)$ converges absolutely on the half-plane $\Re(s) > 1$. When $\Re(s) \leq 1$, the series diverges.

Absolute convergence means we may rearrange terms without changing the sum — but more importantly, it implies $\zeta(s)$ is **holomorphic** (Chapter 10) on $\Re(s) > 1$. We may differentiate term by term:

$$
\zeta'(s) = -\sum_{n=1}^{\infty} \frac{\ln n}{n^s}, \quad
\zeta''(s) = \sum_{n=1}^{\infty} \frac{(\ln n)^2}{n^s}, \ldots
$$

## The Euler Product

On $\Re(s) > 1$, $\zeta(s)$ possesses the Euler product representation (Chapter 11):

$$
\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}
$$

Taking logarithms (principal branch):

$$
\ln \zeta(s) = \sum_{p} \sum_{k=1}^{\infty} \frac{1}{k \, p^{ks}}
$$

This is the bridge between addition (integers) and multiplication (primes). The product form is valid only on $\Re(s) > 1$ — cross that line, enter the critical strip, and $\zeta(s)$'s behavior is governed by the global properties of its analytic continuation.

## Values of $\zeta(s)$ on the Real Axis

When $s > 1$ is real, $\zeta(s)$ takes elegant values. Euler (1734) first computed:

$$
\zeta(2) = \frac{\pi^2}{6} \approx 1.6449
$$

More generally, for positive even integers:

$$
\zeta(2n) = (-1)^{n+1} \frac{B_{2n} (2\pi)^{2n}}{2(2n)!}
$$

where $B_{2n}$ are Bernoulli numbers: $B_2 = \frac{1}{6}, B_4 = -\frac{1}{30}, B_6 = \frac{1}{42}, \ldots$

Hence: $\zeta(4) = \frac{\pi^4}{90}, \zeta(6) = \frac{\pi^6}{945}, \ldots$

For **odd positive integers**, the situation is starkly different. $\zeta(3)$ (Apéry's constant) was proved irrational only in 1978. Whether $\zeta(5), \zeta(7), \ldots$ are irrational remains open.

## Divergence at $s = 1$

As $s \to 1^+$ from the right, $\zeta(s)$ diverges:

$$
\zeta(s) \sim \frac{1}{s-1} \qquad (s \to 1^+)
$$

More precisely, near $s = 1$ there is a Laurent expansion:

$$
\zeta(s) = \frac{1}{s-1} + \gamma + \gamma_1 (s-1) + \cdots
$$

where $\gamma \approx 0.5772$ is the Euler-Mascheroni constant.

## Integral Representations

$\zeta(s)$ has multiple integral representations linking it to the Gamma function (Chapter 9):

$$
\zeta(s) = \frac{1}{\Gamma(s)} \int_0^{\infty} \frac{x^{s-1}}{e^x - 1} \, dx \qquad (\Re(s) > 1)
$$

This follows from the geometric series $\frac{1}{e^x - 1} = \sum_{n=1}^{\infty} e^{-nx}$ and termwise integration.

This representation is important because it can be extended, via contour integration techniques, to the entire complex plane — precisely the starting point of Riemann's 1859 paper.

## $\zeta(s)$ and the Primes

Information about primes is extracted from $\zeta(s)$ through the logarithmic derivative of the Euler product:

$$
-\frac{\zeta'(s)}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\Lambda(n)}{n^s}
$$

Recall (Chapter 13): $\Lambda(n)$ is the von Mangoldt function — $\ln p$ when $n = p^k$, zero otherwise. This formula is the direct channel linking the analytic properties of $\zeta(s)$ to prime distribution.

## A First Glimpse: The Numerical Face of $\zeta(s)$

On the real axis $s > 1$, $\zeta(s)$ is a smooth, monotonically decreasing function, starting from the pole at $s = 1$ and asymptotically approaching $1$ (since $\zeta(s) \to 1$ as $s \to \infty$).

But extending our gaze into the complex plane, $\zeta(s)$ reveals behavior of extraordinary richness and complexity. Chapter 17 takes up the task of extending this function — defined so far only by a series on $\Re(s) > 1$ — to the entire complex plane: analytic continuation, perhaps the most powerful operation in all of complex analysis.

---

> **Key points**: $\zeta(s) = \sum n^{-s}$ converges absolutely on $\Re(s) > 1$, defining a holomorphic function there. The Euler product links addition (over integers) to multiplication (over primes). At positive even integers, $\zeta(2n)$ is expressible in closed form via Bernoulli numbers; values at odd integers remain mysterious. Integral representations connect $\zeta(s)$ to $\Gamma(s)$. The logarithmic derivative $-\zeta'/\zeta$ has coefficients $\Lambda(n)$.

> **See also**: [Chapter 17: Analytic Continuation](./chapter-17-analytic-continuation.md) ★★
