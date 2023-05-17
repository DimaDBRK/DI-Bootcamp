# Week3 Day3
# Dmitry Dubrov
# Exercises XP
# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python 
# documentation online.

# 1. Write a program which prints the results of the following python built-in functions: 
# abs(), int(), input().
# 2. Using the __doc__ dunder method create your own documentation which explains the 
# execution of your code. Take a look at the doc method on google for help.


class Calc :
    '''Calc - it is class for explanation python built-in functions: abs(), int(), input()
    And it will help to test Doc'''
       
    # abs()
        # dunder method
    @staticmethod
    def abs_new(y:int) -> int :
        ''' abs - is built in functionn which return absolute value.
        Here we use __abs__()
        '''
        res = y.__abs__()
        return res
    
        # code
    def abs_new_1(y) :
        ''' abs - is built in functionn which return absolute value.
        Here we use if and *
        '''
        if y < 0: y = y * -1
        return y 

    # int()
      # dunder method or code
    def int_new(y) -> int :
        ''' int - is built in functionn which return int value (rounded).
        Here we use int() and return
        '''
        res = int(y)
        return res
    
    #input
    def input_new_sys(text = "") :
        ''' input - import sys method which allow to read symbols from comand line
        in loop until Enter. Return string.
        '''
        print(text)
        import sys #we import sus method which allow to read symbols from comand line
        for line in sys.stdin: #read symbols from comand 
            line = line.rstrip()
            break
        return line

    def input_new(text = ":"):
        ''' input - Return string after input.
        '''
        line = input()
        return line

# Driver
x = Calc
# abs()
print("abs()")
print("python built-in function:", abs(-5))
print("new method 1:",x.abs_new(-5))
print("new method 2:",x.abs_new_1(-5))

 # int()
print("# int()")
print("python built-in function:", int(3.3))
print("new method:",x.int_new(3.3))

# input()
s = input("python built-in input : ")
print(s)
print(x.input_new_sys("New input with sys :"))
print(x.input_new())

# 2. Using the __doc__ 
print(Calc.__doc__)
print(Calc.input_new_sys.__doc__)

# 🌟 Exercise 2: Currencies
# Instructions
# class Currency:
#     def __init__(self, currency, amount):
#         self.currency = currency
#         self.amount = amount
# 1. Using the code above, implement the relevant methods and dunder methods which will
# output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should 
# raise an error.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self) :
        print(f'{self.amount} {self.currency}s')
        return f'{self.amount} {self.currency}s'
    
    def __int__(self) :
        print (self.amount)
        return self.amount
    
    def __repr__(self) :
        print(f'{self.amount} {self.currency}s')
        return f'{self.amount} {self.currency}s'
    
    def __add__(self, second) :
        if type(second) == int :
            res = self.amount + second
            # print(f'{self.amount} {self.currency}')
            print(res)
            return res           
            # return repr(self) #f'{self.amount} {self.currency}'
        else  :
            if self.currency == second.currency :
                res = self.amount + second.amount
                print(res)
                return res     
            # return repr(self) #f'{self.amount} {self.currency}'
            else :
                # raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{second.currency}>")
                try : #update 17.05 after class explanation
                    raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{second.currency}>")
                except TypeError as error:
                    print(TypeError.__name__, error)
                
    # for +=
    def __iadd__(self, second) :
        if type(second) == int :
            self.amount += second
            print(f'{self.amount} {self.currency}')
            
        else :
           
            if self.currency == second.currency :
                print("+= c1 and c2, retuern self:")
                self.amount = self.amount + second.amount
                # print(f'{self.amount} {self.currency}')
                # return f'{self.amount} {self.currency}'   
            else :
                # raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{second.currency}>")   
                try : #update 17.05 after class explanation
                    raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{second.currency}>")
                except TypeError as error:
                    print(TypeError.__name__, error)
        
        return self
# Driver
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

# >>> str(c1) 
# # '5 dollars' -> __str__
str(c1)
# >>> int(c1)
# 5
int(c1)
# >>> repr(c1)
# '5 dollars'
repr(c1)

# >>> c1 + 5
# 10
c1 + 5

# >>> c1 + c2
# 15
c1 + c2

# >>> c1 
# 5 dollars
str(c1)

# >>> c1 += 5
# >>> c1
# 10 dollars
c1 += 5
str(c1)

# >>> c1 += c2
# >>> c1
# 20 dollars
c1 += c2
str(c1)

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
c1 + c3