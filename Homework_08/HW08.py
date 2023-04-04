# Refer to HW08.pdf

import math
import requests

# Function Name: averagePopulation() 
# Parameters: regionalBloc ( str ) 
# Returns: average population ( float )

def averagePopulation(bloc):
    r = requests.get("https://restcountries.com/v2/all")
    countries = r.json()
    blocPop = 0
    n = 0
    for country in countries:
        if 'regionalBlocs' in country:
            if country['regionalBlocs'][0]['acronym'] == bloc:
                blocPop += country['population']
                n += 1
    return round(float(blocPop/n),2)

# Function Name: commonCountries() 
# Parameters: langTup1 ( tuple ), langTup2 ( tuple ) 
# Returns: list of countries ( list )

def commonCountries(lang1,lang2): 
    validCountries = []
    r = requests.get(f'https://restcountries.com/v2/lang/{lang1[0]}')
    lang1Countries = r.json()
    for country in lang1Countries:
        for language in country['languages']:
            if lang2[0] in language.values():
                validCountries.append(country['name'])
    return validCountries

# Function Name: uniqueRegions() 
# Parameters: countryList ( list ) 
# Returns: True or False ( bool ) or Error Message ( str )

def uniqueRegions(countryList):
    regions = []
    for country in countryList:
        r = requests.get(f"https://restcountries.com/v2/alpha/{country}")
        countryInfo = r.json()
        try:
            regions.append(countryInfo['region'])
        except KeyError: # error where key does not exist. 
            return "Invalid country code!"
    if len(set(regions)) == 1:
        return False
    else:
        return True
    
# Function Name: organizeCapitals() 
# Parameters: capitalList ( list ) 
# Returns: Dictionary mapping regions to a list of countries ( dict )

def organizeCapitals(capitalList):
    regionMap = {}
    for capital in capitalList:
        r = requests.get(f"https://restcountries.com/v2/capital/{capital}")
        countryInfo = r.json()
        try:
            if countryInfo[0]['region'] not in regionMap:
                regionMap[countryInfo[0]['region']] = [countryInfo[0]['name']['common'],]
            elif countryInfo[0]['region'] in regionMap:
                regionMap[countryInfo[0]['region']].append(countryInfo[0]['name']['common'])
        except KeyError:
            pass
    return regionMap

# Function Name: visitableCountries() 
# Parameters: countryCodeList ( list ) 
# Returns: list of country names ( list ) 

def visitableCountries(countryCodeList):
    string = ""
    for cc in countryCodeList:
        string += cc + ","
    r = requests.get(f"https://restcountries.com/v2/alpha?codes={string}")
    countryInfo = r.json()
    visitable = []
    for index,value in enumerate(countryInfo):
        if visitable == []:
            visitable.append(value['name'])
        elif value['alpha3Code'] in countryInfo[index-1]['borders']:
            visitable.append(value['name'])
        else:
            return visitable
    return visitable














        

    














