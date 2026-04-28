---
difficulty = "★"
prerequisites = ["II-08"]
paths = ["blue", "red"]
keywords = ["Riemann integral", "FTC", "improper integral", "Gamma function", "Mellin transform"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第九章：积分学

> 难度：★ | 路径：🟡🔴 | 前置：第八章

## 积分的两种视角

**积分**可以从两个角度理解：

1. **反导数视角**：$F$ 是 $f$ 的原函数，如果 $F'(x) = f(x)$。则 $\int_a^b f(x)\,dx = F(b) - F(a)$。
2. **黎曼和视角**：积分是"无穷多个无穷小矩形面积之和"的极限。

第二种视角是黎曼本人在其任教资格论文（1853 年）中严格定义的，因此称为**黎曼积分**。

## 黎曼积分的严格定义

将区间 $[a, b]$ 划分为 $n$ 个子区间，分割记为 $P = \{x_0, x_1, \ldots, x_n\}$，其中 $a = x_0 < x_1 < \cdots < x_n = b$。在每个子区间 $[x_{i-1}, x_i]$ 中任选一点 $x_i^*$。**黎曼和**为：

$$
S(P, f) = \sum_{i=1}^{n} f(x_i^*) \, \Delta x_i, \quad \Delta x_i = x_i - x_{i-1}
$$

> **定义**：若存在数 $I$ 使得对于任意 $\varepsilon > 0$，存在 $\delta > 0$，当分割的最大宽度 $\|P\| < \delta$ 时，无论 $x_i^*$ 如何选取，均有 $|S(P, f) - I| < \varepsilon$，则称 $f$ 在 $[a, b]$ 上黎曼可积，$I$ 称为黎曼积分，记作 $\int_a^b f(x)\,dx$。

这个定义的精妙之处在于：它允许 $f$ 是不连续的——只要"坏点"不太多。一个函数黎曼可积的充要条件是：其不连续点构成的集合是零测集（Lebesgue 准则）。

## 微积分基本定理（FTC）

导数与积分之间的联系由**微积分基本定理**（Fundamental Theorem of Calculus）给出：

> **FTC 第一部分**：若 $F'(x) = f(x)$，且 $f$ 黎曼可积，则：
> $$
> \int_a^b f(x)\,dx = F(b) - F(a)
> $$

> **FTC 第二部分**：若 $f$ 在 $[a, b]$ 上连续，定义 $G(x) = \int_a^x f(t)\,dt$，则 $G'(x) = f(x)$。

FTC 统一了微积分的两大分支——微分学和积分学——揭示了它们本质上互为逆运算。

## 反常积分

有时积分区间是无穷的，或被积函数在某些点处无界。这些称为**反常积分**（improper integrals），通过极限定义：

$$
\int_a^{\infty} f(x)\,dx = \lim_{b \to \infty} \int_a^b f(x)\,dx
$$

例如：
- $\int_1^{\infty} \frac{1}{x^s}\,dx$ 在 $s > 1$ 时收敛，在 $s \leq 1$ 时发散——与 $p$-级数完全一致（积分判别法！）。
- $\int_0^{\infty} e^{-x} x^{s-1}\,dx$ 对所有 $s > 0$ 收敛，这就是 $\Gamma(s)$ 的定义。

## $\Gamma$ 函数：阶乘的推广

在 $\zeta$ 函数的研究中，最重要的特殊函数之一是 $\Gamma$ 函数（Gamma function），由欧拉于 1729 年引入：

$$
\Gamma(s) = \int_0^{\infty} e^{-t} \, t^{s-1} \, dt \qquad (\Re(s) > 0)
$$

$\Gamma$ 函数将阶乘从整数推广到复数。基本性质：

- $\Gamma(n) = (n-1)!$ 对所有正整数 $n$ 成立
- $\Gamma(s+1) = s\,\Gamma(s)$（函数方程）
- $\Gamma(s)$ 可以解析延拓到整个复平面（除 $s = 0, -1, -2, \ldots$ 处的简单极点）

$\Gamma$ 函数出现在 $\zeta(s)$ 的函数方程中（第十八章），将 $\zeta(s)$ 与 $\zeta(1-s)$ 联系起来。这是理解黎曼猜想的核心工具。

## 积分与 Mellin 变换

许多特殊函数可以通过积分表示定义。$\zeta(s)$ 也有积分表示——例如：

$$
\zeta(s) = \frac{1}{\Gamma(s)} \int_0^{\infty} \frac{x^{s-1}}{e^x - 1}\,dx \qquad (\Re(s) > 1)
$$

这种类型的积分表示属于 **Mellin 变换**的范畴，在解析数论中广泛应用。

---

> **本章要点**：黎曼积分通过划分的极限精确定义了曲线下的面积。微积分基本定理统一了微分与积分。反常积分处理无穷区间和无界函数。$\Gamma$ 函数将阶乘推广到复数，是 $\zeta$ 函数函数方程的关键组成部分。

> **参见**：[第十章：复数与复变函数](./chapter-10-complex-numbers.md) ★★
