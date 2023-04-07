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
    for index, value in enumerate(stringlist):
        if value == sorted(value):
            if value not in grouped:
                grouped[value] = [value,]
        if value != sorted(value):
            if sorted(value) not in grouped:
                grouped[sorted(value)] = [value,]
            if sorted(value) in grouped:
                grouped[sorted(value)].append(value)
        return grouped




        
