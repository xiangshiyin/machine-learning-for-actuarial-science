# Week 12: Model Serving Approaches
---

**Table of Content**
- [Week 12: Model Serving Approaches](#week-12-model-serving-approaches)
  - [Objectives](#objectives)
  - [Topic](#topic)
    - [Bias-Variance Tradeoff](#bias-variance-tradeoff)
  - [Course materials](#course-materials)
  - [Suggested reading](#suggested-reading)

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



## Course materials
* slides [[link](https://docs.google.com/presentation/d/13vqPczJpCipRyvEPclbzyjND77ilX1Fa$$EnsBRjSMQ_E)]

## Suggested reading
* TBD
* Online resources
* TBD