# Week3 Day5
# Dmityr Dubrov
# Daily Challenge: OOP Quizz

# Part 1 : Quizz :
# Answer the following questions

# What is a class?
    #Class is the most basic entity of Python because it acts as the core 
    # of object-oriented programming. Because of this, users can create
    # and use classes and instances that are downright simple and easy.
    # Everything that a user sees in Python is an object, such as integers, 
    # functions, dictionaries, lists, and many other entities. 
    # It is a subpart of a class. Every Python object has a type, 
    # and users can create the object types using classes.
    
# What is an instance?
    #Instances are objects of a class in Python. In other words, users can 
    # define an instance of a particular class as an individual object.
    # Users can define the Instance methods inside a Python class, similar 
    # to how they define a regular function.
    # First, users use the "def" keyword to define an instance method.
    # Secondly, while defining the instance methods, users use the "self" as the first parameter within the instance method. The self parameter directs to the existing object.
    # Lastly, users can use the self parameter to access or change the existing attributes of the Python object.
    
# What is encapsulation?
    #In object-oriented programming (OOP), encapsulation refers to the bundling of data with the methods that operate on that data, or the restricting of direct access to some of an object's components. Encapsulation is used to hide the values or state of a structured data object inside a class, preventing direct access to them by clients in a way that could expose hidden implementation details or violate state invariance maintained by the methods.
    
# What is abstraction?
    #Abstraction is one of the key concepts of object-oriented programming 
    # (OOP) languages. Its main goal is to handle complexity by hiding 
    # unnecessary details from the user. That enables the user to implement 
    # more complex logic on top of the provided abstraction without 
    # understanding or even thinking about all the hidden complexity.
    # Objects in an OOP language provide an abstraction that hides the 
    # internal implementation details. Similar to the coffee machine in 
    # your kitchen, you just need to know which methods of the object are
    # available to call and which input parameters are needed to trigger 
    # a specific operation. But you don’t need to understand how this 
    # method is implemented and which kinds of actions it has to perform 
    # to create the expected result.
    
# What is inheritance?
    #In object-oriented programming (OOP), inheritance describes a 
    # relationship between two classes in which one class (the child class) 
    # subclasses the parent class. The child inherits methods and attributes
    # of the parent, allowing for shared functionality. For example,
    # one might create a variable class Mammal with features such as eating, 
    # reproducing, etc.; then define a child class Cat that inherits those 
    # features without having to explicitly program them, while adding new 
    # features like chasing mice.
    
# What is multiple inheritance?
    #Multiple inheritance is a feature of some object-oriented computer 
    # programming languages in which an object or class can inherit features 
    # from more than one parent object or parent class. 
    # 
    
# What is polymorphism?
    #Polymorphism is one of the core concepts of object-oriented programming
    # (OOP) and describes situations in which something occurs in several 
    # different forms. In computer science, it describes the concept that 
    # you can access objects of different types through the same interface.
    # Each type can provide its own independent implementation of this 
    # interface.
    
# What is method resolution order or MRO?
    # MRO is a concept used in inheritance. It is the order in which a method is searched for in a classes hierarchy and is especially useful in Python because Python supports multiple inheritance.
    # In Python, the MRO is from bottom to top and left to right. This means that,
    # first, the method is searched in the class of the object. If it’s not found,
    # it is searched in the immediate super class. In the case of multiple super
    # classes, it is searched left to right, in the order by which was declared 
    # by the developer.
    


# Part 2: Create A Deck Of Cards Class.
# The Deck of cards class should NOT inherit from a Card class.
# The requirements are as follows:
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.

import random

class Card :
    def __init__(self):
        self.suit = ('Spade','Heart','Diamond','Club')
        self.value = ('A',2,3,4,5,6,7,8,9,10,'J','Q','K')

class Deck:
    def __init__(self):
        self.cards = []
    
    def make_deck(self, card):
        for item in card.suit:
            for value in card.value:
               self.cards.append(f'{item}-{value}')
    
    def shuffle(self) :
        if len(self.cards)  == 52:  
            for i in range(len(self.cards)-1,0,-1):
                r = random.randint(0, i)
                self.cards[i],self.cards[r] = self.cards[r],self.cards[i]     
        else:
            print(f"Deck of cards doesn't have all 52 cards")
   
    def deal(self):
        res = "No card left."
        if len(self.cards) > 0:
            res = self.cards.pop()
        else:
            print ("Deck is empty. No card left")
        return res
      
card_item = Card()
deck = Deck()
deck.make_deck(card_item)
print(len(deck.cards))
deck.shuffle()
print(deck.deal())
print(len(deck.cards))