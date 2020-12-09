'''
Finds the average using county median household income 
for each state and county and returns a dictionary also finds the min and max of each state
'''
import csv

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
        if(med == 0 or med == 300000):
            continue
        key = county + ", " + state
        if(prevState != state):
            states[prevState] = round(total/count, 2)
            total = 0
            count = 0
            prevState = state
        if(key not in counties):
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
        state  = row.pop("State_Name")
        med = int(row.pop("Median"))
        if(med == 0 or med == 300000):
            continue
        if(prevState != state):
            states[prevState] = ["Min: " + str(minimum), "Max: " + str(maximum)]
            minimum = med
            maximum = 0
            prevState = state
        else:
            if(minimum > med):
                minimum = med
            if(maximum < med):
                maximum = med
        
        prevState = state
    

    return states

averageMedian()
minmaxMedian()