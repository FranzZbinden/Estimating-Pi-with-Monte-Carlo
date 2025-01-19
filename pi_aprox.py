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

import tkinter as tk
import random
import math
import time

theme_mode = "white"   # Variable to store theme state

def toggle_dark_mode():
    global theme_mode

    if theme_mode == "white":
        # Switch to dark mode
        root.config(bg="grey15")
        main_frame.config(bg="grey15")
        canvas_frame.config(bg="grey15")
        canvas.config(bg="grey15")
        control_frame.config(bg="grey15", bd=0)
        
        label_result.config(bg="grey15", fg="white")
        label_inside.config(bg="grey15", fg="white")
        label_outside.config(bg="grey15", fg="white")
        label_timer.config(bg="grey15", fg="white")
        
        scale.config(bg="grey15", fg="white", troughcolor="gray20")
        button.config(bg="grey15", fg="white")
        dark_button.config(bg="gray30", fg="white", text="Light Mode")
        
        theme_mode = "dark"  # Switch theme to "dark"
    else:
        # Switch to dight mode
        root.config(bg="SystemButtonFace")       # SystemButtonFace = default color of windows
        main_frame.config(bg="SystemButtonFace")
        canvas_frame.config(bg="SystemButtonFace")
        canvas.config(bg="SystemButtonFace")
        control_frame.config(bg="SystemButtonFace", bd=0)
        
        label_result.config(bg="SystemButtonFace", fg="grey30")
        label_inside.config(bg="SystemButtonFace", fg="grey30")
        label_outside.config(bg="SystemButtonFace", fg="grey30")
        label_timer.config(bg="SystemButtonFace", fg="grey30")
        
        scale.config(bg="SystemButtonFace", fg="grey30", troughcolor="white")
        button.config(bg="SystemButtonFace", fg="grey30")
        dark_button.config(bg="SystemButtonFace", fg="grey30", text="Dark Mode")
        
        theme_mode = "white"  # Switch theme to "white"


def calc_random():
    return random.uniform(-1.0, 1.0) # Generate a random float between -1 and 1 

def run_simulation():
    start_time = time.perf_counter()    # Record the start time of the simulation

    canvas.delete("all")  # Clear the canvas when starting new simulation
    
    points_amount = int(scale.get())
    
    # Drawing the circle
    canvas.create_oval(1.5, 1.5, CANVAS_SIZE, CANVAS_SIZE, width=2, outline= "red")

        
    inside_circle = 0   
    
    for _ in range(points_amount):
        x = calc_random()
        y = calc_random()
        distance = math.sqrt(x**2 + y**2)   # Distance formula optimized 
        
        if distance <= 1:   # Determines if the dot is inside the circle
            inside_circle += 1  #increment the counter if the dot is inside the circle
            color = "green" # Asign the color green to the points inside the circle radius
        else:
            color = "red" # Asign the color red to the points outsaide the circle radius
        
        # Convert [-1,1] to [0, CANVAS_SIZE] for the Canvas ilustration
        px = (x + 1) * (CANVAS_SIZE / 2)
        py = (1 - y) * (CANVAS_SIZE / 2)
        
        # For drawing a dot
        radius = 1
        canvas.create_oval(px - radius, py - radius, px + radius, py + radius, 
                           fill=color, outline=color)
        
        # Timer to calculate the time
        end_time = time.perf_counter()  # Record the end time of the simulation
        elapsed = end_time - start_time # Calculate the elapsed time
        label_timer.config(text=f"Calculation time: {elapsed:.4f} seconds")
        
    pi_approx = 4 * (inside_circle / points_amount) # Monte Carlo formula

    # Updates the widgets
    label_result.config(text=f"Pi approximation: {pi_approx:.6f}")  
    label_inside.config(text=f"Dots inside the circle: {inside_circle:}")
    label_outside.config(text=f"Dots outside the circle: {points_amount-inside_circle:}")

# Graphical User Interface
root = tk.Tk()  # Initializes the main window

root.title("Monte Carlo π Visualization")   

CANVAS_SIZE = 600   # Size of the canvas

# Spacing around the window
main_frame = tk.Frame(root, padx=10, pady=10)
main_frame.pack()

# Create a row (frame) for the scale and button side by side
control_frame = tk.Frame(main_frame)
control_frame.pack(pady=5)  # spacing around the row

# Scale (slider) to choose the number of points
scale = tk.Scale(
    control_frame,
    from_=50, to=10000,
    orient=tk.HORIZONTAL,
    length=200,
    font=10
)
scale.set(50)  # Default initial value
scale.pack(side=tk.LEFT, padx=5)
scale.config(highlightthickness=0, troughcolor="gray20")

# Button to run the simulation
button = tk.Button(control_frame, text="Run Simulation", font = 15, command=run_simulation,
width=13, height=1)

button.pack(side=tk.LEFT, padx=5)

label_timer = tk.Label(main_frame, text="Calculation time:", font=("TkDefaultFont", 12))
label_timer.pack(pady=2)

# Frame only for the canvas, with a visible border
canvas_frame = tk.Frame(main_frame, bd=2, relief="groove", bg="black")
canvas_frame.pack(pady=5)

# Canvas inside the bordered frame
canvas = tk.Canvas(canvas_frame, width=CANVAS_SIZE, height=CANVAS_SIZE, highlightthickness=0)
canvas.pack()

# Creates the circle on the canvas when starting the app
canvas.create_oval(1.5, 1.5, CANVAS_SIZE, CANVAS_SIZE, width=2, outline= "red")

# Label to display the Pi approximation
label_result = tk.Label(main_frame, text="Pi approximation:", font=("TkDefaultFont", 14))
label_result.pack(pady=4)

# Label to display the dots inside circle
label_inside = tk.Label(main_frame, text="Dots inside the circle:", font=("TkDefaultFont", 12))
label_inside.pack(pady=1)

# Label to display the dots outside circle
label_outside = tk.Label(main_frame, text="Dots outside the circle:", font=("TkDefaultFont", 12))
label_outside.pack(pady=2)

# Button to switch theme of the program
dark_button = tk.Button(main_frame, text="Dark Mode", command=toggle_dark_mode)
dark_button.pack(pady=2)

root.mainloop()
