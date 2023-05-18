# Week3 Day4
# Dmitry Dubrov
# Daily Challenge : Text Analysis

# Instructions :
# The goal of the exercise is to create a class that will help you analyze a 
# specific text. A text can be just a simple string, like “Today, is a happy day” or it can be an external text file.
# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.

# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
# Implement a classmethod that returns a Text instance but with a text file:
#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.
# Now, use the provided the_stranger.txt file and try using the class you created above.
# Bonus:
# Create a class called TextModification that inherits from Text.
# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

#import
import os
import random
import string


#classes
class Text() :
    
    def __init__(self, str_in):
        self.text_str = str_in
        # self.text_list = self.text_str.lower().split()

# Implement the following methods:

    def freq_of_all(self) : #returm dic word -qty in text
        lst = self.text_str.lower().replace('.','').split() #18.05 after class review added "." to split
        words = {}
        for items in lst:
            if items not in words:
                words[items] = lst.count(items)
        return words
    
    
# a method to return the frequency of a word in the text (assume words are separated 
# by whitespace) return None or a meaningful message.
    def freq_words(self, word) :
        dic = self.freq_of_all()
        if word not in dic:
            str_out = None
        else:
            qty = dic[word]
            str_out = f'The text has words " {word} ": {qty} times'  #make it more good
        return str_out                    
                        
    
    #a method that returns the most common word in the text.
    def common_word(self) :
        dic = self.freq_of_all()
        max_qty = max(dic.values()) #updated 18.05 after review in class
        res = [item for item, q in dic.items() if q == max_qty]
        # max = max(dic, key=dic.get)
        return res #max(dic, key=dic.get)
    
    
    # a method that returns a list of all the unique words in the text.
    def unique_word(self) :
        dic = self.freq_of_all()
        res = [item for item, q in dic.items() if q == 1]
        return res             
    
    @classmethod
    def from_file(cls, filename) :
         #path to file
        dir_path = os.path.dirname(os.path.realpath(__file__))
    
        with open((dir_path+"\\" + filename), "r") as file_in :
            new_text = file_in.read()
        return cls(new_text)

#     Bonus:
# Create a class called TextModification that inherits from Text.
class TextModification(Text) :
    # init  to
    def __init__(self, text):
        super().__init__(text)
        
    # Implement the following methods:
# a method that returns the text without any punctuation.
    def no_punctuation(self):
        str = self.text_str
        for character in string.punctuation:
            str = str.replace(character, '')
        return str
# a method that returns the text without any english stop-words (check out what this is !!).    
    def no_stop_words(self):
        stop_words = ["i", "was", "a", "an", "the", "and", "but", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "can", "will", "just"]
        lst = self.text_str.split()
        filtered_words = [] 
        # Iterate over the list of words 
        for word in lst: 
        # If the word is not in the stop word list, add it to the filtered list 
            if word.lower() not in stop_words: 
                filtered_words.append(word) 
        str = " ".join(filtered_words)
        return str
    
    
#  a method that returns the text without any special characters.
    def no_special(self):
        str = ""
        for char in self.text_str:
            if char == ' ':
                str += ' '
            elif char.isalnum(): #isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers)
                str += char
        # Option 2. With string of symbols
        # str = self.text_str
        # spech_str = '[@_!#$%^&*()<>?/\|}{~:]'
        # for character in spech_str:
        #     str = str.replace(character, '')
        
        return str
    
#input data
text_input = "A good book would sometimes cost as much as a good house."
# tests
a = Text(text_input)
print(a.freq_of_all())
print(a.freq_words('book'))
print(a.common_word())
print(a.unique_word())


#Part 2
filename =  'the_stranger.txt'


b = Text.from_file(filename)
b.freq_of_all()
print(b.freq_words('the'))
print(b.common_word())
print(b.unique_word())

c = TextModification(text_input)
print(c.no_punctuation())
print(c.no_stop_words())
print(c.no_special())

d = TextModification.from_file(filename)
new_txt = d.no_stop_words()
c = TextModification(new_txt)
print(c.common_word())