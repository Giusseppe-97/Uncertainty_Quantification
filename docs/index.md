---
title: Statistical learning final project
permalink: /
nav_order: 1
---

# Statistical learning final project

In this project, I am going to analyze some real-world datasets using supervised machine learning algorithms. Regression and classification are the main subjects studied.

  + This project is written in Jupyter Notebook in order to be as interactive and visual as possible. The codes for both the regression and the classification algorithms are the solutions of the tutorials submitted each week in my Statistical Learning course. 

Ideally, the repository should work on any computer that runs Jupyter Notebook. Even if the main codes are witten for pc, mac code is added in the repository and can be easily addapted. 

<img src="img/The_mice_counter_xlsx_result.png" width="100%">

## Motivation

For the submission of this project, I was encouraged to not only adapt the codes to some given datasets, but to understand the undergoing functionality of each algorithm. Particularly, I wanted to get a better notion of when to use each algorithm and how well I they can perform under different characteristics, without overfitting them.   

## Organization

* For regression datasets, `Mean Squared Error` (MSE) is usually used to evaluate the performances of regressors. The regression algorithms include:
  + Linear Regression
  + Support Vectore Regression
  + Decision Tree Regression
  + Random Forest Regression
  + Gradient Boosting Regression
  + Multi-Layer Perceptron Regression
  
* For classification, `Accurcary` is usually used to evaluate the performances of classifiers. The classification algorithms include:
  + Logistic Regression 
  + Support Vector Machine
  + Linear Discriminant Analysis
  + Decision Tree Classification (Trimming is Optional)
  + Random Forest Classification
  + Adaboost Classification 
  + Multi-Layer Perceptron Classification

##  Tasks acomplished:
1. Results Summary:
  + For each dataset, 3 algorithms or more were runned and their results were summarized.
2. Results Comparison:
  + For each dataset, I described why I think my algorithms performs differently.
    + some algorithms may suffer from the curse of dimensionality;
    + some algorithms take a lot of time to run on XXX dataset;
    + too many categorical variables may affect the performace of a certain algorithm;
3. Parameter Analysis:
  + For the Messidor dataset and the SVM algorithm, I explore the relationship between the parameter and corresponding performances. I runned the model with different parameters on this dataset and recorded multiple test errors. 
Then I found out the best performance and its corresponding parameters.

## Getting started

Check the [installation](pages/installation/installation.html) to learn how to clone the repository.

Check the [demos](pages/demos/demos.html) to see how to:
+ Introduction to the datasets.
+ Introduction to the algorithms.
+ Distribution of the algorithms used for each dataset.
+ Start running the algorithms and discovering their results by yourself.