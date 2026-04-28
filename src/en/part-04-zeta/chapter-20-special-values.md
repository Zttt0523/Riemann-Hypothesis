---
difficulty = "★★★"
prerequisites = ["IV-18"]
paths = ["red"]
keywords = ["special values", "Riemann-Siegel", "zeta on critical line", "Hardy Z-function", "universality"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 20: Special Values and the Riemann–Siegel Formula

> Difficulty: ★★★ | Paths: 🔴 | Prerequisites: Chapter 18

## Special Values on the Real Axis

Chapter 16 gave $\zeta(2n)$ for positive even integers:

$$
\zeta(2n) = (-1)^{n+1} \frac{B_{2n} (2\pi)^{2n}}{2(2n)!}
$$

The functional equation also yields values at negative integers:

$$
\zeta(1 - 2n) = -\frac{B_{2n}}{2n} \qquad (n \geq 1)
$$

Thus: $\zeta(-1) = -1/12$ (the famously "controversial" sum of all natural numbers), $\zeta(-3) = 1/120$, $\zeta(-5) = -1/252$. Note: these are values assigned by analytic continuation, not by any convergent series — the series $\sum n$ is, of course, divergent.

For **positive odd integers**, the situation is profoundly different. $\zeta(3)$ was proved irrational by Apéry in 1978. Whether $\zeta(5), \zeta(7), \ldots$ are irrational remains open. It is known that infinitely many positive odd zeta values are irrational — but *which* ones is not known.

## $\zeta(s)$ on the Critical Line

The central stage for the Riemann Hypothesis is the critical line $\operatorname{Re}(s) = 1/2$. Along this line, $\zeta(1/2 + it)$ is a complex-valued function of the real variable $t$.

Define the **Hardy $Z$-function**:

$$
Z(t) = e^{i\theta(t)} \, \zeta\!\left(\frac{1}{2} + it\right), \qquad
\theta(t) = \arg\left[\pi^{-it/2} \, \Gamma\!\left(\frac{1}{4} + \frac{it}{2}\right)\right]
$$

The $Z(t)$ function has remarkable properties:
- $Z(t)$ is **real-valued** when defined this way
- The zeros of $Z(t)$ correspond exactly to the zeros of $\zeta(s)$ on the critical line
- $|Z(t)| = |\zeta(1/2 + it)|$

$Z(t)$ is the fundamental tool for numerical verification of the Riemann Hypothesis. If $Z(t)$ changes sign at some height $t$, then $\zeta(s)$ has a zero on the critical line near that height.

## The Riemann–Siegel Formula

In 1932, Carl Ludwig Siegel made a dramatic discovery while studying Riemann's surviving unpublished notes in the Göttingen University Library. Among the fragments not burned by the housekeeper, Siegel found that Riemann had developed an efficient numerical method for computing $\zeta(1/2 + it)$ — the **Riemann–Siegel formula**:

$$
Z(t) \approx 2\sum_{n=1}^{\lfloor \sqrt{t/(2\pi)} \rfloor} \frac{\cos(\theta(t) - t \ln n)}{\sqrt{n}} + R(t)
$$

where $R(t)$ is an asymptotic error term. The computational cost scales as roughly $\sqrt{t}$ — vastly more efficient than summing $t$ terms directly. It was with this formula that Riemann, computing by hand, calculated the first several non-trivial zeros to high precision.

Siegel published the complete derivation in 1932. H. M. Edwards, in his classic *Riemann's Zeta Function* (1974), wrote of this discovery: "Riemann had kept these computations secret for over seventy years, and they revealed a numerical technique whose sophistication was far beyond anyone else of his time."

## Numerical Verification

Since Riemann's day, digital computers have calculated astronomical numbers of $\zeta$ zeros — and every one has lain on the critical line. As of the 2020s, over $10^{13}$ zeros have been verified to satisfy $\operatorname{Re}(s) = 1/2$. The only "off-critical-line" zeros would represent computer errors, and **no counterexample has ever been found**.

This overwhelming numerical evidence is among the most compelling arguments for the truth of the Riemann Hypothesis — but it is not a proof. The history of mathematics offers cautionary examples: a conjecture may hold for $10^{10}$ instances yet ultimately be false.

The Riemann–Siegel formula is still used today in high-precision zero computations. Mathematical insight from a century and a half ago lives on in modern supercomputers.

## Universality of $\zeta(s)$

In 1975, the Soviet mathematician Sergei Voronin proved a remarkable theorem: $\zeta(s)$ exhibits **universality** within the critical strip. Roughly, *any* "well-behaved" analytic function can be approximated to arbitrary precision by appropriately shifted copies of $\zeta(s)$. This means the graph of $\zeta(s)$ contains, within it, all possible analytic behavior — a single function encompassing the full complexity of mathematics.

---

> **Key points**: $\zeta(-1) = -1/12$ and other negative integer values are linked to Bernoulli numbers via the functional equation. The Hardy $Z(t)$-function is the real-valued tool for studying $\zeta$ on the critical line. The Riemann–Siegel formula computes $Z(t)$ in $\sim\sqrt{t}$ steps — secretly discovered by Riemann, published by Siegel in 1932. Over $10^{13}$ zeros have been verified on the critical line. Voronin's universality theorem shows $\zeta(s)$ contains all possible analytic behavior.

> **Continue to**: [Part V: The Riemann Hypothesis — Into the Core](../part-05-rh/chapter-21-statement-history.md) ★★
