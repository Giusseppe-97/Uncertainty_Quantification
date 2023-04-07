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
The performance best of the Logistic regression was 0.77. This was achieved with the following parameters:
- lr=0.01
- max_itr=100000
- tol = 1e-5

The performance best of the Support Vecotr Machine was 0.63. This was achieved with the following parameters:
- C = 1
- sigma = 1
- toler = 0.01
- maxIter = 100



## Logistic Regression Analysis
Going a little bit deeper into the analysis, I wanted to describe why the best parameters make sense. The learning rate needs to be a value not too big that the value never converges because it is making very big steps, nor very small that it will be computationally exhausting to converge to the answer. 0.01 seems like a value in the middle. 

The maximum number of iteration for gradient descent makes sense to be big if you have the time and computational power for the algorithm to find the right answer. Too small makes no sense unless you just want to see if the algorithm is working properly and you don't want to wait too long for the model to run. I believe a higher iteration when you are approaching a model that you like makes sense, but too big is unecessary given that it still will eventually converge to an answer and is waiting resources. 

Tolerance prevents you from spending too long running a model that might have troubles and won't converge. An accuracy of 0.77 is a good result.  

## Support Vector Machine Analysis

Let's describe why the best found parameters make sense for SVM. The C parameter needs to be a value not too big that restriction is super high nor viceversa. To ilustrate this, just picture how changing the parameter C makes the tolerance of the parallel lines get wider or closer together, therefore a restrictive yet not extreme case is preferable.

The maximum number of iteration to search a pair of alpha's to update makes sense to be big if you have the time and computational power for the algorithm to find the right answer. Too small makes no sense unless you just want to see if the algorithm is working properly and you don't want to wait too long for the model to run. I believe a higher iteration when you are approaching a model that you like makes sense, but too big is unecessary given that it still will eventually converge to an answer and is waiting resources. 

Tolerance prevents you from spending too long running a model that might have troubles and won't converge. An accuracy of 0.63 is a good result, but could be improved and maybe I still could find better parameters.  

# Conclusions

Undoubtably, parameter analysis is an important practice to improve your results of your model. In all the experiments I was able to run for changing parameters, the variation of the accuracy was surprisingly high. For instance, for Logistic Regression I was able to achieve 0.77 accuracy, yet with not so different combination of paramenters it decreased even to the mid-60's. 
A great idea to rapidly find the best parameters is using tools that iterate with different values and print the best chosen values. Given that in this project we were not allowed to use such tools, I had to run my own version with the addition of some trial and error. In the end, the performance of both algorithms is satisfactory. 