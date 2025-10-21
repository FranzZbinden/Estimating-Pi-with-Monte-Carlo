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


def aproximation(points_amount):
    outside_circle = 0
    inside_circle = 0

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


for count in range (1,100000,100):
    pi = aproximation(count)
    print("Using", count, " points, the pi aproximation is", pi)
