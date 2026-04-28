---
difficulty = "★★"
prerequisites = ["II-06"]
paths = ["blue", "red"]
keywords = ["arithmetic function", "Möbius", "Dirichlet convolution", "Mertens", "multiplicative"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 13: Arithmetic Functions

> Difficulty: ★★ | Paths: 🟡🔴 | Prerequisites: Chapter 6

## Definition and Examples

An **arithmetic function** is a function whose domain is the positive integers and whose codomain is the complex (or real) numbers. They are the basic vocabulary of number theory.

| Function | Symbol | Definition |
|----------|--------|------------|
| Divisor function | $d(n)$ | Number of positive divisors of $n$ |
| Sum-of-divisors | $\sigma(n)$ | Sum of all positive divisors of $n$ |
| Euler's totient | $\varphi(n)$ | Count of integers $\leq n$ coprime to $n$ |
| Möbius function | $\mu(n)$ | $0$ if $n$ has a squared prime factor; otherwise $(-1)^k$ |
| von Mangoldt function | $\Lambda(n)$ | $\ln p$ if $n = p^k$; $0$ otherwise |
| Constant function | $\mathbf{1}(n)$ | $1$ for all $n$ |

Among these, the **Möbius function** $\mu(n)$ and the **von Mangoldt function** $\Lambda(n)$ occupy center stage in analytic number theory — and in the theory of $\zeta(s)$.

## Multiplicative Functions

An arithmetic function $f$ is **multiplicative** if, for coprime $m, n$:

$$
f(mn) = f(m)f(n) \quad \text{when} \quad \gcd(m, n) = 1
$$

$\varphi(n)$, $\mu(n)$, and $\sigma(n)$ are all multiplicative. The values of a multiplicative function are completely determined by its values at prime powers — and this is the source of their power.

## Möbius Inversion

The **Möbius function** is defined as:

$$
\mu(n) = \begin{cases}
1 & n = 1 \\
(-1)^k & n \text{ is the product of } k \text{ distinct primes} \\
0 & n \text{ has a squared prime factor}
\end{cases}
$$

First few values: $\mu(1) = 1$, $\mu(2) = -1$, $\mu(3) = -1$, $\mu(4) = 0$, $\mu(5) = -1$, $\mu(6) = 1$, $\ldots$

The fundamental property of $\mu$: for $n > 1$,

$$
\sum_{d \mid n} \mu(d) = 0
$$

This deceptively simple identity encodes the **Möbius inversion formula**:

$$
g(n) = \sum_{d \mid n} f(d) \iff f(n) = \sum_{d \mid n} \mu(d) \, g\!\left(\frac{n}{d}\right)
$$

Möbius inversion is intimately connected to the inclusion-exclusion principle and is a cornerstone of combinatorial number theory.

## Dirichlet Convolution

The natural algebraic operation on arithmetic functions is **Dirichlet convolution**:

$$
(f * g)(n) = \sum_{d \mid n} f(d) \, g\!\left(\frac{n}{d}\right)
$$

It is commutative, associative, and has an identity $\varepsilon(n) = \lfloor 1/n \rfloor$. Crucially, $\mu * \mathbf{1} = \varepsilon$ — the Möbius function and the constant function are convolution inverses. Möbius inversion then becomes simply $g = f * \mathbf{1} \iff f = g * \mu$.

## Connection to $\zeta(s)$

The deep link between arithmetic functions and $\zeta(s)$ runs through Dirichlet series (the subject of Chapter 14). In preview:

- The Dirichlet series of the constant function $\mathbf{1}$ is $\zeta(s) = \sum n^{-s}$
- **The Dirichlet series of $\mu(n)$ is the reciprocal of $\zeta(s)$**: $\sum_{n=1}^{\infty} \frac{\mu(n)}{n^s} = \frac{1}{\zeta(s)}$. This follows directly from the Euler product.
- The Dirichlet series of $\Lambda(n)$ is the logarithmic derivative: $\sum \frac{\Lambda(n)}{n^s} = -\frac{\zeta'(s)}{\zeta(s)}$

This last relation is the technical heart of the classical proof of the Prime Number Theorem.

---

> **Key points**: Arithmetic functions map integers to complex numbers. The Möbius function's inversion property ($\mu * \mathbf{1} = \varepsilon$) is the fundamental tool of combinatorial number theory. Dirichlet convolution is the "multiplication" of arithmetic functions. The Dirichlet series of $\mu(n)$ and $\Lambda(n)$ are directly linked to $\zeta(s)$ and its derivative.

> **See also**: [Chapter 14: Dirichlet Series](./chapter-14-dirichlet-series.md) ★★
