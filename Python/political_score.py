'''make a composite score using data weighing current governors' parties, 2012 and 2016 Presidential Election, 2016 and 2018 House, Current Senate, 
 etc.'''

import csv

# dictionary for party of each state governor
def compileGovernor():
    governorParty = {}
    governorRow = csv.DictReader(open("../CSV/us-governors.csv", "r"))
    for row in governorRow:
        governorParty[row.pop("state_name")] = row.pop("party")

    return governorParty
    

# dictionaries for party each state voted for in 2012
def compilePresident2012():
    presidentialParty2012 = {}
    presidentRow = csv.DictReader(open("../CSV/1976-2016-president.csv", "r"))
    for row in presidentRow:
        state = row.pop("state")
        year = row.pop("year")
        if(year == "2012" and state not in presidentialParty2012):
            presidentialParty2012[state] = row.pop("party")

    return presidentialParty2012
        

# dictionaries for party each state voted for in 2016
def compilePresident2016():
    presidentialParty2016 = {}
    presidentRow = csv.DictReader(open("../CSV/1976-2016-president.csv", "r"))
    for row in presidentRow:
            state = row.pop("state")
            year = row.pop("year")
            if(year == "2016" and state not in presidentialParty2016):
                presidentialParty2016[state] = row.pop("party")

    return presidentialParty2016
       

# dictionary for house of rep parties 2016
def compileHouseRep2016():
    houseReps2016 = {}
    
    prev_district = 1
    district = 1
    most_votes = 0
    most_party = ""
    winners = []
    curr_state = ""
    
    houseRepRows = csv.DictReader(open("../CSV/1976-2018-house2.csv", "r", encoding="utf8", errors="ignore"))

    for row in houseRepRows:
        state = row.pop("state")
        year = row.pop("year")
        currentDist = (int)(row.pop("district"))
        if currentDist == 0:
            currentDist = 1
        
        currentParty = row.pop("party")
        vote_count = (int)(row.pop('candidatevotes'))
   
        if year == "2016":
            if state not in houseReps2016:
                if most_party != "":
                    winners.append(most_party)
                if winners != []:
                    houseReps2016[curr_state] = winners

                houseReps2016[state] = []
                prev_district = currentDist
                most_votes = vote_count
                most_party = currentParty
                curr_state = state
                winners = []

            if vote_count > most_votes and prev_district == currentDist:
                most_party = currentParty
                most_votes = vote_count

            if prev_district != currentDist and curr_state == state:
                winners.append(most_party)
                most_votes = vote_count
                most_party = currentParty

        prev_district = currentDist

    houseReps2016['Wyoming'] =  ['republican'] 

    return houseReps2016


# dictionary for house of rep parties 2018
def compileHouseRep2018():      
    houseReps2018 = {}
    
    prev_district = 1
    district = 1
    most_votes = 0
    most_party = ""
    winners = []
    curr_state = ""
    
    houseRepRows = csv.DictReader(open("../CSV/1976-2018-house2.csv", "r", encoding="utf8", errors="ignore"))
  
    for row in houseRepRows:
        state = row.pop("state")
        year = row.pop("year")
        currentDist = (int)(row.pop("district"))
        if currentDist == 0:
            currentDist = 1
        
        currentParty = row.pop("party")
        vote_count = (int)(row.pop('candidatevotes'))
   
        if year == "2018":
            if state not in houseReps2018:
                if most_party != "":
                    winners.append(most_party)
                if winners != []:
                    houseReps2018[curr_state] = winners

                houseReps2018[state] = []
                prev_district = currentDist
                most_votes = vote_count
                most_party = currentParty
                curr_state = state
                winners = []

            if vote_count > most_votes and prev_district == currentDist:
                most_party = currentParty
                most_votes = vote_count

            if prev_district != currentDist and curr_state == state:
                winners.append(most_party)
                most_votes = vote_count
                most_party = currentParty

        prev_district = currentDist
        
    if most_party != "":
        winners.append(most_party)
    if winners != []:
        houseReps2018[curr_state] = winners
    
    return houseReps2018


# dictionaries for parties of current us senators by state
def compileSenators():
    stateSenators = {}
    
    senatorRow = csv.DictReader(open("../CSV/arnoudb_Senators-of-the-116th-Congress.csv", "r"))
    for row in senatorRow:
        state = row.pop("State")
        party = row.pop("PartyAffiliation")
        if(state not in stateSenators):
            stateSenators[state] = [party]
        else:
            stateSenators[state].append(party)
    
    return stateSenators


# compiles a score for every state where + is Republican and - is Democrat
def getScores():
    scores = dict.fromkeys(compileGovernor(), 0)
    govDict = compileGovernor()
    presDict2012 = compilePresident2012()
    presDict2016 = compilePresident2016()
    senatorDict = compileSenators()
    repDict2016 = compileHouseRep2016()
    repDict2018 = compileHouseRep2018()
    for state in scores:
        if(govDict[state] == "republican"):
            scores[state] += 1
        elif(govDict[state] == "democrat"):
            scores[state] -= 1
        if(presDict2012[state] == "republican"):
            scores[state] += 1
        elif(presDict2012[state] == "democrat"):
            scores[state] -= 1
        if(presDict2016[state] == "republican"):
            scores[state] += 1
        elif(presDict2016[state] == "democrat"):
            scores[state] -= 1
        for party in senatorDict[state]:
            if(party == "republican"):
                scores[state] += 1
            elif(party == "democrat"):
                scores[state] -= 1
        for party in repDict2016[state]:
            if(party == "republican"):
                scores[state] += 1
            elif(party == "democrat"):
                scores[state] -= 1
        for party in repDict2018[state]:
            if(party == "republican"):
                scores[state] += 1
            elif(party == "democrat"):
                scores[state] -= 1

    return scores

print(getScores())