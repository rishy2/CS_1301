# Refer to HW04.pdf

import math

# Function Name: findMax()
# Parameters: list of numbers ( list ), start index ( int ), stop index ( int )
# Returns: highest number ( int )

def findMax(list,start,stop):
    checklist = list[start:stop]
    max = list[start]
    for num in checklist:
        if num > max:
            max = num
    return max

# Function Name: fruitPie()
# Parameters: fruits ( list ), minimum quantity ( int )
# Returns: fruits for pie ( list )

def fruitPie(fruits,min):
    pielist = []
    for char in fruits:
        if (type(char) == int) and (char >= min):
            pielist.append(fruits[fruits.index(char)-1])
    return pielist

# Function Name: replaceWord()
# Parameters: initial sentence ( str ), replacement word ( str )
# Returns: corrected sentence ( str )

def replaceWord(sentence,replacement):
    correctSentence = ""
    for word in sentence.split(" "):
        if len(word) < 5:
            correctSentence = correctSentence + " " + word
        else: 
            correctSentence = correctSentence + " " + replacement
    return correctSentence.strip()

# Function Name: highestSum()
# Parameters: list of strings ( list )
# Returns: index of string with the highest sum ( int )

def highestSum(list):
    sums = []
    for str in list:
        charsum = 0
        for char in str:
            if char.isdigit():
                charsum = charsum + int(char)
        sums.append(charsum)
    return sums.index(max(sums))

# Function Name: sublist()
# Parameters: alist ( list ), blist ( list )
# Returns: True or False ( bool )

def sublist(alist,blist):
    if len(blist) == 0:
        return True
    for num in alist:
        if num == blist[0]:
            if blist == alist[alist.index(blist[0]):alist.index(blist[0])+len(blist)]:
                return True
            else:
                return False
    return False


    











