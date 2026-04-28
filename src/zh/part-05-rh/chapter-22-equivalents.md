---
difficulty = "★★★"
prerequisites = ["V-21"]
paths = ["red"]
keywords = ["equivalent formulations", "Weil explicit formula", "Li criterion", "Hilbert-Pólya", "operator theory"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第二十二章：等价形式

> 难度：★★★ | 路径：🔴 | 前置：第二十一章

## 黎曼猜想的多种面孔

黎曼猜想的一大魅力在于，它可以被等价地重述为数学中多个不同领域中的陈述。没有哪两个等价表述看起来"相同"——它们的等价性是某种深层数学结构的反映。

## 素数分布的等价

第二十一章中已给出最基本的等价：

**RH** $\iff$ $\pi(x) = \operatorname{Li}(x) + O(\sqrt{x} \ln x)$

更精确地，RH 等价于对任意 $\varepsilon > 0$：

$$
|\pi(x) - \operatorname{Li}(x)| < \frac{1}{8\pi} \sqrt{x} \ln x \quad \text{对所有 } x \geq 2657 \text{ 成立}
$$

这一等价形式直接回答了"黎曼猜想关乎什么"——关乎素数分布的可预测性。

## Mertens 函数的等价

Mertens 函数 $M(x) = \sum_{n \leq x} \mu(n)$ 与 RH 之间的联系由来已久。1897 年，Mertens 本人猜想 $|M(x)| < \sqrt{x}$（Mertens 猜想）。如果 Mertens 猜想成立，RH 也成立。但 1985 年 Odlyzko 和 te Riele 证明 Mertens 猜想（在其强形式下）是错误的——不过反例出现在天文数字的 $x$ 处。

精确的等价表述是：RH $\iff$ $M(x) = O(x^{1/2 + \varepsilon})$ 对任意 $\varepsilon > 0$。

## Li 准则 (1997)

令 $X(n)$ 为 $\xi$ 函数对数导数在 $s=1$ 处的 Taylor 系数构成的序列。华人数学家李祥（Xian-Jin Li）于 1997 年证明：

**RH** $\iff$ 对所有正整数 $n$，序列 $\lambda_n \geq 0$

其中 $\lambda_n = \sum_{\rho} [1 - (1 - 1/\rho)^n]$（求和遍历 $\zeta$ 的非平凡零点）。Li 准则的优雅在于它将一个关于复数位置的陈述转化为一个实数序列的非负性陈述。

## Hilbert-Pólya 猜想

20 世纪初，希尔伯特和波利亚独立提出：黎曼猜想可以通过"找到一个自伴算子（Hermitian operator）$H$，使得其谱（特征值）对应于 $\zeta(s)$ 的非平凡零点"来证明。

具体地说，若存在 Hilbert 空间上的自伴算子 $H$，使得 $H$ 的特征值恰好为 $\zeta$ 的非平凡零点，则由于自伴算子的特征值均为实数，$\zeta$ 非平凡零点的虚部——通过某种变换后——将是实的，即 $\operatorname{Re}(\rho) = 1/2$。

这个猜想是"物理证明 RH"思想路线的源头。在量子力学中，可观测量由自伴算子表示，其谱（特征值）是实的。因此，找到这样一个算子就等于将 $\zeta$ 的零点解释为某个"量子系统"的能级。

## 与随机矩阵理论的联系

Hilbert-Pólya 猜想在 1972 年获得了意想不到的支持。Hugh Montgomery 与物理学家 Freeman Dyson 在一次茶歇时的偶遇揭示了一个惊人的事实：$\zeta$ 非平凡零点之间的间距分布与随机 Hermitian 矩阵（Gaussian Unitary Ensemble，GUE）的特征值间距分布**完全相同**。

包含这一发现的问题将在第二十九章中展开。它表明，如果 Hilbert-Pólya 算子存在，该算子对应的量子系统是"混沌"的（量子混沌）。这一线索至今仍是连接黎曼猜想与理论物理的最强纽带。

## Weil 显式公式

André Weil 于 1952 年提出了显式公式的一般形式，将素数、$\zeta$ 零点和测试函数之间的关系形式化为一个等式。Weil 的公式以分布的语言表达：

$$
\sum_{\rho} \hat{h}(\rho) = h(0) + h(1) - \sum_{p} \sum_{k=1}^{\infty} \frac{\ln p}{p^{k/2}} \left[h(k \ln p) + h(-k \ln p)\right]
$$

其中 $\hat{h}$ 是测试函数 $h$ 的 Mellin 变换。求和遍历 $\zeta(s)$ 的所有非平凡零点。

Weil 显式公式的深刻之处在于它揭示：**RH 等价于对某个正定泛函的非负性**。这一观察与 Connes 的非交换几何进路（第二十五章）密切相关。

## 等价形式的地图

黎曼猜想的等价形式遍布数学各领域：

| 领域 | 等价形式 | 关键词 |
|------|---------|--------|
| 素数分布 | 最优误差项 | $\pi(x) - \operatorname{Li}(x)$ |
| Möbius 函数 | $M(x)$ 的增长 | $O(x^{1/2+\varepsilon})$ |
| 泛函分析 | Hilbert-Pólya 猜想 | 自伴算子 |
| 代数数论 | 广义黎曼猜想 | L-函数 |
| 积分理论 | Li 准则 | $\lambda_n \geq 0$ |
| 随机矩阵 | GUE 统计 | 零点间距 |

所有这些等价形式都在讲述同一个故事：**RH 不仅仅是关于 $\zeta$ 零点的命题——它是关于素数、算子、矩阵与量子混沌的深层统一原理。**

---

> **本章要点**：RH 有多种等价表述，跨越素数分布、Möbius 函数增长、Li 准则、Hilbert-Pólya 算子猜想和 Weil 显式公式。Hilbert-Pólya 猜想将 RH 与自伴算子的谱联系起来，启发了物理路径。蒙哥马利-戴森相遇揭示了零点间距与随机矩阵特征值间距的深层联系。RH 是跨越多个数学领域的统一原理。

> **参见**：[第二十三章：无零点区域](./chapter-23-zero-free-regions.md) ★★★
