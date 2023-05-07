# Exercise 1 : Hello World-I Love Python
# Instructions
# Print the following output in one line of code:
    # Option 1
print("Hello world \nHello world \nHello world \nHello world \nHello world \nI love python \nI love python \nI love python \nI love python \nI love python")
    # Option 2
for i in range(10): print("Hello world") if i < 5 else print("I love python")

# Exercise 2 : What Is The Season ?
# Instructions
# Ask the user to input a month (1 to 12).
# Display the season of the month received :
# Spring runs from March (3) to May (5)
# Summer runs from June (6) to August (8)
# Autumn runs from September (9) to November (11)
# Winter runs from December (12) to February (2)

mounth_user = int(input("Input mounth (ex. 1-12): "))
if  1 <= mounth_user <= 12:
    if mounth_user >= 3 and mounth_user <= 5:
        season = "Spring"
    elif mounth_user >= 6 and mounth_user <= 8:
        season = "Summer"
    elif mounth_user >= 9 and mounth_user <= 11:
        season = "Autumn"
    else:
        season = "Winter"
    print(f" Season is: {season}")
else:
    print("Wrong number of mounth. Try again.")
