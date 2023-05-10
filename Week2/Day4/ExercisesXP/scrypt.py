# Exercise 1 : What Are You Learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in 
# this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print("I am learning SW development.")

display_message()

# 🌟 Exercise 2: What’s Your Favorite Book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f'One of my favorite books is {title}')

favorite_book("Ecomomist")


# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country):
    print(f'{city} is in {country}')

describe_city("New York", "USA")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number 
# randomly between 1 and 100.
# Compare the two numbers, if it’s the same number, 
# display a success message, otherwise show a fail message and display both numbers.

def number_formula(user_number):
    import random
    if user_number >=1 and user_number <= 100:
        rand_number = random.randint(1,100)
        print("Ssuccess") if int(user_number) == rand_number else print(f'Fail. Your number: {int(user_number)} and \
random number is {rand_number}.')
    else:
        print("Number is not correct. It shold be between 1 and 100.")
#tests:
number_formula(2)
number_formula(0)
number_formula(50)
number_formula(100)
number_formula(110)

# 🌟 Exercise 5 : Let’s Create Some Personalized Shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the 
# shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as 
# "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads 
# “I love Python” by default.
# Make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirt(size, text):
    print(f'The size of the shirt is: {size} and the text is: {text}')
    
make_shirt("L", "Hello!")

# Modify the make_shirt() function so that shirts are large by default with a message that reads 
# “I love Python” by default.

def make_shirt2(size = "L", text = "I love Python"):
    if str(size).lower() not in "lsmxlxsxxlxlxxxl":
        size = "L"
    if str(text).lower() in ['        ',""]:
        text = "I love Python"
    print(f'New! The size of the shirt is: {size} and the text is: {text}')
#tests size        
make_shirt2("M", "Hello!")
make_shirt2("XS", "Hello!")
make_shirt2(2, "Hello!")
#tests text
make_shirt2("S", "")
make_shirt2("S", "  ")
make_shirt2("S", "def")
make_shirt2("S", "Hi!!!")

# Make a large shirt with the default message
make_shirt2()
# Make medium shirt with the default message
make_shirt2("M")
# Make a shirt of any size with a different message.
make_shirt2("S", "Hi 123!")

#Bonus: Call the function make_shirt() using keyword arguments.
make_shirt(text = "This is bonus!", size = "XL")

# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" 
# to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

#Pass the list to a function called show_magicians(), which prints the name of each magician in the list.

def show_magicians(user_list):
    print(", ".join(user_list))

show_magicians(magician_names)

# Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" 
# to each magician’s name.

def make_great(user_list):
    for i in range(len(user_list)):
        user_list[i] = " ".join(("The Great", user_list[i]))
        
# Call the function make_great().
make_great(magician_names)
# Call the function show_magicians() to see that the list has actually been modified.
show_magicians(magician_names)
#test result: The Great Harry Houdini, The Great David Blaine, The Great Criss Angel

# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees 
# Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper 
# limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly.
# Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). 
# Determine the season according to the month.

# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.

def get_random_temp():
    import random
    return random.randint(-10,40)

# Test your function to make sure it generates expected results.
i = 0
test= []
while i < 1000:
    i += 1
    test.append(get_random_temp())

for item in test:
    res1 = "Temp rnage is NOT OK" if (item <= -10 and item >= 40) else "Temp rnage is OK"
    res2 = "Not integer" if type(item) != int else "Temp type is OK"
print("get_random_temp() test results:", res1, "&", res2)
#  result: Temp rnage is OK & Temp type is OK

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees 
# Celsius.”

def main():
    user_temp = get_random_temp()
    print(f'The temperature right now is {user_temp} degrees ')

main()

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

def main():
    user_temp = get_random_temp()
    print(f'The temperature right now is {user_temp} degrees ')
    if user_temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif user_temp >= 0 and user_temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif user_temp >= 16 and user_temp <= 23:
        print("That's good!")
    elif user_temp >= 24 and user_temp < 32:
        print("Hot! Don't forget hat")
    elif user_temp >= 32 and user_temp <= 40:
        print("Very hot! May be better to stay at home!")
main()

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper 
# limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
def get_random_temp(season = "summer"):
    # if season in ["winter","spring", "summer", "autumn"] - else - set to summer:
    if season == "winter":
        min, max = -40, 0
    elif season == "spring":
        min, max = -10, 25
    elif season == "summer":
        min, max = 5, 40
    elif season == "autumn":
        min, max = -5, 25
    else:  
        print(f'{season} is NOK. Should be like "winter","spring", "summer", "autumn". Check it' )
        min, max = -40, 40
    import random
    return random.randint(min,max)

print(get_random_temp())

# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly.
# Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

def main():
    user_season = input("Input season - 'winter','spring', 'summer', 'autumn': ")
    user_temp = get_random_temp(user_season)
    print(f'It is {user_season} and {user_temp} degrees.')
    if user_temp < 0:
        print(f"Brrr, that’s freezing! Wear some extra layers today")
    elif user_temp >= 0 and user_temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif user_temp >= 16 and user_temp <= 23:
        print("That's good!")
    elif user_temp >= 24 and user_temp < 32:
        print("Hot! Don't forget hat")
    elif user_temp >= 32 and user_temp <= 40:
        print("Very hot! May be better to stay at home!")

main()

# Bonus: Give the temperature as a floating-point number instead of an integer.
def get_random_temp(season = "summer"):
    # if season in ["winter","spring", "summer", "autumn"] - else - set to summer:
    if season == "winter":
        min, max = -40, 0
    elif season == "spring":
        min, max = -10, 25
    elif season == "summer":
        min, max = 5, 40
    elif season == "autumn":
        min, max = -5, 25
    else:  
        print(f'{season} is NOK. Should be like "winter","spring", "summer", "autumn". Check it' )
        min, max = -40, 40
    import random
    # change method from .randint to .randrange()
    return round(random.uniform(min,max),1)

print(get_random_temp())


# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). 
# Determine the season according to the month.

#add new function which Determine the season according to the month number:

def get_season(number):
    if number in [9,10,11] :
        season = "autumn"
    elif number in [6,7,8]  :
        season = "summer"
    elif number in [3, 4, 5] :
        season = "spring"
    elif number in [12,1,2] :
        season = "winter"
    else:
        print(f"Ypu input {number} and it is not number of mounth. So, it will be Jan  = 1 and winter") 
        season = "winter"  
    return season
   
def main():
    user_mounth = int(input("Input mounth from 'Jan' = 1 to 'Dec' = 12: "))
    user_season = get_season(user_mounth)
    user_temp = get_random_temp(user_season)
    print(f'It is {user_mounth} mounth in {user_season}. {user_temp} degrees.')
    if user_temp < 0:
        print(f"Brrr, that’s freezing! Wear some extra layers today")
    elif user_temp >= 0 and user_temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif user_temp >= 16 and user_temp <= 23:
        print("That's good!")
    elif user_temp >= 24 and user_temp < 32:
        print("Hot! Don't forget hat")
    elif user_temp >= 32 and user_temp <= 40:
        print("Very hot! May be better to stay at home!")

#test     
print("tets upgrade:")
main()