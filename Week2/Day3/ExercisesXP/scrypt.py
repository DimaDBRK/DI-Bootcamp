# Week2 Day3
# Exercises

# 🌟 Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

res = zip(keys, values)
res_dct = dict(res)
print(res_dct)

# 🌟 Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable 
# (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# How much does each family member have to pay ?

total = 0
for name, age in family.items():
   
    if age > 3 and age <= 12:
        price = 10
    elif age > 12:
         price = 15
    else:
        price = 0
    print(f"{name} should pay {price} $")
    total += price
# Print out the family’s total cost for the movies.
print(f"total price is {total} $")

# Bonus: Ask the user to input the names and ages instead of using the provided family variable 
family2 = {}
while True:
    name = input("Enter name (for exit - quit):")
    if name == "quit":
        break
    age = input("Enter age: ")
    family2[name] = int(age)
print(family2)

# 🌟 Exercise 3: Zara
# Instructions
# 1. Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green


# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3. Change the number of stores to 2.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

# 2. Create a dictionary brand
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue", 
        "Spain": "red", 
        "US": ["pink", "green"]
    }
}

# 3. Change the number of stores to 2.
brand["number_stores"] = 2


# 4. Print a sentence that explains who Zaras clients are.
    #Option 1.
print(f'{brand["name"]} is brand for people in countries like {", ".join(brand["major_color"].keys())}. \
Clients are {", ".join(brand["type_of_clothes"][0:3])}. ')
    #Option 2.
print('{name} is brand for people in different countries.'.format_map(brand))

# 5. Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
print(brand)

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if brand.get("international_competitors") != None:
    brand["international_competitors"].append("Desigual")
else:
    print("Sorry, there is no key in dictonary.")
    
# 7. Delete the information about the date of creation.
    #Option 1. 	POP - Removes the element with the specified key
brand.pop("creation_date")
    #Option 2. 	del
#del brand["creation_date"]
    #Option 3. 	only value
#brand["creation_date"] = ""

# 8. Print the last international competitor.
print(brand["international_competitors"][-1])

# 9. Print the major clothes colors in the US.
print(", ".join(brand["major_color"]["US"]))
# 10. Print the amount of key value pairs (ie. length of the dictionary).
print(len(brand))
# 11. Print the keys of the dictionary
print(", ".join(brand.keys()))
    
# 12. Create another dictionary called more_on_zara with the following details:
# creation_date: 1975 
# number_stores: 10 000

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000 
}


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

brand.update(more_on_zara)

# 14. Print the value of the key number_stores. What just happened ?
print(brand["number_stores"])
#10000 - It's replace value for key number_stores form 2 to 10000.

# Exercise 4 : Disney Characters
# Instructions
# Use this list :

# users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
disney_users_A = {users[i]: i for i in range(0,len(users),1)} 
print(disney_users_A)

# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
disney_users_B = dict(enumerate(users))
print(disney_users_B)

# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

#sort list
users.sort()

disney_users_C = {users[i]: i for i in range(0,len(users),1)} 
print(disney_users_C)

# Only recreate the 1st result for:
# {"Mickey": 0, "Minnie": 1, 

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# The characters, which names contain the letter “i”.
    #Option 1. with new index
disney_users_i = {}
num = 0
for item in users:
    if item.find('i') != -1:
        disney_users_i[item] = num
        num += 1
print(disney_users_i)

    #Option 2. with old index
disney_users_i.clear()
disney_users_i = {users[i]: i for i in range(0,len(users),1) if users[i].find("i") != -1} 
print(disney_users_i)

# The characters, which names start with the letter “m” or “p”.

    #Option 1. with new index
disney_users_m_p = {}
num = 0
for item in users:
    if item[0].lower() in ["m", "p"]:
        disney_users_m_p[item] = num
        num += 1
print(disney_users_m_p)
   #Option 2. with old index
disney_users_m_p.clear()
disney_users_m_p = {users[i]: i for i in range(0,len(users),1) if users[i][0].lower() in ["m", "p"]} 
print(disney_users_m_p)

