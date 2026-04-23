import turtle
import random
import time
from Animals import Cat, Giraffe, Dog, Bird, Fish, Elephant, Zebra, Rhinoceros # Import your classes
from Zoo_Keeper import Zookeeper

def start_simulation(zoo_objects):
    screen = turtle.Screen()
    screen.setup(800, 600)
    screen.bgcolor("#228B22") # Forest Green
    screen.title("Hexworth Wildlife Park - Live Sim")
    screen.tracer(0) # Turns off animation for manual updates (smoother)

    # Create visual representations for every object
    turtles = []
    
    for obj in zoo_objects:
        t = turtle.Turtle()
        t.penup()
        # Color coding: Animals = White, Keepers = Yellow
        if isinstance(obj, Zookeeper):
            t.shape("square")
            t.color("yellow")
        else:
            t.shape("circle")
            t.color("white")
            
        t.goto(random.randint(-300, 300), random.randint(-200, 200))
        # Store the turtle and the data object together
        turtles.append((t, obj))

    while True:
        for t, data in turtles:
            # Basic wandering logic
            new_x = t.xcor() + random.randint(-5, 5)
            new_y = t.ycor() + random.randint(-5, 5)
            
            # Boundary checking
            if abs(new_x) < 390 and abs(new_y) < 290:
                t.goto(new_x, new_y)
            
        screen.update()
        time.sleep(0.1)

# Example usage with your new keepers
if __name__ == "__main__":
    larry = Zookeeper("Larry", "Big Cats")
    garwin = Zookeeper("Garwin", "Reptiles")
    Sarah = Zookeeper("Sarah", "Marine Life")
    dumbo = Elephant("Dumbo", "African")
    rex = Dog("Rex", "Collie")
    moxie = Cat("Moxie", "Siamese")
    simba = Giraffe("Simba", "Masai")
    rifiki = Rhinoceros("Rafiki", "White")
    stripes = Zebra("Stripes", "Grassland")
    tweety = Bird("Tweety", "Canary")
    nemo = Fish("Nemo", "Clownfish")
    
    # Pass them in as a list to watch them move
    start_simulation([larry, garwin, Sarah, dumbo, rex, moxie, simba, rifiki, stripes, tweety, nemo])