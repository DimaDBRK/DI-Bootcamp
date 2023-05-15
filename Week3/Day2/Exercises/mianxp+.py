# Week3 Day2
# Dmitry Dubrov
# Exercises XP+

# Exercise 1 : Family
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# last_name : (string)
# Initial members data:

# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]


# 2. Implement the following methods: 
# * born: adds a child to the members list (use **kwargs),# don’t forget to print a message congratulating the family. 
# * is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not. 
# * family_presentation: a method that prints the family’s last name and all the members’ first name.


class Family():
    def __init__(self, ls_name):
        self.memebers = [
                        {'name':'Michael','age':35,'gender':'Male','is_child':False},
                        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
                        ]
        self.last_name = ls_name

# 2. Implement the following methods: 
# * born: adds a child to the members list (use **kwargs),
    def born(self, **kwargs) : #in_name, in_age, in_gender
        new_member = {}
       
        if type(kwargs["name"]) == str and kwargs["age"] < 18:
            for key, value in kwargs.items():
                new_member[key] = value
            new_member["is_child"] = True 
            self.memebers.append(new_member)
            print(f'Congratulating the family {self.last_name} with new memeber {(self.memebers[-1]).get("name")}')
        else:
            print("Wrong data or type. Try again.")
        
    # * is_18: takes the name of a family member as a parameter and returns True if 
    # they are over 18 and False if not. 
    
    def is_18(self, in_name) : #in_name, in_age, in_gender
        res = False
        qlty = 0
        for item in self.memebers:
            # print(item.get("name") == in_name)
          
            if item.get("name") == in_name:
                 res = item.get("age") > 18
                 qlty = 1
           
        if qlty == 0:  print("Wrong name")        
           
        return res
    # * family_presentation: a method that prints the family’s last name and all 
    # the members’ first name.      
    def family_presentation(self) : 
        name_list = []
        for item in self.memebers:
             name_list.append(item.get("name"))
          
        print(f'Family {self.last_name} include: {(", ").join(name_list)} .')       
        
    
fam_1 = Family("Smith")
print(fam_1.memebers[1])
fam_1.born(name = "Bob",age = 1, gender = "Male")
fam_1.born(name = "Jun",age = 1)
fam_1.born(name = "Jun",age = 1, gender = "Famel")

print(fam_1.memebers)
print(fam_1.is_18("Michael"))
fam_1.family_presentation()

# Exercise 2 : TheIncredibles Family
# Instructions
# 1. Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
# Initial members data:
# [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
# ]
# 2. Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
# 3. Add a method called incredible_presentation which : * prints the family’s last name and all the members’ first name (ie. use the super() function, to call the family_presentation method) * prints all the members’ incredible name and power.
# 4. Call the incredible_presentation method.
# 5. Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
# 6. Call the incredible_presentation method again.

print("Exercise 2 : TheIncredibles Family")
class TheIncredibles(Family) :
    def __init__(self, ls_name) :
        super().__init__(ls_name)
        self.memebers = [
    {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
        ]
# 2. Add a method called use_power, this method should print the power of a member only if
# they are over 18 years old. If not raise an exception (look up exceptions) which stated 
# they are not over 18 years old.
    def use_power(self, in_name, expection = "No") :
        if self.is_18(in_name) or expection == "Yes" :
            for item in self.memebers:
                if item.get("name") == in_name:
                   print(f'{in_name} power is {item.get("power")}')
                
        else:
            print("Not over 18 years old.")
            
# 3. Add a method called incredible_presentation which : 
# * prints the family’s last name and all the members’ first name 
# (ie. use the super() function, to call  the family_presentation method)
# * prints all the members’ incredible name and power.
    def incredible_presentation(self) : 
        self.family_presentation()
        print("incredible_presentation:")
        incredible_list = []
        for item in self.memebers:
            incredible_list.append(f'{item.get("name")} as {item.get("incredible_name")} - power is {item.get("power")}')
          
        print(f'Family {self.last_name} include: {(", ").join(incredible_list)}.')   

#Drivers
fam_s_2 = TheIncredibles("HuanHu")
print(fam_s_2.last_name)
fam_s_2.use_power("Sarah","Yes")
# 4. Call the incredible_presentation method.
fam_s_2.incredible_presentation()

# 5. Use the born method inherited from the Family class 
# to add Baby Jack with the following power: “Unknown Power”.
fam_s_2.born(name ="Jack", age = 8, gender ="Male", incredible_name = "Baby Jack", power = "Unknown Power")
# 6. Call the incredible_presentation method again.
fam_s_2.incredible_presentation()