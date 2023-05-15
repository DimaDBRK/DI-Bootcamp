# Week3 Day2
# Dmitry Dubrov
# Exercises XP

# 🌟 Exercise 1 : Pets
# 1. Create another cat breed named Siamese which inherits from the Cat class.
# 2. Create a list called all_cats, which holds three cat instances : one Bengal, 
# one Chartreux and one Siamese.
# 3. Those three cats are Sara’s pets. Create a variable called sara_pets which value 
# is an instance of the Pet class, and pass the variable all_cats to the new instance.
# 4. Take all the cats for a walk, use the walk method.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
# 1. Create another cat breed named Siamese which inherits from the Cat class.

class Siamese(Cat) :
    def sing(self, sounds):
        return f'{sounds}'

# 2. Create a list called all_cats, which holds three cat instances 
# : one Bengal, one Chartreux and one Siamese.

all_cats = [Bengal("TomS",5), Chartreux("WhiteC",4),Siamese("BrownS",5)]

# 3. Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the 
# Pet class, and pass the variable all_cats to the new instance.

sara_pets = Pets(all_cats) 

# 4. Take all the cats for a walk, use the walk method.
sara_pets.walk()

# 🌟 Exercise 2 : Dogs
# Instructions
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. 
# This method returns a string stating which dog won the fight. 
# The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.

# 1. Create a class called Dog with the following attributes name, age, weight.

class Dog() :
    def __init__(self, in_name, in_age, in_weight):
        self.name = in_name
        self.age = in_age
        self.weight = in_weight

# 2. Implement the following methods in the Dog class:
    # bark: returns a string which states: “<dog_name> is barking”.
    def bark(self) :
        res = f'{self.name} is barking'
        return res
    
    # run_speed: returns the dogs running speed (weight/age*10).
    def run_speed(self) :
        res = self.weight/ self.age * 10
        return res
    
    
    # fight : takes a parameter which value is another Dog instance, called other_dog. 
    # This method returns a string stating which dog won the fight. 
    # The winner should be the dog with the higher run_speed x weight.
    def fight(self, other_dog) :
        res = f'{self.name} won the fight'
        if (self.run_speed() * self.weight) < (other_dog.run_speed() * other_dog.weight):
            res = f'{other_dog.name} won the fight'
        elif (self.run_speed() * self.weight) == (other_dog.run_speed() * other_dog.weight):
            res = f'{other_dog.name} and {self.name} standoff'
        return res

# Create 3 dogs and run them through your class.   
dog_1 = Dog("Black",5, 10)
dog_2 = Dog("White",4, 15)
dog_3 = Dog("Brown",5, 10)
print(dog_1.bark())
print(dog_1.run_speed())
print(dog_1.fight(dog_2))
print(dog_1.fight(dog_3))

# 🌟 Exercise 3 : Dogs Domesticated
# Instructions
# Create a new python file and import your Dog class from the previous exercise.
# In the new python file, create a class named PetDog that inherits from Dog.
# Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# Add the following methods:
# train: prints the output of bark and switches the trained boolean to True

# play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.

# do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# “dog_name does a barrel roll”.
# “dog_name stands on his back legs”.
# “dog_name shakes your hand”.
# “dog_name plays dead”.

#They ask to Create a new python file. Please check new file Main_xp3