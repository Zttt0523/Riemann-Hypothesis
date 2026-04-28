---
difficulty = "★★"
prerequisites = ["IV-19", "V-21"]
paths = ["green", "blue", "red"]
keywords = ["computation", "zeros", "Turing", "ZetaGrid", "Odlyzko", "Riemann-Siegel"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 31: Computational Verification

> Difficulty: ★★ | Paths: 🟢🟡🔴 | Prerequisites: Chapters 19, 21

## From Riemann's Hand Calculation to Supercomputers

In the final section of his 1859 paper, Riemann used his new formula — now called the Riemann–Siegel formula (Chapter 20) — to compute by hand the imaginary parts of the first several non-trivial zeros of $\zeta(s)$. He calculated three zeros, at heights approximately $14.13$, $21.02$, and $25.01$. For the fourth zero, he merely stated that "the next is even closer to $1/2$."

Riemann's hand calculations proved astonishingly accurate. When Hutchinson recomputed them with more precise methods in 1925, he confirmed Riemann's values to four decimal places. A century and a half later, we know that Riemann correctly located every zero up to at least height $25$.

## Turing and the Era of Manual Computation

Alan Turing, during the Second World War, made an important contribution to $\zeta$ zero computation. He devised a method for verifying that a zero lies on the critical line by checking that a certain related function changes sign. Turing's method reduced the risk of numerical error and was applied to verify the first 1104 zeros.

Turing's motivation was not purely mathematical — he also wanted to demonstrate what was then far from obvious: that the Riemann Hypothesis was, at least as far as the computed zeros were concerned, correct.

## The Dawn of Digital Computation

In 1953, Lehmer used an early electronic computer to verify that the first 10,000 zeros all lie on the critical line. Lehmer's data also became the first publicly available zero dataset for statistical study.

By the late 1960s, approximately 3.5 million zeros had been verified on the critical line. Rosser, Yohe, and Schoenfeld conducted systematic verification programs using increasingly powerful machines.

## Odlyzko and the Supercomputing Era

Andrew Odlyzko, in the late 1980s and 1990s, took zero computation to an entirely new level. He not only verified the positions of the first billion zeros but also conducted groundbreaking high-density statistical studies — computing the distribution of tens of millions of zeros simultaneously at extremely high altitudes. At heights above $t \approx 10^{20}$, he confirmed the statistical predictions of the Montgomery pair correlation conjecture (Chapter 28).

Odlyzko's computations were among the largest numerical experiments in mathematical history, requiring custom code and the most powerful supercomputers of the era. His data remain the benchmark for statistical analysis of zero distribution.

## ZetaGrid: Distributed Computing

Between 2001 and 2005, Sebastian Wedeniwski launched **ZetaGrid** — a distributed computing network harnessing idle CPU cycles from volunteers worldwide, modeled on SETI@home. ZetaGrid verified an astonishing $10^{12}$ (one trillion) zeros, all on the critical line.

Computations on this scale mean that if the Riemann Hypothesis is false — if there exists even one zero off the critical line — that zero must lie at an extraordinarily high altitude, far beyond anything we can currently check.

## The Latest Computations (2020s)

In the 2020s, Dave Platt, Tim Trudgian, and others, using modern algorithms and high-performance computing, have verified over $10^{13}$ zeros on the critical line, reaching heights of $t \approx 3 \times 10^{12}$.

The mathematical community is now working toward the $10^{14}$ milestone and beyond. These computations use high-precision asymptotic expansions of the Riemann–Siegel formula running on modern multi-core CPUs and GPUs.

## The Nature and Limits of Numerical Evidence

Every $\zeta$ zero ever computed lies on the critical line. This is the most powerful empirical argument for the truth of RH — but it is not a proof.

The history of mathematics offers cautionary tales: a conjecture may hold for $10^{10}$ instances (Mertens' conjecture did, up to astronomically large numbers) yet ultimately be proved false. Even $10^{13}$ zeros on the critical line cannot exclude the possibility of a single rogue zero at some unimaginable height.

---

> **Key points**: Riemann hand-computed the first zeros with remarkable accuracy. Turing contributed sign-change verification methods during WWII. The twentieth century witnessed an exponential leap from Lehmer's 10,000 zeros to ZetaGrid's one trillion. By the 2020s, over $10^{13}$ zeros have been numerically verified on the critical line. Overwhelming numerical evidence supports RH but cannot substitute for rigorous proof.

> **See also**: [Chapter 32: Philosophical and Cultural Impact](./chapter-32-philosophy.md) ★
