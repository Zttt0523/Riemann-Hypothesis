import Lake
open Lake DSL

package «lean-rh» where
  -- Riemann Hypothesis formalization project
  -- Mathlib4 cloned locally under lean/mathlib4/

-- Use local Mathlib4 clone instead of remote dependency
require mathlib from "../mathlib4"

@[default_target]
lean_lib RiemannHypothesis where
  -- Modules:
  --   Basic.lean       — arithmetic functions, Dirichlet series, prime counting
  --   ZetaFunction.lean — ζ(s) definition, Euler product, analytic continuation
  --   RHStatement.lean  — formal statement of the Riemann Hypothesis
