# Refer to HW07.pdf

import math as m

# Function Name: findCuisine()
# Parameters: filename ( str ), cuisine ( str )
# Returns: list of restaurants ( list )

def findCuisine(filename, cuisine):
    restaurants = []
    with open(f"/Users/rishithauluka/Code/Python/CS_1301/Homework_07/{filename}", 'r') as f:
        lines = f.readlines()
    for index, element in enumerate(lines):
          if cuisine in element:
            restaurants.append(lines[index-1].strip())
    return restaurants

# Function Name: restaurantFilter()
# Parameters: filename ( str )
# Returns: dictionary that maps cuisine type ( str ) to a list of restaurants of the same cuisine type ( list )

def restaurantFilter(filename):
    restaurantDict = {}
    with open(f"/Users/rishithauluka/Code/Python/CS_1301/Homework_07/{filename}", 'r') as f:
        lines = f.read()
    for restaurant in lines.split('\n\n'):
        if restaurant.split("\n")[1] not in restaurantDict:
            restaurantDict[restaurant.split("\n")[1]] = [restaurant.split("\n")[0],]
        elif restaurant.split("\n")[1] in restaurantDict:
            restaurantDict[restaurant.split("\n")[1]].append(restaurant.split("\n")[0])
    return restaurantDict

# Function Name: createDirectory()
# Parameters: filename ( str ), output filename ( str )
# Returns: None ( NoneType )

def createDirectory(filename,outputfile):
    infoDict = {}
    with open(f"/Users/rishithauluka/Code/Python/CS_1301/Homework_07/{filename}", 'r') as rf:
        lines = rf.read()
    for restaurant in lines.split('\n\n'):
        if restaurant.split("\n")[2] not in infoDict:
            infoDict[restaurant.split("\n")[2]] = [restaurant.split('\n')[0] + " - " + restaurant.split('\n')[1],]
        elif restaurant.split("\n")[2] in infoDict:
            infoDict[restaurant.split("\n")[2]].append(restaurant.split('\n')[0] + " - " + restaurant.split('\n')[1])

    with open(f"/Users/rishithauluka/Code/Python/CS_1301/Homework_07/{outputfile}", 'w') as wf:
        wf.write("Restaurant Directory")
        for key in infoDict:
            wf.write("\n\n" + key)
            for index,value in enumerate(infoDict[key]):
                wf.write(f"\n{index + 1}. {value}")

# createDirectory('restaurants.txt', 'directory.txt') ==> was ran to create 'directory.txt'

# Function Name: infectedPercentage()
# Parameters: country list( list ), filename ( str )
# Returns: country and percentage ( tuple )

def infectedPercentage(countries,filename):
    countryDict = {}
    maxInfect = 0
    with open(f"/Users/rishithauluka/Code/Python/CS_1301/Homework_07/{filename}", 'r') as rf:
        next(rf)
        lines = rf.read().split('\n')
    if countries != []:
        for data in lines:
            data = data.split(',')
            countryDict[data[0]] = round((int(data[2])/int(data[1])*100),2)
        for country in countries:
            if countryDict[country] > maxInfect:
                maxInfect = countryDict[country]
        for key, value in countryDict.items():
            if value == maxInfect:
                return (key,value)
    return None
    
# Function Name: countryStatus()
# Parameters: country list ( list ), filename( str )
# Returns: risk dictionary ( dict )

def countryStatus(countrylist, filename):
    countryDict = {}
    riskDict = {'Low risk': [],'Medium risk': [],'High risk': []}

    with open(f"/Users/rishithauluka/Code/Python/CS_1301/Homework_07/{filename}", 'r') as rf:
        next(rf)
        lines = rf.read().split('\n')

    for data in lines:
            data = data.split(',')
            countryDict[data[0]] = round((int(data[2])/int(data[1])*100),2)

    for country in countrylist:
        if countryDict[country] > 65:
            riskDict["High risk"].append(country)
        elif countryDict[country] > 25:
            riskDict["Medium risk"].append(country)
        elif countryDict[country] <= 25:
            riskDict["Low risk"].append(country)
    return riskDict

# Function Name: compareRisk()
# Parameters: country to compare ( str ), country list ( list ), filename( str )
# Returns: compared countries ( list )


def compareRisk(compareCountry,countryList,filename): 
    countryDict = {}
    acceptedCountries = []
    with open(f"/Users/rishithauluka/Code/Python/CS_1301/Homework_07/{filename}", 'r') as rf:
        next(rf)
        lines = rf.read().split('\n')
    
    for data in lines:
        data = data.split(',')
        countryDict[data[0]] = data[1:]
    
    for country in countryList:
        if (int(countryDict[country][0]) < int(countryDict[compareCountry][0])) and (int(countryDict[country][1]) > int(countryDict[compareCountry][1])):
            acceptedCountries.append(country)
    if acceptedCountries == []:
        return "No countries"
    else:
        return acceptedCountries
    





            


    


            


    



        
    



    








