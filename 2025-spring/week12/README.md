# Week 12: Model Serving Approaches
---

**Table of Content**
- [Week 12: Model Serving Approaches](#week-12-model-serving-approaches)
  - [Objectives](#objectives)
  - [Topic](#topic)
    - [Bias-Variance Tradeoff](#bias-variance-tradeoff)
    - [`XgBoost`](#xgboost)
  - [Course materials](#course-materials)
  - [Suggested reading](#suggested-reading)
    - [`XgBoost`](#xgboost-1)

---
## Objectives
In this week, we will cover the following topics:
* Ensemble Models
  * Gradient Boosting Models
    * `XgBoost`
    * `LightGBM`
  * Stacking
* Model Serving
  * Different approaches to serve ML models in production environments
  * A survey of the existing techniques
  * Demo
    * `Streamlit`
    * `FastAPI`

## Topic
### Bias-Variance Tradeoff
$$
\begin{array}{l}
E[ (Y - \hat{Y})^2 ] \\
= E[(f(X) + \epsilon - \hat{f}(X))^2] \\
= E[(f(X) - \hat{f}(X))^2 + 2\epsilon (f(X) - \hat{f}(X)) + \epsilon^2] \\
= E[(f(X) - \hat{f}(X))^2] + 2E[\epsilon (f(X) - \hat{f}(X))] + E[\epsilon^2] \\
= E[(f(X) - \hat{f}(X))^2] + \epsilon^2 \\
= E[(f(X) - \bar{f}(X) + \bar{f}(X) - \hat{f}(X))^2] + \epsilon^2 \\
= E[(f(X) - \bar{f}(X))^2] + E[(\bar{f}(X) - \hat{f}(X))^2] + 2E[(f(X) - \bar{f}(X))(\bar{f}(X) - \hat{f}(X))] + \epsilon^2
\end{array}
$$

Since $f(X) - \bar{f}(X)$ is constant and $E(\bar{f}(X) - \hat{f}(X))$ equals 0, the prediction error can be rewritten as
$$
\begin{array}{l}
E[ (Y - \hat{Y})^2 ] \\
= E[(f(X) - \bar{f}(X))^2] + E[(\bar{f}(X) - \hat{f}(X))^2] + \epsilon^2
\end{array} \\
= {bias}^2 + {variance} + \epsilon^2
$$

So essentially, any prediction error can be decomposed to `bias`, `variance` and some `irreducible error`.
- `Bias` measures the systematic difference between the model's hidden pattern and the assumed pattern in the model.
- `Variance` measures the variability of the model's predictions for a given data point.
- `Irreducible error` is the error that cannot be reduced by any model for the given set of features.

![](https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/images/bias_variance/bullseye.png)

### `XgBoost`
`XgBoost` has [built-in regularization](https://xgboost.readthedocs.io/en/stable/tutorials/model.html#objective-function-training-loss-regularization) to control the bias-variance tradeoff.
$$
obj(\theta) = L(\theta) + \Omega(\theta)
$$
where
- $L(\theta)$ is the training loss function, primarily contributing to the model bias
- $\Omega(\theta)$ is the regularization term, primarily contributing to the model variance
- The training loss measure how predictive the model is with respect to the training data
  - For regression problems, a common choice is the squared loss 
    - $L(\theta) = \sum_i (y_i - \hat{y}_i)^2$
  - For classification problems, a common choice is the log loss 
    - $L(\theta) = \sum_i [y_i log(1 + e^{\hat{y_i}}) + (1 - y_i) log(1 + e^{\hat{y_i}})]$

![](https://raw.githubusercontent.com/dmlc/web-data/master/xgboost/model/step_fit.png)

## Course materials
* slides [[link](https://docs.google.com/presentation/d/13vqPczJpCipRyvEPclbzyjND77ilX1Fa$$EnsBRjSMQ_E)]

## Suggested reading
### `XgBoost`
* Introduction to Boosted Trees [[link](https://xgboost.readthedocs.io/en/stable/tutorials/model.html)]
* Notes on parameter tuning [[link](https://xgboost.readthedocs.io/en/stable/tutorials/param_tuning.html)]
* Parameters [[link](https://xgboost.readthedocs.io/en/stable/parameter.html)]