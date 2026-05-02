# Lean 形式化 / Lean Formalization

使用 [Lean 4](https://lean-lang.org/) + [Mathlib4](https://github.com/leanprover-community/mathlib4)
将黎曼猜想百科全书中的核心定理形式化。

---

## Lean 在这个项目中的三重角色

| 角色 | 说明 |
|------|------|
| **学习工具** | 在 Lean 中重写一个定理的证明，等于在原子层面逐条验证自己的理解。没有模糊地带——编译器要么接受，要么拒绝 |
| **精确陈述** | 自然语言中有歧义的句子（"所有非平凡零点…"）在 Lean 中被翻译为无歧义的逻辑公式 |
| **未来资产** | 如果有朝一日 RH 被证明，这个项目将是第一时间可被机器验证的形式化版本 |

---

## 快速开始

### 构建

```bash
cd lean/lean-rh
source ~/.elan/env          # 加载 Lean 工具链
lake build                  # 编译（含 Mathlib，首次可能耗时）
```

当前状态：**8366 个构建任务全部通过。**

### 打开交互式环境

```bash
# 在 VS Code 中打开（推荐——安装 lean4 扩展后，你会获得实时错误提示、类型查看和自动补全）
code lean/lean-rh

# 或在命令行中玩耍
lake exe lean --run RiemannHypothesis/Basic.lean
```

---

## 你可以做什么：三层深度

### 第一层：阅读——看看"精确陈述"长什么样

打开 `lean/lean-rh/RiemannHypothesis/Basic.lean`。这是目前的形式化内容：

```lean
-- 使用 Mathlib4 内置的 riemannZeta 函数
-- ⚠ 这是一个未完成的占位定义——真正的 ζ(s) 包含级数、解析延拓、函数方程

/-- 黎曼猜想的形式化陈述 -/
def RiemannHypothesisStatement : Prop :=
  ∀ s : ℂ,                -- 对所有复数 s
    riemannZeta s = 0 →   -- 如果 ζ(s) = 0
    Complex.re s > 0 →    -- 且 s 在临界带内 (0 < Re(s) < 1)
    Complex.re s < 1 →
    Complex.re s = 1/2    -- 则其实部必为 1/2
```

这是 RH 的**无歧义版本**。没有任何一个词是模糊的；每一个符号都由 Lean 内核验证为类型正确的。

### 第二层：修改——引入显式公式的一条腿

打开 `Basic.lean`，在文件末尾添加你的第一个引理：

```lean
-- 练习：证明 ζ(s) 的平凡零点在 s = -2 处
example : riemannZeta (-2 : ℂ) = 0 := by
  -- 留空——这是一个待证明的命题
  sorry
```

保存后，VS Code 会在 `sorry` 处显示一个警告（证明不完整）。你的目标是逐步替换 `sorry` 为实际的证明步骤。

### 第三层：形式化——从书中的定理出发

附录 C 推荐你从五个阶段逐步深入。Lean 可以作为每一个阶段的"练习本"：

| 阶段 | 在 Lean 中可以做的事 | 难度 |
|------|-------------------|------|
| 1 解析数论 | 证明 Euler 乘积公式、Möbius 反演 | ★★ |
| 2 代数数论 | 证明 $p \equiv 3 \pmod{4}$ 在 $\mathbb{Z}[i]$ 中保持惰性 | ★★★ |
| 3 自守形式 | 定义 Hecke 算子，验证其在模形式上的基本性质 | ★★★★ |
| 4 谱理论 | 陈述 Hilbert-Pólya 猜想、Selberg 迹公式 | ★★★★★ |
| 5 前沿 | 将 Guth-Maynard (2024) 的核心定理形式化 | ★★★★★+ |

---

## 在 VS Code 中工作的样子

1. 用 `code lean/lean-rh` 打开项目
2. Lean 4 扩展会自动激活
3. 右侧出现 **Lean Infoview** 面板——这是你的"思想实验显示器"
4. 将光标放在任意符号上，Infoview 会显示其**类型**和**当前目标**
5. 输入 `by` 后，Infoview 显示待证明的目标（goal）
6. 逐行写证明，目标会随之变化——直到最后显示 `No goals`（证明完成）

这就是"机器验证的数学思维"——每一步都必须严格可推导，没有"显然"的余地。

---

## 一个具体的练习："素数有无穷多个"的形式化

这本书第十二章讲到了欧几里得的经典证明。下面是其在 Lean 中的完整版本（Mathlib4 已有此证明，这里展示其结构）：

```lean
import Mathlib

theorem exists_infinite_primes : ∀ n : ℕ, ∃ p ≥ n, Nat.Prime p := by
  intro n
  -- 构造 N = n! + 1
  let N := n.factorial + 1
  -- 取 N 的最小素因子 p
  have hp : Nat.Prime (Nat.minFac N) := Nat.minFac_prime (by
    have : n.factorial > 0 := Nat.factorial_pos n
    omega)
  -- p 必然 ≥ n（因为 p 不整除 n!，所以 p ≥ n+1 > n）
  have hp_ge : Nat.minFac N ≥ n := ...
  exact ⟨Nat.minFac N, hp_ge, hp⟩
```

练习：在 `Basic.lean` 中补全上述证明的 `...` 部分。

---

## 常用命令速查

| 命令 | 说明 |
|------|------|
| `lake build` | 编译整个项目 |
| `lake build RiemannHypothesis` | 只编译指定库 |
| `#check riemannZeta` | 查看 riemannZeta 的类型 |
| `#eval 1+1` | 计算一个表达式 |
| `example : ... := by ...` | 匿名引理／练习 |
| `theorem` / `lemma` | 命名的定理或引理 |
| `import Mathlib` | 使用数学库 |

---

## 当前状态与路线图

- [x] 项目搭建 + Mathlib4 本地克隆 + lake build 通过
- [x] `RiemannHypothesisStatement`：RH 的形式化陈述
- [x] Chebyshev ϑ(x) 和 π(x) 的初等形式化
- [ ] Euler 乘积的证明
- [ ] PNT 的陈述（Mathlib4 已有 PNT 的证明，可引用）
- [ ] $\zeta(s)$ 的函数方程
- [ ] $\zeta(s)$ 在 $\Re(s)=1$ 上无零点 → PNT 的证明
- [ ] Selberg 迹公式的形式化（长期目标）
