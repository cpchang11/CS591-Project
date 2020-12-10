'''
Finds the average using county median household income 
for each state and county and returns a dictionary also finds the min and max of each state
'''
import csv
import pandas as pd
from state_convertor import *

def averageMedian():
    states = {}
    counties = {} # key will look like {Saratoga County, New York}
    total = 0
    count = 0
    prevState = "Alabama"
    stateRow = csv.DictReader(open("../CSV/kaggle_income.csv", "r", encoding="utf8", errors="ignore"))
    for row in stateRow: 
        state  = row.pop("State_Name")
        county = row.pop("County")
        med = int(row.pop("Median"))
        if med == 0 or med == 300000:
            continue
        key = county + ", " + state
        if prevState != state:
            states[prevState] = round(total/count, 2)
            total = 0
            count = 0
            prevState = state
        if key not in counties:
            counties[key] = [med, 1]
        else:
            entry = counties[key]  
            entry[0] += med
            entry[1] += 1
            counties[key] = entry
        total += med
        count += 1
        prevState = state
    
    states[prevState] = round(total/count, 2)

    for county in counties:
        entry = counties[county]
        save = entry[0]/entry[1]
        counties[county] = round(save, 2)

    return states, counties


def minmaxMedian():
    states = {}
    minimum = 1000000000
    maximum = 0
    prevState = "Alabama"
    stateRow = csv.DictReader(open("../CSV/kaggle_income.csv", "r", encoding="utf8", errors="ignore"))
    for row in stateRow: 
        state = row.pop("State_Name")
        med = int(row.pop("Median"))
        if med == 0 or med == 300000:
            continue
        if prevState != state:
            states[prevState] = ["Min: " + str(minimum), "Max: " + str(maximum)]
            minimum = med
            maximum = 0
            prevState = state
        else:
            if minimum > med:
                minimum = med
            if maximum < med:
                maximum = med
        
        prevState = state

    return states

def average_median_states():
    states = {}
    counties = {} # key will look like {Saratoga County, New York}
    total = 0
    count = 0
    prevState = "Alabama"
    stateRow = csv.DictReader(open("../CSV/kaggle_income.csv", "r", encoding="utf8", errors="ignore"))
    for row in stateRow:
        state  = row.pop("State_Name")
        county = row.pop("County")
        med = int(row.pop("Median"))
        if med == 0 or med == 300000:
            continue
        key = county + ", " + state
        if prevState != state:
            states[prevState] = round(total/count, 2)
            total = 0
            count = 0
            prevState = state
        if key not in counties:
            counties[key] = [med, 1]
        else:
            entry = counties[key]
            entry[0] += med
            entry[1] += 1
            counties[key] = entry
        total += med
        count += 1
        prevState = state

    states[prevState] = round(total/count, 2)

    for county in counties:
        entry = counties[county]
        save = entry[0]/entry[1]
        counties[county] = round(save, 2)

    return states


def average_median_county():
    states = {}
    counties = {} # key will look like {Saratoga County, New York}
    total = 0
    count = 0
    prevState = "Alabama"
    stateRow = csv.DictReader(open("../CSV/kaggle_income.csv", "r", encoding="utf8", errors="ignore"))
    for row in stateRow:
        state  = row.pop("State_Name")
        county = row.pop("County")
        med = int(row.pop("Median"))
        if med == 0 or med == 300000:
            continue
        key = county + ", " + state
        if prevState != state:
            states[prevState] = round(total/count, 2)
            total = 0
            count = 0
            prevState = state
        if key not in counties:
            counties[key] = [med, 1]
        else:
            entry = counties[key]
            entry[0] += med
            entry[1] += 1
            counties[key] = entry
        total += med
        count += 1
        prevState = state

    states[prevState] = round(total/count, 2)

    for county in counties:
        entry = counties[county]
        save = entry[0]/entry[1]
        counties[county] = round(save, 2)

    return counties


# avg_income = minmaxMedian()
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
#     state_income.append(avg_income[abbrev_us_state[state_list[i]]][1][5:])
#
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