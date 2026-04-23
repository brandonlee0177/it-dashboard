import random
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species
        # GUI Data
        self.x = random.randint(-200, 200)
        self.y = random.randint(-200, 200)
        self.dx = random.choice([-3, -2, 2, 3]) # Horizontal speed
        self.dy = random.choice([-3, -2, 2, 3]) # Vertical speed

    def move_tick(self, boundary_x, boundary_y):
        """Updates position and bounces off walls."""
        self.x += self.dx
        self.y += self.dy

        # Bounce logic
        if abs(self.x) > boundary_x: 
            self.dx *= -1
        if abs(self.y) > boundary_y: 
            self.dy *= -1
        
    @abstractmethod
    def speak(self): pass

    @abstractmethod
    def move(self): pass

    def describe(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed
    def speak(self): return f"{self.name} says: Woof! Woof!"
    def move(self): return f"{self.name} runs on four legs"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Feline")
        self.breed = breed
    def speak(self): return f"{self.name} says: Meow!"
    def move(self): return f"{self.name} gracefully leaps around"

class Bird(Animal):
    def __init__(self, name, breed, can_fly=True):
        super().__init__(name, "Bird")
        self.breed = breed
        self.can_fly = can_fly
    def speak(self): return f"{self.name} says: Chirp!"
    def move(self): 
        return f"{self.name} flies through the sky" if self.can_fly else f"{self.name} walks on the ground"

class Giraffe(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Giraffidae")
        self.breed = breed
    def speak(self): return f"{self.name} says: Munch!"
    def move(self): return f"{self.name} stretches its long neck to reach leaves"

class Rhinoceros(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Rhinocerotidae")
        self.breed = breed
    def speak(self): return f"{self.name} says: Snort!"
    def move(self): return f"{self.name} charges through the savanna"

class Zebra(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Equidae")
        self.breed = breed
    def speak(self): return f"{self.name} says: Neigh!"
    def move(self): return f"{self.name} gallops across the plains"

class Elephant(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Elephantidae")
        self.breed = breed
    def speak(self): return f"{self.name} says: Trumpet!"
    def move(self): return f"{self.name} lumbers along on its massive feet"

class Fish(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Fish")
        self.breed = breed
    def speak(self): return f"{self.name} says: Blub!"
    def move(self): return f"{self.name} swims gracefully through the water"
# === THE GUARD ===
# This block ONLY runs if you execute: python animal.py
# It is SKIPPED when main.py does: from animal import Dog

if __name__ == "__main__":
    # Test code -- proves the class works
    rex = Dog("rex", "German Shepherd")
    print(rex.describe())    # Rex is a Canine
    print(rex.speak())      # Rex says: Woof! Woof!
    print(rex.move())       # Rex runs on four legs
    
    print("========================================")
    
    moxie = Cat("moxie", "Siamese")
    print(moxie.describe())  # Moxie is a Feline
    print(moxie.speak())    # Moxie says: Meow!
    print(moxie.move())     # Moxie gracefully leaps around

    print("========================================")

    simba = Giraffe("simba", "Masai")
    print(simba.describe())  # Simba is a Giraffe
    print(simba.speak())    # Simba says: Munch!
    print(simba.move())     # Simba stretches its long neck to reach leaves)

    print("========================================")

    rafiki = Rhinoceros("rafiki", "White")
    print(rafiki.describe())  # Rafiki is a Rhinocerotus
    print(rafiki.speak())    # Rafiki says: Snort!
    print(rafiki.move())     # Rafiki charges through the savanna

    print("========================================")

    stripes = Zebra("stripes", "Grassland")
    print(stripes.describe())  # Stripes is a Zebra
    print(stripes.speak())    # Stripes says: Neigh!
    print(stripes.move())     # Stripes gallops across the plains

    print("========================================")

    dumbo = Elephant("dumbo", "African")
    print(dumbo.describe())  # Dumbo is a Elephant
    print(dumbo.speak())    # Dumbo says: Trumpet!
    print(dumbo.move())     # Dumbo lumbers along on its massive feet
    
    print("========================================")
    
    nemo = Fish("nemo", "Clownfish")
    print(nemo.describe())  # Nemo is a Fish
    print(nemo.speak())    # Nemo says: Blub!
    print(nemo.move())     # Nemo swims gracefully through the water

    print("========================================")

    tweety = Bird("tweety", "Canary")
    print(tweety.describe())  # Tweety is a Bird
    print(tweety.speak())    # Tweety says: Chirp!
    print(tweety.move())     # Tweety flies through the sky

    print("--- animal.py test passed ---")