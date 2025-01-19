# Monte Carlo π Approximation Program

## About the Project


This is a Python program I created to estimate the value of π using the Monte Carlo method. The program generates random points within a square that surrounds a unit circle and checks how many points fall inside the circle. Based on the ratio of points inside the circle to the total points, it calculates an approximation of π.

This project helped me practice important programming concepts like randomness, loops, conditionals, and mathematical calculations. I also got to learn how to use the Tkinter library to build a graphical user interface. The program uses a Monte Carlo simulation to approximate the value of π and shows the process visually with points on a canvas. I added features like a slider to adjust the number of points, a dark mode toggle, and a timer to see how long the calculations take. I also implemented a section to display how many dots fall inside and outside the circle during the simulation. Working on this helped me understand how to combine math, programming, and GUI design in Python.

![Vídeo sin título ‐ Hecho con Clipchamp (3)](https://github.com/user-attachments/assets/957210a2-9f7a-4523-a879-071ad0decfe8)

## How It Works

![image](https://github.com/user-attachments/assets/43b6f9cc-5292-43dc-b8e9-871c9284ab55)


1. **Random Point Generation**:
   - Random points are generated within a square of size 2x2 (coordinates between -1 and 1).
2. **Distance Calculation**:
   - The program calculates the distance of each point from the center of the square \((0, 0)\).
3. **Circle Check**:
   - If the distance is less than or equal to 1, the point is inside the circle.

https://pyscript.com/@franz2/muddy-grass/  <- link to test run the core code online without IDE and UI 


The program increases the number of random points iteratively, demonstrating the improved accuracy of the approximation.

## Example Output

When running the program with different numbers of points, it outputs:

```plaintext
Using 100 points, the pi approximation is 3.287128712871287
Using 1000 points, the pi approximation is 3.1408591408591406
Using 10000 points, the pi approximation is 3.1424857514248576
Using 100000 points, the pi approximation is 3.1432718391207297
```

## Dark Mode Feature
The program includes a Dark Mode feature, allowing users to toggle between light and dark themes for better accessibility and user preference.

![image](https://github.com/user-attachments/assets/5c8a4d7b-dffe-4295-b774-5cecd8f4e8d6)


## How It Works
Clicking the Dark Mode button switches the theme to dark, changing the background and text colors to enhance visibility.
The button text updates to "Light Mode," letting the user switch back to the light theme.
Implementation
The feature uses a global theme_mode variable to track the current theme and updates the UI elements dynamically based on the selected mode. Below is the function responsible for toggling the dark mode:



