# Week3 Day1
# Dmitry Dubrov
# Exercises XP

# 🌟 Exercise 1: Cats
# Instructions
# Using this class

# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”.
# Use the function previously created.
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        
        

# Instantiate three Cat objects using the code provided above.
cat1 = Cat("Snow",3)
cat2 = Cat("Milk",5)
cat3 = Cat("Small",7)

# Outside of the class, create a function that finds the oldest cat and returns the cat.
# I try to find a solutio with lambda instead of loop
def oldes_cat(*item) :
    item
    max_age = max(item, key=lambda x: x.age)
    return max_age

# Print the following string:
print(f'The oldest cat is {oldes_cat(cat1,cat2,cat3).name} and is {oldes_cat(cat1,cat2,cat3).age} years old.')

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. 
# This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> 
# cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and 
# his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the 
# name of the bigger dog.

class Dog:
    def __init__(self, name, height):
        self.dog_name = name
        self.dog_height = height
    
    
    # Create a method called bark that prints the following string “<dog_name> goes woof!”.
    def bark(self):
        print(f'{self.dog_name} goes woof!')
        
    # Create a method called jump that prints the following string “<dog_name> jumps <x> 
    # cm high!”. x is the height*2.
    def jump(self):
        print(f'{self.dog_name} jump {self.dog_height * 2} cm high!')
        
# Print the details of his dog (ie. name and height) and call the methods bark and jump.    
davids_dog = Dog("Rex", 50)
print(davids_dog.dog_name)
print(davids_dog.dog_height)
davids_dog.bark()
davids_dog.jump()

# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
sarahs_dog = Dog("Teacup", 20)
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
print(sarahs_dog.dog_name)
print(sarahs_dog.dog_height)
sarahs_dog.bark()
sarahs_dog.jump()

# Create an if statement outside of the class to check which dog is bigger. Print the 
# name of the bigger dog.
if sarahs_dog.dog_height > davids_dog.dog_height:
    print(f'{sarahs_dog.dog_name} is bigger')
elif sarahs_dog.dog_height == davids_dog.dog_height:
    print("Dogs are the same.")
else:
    print(f'{davids_dog.dog_name} is bigger')
    

# 🌟 Exercise 3 : Who’s The Song Producer?
# Instructions
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# Create an object, for example:

# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])


# Then, call the sing_me_a_song method. The output should be:

# There’s a lady who's sure
# all that glitters is gold
# and she’s buying a stairway to heaven

class Song:
    def __init__(self, lyrics_text) :
        self.lyrics = lyrics_text
    
    def sing_me_a_song(self) :
        [print(item) for item in self.lyrics]
        # other option: print(*self.lyrics, sep = "\n")

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
# Instructions
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }


# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.
# Example
# Which animal should we add to the zoo --> Giraffe
# x.add_animal(Giraffe)

class Zoo:
    def __init__(self, zoo_name) :
        self.animals = []
        self.name = zoo_name 
        
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.   
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"Check animal name. The {new_animal} exist!")
            
# Create a method called get_animals that prints all the animals of the zoo.
    def get_animals(self) :
        print(*self.animals)
     
# Create a method called sell_animal that takes one parameter animal_sold.
# This method removes the animal from the list and of course the animal needs to exist in the list.   
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"The {animal_sold} not exist! Check animal name.")

# Create a method called sort_animals that sorts the animals alphabetically and groups 
# them together based on their first letter.  
    def sort_animals(self):
        self.animals.sort()
        self.group = {}
        num = 1
        first_letter = self.animals[0][0]
        
        for item in self.animals:
            if item[0] == first_letter:
                if num in self.group:
                    self.group[num].append(item)
                else:
                    self.group[num] = [item]
            else:
                num += 1   
                self.group[num] = [item]
                first_letter = item[0]
               
                       

# Create a method called get_groups that prints the animal/animals inside each group.
    def get_groups(self) :
        for key,value in self.group.items():
            print(f'In group {key} we have: {", ".join(item for item in value)}')
        

                

# Create an object called ramat_gan_safari and call all the methods
ramat_gan_safari = Zoo("New zoo")
print(ramat_gan_safari.name)
ramat_gan_safari.add_animal("hipo")
ramat_gan_safari.add_animal("harp")
ramat_gan_safari.add_animal("cat")
ramat_gan_safari.add_animal("dog")
ramat_gan_safari.add_animal("apple")
ramat_gan_safari.add_animal("zebra")
ramat_gan_safari.add_animal("dog")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("dog")
ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
