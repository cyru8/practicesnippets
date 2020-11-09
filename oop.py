# What is OOP - Code-reuse, seperation of code, code legibility, modeling data.
# Defining and instantiating classes
# Member properties
# Menber Methods
# Constructor
# Data Types: x = "Ben" (string data type), custom data type e.g: class
import math
import random


class Circle:
    def calcCircumfrence(self):
        return math.pi * 2 * self.radius

    def calcDiameter(self):
        return math.pi * 2

    def calcArea(self):
        return math.pi * (self.radius ** 2)

# circle1 = Circle()
# circle1.radius = 4.2
# print(circle1.radius)

# circle2 = Circle()
# circle2.radius = 3.9
# print(circle2.radius)


circles = []
for i in range(0, 10):
    c = Circle()
    c.radius = random.uniform(1.1, 9.5)
    circles.append(c)
for c in circles:
    print("Radius:", c.radius, "circumfrence:", c.calcCircumfrence(),
          "Diameter:", c.calcDiameter(), "Area:", c.calcArea())
