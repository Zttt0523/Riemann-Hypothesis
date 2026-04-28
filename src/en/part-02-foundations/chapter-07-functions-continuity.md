---
difficulty = "★"
prerequisites = ["II-05"]
paths = ["blue", "red"]
keywords = ["function", "continuity", "epsilon-delta", "IVT", "uniform continuity"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 7: Functions and Continuity

> Difficulty: ★ | Paths: 🟡🔴 | Prerequisites: Chapter 5

## Functions: From Intuition to Formalism

A **function** is the fundamental object of analysis. It maps each element of a set (the domain) to a unique element of another set (the codomain). Functions can be given by formulas ($f(x) = x^2$), graphs, tables, or as solutions to differential equations — but analysis studies their **analytic properties**: continuity, differentiability, integrability.

## The $\varepsilon$-$\delta$ Definition of Continuity

Intuitively, a function is continuous if its graph has no breaks. The formal definition refines this:

> **Definition**: $f$ is continuous at $a$ if, for every $\varepsilon > 0$, there exists $\delta > 0$ such that when $|x - a| < \delta$, we have $|f(x) - f(a)| < \varepsilon$.

In words: **small changes in input produce small changes in output**. Notice that continuity at $a$ is precisely equivalent to $\lim_{x \to a} f(x) = f(a)$.

If $f$ is continuous at every point in its domain, we simply say $f$ is a continuous function.

## Elementary Functions Are Continuous

Every elementary function is continuous on its domain: polynomials, rational functions (where the denominator is non-zero), $\sin x$, $\cos x$, $e^x$, $\ln x$ (for $x > 0$). Sums, products, quotients (non-zero denominator), and compositions of continuous functions remain continuous.

## Fundamental Theorems of Continuous Functions

### The Intermediate Value Theorem (IVT)

> If $f$ is continuous on $[a, b]$, and $y$ is any number between $f(a)$ and $f(b)$, then there exists $c \in (a, b)$ such that $f(c) = y$.

This is one of the most intuitively natural properties of continuity: a continuous function cannot skip values. The IVT is the theoretical basis for solving equations by bisection.

### The Extreme Value Theorem

> A continuous function on a closed interval attains its maximum and minimum.

The "closed interval" condition is necessary. On the open interval $(0, 1)$, $f(x) = \frac{1}{x}$ is unbounded; even $f(x) = x$ on $(0, 1)$ fails to attain its supremum of $1$.

## Uniform Continuity

Ordinary continuity is defined point by point: given $a$ and $\varepsilon$, we find $\delta$. This $\delta$ may depend on both $\varepsilon$ and $a$.

**Uniform continuity** requires more: $\delta$ must depend on $\varepsilon$ alone — a single "global $\delta$" works everywhere in the domain.

> **Theorem** (Heine-Cantor): A continuous function on a closed interval is uniformly continuous.

Uniform continuity is important because it is a sufficient condition for Riemann integrability.

## Continuity in the Broader Mathematical Landscape

Continuity extends directly to more abstract spaces. For complex functions, the definition is virtually identical — merely replace the absolute value $|x-a|$ with the complex modulus $|z-a|$.

**Holomorphic functions** — the central objects of complex analysis — are a far stronger notion than mere continuity. A function that is once complex-differentiable is automatically infinitely differentiable and equal to its Taylor series. Riemann's doctoral thesis established the foundations of this theory.

The leap from continuity to holomorphicity in the complex domain is a kind of "magic threshold" — once crossed, properties that fail in real analysis (a differentiable function whose derivative is discontinuous; an infinitely differentiable function that is not analytic) become impossible. This magic is the engine that will drive our study of $\zeta(s)$.

---

> **Key points**: The $\varepsilon$-$\delta$ definition of continuity captures the intuitive idea of "no jumps" with complete precision. The Intermediate Value Theorem and Extreme Value Theorem are the fundamental properties of continuous functions on closed intervals. The gap between real continuity and complex holomorphicity is one of the deepest structural facts in all of analysis.

> **See also**: [Chapter 8: Differential Calculus](./chapter-08-differential-calculus.md) ★
