# Week3Day4
# Dmitry Dubrov
# Exercises XP

# 🌟 Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# Download this word list
# Save it in your development directory.
# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?
# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.
# Take the random words and create a sentence (using a python method), the sentence should be lower case.
# Create a function called main which will:
# Print a message explaining what the program does.
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.


#import
import os
import random

#functions

# Create a function called get_words_from_file. 
# This function should read the file’s content and return the words as a collection. 
# What is the correct data type to store the words?
def get_words_from_file(filename):
    #path to file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    
    with open((dir_path+"\\" + filename), "r") as file_in:
        lst = file_in.read().split()
    return lst
# Create another function called get_random_sentence which takes a single 
# parameter called length. The length parameter will be used to determine 
# how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

def get_random_sentence(length):
    res = []
    words = get_words_from_file("sowpods.txt")
    for i in range(length):
       res.append(random.choice(words))
    # Take the random words and create a sentence (using a python method), 
    # the sentence should be lower case.
    str_out = (' '.join(res)).capitalize() + "." # Make it more beautiful way
        
    return str_out

# Create a function called main which will:
def main() :
    # Print a message explaining what the program does.
    print("This function takes the random words and create a sentence (using a python method).Len - input from user.")
   
    # Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
    len = input("How long you want the sentence to be (an integer between 2 and 20): ")
    len_range = [str(i) for i in range(2,21)]
    try:
        if len in len_range:  # If the user inputs correct data, run your code.
            print(get_random_sentence(int(len)))   
        else: # If the user inputs correct data, run your code.
            raise TypeError(f"Incorrect data - length should be an integer between 2 and 20.")
    except TypeError as error:
                    print(TypeError.__name__, error)
    return 
    

#Driver
main()

# 🌟 Exercise 2: Working With JSON
# Instructions
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

import json
import os

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Access the nested “salary” key from the JSON-string above.
new_d = json.loads(sampleJson) #If you have a JSON string, you can parse it by using the json.loads()
target = new_d['company']['employee']['payable']['salary']
    #test link
if target == 7000: print("salary - Ok")

# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
new_d['company']['employee']['birth_date'] = 0
    #test 
target2 = new_d['company']['employee']['birth_date']
    #test link
if target2 == 0: print("birth_date - Ok")

# Save the dictionary as JSON to a file.

#path to file
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = "new_test_json"
with open((dir_path+"\\" + filename), "w") as file_out:
    file_out.write(str(new_d))

    #test 
 
with open((dir_path+"\\" + filename), "r") as file_in:
        str = file_in.readline()
print(str)