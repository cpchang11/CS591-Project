from political_score import *
from state_convertor import *
from collections import OrderedDict
import pandas as pd
import plotly.graph_objects as go
from education import *
from state_convertor import *
import matplotlib.pyplot as plt
from scipy import stats
from age import *
import numpy as np

age_dict = averageAge()
df = pd.read_csv('../CSV/state_cases_political_score.csv')
covid_list = df['c/p'].tolist()
state_list = df['state'].tolist()
state_age = []
state_covid = []

test_array = []
for i in range(50):
    test_array.append(i + 1)

for i in range(len(state_list)):
    state_age.append(age_dict[abbrev_us_state[state_list[i]]])



# def Convert(list1, list2):
#     res_dct = {list1[j]: list2[j] for j in range(len(list1))}
#     return res_dct
#
# csv_dict = Convert(test_array, state_age)
#
# df = pd.DataFrame.from_dict(csv_dict, orient="index")
# df.to_csv("age.csv")


# for i in range(len(covid_list)):
#     high_school.append(edu_dict[abbrev_us_state[state_list[i]]][0])
#     college.append(edu_dict[abbrev_us_state[state_list[i]]][1])


# plt.plot(high_school, covid_list, 'r.')
# plt.xlabel('Percentage of People With High School Degrees ')
# plt.ylabel('COVID Cases Per Population (%)')
# mymodel = np.poly1d(np.polyfit(high_school, covid_list, 1))
# myline = np.linspace(75, 100, 100)
# plt.plot(myline, mymodel(myline))
# gradient, intercept, r_value, p_value, std_err = stats.linregress(high_school, covid_list)
# print("y = ", gradient, "x + ", intercept)
# plt.show()