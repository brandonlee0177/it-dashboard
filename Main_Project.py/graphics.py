import turtle
import tkinter as tk
import math

# --- GRAPHICS FUNCTIONS ---

def draw_topology(manager):
    """Uses Turtle Graphics to draw a star topology map safely inside a Tkinter window."""
    if not manager.devices:
        print("\n[!] No devices to draw. Please add a Router or Switch first.")
        return
    
    print("\n[+] Launching Upgraded Topology Window...")

    # Create a secondary Tkinter window (Toplevel)
    top = tk.Toplevel()
    top.title("Live Network Topology - IT Dashboard")
    top.geometry("800x600")
    top.configure(bg="#0a0e1a") # Dark background

    # Create a Tkinter Canvas inside that window
    canvas = tk.Canvas(top, width=800, height=600, bg="#0a0e1a", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Attach a RawTurtle to the custom canvas
    screen = turtle.TurtleScreen(canvas)
    screen.bgcolor("#0a0e1a")
    t = turtle.RawTurtle(screen)
    t.speed(0)
    t.hideturtle()

    # 1. Draw central "Core Network" node
    t.penup()
    t.goto(0, -30)
    t.pendown()
    t.color("#374151")      # Dark gray border
    t.fillcolor("#1f2937")  # Darker gray fill
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    
    t.penup()
    t.goto(0, -8)
    t.color("#00ffcc")      # Cyan text
    t.write("CORE", align="center", font=("Consolas", 12, "bold"))

    # 2. Calculate positions using trigonometry for a perfect circle
    num_devices = len(manager.devices)
    radius = 180
    
    # Avoid division by zero if something weird happens
    angle_step = 360 / num_devices if num_devices > 0 else 360 

    for i, device in enumerate(manager.devices):
        # Convert degrees to radians for the math functions
        angle = math.radians(i * angle_step)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        # 3. Draw connecting line from CORE to the device
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.color("#374151") # Subtle line color
        t.width(2)
        t.goto(x, y)
        t.width(1)

        # 4. Draw the actual device
        t.penup()
        
        if device.device_type == "router":
            # Routers are Neon Green Circles
            t.goto(x, y - 20) 
            t.pendown()
            t.color("#059669")      # Dark green border
            t.fillcolor("#10b981")  # Bright green fill
            t.begin_fill()
            t.circle(20)
            t.end_fill()
        else:
            # Switches are Blue Squares
            t.goto(x - 20, y - 20)
            t.pendown()
            t.color("#2563eb")      # Dark blue border
            t.fillcolor("#3b82f6")  # Bright blue fill
            t.begin_fill()
            for _ in range(4):
                t.forward(40)
                t.left(90)
            t.end_fill()

        # 5. Label the device
        t.penup()
        t.goto(x, y + 25)
        t.color("white")
        t.write(device.hostname, align="center", font=("Arial", 10, "bold"))
        
        t.goto(x, y + 40)
        t.color("#9ca3af")
        t.write(device.ip_address, align="center", font=("Arial", 8, "normal"))

    print("--- Close Topology window to return to Main Menu ---")