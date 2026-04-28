---
difficulty = "★★"
prerequisites = ["II-07"]
paths = ["blue", "red"]
keywords = ["complex numbers", "holomorphic", "Cauchy-Riemann", "Euler formula", "complex plane"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 10: Complex Numbers and Functions

> Difficulty: ★★ | Paths: 🟡🔴 | Prerequisites: Chapter 7

## The Algebra of Complex Numbers

### From Real to Complex

The real numbers are complete, but algebraically they have a gap: $x^2 + 1 = 0$ has no real solution. Introducing the **imaginary unit** $i$ with $i^2 = -1$ yields the **complex numbers**:

$$
z = x + iy
$$

where $x = \operatorname{Re}(z)$ (the real part) and $y = \operatorname{Im}(z)$ (the imaginary part).

### Operations

Addition mirrors vector addition: $(a+ib) + (c+id) = (a+c) + i(b+d)$.

Multiplication uses $i^2 = -1$: $(a+ib)(c+id) = ac + i(ad+bc) + i^2 bd = (ac-bd) + i(ad+bc)$.

### Conjugate and Modulus

The **conjugate** of $z = x+iy$ is $\bar{z} = x-iy$. The **modulus** is $|z| = \sqrt{x^2 + y^2} = \sqrt{z\bar{z}}$, representing the distance from the origin in the complex plane.

## The Complex Plane

Every complex number corresponds to a point in the plane: the horizontal axis is the real axis; the vertical axis is the imaginary axis. Addition corresponds to vector addition. Multiplication corresponds to **rotation and scaling**.

## Euler's Formula

The most beautiful formula in complex analysis is Euler's formula:

$$
e^{i\theta} = \cos\theta + i\sin\theta
$$

Any complex number can be written in **polar form**:

$$
z = r e^{i\theta} = r(\cos\theta + i\sin\theta)
$$

where $r = |z|$ and $\theta = \arg(z)$ is the argument.

Setting $\theta = \pi$ yields the most celebrated identity in mathematics:

$$
e^{i\pi} + 1 = 0
$$

linking $e$, $i$, $\pi$, $1$, and $0$ — five fundamental constants in a single equation.

Euler's formula is crucial for $\zeta(s)$. Via $n^{-s} = e^{-s \ln n}$, complex exponents appear naturally in every term. Writing $s = \sigma + it$:

$$
n^{-s} = n^{-\sigma - it} = n^{-\sigma} \cdot e^{-i t \ln n}
$$

The imaginary part $t$ produces an oscillatory factor $e^{-i t \ln n}$, while the real part $\sigma$ controls the magnitude.

## Complex Functions

A **complex function** $f: \mathbb{C} \to \mathbb{C}$ maps complex numbers to complex numbers. Simple examples:

- $f(z) = z^2 = (x+iy)^2 = (x^2 - y^2) + i(2xy)$
- $f(z) = e^z = e^{x+iy} = e^x(\cos y + i\sin y)$

Notice that $e^z$ is periodic: $e^{z+2\pi i} = e^z$. The exponential function reveals a richness in the complex domain invisible in the real domain.

## Complex Differentiability and the Cauchy-Riemann Equations

The core concept of complex analysis is **complex differentiability**. $f(z)$ is complex-differentiable at $z_0$ if:

$$
f'(z_0) = \lim_{h \to 0} \frac{f(z_0 + h) - f(z_0)}{h}
$$

exists, where $h$ is a **complex** number. This is fundamentally different from real differentiability: in the reals, $h$ approaches zero from two directions; in the complex plane, $h$ can approach zero from **infinitely many directions**. Complex differentiability is vastly stronger.

Writing $f(z) = u(x,y) + i\,v(x,y)$, complex differentiability is equivalent to the **Cauchy-Riemann equations**:

$$
\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \qquad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}
$$

Functions satisfying these equations are called **holomorphic** (or **analytic**).

## The Astonishing Properties of Holomorphic Functions

Once $f$ is holomorphic on a domain, the following properties are **automatically true**:

1. $f$ is infinitely differentiable
2. $f$ equals its Taylor series (analyticity)
3. $f$ satisfies the **maximum modulus principle**: $|f|$ attains its maximum on the boundary
4. $f$ satisfies **Cauchy's integral formula**: values inside a domain are completely determined by values on the boundary
5. If $f$ is holomorphic and bounded on the entire complex plane, $f$ is constant (**Liouville's theorem**)

Property 5 — Liouville's theorem — is a crucial ingredient in the classical proof of the Prime Number Theorem.

The chasm between real-differentiable and holomorphic functions is profound. Real-differentiable functions can be pathological — continuous everywhere, differentiable nowhere; differentiable with discontinuous derivatives; infinitely differentiable but not analytic. The world of holomorphic functions is orderly and beautiful, governed by "automatic" theorems.

**Understanding these properties is the key to understanding why the Riemann zeta function possesses such deep structure.**

## Complex Analysis and $\zeta(s)$

$\zeta(s)$ is a function of a complex variable. Its deepest properties — **analytic continuation** and the **functional equation** — depend entirely on the machinery of complex analysis. The next chapter treats infinite products, the bridge between the series definition of $\zeta(s)$ and Euler's product over primes. Part IV will deploy the full apparatus of complex analysis to study $\zeta(s)$ in depth.

---

> **Key points**: Complex numbers extend the reals via $i^2 = -1$. Euler's formula $e^{i\theta} = \cos\theta + i\sin\theta$ is the cornerstone of complex analysis. Complex differentiability (holomorphicity) is vastly stronger than real differentiability — it automatically implies infinite differentiability and analyticity. These "automatic" properties of holomorphic functions are the mathematical engine of zeta function theory.

> **See also**: [Chapter 11: Infinite Products](./chapter-11-infinite-products.md) ★★
