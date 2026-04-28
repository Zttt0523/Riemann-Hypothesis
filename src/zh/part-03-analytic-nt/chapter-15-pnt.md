---
difficulty = "★★"
prerequisites = ["III-13", "III-14"]
paths = ["green", "blue", "red"]
keywords = ["prime number theorem", "PNT", "Chebyshev", "Hadamard", "de la Vallée Poussin", "psi"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第十五章：素数定理

> 难度：★★ | 路径：🟢🟡🔴 | 前置：第十三、十四章

## 素数定理的陈述

**素数定理**（Prime Number Theorem，简称 PNT）是解析数论皇冠上的明珠——在黎曼猜想之前，它是整个领域最重大的成果。

记 $\pi(x)$ 为不超过 $x$ 的素数个数：

$$
\pi(x) = \#\{p \leq x : p \text{ 是素数}\}
$$

> **素数定理**：
> $$
> \pi(x) \sim \frac{x}{\ln x} \qquad (x \to \infty)
> $$
> 即 $\lim_{x \to \infty} \frac{\pi(x)}{x / \ln x} = 1$。

更精确的版本使用**对数积分** $\mathrm{Li}(x)$：

$$
\mathrm{Li}(x) = \int_2^x \frac{dt}{\ln t}
$$

$\mathrm{Li}(x)$ 是比 $x / \ln x$ 更好的近似。素数定理的等价陈述是：

$$
\pi(x) \sim \mathrm{Li}(x)
$$

## 从高斯到切比雪夫

高斯和勒让德在十八世纪末猜想了 PNT，但无法证明。第一个实质性进展来自帕夫努蒂·切比雪夫（Pafnuty Chebyshev），他在 1850 年左右证明：若极限 $\lim_{x \to \infty} \frac{\pi(x)}{x/\ln x}$ 存在，则必为 $1$。

切比雪夫还证明了 $\pi(x)$ 被夹在两个常数倍之间。他引入的切比雪夫函数成为后来的标准技术工具：

$$
\vartheta(x) = \sum_{p \leq x} \ln p, \qquad \psi(x) = \sum_{p^k \leq x} \ln p = \sum_{n \leq x} \Lambda(n)
$$

PNT 等价于 $\psi(x) \sim x$。

## 两个关键引理

1896 年证明 PNT 的核心在于两条关于 $\zeta(s)$ 的事实。

**引理 1**：$\zeta(s)$ 在 $\Re(s) = 1$ 的直线上没有零点。

也就是说，$\zeta(1 + it) \neq 0$ 对所有实数 $t$ 成立。这是 PNT 证明中的技术关键。

**引理 2**：$\zeta(s)$ 在 $s = 1$ 处有一个简单极点，留数为 $1$。换言之，在 $s = 1$ 附近，

$$
\zeta(s) \sim \frac{1}{s-1}
$$

第一个性质是数论性质的——它阻止了素数分布中出现系统性的偏差。第二个性质是分析性质的——它决定了素数分布的"主导项"。

## 证明策略概述

使用 Perron 公式（第十四章），将 $\psi(x)$ 表示为复积分：

$$
\psi(x) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \left(-\frac{\zeta'(s)}{\zeta(s)}\right) \frac{x^s}{s} \, ds, \quad c > 1
$$

将被积函数的积分路径向左移动。在移动过程中：

1. $-\frac{\zeta'(s)}{\zeta(s)}$ 在 $s = 1$ 处有一个简单极点（来自 $\zeta(s)$ 的极点），留数为 $1$，贡献主导项 $x$
2. $s = 0$ 处的极点贡献常数项
3. $\zeta(s)$ 的**每个非平凡零点** $\rho$ 贡献振荡项 $\frac{x^\rho}{\rho}$
4. $\zeta(s)$ 的**每个平凡零点**（$s = -2, -4, -6, \ldots$）贡献可忽略的小项

于是：

$$
\psi(x) = x - \sum_{\rho} \frac{x^\rho}{\rho} - \ln(2\pi) - \frac{1}{2}\ln(1 - x^{-2})
$$

这就是**黎曼显式公式**的一种形式。

## 证明中哪一步阻止了更强的结论？

Hadamard 和 de la Vallée Poussin 的证明仅使用了 $\zeta(1+it) \neq 0$ 这一事实，而没有使用黎曼猜想的全部力量——后者断言 $\zeta(\frac{1}{2} + it)$ 才是非零的（除零点外）。

由于 $\zeta(1+it) \neq 0$ 是一个较弱的陈述，我们只能得到较弱的误差项：$\pi(x) = \mathrm{Li}(x) + O(x e^{-c\sqrt{\ln x}})$。

如果黎曼猜想成立，则可以获得极精确的误差估计：$\pi(x) = \mathrm{Li}(x) + O(\sqrt{x} \ln x)$。反之亦然——**黎曼猜想等价于素数定理的误差项达到 $O(x^{1/2+\varepsilon})$**。

## PNT 的意义

素数定理的证明是十九世纪数学的巅峰成就之一。它表明：

1. 分析方法（复分析）可以解决数论中纯粹的离散问题
2. 黎曼的直觉——通过复变函数研究素数——是极为深刻的洞见
3. $\zeta(s)$ 的零点位置精确地决定了素数分布的精细结构

但 PNT 也让我们看到了黎曼猜想的必要性。PNT 回答了"素数大致有多少"——黎曼猜想将回答"素数到底是如何分布的"。

---

> **本章要点**：素数定理 $\pi(x) \sim x/\ln x$ 由 Hadamard 和 de la Vallée Poussin 于 1896 年独立证明。证明的关键步骤是展示 $\zeta(s)$ 在 $\Re(s) = 1$ 上没有零点。Perron 公式和切比雪夫函数是证明的技术基础。PNT 给出了素数分布的"一阶近似"；黎曼猜想等价于该近似的误差项达到最低可能阶 $O(x^{1/2+\varepsilon})$。

> **继续阅读**：[第四部：黎曼 $\zeta$ 函数](../part-04-zeta/chapter-16-zeta-definition.md) ★★
