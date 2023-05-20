# Week3 Day5
# Dmityr Dubrov
# Mini-Project #2 : Anagram Checker
# This will contain all the UI (user interface) functionality of your program,
# and will rely on AnagramChecker for the anagram-related logic.

#imports
from anagram_checker import AnagramChecker
import time

def user_in_str():
    print("\nAnagram Checker:")
    in_str = input("Input word:")
    return in_str

def anagram_print(list):
    if len(list) > 1:
        print(f'Anagrams for your word: {", ".join(list)}.')
    else:
        print("No Anagrams for your word.")
    

def check_input_word(user_str) :
#     If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
# Only alphabetic characters are allowed. No numbers or special characters.
# Whitespace should be removed from the start and end of the user’s input.
    
    #check if Only alphabetic characters
    Alfabet = user_str.isalpha()
    #Whitespace should be removed from the start and end
    user_str = (user_str.rstrip().lstrip())
    #Only a single word is allowed
    spaces = " " not in user_str
    if not Alfabet: print("Only alphabetic characters are allowed. No numbers or special characters.")
    if not spaces: print("Only a single word is allowed.")
    
    if Alfabet and spaces:
        res = user_str
    else:
        res = "typeerror###"
    return res

# def find_anagrams(element, word_in):
# #     Once your code has decided that the user’s input is valid, 
# #                   it should find out the following:
# # All possible anagrams to the user’s word.
#     res = False
#     if element.is_valid_word(word_in):
#         res = element.get_anagrams(word_in)
#     return res


def get_user_menu_choice() :
    """
    this should display a simple menu, get the user’s choice 
    (with data validation), and return the choice. 
    No looping should occur here.
    
    """
    conf_in = "12aq"
    return_dict = {'a':'Find anagrams for the word', '1':'Find anagrams for the word','e':'Exit', '2':'Exit'}
    print("\nMenu:")
    print("(1)(a) - Find anagrams for the word")
    print("(2)(e) - Exit")
    
    user_in = input("Input menu item: ").lower()
    user_in = "".join(user_in.split()) #remove spaces from user input
    if user_in not in conf_in or user_in == "" :
        print("Wrong symbol input")
        res = "typeerror"
    else:
        res = return_dict[user_in]
    return res       

def main() :
    conf_in = ['Find anagrams for the word','Exit','typeerror']
    play1 = AnagramChecker()
    while True:
        # Show a menu, offering the user to input a word or exit. 
        # Keep showing the menu until the user chooses to exit.
        res = get_user_menu_choice()
        if res == conf_in[1] :
            print(f'You chose: {conf_in[1]}')
            break
        
        elif res == conf_in[0] :
            user_in = check_input_word(user_in_str())
          
            if user_in != "typeerror###" :
                if play1.is_valid_word(user_in):
                    print(f"Let's find anagram for word '{user_in}'.")
                    print("This is English word.")
                    start = time.time()
                    list_anagram = play1.get_anagrams(user_in)
                    time_1 = round(time.time() - start, 4)
                    print(f'It takes {time_1} s to get result')
                    anagram_print(list_anagram)
                else:
                    print(f"{user_in} -is not English word.")
               
            
#Driver

main()


#Test