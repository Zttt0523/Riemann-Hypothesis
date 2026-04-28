---
difficulty = "★★"
prerequisites = ["II-06", "III-13"]
paths = ["blue", "red"]
keywords = ["Dirichlet series", "abscissa", "Euler product", "Mellin", "Perron formula"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 14: Dirichlet Series

> Difficulty: ★★ | Paths: 🟡🔴 | Prerequisites: Chapters 6, 13

## What Is a Dirichlet Series?

A **Dirichlet series** is an infinite series of the form:

$$
F(s) = \sum_{n=1}^{\infty} \frac{a_n}{n^s}
$$

where $s$ is a complex variable and $a_n$ is a sequence of complex numbers. This is the central type of series in analytic number theory.

When all $a_n = 1$, $F(s) = \sum n^{-s} = \zeta(s)$ — the Riemann zeta function is the most basic Dirichlet series.

## Convergence of Dirichlet Series

Unlike power series, whose domain of convergence is a disk, the natural convergence domain of a Dirichlet series is a **half-plane**.

> **Theorem**: There exists a real number $\sigma_c$ (the **abscissa of convergence**) such that the Dirichlet series converges for $\Re(s) > \sigma_c$ and diverges for $\Re(s) < \sigma_c$.

For $\zeta(s) = \sum n^{-s}$, $\sigma_c = 1$ (the $p$-series converges for $s > 1$ and diverges for $s \leq 1$).

For a general Dirichlet series, $\sigma_c$ depends on the growth of the coefficients $a_n$. Roughly, if $a_n$ grows no faster than some power $n^A$, then $\sigma_c \leq A + 1$.

### Absolute Convergence Abscissa

There is also an **absolute convergence abscissa** $\sigma_a$, with $\sigma_c \leq \sigma_a \leq \sigma_c + 1$. For $\zeta(s)$, $\sigma_c = \sigma_a = 1$, but the two can differ — for example, $\sum (-1)^{n-1} n^{-s}$ converges (conditionally) for $\Re(s) > 0$ but converges absolutely only for $\Re(s) > 1$.

## Multiplication and Euler Products

The most important algebraic property of Dirichlet series: convolution of coefficients corresponds to multiplication of series. If:

$$
F(s) = \sum_{n=1}^{\infty} \frac{f(n)}{n^s}, \quad G(s) = \sum_{n=1}^{\infty} \frac{g(n)}{n^s}
$$

then:

$$
F(s) G(s) = \sum_{n=1}^{\infty} \frac{(f * g)(n)}{n^s}
$$

where $f * g$ is Dirichlet convolution. This property is the algebraic source of the Euler product: when $f$ is multiplicative, $F(s)$ factorizes over primes.

For example, the Dirichlet series of $\mu$ is:

$$
\sum_{n=1}^{\infty} \frac{\mu(n)}{n^s} = \frac{1}{\zeta(s)} \qquad (\Re(s) > 1)
$$

This relation follows directly from the Euler product and shows how the Möbius function and $\zeta(s)$ are linked through Dirichlet series.

## Perron's Formula: Extracting Coefficients from Series

One of the most powerful technical tools in analytic number theory is **Perron's formula**. It uses a complex integral to "extract" the partial sum of coefficients from a Dirichlet series:

$$
\sum_{n \leq x} a_n = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} F(s) \frac{x^s}{s} \, ds
$$

where the integral is taken along the vertical line $\Re(s) = c$ (with $c > \sigma_a$).

The basic strategy for applying Perron's formula:
1. Start from a Dirichlet series (e.g., $\zeta(s)$ or a related function)
2. Shift the integration contour leftward, past the poles of the integrand
3. The contributions left behind come from the poles (singularities) and branch cuts

The interplay between zeros, poles, and integration contours is the technical foundation of every "explicit formula" in analytic number theory — including Riemann's explicit formula for $\pi(x)$.

## Key Example: von Mangoldt's Series

The Dirichlet series of the von Mangoldt function is:

$$
-\frac{\zeta'(s)}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\Lambda(n)}{n^s}
$$

The Prime Number Theorem is then equivalent to $\psi(x) = \sum_{n \leq x} \Lambda(n) \sim x$. Via Perron's formula, this becomes a complex-analytic study of the poles of $-\zeta'/\zeta$ — which are determined by the zeros of $\zeta(s)$.

**The structural framework of the Riemann Hypothesis is now visible**:

$$
\text{Primes} \xleftrightarrow[]{\text{Perron}} \text{$\zeta'/\zeta$} \xleftrightarrow[]{\text{poles = zeros}} \text{Zeros of $\zeta(s)$} \xleftrightarrow[]{\text{RH}} \text{$\Re(\rho) = 1/2$}
$$

---

> **Key points**: Dirichlet series $\sum a_n n^{-s}$ converge in half-planes. Multiplicative coefficients yield Euler product representations. Perron's formula recovers coefficient sums from Dirichlet series via complex contour integration. The logarithmic derivative $-\zeta'/\zeta$ has coefficients $\Lambda(n)$, linking primes directly to the analytic properties of $\zeta(s)$.

> **See also**: [Chapter 15: The Prime Number Theorem](./chapter-15-pnt.md) ★★
