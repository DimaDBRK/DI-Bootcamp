# Exercise 1 : Hello World
# Instructions
# Print the following output in one line of code:
    # Option 1
print("Hello world \nHello world \nHello world \nHello world \nHello world")
    # Option 2
for i in range(5): print("Hello world")

# Exercise 2 : Some Math
# Instructions
# Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
print((99**3)*8)

# Exercise 3 : What Is The Output ?
# Instructions
# Predict the output of the following code snippets:
# >>> 5 < 3 - output  is:  False
# >>> 3 == 3 - output  is:  True
# >>> 3 == "3" - output  is:  False
# >>> "3" > 3 - Error
# >>> "Hello" == "hello" - output  is:  False

#  Exercise 4 : Your Computer Brand
# Instructions
# Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
computer_brand = "Asus"
   # Option 1
print(f"I have a {computer_brand} computer")
   # Option 2
print("I have a", computer_brand, "computer")

# Exercise 5 : Your Information
# Instructions
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code
name = "Dmitry"
age = 30
shoe_size = 42
info = f"My name is {name}. I'm {age} years old. I wear size {shoe_size} boots."
print(info)

# Exercise 6 : A & B
# Instructions
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.
a = 20
b = 10
if a > b:
    print("Hello World")

# Exercise 7 : Odd Or Even
# Instructions
# Write code that asks the user for a number and determines whether this number is odd or even.
a = int(input("Input number and I'll determines whether this number is odd or even: "))
if a % 2 > 0:
    print("This number is odd")
else:
    print("This number is even")
    
# Exercise 8 : What’s Your Name ?
# Instructions
# Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
my_name = "Dima"
user_name = input("Input your name: ")

if user_name.lower() == my_name.lower():
    print(f"Hello {user_name}. We have the same names. I like that name {my_name} become very popular.")
else:
    print(f"Hello {user_name}. We have different names. My name is {my_name}.")

# Exercise 9 : Tall Enough To Ride A Roller Coaster
# Instructions
# Write code that will ask the user for their height in inches.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.
height_inches = int(input("Input your height in inches: "))
if height_inches * 2.54 > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.")