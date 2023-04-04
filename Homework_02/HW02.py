# Refer to HW02.pdf

import math

# Function Name: skillLevel()
# Parameters: passRate ( int )
# Returns: "Beginner" or "Moderate" or "Advanced" ( str )

def skillLevel(passrate):
    if passrate <= 25:
        return "Beginner"
    elif passrate <= 75:
        return "Moderate"
    else:
        return "Advanced"
    
# Function Name: bookStore()
# Parameters: item ( str ), walletAmount ( float ), quantity ( int )
# Returns: moneyLeftOver ( float )

def bookStore(item,walletAmount,quantity):
    if item == "Shirt":
        walletAmount = walletAmount - (15.50 * quantity)
    elif item == "Lanyard":
        walletAmount = walletAmount - (15.50 * quantity)
    elif item == "Sweatshirt":
        walletAmount = walletAmount - (15.50 * quantity)
    elif item == "Mug":
        walletAmount = walletAmount - (15.50 * quantity)

    if walletAmount < 0:
        return("Not enough money!")
    else:
        return(round(walletAmount,2))
    
# Function Name: dinnerPlans()
# Parameters: distance ( int ), hungerLevel ( str )
# Returns: transportMode ( str )

def dinnerPlans(distance, hungerLevel):
    if (hungerLevel == 'Very Hungry'):
        if (distance > 1):
            return 'Uber'
        else:
            return 'Walk'
    elif (hungerLevel == 'Hungry'):
        if (distance > 3):
            return 'Uber'
        else:
            return 'Walk'
    elif (hungerLevel == 'Slightly Hungry'):
        if (distance > 5):
            return 'Uber'
        else:
            return 'Walk'
    else:
        if (distance > 7):
            return 'Uber'
        else:
            return 'Walk'

# Function Name: weekendTrip()
# Parameters: distance ( float ), speed ( float ), freeTime ( float )
# Returns: transportMode ( str )

def weekendTrip(dist,sp, freeTime):
    time = dist/sp
    if (time <= (0.2*freeTime*60)):
        if sp <= 15:
            return "Walking"
        elif sp <= 20:
            return "Biking"
        else:
            return "Driving"
    else:
        return 'Going to this destination would take too much time.'

# Function Name: textFriends()
# Parameters: distance ( float ), speed ( float ), freeTime ( float ), numSnacks ( int ),
# numFriends ( int )
# Returns: textMsg ( str )

def textFriends(d,v,freeTime,numSnacks,numFriends):
    time = d/v
    maxsnack = math.floor(numSnacks/numFriends)
    if (time > (0.2*freeTime*60)):
        return weekendTrip(d,v,freeTime)
    else:
        return f"If each of us gets {maxsnack} snack(s), there will be {numSnacks-(maxsnack*numFriends)} left. I will be {(weekendTrip(d,v,freeTime)).lower()}, who else is doing the same?"

