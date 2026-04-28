---
difficulty = "★"
prerequisites = ["I-01", "I-02"]
paths = ["green", "blue", "red"]
keywords = ["Habilitation", "geometry", "Riemann zeta", "1859 paper", "professorship"]
zh-status = "missing"
zh-missing-note = "Chinese version is the primary text for this chapter"
en-status = "complete"
---

# Chapter 3: Riemann's Collected Works

> Difficulty: ★ | Paths: 🟢🟡🔴 | Prerequisites: Chapters 1, 2

## Habilitation and the Trial Lecture

After earning his doctorate, Riemann remained at Göttingen to pursue the Habilitation — the qualification required to lecture at a German university. In 1853 he completed his Habilitation thesis, *Über die Darstellbarkeit einer Function durch eine trigonometrische Reihe* (On the Representability of a Function by a Trigonometric Series). This work introduced the rigorous definition of the Riemann integral — the limit of Riemann sums, $\int_a^b f(x)\,dx = \lim_{\|P\|\to 0} \sum f(x_i^*)\Delta x_i$ — which remains the foundation of integration theory.

As was customary, Riemann submitted three possible topics for his trial lecture (*Probevorlesung*). Gauss, following tradition, chose the third: *Über die Hypothesen, welche der Geometrie zu Grunde liegen* (On the Hypotheses That Lie at the Foundations of Geometry).

On June 10, 1854, Riemann stood before the assembled Göttingen faculty and delivered what became one of the most famous lectures in the history of science.

## The Birth of Riemannian Geometry

Riemann's lecture asked a question of breathtaking audacity: what is the geometry of the space we live in?

He began by liberating geometry from three-dimensional intuition, defining manifolds (*Mannigfaltigkeiten*) of arbitrary dimension. On a manifold, the infinitesimal distance is given by a quadratic differential form:

$$
ds^2 = \sum_{i,j} g_{ij}(x)\,dx_i\,dx_j
$$

where $g_{ij}(x)$ is the metric tensor. From the metric and its derivatives, curvature is determined. Riemann proved a profound result: at infinitesimal scales, Euclidean geometry always holds; but at finite scales, space can be curved, and this curvature can be measured intrinsically — without reference to an embedding in higher dimensions.

The lecture was fifty years ahead of its time. Among the audience, only the aged Gauss truly grasped what he had heard — witnesses reported that Gauss left the lecture room "deep in thought, visibly agitated." When Einstein built general relativity half a century later, Riemannian geometry was waiting for him, the perfect mathematical language.

## The Professorship

In 1854, Riemann became a *Privatdozent* — an unsalaried lecturer paid only by student fees. His teaching style was unconventional: he lectured without notes, building the theory from geometric intuition on the spot. Because his lectures were demanding, his student numbers were always modest — but among them was Richard Dedekind, who would become the principal editor of Riemann's collected works and his deepest interpreter.

In 1857, Riemann was promoted to associate professor (*außerordentlicher Professor*) with a modest salary. Two years later, upon Dirichlet's death, he succeeded to the full professorship (*ordentlicher Professor*) at the age of thirty-three. For the first time in his life, he was free from financial anxiety.

## 1859: The Pinnacle — On the Number of Primes

In August 1859, Riemann submitted a short paper to the Berlin Academy of Sciences. He had just been elected a corresponding member, and the paper was the customary acknowledgment. The title was *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse* — "On the Number of Primes Less Than a Given Magnitude."

The paper was eight pages long.

It was the only number-theoretic paper Riemann ever published. And it transformed the history of mathematics.

Riemann began from Euler's product formula:

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_{p \text{ prime}} \frac{1}{1 - p^{-s}} \qquad (\operatorname{Re}(s) > 1)
$$

He analytically continued $\zeta(s)$ to the entire complex plane (except for a simple pole at $s=1$), proved its functional equation, derived an explicit formula linking the zeros of $\zeta(s)$ to the distribution of prime numbers, computed the first several non-trivial zeros, and — on the sixth page — made the conjecture that now bears his name:

> It is very probable that all [non-trivial] roots have real part $1/2$. Certainly one would wish for a rigorous proof of this; I have, however, temporarily set aside the search for such a proof after several fleeting unsuccessful attempts, as it appears unnecessary for the immediate objective of my investigation.

Parts V and VI of this encyclopedia explore the Riemann Hypothesis in depth. Here it suffices to note that the eight-page paper contained five epochal contributions: the method of analytic continuation, the functional equation, the explicit formula for primes, the Riemann Hypothesis itself, and the first-hand computation of non-trivial zeros.

## Other Major Works

Riemann's contributions extended far beyond number theory:

**Complex Analysis**: His doctoral thesis founded the geometric theory of complex functions. The concept of the Riemann surface — a multi-sheeted surface that renders multi-valued functions like $\sqrt{z}$ and $\log z$ single-valued — became one of the central ideas of modern mathematics.

**Abelian Functions**: His 1857 paper *Theorie der Abel'schen Functionen* was the high point of algebraic function theory. Riemann introduced the genus (*Geschlecht*) of a curve and established what became the Riemann-Roch theorem — one of the deepest results in algebraic geometry.

**Mathematical Physics**: Riemann studied the propagation of shock waves and developed the method of characteristics for hyperbolic partial differential equations. This work directly influenced modern computational fluid dynamics.

**Hypergeometric Functions**: He introduced the Riemann P-symbol to represent solutions of hypergeometric differential equations.

## Personal Life and Early Death

Riemann's health had always been fragile. Years of intense work and periods of poverty had worn him down. In 1862 he married Elise Koch; their daughter Ida was born the following year. The marriage brought rare happiness to his difficult life.

Later in 1862 he contracted pleurisy, and from that point onward was frequently ill. He traveled repeatedly to Italy for its milder climate. In Pisa, Florence, and by the shores of Lake Maggiore he continued to think about mathematics, forming deep friendships with Italian mathematicians, especially Beltrami and Betti. He even gave a lecture in Naples on the unification of gravitation and light — an early attempt at a field theory.

On July 20, 1866, Riemann died of tuberculosis at Selasca, on Lake Maggiore, aged thirty-nine. He is buried in the church cemetery there, where his gravestone can still be visited.

After his death, his housekeeper — to the enduring grief of mathematicians — burned a large quantity of his unpublished manuscripts while clearing his study.

Riemann published fewer than ten papers in his lifetime. Every one of them revolutionized its field. Dedekind and Heinrich Weber edited the first edition of his collected works in 1876. A second edition followed in 1892, with a supplementary volume in 1902.

---

> **Key points**: Riemann's Habilitation lecture founded Riemannian geometry — the mathematics of curved space, later essential for Einstein's general relativity. His 1859 eight-page paper on primes contained the Riemann Hypothesis. He published very few papers, but each one transformed its field. He died of tuberculosis at thirty-nine.

> **See also**: [Chapter 4: Riemann's Legacy](./chapter-04-legacy.md) ★
