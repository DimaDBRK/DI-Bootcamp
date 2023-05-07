# Week 2 - Day 1
# Dmitry Dubrov
# Daily Challenge: Build Up A String
# 1. Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# 2. Then, print the first and last characters of the given text.
#
# 3. Using a for loop, construct the string character by character: Print the first character,
# then the second, then the third, until the full string is printed.

# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).

# 1
user_str = input("Please input string. It should be 10 characters long : ")
if len(user_str) < 10:
    print("string not long enough")
elif len(user_str) > 10:
    print("string too long")

# 2 print the first and last characters
print(user_str[0])
print(user_str[-1])

# 3. Using a for loop, construct the string character by character
for i in range(len(user_str)+1):
    print(user_str[0 : i])

# 4. Bonus: Swap some characters around
import random
# conver str to list, need to use - shuffle
char_list = list(user_str)
random.shuffle(char_list)

# conver list to str by elements
user_str_new =  ""
for i in char_list:
        user_str_new += i

print(user_str_new)