# Refer to HW09.pdf

import math

# Function Name: pickyEater() 
# Parameters: food list ( list ) 
# Returns: number of food items that can be eaten ( int )

def pickyEater(flist): 
    count = 0 
    if flist == []: # base condition
        return flist 
    if (len(flist[0]) % 2) == 0 and flist[0] != "":
        count += 1
    return count + pickyEater(flist[1:]) # smallest piece we can remove

# Function Name: inviteFriends() 
# Parameters: list of invitees ( list ) 
# Returns: flattened list of all invitees ( list )

def inviteFriends(invList):
    if invList == []: # base condition
        return invList
    if type(invList[0]) == list:
        return inviteFriends(invList[0]) + inviteFriends(invList[1:])
    if type(invList[0]) == str:
        return [invList[0],] + inviteFriends(invList[1:]) # smallest piece we can remove

# Function Name: friendsgiving() 
# Parameters: stores ( list ), budget ( float ), maxDistance ( int ) 
# Returns: price of sauce at each store ( dict )

def friendsgiving(stores,budget,maxD):
    if stores == []:
        return {}
    if float(stores[0][1]) < float(budget) and int(stores[0][2]) < int(maxD):
        return {**{stores[0][0]: float(stores[0][1])},**friendsgiving(stores[1:],budget,maxD)} # ** merges dictionaries
    else:
        return friendsgiving(stores[1:],budget,maxD)
    
# Function Name: palindrome() 
# Parameters: string ( str ), guess ( int ) 
# Returns: Whether the string contains a number of palindromes ( bool ) 

def palindrome(string,guess):
    if len(string) < 3:
        if guess == 0:
            return True
        else:
            return False
    if string[0] == string[2] and string[0] != string[1]:
        return palindrome(string[1:],(guess-1)) 
    return palindrome(string[1:],guess)







