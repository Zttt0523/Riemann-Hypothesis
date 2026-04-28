---
difficulty = "★★"
prerequisites = []
paths = ["blue", "red"]
keywords = ["reading list", "roadmap", "learning path", "Langlands", "analytic NT", "spectral theory"]
zh-status = "complete"
en-status = "missing"
en-missing-note = "English version pending"
---

# 附录 C：攻克黎曼猜想——完整阅读地图与渐进学习计划

> 难度：★★ | 路径：🟡🔴 | 前置：无（可作为独立导航使用）

这份附录是一张从"你现在的位置"（数学基础 + 信号处理 + 线性代数）通向 RH 前沿的地图。它按照**解析 → 代数 → 谱**三条进路组织，每层标注了最值得阅读的书籍、论文和人物。

## 学习阶段总览

| 阶段 | 主题 | 目标 | 时间估计 |
|------|------|------|---------|
| **0** | 基础巩固 | 复分析、抽象代数、线性代数进阶 | (已有基础，少量查漏) |
| **1** | 解析数论入门 | 掌握 $\zeta(s)$ 的完整理论 | 3-6 个月 |
| **2** | 代数数论 | 理解素数分解的代数图景 | 6-12 个月 |
| **3** | 自守形式与 L-函数 | 理解 Langlands 纲领的 $\mathrm{GL}_2$ 实例 | 6-12 个月 |
| **4** | 谱理论与非交换几何 | 理解 Hilbert-Pólya 与 Connes 框架 | 6-12 个月 |
| **5** | 三条进路的交汇 | 前沿论文、活跃方向 | 持续 |

总计约 2-3 年可以走完第 1-4 阶段（业余时间），然后进入第 5 阶段的前沿。

---

## 阶段 0：基础巩固（你已有的基础 + 少量查漏）

#### 复分析
- **推荐**：Lars Ahlfors, *Complex Analysis* (1953, 3rd ed. 1979)。无可替代的经典——围道积分、全纯函数、解析延拓，全部清晰到底。
- **补充**：Tristan Needham, *Visual Complex Analysis* (1997)。用几何直观填补 Ahlfors 的抽象——如果你更适应视觉思维，先看这一本。

#### 线性代数进阶
你需要的不再是矩阵运算，而是**算子与谱**的视角。
- **推荐**：Sheldon Axler, *Linear Algebra Done Right* (1995, 3rd ed. 2015)。以算子和特征空间而不是以行列式为中心——这是迈向 Hilbert 空间和谱理论的正确起点。
- **进阶**：Rajendra Bhatia, *Matrix Analysis* (1997)。迹范数、谱范数、特征值扰动——Connes 框架中直接需要的工具。

#### 抽象代数
- **推荐**：Michael Artin, *Algebra* (1991, 2nd ed. 2010)。用对称性（群论）驱动整个叙事——比 Dummit & Foote 更与 Langlands 精神契合。
- **补充**：Joseph Rotman, *Galois Theory* (1990, 2nd ed. 1998)。薄薄一册，Galois 对应的核心原理讲得极为透彻——这是理解 Artin 互反律的前置知识。

---

## 阶段 1：解析数论——掌握 $\zeta(s)$ 的完整理论

这是你目前离 RH 最近的一条进路——你的级数、傅里叶和 Z 变换背景使这里成为自然的第一站。

#### 推荐书籍

1. **Harold M. Edwards**, *Riemann's Zeta Function* (1974)。
   - 整本书围绕黎曼 1859 年论文展开。每一章对应论文中的一个段落。Edwards 在讲解中逐步揭示 Riemann 未言明的计算和直觉——包括 Siegel 发现 Riemann-Siegel 公式的故事。
   - **这本书是所有 RH 阅读的最佳起点**。学完后你将完整理解：$\zeta(s)$ 的级数定义、解析延拓、函数方程、显式公式、零点的数值计算。

2. **Tom M. Apostol**, *Introduction to Analytic Number Theory* (1976)。
   - 数论方向最优雅的入门。前半部分涵盖算术函数、Möbius 反演、Dirichlet 卷积；后半部分涉及 Dirichlet 级数和 $\zeta(s)$ 在实数域上的行为。
   - **先读 Apostol 前半，再读 Edwards，然后回到 Apostol 后半。**

