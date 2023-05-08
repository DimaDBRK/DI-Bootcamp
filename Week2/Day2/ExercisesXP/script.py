# Week2 Day2
# Exercises XP

# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_number = {122, 125, 14, 6}

   
    #Option 1. Add two new numbers to the set.
my_fav_number.add(15)
my_fav_number.add(18)


    #Option 2. Add two new numbers to the set.
my_fav_number.update((20, 21))

    # Remove the last number.
#my_fav_number.pop(-1)

friend_fav_numbers = {1, 2, 3}

    # Concatenate my_fav_numbers and friend_fav_numbers
our_fav_numbers = my_fav_number.union(friend_fav_numbers)


# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
y = list(thistuple)
y[2] = "milk"
thistuple = tuple(y)


# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove “Banana” from the list.
basket.remove("Banana")
print(basket)
# Remove “Blueberries” from the list.
basket.remove("Blueberries")
    # Option 2:
    # basket.pop(-1)
print(basket)
# Add “Kiwi” to the end of the list.
basket.append("Kiwi")
print(basket)
# Add “Apples” to the beginning of the list.
basket.insert(0, "Apples")
print(basket)
# Count how many apples are in the basket.
basket.count('Apples')
# Empty the basket.
basket.clear()
# Print(basket)
print(basket)

# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?

# Float is used to represent real numbers and is written with a decimal point dividing the integer and fractional parts.
# Integer (pronounced IN-tuh-jer) is a whole number (not a fractional number) that can be positive, negative, or zero.

# Can you think of another way to generate a sequence of floats?
#It is possible to use loop with formula inside, also thera are several libraries for import (ex. numpy package). 

# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
    #Option 1.
dig_sequence = []
start = 1.5
step = 0.5
for i in range(8):
    dig_sequence.append(start + step * i)



#Option 2.
dig_sequence = []
start = 1.5
step = 0.5
end = 10
while start < end:
    start += step 
    dig_sequence.append(start)


# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(1,21,1):
    print(i, end=" ")

    #Option 1. Even elements = numbers (1...20)
print("\neven elements:")
for i in range(1,21,1):
    if i % 2 == 0: print(i, end=" ")
    #Option 2. Elements with even index (first element - index = 0, last = 19)
print("\neven index of elements:")
for i in range(1,21,1):
    if i % 2 != 0: print(i, end=" ")

# 🌟  Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
print("\nExercise 6:")
user_name = ""
my_name = "Dima"
while user_name != my_name:
    user_name = input(f"Input your name. I will ask you unless the input will be equal to my name - {my_name}: ")
    print(user_name)
    
#     🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

user_fruits = (input("Input their favorite fruit(s) - separate the fruits with a single space: ")).split()

input_fruit = input("Input a name of any fruit: ").replace(' ', '')

if input_fruit in user_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy.")

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

topping_list = []
topping_input = ""
while topping_input != "quit":
    topping_input = input("Enter a series of pizza toppings (for stop - input quit )")
    if topping_input != "quit":
        topping_list.append(topping_input)
        print(f"you’ll add topping {topping_input} to youy pizza")
    else:
        print("Ok, lets go to the next step.")
        for item in topping_list:
            print("topping : ",item)
        print("Total price is (10 + 2.5 for each topping): ",(10 + 2.5*len(topping_list)), "-")

# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.

# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

    #total cost of all the family’s tickets
age_list = []
age_input = ""
total_price = 0

age_list = (input("Input age of each person who wants a ticket - separate it with a single space: ")).split()

for item in age_list:
    if int(item) <= 3:
        continue
    elif int(item) > 3 and int(item) <= 12:
         total_price += 10
    else:  
        total_price += 15
print(f"total cost of all the family’s tickets : {total_price} $")

    #Given a list of names
    #Option 1. With additional list
visitors_names = ["Tony", "Mary", "Jhon", "Bob", "Albert"]
names_not_permitted = []
visitors_age_list = []
visitor_age_input = ""
        #ask teenager for their age


for item in visitors_names:
    visitor_age_input = int(input(f"{item} Please input your age : "))
    if  visitor_age_input >= 16 and visitor_age_input < 21:
        names_not_permitted.append(item)

for item in names_not_permitted:
    visitors_names.remove(item)
print(visitors_names)

     #Option 2. With reverce direct of list
visitors_names = ["Tony", "Mary", "Jhon", "Bob", "Albert"]
for item in reversed(visitors_names):
    visitor_age_input = int(input(f"{item} Please input your age : "))
    if  visitor_age_input >= 16 and visitor_age_input < 21:
        visitors_names.remove(item)
print(visitors_names)

# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# an empty list called finished_sandwiches
finished_sandwiches = []
for item in sandwich_orders:
    finished_sandwiches.append(item)
    print(f"I made your tuna sandwich {item} .")
sandwich_orders.clear()

# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.


sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Pastrami sandwich", "Pastrami sandwich", "Sabih sandwich", "Pastrami sandwich"]
#make sure the sandwich ‘pastrami’ appears in the list at least three times.
if sandwich_orders.count("Pastrami sandwich") >= 3:
    print(f"there are more 3 Pastrami")

#use a while loop to remove all occurrences of ‘pastrami’
print("The deli has run out of pastrami.")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

#end up in finished_sandwiches.
finished_sandwiches = []
for item in sandwich_orders:
    if item != "Pastrami sandwich": # Make sure no pastrami sandwiches
        finished_sandwiches.append(item)
        print(f"I made your tuna sandwich {item} .")
    else:
        print(f"No ingredients for {item}.")
