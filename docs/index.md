---
title: UQ final project
permalink: /
nav_order: 1
---

# UQ final project

In this project, I am first going to expain the theory behind the Galerkin and the collocation methods. Then, I am going to present three examples, solve them, and discuss my results. Finally, I am going to explain the codes so that the readers can recreate those results.

  + This project is written in Jupyter Notebook in order to be as interactive and visual as possible. The codes for both the book examples and the independent example intended to have a Matlab alternative. 

Ideally, the repository should work on any computer that runs Jupyter Notebook. Even if the main codes are witten for pc, when the repository is added to a mac it can be easily addapted. 

## Motivation

For the submission of this project, I was encouraged to not only find a solution to one Stochastic Galerkin problem and one Collocation Interpolation problem but to understand the undergoing theory behind them and also recreate a complex example of the Galerkin Method for Poisson's equation. Personally, I wanted to get a better notion of when to use each technique and how well they can develop different codes at least to find simple results. In the future, I would like to be able to employ this finite element method if I ever encounter such problems. Creating the Github page was an added value for the project. Even if this took me some weekend time, I wanted to have something tangible accessible to others and not another report in my University Dropbox folder.       

## Getting started

Check the [installation](pages/installation/installation.html) to learn how to clone the repository.

Check the [demos](pages/demos/demos.html) to see:
+ Theory.
  + Galerkin Method
  + Collocation Method
+ Analysis.
  + Problem 1. Solve a differential equation with uniformed distributed alpha and beta using the Stochastic Galerkin Method.
  + Problem 2. Solve problem 1 using the Collocation Method.
  + Problem 3. Solve Poisson's equation using the Galerkin  Method. 
+ Analysis.
  + Python code.
  + Matlab code.