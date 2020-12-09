# COVID DEATH NUMBERS PER COVID CASES AS OF DECEMBER 6, 2020 FOR EACH COUNTY

import plotly.figure_factory as ff
import numpy as np
import pandas as pd

df_sample = pd.read_csv('../CSV/covid_county_population_usafacts.csv')
df_sample = df_sample[df_sample['countyFIPS'] > 0]
df_sample = df_sample[df_sample['population'] > 0]
df_sample = df_sample[df_sample['covid'] > 0]

colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef",
              "#b3d2e9", "#9ecae1", "#85bcdb", "#6baed6", "#57a0ce",
              "#4292c6", "#3082be", "#2171b5", "#1361a9", "#08519c",
              "#0b4083","#08306b"]

fips = df_sample['countyFIPS'].tolist()
covid = df_sample['covid'].tolist()
death = df_sample['death'].tolist()

# endpts = [0.01, 0.025, 0.05, 0.075, 0.1, 0.15, 0.2, 0.3, 0.5, 0.75, 1, 2, 4, 7, 10]
endpts = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 3, 3.5, 4, 5, 6, 8]

percentage = []

for i in range(len(death)):
    num = death[i] / covid[i]
    num = round(num * 100, 2)
    percentage.append(num)

fig = ff.create_choropleth(
    fips=fips, values=percentage, scope=['usa'],
    binning_endpoints=endpts, colorscale=colorscale,
    show_state_data=True,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    state_outline={'color': 'rgb(0,0,0)', 'width': 0.5},
    show_hover=True,
    asp = 2.9,
    title_text = 'Total Deaths Per COVID-19 Cases (Dec 6, 2020)',
    legend_title = 'Percentage'
)

fig.layout.template = None
fig.show()
