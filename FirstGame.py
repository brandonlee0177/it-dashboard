import turtle
import time
import random
import tkinter
import os

# 1. Screen Setup
screen = turtle.Screen()
screen.title("Runner v16 - Full Stability")
WIDTH, HEIGHT = 1200, 600 
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

# Paths
BG_PATH = r"C:\Users\jupit\Desktop\it-dashboard\.gif photos\DesertSunset-large.gif"
player_image = r"C:\Users\jupit\Desktop\it-dashboard\.gif photos\charachterfixed.gif"
rock_image   = r"C:\Users\jupit\Desktop\it-dashboard\.gif photos\rocksfixed.gif"
box_image    = r"C:\Users\jupit\Desktop\it-dashboard\.gif photos\Boxesfixed.gif"
bird_1_image = r"C:\Users\jupit\Desktop\it-dashboard\.gif photos\bird1.gif" 
bird_2_image = r"C:\Users\jupit\Desktop\it-dashboard\.gif photos\bird2.gif" 

# --- 2. FUNCTIONS (Must be defined BEFORE they are called/bound) ---

def restart_game():
    global game_state, score
    if game_state == "game_over":
        score = 0
        player.goto(-400, -75)
        player.dy = 0
        player.jump_count = 0
        # Reset platforms
        platforms[0].goto(-400, -100)
        platforms[1].goto(300, -100)
        platforms[2].goto(800, -20)
        for obs in ground_obstacles:
            obs.hideturtle()
            obs.goto(0, -4000)
        game_state = "start_menu"
        ui_pen.clear()

def jump():
    global game_state
    if game_state == "start_menu":
        game_state = "playing"
        ui_pen.clear()
    if game_state == "playing" and player.jump_count < 3:
        player.dy = 14
        player.jump_count += 1

# Smooth Movement Key States
keys = {"Left": False, "Right": False}
def press_left(): keys["Left"] = True
def release_left(): keys["Left"] = False
def press_right(): keys["Right"] = True
def release_right(): keys["Right"] = False

def create_platform_unit(x, y, stretch=10, is_start=False):
    plat = turtle.Turtle()
    plat.shape("square") 
    plat.shapesize(stretch_wid=0.7, stretch_len=stretch) 
    plat.color("sienna")
    plat.penup()
    plat.goto(x, y)
    platforms.append(plat)
    
    obs = turtle.Turtle()
    obs.penup()
    if not is_start and random.random() < 0.6:
        img = random.choice(ground_obs_pool)
        try:
            obs.shape(img)
            obs.goto(x, y + offsets.get(img, 40))
            obs.showturtle()
        except:
            obs.hideturtle()
    else:
        obs.hideturtle()
        obs.goto(x, -4000) 
    ground_obstacles.append(obs)

# --- 3. INITIALIZE OBJECTS ---

# Background (Created FIRST to be at the bottom layer)
bg_manager = turtle.Turtle()
bg_manager.penup()
if os.path.exists(BG_PATH):
    screen.addshape(BG_PATH)
    bg_manager.shape(BG_PATH)
    bg_manager.goto(0, 0)
else:
    screen.bgcolor("skyblue")

# UI and Sprites
score = 0
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.color("white")

ui_pen = turtle.Turtle()
ui_pen.penup()
ui_pen.hideturtle()
ui_pen.color("white")

for img in [player_image, rock_image, box_image, bird_1_image, bird_2_image]:
    if os.path.exists(img): screen.addshape(img)

offsets = {rock_image: 54, box_image: 29}
hitboxes = {rock_image: 35, box_image: 25, bird_1_image: 20, bird_2_image: 20}
ground_obs_pool = [rock_image, box_image]
bird_pool = [bird_1_image, bird_2_image]

# Player
player = turtle.Turtle()
try: player.shape(player_image)
except: player.shape("turtle")
player.penup()
player.goto(-400, -75) 
player.dy = 0      
player.jump_count = 0  
gravity = -0.6

# Platforms
platforms = []
ground_obstacles = [] 
create_platform_unit(-400, -100, stretch=20, is_start=True)
create_platform_unit(300, -100, stretch=10)
create_platform_unit(800, -20, stretch=10) 

