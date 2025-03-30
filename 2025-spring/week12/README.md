# Week 12: Model Serving Approaches
---

**Table of Content**
- [Week 12: Model Serving Approaches](#week-12-model-serving-approaches)
  - [Objectives](#objectives)
  - [Topic](#topic)
    - [Bias-Variance Tradeoff](#bias-variance-tradeoff)
    - [`XgBoost`](#xgboost)
      - [Regularization](#regularization)
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
= E[(f(X) - \bar{f}(X))^2] + E[(\bar{f}(X) - \hat{f}(X))^2] + \epsilon^2 \\
= {bias}^2 + {variance} + \epsilon^2
\end{array}
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

#### Regularization
The objective function can be simplied as
$$
\begin{aligned}
obj(\theta) &= -\frac{1}{2} \sum_{j=1}^T \frac{G_j^2}{H_j + \lambda} +  \gamma T \\
\end{aligned}
$$

where
- $T$ is the number of trees in the model
- $\lambda$ is the L2 regularization factor
- $\gamma$ is the factor penalizing adding new splits to the model
- $G$ represent the summation of the gradients of the data points in the node
- $H$ represent the summation of the hessians of the data points in the node

For regression problems, assuming the loss function is the squared loss, $G$ and $H$ can be simplified as
$$
\begin{aligned}
G &= \sum_{i \in I} \frac{\partial L(y_i, \hat{y}_i)}{\partial \hat{y}_i} \\
&= \sum_{i \in I} (y_i - \hat{y}_i) \\

H &= \sum_{i \in I} \frac{\partial^2 L(y_i, \hat{y}_i)}{\partial \hat{y}_i^2} \\
&= \sum_{i \in I} 1 \\
\end{aligned}
$$

In this case, $G$ is simply the total residuals of the data points in the node, and $H$ is simply the number of data points in the node.

The node splitting can be evaluated via the following objective function
$$
\begin{aligned}
{Grain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma
\end{aligned}
$$


## Course materials
* slides [[link](https://docs.google.com/presentation/d/13vqPczJpCipRyvEPclbzyjND77ilX1Fa$$EnsBRjSMQ_E)]

## Suggested reading
### `XgBoost`
* Introduction to Boosted Trees [[link](https://xgboost.readthedocs.io/en/stable/tutorials/model.html)]
* Notes on parameter tuning [[link](https://xgboost.readthedocs.io/en/stable/tutorials/param_tuning.html)]
* Parameters [[link](https://xgboost.readthedocs.io/en/stable/parameter.html)]