---
difficulty = "★"
prerequisites = []
paths = ["green", "blue", "red"]
keywords = ["real numbers", "limits", "epsilon-delta", "convergence", "Cauchy"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 5: Real Numbers and Limits

> Difficulty: ★ | Paths: 🟢🟡🔴 | Prerequisites: None

## From Rationals to Reals

The first mathematical concept needed to understand the Riemann Hypothesis is the **limit**. And limits rest on an even deeper foundation: what exactly is a real number?

### The World of Rationals

Rational numbers — numbers expressible as fractions $\frac{p}{q}$ where $p$ and $q$ are integers with $q \neq 0$ — form a world that seems complete at first glance. Between any two rationals there is always another (take their average). This property is called **density**: the rationals are packed densely along the number line.

Yet the ancient Greeks already discovered that the rational world has "holes."

### The Discovery of $\sqrt{2}$

Consider the diagonal of a unit square. By the Pythagorean theorem, its length $d$ satisfies $d^2 = 1^2 + 1^2 = 2$, so $d = \sqrt{2}$.

The Pythagoreans proved a startling result: $\sqrt{2}$ is **not** rational.

**Proof** (by contradiction): Suppose $\sqrt{2} = \frac{p}{q}$ where $p$ and $q$ are coprime integers. Squaring both sides: $2 = p^2/q^2$, so $p^2 = 2q^2$. Thus $p^2$ is even, so $p$ is even. Write $p = 2k$, substitute: $4k^2 = 2q^2$, so $2k^2 = q^2$. Thus $q$ is even. But this contradicts $p, q$ being coprime. $\square$

$\sqrt{2}$ is not rational, yet as a length it clearly exists. This reveals gaps between the rationals — irrational numbers.

### Constructing the Reals (Intuitive Description)

The real number system fills all the gaps. Intuitively, every real number can be represented as an infinite decimal:

$$
\pi = 3.1415926535\ldots
$$

This infinite decimal defines the number exactly — not an approximation. A finite decimal cannot capture $\pi$ precisely, but the infinite expansion does.

More rigorously, the reals can be constructed via **Dedekind cuts** or **equivalence classes of Cauchy sequences**. Both constructions guarantee that the real numbers are **complete** — every bounded, monotone increasing sequence has a limit.

## Limits: The First Building Block of Analysis

### Limits of Sequences

Consider the sequence:

$$
a_n = \frac{1}{n}: \quad 1,\; \frac{1}{2},\; \frac{1}{3},\; \frac{1}{4},\; \ldots
$$

As $n$ grows, $a_n$ gets arbitrarily close to $0$. We say the **limit** of this sequence is $0$, written:

$$
\lim_{n \to \infty} \frac{1}{n} = 0
$$

### The $\varepsilon$-$N$ Definition

Intuition needs precision. What exactly does "arbitrarily close" mean?

> **Definition**: A sequence $\{a_n\}$ has limit $L$ if, for every positive number $\varepsilon > 0$, there exists a positive integer $N$ such that whenever $n > N$, we have $|a_n - L| < \varepsilon$.

In words: **no matter how close you want to get to $L$ (that's $\varepsilon$), from some point onward (from $N$ on), all terms of the sequence are within that distance.**

For $a_n = 1/n$: to ensure $|1/n - 0| < \varepsilon$, choose $N > 1/\varepsilon$. For $\varepsilon = 0.001$, take $N = 1000$.

### The $\varepsilon$-$\delta$ Definition: Limits of Functions

For a function $f(x)$ as $x$ approaches a point $a$, the limit is $L$, written:

$$
\lim_{x \to a} f(x) = L
$$

The rigorous $\varepsilon$-$\delta$ definition:

> For every $\varepsilon > 0$, there exists $\delta > 0$ such that whenever $0 < |x - a| < \delta$, we have $|f(x) - L| < \varepsilon$.

This is one of the most important definitions in all of analysis. It captures the notion of "approaching" with complete precision.

## Basic Properties of Limits

- **Sum**: $\lim (a_n + b_n) = \lim a_n + \lim b_n$ (when both limits exist)
- **Product**: $\lim (a_n \cdot b_n) = \lim a_n \cdot \lim b_n$
- **Quotient**: $\lim \frac{a_n}{b_n} = \frac{\lim a_n}{\lim b_n}$ (when the denominator limit is non-zero)

These rules let us compute limits of complicated expressions without returning to $\varepsilon$-$\delta$ every time.

## Important Limits

### Defining $e$

One of the most important constants in mathematics, $e \approx 2.71828\ldots$, can be defined via a limit:

$$
e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n
$$

The existence of this limit follows from the monotone bounded principle. Euler's formula $e^{i\pi} + 1 = 0$ links $e$, $i$, and $\pi$, connecting exponential growth to circles — a connection that runs through the entire theory of the zeta function.

### The Harmonic Series: When Limits Don't Exist

The series $1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots$ has terms that tend to zero, yet its partial sums grow without bound:

$$
\lim_{n \to \infty} \sum_{k=1}^{n} \frac{1}{k} = \infty
$$

A beautiful proof (due to the 14th-century scholar Oresme): group terms so each group's sum exceeds $\frac{1}{2}$:

$$
1 + \frac{1}{2} + \underbrace{\left(\frac{1}{3} + \frac{1}{4}\right)}_{> \frac{1}{2}} + \underbrace{\left(\frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8}\right)}_{> \frac{1}{2}} + \cdots
$$

Infinitely many groups, each larger than $\frac{1}{2}$, so the sum is infinite.

The harmonic series is intimately related to the Riemann zeta function: $\zeta(s) = \sum_{n=1}^{\infty} n^{-s}$. At $s=1$, it is the harmonic series — divergent. For $s > 1$, the series converges. And $s$ can be complex — which is where the story of $\zeta(s)$ truly begins.

## Limits and the Riemann Hypothesis

Limits are the fundamental tool throughout our journey:

- Convergence of series (Chapters 6, 11)
- The definition of analytic continuation (Chapter 17)
- The asymptotic distribution of zeros (Chapters 19, 23)
- The asymptotic formula for $\pi(x)$ (Chapter 15)

The next chapter takes up **series** — sums of infinitely many terms — the bridge from elementary mathematics to the zeta function.

---

> **Key points**: Real numbers complete the rationals by filling all "gaps," making limit operations well-founded. The $\varepsilon$-$\delta$ definition gives precise meaning to limits. Classic examples — $e$, the harmonic series — illustrate the power of limit arguments. Limits are the gateway to analysis and, ultimately, to the Riemann Hypothesis.

> **See also**: [Chapter 6: Sequences and Series](./chapter-06-sequences-series.md) ★
