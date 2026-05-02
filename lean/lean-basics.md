# Lean 4 基础符号指南 —— 从"我是谁"到"我能干什么"

> 本文档为零基础初学 Lean 4 而写。每个概念从代码示例出发，再往下一层层解释。目标读者：认识数学符号（如 $\mathbb{N}, \mathbb{R}, \forall, \sum$）但不知道它们在 Lean 中如何"说话"的人。

---

## 1. 先理解一个核心概念： "一切东西都有类型"

在 Lean 中，**每一个**合法表达式都有一个"类型"（type）。它不是 Python——在 Python 中你写 `x = 3`，类型自动推断。在 Lean 中，学会看懂类型是看懂一切的第一步。

Lean 中有两条命令是你的"问路石"：

```lean
#check 3         -- 询问 "3 的类型是什么？"
#eval 1 + 2      -- 计算表达式的值
```

`#check` 告诉你"这个东西属于哪个集合"；`#eval` 让计算机跑出结果。

打开 VS Code，在 `Basic.lean` 末尾逐行输入下面的例子，观察 Infoview 右侧面板的输出。

---

## 2. 数字类型家族

| 符号 | Lean 代码 | 含义 | 例子 | 能 `#eval` 吗？ |
|------|----------|------|------|:---:|
| $\mathbb{N}$ | `Nat` 或 `ℕ` | 自然数 0, 1, 2, ... | `3 : ℕ` | ✅ |
| $\mathbb{Z}$ | `Int` 或 `ℤ` | 整数 ...-2, -1, 0, 1, 2... | `-3 : ℤ` | ✅ |
| $\mathbb{Q}$ | `Rat` 或 `ℚ` | 有理数 | `(1/3 : ℚ)` | ✅ |
| $\mathbb{R}$ | `Real` 或 `ℝ` | 实数 | `π : ℝ` | ❌ |
| $\mathbb{C}$ | `Complex` 或 `ℂ` | 复数 | `(1 + 2*I : ℂ)` | ❌ |
| 命题 | `Prop` | 可证明/反驳的陈述 | `1+1=2 : Prop` | ❌ |

关键洞察：**Lean 只能 `#eval` 那些"由有限步构造出来"的类型**——`ℕ`, `ℤ`, `ℚ`。`ℝ` 和 `ℂ` 涉及无穷精度，Lean 无法在有限时间内还原它们的完整表示，所以标记为 `noncomputable`（不可计算）。

---

## 3. `ℕ` 的严格定义：皮亚诺公理

`Nat` 不是"内置的魔法数字"。它在 Lean 中的源代码只有三句话：

```lean
inductive Nat : Type where
  | zero : Nat
  | succ (n : Nat) : Nat
```

这读作：

> - `zero` 是一个自然数（就是 0）
> - 如果 `n` 是一个自然数，那么 `succ n`（读作"后继"）也是一个自然数
> - **所有自然数都是通过反复应用这两条规则构造出来的**

所以 `3` 在 Lean 内部其实是 `succ (succ (succ zero))`。

你不需要手写 `succ`——Lean 自动识别阿拉伯数字。但知道这个定义意味着：**`Nat` 是一棵树，每一个数都是有限层的构造**。这就是为什么 `ℕ` 可以 `#eval`——计算机只需要"沿着树走到叶节点"即可。

那 `ℕ` 上的加法和乘法哪来的？它们是用 `succ` 递归定义的：

```lean
def add (m n : Nat) : Nat :=
  match n with
  | zero => m
  | succ n' => succ (add m n')
```

翻译：`m + 0 = m`，否则 `m + (n'+1) = (m + n') + 1`。

你不需要自己写这些——Mathlib4 已经为你定义了整个小学算术大厦。

---

## 4. `ℝ` 为什么不能跑 `#eval`？

`ℝ` 不是"有限构造"——它由柯西序列构造或 Dedekind 分割构造，每一步都涉及"对于任意 $\varepsilon > 0$..."这样的极限描述。它不是一颗有限层的树。

因此 Lean 要求我们标记任何使用 `ℝ` 的定义为 `noncomputable`：

```lean
noncomputable def primeCounting (x : ℝ) : ℕ :=
  -- 这个符号可以在定理陈述中使用，但不能用 #eval 跑出数字结果
  ...

-- ❌ #eval primeCounting 10     -- 报错
-- ✅ #eval primeCountingNat 10  -- 4
```

**最佳实践**：给你的每一个概念同时写"理论版本"（类型复杂但方便陈述定理）和"实验版本"（类型简单但可以 `#eval` 验证直觉）。两者的名字通常靠后缀区分，如 `primeCounting` vs `primeCountingNat`。

---

## 5. 函数与箭头

在 Lean 中，函数的类型用 $\to$ 表示：

```lean
def square (x : ℕ) : ℕ := x * x
#check square    -- square : ℕ → ℕ     "接受一个 ℕ，返回一个 ℕ"
```

多参数函数靠"套娃"：

```lean
def add3 (a b c : ℕ) : ℕ := a + b + c
#check add3      -- add3 : ℕ → ℕ → ℕ → ℕ
```

