# Suggested Topics

## Medical Insurance Premium Prediction
### Idea
- Build ML models to predict the medical insurance premium based upon the given dataset
- Utilize the appropriate methods to evaluate the model and identify key determinant features that influence the premium prices
- Compare the performance and interpretability of different models, identify the common and divergent patterns captured by each model
### Dataset
[[Link](https://www.kaggle.com/datasets/tejashvi14/medical-insurance-premium-prediction/data)]


## Loan Default Prediction
### Idea
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

