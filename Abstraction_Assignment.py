
from abc import ABC, abstractmethod

# Define the parent class with an abstract method
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    def display_area(self):
        print("Area:", self.area())

# Define the first child class that implements the abstract method
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Define the second child class that implements the abstract method
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Create objects of the child classes and display their areas
rect = Rectangle(5, 10)
rect.display_area()
print()
circle = Circle(7)
circle.display_area()
