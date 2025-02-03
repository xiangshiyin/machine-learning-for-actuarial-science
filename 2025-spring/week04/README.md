# Week 04: Actuarial Science and Machine Learning
---

**Table of Content**
- [Week 04: Actuarial Science and Machine Learning](#week-04-actuarial-science-and-machine-learning)
  - [Objectives](#objectives)
  - [Topics](#topics)
  - [Course materials](#course-materials)
  - [Suggested reading](#suggested-reading)
    - [Logistic Regression and Generalized Linear Models](#logistic-regression-and-generalized-linear-models)
    - [Decision Trees](#decision-trees)
  - [References](#references)

---
## Objectives
Actuarial science has traditionally been data-driven, utilizing statistical methods to assess risk, price insurance products, and manage reserves. The emergence of machine learning (ML) has significantly broadened the tools available to actuaries, allowing them to address more complex challenges and harness new types of data. However, the inherent opacity of some ML algorithms can undermine consumer trust and raise concerns among regulators. In this lecture, we will explore the intersections and distinctions between ML and actuarial science.

## Topics
Here are the topics we are going to cover
* [ ] Machine Learning vs. Actuarial Science - the methodologies, principles, and opportunities
* [ ] Can we explain ML models?
  * [ ] Example - Tree based models
    * [ ] Generalized Linear Model (**GLM**) $\eta = g(\mu) = z^T \beta = \beta_0 + \sum_{i=1}^D \beta_i z_i$
    * [ ] Generalized Additive Model (**GAM**) $g(\mu) = \beta_0 + f_1(x_1) + f_2(x_2) + ... + f_D(x_D)$
    * [ ] Tree-base models (Decision Tree, Regression Tree, etc.)
  * [ ] General approaches - What's possible?


## Course materials
* slides [[link](https://docs.google.com/presentation/d/1HpfN628BOZYSKeQhYkdcT4Kn1okLSNzIYWhlrSx2gjE/edit?usp=sharing)]

## Suggested reading
Below are some recommended book chapters that provide insightful explanations on tree-based models (pick one that's accessible):

### Logistic Regression and Generalized Linear Models
* Chapter 4 of *Introduction to Statistical Learning in Python*

### Decision Trees
* Chapter 6 of *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow, 3rd Edition* 
* Chapter 8 of *Introduction to Statistical Learning in Python*
* Chapter 4 of *Fundamentals of Machine Learning for Predictive Data Analytics*

## References
* Machine Learning algorithms vs. Actuarial Science [[link](https://towardsdatascience.com/machine-learning-algorithm-vs-actuarial-science-who-will-win-b203f31145ce)]
* Machine Learning for Financial Risk Management: A Survey [[link](https://www.researchgate.net/publication/346731605_Machine_Learning_for_Financial_Risk_Management_A_Survey)]
* Exploring Risk Assessment with Machine Learning in Finance [[link](https://www.hyperstack.cloud/blog/case-study/exploring-risk-assessment-with-machine-learning-in-finance)]
* Boosting Insights in Insurance Tariff Plans with Tree-Based Machine Learning Methods [[link](https://www.tandfonline.com/doi/full/10.1080/10920277.2020.1745656)]
* A data driven binning strategy for the construction of insurance tariﬀ classes [[link](https://www.webofscience.com/wos/alldb/full-record/WOS:000444817300002)]
* Interpreting Black-Box Models: A Review on Explainable Artificial Intelligence [[link](https://link.springer.com/article/10.1007/s12559-023-10179-8#:~:text=A%20black%2Dbox%20model%20in,not%20easily%20accessible%20or%20interpretable.)]
* A gentle introduction to Splines [[link](https://joshua-nugent.github.io/splines/)]
* Other readings
  * Introduction to GLMs [[link](https://online.stat.psu.edu/stat504/lesson/6/6.1)]
  * Introduction to GAMs [[link](https://m-clark.github.io/generalized-additive-models/introduction.html)]