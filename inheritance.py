# basic inheritance
# method overloading
# inherintance hierachies
import math


class Shape():
    def __init__(self):
        self.color = "Red"
        self.sides = 0


class Square(Shape):
    def __init__(self, w):
        Shape.__init__(self)
        self.width = w


sq1 = Square(5)
sq2 = Square(9)

print("Square Sizes:", sq1.width, "x", sq1.sides,
      sq1.color, ",", sq2.width, "x", sq2.sides, sq2.color)
