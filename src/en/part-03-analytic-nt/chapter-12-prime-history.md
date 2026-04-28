---
difficulty = "★"
prerequisites = []
paths = ["green", "blue", "red"]
keywords = ["prime numbers", "Eratosthenes", "Gauss", "prime counting", "PNT"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 12: Prime Numbers Through History

> Difficulty: ★ | Paths: 🟢🟡🔴 | Prerequisites: None

## Primes: The Atoms of Mathematics

A **prime number** is an integer greater than $1$ divisible only by $1$ and itself. The first few primes are:

$$
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \ldots
$$

Primes are called the "atoms of mathematics" — just as matter is composed of atoms, every integer greater than $1$ is composed of primes multiplied together. This is the **Fundamental Theorem of Arithmetic**: each integer $> 1$ factors uniquely into primes (up to order):

$$
60 = 2^2 \times 3 \times 5
$$

But what fascinates mathematicians is not the uniqueness of factorization — it is the **unpredictability** of the primes. In the natural numbers, primes appear to emerge without pattern — sometimes clustered, sometimes separated by vast gaps. For over two millennia, the search for the law governing prime distribution has been one of the deepest threads in mathematics.

## Antiquity: Euclid and Eratosthenes

### The Infinitude of Primes

Euclid (c. 300 BCE) gave the first proof that there are infinitely many primes — and it remains one of the most elegant arguments in mathematics.

> **Euclid's proof**: Suppose there were only finitely many primes $p_1, \ldots, p_n$. Consider $N = p_1 p_2 \cdots p_n + 1$. No known prime divides $N$ (each leaves remainder $1$), so $N$ is either prime itself or has a prime factor not in the list. Either way, a prime exists beyond the list — contradiction.

The elegance of this proof lies in its indirection: it does not construct primes; it shows that any finite list must be incomplete. Two thousand three hundred years later, Riemann's approach would take an entirely different path — using the analytic behavior of $\zeta(s)$ in the complex plane — to obtain precise quantitative information about prime distribution.

### The Sieve of Eratosthenes

Eratosthenes (c. 276–194 BCE) invented the earliest algorithm for generating primes. Starting from $2$, cross out all multiples of $2$. Take the next surviving number ($3$) and cross out all its multiples. Continuing, the numbers that remain are prime.

The algorithm runs in $O(n \log \log n)$ time and remains among the most efficient methods for generating primes today — a two-thousand-year-old algorithm running at modern speeds, a vivid illustration of the power of a simple idea.

## The 17th and 18th Centuries: Fermat, Mersenne, Euler

### Fermat Primes

Pierre de Fermat conjectured that numbers of the form $F_n = 2^{2^n} + 1$ are all prime. Indeed, $F_0 = 3$, $F_1 = 5$, $F_2 = 17$, $F_3 = 257$, and $F_4 = 65537$ are prime. But in 1732, Euler found:

$$
F_5 = 2^{32} + 1 = 4294967297 = 641 \times 6700417
$$

Fermat's failed conjecture is a cautionary tale: prime distribution resists simple formulas. To this day, no useful closed formula generates all primes — or only primes.

### Euler's Product Discovery

In 1737, Euler discovered the bridge between series and products — the Euler product (discussed in Chapter 11). This was the first time analytic methods were applied to the study of primes, effectively founding **analytic number theory** as a discipline.

### The Asymptotic Law: Conjectures of Gauss and Legendre

By the late eighteenth century, mathematicians began asking a more refined question: how many primes are there up to $x$? Denote this count by $\pi(x)$:

| $x$ | $\pi(x)$ | $\pi(x)/x$ |
|-----|----------|------------|
| $10$ | $4$ | $0.4000$ |
| $100$ | $25$ | $0.2500$ |
| $1000$ | $168$ | $0.1680$ |
| $10^6$ | $78498$ | $0.0785$ |

Observe: the density $\pi(x)/x$ decreases slowly as $x$ grows.

Gauss, at the age of fifteen (c. 1792), and Legendre (1798) independently conjectured:

$$
\pi(x) \sim \frac{x}{\ln x}
$$

That is, for large $x$, the number of primes up to $x$ is approximately $x / \ln x$. More precisely:

$$
\lim_{x \to \infty} \frac{\pi(x)}{x / \ln x} = 1
$$

This is the **Prime Number Theorem** (PNT). But neither Gauss nor Legendre could prove it.

## 1859: Riemann's Revolution

In 1859, Riemann submitted his paper "On the Number of Primes Less Than a Given Magnitude." His key innovation: **treat $\zeta(s)$ as a function of a complex variable** and deploy the full power of complex analysis.

Riemann's explicit formula expresses $\pi(x)$ as a sum over the zeros of $\zeta(s)$:

$$
\pi(x) \approx \mathrm{Li}(x) - \sum_{\rho} \mathrm{Li}(x^\rho) + \cdots
$$

where $\rho$ runs over the **non-trivial zeros** of $\zeta(s)$. This breathtaking formula reveals that the primes and the zeros of $\zeta(s)$ are in precise correspondence. Each zero contributes an oscillatory "correction wave" to the prime distribution.

The Riemann Hypothesis is precisely a claim about the location of these zeros: **all non-trivial zeros lie on the line $\Re(s) = 1/2$**.

## 1896: The Proof of PNT

Thirty years after Riemann's death, Jacques Hadamard and Charles de la Vallée Poussin independently proved the Prime Number Theorem in 1896.

Their proofs used Riemann's framework but sidestepped the full Riemann Hypothesis. They proved the weaker but sufficient fact that $\zeta(s)$ has no zeros on the line $\Re(s) = 1$ — enough to establish $\pi(x) \sim x/\ln x$, but far from the extraordinarily precise error bound that the Riemann Hypothesis would imply.

## The Prime Journey: From Then to Now

From Euclid to Riemann, from "there are infinitely many primes" to "the primes are precisely governed by the zeros of $\zeta(s)$," our understanding has undergone a profound transformation. The deepest insight: **the order of the primes lies not in their individual positions but in their statistical distribution** — and the finest description of that distribution is hidden in the zeros of the Riemann zeta function.

---

> **Key points**: Prime numbers are the indivisible atoms of the integers. Euclid proved their infinitude. Eratosthenes devised the first prime sieve. Gauss and Legendre conjectured the Prime Number Theorem, $\pi(x) \sim x/\ln x$. Riemann's 1859 paper introduced $\zeta(s)$ into prime number theory, establishing an exact correspondence between the zeros of $\zeta(s)$ and the distribution of primes.

> **See also**: [Chapter 13: Arithmetic Functions](./chapter-13-arithmetic-functions.md) ★★
