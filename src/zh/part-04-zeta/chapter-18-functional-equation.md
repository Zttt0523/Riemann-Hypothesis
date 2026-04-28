---
difficulty = "★★★"
prerequisites = ["IV-17"]
paths = ["red"]
keywords = ["functional equation", "Gamma function", "Xi function", "symmetry", "critical line"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第十八章：函数方程

> 难度：★★★ | 路径：🔴 | 前置：第十七章

## 函数方程：对称性与结构

$\zeta(s)$ 最深刻的性质之一是其**函数方程**（functional equation）——一个将 $\zeta(s)$ 与 $\zeta(1-s)$ 联系起来的恒等式。这一对称性由黎曼在 1859 年证明，是理解 $\zeta(s)$ 全局行为的关键。

> **黎曼函数方程**：
> $$
> \zeta(s) = 2^s \pi^{s-1} \sin\!\left(\frac{\pi s}{2}\right) \Gamma(1-s) \, \zeta(1-s)
> $$

这个等式在整个复平面上（除 $s = 0$ 和 $s = 1$ 的极点外）成立。

## 对称形式的函数方程

引入**完备 $\zeta$ 函数**（completed zeta function）或 $\xi$ 函数（黎曼的记号）可以使对称性更加明显。定义：

$$
\xi(s) = \frac{1}{2} s(s-1) \pi^{-s/2} \,\Gamma\!\left(\frac{s}{2}\right) \zeta(s)
$$

因子 $\frac{1}{2}s(s-1)$ 抵消了 $\zeta(s)$ 在 $s=1$ 的极点和 $\Gamma(s/2)$ 在 $s=0$ 的极点。于是 $\xi(s)$ 是一个**整函数**——在整个复平面上全纯。

函数方程化为极其简洁的形式：

$$
\xi(s) = \xi(1-s)
$$

$\xi$ 函数关于临界线 $\Re(s) = 1/2$ 对称。这是黎曼猜想自然性的直观来源：如果有零点偏离了临界线，其对称点也将是零点，由此产生的结构似乎"过于复杂"。

## 函数方程的证明概要

黎曼的原始证明使用了 $\theta$ 函数的一个恒等式。定义 Jacobi $\theta$ 函数：

$$
\theta(x) = \sum_{n=-\infty}^{\infty} e^{-\pi n^2 x}
$$

$\theta$ 函数满足变换公式 $\theta(1/x) = \sqrt{x}\,\theta(x)$（来自 Poisson 求和公式）。通过 Mellin 变换，$\zeta(s)$ 与 $\theta(x)$ 相关联，而 $\theta$ 的对称性直接翻译为 $\zeta(s)$ 的函数方程。

## 平凡零点的起源

函数方程中 $\sin(\pi s/2)$ 的因式直接给出了平凡零点。由于 $\sin(\pi s/2) = 0$ 当 $s = -2, -4, -6, \ldots$，而 $\Gamma(1-s)$ 在 $s = 2, 3, 4, \ldots$ 处具有极点，两者的乘积在精确抵消后，仅留负偶数处的零点。这些就是 $\zeta(s)$ 的**平凡零点**，全部位于负实轴上。

## 临界线 $\Re(s) = 1/2$

由函数方程知：若 $\rho$ 是 $\zeta(s)$ 的非平凡零点，则 $1-\rho$ 也是零点。因此关于临界线 $\Re(s) = \frac{1}{2}$，零点成对出现，除非 $\rho$ 恰好位于临界线上——此时 $\rho$ 与 $1-\rho$ 是复共轭关系（$\bar{\rho} = 1 - \rho$）。

此外，由于 $\zeta(\bar{s}) = \overline{\zeta(s)}$（Schwarz 反射原理），若 $\rho$ 是零点，则 $\bar{\rho}$ 也是零点。因此零点也关于实轴对称。

这两条对称性——函数方程给出的**临界线反射对称**和 Schwarz 反射给出的**实轴对称**——共同将非平凡零点限制在一种高度对称的图案中。

## 临界带 $0 < \Re(s) < 1$

函数方程的一个直接推论是：所有非平凡零点都位于**临界带** $0 < \Re(s) < 1$ 之内。证明思路是：当 $\Re(s) > 1$ 时，欧拉乘积绝对收敛，因此 $\zeta(s) \neq 0$。函数方程随之推出 $\zeta(s) \neq 0$ 对 $\Re(s) < 0$ 也成立（除了平凡零点）。因此非平凡零点只能存在于 $0 \leq \Re(s) \leq 1$ 之内。在 $\Re(s) = 0$ 和 $\Re(s) = 1$ 直线上无零点的事实分别由函数方程和 PNT 的引理 1 给出。

## 函数方程的深层含义

函数方程不仅是 $\zeta(s)$ 的一个代数性质，它揭示了某种更深层的**自守性**（automorphy）。在现代 Langlands 纲领的视角下，$\zeta(s)$ 的函数方程是一个巨大的对称性之网中最简单的实例——L-函数形成了一个由函数方程相互关联的家族，而黎曼猜想是这个家族中每个成员都满足的普遍性质。

---

> **本章要点**：函数方程 $\xi(s) = \xi(1-s)$ 显示了 $\zeta(s)$ 关于临界线 $\Re(s) = 1/2$ 的对称性。$\xi$ 函数是整函数，去除了 $\zeta(s)$ 的极点和 $\Gamma$ 函数带来的平凡零点。平凡零点位于 $s = -2, -4, -6, \ldots$。所有非平凡零点位于临界带 $0 < \Re(s) < 1$ 内。函数方程是理解黎曼猜想自然性的核心——它暗示临界线是零点分布的"天然位置"。

> **参见**：[第十九章：$\zeta$ 函数的零点](./chapter-19-zeros.md) ★★★