3. **Aleksandar Ivić**, *The Riemann Zeta-Function: Theory and Applications* (1985, 重印 Dover 2003)。
   - Edwards 之后的"进阶读物"。$N(T)$ 计数函数的详细推导、零点密度的各种估计、临界线上 $\zeta(s)$ 的增长速率、幂次矩。是桥梁到当前解析数论前沿的关键文本。

#### 关键论文

- Riemann, B. (1859). *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse.* — 必须读原文，配合 Edwards 逐段讲解。
- Hadamard, J. (1896). *Sur la distribution des zéros de la fonction $\zeta(s)$ et ses conséquences arithmétiques.* — PNT 的第一次证明。
- de la Vallée Poussin, C.-J. (1896). *Recherches analytiques sur la théorie des nombres premiers.* — 同一天宣布的独立证明。
- Hardy, G. H. (1914). *Sur les zéros de la fonction $\zeta(s)$ de Riemann.* — 第一次证明临界线上有无穷多零点。
- Selberg, A. (1942). *On the zeros of Riemann's zeta-function.* — 临界线上正比例零点。

#### 人物

- **G. H. Hardy** — 搜集他所有的 $\zeta(s)$ 论文；写作风格是英语数学散文的巅峰。
- **Atle Selberg** — 迹公式的发明者，他的工作同时出现在解析数论和谱理论中（两个词在他面前没有界限）。
- **Andrew Odlyzko** — 他的个人网站有海量零点数据的开放获取，以及他关于零点间距和 GUE 统计的经典论文。

---

## 阶段 2：代数数论——理解素数分解的代数图景

附录 A 中的"惰性、分裂、分歧"故事需要从这里继续展开。

#### 推荐书籍

1. **Ian Stewart & David Tall**, *Algebraic Number Theory and Fermat's Last Theorem* (1977, 4th ed. 2016)。
   - 从具体例子出发，带读者自然地进入数域、整数环、理想、类群。在你还不知道什么是 Dedekind 域之前，你已经理解什么是理想分解了。

2. **Daniel A. Marcus**, *Number Fields* (1977, 2nd ed. 2018)。
   - 所有代数数论入门书中最可读的一本。素理想的分解行为（惰性、分裂、分歧）用习题一步步展开。**读完 Marcus 能独立计算任何二次域的分解定律。**

3. **Jürgen Neukirch**, *Algebraic Number Theory* (1999, 英译本)。
   - 进阶阅读。从赋值的角度统一局部域与整体域——这是 Langlands 纲领的底层语言。
   - **在读完 Stewart & Tall 以及 Marcus 之后再看 Neukirch**，否则大概率会被抽象程度击退。

#### 关键论文

- Kummer, E. (1847). *Über die Zerlegung der aus Wurzeln der Einheit gebildeten complexen Zahlen in ihre Primfactoren.* — 理想数的诞生。
- Dedekind, R. (1871). *Supplement X* 到 Dirichlet 的 *Vorlesungen über Zahlentheorie* (第 2 版)。— 理想概念的形式定义。
- Artin, E. (1927). *Beweis des allgemeinen Reziprozitätsgesetzes.* — Artin 互反律，将 Galois 群表示与素数分解联系起来。这是 Langlands 纲领的起点。

#### 人物

- **Ernst Kummer** — 对 Fermat 大定理的攻击迫使他在素数分解中发明了"理想数"。读他的原始论文，体会一个理论是如何从"失败的证明尝试"中诞生的。
- **Emil Artin** — 1923-1931 年间关于 L-函数和互反律的系列论文。他的全集是解析-代数交汇处最重要的文献之一。
- **Robert Langlands** — 1967 年致 André Weil 的 17 页信（"Langlands 函子性猜想"的原始陈述），以及他 1970 年的文章 *Problems in the Theory of Automorphic Forms*。

---

## 阶段 3：自守形式与 Langlands 纲领——$\mathrm{GL}_2$ 的实例

从这里开始，你不只是在学定理，你是在学一种新的语言。

#### 推荐书籍

