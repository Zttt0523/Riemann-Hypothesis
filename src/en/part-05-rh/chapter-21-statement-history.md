---
difficulty = "★★"
prerequisites = ["IV-16", "IV-17"]
paths = ["green", "blue", "red"]
keywords = ["Riemann Hypothesis", "1859 paper", "critical line", "Hilbert", "Millennium"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 21: Statement and History of the Riemann Hypothesis

> Difficulty: ★★ | Paths: 🟢🟡🔴 | Prerequisites: Chapters 16, 17

## Formal Statement

> **Riemann Hypothesis (RH)**: All non-trivial zeros of the Riemann zeta function have real part equal to $\frac{1}{2}$.

Equivalently: if $\zeta(\rho) = 0$ and $0 < \operatorname{Re}(\rho) < 1$, then $\operatorname{Re}(\rho) = \frac{1}{2}$.

This is the most famous — and most important — unsolved problem in mathematics. It is simple enough to state in a single line, profound enough to have resisted the efforts of the finest mathematical minds for over a century and a half.

## Riemann's Original Statement (1859)

Riemann first made the conjecture on the sixth page of his 1859 paper. His actual words (Dedekind's 1876 edition) were:

> *"One finds in fact about this many real roots within these bounds, and it is very probable that all roots are real. One would certainly wish for a rigorous proof of this; I have, however, temporarily set aside the search for such a proof after several fleeting unsuccessful attempts, as it appears unnecessary for the immediate objective of my investigation."*

Several points deserve notice:
1. **"All roots are real"**: Riemann was speaking of the $\xi$-function. For $\xi$, "real" means the zero lies on $\operatorname{Re}(s) = 1/2$. Hence "all roots are real" is precisely equivalent to the modern statement of RH.
2. **"Several fleeting unsuccessful attempts"**: Riemann himself tried and failed to prove his own conjecture. In the 160+ years since, no one else has succeeded either.
3. **"Unnecessary for the immediate objective"**: Riemann's main purpose was to derive the explicit formula for $\pi(x)$ — a more practical goal — and the Hypothesis, though it would yield stronger results, was not essential for getting started.

## Equivalent Formulations

The RH can be recast in dramatically different languages.

### Prime Distribution Equivalence

RH is equivalent to the optimal error bound in the Prime Number Theorem:

$$
\pi(x) = \operatorname{Li}(x) + O(\sqrt{x} \ln x)
$$

### Mertens Function Equivalence

Let $M(x) = \sum_{n \leq x} \mu(n)$. Then RH $\iff$ $M(x) = O(x^{1/2 + \varepsilon})$ for every $\varepsilon > 0$.

### Robin's Inequality (1984)

RH is equivalent to the inequality holding for all $n \geq 5041$:

$$
\sigma(n) < e^{\gamma} n \ln \ln n
$$

where $\sigma(n)$ is the sum of divisors of $n$. That an inequality about divisors should be equivalent to a conjecture about zeta zeros is one of the more startling facts in mathematics.

## Historical Milestones

| Year | Event |
|------|-------|
| **1859** | Riemann formulates the conjecture |
| **1900** | Hilbert names it Problem #8 of his 23 problems |
| **1914** | Hardy proves infinitely many zeros *on* the critical line |
| **1942** | Selberg proves a positive proportion of zeros on the critical line |
| **1974** | Levinson proves at least $1/3$ of zeros on the line |
| **1989** | Conrey proves at least $2/5$ of zeros on the line |
| **2000** | Clay Mathematics Institute names RH a Millennium Prize Problem |
| **2020s** | Over $10^{13}$ zeros numerically verified on the critical line |

## Hilbert's Encomium

Hilbert's words at the 1900 ICM in Paris have become legendary:

> "If I were to awaken after having slept for a thousand years, my first question would be: Has the Riemann Hypothesis been proved?"

He was also characteristically optimistic:

> "If we wake from our hypnosis, this problem may already be solved."

Over 125 years later, Hilbert's optimism remains unvindicated.

## Why Is the Riemann Hypothesis So Hard?

The difficulty lies in the gap RH occupies: it is a statement about a specific property of a specific function, yet proving that property seems to require a unified insight spanning the whole edifice of analytic number theory — and perhaps mathematics itself. Every attempted proof, whether successful or not, has opened new mathematical territory. The difficulty is both curse and blessing: the sheer stubbornness of RH has driven more mathematical progress than most solved problems ever could.

---

> **Key points**: The Riemann Hypothesis asserts $\operatorname{Re}(\rho) = 1/2$ for all non-trivial zeros of $\zeta(s)$. Riemann proposed it in 1859 with only "fleeting unsuccessful attempts" at proof. Hilbert elevated it to Problem #8 in 1900; the Clay Institute made it a Millennium Prize Problem in 2000. RH is equivalent to the Prime Number Theorem having optimal error $O(\sqrt{x}\ln x)$. Multiple equivalent formulations — prime distribution, Mertens function, Robin's inequality — attest to RH's centrality.

> **See also**: [Chapter 22: Equivalent Formulations](./chapter-22-equivalents.md) ★★★
