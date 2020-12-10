import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('../CSV/state_cases_political_score.csv')
X = df[['age', 'avg_income', 'highschool', 'college', 'political_score']]
y = df['covid_per_population']

## fit a OLS model with intercept on TV and Radio
X = sm.add_constant(X)

est = sm.OLS(y, X).fit()
print(est.summary())
