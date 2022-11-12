---
title: Parameter Analysis
has_children: false
parent: Getting started
grand_parent: Demos
nav_order: 1
---

# Overview
Here you can see the messidor parameter analysis. I chosed both logistic regression and Support Vector machine to find the best results for this particular dataset.


## Dataset Context
In a nutshell, DR is a eye complication that affects around 40% of people with diabetes, leading to blindness. If detected in time can be slowed down. 
This dataset is composed of features extracted from the output of several retinal image processing algorithms, such as:
- imagelevel (quality assessment, pre-screening, AM/FM)
- lesion-specific (microaneurysms, exudates) 
- anatomical (macula, optic disc) components. 
The actual decision about the presence of the disease is then made by comparing machine learning classifiers.

## Logistic Regression
For this, I am going to compare different parameters for the logistic regression in order to guarantee the best performance. Understanding how to tune these parameters can help get the best from my data. 

## Parameters in question
The parameters needed for Logistic Regression are:
- lr:        learning rate of gradient descent
- max_itr:   maximum number of iteration for gradient descent
- tol:       if the change in loss is smaller than tol, then we stop iteration


## Comparing parameters

### Learning rate 
Learning rate of gradient descent can be placed in different scales and see the difference. Here are the values explored in the experiments: [100, 10, 1, 0.1, 0.001, 0.001]

### Maximum number of iteration
maximum number of iteration for gradient descent. THis can be set very big if you are searching for a better performance and have the time and computational power. It can also be set low if you want an quick aproximation of what your results are going to be or if the algorithm is working properly. Here are the values explored in the experiments: [100, 10, 100, 1000, 10000, 100000, 1000000]

### Tolerance
If the change in loss is smaller than tolerance, then we stop iteration. This really doesn't affect the performance of the algorithm. Rather, it prevents you from spending too long running a model that might have troubles and won't converge. For this reason, there are no experimental parameters. 


## Support Vector Machine
For this, I am going to compare different parameters for the Support Vector Machine in order to guarantee the best performance. Understanding how to tune these parameters can help get the best from my data. 

## Parameters in question
The parameters needed for Support Vector Machine are:
- C: the hyperparameter for SVM algorithm
- sigma: the kernel bandwidth Sigma of Gaussian kernel 
- toler: the threshold value of prediction error. If the prediction error of a sample is larger than this value, the corresponding alpha_i will be probably updated.
- maxIter: the maximum number of iteration to search a pair of alpha's to update
- alphas: the alpha vector in the dual problem 
- b: the bias b


## Comparing parameters

### Parameter C
the hyperparameter for SVM algorithm (positive number). Here are the values explored in the experiments: [100, 10, 1, 0.1, 0.001, 0.001]

### Sigma
the kernel bandwidth $\sigma$ of Gaussian kernel 

### Tolerance
The threshold value of prediction error. If the prediction error of a sample is larger than this value, the corresponding alpha_i will be probably updated.. Rather, it prevents you from spending too long running a model that might have troubles and won't converge. For this reason, there are no experimental parameters. 

### Maximum number of iteration
Maximum number of iteration to search a pair of alpha's to update (positive integer). This can be set very big if you are searching for a better performance and have the time and computational power. It can also be set low if you want an quick aproximation of what your results are going to be or if the algorithm is working properly. Here are the values explored in the experiments: [100, 10, 100, 1000, 10000, 100000, 1000000]

### Alphas
The alpha vector in the dual problem (vector, num_samples). Here are the values explored in the experiments: [100, 10, 100, 1000, 10000, 100000, 1000000]

### Bias
The bias b(number).

# Results


# Conclusions
