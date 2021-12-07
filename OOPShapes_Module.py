#OOPShapes_Module.py

#12/6/21

#Lord Alya Vijana

from math import pi

class Line:

    def __init__(self, value):
        self.length=value

#    @classmethod
#    def from_input(cls):
#        while True:
#            length = float(input("Enter the length of the line: "))
#            if length:
#               return cls(length)

    def __init__(self):
        self.length = float(input("Enter the length of the line: "))


    def print_length(self):
        print(f"Length of Line: {self.length}")

class Circle(Line):

    #raidus = 0
    #diameter = 0

    def __init__(self):
        self.radius = float(input("Enter the length of the radius: "))
        self.diameter = self.radius*2
        self.area = (self.radius)*pi
        self.circumference = 2*self.radius*pi


    #diameter = radius*2

#    def calculate_properties(self):
#        self.diameter = self.radius *2
#        self.area = (self.radius**2)*pi
#        self.circumference = 2*self.radius*pi

    def print_radius(self):
        print(f"Radius of the circle: {self.radius}")

    def print_diameter(self):
        #diameter = 2*self.radius
        print(f"The Diameter of the Circle is: {self.diameter}")

    def print_circumference(self):
        print(f"Circumference of the circle: {self.circumference}")

    def print_area(self):
        print(f"The Area of the Circle: {self.area}")

class Sphere(Circle):
    
    def __init__(self, radius):
        self.radius = radius

    def print_radius(self):
        print(f"Radius of the Sphere: {self.radius}")

