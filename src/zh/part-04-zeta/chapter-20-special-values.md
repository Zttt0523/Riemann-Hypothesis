---
difficulty = "★★★"
prerequisites = ["IV-18"]
paths = ["red"]
keywords = ["special values", "Riemann-Siegel", "zeta on critical line", "numerical computation", "Hardy Z-function"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第二十章：特殊值与 Riemann-Siegel 公式

> 难度：★★★ | 路径：🔴 | 前置：第十八章

## $\zeta(s)$ 在实轴上的特殊值

第十六章已介绍了正偶数处的值：

$$
\zeta(2n) = (-1)^{n+1} \frac{B_{2n} (2\pi)^{2n}}{2(2n)!}
$$

而函数方程允许我们计算负整数处的值：

$$
\zeta(1 - 2n) = -\frac{B_{2n}}{2n} \qquad (n \geq 1)
$$

由此得到：$\zeta(-1) = -1/12$（著名的"全体自然数之和），$\zeta(-3) = 1/120$，$\zeta(-5) = -1/252$。注意这是解析延拓给出的值，而非级数求和——级数 $\sum n$ 当然是发散的。

对于**正奇数整数**上的值，情况截然不同。$\zeta(3)$ 于 1978 年被 Apéry 证明为无理数。$\zeta(5)$、$\zeta(7)$ 等是否无理数，至今仍是开放问题。已知有无穷多个正奇数 $\zeta$ 值是无理数，但具体是哪些——尚不清楚。

## $\zeta(s)$ 在临界线上的值

黎曼猜想的核心舞台是临界线 $\Re(s) = \frac{1}{2}$。沿着这条直线，$\zeta(\frac{1}{2} + it)$ 是 $t \in \mathbb{R}$ 的复值函数。

定义 **Hardy $Z$ 函数**：

$$
Z(t) = e^{i\theta(t)} \, \zeta\!\left(\frac{1}{2} + it\right), \qquad
\theta(t) = \arg\left[\pi^{-it/2} \, \Gamma\!\left(\frac{1}{4} + \frac{it}{2}\right)\right]
$$

$Z(t)$ 具有以下性质：
- $Z(t)$ 是 $t$ 的**实值**函数——当 $\zeta$ 在临界线上时
- $Z(t)$ 的零点恰好对应于 $\zeta(s)$ 在临界线上的零点
- $|Z(t)| = |\zeta(\frac{1}{2} + it)|$

$Z(t)$ 是验证黎曼猜想的数值实验的基本工具。若在某一高度 $t$ 处 $Z(t)$ 改变了符号，则 $\zeta$ 在该高度附近的临界线上有一个零点。

## Riemann-Siegel 公式

1932 年，西格尔（Carl Ludwig Siegel）在哥廷根大学图书馆深入研究黎曼遗留的未发表手稿时，做出了一个惊人的发现。在那些未被管家烧毁的残页中，西格尔发现黎曼已经发展出了一种用于计算 $\zeta(1/2 + it)$ 的高效数值方法——**Riemann-Siegel 公式**。

$$

Z(t) \approx 2\sum_{n=1}^{\lfloor \sqrt{t/(2\pi)} \rfloor} \frac{\cos(\theta(t) - t \ln n)}{\sqrt{n}} + R(t)

$$

其中 $R(t)$ 是渐近误差项。这个公式的计算量仅约为 $\sqrt{t}$——远远优于直接求和 $t$ 项。正是使用这个公式，黎曼手工计算了前几个非平凡零点，得到了高度精确的结果。

西格尔于 1932 年发表了这个公式的详细推导。H. M. Edwards 在他的经典著作 *Riemann's Zeta Function*（1974）中盛赞了这一发现："黎曼将这些计算秘藏了七十余年，而它们展示了一种数值技术，其精巧程度远远超越了同时代的任何人。"

## 数值验证

自黎曼以来，数字计算机已计算出天文数字级别的 $\zeta$ 零点——全部位于临界线上。截至 2020 年代，已验证超过 $10^{13}$ 个零点全部满足 $\Re(s) = 1/2$。仅有的离群零点将意味着计算机的计算有误，但**没有一个反例被发现**。

这些数值证据是支持黎曼猜想为真的最有力论据之一，但并非证明。数学史上有过这样的先例：一个猜想在 $10^{10}$ 个实例中成立，却最终被发现是错误的。

Riemann-Siegel 公式至今仍被用于高精度零点计算——一个半世纪前的数学洞察力至今活在现代超级计算机中。

## $\zeta(s)$ 的普遍性（Universality）

1975 年，苏联数学家沃罗宁（Sergei Voronin）证明了一个惊人的定理：$\zeta(s)$ 在临界带内具有**普遍性**（universality）。粗略地说，任何"行为良好"的解析函数都可以通过 $\zeta(s)$ 的适当平移来任意精度地逼近。这意味着 $\zeta(s)$ 的图形中包含了所有可能的解析行为——一个函数，包含了数学的全部复杂性。

---

> **本章要点**：$\zeta(-1) = -1/12$ 等负整数值通过函数方程与伯努利数联系。$Z(t)$ 是研究临界线上 $\zeta$ 行为的实值工具。Riemann-Siegel 公式以 $\sqrt{t}$ 的计算量高效计算 $\zeta(1/2+it)$——由黎曼秘密发现，西格尔于 1932 年公开。超过 $10^{13}$ 个零点的数值验证一致支持黎曼猜想。$\zeta(s)$ 的普遍性定理表明它包含了所有可能的解析行为。

> **继续阅读**：[第五部：黎曼猜想——深入核心](../part-05-rh/chapter-21-statement-history.md) ★★
