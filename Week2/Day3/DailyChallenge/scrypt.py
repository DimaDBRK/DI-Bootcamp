# Week 2 Day 3
# DailyChallenge
# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of 
# each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }
# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}

# Option 1.
#user_word = input("Input your word : ")
letter_dic = {}
user_word = "qqqqq2445455553241ddddfffg112135"
# start loop in str  = user_word from letter index 0 to last letter (calculate with str len)
for i in range(len(user_word)):
    # check if there are no this letter uin keys of dictonary with uasing .get method. 
    # it provides None in case if there is not this letter exist in dictinary, or index if it is
    if letter_dic.get(user_word[i]) == None:
        # there is no tis letter, so we add new pair of key = letter in string (user_word[i]) 
        # and value = index. Pay attantion, we shoud set value to the list with uasing [], 
        # it will allow to add in fitute indexes of the same letters
        letter_dic[user_word[i]] = [i]
    else:
        #if this letter = user_word[i] exist, we take value for the key = this letter = 
        # = ser_word[i], value wull be list. And add current index to the list with .append method.
        letter_dic[user_word[i]].append(i)
        
print(letter_dic)

    # Option 2. With enumerate and dict
user_word = "qqqqq2445455553241ddddfffg112135"
user_dict = {letter : [] for letter in user_word}
for i,letter in enumerate(user_word):
    user_dict[letter].append(i)   
print(user_dict)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.

items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

wallet = "$100" 

fin_list = []
for product, price in items_purchase.items():
    if (int(price.replace("$","").replace(",",""))) <= (int(wallet.replace("$","").replace(",",""))):
        fin_list.append(product) 
        
if len(fin_list) != 0:
    fin_list.sort()
    print(fin_list)
else:
    print("Nothing")
print