---
title: 5. Takeaways
has_children: false
parent: Getting started
grand_parent: Demos
nav_order: 5
---

This project was a challenging journey through classical Spectral Methods and finite element methods (FEM) execution. In particular, the Galerkin method and the collocation method. These methods, even when coming from a similar structure, (With the stochastic collocation being a special form of the stochastic
Galerkin), had a lot of differences. For instance, the fundamental structure of the Galerkin was based on the projection of the weight residuals onto the space of approximating polynomials, while the collocation was purely based on interpolation. On the other hand, the Galerkin is an intrusive method, which makes it more computationally challenging than the non-intrusive Collocation. Additionally, working with Galerkin is restricted by two very big assumptions for the use of polynomial chaos expansion:

+ It can be used only for densities with associated orthogonal polynomials, not feasible for general densities.

+ It relies on the assumption that the random parameters are mutually independent.

On the contrary, the stochastic collocation method is applicable to general parameter distributions, which makes a significant advantage over the Galerkin method where the orthogonality of the inner products depends on the compatibility between the density function and the basis polynomials, which can't be always found.
The collocation, by choosing the quadrature points as collocation points, we can decouple the parametric and spatial components of the Galerkin projection, making it computationally more efficient.

It was interesting to learn about FEM, a very general and powerful technique for solving PDEs. The breaking up of the solution domain into a set of small, interconnected elements, is easy to follow, and the approximation of the solution within each element using a set of basis functions makes it very robust. The solution by solving a set of algebraic equations turns out to be a bit cumbersome when derived from a particular PDE and the boundary conditions. Of course, when implemented is captivating. It was computationally intensive and required deepening into the literature to adapt and implement the codes. 






