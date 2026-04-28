---
difficulty = "★"
prerequisites = ["II-08"]
paths = ["blue", "red"]
keywords = ["Riemann integral", "FTC", "improper integral", "Gamma function", "Mellin transform"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 9: Integral Calculus

> Difficulty: ★ | Paths: 🟡🔴 | Prerequisites: Chapter 8

## Two Perspectives on the Integral

The **integral** can be understood in two ways:

1. **Antiderivative**: $F$ is an antiderivative of $f$ if $F'(x) = f(x)$. Then $\int_a^b f(x)\,dx = F(b) - F(a)$.
2. **Riemann sum**: The integral is the limit of sums of areas of rectangles as the rectangles become infinitely thin.

The second perspective was made rigorous by Riemann himself in his 1853 Habilitation thesis — hence the name **Riemann integral**.

## The Rigorous Definition of the Riemann Integral

Partition $[a, b]$ into subintervals: $P = \{x_0, \ldots, x_n\}$ with $a = x_0 < x_1 < \cdots < x_n = b$. In each subinterval $[x_{i-1}, x_i]$, pick any sample point $x_i^*$. The **Riemann sum** is:

$$
S(P, f) = \sum_{i=1}^{n} f(x_i^*) \, \Delta x_i, \quad \Delta x_i = x_i - x_{i-1}
$$

> **Definition**: If there exists a number $I$ such that for every $\varepsilon > 0$ there is $\delta > 0$ for which, whenever the mesh size $\|P\| < \delta$, every Riemann sum (regardless of the choice of sample points) satisfies $|S(P, f) - I| < \varepsilon$, then $f$ is Riemann integrable on $[a, b]$ and $I = \int_a^b f(x)\,dx$.

The beauty of this definition: it allows $f$ to be discontinuous — as long as "bad points" are sparse. A function is Riemann integrable iff its set of discontinuities has measure zero (Lebesgue's criterion).

## The Fundamental Theorem of Calculus (FTC)

The link between differentiation and integration:

> **FTC Part 1**: If $F'(x) = f(x)$ and $f$ is Riemann integrable, then:
> $$
> \int_a^b f(x)\,dx = F(b) - F(a)
> $$

> **FTC Part 2**: If $f$ is continuous on $[a, b]$, define $G(x) = \int_a^x f(t)\,dt$. Then $G'(x) = f(x)$.

The FTC unifies the two great branches of calculus — differential and integral — revealing them as inverse operations.

## Improper Integrals

When the interval is infinite or the integrand has a singularity, we use **improper integrals**, defined via limits:

$$
\int_a^{\infty} f(x)\,dx = \lim_{b \to \infty} \int_a^b f(x)\,dx
$$

For example:
- $\int_1^{\infty} \frac{1}{x^s}\,dx$ converges for $s > 1$ and diverges for $s \leq 1$ — perfectly matching the $p$-series (the integral test in action).
- $\int_0^{\infty} e^{-x} x^{s-1}\,dx$ converges for all $s > 0$ — this is the definition of $\Gamma(s)$.

## The Gamma Function: Generalizing the Factorial

The most important special function in zeta function theory is the **Gamma function**, introduced by Euler in 1729:

$$
\Gamma(s) = \int_0^{\infty} e^{-t} \, t^{s-1} \, dt \qquad (\Re(s) > 0)
$$

The Gamma function extends the factorial from positive integers to complex numbers:

- $\Gamma(n) = (n-1)!$ for positive integers $n$
- $\Gamma(s+1) = s\,\Gamma(s)$ (the functional equation)
- $\Gamma(s)$ can be analytically continued to the whole complex plane, with simple poles at $s = 0, -1, -2, \ldots$

The Gamma function appears in the functional equation of $\zeta(s)$ (Chapter 18), linking $\zeta(s)$ to $\zeta(1-s)$. It is an indispensable tool for understanding the Riemann Hypothesis.

## Integrals and the Mellin Transform

Many special functions have integral representations. $\zeta(s)$ itself does:

$$
\zeta(s) = \frac{1}{\Gamma(s)} \int_0^{\infty} \frac{x^{s-1}}{e^x - 1}\,dx \qquad (\Re(s) > 1)
$$

This type of integral representation belongs to the theory of the **Mellin transform**, widely used in analytic number theory.

---

> **Key points**: The Riemann integral defines "area under the curve" through limits of sums. The Fundamental Theorem of Calculus unifies differentiation and integration. Improper integrals extend the concept to infinite intervals. The Gamma function extends the factorial to complex numbers and plays a central role in the functional equation of $\zeta(s)$.

> **See also**: [Chapter 10: Complex Numbers and Functions](./chapter-10-complex-numbers.md) ★★
