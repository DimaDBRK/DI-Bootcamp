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
                try :
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
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{second.currency}>")   
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