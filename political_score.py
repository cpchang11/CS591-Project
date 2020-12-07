'''make a composite score using data weighing current governors' parties, 2016 Presidential Election, 2018 House/Senate, 
 etc.'''

import csv

def compileData():
    # dictionary for party of each state 
    governorParty = {}
    governorRow = csv.DictReader(open("us-governors.csv", "r"))
    for row in governorRow:
        governorParty[row.pop("state_name")] = row.pop("party")

    # dictionaries for party each state voted for in 2012 and 2016
    presidentialParty2012 = {}
    presidentialParty2016 = {}
    presidentRow = csv.DictReader(open("1976-2016-president.csv", "r"))
    for row in presidentRow:
        state = row.pop("state")
        year = row.pop("year")
        if(year == "2012" and state not in presidentialParty2012):
            presidentialParty2012[state] = row.pop("party")
        elif(year == "2016" and state not in presidentialParty2016):
            presidentialParty2016[state] = row.pop("party")

    # dictionary for house of rep parties
    houseReps2016 = {}
    houseReps2018 = {}
    
    district = 1
    houseRepRows = csv.DictReader(open("1976-2018-house2.csv", "r", encoding="utf8", errors="ignore"))
    for row in houseRepRows:
        state = row.pop("state")
        year = row.pop("year")
        if(year == "2016"):
            if(state not in houseReps2016):
                houseReps2016[state] = [row.pop("party")]
                if(row.pop("district") == 0):
                    district = 1
                else:
                    district = 2
            elif(district == row.pop("district")):
                houseReps2016[state].insert(row.pop("party"))
                district += 1
    print(houseReps2016)
    
compileData()