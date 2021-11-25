#OOPshapes11_4_21.py

#Lord Alya Vijana

#simple program to take user input and create shapes using object oriented programing

from math import pi

print("OOP Shapes\n created 11/4/21")
print("This program takes user input and creates shapes based off what parameters you enter.")

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

    #diameter = radius*2

    def calculate_properties(self):
        self.diameter = self.radius *2
        self.area = (self.radius**2)*pi
        self.circumference = 2*self.radius*pi

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

#length = input("Enter the length of a line: ")


#line_1 = Line(length) 

line_1 = Line()

#line_1 = Line.from_input()

line_1.print_length()

#circle_1 = Circle.from_input()

circle_1 = Circle()

circle_1.calculate_properties()

circle_1.print_radius()

circle_1.print_diameter()

circle_1.print_circumference()

circle_1.print_area()

#circle_1 = Circle

#circle_1.print_radius()

#circle_1.print_diameter()

#sphere_1 = Sphere.from_input()

#sphere_1.print_radius()

#print("Line.__name__ : ",Line.__name__)

#print("Line.__bases__: ",Line.__bases__)

#print("line_1.__class__: ",line_1.__class__)

#print("Line.__dict__: ", Line.__dict__)

#print("line_1.__dict__: ", line_1.__dict__)

#print("type(line_1): ", type(line_1))

#print("type(Line): ", type(Line))

#print("Line.print_length: ",Line.print_length)

#print("line_1.print_length: ", line_1.print_length)

#print("line_1.im_class: ", line_1.im_class)

#print("line_1.im_func: ", line_1.im_func)


#print("line_1.im_self: ", line_1.im_self)
