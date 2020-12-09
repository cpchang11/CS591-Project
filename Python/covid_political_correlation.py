import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go
from political_score import *
from state_convertor import *

YEAR = 2016

df_covid = pd.read_csv('../CSV/covid_county_population_usafacts.csv')
# df_covid = df_covid[df_covid['countyFIPS'] > 0]

df_political = pd.read_csv('../CSV/countypres_2000-2016.csv')
df_political = df_political[df_political['year'] == YEAR]
df_political = df_political[df_political['FIPS'] > 0]

county_fips_list = df_covid['countyFIPS'].tolist()

# print(len(county_fips_list))

county_political = {}
county_score = {}

nonce = 0
for county_fips in county_fips_list:
    if county_fips == 0:
        nonce -= 1
        county_score[county_fips + nonce] = -1
        county_political[county_fips + nonce] = 'NA'
    else:
        county = df_political[df_political['FIPS'] == county_fips]
        county_dem_row = county[county['party'] == 'democrat']
        county_dem_votes = sum(county_dem_row['candidatevotes'].tolist())
        county_rep_row = county[county['party'] == 'republican']
        county_rep_votes = sum(county_rep_row['candidatevotes'].tolist())
        # Republican ( +1 ), Democratic ( -1 )
        county_score[county_fips] = county_rep_votes - county_dem_votes
        if county_dem_votes > county_rep_votes:
            county_political[county_fips] = 'Democrat'
        else:
            county_political[county_fips] = 'Republican'


# Convert Dictionary to CSV
# df = pd.DataFrame.from_dict(county_political, orient="index")
# df.to_csv("political.csv")

nonce = 0
state_score = {}

political_score = getScores()
political_score = dict((us_state_abbrev[key], value) for (key, value) in political_score.items())

# county_fips_list = [1133, 0, 2013, 4003]
# print(len(county_fips_list))

for fips in county_fips_list:
    if fips == 0:
        nonce -= 1
        state_score[nonce] = -999999
    else:
        row = df_covid[df_covid['countyFIPS'] == fips]
        state = row['State'].tolist()
        state = state[0]
        if state == 'DC':
            state_score[fips] = -999999
        else:
            state_score[fips] = political_score[state]

# print(state_score)

df = pd.DataFrame.from_dict(state_score, orient="index")
df.to_csv("state_score.csv")

# print(county_fips_list)
# print(county_political)
# print(county_score)
# print('--')
# print(len(county_fips_list))
# print(len(county_political))
# print(len(county_score))
