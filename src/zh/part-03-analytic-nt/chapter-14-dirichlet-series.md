---
difficulty = "★★"
prerequisites = ["II-06", "III-13"]
paths = ["blue", "red"]
keywords = ["Dirichlet series", "abscissa", "Euler product", "Mellin", "Perron formula"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第十四章：Dirichlet 级数

> 难度：★★ | 路径：🟡🔴 | 前置：第六章、第十三章

## 什么是 Dirichlet 级数？

一个 **Dirichlet 级数**是形如以下的无穷级数：

$$
F(s) = \sum_{n=1}^{\infty} \frac{a_n}{n^s}
$$

其中 $s$ 是复变量，$a_n$ 是一个复数序列。这是解析数论中最核心的级数类型。

当所有 $a_n = 1$ 时，$F(s) = \sum n^{-s} = \zeta(s)$——黎曼 $\zeta$ 函数是 Dirichlet 级数中最基本的例子。

## Dirichlet 级数的收敛性

与幂级数不同，Dirichlet 级数的收敛域不是圆，而是**半平面**。

> **定理**：存在一个实数 $\sigma_c$（称为收敛横坐标，abscissa of convergence），使得 Dirichlet 级数在 $\Re(s) > \sigma_c$ 时收敛，在 $\Re(s) < \sigma_c$ 时发散。

对于 $\zeta(s) = \sum n^{-s}$，$\sigma_c = 1$（因为当 $s > 1$ 时 $p$-级数收敛，当 $s \leq 1$ 时发散）。

对于一般的 Dirichlet 级数，收敛横坐标取决于系数 $a_n$ 的增长速度。粗略地说，如果 $a_n$ 增长不超过某个幂次 $n^A$，则 $\sigma_c \leq A + 1$。

### 绝对收敛横坐标

还有一个**绝对收敛横坐标** $\sigma_a$，使得级数在 $\Re(s) > \sigma_a$ 时绝对收敛。一般而言 $\sigma_c \leq \sigma_a \leq \sigma_c + 1$。

对于 $\zeta(s)$，$\sigma_c = \sigma_a = 1$。但并非总是相等——$\sum (-1)^{n-1} n^{-s}$ 在 $\Re(s) > 0$ 时收敛（非绝对），而在 $\Re(s) > 1$ 时才绝对收敛。

## 乘法性质与 Euler 乘积

Dirichlet 级数最重要的代数性质是：卷积对应于乘法。具体地，若

$$
F(s) = \sum_{n=1}^{\infty} \frac{f(n)}{n^s}, \quad G(s) = \sum_{n=1}^{\infty} \frac{g(n)}{n^s}
$$

则

$$
F(s) G(s) = \sum_{n=1}^{\infty} \frac{(f * g)(n)}{n^s}
$$

其中 $f * g$ 是 Dirichlet 卷积。这一性质是欧拉乘积的代数根源：当 $f$ 是积性函数时，$F(s)$ 可以表示为素数的乘积。

例如，$\mu$ 的 Dirichlet 级数是：

$$
\sum_{n=1}^{\infty} \frac{\mu(n)}{n^s} = \frac{1}{\zeta(s)} \qquad (\Re(s) > 1)
$$

这一关系从欧拉乘积即可得出。它表明 Möbius 函数通过 Dirichlet 级数与 $\zeta$ 函数直接相连——这是解析数论中最基本的对应关系之一。

## Perron 公式：连接系数与级数

解析数论中最强大的技术工具之一是 **Perron 公式**（Perron's formula）。它通过复积分，从 Dirichlet 级数的信息中"提取"其系数的部分和：

$$
\sum_{n \leq x} a_n = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} F(s) \frac{x^s}{s} \, ds
$$

其中积分沿垂直线 $\Re(s) = c$（$c > \sigma_a$）进行。

应用 Perron 公式的基本策略是：
1. 从 Dirichlet 级数出发（例如 $\zeta(s)$ 或与其相关的函数）
2. 将积分路径向左移动，越过被积函数的极点
3. 遗留的贡献来自被积函数的极点（奇点）和割线

零点、极点与积分路径之间的相互作用是解析数论中一切"显式公式"的技术基础——包括黎曼关于 $\pi(x)$ 的显式公式。

## 关键例子

**von Mangoldt 函数**的 Dirichlet 级数是：

$$
-\frac{\zeta'(s)}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\Lambda(n)}{n^s}
$$

由此，素数定理等价于 $\psi(x) = \sum_{n \leq x} \Lambda(n) \sim x$。通过 Perron 公式，这变成了对 $\zeta'(s)/\zeta(s)$ 的极点分布的复分析研究——而极点分布又由 $\zeta(s)$ 的零点决定。

**到此，黎曼猜想的结构框架已经可见**：

$$
\text{素数分布} \xleftrightarrow[]{\text{Perron 公式}} \text{$\zeta(s)$ 的对数导数} \xleftrightarrow[]{\text{极点由零点决定}} \text{$\zeta(s)$ 的零点} \xleftrightarrow[]{\text{黎曼猜想}} \text{$\Re(\rho) = 1/2$}
$$

---

> **本章要点**：Dirichlet 级数 $\sum a_n n^{-s}$ 的收敛域是复平面上的半平面。积性系数的 Dirichlet 级数具有 Euler 乘积表示。Perron 公式通过复积分从 Dirichlet 级数中提取系数和，是黎曼显式公式的技术基础。$-\zeta'/\zeta$ 的 Dirichlet 级数系数正是 von Mangoldt 函数 $\Lambda(n)$。

> **参见**：[第十五章：素数定理](./chapter-15-pnt.md) ★★
