# Monte Carlo π Approximation Program

## About the Project


![Vídeo sin título ‐ Hecho con Clipchamp (3)](https://github.com/user-attachments/assets/957210a2-9f7a-4523-a879-071ad0decfe8)



This is a Python program I created to estimate the value of π (Pi) using the Monte Carlo method. The program generates random points within a square that surrounds a unit circle and checks how many points fall inside the circle. Based on the ratio of points inside the circle to the total points, it calculates an approximation of π.

This project helped me practice concepts like randomness, loops, conditionals, and mathematical calculations in Python.

## How It Works

![image](https://github.com/user-attachments/assets/43b6f9cc-5292-43dc-b8e9-871c9284ab55)


1. **Random Point Generation**:
   - Random points are generated within a square of size 2x2 (coordinates between -1 and 1).
2. **Distance Calculation**:
   - The program calculates the distance of each point from the center of the square \((0, 0)\).
3. **Circle Check**:
   - If the distance is less than or equal to 1, the point is inside the circle.

https://pyscript.com/@franz2/muddy-grass/  <- link to test run code without IDE (online)


The program increases the number of random points iteratively, demonstrating the improved accuracy of the approximation.

## Example Output

When running the program with different numbers of points, it outputs:

```plaintext
Using 100 points, the pi approximation is 3.287128712871287
Using 1000 points, the pi approximation is 3.1408591408591406
Using 10000 points, the pi approximation is 3.1424857514248576
Using 100000 points, the pi approximation is 3.1432718391207297



