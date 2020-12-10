import plotly.graph_objects as go
from education import *
from state_convertor import *
import matplotlib.pyplot as plt
from scipy import stats
from age import *
import numpy as np

df = pd.read_csv('../CSV/state_cases_political_score.csv')
list1 = df['age'].tolist()
list2 = df['c/p'].tolist()

plt.plot(list1, list2, 'r.')
# List 1
plt.xlabel('Average Age of State')
# List 2
plt.ylabel('COVID Cases Per Population (%)')
mymodel = np.poly1d(np.polyfit(list1, list2, 1))
myline = np.linspace(round(min(list1) - 5), round(max(list1) + 5), 1000)
plt.plot(myline, mymodel(myline))
gradient, intercept, r_value, p_value, std_err = stats.linregress(list1, list2)
print("y = ", gradient, "x + ", intercept)
plt.show()