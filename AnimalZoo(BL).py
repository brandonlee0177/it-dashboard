import os
import time  # <-- Added the time module here
from abc import ABC, abstractmethod

# Enable ANSI escape codes for Windows File Explorer / CMD
os.system("")

# --- Terminal Color Codes ---
class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RED = '\033[91m'
    RESET = '\033[0m'

# ==========================================
# BASE CLASSES
# ==========================================
class Animal(ABC):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass
    
    def describe(self):
        return f"{self.name} is a {self.breed} {self.__class__.__name__}."

# ==========================================
# ANIMAL SUBCLASSES
# ==========================================
class Dog(Animal):
    def speak(self): return f"{self.name} says Woof!"
    def move(self): return f"{self.name} runs on all fours."
    def fetch(self, item): return f"{self.name} fetches the {item}."

class Cat(Animal):
    def speak(self): return f"{self.name} says Meow!"
    def move(self): return f"{self.name} gracefully leaps around."
    def purr(self, how): return f"{self.name} purrs {how}."

class Giraffe(Animal):
    def speak(self): return f"{self.name} says Munch!"
    def move(self): return f"{self.name} stretches its long neck to reach leaves."
    def eat(self, food): return f"{self.name} eats {food}."

class Rhinoceros(Animal):
    def speak(self): return f"{self.name} says Snort!"
    def move(self): return f"{self.name} charges through the savanna."
    def charge(self, how): return f"{self.name} charges {how}."

class Zebra(Animal):
    def speak(self): return f"{self.name} says Neigh!"
    def move(self): return f"{self.name} gallops across the plains."
    def run(self, how): return f"{self.name} runs {how}."

class Elephant(Animal):
    def speak(self): return f"{self.name} says Trumpet!"
    def move(self): return f"{self.name} lumbers along on its massive feet."
    def trumpet(self, how): return f"{self.name} trumpets {how}."

class Bird(Animal):
    def __init__(self, name, breed, can_fly=True):
        super().__init__(name, breed)
        self.can_fly = can_fly

    def speak(self): return f"{self.name} says Chirp!"
    def move(self):
        if self.can_fly:
            return f"{self.name} flutters its wings and takes flight."
        return f"{self.name} waddles on the ground."
    def fly(self, how):
        if self.can_fly:
            return f"{self.name} flies {how}."
        return f"{self.name} cannot fly."

class Fish(Animal):
    def speak(self): return f"{self.name} says Blub!"
    def move(self): return f"{self.name} swims gracefully through the water."
    def swim(self, how): return f"{self.name} swims {how}."

# ==========================================
# MAIN APPLICATION LOOP
# ==========================================
def main():
    # Instantiate all our animals once
    zoo_animals = [
        Dog("Rex", "German Shepherd"),
        Cat("Moxie", "Siamese"),
        Giraffe("Brody", "Masai"),
        Rhinoceros("Ace Ventura", "White Rhino"),
        Zebra("Marty", "Plains Zebra"),
        Elephant("Grant", "African Elephant"),
        Bird("Tweety", "Canary"),
        Fish("Nemo", "Clownfish")
    ]

    while True:
        # Clear the screen for a fresh menu every time (cls for Windows, clear for Linux)
        os.system('cls' if os.name == 'nt' else 'clear')

        print(f"{Color.CYAN}=========================================={Color.RESET}")
        print(f"{Color.YELLOW}        WELCOME TO THE VIRTUAL ZOO        {Color.RESET}")
        print(f"{Color.CYAN}=========================================={Color.RESET}")
        print("Which animal would you like to visit?\n")
        
        # Dynamically build the menu based on the animals list
        for i, animal in enumerate(zoo_animals, 1):
            print(f"{Color.GREEN}{i}){Color.RESET} {animal.__class__.__name__} ({animal.name})")
        
        print(f"\n{Color.MAGENTA}R){Color.RESET} Zoo Rollcall (See everyone!)")
        print(f"{Color.RED}X){Color.RESET} Exit Zoo")
        print(f"{Color.CYAN}=========================================={Color.RESET}")

        choice = input("\nSelect an option: ").strip().upper()

        print(f"\n{Color.CYAN}------------------------------------------{Color.RESET}")

        if choice == 'X':
            print(f"{Color.YELLOW}Smell ya later stinky! Closing the zoo gates...{Color.RESET}")
            break
            
        elif choice == 'R':
            # Polymorphism Demo: Rollcall
            print(f"{Color.YELLOW}--- ZOO ROLLCALL ---{Color.RESET}\n")
            for animal in zoo_animals:
                print(f"{Color.GREEN}{animal.describe()}{Color.RESET}")
                print(f"  Voice:  {animal.speak()}")
                print(f"  Motion: {animal.move()}")
                print()
                
                # --- This pauses the script for 1.5 seconds before printing the next animal ---
                time.sleep(1.5)
                
        elif choice.isdigit() and 1 <= int(choice) <= len(zoo_animals):
            # Show specific animal based on user selection
            # We subtract 1 because lists are 0-indexed, but our menu starts at 1
            selected_animal = zoo_animals[int(choice) - 1]
            
            print(f"{Color.YELLOW}You are visiting the {selected_animal.__class__.__name__}!{Color.RESET}\n")
            print(f"{Color.GREEN}{selected_animal.describe()}{Color.RESET}")
            print(selected_animal.speak())
            print(selected_animal.move())
            
            # Trigger specific methods if they exist
            if isinstance(selected_animal, Dog):
                print(selected_animal.fetch("frisbee"))
            elif isinstance(selected_animal, Cat):
                print(selected_animal.purr("loudly"))
            elif isinstance(selected_animal, Elephant):
                print(selected_animal.trumpet("magnificently"))
            elif isinstance(selected_animal, Bird):
                print(selected_animal.fly("high into the clouds"))

        else:
            print(f"{Color.RED}Invalid choice. Please select a valid option from the menu.{Color.RESET}")

        print(f"{Color.CYAN}------------------------------------------{Color.RESET}")
        # This input acts as a pause screen so you can read the output before the menu loops and clears the screen!
        input(f"{Color.MAGENTA}Press Enter to continue...{Color.RESET}")

if __name__ == "__main__":
    main()