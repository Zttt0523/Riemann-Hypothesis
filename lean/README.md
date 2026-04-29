# Lean 形式化 / Lean Formalization

使用 [Lean 4](https://lean-lang.org/) + [Mathlib4](https://github.com/leanprover-community/mathlib4) 
将黎曼猜想百科全书中的核心定理形式化。

## 动机

- 形式化是数学的"第四种语言"——在解析、代数、谱三种语言之外，增加逻辑/计算语言
- 每一个定理的机器验证都要求逐层理解全部前置概念
- Lean 是学习数学的最佳工具之一——它不接受任何"显然"

## 形式化路线图

### Phase 1：定义层 — 建立话语体系

- [ ] 算术函数：Möbius $\mu$, von Mangoldt $\Lambda$, Euler $\varphi$
- [ ] Dirichlet 级数：收敛横坐标、形式级数
- [ ] 素数计数 $\pi(x)$ 和 Chebyshev 函数 $\psi(x)$
- [ ] Riemann $\zeta$ 函数：级数定义、Euler 乘积

### Phase 2：关键定理 — 验证已知结论

- [ ] Euler 乘积公式的严格证明
- [ ] $\zeta(s)$ 在 $\Re(s) > 1$ 上的解析性
- [ ] 素数有无穷多个（Euler 乘积解析证明）
- [ ] Prime Number Theorem（Mathlib4 已有形式化）

### Phase 3：复分析工具链

- [ ] 解析延拓
- [ ] $\zeta(s)$ 的函数方程
- [ ] $\Gamma$ 函数及其关键恒等式

### Phase 4：RH 陈述层 — 精确陈述猜想

- [ ] $\zeta(s)$ 的平凡零点与非平凡零点的形式化定义
- [ ] 黎曼猜想的精确陈述（对所有非平凡零点 $\Re(\rho) = 1/2$）
- [ ] RH 的等价形式（素数定理误差项、Mertens 函数）

## 参考

- [Mathlib4 文档](https://leanprover-community.github.io/mathlib4_docs/)
- [Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/)
- [The Mechanics of Proof](https://hrmacbeth.github.io/math2001/)
