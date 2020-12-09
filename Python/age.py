# Finds the average age of a state and returns a dictionary

import csv

def averageAge():
    states = {}
    stateRow = csv.DictReader(open("../CSV/2019age.csv", "r", encoding="utf8", errors="ignore"))
    total = 0
    for row in stateRow:
        state  = row.pop("NAME")
        sex = row.pop("SEX")
        age = int(row.pop("AGE"))
        pop = int(row.pop("POPEST2019_CIV"))
        if(state != "United States" and sex == "0" and age != 999):
            total += age*pop    
        if(state != "United States" and sex == "0" and age == 999):
            states[state] = round(total/pop, 2)
            total = 0
    
    return states

averageAge()
