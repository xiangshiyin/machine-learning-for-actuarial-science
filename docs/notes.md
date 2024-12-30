## Supervised Learning for Sentiment Analysis
In supervised learning, you usually have an input $X$, which goes to your prediction function and get your output $\hat{Y}$. You can then compare your prediction with the true value $Y$, and this gives you the the cost which you use to update the parameter $\theta$ of your model.

### Numeric Representation of Text
There are a couple of ways to represent text information by numbers for sentiment analysis. Some of the basic methods include:
- One-hot encoding
  - This is the simplest way to represent text information. You can represent each word in your vocabulary by a vector of zeros and a single one. The length of the vector is the size of your vocabulary.
- Positive/Negative word frequency mapping
  - Use the frequency of a word in positive and negative corpus to represent the word.
- TBD

### Preprocessing Techniques
Depends on the actual modeling method, you may need to preprocess the text data following different strategies. Here are some classic preprocessing techniques:
- Tokenization - This typically involves stop word removal, stemming, and lemmatization. However, with the deep learning models especially the transformer models, you may not need to do this since the text info removed by these techniques may provide useful context information for the language model.
- TBD

### Modeling Techniques
There are many ways to model the sentiment analysis problem. Some of the classic methods include:
- Logistic Regression
  - Formula: $h_{\theta}(x) = \frac{1}{1 + e^{-\theta^Tx}}$
  - Lost function: $J(\theta) = -\frac{1}{m} \sum^{m}_{i=1}[y^{(i)}log h(x^{(i)}, \theta) + (1-y^{(i)})log(1-h(x^{(i)}))]$, some properties include
    - $h'(x) = h(x) (1 - h(x))$
    - $\partial_{\theta_j}J = \frac{1}{m} \sum^{m}_{i=1}(h(x^{(i)}, \theta) - y^{(i)})x^{(i)}_j$
    - $\theta_{n+1} = \theta_{n} - \alpha \partial_{\theta}J(\theta_{n})$
    - In vector representation, the gradient formular can be written as $\nabla_{\theta}J = \frac{1}{m}X^T(h(X, \theta) - Y)$
- 
