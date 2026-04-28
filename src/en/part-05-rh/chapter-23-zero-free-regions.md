---
difficulty = "★★★"
prerequisites = ["IV-19", "V-21"]
paths = ["red"]
keywords = ["zero-free region", "Vinogradov", "Korobov", "explicit formula", "de la Vallée Poussin"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 23: Zero-Free Regions

> Difficulty: ★★★ | Paths: 🔴 | Prerequisites: Chapters 19, 21

## From "No Zeros" to "Where Are the Zeros?"

Chapter 15 showed that the key step in proving the Prime Number Theorem is showing $\zeta(s) \neq 0$ on the line $\operatorname{Re}(s) = 1$. This can be generalized: $\zeta(s)$ has no zeros in certain regions to the right of the critical line — **zero-free regions**. The larger the zero-free region, the sharper the error term in the Prime Number Theorem.

We already know $\zeta(s)$ has infinitely many zeros *on* the critical line — these zeros block any zero-free region from extending past $\operatorname{Re}(s) = 1/2$. The maximum possible zero-free region is therefore bounded by the critical line itself.

## The Classical Zero-Free Region

In proving PNT in 1896, Hadamard and de la Vallée Poussin actually proved more than $\zeta(1+it) \neq 0$ — they found a wedge-shaped zero-free region extending leftward from $\operatorname{Re}(s) = 1$.

de la Vallée Poussin (1899) proved:

> $\zeta(s) \neq 0$ in the region $\sigma \geq 1 - \frac{c}{\ln(2+|t|)}$, for some constant $c > 0$.

As you go upward ($|t|$ increases), the left boundary of the zero-free region recedes toward $\operatorname{Re}(s) = 1$ at a rate proportional to $1/\ln t$.

## The Vinogradov–Korobov Zero-Free Region

In 1958, the Soviet mathematicians Vinogradov and Korobov independently proved a substantially **wider** zero-free region using estimates of Weyl sums:

> $\zeta(s) \neq 0$ in the region $\sigma \geq 1 - \frac{c}{(\ln(2+|t|))^{2/3} (\ln\ln(3+|t|))^{1/3}}$.

This is currently the best known zero-free region. Note the exponent $2/3$ — for decades no one has improved it below $1$, though it is universally believed that the optimal exponent should be $1$.

If the Riemann Hypothesis holds, the zero-free region extends to the entire half-plane $\sigma > 1/2$ — effectively taking $c$ down to $1/2$. The mathematical distance from Vinogradov–Korobov to RH is the gulf between an exponent of $2/3$ and a constant of $1/2$.

## Zero-Free Regions and the PNT Error Term

The width of the zero-free region directly controls the PNT error term. The Vinogradov–Korobov region yields:

$$
\pi(x) = \operatorname{Li}(x) + O\!\left(x \exp\!\left(-c \frac{(\ln x)^{3/5}}{(\ln\ln x)^{1/5}}\right)\right)
$$

This is vastly more precise than anything Gauss or Legendre could have dreamed — yet it remains an immeasurably weaker bound than the $O(\sqrt{x}\ln x)$ promised by the Riemann Hypothesis.

## Why Are Zero-Free Regions Hard to Enlarge?

The bottleneck is a fundamental tension: to prove no zeros exist in a region to the right of the critical line, one must show $\zeta(s)$ cannot vanish there. But the growth of $\zeta(s)$ near $\operatorname{Re}(s) = 1$ is constrained by subtle "modulations." Distinguishing "no zero" from "zero, but very close to $1/2$" requires ever finer estimates of exponential sums.

This leads to some of the deepest conjectures in analytic number theory, including the Lindelöf Hypothesis (Chapter 26), which concerns the growth rate of $\zeta(s)$ on the critical line.

## Modern Efforts to Enlarge the Zero-Free Region

In recent years, mathematicians including Maynard and Guth have brought new tools — Fourier analysis, combinatorial sieve methods — to bear on classical zero-distribution problems. In 2024, Guth and Maynard published work widely discussed as a potential step toward improving the Vinogradov–Korobov zero-free region.

While these advances do not touch the Riemann Hypothesis itself, they demonstrate: **even the most classical, most intensively studied problems still admit new tools and fresh perspectives.**

---

> **Key points**: $\zeta(s)$ has zero-free regions extending leftward from $\operatorname{Re}(s) = 1$. The de la Vallée Poussin region has width $O(1/\ln t)$. The Vinogradov–Korobov region (1958), with width $O(1/(\ln t)^{2/3})$, is the best currently known. The zero-free region directly controls the PNT error term. The gap between the Vinogradov–Korobov region and the RH (the entire half-plane $\sigma > 1/2$) remains vast.

> **See also**: [Chapter 24: Consequences of RH](./chapter-24-consequences.md) ★★★
