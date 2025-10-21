import random

def calc_random():
    return random.uniform(-1.0, 1.0) # Generate a random float between -1 and 1 

def inside_circle(distance, inside_circle):
    if distance <= 1:   # Dot is inside the circle
        inside_circle += 1  
        return "green", inside_circle # Asign the color green to the point
    else:
        return "red", inside_circle # Asign the color red to the point