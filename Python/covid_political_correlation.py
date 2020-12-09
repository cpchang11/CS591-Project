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

""" Total Counties Cases Separated by Political Views """
df_view = df_covid[df_covid['countyFIPS'] > 0]
df_view = df_view[df_view['State'] != 'DC']

political_list = df_view['political'].tolist()
population_list = df_view['population'].tolist()
covid_list = df_view['covid'].tolist()
death_list = df_view['death'].tolist()
fips_list = df_view['countyFIPS'].tolist()
score_list = df_view['score'].tolist()
dem_percentage_list = df_view['dem_percentage'].tolist()
voters_list = df_view['voters'].tolist()

assert(len(political_list) == len(population_list) == len(covid_list) == len(death_list) == len(fips_list)
       == len(score_list) == len(dem_percentage_list) == len(voters_list))

democrat_population = 0
democrat_covid = 0
democrat_death = 0
republican_population = 0
republican_covid = 0
republican_death = 0

for i in range(len(fips_list)):
    if dem_percentage_list[i] != -1:
        voters_percent = voters_list[i] / population_list[i]

        democrat_population += dem_percentage_list[i] * voters_list[i]
        republican_population += (1 - dem_percentage_list[i]) * voters_list[i]

        democrat_covid += dem_percentage_list[i] * covid_list[i] * voters_percent
        republican_covid += (1 - dem_percentage_list[i]) * covid_list[i] * voters_percent

        democrat_death += dem_percentage_list[i] * death_list[i] * voters_percent
        republican_death += (1 - dem_percentage_list[i]) * death_list[i] * voters_percent

democrat_death = round(democrat_death)
democrat_population = round(democrat_population)
democrat_covid = round(democrat_covid)

republican_death = round(republican_death)
republican_population = round(republican_population)
republican_covid = round(republican_covid)

print(democrat_population, democrat_covid, democrat_death)
print(republican_population, republican_covid, republican_death)


""" Other Stuff """

""" Political View, County Score, County Percentage, Total Dem/Rep Voters """

# county_political = {}
# county_score = {}
# county_dem_percentage = {}
# county_voters = {}
#
# nonce = 0
# for county_fips in county_fips_list:
#     if county_fips == 0:
#         nonce -= 1
#         county_score[county_fips + nonce] = -1
#         county_political[county_fips + nonce] = 'NA'
#         county_dem_percentage[county_fips + nonce] = -1
#         county_voters[county_fips + nonce] = -1
#     else:
#         county = df_political[df_political['FIPS'] == county_fips]
#         county_dem_row = county[county['party'] == 'democrat']
#         county_dem_votes = sum(county_dem_row['candidatevotes'].tolist())
#         county_rep_row = county[county['party'] == 'republican']
#         county_rep_votes = sum(county_rep_row['candidatevotes'].tolist())
#         # Republican ( +1 ), Democratic ( -1 )
#         county_score[county_fips] = county_rep_votes - county_dem_votes
#         county_voters[county_fips] = county_rep_votes + county_dem_votes
#         if county_dem_votes + county_rep_votes != 0:
#             county_dem_percentage[county_fips] = county_dem_votes / (county_dem_votes + county_rep_votes)
#         else:
#             county_dem_percentage[county_fips] = -1
#         if county_dem_votes > county_rep_votes:
#             county_political[county_fips] = 'Democrat'
#         else:
#             county_political[county_fips] = 'Republican'

# Convert Dictionary to CSV
# df = pd.DataFrame.from_dict(county_score, orient="index")
# df.to_csv("score.csv")
# df = pd.DataFrame.from_dict(county_political, orient="index")
# df.to_csv("political.csv")
# df = pd.DataFrame.from_dict(county_dem_percentage, orient="index")
# df.to_csv("percentage.csv")
# df = pd.DataFrame.from_dict(county_voters, orient="index")
# df.to_csv("voters.csv")

""" Political Score """

# nonce = 0
# state_score = {}
#
# political_score = getScores()
# political_score = dict((us_state_abbrev[key], value) for (key, value) in political_score.items())
#
# for fips in county_fips_list:
#     if fips == 0:
#         nonce -= 1
#         state_score[nonce] = -999999
#     else:
#         row = df_covid[df_covid['countyFIPS'] == fips]
#         state = row['State'].tolist()
#         state = state[0]
#         if state == 'DC':
#             state_score[fips] = -999999
#         else:
#             state_score[fips] = political_score[state]

# print(state_score)
# df = pd.DataFrame.from_dict(state_score, orient="index")
# df.to_csv("state_score.csv")
