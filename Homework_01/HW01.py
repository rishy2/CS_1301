# Refer to HW01.pdf

import math

# Function Name: listen()
# Parameters: N/A
# Returns: None

def listen():
    songs = int(input("How many songs did you listen to? "))
    podcasts = int(input("How many podcasts did you listen to? "))
    sum = songs * 3 + podcasts * 25
    print(f"By listening to {songs} songs and {podcasts} podcasts, you have spent {math.floor(sum/60)} hours and {sum % 60} minutes on Spotify ")
    
# Function Name: dominosTime()
# Parameters: N/A
# Returns: None

def dominosTime():
    pizza = int(input("How many pizzas do you want? "))
    pasta = int(input("How many orders of pasta do you want? "))
    cws = int(input("How many orders of chicken wings do you want? "))
    sum = pizza*12 + pasta*6+ cws*8
    print(f"By ordering {pizza} pizzas, {pasta} orders of pasta, and {cws} orders of chicken wings, your order total comes to ${sum} ")

# Function Name: tipAndSplit()
# Parameters: N/A
# Returns: None

def tipAndSplit():
    total = int(input("What was the order total? "))
    ptip = int(input("What percentage would you like to tip? "))
    split = int(input("How many people are splitting the order? "))
    tip = total * (ptip/100)
    print(f"The driver got a tip of ${tip}. Each person paid ${(total+tip)/split}.")

# Function Name: youtuber()
# Parameters: N/A
# Returns: None

def youtuber():
    videos = int(input("How many videos have you made? "))
    perview = float(input("How much do you get paid per view? "))
    viewcount = int(input("How many views do your videos have? "))
    print(f"You have made ${videos*viewcount*perview} by making YouTube videos!")

# Function Name: bathBomb()
# Parameters: N/A
# Returns: None

def bathBomb():
    r = float(input("What is the radius of the bath bomb? "))
    v = (4/3)*(3.14)*(r**3)
    rounded = round(v, 2)
    print(f"The volume of a bath bomb with radius {r} is {rounded}. ")





