# Week3 Day5
# Dmityr Dubrov
# Mini-Project #2 : Anagram Checker
# We will create a program that will ask the user for a word.
# It will check if the word is a valid English word, and then find 
# all possible anagrams for that word.

#imports
import os
import time 
# After Dmitry's message in slack, I would like to test variants to speed up 
# process. Also, the same items discussed on stackoverflow

# stuff to run always here such as class/def

class AnagramChecker :
    
    #should load the word list file (text file) into a variable, 
    # so that it can be searched later on in the code.
    def __init__(self) :
        #get info from file
        filename = "sowpods.txt"
        self.words_list = self.list_of_words(filename)
        
    #it helps to get words to list  from txt file
    @staticmethod
    def list_of_words(filename) :
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open((dir_path+"\\" + filename), "r") as file_in:
            lst = [item.replace('\n', '').lower() for item in file_in.readlines()]
        return lst
    # should check if the given word (ie. the word of the user) is a valid word.
    def is_valid_word(self, word) :
        res = word.lower() in self.words_list
        return res
    
    # Hint: you might want to create a separate method called 
    # is_anagram(word1, word2), that will compare 2 words and return 
    # True if they contain the same letters (but not in the same order),
    # and False if not.
    def is_anagram(self, word_user, word_from_dict) :
        return word_user == self.sortString(word_from_dict)
    
    @staticmethod
    def sortString(str) :
        str = ''.join(sorted(str))  
        return str
       
    # should find all anagrams for the given word. (eg. if word of the user is 
    # ‘meat’, the function should return a list containing 
    # [“mate”, “tame”, “team”].)
    def get_anagrams(self, word) :
          
        # def sortString(str) :
        #     str = ''.join(sorted(str))  
        #     return str
        word_sorted = self.sortString(word.lower())
        
        list_of_words = []
        for items in self.words_list:
            if word[0].lower() in items: #added check if on of the word
                #under test is in word from dictonary (list of words) aprox. 0,06s
                if self.is_anagram(word_sorted, items) and word.lower() != items: #don't add user's word
                    list_of_words.append(items) 
                    
        return list_of_words

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
#Tests

    a = AnagramChecker()
    print(a.words_list[1])
    print(a.is_valid_word("print"))
    test_word = "MEAT"

    # test time
    start = time.time()
    print(a.get_anagrams(test_word))
    time_1 = round(time.time() - start, 4)
    print(time_1)