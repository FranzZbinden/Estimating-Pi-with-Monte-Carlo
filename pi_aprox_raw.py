"""

This program estimates the value of PI using the Monte Carlo method. 
It generates random points within a square that bounds a unit circle 
and calculates the ratio of points that fall inside the circle to 
the total number of points generated. The estimated value of π is 
then calculated based on this ratio.

Author: Franz Zbinden García
Date: 1/3/2025
Version: 1.0

Usage:
Run the program to see the approximation of π using different 
amounts of random points, iterating from 1 to 100,000 in steps of 100.

"""

import random, math

# Generate random floats betwen -1 and 1
def calc_random(): 
    return random.uniform(-1.0,1.0) 

# Calculate distance betwen the center and the given point
def distance_calc(x,y):
    return math.sqrt(x**2 + y**2)

# Define if an individual point is inside or outside the circle using a radio of 1 
def inside_oitside(distance):
    if distance <= 1: 
        return True
    else:
        return False

# Main Function
def aproximation(points_amount):

    # Counter of points inside/outside of circle
    outside_circle = 0
    inside_circle = 0

    # Loop 
    for _ in range(points_amount):
        x = calc_random()
        y = calc_random()   
        distance = distance_calc(x,y)
        where = inside_oitside(distance)

        if where == True:
            inside_circle = inside_circle + 1
        else:
            outside_circle = outside_circle + 1


    pi = 4 * (inside_circle / points_amount) 
    return pi

# Entry point of program that iterates aproximation with different points amount (1-5000)
for count in range (1,100000,100):
    pi = aproximation(count)
    print("Using", count, " points, the pi aproximation is", pi)
