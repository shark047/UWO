"""
CS1026 - Assignment 1 - Shapes and Sizes
Code by: Yiwei Dong
Student ID: ydong445
File created: Sep.25, 2024

This file calculate the perimeter and area for different shapes.
"""


import math

shape = input("Enter a 2D shape: ")

if shape.lower() == "rectangle": #make inputs to lowercase for comparison

    h = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    #get the width and length of rectangle from user

    if h <= 0 or w <= 0:
    #if number is zero or a negative value, print "Invalid value entered"

        print("Invalid value entered")
        # check value

    else:

        perimeter = (2 * w) + (2 * h)
        area = w * h
        #calculate the perimeter and area of rectangle

        print("Shape: {}".format(shape))
        print("Perimeter: {}".format(round(perimeter, 2))) #rounded to 2 decimal places
        print("Area: {}".format(round(area, 2)))
        #output shape, perimeter, area

elif shape.lower() == "triangle":

    b = float(input("Enter the base length of the triangle: "))
    a = float(input("Enter the 2nd length of the triangle: "))
    c = float(input("Enter the 3rd length of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    #get the base, 2nd, 3rd length of the triangle

    if b <= 0 or a <= 0 or c <= 0 or h <= 0:

        print("Invalid value entered")
        # check value

    else:

        perimeter = a + b + c
        area = (b * h) / 2
        #calculate the perimeter and area of triangle

        print("Shape: {}".format(shape))
        print("Perimeter: {}".format(round(perimeter, 2)))
        print("Area: {}".format(round(area, 2)))
        #output shape, perimeter, area

elif shape.lower() == "circle":

    r = float(input("Enter the radius of the circle: "))
    #get the radius of the circle from user

    if r <= 0:

        print("Invalid value entered")
        # check value

    else:

        perimeter = 2 * r * math.pi
        area = (r ** 2) * math.pi
        # calculate the perimeter and area of circle

        print("Shape: {}".format(shape))
        print("Perimeter: {}".format(round(perimeter, 2)))
        print("Area: {}".format(round(area, 2)))
        #output shape, perimeter, area

elif shape.lower() == "trapezoid":

    t = float(input("Enter the top of the Trapezoid: "))
    b = float(input("Enter the bottom of the Trapezoid: "))
    l = float(input("Enter the left side of the Trapezoid: "))
    r = float(input("Enter the right side of the Trapezoid: "))
    h = float(input("Enter the height of the Trapezoid: "))
    #get the top, bottom, left, right, height length of trapezoid from user

    if t <= 0 or b <= 0 or l <= 0 or r <= 0 or h <= 0:

        print("Invalid value entered")
        # check value

    else:

        perimeter = t + r + b + l
        area = ((t + b) / 2) * h
        # calculate the perimeter and area of trapezoid

        print("Shape: {}".format(shape))
        print("Perimeter: {}".format(round(perimeter, 2)))
        print("Area: {}".format(round(area, 2)))
        #output shape, perimeter, area

elif shape.lower() == "hexagon":

    s = float(input("Enter the side length of the hexagon: "))
    # get the side length of the hexagon from user

    if s <= 0:

        print("Invalid value entered")
        #check value

    else:

        perimeter = 6 * s
        area = 3 * math.sqrt(3) / 2 * (s ** 2)
        # calculate the perimeter and area of hexagon

        print("Shape: {}".format(shape))
        print("Perimeter: {}".format(round(perimeter, 2)))
        print("Area: {}".format(round(area, 2)))
        # output shape, perimeter, area

else:
    print("Invalid shape entered")
    #check shape
