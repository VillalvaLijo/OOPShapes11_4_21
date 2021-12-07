#OOPshapes11_4_21.py

#Lord Alya Vijana

#simple program to take user input and create shapes using object oriented programing

from math import pi
from OOPShapes_Module import *


print("OOP Shapes\n created 11/4/21")
print("This program takes user input and creates shapes based off what parameters you enter.")

#length = input("Enter the length of a line: ")


#line_1 = Line(length) 

line_1 = Line()

#line_1 = Line.from_input()

line_1.print_length()

#circle_1 = Circle.from_input()

circle_1 = Circle()

#circle_1.calculate_properties()

circle_1.print_radius()

circle_1.print_diameter()

circle_1.print_circumference()

circle_1.print_area()

print("The Value of __name__ is: ", repr(__name__))

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
