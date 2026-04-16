import random
from datetime import datetime

APPNAME = "IT Dashboard"
VERSION = "0.1.0"
AUTHOR = "Brandon Lee"
COPYRIGHT = "Copyright (c) 2026 Brandon Lee. All rights reserved."
COURSENAME = "Programming for Technology Professionals - KUJAXCOP1034CD4-104062026"
INSTRUCTORSNAME = "Professor Mora"
ASSIGNMENTNAME = "Week 2 - IT Dashboard Number game"

msg1 = '''Rules to play my game:
1. Guess a number between 1 and 177.
2. You have 10 tries.
3. If you suck and wanna quit type "exit" at any time.
4. I hope you lose.'''

# Get the current local date and time
currenttime = datetime.now()

# Print the header information
print("-------------------------------- ")
print(f"Author: {AUTHOR}")
print(f"{COPYRIGHT}")
print("-------------------------------- ")
print(f"Course: {COURSENAME}")
print(f"Instructor: {INSTRUCTORSNAME}")
print(f"Assignment: {ASSIGNMENTNAME}")
print("-------------------------------- ")

# Format as YYYY-MM-DD HH:MM:SS
formattedtime = currenttime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Report generated on: {formattedtime}")
print()
print()
print("=" * 50)
print(msg1)
print("=" * 50)
print()
print()
print()

# Main loop
import random

while True:
    secret = random.randint(1, 177)
    triesleft = 9
    attempts = 0
    exitgame = False

    while triesleft > 0:
        guessinput = input("Enter your guess, biatch. it's prolly wrong asf: ").strip()
        if guessinput.lower() == "exit":
            print("Smell ya later, Stinky.")
            exitgame = True
            break

        print(f"Your number of remaining lives: {triesleft}")

        try:
            guess = int(guessinput)
        except ValueError:
            print("Enter a fucking number between 1 and 177 you fool.")
            continue

        attempts += 1

        if guess == secret:
            print()
            if attempts <= 3:
                print("Wow, you did it in less than 3, you are not a dumbass.")
            else:
                print(f"Took yo dumbass {attempts} tries")
            print()
            
            break
        elif guess > secret:
            print()
            print("Too High, dumbass")
            print()
        else:
            print()
            print("Too Low, dumbass")
            print()
        triesleft -= 1

    if exitgame:
        break

    if triesleft == 0:
        print(f"You literally had 10 tries, dumbass. *face palm* The number was {secret}")
        print()

    playagain = input("Play again? (y/n): ").strip().lower()
    if playagain != "y":
        break
