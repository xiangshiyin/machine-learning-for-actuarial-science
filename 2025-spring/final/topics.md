# Suggested Topics

- [Suggested Topics](#suggested-topics)
  - [Project 01: Medical Insurance Premium Prediction](#project-01-medical-insurance-premium-prediction)
    - [Idea](#idea)
    - [Dataset](#dataset)
  - [Project 02: Loan Default Prediction](#project-02-loan-default-prediction)
    - [Idea](#idea-1)
    - [Dataset](#dataset-1)
      - [Key Variables](#key-variables)
  - [Project 03: Lending Club Dataset](#project-03-lending-club-dataset)
    - [Idea](#idea-2)
    - [Dataset](#dataset-2)
    - [Caveat](#caveat)
  - [Project 04: Fraud Detection with Synthetic Financial Data](#project-04-fraud-detection-with-synthetic-financial-data)
    - [Idea](#idea-3)
    - [Dataset](#dataset-3)
      - [Caveat](#caveat-1)
  - [Project 05: Time Series Forecasting - A Survey of Classical Stats Models vs. Modern ML Approaches](#project-05-time-series-forecasting---a-survey-of-classical-stats-models-vs-modern-ml-approaches)
    - [Idea](#idea-4)
    - [Dataset](#dataset-4)
  - [Project 06: AutoML - A Survey of available AutoML techniques](#project-06-automl---a-survey-of-available-automl-techniques)
    - [Idea](#idea-5)


## Project 01: Medical Insurance Premium Prediction
### Idea
- Analyze the medical insurance premium dataset provided
- Build ML models to predict the medical insurance premium based upon the given dataset
- Utilize the appropriate methods to evaluate the model and identify key determinant features that influence the premium prices
- Compare the performance and interpretability of different models, identify the common and divergent patterns captured by each model
### Dataset
[[Link](https://www.kaggle.com/datasets/tejashvi14/medical-insurance-premium-prediction/data)]


## Project 02: Loan Default Prediction
### Idea
- Analyze the loan default dataset provided
- Build ML models to predict the loan default based upon the given dataset
- Utilize the appropriate methods to evaluate the model and identify key determinant features that influence the loan default
- Compare the performance and interpretability of different models, identify the common and divergent patterns captured by each model

### Dataset
[[link](https://www.deepcreditrisk.com/uploads/1/9/5/1/19511601/dcr_full.csv)]

The data set is in panel form and reports origination and performance observations for 50,000 residential U.S. mortgage borrowers over 60 periods. The periods have been de-identified. As in the real world, loans may originate before the start of the observation period (this is an issue where loans are transferred between banks and investors as in securitization). The loan observations may thus be censored as the loans mature or borrowers refinance. The data set is a randomized selection of mortgage-loan-level data collected from the portfolios underlying U.S. residential mortgage-backed securities (RMBS) securitization portfolios and provided by International Financial Research (www.internationalfinancialresearch.org).

#### Key Variables  
<details>
  <summary>Click to expand</summary>

- **id**: borrower ID  
- **time**: timestamp of observation  
- **orig_time**: timestamp for origination  
- **first_time**: timestamp for first observation  
- **mat_time**: timestamp for maturity  
- **res_time**: timestamp for resolution  
- **balance_time**: outstanding balance at observation time  
- **LTV_time**: loan-to-value ratio at observation time, in %  
- **interest_rate_time**: interest rate at observation time, in %  
- **rate_time**: risk-free rate  
- **hpi_time**: house price index at observation time (base year = 100)  
- **gdp_time**: GDP growth at observation time, in %  
- **uer_time**: unemployment rate at observation time, in %  
- **REtype_CO_orig_time**: real estate type condominium (1 if yes, 0 otherwise)  
- **REtype_PU_orig_time**: real estate type planned urban developments (1 if yes, 0 otherwise)  
- **REtype_SF_orig_time**: single-family home (1 if yes, 0 otherwise)  
- **investor_orig_time**: investor borrower (1 if yes, 0 otherwise)  
- **balance_orig_time**: outstanding balance at origination time  
- **FICO_orig_time**: FICO score at origination time, in %  
- **LTV_orig_time**: loan-to-value ratio at origination time, in %  
- **Interest_Rate_orig_time**: interest rate at origination time, in %  
- **state_orig_time**: US state in which the property is located  
- **hpi_orig_time**: house price index at observation time (base year = 100)  
- **default_time**: default observation at observation time  
- **payoff_time**: payoff observation at observation time  
- **status_time**: default (1), payoff (2), and non-default/non-payoff (0) observation at observation time  
- **lgd_time**: loss given default (LGD) assuming no discounting of cash flows  
- **recovery_res**: sum of all cash flows received during the resolution period  

</details>

## Project 03: Lending Club Dataset
### Idea
- Analyze the dataset provided
- Build credit risk models based upon the lending club dataset

### Dataset
[[link](https://www.kaggle.com/datasets/wordsforthewise/lending-club)]

### Caveat
- Figuring out the meaning of all features is a challenge. You may need some research in the lending club website and check some existing discussions on Kaggle [[example](https://www.kaggle.com/datasets/wordsforthewise/lending-club/discussion/170691)].
- Accepted and rejected loans are in separate csv files!

## Project 04: Fraud Detection with Synthetic Financial Data
### Idea
- Analyze the dataset provided
- Build ML models to predict fraudulent transactions
- Utilize the appropriate methods to evaluate the model and identify key determinant features that influence the fraud prediction
- Identify potential issues with the synthetic dataset

### Dataset
[[link](https://www.kaggle.com/datasets/ealaxi/paysim1)]
#### Caveat
- The dataset is synthetic data created via a simulator Paysim

## Project 05: Time Series Forecasting - A Survey of Classical Stats Models vs. Modern ML Approaches
### Idea
We only discussed a small subset of time series forecasting techniques in our class. It'll be beneficial for you to do some first hand explorations and research into this domain and see if you can find something new.
- Fetch and analyze selected stocks or stock indecies over time
- Compare the performance of classical stats models and modern ML approaches
- Discuss advantages and disadvantages of each approach

### Dataset
[[Yahoo Finance API](https://github.com/ranaroussi/yfinance)]

## Project 06: AutoML - A Survey of available AutoML techniques
### Idea
We only discussed the AutoML technique from high level and demonstrated one AutoML tool `FLAML` in our class. It'll be beneficial to do some further research into other available AutoML techniques
- Research and explore different AutoML techniques/tools with some first hand experiments
- Discuss advantages and disadvantages of each approach, identify their capabilities and limitations
- Open question: can we fully rely on AutoML techniques?
