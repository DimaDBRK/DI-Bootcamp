# Week3 Day3
# Exercises XP+ Modules

# Instructions
# 1. In a file named func.py create a function that adds 2 number, and prints the result
# 2. In a file namedexercise_one.py import and the function
# Hint: You can use the the following syntaxes:

# import module_name # OR 
# from module_name import function_name # OR 
# from module_name import function_name as fn # OR
# import module_name as mn
from func import sum as fn

fn(3,5)

# 🌟 Exercise 2: Random Module
# Instructions
# Create a function that accepts a number between 1 and 100, then rolls a random 
# number between 1 and 100,
# if it’s the same number, display a success message to the user, else don’t.


def compare(a):
    import random
    list_num = [str(i) for i in range(1,101)] # it will allow input string and int to if
    rand_num = random.randint(1,100)
    if a in list_num and int(a) == rand_num: #int: #and int(a) >= 1 and int(a) <= 100:
        print("You win.")

compare(input("Enter number 1...100: "))

# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. 
# No numbers and a special symbol.
# Hint: use the string module
import string
import random

s = ""
symbols = string.ascii_lowercase + string.ascii_uppercase  
for i in range(5): s = s + random.choice(symbols) 
print(f'New string with len {len(s)} : {s}')

# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

def today_date():
    from datetime import date
    today = date.today()
    print(today)
    return today


today_date()

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

def till_101(): 
    from datetime import datetime
    now = datetime.now()
    target = datetime(now.year + 1,1,1,0,0,0,0)
    delta = target - now
    delta_time = (str(delta).split(", ")[1]).split(".")[0]
    print(f'the 1st of January is in {delta.days} days and {delta_time} hours')
    return delta


till_101()

# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument 
# (in the format of your choice), then displays a message stating 
# how many minutes the user lived in his life.

def bd_minutes(bd_date_str = input("Input birthdate YYYY-MM-DD : ")):
     
    from datetime import datetime, timedelta
    bd_date = datetime.strptime(bd_date_str, "%Y-%m-%d")
    now = datetime.now()
    
    delta = now - bd_date
    print(f'Here is minutes: {round(delta.total_seconds() / 60, 1)}')
    return 

bd_minutes()

# Exercise 7 : Upcoming Holiday
# Instructions
# Write a function that displays today’s date.
# The function should also display the amount of time left from now until the 
# next upcoming holiday and print which holiday that is. 
# (Example: the next holiday is in 30 days and 12:03:45 hours).
# Hint: Start by hardcoding the datetime and name of the upcoming holiday.

def next_holiday(): 
    from datetime import datetime
    now = datetime.now() 
    print(f'Today date: {str(now.date())}')
    holoday_list = [{'name': 'Holiday1', 'h_date' : datetime(now.year, 6,17), 'h_delta': 0},
                    {'name': 'Holiday2', 'h_date' : datetime(now.year,4,17), 'h_delta': 0},
                    {'name': 'Holiday3', 'h_date' : datetime(now.year,7,17), 'h_delta': 0}]
    for items in holoday_list:
        if items.get("h_date") < now:
            items["h_date"] = datetime(now.year + 1, 6,17) 
        items["h_delta"] = items["h_date"] - now
    
    minDeltaItem = min(holoday_list, key=lambda x:x['h_date'])
          
    next_holiday_date = minDeltaItem['h_date']
    next_holiday_name = minDeltaItem['name']
    
    delta = next_holiday_date - now
    delta_time = (str(delta).split(", ")[1]).split(".")[0]
    print(f'Next holiday is {next_holiday_name} on {str(next_holiday_date.date())} in {delta.days} days and {delta_time} hours')
    return delta

next_holiday()

# Exercise 8 : How Old Are You On Jupiter?
# Instructions
# Given an age in seconds, calculate how old someone would be on:
# Earth: orbital period 365.25 Earth days, or 31557600 seconds
# Mercury: orbital period 0.2408467 Earth years
# Venus: orbital period 0.61519726 Earth years
# Mars: orbital period 1.8808158 Earth years
# Jupiter: orbital period 11.862615 Earth years
# Saturn: orbital period 29.447498 Earth years
# Uranus: orbital period 84.016846 Earth years
# Neptune: orbital period 164.79132 Earth years
# So if you are told someone is 1,000,000,000 seconds old, the function 
# should output that they are 31.69 Earth-years old.

def age_planets(a_sec):
    
    age_Earth_sec = 31557600
    age_Earth = a_sec/age_Earth_sec
    print(f'if you are told someone is {a_sec} seconds old, so you are:')
    res = [{'planet': 'Earth','k': 1,'age': 0 },
           {'planet': 'Mercury','k': 0.2408467,'age': 0 },
           {'planet': 'Venus','k': 0.61519726,'age': 0 },
           {'planet': 'Mars','k': 1.8808158,'age': 0 },
           {'planet': 'Jupiter','k': 11.862615,'age': 0 },
           {'planet': 'Saturn','k': 29.447498,'age': 0 },
           {'planet': 'Uranus','k': 84.016846,'age': 0 },
           {'planet': 'Neptune','k': 164.79132,'age': 0 },
        ]
    
    for items in res:
        items["age"] = round((age_Earth/items.get("k")),2)
        s = "s" if  items["age"] >= 2 else ""
        print(f'___ {items.get("age")} year{s} on the {items.get("planet")}')
    
#Drivers    
s = 1000000000
age_planets(s)


# Exercise 9 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to 
# properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has 
# the following keys: name, adress, langage_code. Use faker to populate them 
# with fake data.

# Install the faker module,+
from faker import Faker

users = []
fake = Faker()

def add_user():
    user_info = {'name':fake.name(), 'adress': fake.address(),'language_code':fake.language_code()}
    return user_info

for i in range(10):
    users.append(add_user())
        
print(add_user())
print(users)

