'''
Returns state education levels
'''
import csv
import pandas as pd
from state_convertor import *


# Finds the percentage of education of pop in each state
def stateEdu():
    states = {}
    stateRow = csv.DictReader(open("../CSV/state_demographics.csv", "r", encoding="utf8", errors="ignore"))
    
    for row in stateRow:
        state  = row.pop("State")
        hs = float(row.pop("Education.High School or Higher"))
        ba = float(row.pop("Education.Bachelor's Degree or Higher"))
        if(state not in states):
            states[state] = ["High School or higher " + str(hs), "BA or Higher " + str(ba)]
    
    return states

# if numbers are higher or equal to the US average they get a 1 if not 0
def normalize():
    stateDict = stateEdu()
    us = stateDict["United States"]
    data = stateDict
    for state in stateDict:
        entry = data[state]
        if(state == "United States"):
            continue
        if(entry[0] >= us[0]):
            entry[0] = 1
        else:
            entry[0] = 0
        if(entry[1] >= us[1]):
            entry[1] = 1
        else:
            entry[1] = 0
        data[state] = entry
    
    return data


def state_edu():
    states = {}
    stateRow = csv.DictReader(open("../CSV/state_demographics.csv", "r", encoding="utf8", errors="ignore"))

    for row in stateRow:
        state  = row.pop("State")
        hs = float(row.pop("Education.High School or Higher"))
        ba = float(row.pop("Education.Bachelor's Degree or Higher"))
        if(state not in states):
            states[state] = [hs, ba]

    return states


# print(normalize())

# avg_income = state_edu()
# print(avg_income)
#
# df = pd.read_csv('../CSV/state_cases_political_score.csv')
# state_list = df['state'].tolist()
# state_income = []
#
# test_array = []
# for i in range(50):
#     test_array.append(i + 1)
#
# for i in range(len(state_list)):
#     # print(avg_income[0][abbrev_us_state[state_list[i]]])
#     state_income.append(avg_income[abbrev_us_state[state_list[i]]][1])
#
#
# def Convert(list1, list2):
#     res_dct = {list1[j]: list2[j] for j in range(len(list1))}
#     return res_dct
#
#
# csv_dict = Convert(test_array, state_income)
#
#
# df = pd.DataFrame.from_dict(csv_dict, orient="index")
# df.to_csv("avg.csv")
