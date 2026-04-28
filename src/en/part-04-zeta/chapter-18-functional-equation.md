---
difficulty = "★★★"
prerequisites = ["IV-17"]
paths = ["red"]
keywords = ["functional equation", "Gamma function", "Xi function", "symmetry", "critical line"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 18: The Functional Equation

> Difficulty: ★★★ | Paths: 🔴 | Prerequisites: Chapter 17

## The Functional Equation: Symmetry and Structure

One of the deepest properties of $\zeta(s)$ is its **functional equation** — an identity linking $\zeta(s)$ to $\zeta(1-s)$. This symmetry, proved by Riemann in his 1859 paper, is the key to understanding the global behavior of $\zeta(s)$.

> **Riemann's Functional Equation**:
> $$
> \zeta(s) = 2^s \pi^{s-1} \sin\!\left(\frac{\pi s}{2}\right) \Gamma(1-s) \, \zeta(1-s)
> $$

This identity holds throughout the complex plane (except at the poles of the individual factors at $s = 0$ and $s = 1$).

## The Symmetric Form

The symmetry becomes more transparent by introducing the **completed zeta function**, or $\xi$-function (Riemann's notation):

$$
\xi(s) = \frac{1}{2} s(s-1) \pi^{-s/2} \,\Gamma\!\left(\frac{s}{2}\right) \zeta(s)
$$

The factor $\frac{1}{2}s(s-1)$ cancels the pole of $\zeta(s)$ at $s = 1$ and the pole of $\Gamma(s/2)$ at $s = 0$. Thus $\xi(s)$ is an **entire function** — holomorphic everywhere.

The functional equation now takes the strikingly simple form:

$$
\xi(s) = \xi(1-s)
$$

The $\xi$ function is symmetric about the critical line $\Re(s) = 1/2$. This symmetry is the intuitive source of the Riemann Hypothesis's plausibility: if a zero were to deviate from the critical line, its symmetric counterpart would also be a zero, producing a structure that seems "too complicated" for a function as fundamental as $\zeta(s)$.

## Proof Sketch

Riemann's original proof used an identity of the Jacobi $\theta$-function:

$$
\theta(x) = \sum_{n=-\infty}^{\infty} e^{-\pi n^2 x}
$$

The $\theta$-function satisfies the transformation $\theta(1/x) = \sqrt{x}\,\theta(x)$ (derived from the Poisson summation formula). Via the Mellin transform, $\zeta(s)$ is related to $\theta(x)$, and $\theta$'s symmetry translates directly into the functional equation for $\zeta(s)$.

## Origin of the Trivial Zeros

The factor $\sin(\pi s/2)$ in the functional equation directly accounts for the trivial zeros. Since $\sin(\pi s/2) = 0$ when $s = -2, -4, -6, \ldots$, and $\Gamma(1-s)$ has poles at $s = 2, 3, 4, \ldots$, the product of the two factors — after careful cancellation — leaves zeros precisely at the negative even integers. These are the **trivial zeros** of $\zeta(s)$, all on the negative real axis.

## The Critical Line $\Re(s) = 1/2$

From the functional equation: if $\rho$ is a non-trivial zero of $\zeta(s)$, then $1 - \rho$ is also a zero. Zeros therefore come in symmetric pairs about the critical line $\Re(s) = 1/2$, unless $\rho$ lies exactly on it — in which case $\rho$ and $1-\rho$ are complex conjugates ($\bar{\rho} = 1 - \rho$).

Additionally, the Schwarz reflection principle ($\zeta(\bar{s}) = \overline{\zeta(s)}$) implies: if $\rho$ is a zero, $\bar{\rho}$ is also a zero. Zeros are symmetric about the real axis as well.

These two symmetries — **reflection about the critical line** from the functional equation and **reflection about the real axis** from Schwarz — combine to constrain non-trivial zeros into a highly symmetric pattern.

## The Critical Strip $0 < \Re(s) < 1$

A direct consequence of the functional equation: all non-trivial zeros lie within the **critical strip** $0 < \Re(s) < 1$. The reasoning: for $\Re(s) > 1$, the Euler product converges absolutely, so $\zeta(s) \neq 0$. The functional equation then forces $\zeta(s) \neq 0$ for $\Re(s) < 0$ (except for the trivial zeros). Non-trivial zeros are therefore forced into $0 \leq \Re(s) \leq 1$. The absence of zeros on $\Re(s) = 0$ and $\Re(s) = 1$ follows, respectively, from the functional equation and from Lemma 1 of the PNT proof (Chapter 15).

## The Deeper Meaning of the Functional Equation

The functional equation is more than an algebraic property of $\zeta(s)$ — it reveals a deeper **automorphy**. In the modern perspective of the Langlands program, the functional equation of $\zeta(s)$ is the simplest instance of a vast web of symmetries. L-functions form a family interrelated by functional equations, and the Riemann Hypothesis is conjectured to be a universal property shared by every member of that family.

---

> **Key points**: The functional equation $\xi(s) = \xi(1-s)$ exhibits $\zeta(s)$'s symmetry about the critical line $\Re(s) = 1/2$. The $\xi$-function is entire, removing the pole of $\zeta(s)$ and the trivial zeros. Trivial zeros lie at $s = -2, -4, -6, \ldots$. All non-trivial zeros lie in the critical strip $0 < \Re(s) < 1$. The functional equation suggests the critical line as the natural locus of zeros.

> **See also**: [Chapter 19: Zeros of the Zeta Function](./chapter-19-zeros.md) ★★★