1. **Daniel Bump**, *Automorphic Forms and Representations* (1997)。
   - 从 $\mathrm{GL}_2$ 入手——最简单的情况——逐步建立自守形式的理论。每个抽象概念之前都先给出一个明确的数值例子。**Langlands 入门的最佳英文教材。**

2. **Stephen Gelbart**, *Automorphic Forms on Adèle Groups* (1975)。
   - 薄薄一本，但密度极高。从经典的 $\mathrm{GL}_2$ 自守形式过渡到 adèle 语言。读完 Bump 的 $\mathrm{GL}_2$ 之后，用 Gelbart 过渡到 adèlic 观点。

3. **Jean-Pierre Serre**, *A Course in Arithmetic* (1973)。
   - 极其薄的小册子，但每一章都将初等数论与模形式之间最深层的联系揭示出来。读完这本书你会知道为什么模形式的 Fourier 系数与二次型表示有关。

#### 关键论文

- Hecke, E. (1937). *Über Modulfunktionen und die Dirichletschen Reihen.* — 建立了模形式与 L-函数之间的 Hecke 对应。
- Langlands, R. P. (1967/1970). *Euler Products* 和 *Problems in the Theory of Automorphic Forms.* — 函子性猜想的原始陈述。
- Wiles, A. (1995). *Modular elliptic curves and Fermat's Last Theorem.* — 不仅是费马大定理的证明，也是 Langlands 纲领的最重要检验案例（$\mathrm{GL}_2$ 上的模性提升定理）。

#### 人物

- **Erich Hecke** — 他关于模形式和 Dirichlet 级数的论文是连接数论与调和分析的桥梁。
- **Goro Shimura** — 他和 Taniyama 的工作（Shimura-Taniyama 猜想）最终成为了 Wiles 证明的核心。
- **Pierre Deligne** — 1974 年证明了 Weil 猜想（包括"黎曼猜想的代数几何类比"）。**读他的论文来理解"上同调版本的 RH"是什么意思。**
- **Vladimir Drinfeld** 和 **Laurent Lafforgue** — 两人都因证明函数域上的 Langlands 猜想而获得菲尔兹奖（Drinfeld $\mathrm{GL}_2$，Lafforgue $\mathrm{GL}_n$）。函数域上的成功是数域上的重要参考模板。

---

## 阶段 4：谱理论与非交换几何——Hilbert-Pólya 和 Connes 的框架

这是三条进路中**距离证明 RH 最近的一条**——如果你能成功构造出正确的算子。

#### 推荐书籍

1. **Peter Sarnak**, *Some Applications of Modular Forms* (1990)。
   - 通过 Selberg 特征值猜想展示了如何将"零点 = 算子的谱"这一联系在 $\mathrm{GL}_2$ 的层面上建立起来。**在进入 Connes 之前先读 Sarnak**，否则你无法理解为什么非交换几何需要在这个特定的地方介入。

2. **Alain Connes & Matilde Marcolli**, *Noncommutative Geometry, Quantum Fields and Motives* (2008)。
   - 这就是 Connes 对 RH 进路的完整描述。**不要试图从头到尾读完**——阅读前言和介绍性章节以掌握全局图景，然后深入阅读关于 adèle 类空间与迹映射的章节。
   - 结合 Connes 1998 年的论文 *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* 一起阅读。

3. **Isaac Chavel**, *Eigenvalues in Riemannian Geometry* (1984)。
   - Selberg 迹公式的严格推导。Laplacian 在紧致 Riemann 面上的谱分析。**理解 Selberg 迹公式是理解"算子的谱 ↔ 测地线的长度"这一对偶的本质——而这正是素数（长度） ↔ 零点（谱）对偶的原型。**

4. **M. L. Mehta**, *Random Matrices* (1967, 3rd ed. 2004)。
   - "随机矩阵的圣经"。GUE 统计的完整推导、Wigner 半圆律、Tracy-Widom 分布。这本书与 RH 之间的联系在于你需要理解"什么样的算子会产生 GUE 统计"这个反问题的输入端。

#### 关键论文

