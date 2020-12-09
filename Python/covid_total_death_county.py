# TOTAL COVID DEATH NUMBERS AS OF DECEMBER 6, 2020 FOR EACH COUNTY

import plotly.figure_factory as ff
import numpy as np
import pandas as pd

df_sample = pd.read_csv('../CSV/covid_county_population_usafacts.csv')
df_sample = df_sample[df_sample['countyFIPS'] > 0]
df_sample = df_sample[df_sample['population'] > 0]

colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef",
              "#b3d2e9", "#9ecae1", "#85bcdb", "#6baed6", "#57a0ce",
              "#4292c6", "#3082be", "#2171b5", "#1361a9", "#08519c",
              "#0b4083","#08306b"]

endpts = [10, 20, 30, 40, 50, 75, 100, 200, 300, 500, 750, 1000, 1500, 2000, 3000, 5000]

fips = df_sample['countyFIPS'].tolist()
population = df_sample['population'].tolist()
death = df_sample['death'].tolist()

fig = ff.create_choropleth(
    fips=fips, values=death, scope=['usa'],
    binning_endpoints=endpts, colorscale=colorscale,
    show_state_data=True,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    state_outline={'color': 'rgb(0,0,0)', 'width': 0.5},
    show_hover=True,
    asp = 2.9,
    title_text = 'Confirmed Death from COVID-19 (Dec 6, 2020)',
    legend_title = 'Number of Deaths'
)

fig.layout.template = None
fig.show()