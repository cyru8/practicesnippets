#! /usr/bin/env python
"""
Snippet03 is a game
"""

__author__ = "O.A"
__author_email__ = "oa@live.com"

#This is a python dictionary
author = {"name": "Banjo", "color": "green", "shape": "circle"}

#This python List
colors = ["blue", "green", "red"]

#This is a List of Dictionary
favourite_colors = [
        {
            "student": "Feranmi",
            "color": "red"
            },
        {
            "student": "Ire",
            "color": "blue"
            }
        ]

# Program Entry 
if __name__ == '__main__':
    print("The author's name is {}.".format(author["name"]))
    print("His favourite color is {}.".format(author["color"]))
    print("His favourite shape is {}.".format(author["shape"]))
    print("")

    print("The current colors are: ")
    for color in colors:
        print(color)
    print("")

    #Ask user for favourite color and compare to author's color
    new_color = input("What is your favourite color? ")
    if new_color == author["color"]:
        print("You have the same favourite as {}.".format(author["name"]))
        print("")
