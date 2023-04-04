# Refer to HW06.pdf

import math as m

# Function Name: findTicket() 
# Parameters: ticketDictionary ( dict ) 
# Returns: cheapestTicket ( tuple ) 

def findTicket(ticketDictionary):
    if ticketDictionary != {}:
        minVal = min(ticketDictionary.values())
        for key,value in ticketDictionary.items():
            if value == minVal:
                return tuple((key,value))
    else:
        return "No tickets available!"
    
# Function Name: findHotel() 
# Parameters: hotelDictionary ( dict ) 
# Returns: preferredHotel ( dict )

def findHotel(hotelDictionary):
    votes = {}
    if hotelDictionary != {}:
        for value in hotelDictionary.values():
            if value not in votes:
                votes[value] = 1  # used "=="; took me ages to figure out what was wrong
            else:
                votes[value] = votes[value] + 1
    maxVotes = max(votes.values())
    for key,value in votes.items():
        if value == maxVotes:
            return {key:value}
    return "No hotels available!"

# Function Name: findEvent() 
# Parameters: myInterests ( list ), schedule ( dict ) 
# Returns: match ( list ) 

def findEvent(myInterests,schedule):
    dates = []
    for key,value in schedule.items():
        for activity in value:
            if activity in myInterests and key not in dates:
                dates.append(key)
    return sorted(dates)

# Function Name: figureSkating() 
# Parameters: technicalScores ( list ), componentScores ( list ) 
# Returns: finalScores ( list ) 

def figureSkating(technicalScores, componentScores):
    finalScores = []
    for index, element in enumerate(technicalScores): # enumerate is a better way of doing range(len(technicalScores))
        try:
            finalScores.append(element + componentScores[index])
        except Exception:
            pass
    return finalScores

# Function Name: sportManagement() 
# Parameters: countryDict ( dict ) 
# Returns: sportDict ( dict ). 

def sportManagement(countryDict):
    sportsDict = {}
    for key,value in sorted(countryDict.items()): # sorts alphabetically by key so we don't have to later
        for sport in value:
            if sport not in sportsDict.keys():
                sportsDict[sport] = list((key,))
            elif sport in sportsDict.keys():
                sportsDict[sport].append(key)
    return sportsDict










            

    

        
