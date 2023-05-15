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


# 1. Create a new python file and import your Dog class from the previous exercise.
from main import Dog
import random

# 2. In the new python file, create a class named PetDog that inherits from Dog.

class PetDog(Dog) :
# 3. Add an attribute called trained to the __init__ method, this attribute is a boolean 
# and the value should be False by default.
    def __init__(self, in_name, in_age, in_weight, in_trained = False):
        super().__init__(in_name, in_age, in_weight)
        self.trained = in_trained
    
# 4. Add the following methods:
    # train: prints the output of bark and switches the trained boolean to True

    def train(self):
        self.bark
        self.trained = True
    # play: takes a parameter which value is a few names of other Dog instances 
    # (use *args). The method should print the following string: 
    # “dog_names all play together”.
    def play(self, *other_names):
        print(other_names)
        print(f'{self.name}, {" , ".join(other_names)} all play together')
        
    # do_a_trick: If the dog is trained the method should print one of the following 
    # sentences at random:
        # “dog_name does a barrel roll”.
        # “dog_name stands on his back legs”.
        # “dog_name shakes your hand”.
        # “dog_name plays dead”.
    def do_a_trick(self):
        trick_list = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
        if self.trained:
            res = f'{self.name} {random.choice(trick_list)}'
        else: 
            res = f'{self.name} not traind'
        print(res)
# # Tests
dog_11 = PetDog("Black2",5, 10)
dog_12 = PetDog("White2",4, 15)
dog_13 = PetDog("Brown2",5, 10)

dog_11.train()
print(dog_11.trained)
print(dog_12.trained)
dog_11.play("White", "Green") 
dog_11.do_a_trick()   
dog_11.do_a_trick()
dog_11.do_a_trick()    
dog_12.do_a_trick()   