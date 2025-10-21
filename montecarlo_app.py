import tkinter as tk
import math
import time
import pi_calc_help as p

CANVAS_SIZE = 600
p.calc_random()

def run_simulation():
    start_time = time.perf_counter()
    canvas.delete("all")
    
    points_amount = int(scale.get())
    canvas.create_oval(1.5, 1.5, CANVAS_SIZE, CANVAS_SIZE, width=2, outline="red")
        
    inside_circle = 0   
    
    for _ in range(points_amount):
        x = p.calc_random()
        y = p.calc_random()
        distance = math.sqrt(x**2 + y**2)
        
        color, inside_circle = p.inside_circle(distance, inside_circle)

        px = (x + 1) * (CANVAS_SIZE / 2)
        py = (1 - y) * (CANVAS_SIZE / 2)
        
        radius = 1
        canvas.create_oval(px - radius, py - radius, px + radius, py + radius, fill=color, outline=color)
        
        elapsed = time.perf_counter() - start_time
        label_timer.config(text=f"Calculation time: {elapsed:.4f} seconds")
        
    pi_approx = 4 * (inside_circle / points_amount)

    label_result.config(text=f"Pi approximation: {pi_approx:.6f}")  
    label_inside.config(text=f"Dots inside the circle: {inside_circle}")
    label_outside.config(text=f"Dots outside the circle: {points_amount - inside_circle}")

root = tk.Tk()
root.title("Monte Carlo π Visualization")   
root.config(bg="SystemButtonFace")

main_frame = tk.Frame(root, padx=10, pady=10, bg="SystemButtonFace")
main_frame.pack()

control_frame = tk.Frame(main_frame, bg="SystemButtonFace")
control_frame.pack(pady=5)

scale = tk.Scale(
    control_frame,
    from_=50, to=10000,
    orient=tk.HORIZONTAL,
    length=200,
    font=10,
    bg="SystemButtonFace",
    fg="black",
    troughcolor="white",
    highlightthickness=0
)
scale.set(50)
scale.pack(side=tk.LEFT, padx=5)

button = tk.Button(
    control_frame, 
    text="Run Simulation", 
    font=15, 
    command=run_simulation,
    width=13, 
    height=1,
    bg="SystemButtonFace", 
    fg="black"
)
button.pack(side=tk.LEFT, padx=5)

label_timer = tk.Label(main_frame, text="Calculation time:", font=("TkDefaultFont", 12),
                       bg="SystemButtonFace", fg="black")
label_timer.pack(pady=2)

canvas_frame = tk.Frame(main_frame, bd=2, relief="groove", bg="SystemButtonFace")
canvas_frame.pack(pady=5)

canvas = tk.Canvas(canvas_frame, width=CANVAS_SIZE, height=CANVAS_SIZE,
                   highlightthickness=0, bg="white")
canvas.pack()
canvas.create_oval(1.5, 1.5, CANVAS_SIZE, CANVAS_SIZE, width=2, outline="red")

label_result = tk.Label(main_frame, text="Pi approximation:", font=("TkDefaultFont", 14),
                        bg="SystemButtonFace", fg="black")
label_result.pack(pady=4)

label_inside = tk.Label(main_frame, text="Dots inside the circle:", font=("TkDefaultFont", 12),
                        bg="SystemButtonFace", fg="black")
label_inside.pack(pady=1)

label_outside = tk.Label(main_frame, text="Dots outside the circle:", font=("TkDefaultFont", 12),
                         bg="SystemButtonFace", fg="black")
label_outside.pack(pady=2)

root.mainloop()
