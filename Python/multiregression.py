import plotly.graph_objects as go
from education import *
from state_convertor import *
import matplotlib.pyplot as plt
from scipy import stats
from age import *
import numpy as np
import statsmodels.api as sm
# c/p
df = pd.read_csv('../CSV/state_cases_political_score.csv')
y = df['c/p'].tolist()
print(y)
# age
x = []
x.append(df['age'].tolist())
x.append(df['political_score'].tolist())
x.append(df['d/c'].tolist())

a = df['avg'].tolist()
b = df['min'].tolist()
c = df['max'].tolist()
a = [j / 1000 for j in a]
b = [j / 1000 for j in b]
c = [j / 1000 for j in c]
x.append(a)
x.append(b)
x.append(c)

x.append(df['highschool'].tolist())
x.append(df['college'].tolist())
x.append(df['d or r'].tolist())


def reg_m(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results


print(reg_m(y, x).summary())

# y =  -0.638818718431507 x +  29.873288528436333