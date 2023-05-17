# Main task is done in time (I hope). I will try to use for draw later, 
# it is not mandtory as I understend.
# Thank you!

#Week3 Day3 
#Dmityr Dubrov
#Daily Challenge - Circle

# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# + Compute the circle’s area
# Print the circle and get something nice
# + Be able to add two circles together
# + Be able to compare two circles to see which is bigger
# + Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them

class Circle:
    # A Circle can be defined by either specifying the radius or the diameter.   
    def __init__(self, radius=0, diameter=0):
        self.radius = float(radius)
        self.diameter = float(diameter)
        
        
    @classmethod
    def from_radius(cls, radius):
        '''Calculate the diameter getting the radius as arg'''
        return cls(radius = radius, diameter = radius*2)
    
    @classmethod
    def from_diameter(cls, diameter):
        '''Calculate the radius getting the diameter as arg'''
        return cls(diameter = diameter, radius = diameter/2)
    
    # Compute the circle’s area
    def get_area(self) -> float:
        '''Calculate the area'''
        return 3.14 * self.radius ** 2
    
    # + Be able to add two circles together
    def __add__(self, other_circle) -> float:
        '''Adds two circle areas'''
        return self.get_area() + other_circle.get_area()
    
    # Be able to compare two circles to see which is bigger
    def __gt__(self, other_circle):
        '''compare two circles to see which is bigger'''
        return ((self.get_area()) > (other_circle.get_area())) 
    
    def __lt__(self, other_circle):
        '''compare two circles to see which is bigger'''
        return ((self.get_area()) < (other_circle.get_area()))   
        
    def __ge__(self, other_circle):
        '''compare two circles to see which is bigger or eq'''
        return ((self.get_area()) >= (other_circle.get_area())) 
    
    def __le__(self, other_circle):
        '''compare two circles to see which is bigger or eq'''
        return ((self.get_area()) <= (other_circle.get_area()))  
    
    # Be able to compare two circles and see if there are equal
    def __eq__(self, other_circle) -> float:
        '''compare two circles to see if there are equal'''
        return ((self.get_area()) == (other_circle.get_area())) 
    
    def __ne__(self, other_circle) -> float:
        '''compare two circles to see if there are not equal'''
        return ((self.get_area()) != (other_circle.get_area())) 
    
    
    # Print the circle and get something nice
    def __str__(self) :
        '''str for print'''
        res = f'This is Circle with radius {self.radius}, diametr {self.diameter} and square {self.get_area()}'
        return res
    # Be able to put them in a list and sort them
    def __repr__(self):
        return str(((self.__name__), self.diameter))
    
    
circleA = Circle.from_diameter(diameter = 4)
circleB = Circle.from_radius(radius = 4)
circleC = Circle(3,6)
circleA.get_area()

print("CircleA radius : ", circleA.radius, "CircleA diameter: ", circleA.diameter)
print("CircleB radius : ", circleB.radius, "CircleB diameter: ", circleB.diameter)
print("CircleC radius : ", circleC.radius, "CircleC diameter: ", circleC.diameter)
print("circleA.get_area : ", circleA.get_area())
print("circleB.get_area : ", circleB.get_area())
print('add A and B: ', round(circleA + circleB, 2)) # adding Circles and rouding the float

print(circleA > circleB)
print(circleA < circleB)
print(circleA == circleB)
print(circleA != circleB)
print(circleA)

circle_list= [circleA, circleB, circleC ]
print(circle_list)

# sorting objects on the basis of value 
# after sorting (by square)
print(sorted(circle_list))