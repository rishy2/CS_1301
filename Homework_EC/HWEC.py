# Refer to HWEC.pdf

# Function Name: validParentheses() 
# Parameters: a string with parentheses ( str ) 
# Returns: valid or not ( bool ) 

def validParentheses(string):
    boxindices = []
    for index, char in enumerate(string):
            if char == "[" or char == "]":
                boxindices.append(index)
    if (string[boxindices[0]:boxindices[-1]].count("(") % 2 == 0) and (string[boxindices[0]:boxindices[-1]].count(")") % 2 == 0):
        return True
    else:
         return False

# Function Name: bubbleSort() 
# Parameters: a list ( list ), the list's length ( int ) 
# Returns: None ( NoneType ) 

# Hint: You should be using loops in combination with recursion for this function.

def bubbleSort(list,length):
    swapped = False
    if length < 2:
        return list
    for index, char in enumerate(list):
        if index == 0:
            continue
        if (char < list[index - 1]):
            list[index], list[index - 1] = list[index - 1], list[index]
            swapped = True
    if swapped is True:
        return list
    return bubbleSort(list, length)

# Function Name: groupAnagrams() 
# Parameters: list of strings ( list ) 
# Returns: grouped anagrams ( dict )

def groupAnagrams(stringlist):
    grouped = {}
    for word in stringlist:
        sorted_word = ''.join(sorted(word))
        if sorted_word in grouped:
            grouped[sorted_word].append(word)
        elif sorted_word not in grouped:
            grouped[sorted_word] = [word]
    return grouped

# Winter Break Planner
# Description: Winter Break is almost here, which means you want to start planning some vir-
# tual hang out sessions with your friends. To do this, you will be creating 2 classes: a Friend
# class and a Planner class. The implementation of these classes will be explained below.

class Friend:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def addActivity(self, inputTup):
        if not inputTup[0] in self.schedule:
            self.schedule[inputTup[0]] = inputTup[1]
        else:
            return "Not possible"

class Planner:
    def __init__(self, friendsList):
        self.friendsList = friendsList

    def freeTime(self):
        temp = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for x in self.friendsList:
            for y in x.schedule.keys():
                if y in temp:
                    temp.remove(y)
        if len(temp) == 0:
            return "No one is free"
        return temp

    def plans(self, inputDay):
        days = {}
        for x in self.friendsList:
            if inputDay in x.schedule and x.schedule[inputDay] in days:
                tempList = days[x.schedule[inputDay]]
                tempList.append(x.name)
                days[x.schedule[inputDay]] = tempList
            else:
                days[x.schedule[inputDay]] = [x.name]
        return days




        