birds = []
for _ in range(3):
    b = turtle.Turtle()
    b.penup()
    # --- ADD THIS LINE TO FIX THE IMAGES ---
    try:
        b.shape(random.choice(bird_pool))
    except:
        b.shape("triangle") # Fallback if image fails
    # ---------------------------------------
    b.goto(random.randint(800, 1600), random.randint(50, 250))
    birds.append(b)

obstacle_speed = -9 
game_state = "start_menu" 

# --- 4. BINDINGS ---
screen.listen()
screen.onkeypress(jump, "space")
screen.onkeypress(restart_game, "r")
screen.onkeypress(press_left, "Left")
screen.onkeyrelease(release_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeyrelease(release_right, "Right")

# --- 5. MAIN LOOP ---
running = True
while running:
    try:
        w, h = screen.window_width(), screen.window_height()
        half_w, half_h = w / 2, h / 2
        bg_manager.goto(0, 0) # Force background center
        
        time.sleep(0.015)
        
        if game_state == "start_menu":
            ui_pen.goto(0, 0)
            ui_pen.write("HOLD ARROWS TO MOVE | SPACE TO START", align="center", font=("Courier", 24, "bold"))

        if game_state == "playing":
            # Smooth Movement
            if keys["Left"]: player.setx(player.xcor() - 10)
            if keys["Right"]: player.setx(player.xcor() + 10)

            # Boundaries
            if player.xcor() < -half_w: player.setx(-half_w)
            if player.xcor() > half_w: player.setx(half_w)

            # Physics
            player.dy += gravity
            player.sety(player.ycor() + player.dy)
            
            # Collisions
            for plat in platforms:
                hw = (plat.shapesize()[1] * 10) + 20
                if abs(player.xcor() - plat.xcor()) < hw:
                    pt = plat.ycor() + 28
                    if player.dy <= 0 and pt - 20 < player.ycor() < pt + 10:
                        player.sety(pt); player.dy = 0; player.jump_count = 0

            if player.ycor() < -half_h - 100: game_state = "game_over"

            # Scrolling World
            for i in range(len(platforms)):
                p, o = platforms[i], ground_obstacles[i]
                p.setx(p.xcor() + obstacle_speed)
                if o.isvisible(): o.setx(p.xcor())
                
                if p.xcor() < -half_w - 200:
                    nx = half_w + random.randint(100, 500)
                    ny = random.choice([-100, -20, 80, 120])
                    p.goto(nx, ny)
                    if random.random() < 0.6:
                        img = random.choice(ground_obs_pool)
                        try:
                            o.shape(img); o.showturtle()
                            o.goto(nx, ny + offsets.get(img, 40))
                        except: pass
                    else:
                        o.hideturtle(); o.goto(nx, -4000)

   # Bird movement and collision
            for b in birds:
                b.setx(b.xcor() + obstacle_speed - 2)
                
                # Respawn logic
                if b.xcor() < -half_w - 100: 
                    b.goto(half_w + random.randint(300, 800), random.randint(50, 250))
                    try:
                        b.shape(random.choice(bird_pool))
                    except:
                        pass
                
                # Collision check (This must be inside the 'for b in birds' loop)
                if player.distance(b) < 25: 
                    game_state = "game_over"

            # Ground obstacle collision
            for o in ground_obstacles:
                if o.isvisible():
                    sz = hitboxes.get(o.shape(), 25)
                    if abs(player.xcor() - o.xcor()) < sz and abs(player.ycor() - o.ycor()) < (sz + 5):
                        game_state = "game_over"

            # Scoring logic
            score += 1
            if score % 10 == 0:
                score_display.clear()
                score_display.goto(-half_w + 30, half_h - 50)
                score_display.write(f"Score: {score}", font=("Courier", 18, "bold"))
        
        # Game Over Screen logic
        if game_state == "game_over":
            ui_pen.goto(0, 0)
            ui_pen.write("GAME OVER! PRESS R", align="center", font=("Courier", 24, "bold"))

        screen.update()

    except (turtle.Terminator, tkinter.TclError):
        running = False
        break