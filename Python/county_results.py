import plotly.figure_factory as ff
import pandas as pd

YEAR = 2016

df_sample = pd.read_csv('countypres_2000-2016.csv')
df_sample = df_sample[df_sample['year'] == YEAR]
df_sample = df_sample[df_sample['FIPS'] > 0]

democrats = df_sample[df_sample['party'] == 'democrat']
republicans = df_sample[df_sample['party'] == 'republican']

#0000FF (BLUE) DEMOCRATIC
#FF0000 (RED) REPUBLICAN
#00FF00 (GREEN) NA
colorscale = ["#0000ff", "#00ff00", "#ff0000"]

endpts = [1, 2]

# democrats vs republican
dem_votes = democrats['candidatevotes'].tolist()
rep_votes = republicans['candidatevotes'].tolist()

# make sure length of lists are the same to compare
assert(len(dem_votes) == len(rep_votes))

# fips value in list
fips = democrats['FIPS'].tolist()

# initialize empty lists
political_party = []

# append to empty list
for i in range(len(dem_votes)):
    if dem_votes[i] > rep_votes[i]:
        political_party.append('Democrat')
    elif dem_votes[i] < rep_votes[i]:
        political_party.append('Republican')
    else:
        political_party.append('NA')

fig = ff.create_choropleth(
    fips=fips, values=political_party, scope=['usa'],
    colorscale=colorscale,
    show_state_data=True,
    county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
    state_outline={'color': 'rgb(0,0,0)', 'width': 0.5},
    show_hover=True,
    asp = 2.9,
    title_text = '2016 Presidential Election by County',
    legend_title = 'Political Party'
)

fig.layout.template = None
fig.show()

