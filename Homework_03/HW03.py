# Refer to HW03.pdf

import math

# Function Name: movieNight()
# Parameters: a caption ( str )
# Returns: the fixed caption ( str )

def movieNight(caption):
    string = ""
    for letter in caption:
        if not letter.isdigit():
            string = string + letter
    return string

# Function Name: iceCream()
# Parameters: flavor ( str ), number of vowels ( int )
# Returns: a sentence ( str )

def iceCream(flavor,nv):
    vowelcount = 0
    for letter in flavor:
        if letter in "aeiouAEIOU":
            vowelcount = vowelcount+1
    if vowelcount > nv:
        return f"Yes, {flavor.lower()} ice cream has more than {nv} vowels!"
    else:
        return f"No, {flavor.lower()} ice cream doesn't have more than {nv} vowels!"

# Function Name: dreamCar()
# Parameters: car price ( float ), bank balance( float ), interest rate ( float )
# Returns: number of years ( int )

def dreamCar(price,bal,ir):
    return math.ceil(math.log(price/bal)/math.log(1+ir/100))

# Function Name: battleship()
# Parameters: board size ( int )
# Returns: None ( NoneType )

def battleship(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(size):
        for j in range(size):
            if ((j+1) == size):
                print(alphabet[i]+str(j+1))
            else:
                print(alphabet[i]+str(j+1), end=" ")

# Function: tennisMatch()
# Parameters: player 1 ( str ), player 2 ( str ), match record ( str )
# Returns: winner ( str )
        
def tennisMatch(p1,p2,record):
    p1games = 0
    p2games = 0 
    for game in record.split("-"):
        points1 = 0
        points2 = 0
        for char in game:
            if char == 1:
                points1 = points1 + 1
            elif char == 2:
                points2 = points2 + 1
        if points1 > points2:
            p1games = p1games + 1
        elif points2 > points1:
            p2games = p2games + 1
    if p1games > p2games:
        return f'{p1} won! The score was {p1games}-{p2games}.'
    elif p2games > points1:
        return f'{p2} won! The score was {p1games}-{p2games}.'
    elif p1games == p2games:
        return "It's a tie!"


    


        



            
        
        
            
