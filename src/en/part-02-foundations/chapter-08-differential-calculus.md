---
difficulty = "★"
prerequisites = ["II-07"]
paths = ["blue", "red"]
keywords = ["derivative", "Taylor series", "mean value theorem", "power series", "analytic"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 8: Differential Calculus

> Difficulty: ★ | Paths: 🟡🔴 | Prerequisites: Chapter 7

## The Derivative: Instantaneous Rate of Change

The **derivative** captures how fast a function changes at a point.

> **Definition**: The derivative of $f$ at $a$ is:
> $$
> f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h}
> $$
> provided the limit exists.

Geometrically, the derivative is the slope of the tangent line. The difference quotient $\frac{f(a+h)-f(a)}{h}$ is the slope of a secant line; as $h \to 0$, the secant becomes the tangent.

### Basic Derivatives

| Function | Derivative |
|----------|-----------|
| $x^n$ | $n x^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |

Together with the sum, product, quotient, and **chain rules** — $\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$ — these form the computational engine of calculus.

## The Mean Value Theorem

> **Lagrange's Mean Value Theorem**: If $f$ is continuous on $[a, b]$ and differentiable on $(a, b)$, then there exists $c \in (a, b)$ such that:
> $$
> f'(c) = \frac{f(b) - f(a)}{b - a}
> $$

At some interior point, the instantaneous rate of change equals the average rate over the whole interval. The MVT is the starting point for countless analytic arguments, including the proof that positive derivative implies monotonic increase.

## Taylor Series: Approximating Functions by Polynomials

One of the most powerful applications of differentiation is the **Taylor expansion**. If $f$ is infinitely differentiable at $a$, we can expand it as a power series:

$$
f(x) = f(a) + f'(a)(x-a) + \frac{f''(a)}{2!}(x-a)^2 + \frac{f'''(a)}{3!}(x-a)^3 + \cdots
$$

**Fundamental Taylor expansions**:

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$

$$
\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!}
$$

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots = \sum_{n=1}^{\infty} (-1)^{n+1} \frac{x^n}{n} \quad (|x| < 1)
$$

Taylor series are profound because they represent functions as **power series** — "infinite polynomials" — allowing algebraic methods to be applied to transcendental objects.

## Power Series and Analytic Functions

A **power series** is an expression $\sum_{n=0}^{\infty} a_n (x - c)^n$. Every power series has a **radius of convergence** $R$: it converges for $|x-c| < R$ and diverges for $|x-c| > R$.

A function representable by a convergent power series near any point in its domain is called **analytic**.

Here is where real and complex analysis diverge profoundly. In real analysis, differentiability does **not** imply analyticity. The function:

$$
f(x) = \begin{cases} e^{-1/x^2} & x \neq 0 \\ 0 & x = 0 \end{cases}
$$

is infinitely differentiable at $0$, with all derivatives equal to $0$. Its Taylor series at $0$ is identically zero — yet $f(x) \neq 0$ for $x \neq 0$. The Taylor series fails to recover the function.

**In complex analysis: one complex derivative implies analyticity.** Once $f'(z)$ exists in a neighborhood, $f$ is automatically infinitely differentiable and equals its Taylor series. This is the single most important structural difference between real and complex function theory — and it is the mathematical foundation for everything that follows about $\zeta(s)$.

## Calculus and the Zeta Function

Derivatives and Taylor expansions play essential roles in $\zeta(s)$ theory:

- $\zeta'(s)$ encodes information about zero distribution
- Derivation of the functional equation involves derivatives of the Gamma function
- The Riemann-Siegel formula is a kind of asymptotic expansion of $\zeta(s)$ along the critical line

These topics return in Part IV.

---

> **Key points**: The derivative captures instantaneous rate of change. The Mean Value Theorem is a cornerstone of analytic reasoning. Taylor expansions represent functions as infinite polynomials. The crucial difference between real and complex analysis — complex differentiability implies analyticity — is the foundation on which zeta function theory rests.

> **See also**: [Chapter 9: Integral Calculus](./chapter-09-integral-calculus.md) ★
