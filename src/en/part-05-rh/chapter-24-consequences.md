---
difficulty = "★★★"
prerequisites = ["V-21"]
paths = ["red"]
keywords = ["consequences", "prime gaps", "Skewes number", "error term", "arithmetic"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 24: Consequences of the Riemann Hypothesis

> Difficulty: ★★★ | Paths: 🔴 | Prerequisites: Chapter 21

## What If the Riemann Hypothesis Is True?

If RH were proved tomorrow — or disproved — a vast landscape of mathematical results would shift. This chapter catalogs the principal consequences of RH. Even unproved, these consequences are supported by overwhelming numerical evidence and have been "provisionally adopted" in countless number theory papers.

## Prime Distribution

The most important consequence of RH is the optimal estimate for primes:

$$
\pi(x) = \mathrm{Li}(x) + O(\sqrt{x} \ln x)
$$

The prime distribution becomes extraordinarily uniform — any local "clumping" or "sparseness" is governed by a square-root law. Corollaries:
- The $n$-th prime: $p_n = n\ln n + n\ln\ln n - n + O(\sqrt{n}\ln n)$
- Average prime gap: $\ln n$; largest gap: $O(\sqrt{p_n}\ln p_n)$ (stronger conjectures like Cramér's predict the gap is $O((\ln p_n)^2)$)

## The Skewes Number

In 1955, Stanley Skewes proved: *assuming RH*, there exists a number $S$ such that $\pi(S) > \mathrm{Li}(S)$ — the first time the prime counting function overtakes the logarithmic integral. Under RH: $S < e^{e^{e^{79}}} \approx 10^{10^{10^{34}}}$ — the "Skewes number."

The sheer size of this number is telling: although $\mathrm{Li}(x)$ overestimates $\pi(x)$ for all computationally accessible $x$, the model predicts infinitely many crossings — but so slowly that no human being will ever witness one.

## Möbius Sums and Squarefrees

RH implies that Möbius sums have minimal fluctuation:

$$
\sum_{n \leq x} \mu(n) = O(x^{1/2+\varepsilon})
$$

This directly controls the error in the natural density of squarefree integers: $\frac{6}{\pi^2}$.

## Primes in Arithmetic Progressions

The Generalized Riemann Hypothesis (GRH, Chapter 30) would imply uniform prime distribution across every arithmetic progression $a \bmod q$ (where $\gcd(a,q)=1$). Specifically, GRH yields a strengthened Dirichlet theorem:

$$
\pi(x; q, a) = \frac{\mathrm{Li}(x)}{\varphi(q)} + O(\sqrt{x} \ln(qx))
$$

Primes would be **perfectly equitably distributed** among valid residue classes, to within square-root fluctuations.

## Other Consequences

Numerous results currently prefaced with "assuming RH" would become unconditional:
- **Miller's primality test** (widely used in cryptography) is deterministic polynomial-time under RH
- Fine-grained estimates of $\zeta(s)$ oscillations on the critical line
- Lower bounds for Chen primes and twin primes would sharpen dramatically

## Living with an Unproved Hypothesis

Mathematical practice treats RH with pragmatic realism. Number theory papers routinely begin with "Assuming the Riemann Hypothesis..." — the result is conditional, but the condition is so widely believed that the result is treated as a "probable theorem."

Thirteen trillion zeros, all on the critical line — mathematical intuition and numerical evidence converge on "RH is true." But intuition and evidence, however overwhelming, are not proof.

---

> **Key points**: RH implies the sharpest possible error term $O(\sqrt{x}\ln x)$ for $\pi(x)$. Möbius sums are bounded by $O(x^{1/2+\varepsilon})$. The Skewes number gives an RH-conditional upper bound for the first $\pi(x) > \mathrm{Li}(x)$. Miller's primality test becomes deterministic. Countless number-theoretic results transition from "conditional" to "unconditional" upon proof of RH.

> **See also**: [Chapter 25: Attempted Proofs and Approaches](./chapter-25-attempts.md) ★★★
