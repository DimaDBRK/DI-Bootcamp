# Week2 Day2
# Dayly Challenge
# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples
# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]
# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

num1 = int(input("Input first number : "))
num_len = int(input("Input length  : "))
fin_list = []
for i in range(1,num_len +1,1):
    fin_list.append(num1*i)
print(fin_list)

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples
# user's word : "ppoeemm" ➞ "poem"
# user's word : "wiiiinnnnd" ➞ "wind"
# user's word : "ttiiitllleeee" ➞ "title"
# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).
 
user_input = input("Input string : ")

# convert str to list 
user_list = list(user_input)
for i in range(len(user_list)-1,0,-1):
  print(i,user_list[i])
  if user_list[i] == user_list[i-1]: user_list.pop(i)
  print(user_list)
# convert list to str with join
user_input = ''.join(map(str, user_list))
print(user_input)