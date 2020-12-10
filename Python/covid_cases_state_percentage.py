from political_score import *
from state_convertor import *
from collections import OrderedDict
import pandas as pd
import plotly.graph_objects as go
from education import *
from state_convertor import *
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

score_dict = getScores()

df_sample = pd.read_csv('../CSV/covid_county_population_usafacts.csv')
df_sample = df_sample[df_sample['countyFIPS'] > 0]
df_sample = df_sample[df_sample['population'] > 0]
df_sample = df_sample[df_sample['State'] != 'DC']

# Number of States
states = df_sample['State'].tolist()
states = list(OrderedDict.fromkeys(states))

# Change Dictionary Key Value
score_dict = dict((us_state_abbrev[key], value) for (key, value) in score_dict.items())

# Total Cases Per State
state_cases = {}
for state in score_dict.keys():
    curr_state = df_sample[df_sample['State'] == state]
    curr_state = curr_state['covid'].tolist()
    total_cases = sum(curr_state)
    state_cases[state] = total_cases

# State Population
state_population = {}
for state in score_dict.keys():
    curr_state = df_sample[df_sample['State'] == state]
    curr_state = curr_state['population'].tolist()
    total_population = sum(curr_state)
    state_population[state] = total_population

# Total Death
state_death = {}
for state in score_dict.keys():
    curr_state = df_sample[df_sample['State'] == state]
    curr_state = curr_state['death'].tolist()
    total_death = sum(curr_state)
    state_death[state] = total_death

# Convert Dictionary to CSV
# df = pd.DataFrame.from_dict(state_population, orient="index")
# df.to_csv("pop.csv")

# State Graphs
df = pd.read_csv('../CSV/state_cases_political_score.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

df['text'] = df['state']

fig = go.Figure(data=go.Choropleth(
    locations=df['state'],
    z=df['c/p'].astype(float),
    locationmode='USA-states',
    colorscale='Reds',
    autocolorscale=False,
    text=df['text'], # hover text
    marker_line_color='white', # line markers between states
    colorbar_title="COVID-19 Cases (Percentage)"
))

fig.update_layout(
    title_text='COVID-19 Cases as of Dec 6 Per Population, 2020 by State<br>(Hover for breakdown)',
    geo = dict(
        scope='usa',
        projection=go.layout.geo.Projection(type = 'albers usa'),
        showlakes=True, # lakes
        lakecolor='rgb(255, 255, 255)'),
)

fig.show()

""" COVID vs Education Correlation """

high_school = []
college = []
covid_list = df['c/p'].tolist()
edu_dict = state_edu()
state_list = df['state'].tolist()
for i in range(len(state_list)):
    high_school.append(edu_dict[abbrev_us_state[state_list[i]]][0])
    college.append(edu_dict[abbrev_us_state[state_list[i]]][1])

covid_list = [round(float(num), 3) for num in covid_list]

# High School
plt.plot(high_school, covid_list, 'r.')
plt.xlabel('Percentage of People With High School Degrees ')
plt.ylabel('COVID Cases Per Population (%)')
mymodel = np.poly1d(np.polyfit(high_school, covid_list, 1))
myline = np.linspace(75, 100, 100)
plt.plot(myline, mymodel(myline))
gradient, intercept, r_value, p_value, std_err = stats.linregress(high_school, covid_list)
print("y = ", gradient, "x + ", intercept)
plt.show()

# College
plt.plot(college, covid_list, 'r.')
plt.xlabel('Percentage of People With College Degrees ')
plt.ylabel('COVID Cases Per Population (%)')
mymodel = np.poly1d(np.polyfit(college, covid_list, 1))
myline = np.linspace(15, 45, 100)
plt.plot(myline, mymodel(myline))
gradient, intercept, r_value, p_value, std_err = stats.linregress(college, covid_list)
print("y = ", gradient, "x + ", intercept)
plt.show()




