---
difficulty = "★★★"
prerequisites = ["IV-16", "V-21"]
paths = ["red"]
keywords = ["L-functions", "Selberg class", "Dirichlet L-functions", "automorphic", "Langlands"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第二十七章：$L$-函数与 Selberg 类

> 难度：★★★ | 路径：🔴 | 前置：第十六、二十一章

## 从 $\zeta(s)$ 到 $L$-函数

$\zeta(s)$ 并非孤立的数学对象——它属于一个巨大的**$L$-函数**家族。广义地说，$L$-函数是一类具有以下共同特征的复变函数：

1. **Dirichlet 级数表示**：$L(s) = \sum_{n=1}^{\infty} \frac{a_n}{n^s}$（在某个右半平面内）
2. **Euler 乘积**：$L(s) = \prod_p (\text{局部因子})$（系数的积性）
3. **解析延拓**：到整个复平面的亚纯延拓
4. **函数方程**：将 $L(s)$ 与 $L(1-s)$ （或其他对称版本）联系起来

$\zeta(s)$ 是最简单的 $L$-函数——所有 $a_n = 1$，局部因子为 $(1 - p^{-s})^{-1}$。

## Dirichlet $L$-函数

第二简单的 $L$-函数系列由 Dirichlet 于 1837 年引入，用于证明有无穷多个素数位于每个合法的算术级数中。

对于 Dirichlet 特征 $\chi$（模 $q$ 的积性周期函数），定义：

$$
L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s} = \prod_p \frac{1}{1 - \chi(p) p^{-s}} \qquad (\Re(s) > 1)
$$

$\chi$ 的周期性意味着 $L(s, \chi)$ 关于模 $q$ 的素数分布携带信息。每个 $L(s, \chi)$ 满足一个函数方程并具有解析延拓。对应的**广义黎曼猜想**（第三十章）断言：$L(s, \chi)$ 的所有非平凡零点的实部均为 $1/2$。

## 自守 $L$-函数

$L$-函数家族中最丰富的来源是**自守形式**。自守形式是定义在对称空间上、具有极强对称性的高度结构化的函数。

每个自守形式 $\pi$ （适当正规化后）关联一个 $L$-函数 $L(s, \pi)$，其系数包含深层算术信息。例如，模形式的 $L$-函数的系数与椭圆曲线的点数有关——这直接引向 Wiles 对费马大定理的证明以及 Birch–Swinnerton-Dyer 猜想。

## Selberg 类

Atle Selberg 于 1989 年提出了**Selberg 类**（$\mathcal{S}$），旨在将"$L$-函数"的概念公理化。

Selberg 类由一个公理集合定义：

1. **Dirichlet 级数**：$F(s) = \sum_{n=1}^{\infty} \frac{a_n}{n^s}$，在 $\Re(s) > 1$ 上绝对收敛，$a_1 = 1$
2. **解析延拓**：$F(s)$ 可以亚纯地延拓到 $\mathbb{C}$，在 $s=1$ 处至多有一个极点
3. **函数方程**：存在因子 $Q > 0$、复数 $\gamma_j$ 和 $\varepsilon$ （$|\varepsilon| = 1$）使得 $\Phi(s) = \varepsilon \overline{\Phi(1 - \bar{s})}$，其中 $\Phi(s) = Q^s \prod \Gamma(\lambda_j s + \mu_j) \, F(s)$
4. **Ramanujan 猜想**：系数 $a_n$ 满足 $a_n = O(n^\varepsilon)$ 对任意 $\varepsilon > 0$ 成立
5. **Euler 乘积**：$\ln F(s) = \sum_{n=1}^{\infty} \frac{b_n}{n^s}$，其中 $b_n = 0$ 除非 $n$ 是素数幂，且 $b_n = O(n^\theta)$ 对某个 $\theta < 1/2$ 成立

$\zeta(s)$ 属于 Selberg 类。Dirichlet $L$-函数、Dedekind $\zeta$ 函数以及所有自守 $L$-函数（在适当正规化后）也属于 Selberg 类。

## 广义黎曼猜想（对 Selberg 类的版本）

Selberg 类的引入使得黎曼猜想可以推广到整个 $L$-函数族：

> **广义黎曼猜想（对 Selberg 类）**：对于 Selberg 类中的每个函数 $F$，$F(s)$ 的所有非平凡零点满足 $\Re(s) = 1/2$。

## 与 Langlands 纲领的联系

Selberg 类与 **Langlands 纲领**之间的联系是当代数学最深刻的主题之一。Langlands 纲领预测：**每个"有算术意义的" $L$-函数都来自于某个自守表示**。如果这一预测正确，Selberg 类将与所有自守 $L$-函数的集合重合。

Langlands 纲领将 RH 置于一个无比宏伟的框架中——LH 不再仅仅是关于 $\zeta(s)$ 的猜想，而是关于整个 $L$-函数宇宙的统一对称原理。

---

> **本章要点**：$L$-函数是具有 Dirichlet 级数、Euler 乘积、解析延拓和函数方程的复变函数族。Dirichlet $L$-函数关联素数在算术级数中的分布。自守 $L$-函数连接 Langlands 纲领与费马大定理。Selberg 类将 $L$-函数概念公理化，黎曼猜想可推广为该类中所有函数的性质。Langlands 纲领预测所有有算术意义的 $L$-函数均来自自守表示。

> **参见**：[第二十八章：Montgomery 对关联猜想](./chapter-28-montgomery.md) ★★★
