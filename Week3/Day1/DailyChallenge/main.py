# Week3 Day1
# Dmitry Dubrov
# Daily Challenge: Old MacDonald’s Farm
# Instructions : Old MacDonald’s Farm
# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())

# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!
# Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?
# Do you notice anything interesting about the way we are calling the add_animal method? 
# What parameters should this function have? How many…?
# Test your code and make sure you get the same results as the example above.
# Bonus: nicely line the text in columns as seen in the example above. Use string formatting.
# Expand The Farm
# Add a method called get_animal_types to the Farm class. This method should return a sorted list of all the animal types (names) in the farm. With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info. This method should return the following string: “McDonald’s farm has cows, goats and sheep.”. The method should call the get_animal_types function to get a list of the animals.

# Create a class called Farm
class Farm:
    def __init__(self, farm_name) :
        self.animals = []
        self.name = farm_name 
        print(f'{self.name} `s farm \n')
        
    def add_animal(self, new_animal, qty = 1) :
        res = True
        for i in range(len(self.animals)) :
            if new_animal == self.animals[i][0]:
                self.animals[i][1] += qty
                res = False
                
        if res:
                self.animals.append([new_animal, qty])


    def get_info(self) :
        output_str = ''
        for item in self.animals:
            output_str += (f'{(item[0])} : {item[1]} \n')
        output_str += '\n      E-I-E-I-0!'
        
        return output_str
# Add a method called get_animal_types to the Farm class. 
# This method should return a sorted list of all the animal types (names) in the farm. 
# With the example above, the list should be: ['cow', 'goat', 'sheep'].

   
    def get_animal_types(self) :
        
        short_list = [i[0] for i in self.animals]
        short_list.sort()
        return short_list
        
   
# Add another method to the Farm class called get_short_info. 
# This method should return the following string: 
# “McDonald’s farm has cows, goats and sheep.”. 
# The method should call the get_animal_types function to get a list of the animals.
    def get_short_info(self) :
        
        # out_str = (f'[{self.get_animal_types()[i]}']) for i in self.animals
    
        update_list = macdonald.get_animal_types()
        
        # 15.05 after review in class I should add "s" symbols to animals with
        # q-ty more one and add "and" before last one animal:
        for item in range(len(update_list)):
            for i in range(len(self.animals)) :
                if update_list[item] == self.animals[i][0] and self.animals[i][1] > 1:
                    update_list[item] += "s"
                
        out_str = f'{macdonald.name}`s farm has: {", ".join(item for item in update_list[0:-1])} and {update_list[-1]} .'
        return out_str
    
# Main
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)

macdonald.add_animal('sheep')

macdonald.add_animal('sheep')

macdonald.add_animal('goat', 12)

print(macdonald.get_info())

print(macdonald.get_animal_types())
print(macdonald.get_short_info())
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!