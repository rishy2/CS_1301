# Refer to HW05.pdf

import math
from calendar import weekday

# Function Name: showToWatch() 
# Parameters: friendsFavShows ( list ), favoriteShow ( str ) 
# Returns: list of friends ( list )

def showToWatch(friendsFavShows, favoriteShow):
    compatible = []
    for friend in friendsFavShows:
        if favoriteShow in friend[1]:
            compatible.append(friend[0])
    if compatible == []:
        return "Lonely night :("
    else:
        return sorted(compatible)

# Function Name: fixLabels() 
# Parameters: labelList ( list ) 
# Returns: list of correct labels ( list ) 

def fixLabels(labelList):
    prices = []
    labels = []
    sortedList = []
    for val in labelList:
        if type(val) == float:
            prices.append(val)
        elif type(val) == str:
            labels.append(val)
    if len(prices) != len(labels):
        return 'Missing labels'
    else:
        for i in range(len(prices)):
            tempTuple = (labels[i],prices[i])
            sortedList.append(tempTuple)
    return sorted(sortedList)

# Function Name: newPlaylist() 
# Parameters: playlist ( list ) 
# Returns: list of songs ( list ) 

def newPlaylist(playlist):
    newplay = []
    songnames = []
    time = 0
    for song in playlist:
        songnames.append(song[0])
        time = time + int(song[1].split(":")[0]) * 60 + int(song[1].split(":")[1])
    newplay.append(tuple(sorted(songnames)))
    newplay.append(round((time/60),2))
    return newplay

# Function Name: birthdays() 
# Parameters: friends ( list ), birthdates ( list ) 
# Returns: list of names ( list )

def birthdays(friends,birthdates):
    weekendBirthdays = []
    for date in birthdates:
        if weekday(2022,date[0],date[1]) >= 5:
            weekendBirthdays.append(friends[birthdates.index(date)])
    return sorted(weekendBirthdays)

# Function Name: smashBros() 
# Parameters: fighterList ( list ), opponent ( str ) 
# Returns: list of good picks ( list ) 

# smashData.py is required ==> (I don't have it)
# Idea is to import function from another file using from and import keywords
#  ==> "from smashData import counterPick"





    