读法：$\mathbb{N} \to (\mathbb{N} \to (\mathbb{N} \to \mathbb{N}))$ ——每一个箭头经过一个参数，最终返回一个值。

---

## 6. 命题的类型是 `Prop`

在 Lean 中，所有"可以被证明或反驳的句子"都是 `Prop` 类型的"居民"：

```lean
#check (1 + 1 = 2)        -- Prop
#check (Nat.Prime 7)      -- Prop
#check (∀ n : ℕ, n ≥ 0)   -- Prop
```

`Prop` 不能 `#eval`，因为它不是一个具体的数字——它是"一个真值（true 或 false）的数学断言"。

```lean
def RiemannHypothesisStatement : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → Complex.re s > 0 → Complex.re s < 1 → Complex.re s = 1/2
```

这个定义的意思是：**我声明了一个待证明的命题**——它不是 `true` 也不是 `false`，它是一个"等待严格证明来填的空格"。RH 的悬赏奖金就在这个空格后面。

---

## 7. `∀` 与 `→`：全称量词与蕴含

| 符号 | 读作 | 数学意思 | Lean 代码 |
|------|------|---------|-----------|
| $\forall$ | "对所有" | 全体 | `∀ s : ℂ, ...` |
| $\to$ | "则" / "蕴含" | 如果...那么... | `A → B` |

```lean
-- "对所有自然数 n，存在一个素数大于 n" —— 欧几里得的无穷素数定理
∀ n : ℕ, ∃ p : ℕ, p > n ∧ Nat.Prime p
```

在 Lean 中，`∀` 和 `→` 本质上是同一种东西——都是函数类型。`A → B` 是一个接受 `A` 类型参数并返回 `B` 类型结果的函数。`∀ x, ...` 只是这个函数的参数多了一个名字。

---

## 8. `Prop` vs `Bool`：关键区分

初学者的常见误区是把 `Prop` 当成 `Bool`。它们在 Lean 中是严格不同的：

| 概念 | 类型 | 含义 | 能 `#eval`？ |
|------|------|------|:---:|
| 逻辑命题 | `Prop` | "可以被证明的句子" | ❌ |
| 布林值 | `Bool` | `true` 或 `false` | ✅ |

```lean
#check (Nat.Prime 5)       -- Prop   "5 是一个素数的命题"
#check (Nat.Prime 5).decide -- 可以通过 decide 策略转化为 Bool
```

`Prop` 在你的证明中工作；`Bool` 只在你需要写条件表达式时偶尔出现。**在日常形式化中，你 95% 的时间面对的是 `Prop`**。

---

## 9. 常见 Lean 命令速览

| 命令 | 用途 | 例子 |
|------|------|------|
| `#check` | 查看表达式的类型 | `#check 3` |
| `#eval` | 计算一个可计算表达式 | `#eval 1 + 1` |
| `def` | 定义一个函数或常量 | `def square (x:ℕ) := x*x` |
| `noncomputable def` | 同上，但标记为不可计算 | `noncomputable def primeCounting ...` |
| `theorem` | 声明一个可证明的陈述 | `theorem hello : 1+1=2 := by rfl` |
| `example` | 声明一个匿名的可证明陈述 | `example : Nat.Prime 7 := by native_decide` |
| `inductive` | 定义一个新的数据类型 | `inductive Nat where ...` |
| `sorry` | 占位——"我暂时不会证明，允许编译通过" | `sorry` |

---

## 10. 练习清单

按顺序完成这些步骤，你就能正式开始用 Lean 学习数学：

1. **打开** `lean/lean-rh` 目录（不是 Riemann-Hypothesis 根目录）在 VS Code 中
2. **确认 Lean 4 扩展已激活**（左下角看到版本号）
3. **在 `Basic.lean` 末尾**逐行输入以下代码并观察 Infoview：

```lean
-- 练习 1：检查类型
#check 3               -- ℕ
#check (3 : ℝ)         -- ℝ
#check (Nat.Prime 5)   -- Prop

-- 练习 2：计算
#eval 2 + 3            -- 5
#eval List.range 5     -- [0,1,2,3,4]

-- 练习 3：加一个你自己的可计算函数
def double (n : ℕ) : ℕ := n + n
#eval double 5         -- 10

-- 练习 4：声明一个平凡的定理并证明
example : double 3 = 6 := by
  rfl                 -- "两边展开定义即可"
```

`rfl`（reflexivity 的缩写）是最简单的证明步骤——它告诉 Lean "等号两边化简后一模一样，你帮我验证一下"。当证明通过时，Infoview 会显示 `No goals`。

---

## 11. 之后该做什么

- 翻开本书 **第十四章 Dirichlet 级数**，找到 $\sum_{n=1}^\infty \frac{1}{n^s}$ 的定义，尝试在 Lean 中写它的"有限截断"版本（即只取前 $N$ 项的级数部分和）
- 这不需要复分析——你只需要 `ℕ` 上的可计算函数
- 当你做到这一步时，你就已经学会了：
  - 在 Lean 中陈述一个数学定义
  - 区分 `ℕ`（可计算）和 `ℝ`（不可计算）
  - 用 `#eval` 验证你的定义在实际值 $N=5,10,\ldots$ 上的表现