- Montgomery, H. (1973). *The pair correlation of zeros of the zeta function.* — 与 Dyson 偶遇的那篇论文。
- Odlyzko, A. M. (1987). *On the distribution of spacings between zeros of the zeta function.* — 大量的数值验证确立了 Montgomery-Dyson 联系为"事实"。
- Connes, A. (1999). *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function.* — Connes 进路的标准参考文献。

#### 人物

- **Alain Connes** — 搜集他 1995-2005 年间关于非交换几何与 RH 的所有论文。
- **Peter Sarnak** — 他在谱理论、随机矩阵与数论交汇处的工作是这三个领域之间的粘合剂。
- **Freeman Dyson** — 量子混沌与随机矩阵理论——这两种理论的统一视角是 Hilbert-Pólya 猜想的必要背景。
- **Michael Berry** — "量子混沌"的命名者。他在 1980 年代的论文首次明确地连接了 $\zeta$ 零点与量子混沌系统。

---

## 阶段 5：前沿——三条进路的交汇点

当你的知识覆盖了上面所有阶段，你会开始注意到**同一定理以不同语言被反复证明**——这就是"投影可以拼回原物体"的信号。

#### 需要追踪的活跃方向

| 方向 | 代表研究者 | 关注的焦点 |
|------|----------|----------|
| 解析围城 | Guth, Maynard | Vinogradov-Korobov 之后的第一个无零点区域突破 (2024) |
| 完美空间与 $p$-进 Langlands | Scholze, Fargues | 几何化 Langlands 纲领（2018–2025）|
| 函数域上的 Langlands | Drinfeld, Lafforgue, Gaitsgory | $\mathrm{GL}_n$ 的几何 Langlands（2024 年证明了全 de Rham 几何 Langlands）|
| 随机矩阵 & 矩猜想 | Keating, Snaith, Conrey, Hughes | 临界线上 $\zeta$ 的高阶矩（GUE 特征多项式积分）|
| 超越 RH | Connes, Consani, Marcolli | 迹映射正定性和非交换空间的全局结构 |
| 解析 Hodge 理论 | Bhatt, Scholze | 新的上同调理论——可能对未来的 RH 上同调类比提供工具 |

#### 从哪里开始追踪

- **ArXiv** 订阅 `math.NT`（数论）, `math.RT`（表示论）, `math.SP`（谱理论）
- 关注 **Terence Tao** 的博客 (`terrytao.wordpress.com`)——他经常对新进展做长篇解读
- 每年关注 **International Congress of Mathematicians (ICM)** 的主旨报告——每个方向的领袖会在那里梳理最近四年的全景
- **Peter Scholze** 在 2018 ICM 报告的 *p-adic geometry* 以及 **Laurent Fargues** 在 2022 ICM 报告的函数域 Langlands 进展
- **Seminaire Bourbaki** 的年度综述——覆盖 Langlands 与数论的最新突破

---

## 给作者的一条附注

你不必成为一个领域的专家才开始进入下一个领域。Langlands 纲领的美妙之处在于：它让你在 $\mathrm{GL}_2$ 层面上**仅用一组方程**（模形式的 Hecke 算子）就同时看到了解析侧（$L$-函数的系数）、代数侧（Galois 表示的迹）和谱侧（自守 Laplace 算子的本征值）。

**不要直接攻击 RH。先学会三个领域各将同一定理证明一次。** （例如：素数定理的复分析证明，素数定理的初等证明，以及在函数域上 Weil 猜想的 étale cohomology 证明。）当你能看出这三种证明其实是同一个证明在三种语言中的投影时，你就看清了整个形状。

---

> **附录要点**：这份阅读地图以五个阶段组织——基础巩固（Ahlfors, Axler, Artin）、解析数论（Edwards, Apostol, Ivić）、代数数论（Marcus, Neukirch）、自守形式与 Langlands（Bump, Gelbart, Serre）、谱理论与非交换几何（Connes, Sarnak, Mehta）。每个阶段标注了最值得阅读的书籍、论文和人物。前沿方向包含 Guth-Maynard 无零点区域突破、几何 Langlands（Scholze-Fargues）和随机矩阵矩猜想等。

> **阅读建议**：先学会三个领域各自将同一定理证明一次，直到你能看出三个证明是同一个证明的投影。
