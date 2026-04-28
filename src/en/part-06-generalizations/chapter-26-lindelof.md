---
difficulty = "★★★"
prerequisites = ["IV-19"]
paths = ["red"]
keywords = ["Lindelöf Hypothesis", "growth", "critical line", "subconvexity", "convexity bound"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 26: The Lindelöf Hypothesis

> Difficulty: ★★★ | Paths: 🔴 | Prerequisites: Chapter 19

## RH's "Little Cousin"

The Lindelöf Hypothesis is often called the Riemann Hypothesis's "little cousin" — its conclusion is weaker, but the two are intimately related: **RH implies Lindelöf, but the converse may be false**.

Lindelöf concerns the growth rate of $\zeta(s)$ on the critical line — a statement about the *magnitude* of function values, rather than the *location* of zeros.

## Statement

> **Lindelöf Hypothesis**: For every $\varepsilon > 0$,
> $$
> \zeta\!\left(\frac{1}{2} + it\right) = O(t^{\varepsilon}) \qquad (t \to \infty)
> $$

In words: the value of $\zeta$ on the critical line grows slower than any positive power of $t$. Equivalently, for every $\varepsilon > 0$ there exists a constant $C_\varepsilon$ such that $|\zeta(1/2 + it)| \leq C_\varepsilon \, t^\varepsilon$ for all sufficiently large $t$.

## Relationship to RH

RH implies Lindelöf. Under RH, the bound can actually be sharpened to $\zeta(1/2 + it) = O(\exp(c \ln t / \ln\ln t))$.

But Lindelöf does **not** imply RH. It is possible that Lindelöf is true — $\zeta$ on the critical line grows extremely slowly — while some zeros still deviate from the critical line. This makes Lindelöf a more approachable target for independent study.

## Known Bounds: Convexity and Subconvexity

**The convexity bound**: a general argument from the Phragmén–Lindelöf principle in complex analysis gives:

$$
\zeta\!\left(\frac{1}{2} + it\right) = O(t^{1/4})
$$

This is the "generic" bound requiring no extra input.

**Weyl's subconvexity bound**: Hermann Weyl improved this to:

$$
\zeta\!\left(\frac{1}{2} + it\right) = O(t^{1/6 + \varepsilon})
$$

Weyl's argument uses a delicate exponential sum estimate. Subsequent improvements have pushed the exponent further down.

The current record, due to Bourgain (2017):

$$
\zeta\!\left(\frac{1}{2} + it\right) = O(t^{13/84 + \varepsilon}) \approx O(t^{0.1548})
$$

The halfway point from the convexity bound's $1/4$ to Lindelöf's $0$ has been more than crossed.

## Significance

The Lindelöf Hypothesis is important beyond its link to RH:

- It is equivalent to strong results on the vertical spacing of $\zeta$ zeros
- It plays a central role in the subconvexity problem for automorphic $L$-functions — one of the most active areas of modern analytic number theory
- It is the simplest instance of the "subconvexity problem" family in number theory, where the convexity bound is a "free" estimate from basic complex analysis and subconvexity requires deep arithmetic input

Extraordinary progress on subconvexity problems has been made in the last two decades, with some of the deepest breakthroughs coming from Zhang Wei, Kowalski, Michel, and Venkatesh.

---

> **Key points**: The Lindelöf Hypothesis asserts $\zeta(1/2+it) = O(t^\varepsilon)$. RH implies Lindelöf but not conversely. The convexity bound $O(t^{1/4})$ has been improved via subconvexity techniques to Bourgain's $O(t^{0.1548})$. Lindelöf is part of the broader "subconvexity problem" family in number theory.

> **See also**: [Chapter 27: L-Functions and the Selberg Class](./chapter-27-l-functions.md) ★★★
