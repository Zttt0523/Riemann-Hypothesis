---
difficulty = "★★★"
prerequisites = ["IV-19"]
paths = ["red"]
keywords = ["Lindelöf Hypothesis", "growth", "critical line", "subconvexity", "convexity bound"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第二十六章：Lindelöf 猜想

> 难度：★★★ | 路径：🔴 | 前置：第十九章

## 黎曼猜想的"小表弟"

Lindelöf 猜想通常被称为黎曼猜想的"小表弟"——它的结论比 RH 弱，但两者之间有着密切的逻辑联系：**RH 蕴含 Lindelöf 猜想，但逆命题可能不成立**。

Lindelöf 猜想是关于 $\zeta(s)$ 在临界线上增长速率的命题——不同于 RH 关于零点位置的命题，它关注函数值的幅度。

## 陈述

> **Lindelöf 猜想**：对任意 $\varepsilon > 0$，
> $$
> \zeta\!\left(\frac{1}{2} + it\right) = O(t^{\varepsilon}) \qquad (t \to \infty)
> $$

换句话说：$\zeta$ 在临界线上的值增长得"比 $t$ 的任何正幂次都慢"。等价地，对于任何 $\varepsilon > 0$，存在常数 $C_\varepsilon$，使得 $|\zeta(1/2 + it)| \leq C_\varepsilon \, t^\varepsilon$ 对所有充分大的 $t$ 成立。

## 与 RH 的关系

黎曼猜想蕴含 Lindelöf 猜想。在 RH 下，Lindelöf 猜想的陈述实际上可以改进为 $\zeta(1/2 + it) = O(\exp(c \ln t / \ln\ln t))$。

但 Lindelöf 猜想**不蕴含** RH。有可能 Lindelöf 猜想为真——$\zeta$ 在临界线上的值增长非常缓慢——而某些零点仍然偏离了临界线。这种可能性使 Lindelöf 猜想成为一个比 RH 更容易独立研究的目标。

## 已知结果：凸性界与次凸性界

**凸性界**（convexity bound）：来自 Phragmén-Lindelöf 原理的一般复分析论证给出了：

$$
\zeta\!\left(\frac{1}{2} + it\right) = O(t^{1/4})
$$

这是无需任何额外输入即可证明的"通用"界限。

**Weyl 界**（subconvexity bound）：Hermann Weyl 改进了这一界限：

$$
\zeta\!\left(\frac{1}{2} + it\right) = O(t^{1/6 + \varepsilon})
$$

Weyl 的论证使用了一种精妙的指数和估计。此后 Weyl 界本身也被多次改进。

目前已知的最优界由 Bourgain（2017 年）给出：

$$
\zeta\!\left(\frac{1}{2} + it\right) = O(t^{13/84 + \varepsilon}) \approx O(t^{0.1548})
$$

从凸性界 $1/4$ 到 Lindelöf 猜想 $0$ 的距离上，我们大约走了一半多。

## Lindelöf 猜想的意义

Lindelöf 猜想之所以重要，不仅因为它与 RH 的联系：

- 它等价于 $\zeta$ 零点的垂直间距分布方面的强大结果
- 它在关于自守 $L$-函数的次凸性（subconvexity）问题中扮演核心角色——这是现代解析数论最活跃的领域之一
- 它是数论中"次凸性问题"家族中最简单的实例——在这些问题中，凸性界是一个来自复分析基本原理的"免费"界限，而次凸性需要深入的算术信息

次凸性问题的研究在过去二十年中取得了非凡的进展，其中一些最深刻的突破来自张伟、Kowalski、Michel 和 Venkatesh 等人的工作。

---

> **本章要点**：Lindelöf 猜想断言 $\zeta(1/2 + it) = O(t^\varepsilon)$——$\zeta$ 在临界线上的增长比 $t$ 的任何正幂都慢。RH 蕴含 Lindelöf 猜想，但逆命题不成立。凸性界 $O(t^{1/4})$ 已通过子凸性技术改进到 Bourgain 的 $O(t^{0.1548})$。Lindelöf 猜想是数论中更广泛的"次凸性问题"家族的一部分。

> **参见**：[第二十七章：L-函数与 Selberg 类](./chapter-27-l-functions.md) ★★★
