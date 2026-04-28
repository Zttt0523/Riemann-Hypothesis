---
difficulty = "★★"
prerequisites = ["IV-16", "IV-17"]
paths = ["green", "blue", "red"]
keywords = ["Riemann Hypothesis", "1859 paper", "critical line", "Hilbert", "Millennium"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English translation pending"
---

# 第二十一章：黎曼猜想的陈述与历史

> 难度：★★ | 路径：🟢🟡🔴 | 前置：第十六、十七章

## 正式陈述

> **黎曼猜想（Riemann Hypothesis，RH）**：黎曼 $\zeta$ 函数的所有非平凡零点的实部均为 $\frac{1}{2}$。

等价地说：若 $\zeta(\rho) = 0$ 且 $0 < \operatorname{Re}(\rho) < 1$，则 $\operatorname{Re}(\rho) = \frac{1}{2}$。

这是数学中最著名、最重要的未解问题。它简单到可以在一行内写出，深刻到足以让全世界最优秀的数学家耗费一生也无法攻破。

## 黎曼 1859 年原文

黎曼在其 1859 年论文的第六页首次提出了这一猜想。他用德语写道（戴德金 1876 年版）：

> "Man findet nun in der That etwa so viel reelle Wurzeln innerhalb dieser Grenzen, und es ist sehr wahrscheinlich, dass alle Wurzeln reell sind. Hiervon wäre allerdings ein strenger Beweis zu wünschen; ich habe indess die Aufsuchung desselben, nach einigen flüchtigen vergeblichen Versuchen vorläufig bei Seite gelassen, da er für den nächsten Zweck meiner Untersuchung entbehrlich schien."

钱译："在这些界限内确实可以找到大约这么多实根，并且所有根很可能都是实的。当然，人们希望得到一个严格的证明；然而，在几次短暂的失败尝试后，我暂时将这个证明搁置一旁，因为它对于我当前的研究目标似乎不是必需的。"

值得注意的几点：
1. **"所有根很可能都是实的"**：这里的"根"指 $\xi$ 函数的零点，当应用于 $\xi$ 函数时，"实"意味着零点位于 $\operatorname{Re}(s) = 1/2$ 上。因此"所有根都是实的"等价于黎曼猜想的现代陈述。
2. **"几次短暂的失败尝试"**：黎曼试图证明自己的猜想但失败了。此后超过 160 年里，无人成功。
3. **"对于当前目标似乎不是必需的"**：黎曼的主要目标是推导 $\pi(x)$ 的显式公式——一个更为实际的目标——而他的猜想只是实现该目标的一条更优路径。

## 黎曼猜想的等价表述

以下是黎曼猜想最直接的等价表述。

### 素数分布等价

黎曼猜想等价于素数定理的误差项达到最优：

$$
\pi(x) = \operatorname{Li}(x) + O(\sqrt{x} \ln x)
$$

换句话说，黎曼猜想成立当且仅当素数计数函数与对数积分之间的偏差不超过 $x^{1/2}$ 乘以对数因子。

### Mertens 函数等价

Mertens 函数定义为 Möbius 函数的求和：

$$
M(x) = \sum_{n \leq x} \mu(n)
$$

RH 等价于：$M(x) = O(x^{1/2 + \varepsilon})$ 对任意 $\varepsilon > 0$ 成立。

### $\zeta$ 函数的对数导数

RH 等价于：$\frac{\zeta'(s)}{\zeta(s)}$ 在半平面 $\operatorname{Re}(s) > 1/2$ 内解析（除去 $s = 1$ 处的极点在 $\operatorname{Re}(s) = 1/2$ 的右侧）。

### Robin 不等式

1984 年，法国数学家 Guy Robin 证明：RH 等价于对所有 $n \geq 5041$ 成立：

$$
\sigma(n) < e^{\gamma} n \ln \ln n
$$

其中 $\sigma(n)$ 是 $n$ 的除数和。这是一个极不寻常的等价表述——一个关于除数和的不等式居然等价于关于 $\zeta$ 零点的猜想。

## 黎曼猜想的历史里程碑

| 年份 | 事件 |
|------|------|
| **1859** | 黎曼提出猜想 |
| **1900** | 希尔伯特将其列为 23 个问题之八 |
| **1914** | 哈代证明临界线上有无穷多零点 |
| **1942** | 塞尔伯格证明正比例零点在临界线上 |
| **1974** | 莱文森证明至少 $1/3$ 零点在临界线上 |
| **1989** | Conrey 证明至少 $2/5$ 零点在临界线上 |
| **2000** | 克雷数学研究所宣布其为千禧年大奖难题 |
| **2020s** | 超过 $10^{13}$ 零点经数值验证位于临界线上 |

## 希尔伯特的赞词

希尔伯特在 1900 年巴黎 ICM 演讲中对黎曼猜想的描述已成为名言：

> "如果我在沉睡一千年后醒来，我的第一个问题将是：黎曼猜想被证明了吗？"

他也颇为乐观地表示：

> "如果我们从催眠中醒来，这个问题也许已经解决了。"

超过 125 年过去了，希尔伯特的乐观预期落空了。

## 为什么黎曼猜想如此困难？

黎曼猜想困难的根源在于它所处的数学"间隙"：它关于一种特定函数（$\zeta$）的特定性质（零点），而证明这一性质所需的理解，似乎要求对整个解析数论大厦——甚至数学本身——有更深一层的洞察。每一个提出证明的尝试，无论是成功的还是失败的，都揭示了新的数学领域。困难既是诅咒也是祝福：黎曼猜想的难度推动了整个学科的发展。

---

> **本章要点**：黎曼猜想断言 $\zeta(s)$ 所有非平凡零点满足 $\operatorname{Re}(s) = 1/2$。黎曼于 1859 年提出，希尔伯特于 1900 年列为第八问题，克雷研究所于 2000 年列为千禧年大奖难题。RH 等价于素数定理达到最优误差估计 $O(x^{1/2} \ln x)$。Mertens 猜想、Robin 不等式等多种表述均等价于 RH。

> **参见**：[第二十二章：等价形式](./chapter-22-equivalents.md) ★★★
