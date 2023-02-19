# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger 
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them


from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @property
    def area(self):
        return pi * self.radius ** 2
    
    def __str__(self):
        return f"Circle with radius {self.radius}"
    
    def __repr__(self):
        return f"Circle({self.radius})"
    
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    
    def __lt__(self, other):
        return self.radius < other.radius
    
    def __eq__(self, other):
        return self.radius == other.radius
    
    def __gt__(self, other):
        return self.radius > other.radius

c1 = Circle(5)
c2 = Circle(10)


print(c1.radius)    
print(c2.diameter)  
print(c1.area)      


print(c1)           


c3 = c1 + c2
print(c3.radius)   


print(c1 == c2)     



circles = [Circle(5), Circle(2), Circle(10)]
sorted_circles = sorted(circles)
print(sorted_circles)
