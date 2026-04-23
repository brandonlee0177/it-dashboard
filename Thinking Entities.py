import os
import turtle
import random
import math
import time

# 1. Screen setup
screen = turtle.Screen()
screen.title("Game of Tag - Corner Fix")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)


#paths
BG_PATH = r"C:\Users\jupit\Desktop\it-dashboard\.gif photos\background8.gif"

# 2. Create Person 1
p1 = turtle.Turtle()
p1.shape("circle")
p1.color("blue")
p1.penup()
p1.goto(-100, 0)
p1.is_it = True 

# 3. Create Person 2
p2 = turtle.Turtle()
p2.shape("square")
p2.color("red")
p2.penup()
p2.goto(100, 0)
p2.is_it = False 

# Assign initial random goals
for p in [p1, p2]:
    p.target_x = random.randint(-250, 250)
    p.target_y = random.randint(-250, 250)
    p.speed_val = .9

# 4. Walking logic
def walk_towards_goal(person):
    angle = math.atan2(person.target_y - person.ycor(), person.target_x - person.xcor())
    person.setx(person.xcor() + math.cos(angle) * person.speed_val)
    person.sety(person.ycor() + math.sin(angle) * person.speed_val)
    
    distance_to_goal = math.sqrt((person.target_x - person.xcor())**2 + (person.target_y - person.ycor())**2)
    if distance_to_goal < 5:
        person.target_x = random.randint(-250, 250)
        person.target_y = random.randint(-250, 250)
        
bg_manager = turtle.Turtle()
bg_manager.penup()
if os.path.exists(BG_PATH):
    screen.addshape(BG_PATH)
    bg_manager.shape(BG_PATH)
    bg_manager.goto(0, 0)
else:
    screen.bgcolor("skyblue")

# 5. Main Simulation Loop
cooldown_timer = 0 
running = True

while running:
    try:
        screen.update()
        time.sleep(0.01)
        
        if cooldown_timer > 0:
            cooldown_timer -= 1
        
        distance_apart = math.sqrt((p1.xcor() - p2.xcor())**2 + (p1.ycor() - p2.ycor())**2)
        
        # --- THE TAG INTERACTION ---
        if distance_apart < 15 and cooldown_timer == 0:
            p1.is_it = not p1.is_it
            p2.is_it = not p2.is_it
            
            p1.color("blue" if p1.is_it else "red")
            p2.color("blue" if p2.is_it else "red")
            
            # Increased cooldown to 2 seconds so they have more time to separate
            cooldown_timer = 200 
            
            p1.target_x = random.randint(-250, 250)
            p1.target_y = random.randint(-250, 250)
            p2.target_x = random.randint(-250, 250)
            p2.target_y = random.randint(-250, 250)

        # --- THE BRAINS ---
        if cooldown_timer == 0:
            for person in [p1, p2]:
                other_person = p2 if person == p1 else p1
                
                if person.is_it:
                    # Chaser Logic
                    if distance_apart < 150:
                        person.target_x = other_person.xcor()
                        person.target_y = other_person.ycor()
                        person.speed_val = 0.9 
                    else:
                        person.speed_val = 1.5 
                else:
                    # Runner Logic
                    if distance_apart < 100:
                        
                        # --- NEW: CORNER ESCAPE INSTINCT ---
                        # If they get within 50 pixels of the walls, run to the center (0,0)!
                        if person.xcor() > 230 or person.xcor() < -230 or person.ycor() > 230 or person.ycor() < -230:
                            person.target_x = 0
                            person.target_y = 0
                            person.speed_val = 1.6 # Extra panic speed to escape the corner
                        else:
                            # Normal run away logic
                            person.target_x = person.xcor() - (other_person.xcor() - person.xcor())
                            person.target_y = person.ycor() - (other_person.ycor() - person.ycor())
                            person.speed_val = 0.6 
                    else:
                        person.speed_val = 0.5
        
        # Move them
        walk_towards_goal(p1)
        walk_towards_goal(p2)
        
    except turtle.Terminator:
        running = False
        break