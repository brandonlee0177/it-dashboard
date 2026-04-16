from datetime import datetime


APPNAME = "IT Dashboard"
VERSION = "0.1.0"
AUTHOR = "Brandon Lee"
COPYRIGHT = "Copyright (c) 2026 Brandon Lee. All rights reserved."
COURSE_NAME = "Programming for Technology Professionals - KU_JAX_COP1034CD4-104062026"
INSTRUCTORS_NAME = "Professor Mora"
ASSIGNMENT_NAME = "Week 2 - Geometry calculator + Turtle Visualization"
# Get the current local date and time
currenttime = datetime.now()

import math
import turtle

t = turtle.Turtle()
t.speed(5)  # Set turtle speed to fast

def draw_circle(radius):
    color = "purple"
    t.color(color)
    t.circle(radius)
def draw_square(side_length):
    color = "red"
    t.color(color)
    for _ in range(4):
        t.forward(side_length)
        t.left(90)  
def draw_triangle(side_length):
    color = "green"
    t.color(color)
    for _ in range(3):
        t.forward(side_length)
        t.left(120) 
def draw_squiggly_line(length):
    color = "blue"
    t.color(color)
    for i in range(length):
        t.forward(10)
        if i % 2 == 0:
            t.left(45)
        else:
            t.right(45)
def main():
    while True:
        try:
            print("\nChoose a shape to draw:")
            print("1. Circle")
            print("2. Square")
            print("3. Triangle")
            print("4. Squiggly Line")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")
            if choice == '1':
                radius = float(input("Enter the radius of the circle: "))
                draw_circle(radius)
                print()
                print("--------------------------------")
                print(f"Circle with radius {radius} drawn.")
                print("--------------------------------")
            elif choice == '2':
                side_length = float(input("Enter the side length of the square: "))
                draw_square(side_length)
                print()
                print("--------------------------------")
                print(f"Square with side length {side_length} drawn.")
                print("--------------------------------")
            elif choice == '3':
                side_length = float(input("Enter the side length of the triangle: "))
                draw_triangle(side_length)
                print()
                print("------------------------------------------")
                print(f"Triangle with side length {side_length} drawn.")
                print("------------------------------------------")
            elif choice == '4':
                length = int(input("Enter the length of the squiggly line: "))
                draw_squiggly_line(length)
                print()
                print("------------------------------------------")
                print(f"Squiggly line with length {length} drawn.")
                print("------------------------------------------")
            elif choice == '5':
                print("Exiting the program. Goodbye!")
                turtle.bye()
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid numeric input. Please enter a valid number.")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting the program. Goodbye!")
            break
def draw_shapes():
    t.pendown()
    draw_circle(50)
    t.penup()
    t.goto(150, 0)
    t.pendown()
    draw_square(100)
    t.penup()
    t.goto(-150, 0)
    t.pendown()
    draw_triangle(100)
    t.penup()
    t.goto(0, -150)
    t.pendown()
    draw_squiggly_line(10)
def draw_s():
    pass

if __name__ == "__main__":
    main()
    