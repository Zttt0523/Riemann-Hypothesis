import Lake
open Lake DSL

package «lean-rh» where
  -- Riemann Hypothesis formalization project
  -- Build: lake build
  -- Depends on: mathlib4 (add when network allows)

@[default_target]
lean_lib RiemannHypothesis where
  -- Modules:
  --   Basic.lean       — arithmetic functions, Dirichlet series, prime counting
  --   ZetaFunction.lean — ζ(s) definition, Euler product, analytic continuation
  --   RHStatement.lean  — formal statement of the Riemann Hypothesis
