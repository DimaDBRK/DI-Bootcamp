# Exercise 3 : Outputs
# >> > 3 <= 3 < 9 - True
# >> > 3 == 3 == 3 - True
# >> > bool(0) - False
# >> > bool(5 == "5") - Error
# >> > bool(4 == 4) == bool("4" == "4") - True
# >> > bool(bool(None)) - False
# x = (1 == True) - True
# y = (1 == False) - False
# a = True + 4 ---- 5
# b = False + 10 ---- 10
#
# print("x is", x) ---- x is True
# print("y is", y) ---- y is False
# print("a:", a) ---- 5
# print("b:", b) ---- 10

# Exercise 4 : How Many Characters In A Sentence ?
# Instructions
# Use python to find out how many characters are in the following text, use a single line of code (beyond the establishment of your my_text variable).
# my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit,
#            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
#            Ut enim ad minim veniam, quis nostrud exercitation ullamco
#            laboris nisi ut aliquip ex ea commodo consequat.
#            Duis aute irure dolor in reprehenderit in voluptate velit
#            esse cillum dolore eu fugiat nulla pariatur.
#            Excepteur sint occaecat cupidatat non proident,
#            sunt in culpa qui officia deserunt mollit anim id est laborum.

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, " \
          "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." \
          "Ut enim ad minim veniam, quis nostrud exercitation ullamco" \
          "laboris nisi ut aliquip ex ea commodo consequat." \
          "Duis aute irure dolor in reprehenderit in voluptate velit" \
          "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, " \
          "sunt in culpa qui officia deserunt mollit anim id est laborum."
qty_characters = len(my_text) - my_text.count(" ")

# Exercise 5: Longest Word Without A Specific Character
# Instructions
# Keep asking the user to input the longest sentence they can without the character “A”.
# Each time a user successfully sets a new longest sentence, print a congratulations message.

user_sentence = ""
max_len = 0
while user_sentence not in  ["exit","q","c","Q","C"]:
    user_sentence = input("Input the longest sentence they can without the character “A”. For exit input exit or q or c : ")
    if (user_sentence.find("a") != -1 or user_sentence.find("A") != -1):
        print("You input A try again")
    else:
        if len(user_sentence) > max_len:
            max_len = len(user_sentence)
            print(f"Congratulations. Your sentenc is new longest = {max_len}.")
        else:
            print("Try again. To short.")
