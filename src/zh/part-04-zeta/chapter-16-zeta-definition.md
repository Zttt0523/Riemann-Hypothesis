---
difficulty = "★★"
prerequisites = ["III-14"]
paths = ["blue", "red"]
keywords = ["zeta function", "Dirichlet series", "Euler product", "integral representation", "Mellin"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第十六章：ζ 函数的定义与初等性质

> 难度：★★ | 路径：🟡🔴 | 前置：第十四章

## 定义

黎曼 $\zeta$ 函数最初定义为 Dirichlet 级数（第十四章）：

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} \qquad (\Re(s) > 1)
$$

当 $s$ 是实变量且 $s > 1$ 时，这是我们在第六章中已经见过的 $p$-级数。当 $s$ 推广为复数时，$n^{-s} = e^{-s \ln n}$，$\zeta(s)$ 成为一个复变量的函数。这是黎曼 1859 年论文的第一个关键洞察。

## 收敛性

$\zeta(s)$ 的级数定义在右半平面 $\Re(s) > 1$ 上绝对收敛。当 $\Re(s) \leq 1$ 时，级数发散。

绝对收敛意味着我们可以重排各项而不改变和——但更重要的是，它意味着 $\zeta(s)$ 在 $\Re(s) > 1$ 上是**全纯函数**（第十章）。我们可以逐项求导：

$$
\zeta'(s) = -\sum_{n=1}^{\infty} \frac{\ln n}{n^s}, \quad
\zeta''(s) = \sum_{n=1}^{\infty} \frac{(\ln n)^2}{n^s}, \quad \ldots
$$

## 欧拉乘积

在 $\Re(s) > 1$ 的半平面内，$\zeta(s)$ 具有欧拉乘积表示（第十一章）：

$$
\zeta(s) = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}}
$$

两边取对数（使用对数的主分支），得到：

$$
\ln \zeta(s) = \sum_{p} \sum_{k=1}^{\infty} \frac{1}{k \, p^{ks}}
$$

这是将加法（整数）与乘法（素数）联系起来的桥梁。乘积形式在 $\Re(s) > 1$ 内有效——一旦越过这条线，进入临界带，$\zeta(s)$ 的行为就不再简单地由乘积决定，而是由其解析延拓的全局性质决定。

## $\zeta(s)$ 在实轴上的值

当 $s$ 是大于 $1$ 的实数时，$\zeta(s)$ 取一些优美的值。欧拉在 1734 年首次计算了 $\zeta(2)$：

$$
\zeta(2) = \frac{\pi^2}{6} \approx 1.6449
$$

他还证明了更一般的公式：

$$
\zeta(2n) = (-1)^{n+1} \frac{B_{2n} (2\pi)^{2n}}{2(2n)!}
$$

其中 $B_{2n}$ 是伯努利数：$B_2 = \frac{1}{6}$，$B_4 = -\frac{1}{30}$，$B_6 = \frac{1}{42}$，$\ldots$

由此可以计算出：

$$
\zeta(4) = \frac{\pi^4}{90}, \quad
\zeta(6) = \frac{\pi^6}{945}, \quad
\zeta(8) = \frac{\pi^8}{9450}
$$

但对于**奇数正整数**上的值，情况截然不同。$\zeta(3)$（称为 Apéry 常数）直到 1978 年才被证明是无理数。至于 $\zeta(5)$、$\zeta(7)$ 等是否是无理数，至今仍是开放问题。

## $\zeta(s)$ 在 $s \to 1^+$ 时的发散

当 $s$ 从右侧趋近于 $1$ 时，$\zeta(s)$ 发散：

$$
\zeta(s) \sim \frac{1}{s-1} \qquad (s \to 1^+)
$$

更精确地说，在 $s = 1$ 附近有 Laurent 展开：

$$
\zeta(s) = \frac{1}{s-1} + \gamma + \gamma_1 (s-1) + \cdots
$$

其中 $\gamma \approx 0.5772$ 是 Euler-Mascheroni 常数。

## 积分表示

$\zeta(s)$ 有多种积分表示，它们既是理论工具，也是实际计算的基础。通过与 $\Gamma$ 函数的关系（第九章），可以给出：

$$
\zeta(s) = \frac{1}{\Gamma(s)} \int_0^{\infty} \frac{x^{s-1}}{e^x - 1} \, dx \qquad (\Re(s) > 1)
$$

这个公式的推导利用了几何级数 $\frac{1}{e^x-1} = \sum_{n=1}^{\infty} e^{-nx}$ 和逐项积分。

这一表示的重要性不仅在于它确认了 $\zeta(s)$ 与 $\Gamma(s)$ 之间的深层联系，还在于它可以通过围道积分技术推广到整个复平面——这正是黎曼 1859 年论文的出发点。

## $\zeta(s)$ 与素数

$\zeta(s)$ 关于素数的信息可以从欧拉乘积的对数导数中提取：

$$
-\frac{\zeta'(s)}{\zeta(s)} = \sum_{n=1}^{\infty} \frac{\Lambda(n)}{n^s}
$$

回顾第十三章：$\Lambda(n)$ 是 von Mangoldt 函数——在素数幂 $p^k$ 处取值为 $\ln p$，否则为零。这条公式是将 $\zeta(s)$ 的解析性质与素数分布联系起来的直接通道。

## 初步探索：$\zeta(s)$ 的数值面貌

在实轴上 $s > 1$，$\zeta(s)$ 是一个光滑、单调递减的函数，从 $s = 1$ 处的极点开始，渐近地趋近于 $1$（因为 $\zeta(s) \to 1$ 当 $s \to \infty$）。

但如果我们将目光扩展到整个复平面，$\zeta(s)$ 的行为变得极其丰富而复杂。第十七章将讨论如何将这个仅在 $\Re(s) > 1$ 上由级数定义的函数扩展到整个复平面——解析延拓——这或许是最能展示复分析威力的操作之一。

---

> **本章要点**：$\zeta(s) = \sum n^{-s}$ 在 $\Re(s) > 1$ 上绝对收敛，定义了该半平面上的全纯函数。欧拉乘积 $\prod_p (1-p^{-s})^{-1}$ 将加法与乘法联系起来。当 $s=2n$（正偶数）时，$\zeta(s)$ 的值可以通过伯努利数以闭形式表示；奇数正整数处的值则基本未知。积分表示与 $\Gamma$ 函数建立了联系。$-\zeta'/\zeta$ 的 Dirichlet 系数是 von Mangoldt 函数 $\Lambda(n)$。

> **参见**：[第十七章：解析延拓](./chapter-17-analytic-continuation.md) ★★
