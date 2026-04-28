---
difficulty = "★★"
prerequisites = ["II-06"]
paths = ["blue", "red"]
keywords = ["arithmetic function", "Möbius", "Dirichlet convolution", "Mertens", "multiplicative"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第十三章：算术函数

> 难度：★★ | 路径：🟡🔴 | 前置：第六章

## 定义与例子

**算术函数**（arithmetic function）是以正整数为定义域、以复数（或实数）为值域的函数。它们是数论的基本语言。

最重要的算术函数：

| 函数 | 符号 | 定义 |
|------|------|------|
| 除数函数 | $d(n)$ | $n$ 的正因数个数 |
| 除数和函数 | $\sigma(n)$ | $n$ 的所有正因数之和 |
| Euler 函数 | $\varphi(n)$ | 不超过 $n$ 且与 $n$ 互素的正整数的个数 |
| Möbius 函数 | $\mu(n)$ | 若 $n$ 有平方因子则为 $0$；否则为 $(-1)^k$（$k$ 为素因子个数） |
| von Mangoldt 函数 | $\Lambda(n)$ | 若 $n = p^k$ 则为 $\ln p$；否则为 $0$ |
| 常数函数 | $\mathbf{1}(n)$ | 对所有 $n$ 取值为 $1$ |

在这些函数中，**Möbius 函数** $\mu(n)$ 和 **von Mangoldt 函数** $\Lambda(n)$ 在解析数论——特别是 $\zeta$ 函数理论中——占据核心地位。

## 积性函数

一个算术函数 $f$ 称为**积性**的（multiplicative），如果对于互素的 $m, n$，有：

$$
f(mn) = f(m)f(n) \quad \text{当} \quad \gcd(m, n) = 1
$$

$\varphi(n)$、$\mu(n)$ 和 $\sigma(n)$ 都是积性函数。积性函数的值完全由其素数幂处的值决定——这是它们力量的源泉。

## Möbius 反演

**Möbius 函数** $\mu(n)$ 的定义：

$$
\mu(n) = \begin{cases}
1 & \text{若 } n = 1 \\
(-1)^k & \text{若 } n \text{ 是 } k \text{ 个不同素数的乘积} \\
0 & \text{若 } n \text{ 有平方因子}
\end{cases}
$$

前几个值：$\mu(1) = 1$，$\mu(2) = -1$，$\mu(3) = -1$，$\mu(4) = 0$，$\mu(5) = -1$，$\mu(6) = 1$，$\ldots$

$\mu$ 的核心性质：对于 $n > 1$，

$$
\sum_{d \mid n} \mu(d) = 0
$$

其中求和遍历 $n$ 的所有正因数。这个看似简单的恒等式蕴含了 **Möbius 反演公式**：

$$
g(n) = \sum_{d \mid n} f(d) \iff f(n) = \sum_{d \mid n} \mu(d) \, g\!\left(\frac{n}{d}\right)
$$

Möbius 反演与包含-排除原理（inclusion-exclusion principle）密切相关，是组合数论的基石。

## Dirichlet 卷积

算术函数之间的运算由**Dirichlet 卷积**（Dirichlet convolution）定义：

$$
(f * g)(n) = \sum_{d \mid n} f(d) \, g\!\left(\frac{n}{d}\right)
$$

Dirichlet 卷积是一种"算术函数的乘法"，它具有以下性质：

- 可交换：$f * g = g * f$
- 可结合：$f * (g * h) = (f * g) * h$
- 单位元：$\varepsilon(n) = \lfloor 1/n \rfloor$（$n=1$ 时为 $1$，否则 $0$）
- $\mu * \mathbf{1} = \varepsilon$（即 $\mu$ 和常数函数互为卷积逆元）

Möbius 反演可以简洁地表示为：$g = f * \mathbf{1}$ 当且仅当 $f = g * \mu$。

## 与 $\zeta$ 函数的联系

算术函数与 $\zeta$ 函数之间最深刻的联系在于 **Dirichlet 级数**（下一章的完整主题）。在此先做预告：

算术函数的 Dirichlet 级数 $F(s) = \sum_{n=1}^{\infty} \frac{f(n)}{n^s}$ 的行为与 $f$ 的性质密切相关。例如：

- 常数函数 $\mathbf{1}$ 的 Dirichlet 级数是 $\zeta(s) = \sum n^{-s}$
- **Möbius 函数的 Dirichlet 级数是 $\zeta(s)$ 的倒数**：$\sum_{n=1}^{\infty} \frac{\mu(n)}{n^s} = \frac{1}{\zeta(s)}$。这一关系直接来自欧拉乘积和 $\mu$ 的定义
- von Mangoldt 函数的 Dirichlet 级数是 $\zeta(s)$ 的对数导数：$\sum \frac{\Lambda(n)}{n^s} = -\frac{\zeta'(s)}{\zeta(s)}$

最后一个关系是素数定理经典证明的技术核心。

---

> **本章要点**：算术函数将整数映射到复数，是数论的基本研究对象。Möbius 函数的反演性质（$\mu * \mathbf{1} = \varepsilon$）是组合数论的基本工具。Dirichlet 卷积提供了算术函数的"乘法"运算。Möbius 函数和 von Mangoldt 函数的 Dirichlet 级数直接关联到 $\zeta(s)$ 及其导数。

> **参见**：[第十四章：Dirichlet 级数](./chapter-14-dirichlet-series.md) ★★
