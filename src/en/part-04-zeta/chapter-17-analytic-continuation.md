---
difficulty = "★★"
prerequisites = ["II-10", "IV-16"]
paths = ["blue", "red"]
keywords = ["analytic continuation", "contour integral", "Hankel", "Riemann", "identity principle"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 17: Analytic Continuation

> Difficulty: ★★ | Paths: 🟡🔴 | Prerequisites: Chapters 10, 16

## The Problem

The Dirichlet series defining $\zeta(s)$ converges only for $\Re(s) > 1$. Yet the Riemann Hypothesis concerns zeros in the critical strip $0 < \Re(s) < 1$. To even speak of such zeros, we must first extend the definition of $\zeta(s)$ to the entire complex plane.

**Analytic continuation** is one of the most powerful tools in complex analysis. The fundamental idea: if a holomorphic function is defined on a sufficiently large region, its extension to the whole complex plane (if it exists) is **unique**. This is the **identity theorem**.

> **Identity Theorem**: If two holomorphic functions agree on a set with a limit point, they are identically equal throughout their connected domain of holomorphy.

This fact — which fails in real analysis (consider the $e^{-1/x^2}$ example from Chapter 8) — means that, given $\zeta(s)$ on the half-plane $\Re(s) > 1$, there is **at most one way** to extend it holomorphically to a larger domain.

## Riemann's Method: Contour Integration

Riemann's original 1859 paper used a contour integral. Consider:

$$
\zeta(s) = \frac{\Gamma(1-s)}{2\pi i} \int_C \frac{(-z)^{s-1}}{e^z - 1} \, dz
$$

where $C$ is the Hankel contour — starting from $+\infty$ just above the positive real axis, circling the origin counterclockwise, and returning to $+\infty$ just below the positive real axis.

The beauty of this representation: **the integral converges for all complex $s \neq 1$**. The factor $\Gamma(1-s)$ has poles at $s = 1, 2, 3, \ldots$, but the contour integral vanishes at those same integers, so the poles cancel — except at $s = 1$. We obtain an analytic continuation of $\zeta(s)$ to the whole complex plane, with a single simple pole at $s = 1$.

## Alternative Continuation Methods

### Alternating Series Continuation

Using the Dirichlet $\eta$ function (the alternating zeta function):

$$
\eta(s) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^s} = (1 - 2^{1-s})\,\zeta(s)
$$

The series for $\eta(s)$ converges (conditionally) for $\Re(s) > 0$. Since the factor $(1 - 2^{1-s})$ is analytic on $\Re(s) > 0$, we can solve:

$$
\zeta(s) = \frac{1}{1 - 2^{1-s}} \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^s} \qquad (\Re(s) > 0, \; s \neq 1)
$$

This already extends the domain from $\Re(s) > 1$ to $\Re(s) > 0$. Further extension requires more sophisticated techniques.

### Continuation via the Functional Equation

The functional equation (Chapter 18) provides the final extension: it explicitly links $\zeta(s)$ to $\zeta(1-s)$. Once $\zeta(s)$ is known on $\Re(s) > 0$, the functional equation automatically gives its values on $\Re(s) < 0$ — covering the entire plane.

## The Global Picture of $\zeta(s)$

After analytic continuation, we have the following global view:

- $s = 1$ is a **simple pole** with residue $1$ — the only pole of $\zeta(s)$
- Near $s = 1$: $\zeta(s) \sim \frac{1}{s-1}$
- On $\Re(s) > 1$: $\zeta(s)$ is given by the original series and Euler product
- Everywhere else: $\zeta(s)$ is defined by analytic continuation — via contour integral, functional equation, or alternating series

## The Trivial Zeros

Upon completing the analytic continuation, we immediately discover that $\zeta(s)$ vanishes at the **negative even integers**:

$$
\zeta(-2) = \zeta(-4) = \zeta(-6) = \cdots = 0
$$

These are the **trivial zeros** of $\zeta(s)$ — "trivial" because their origin (from poles of the Gamma factor in the functional equation) is fully understood and their location is completely known.

But $\zeta(s)$ also possesses infinitely many **non-trivial zeros**, all confined to the critical strip $0 < \Re(s) < 1$. The Riemann Hypothesis is a claim about precisely where in the critical strip these zeros lie.

## Why Analytic Continuation Matters

Without analytic continuation, $\zeta(s)$ is merely a harmless series on a right half-plane — the Prime Number Theorem cannot be proved, and the Riemann Hypothesis cannot be formulated.

Analytic continuation reveals the "hidden part" of $\zeta(s)$ — the non-trivial zeros within the critical strip — and it is these zeros that carry the fine-grained information about prime distribution. In a sense, the series definition $\sum n^{-s}$ is only the "visible surface" of $\zeta(s)$; analytic continuation exposes its deep structure — zeros, poles, growth rates — to the full light of analysis.

---

> **Key points**: The identity theorem guarantees uniqueness of analytic continuation. Riemann first continued $\zeta(s)$ via the Hankel contour integral. $\zeta(s)$ is meromorphic on $\mathbb{C}$ with a single simple pole at $s = 1$ (residue $1$). Negative even integers are the trivial zeros. All non-trivial zeros lie in the critical strip $0 < \Re(s) < 1$ and are the object of the Riemann Hypothesis.

> **See also**: [Chapter 18: The Functional Equation](./chapter-18-functional-equation.md) ★★★
