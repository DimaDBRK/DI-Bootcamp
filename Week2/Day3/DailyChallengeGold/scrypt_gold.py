
# Instructions
# In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

# For example, with a left shift of 3 –> D would be replaced by A,
# –> E would become B, and so on.

# The method is named after Julius Caesar, who used it in his private correspondence.

# Create a python program that encrypts and decrypts messages with ceasar cypher.
# The user enters the program, and then the program asks him if he wants to encrypt or decrypt, and then execute encryption/decryption on a given message and a given shift.
#user_text = "abc 123"
user_text = "test"
step = 0

user_text = input("Input text:")
step = int(input("Input shift(step):"))
type = int(input("For Encode input = 1, for Decode = 2"))
if type == 2:
    step = -step

new_text = ""
for letter in user_text:
    new_text += chr(ord(letter) + step)
    
print("Your text: ",user_text)
print("Updated text: ", new_text)
