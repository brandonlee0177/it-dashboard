class Habitat:
    def __init__(self, name, climate, capacity):
        self.name = name
        self.climate = climate
        self.capacity = capacity
        self.animals = []

    def add_animal(self, animal):
        """Silently adds animal or returns a 'full' message."""
        if len(self.animals) >= self.capacity:
            return f"{self.name} is full! ({self.capacity} max)"
        self.animals.append(animal)
        return f"{animal.name} added to {self.name}"

    def roll_call(self):
        """Prints the list of animals inside this habitat."""
        if not self.animals:
            print("    (Empty)")
        for animal in self.animals:
            print(f"    • {animal.describe()}")

    def __str__(self):
        """Fixes the <Habitat object at...> error."""
        return f" [{self.climate.upper()}] {self.name} ({len(self.animals)}/{self.capacity})"

# Test it
savanna = Habitat("Savanna Exhibit", "tropical", 5)
print(savanna)
aviary = Habitat("Sky Dome Aviary", "temperate", 10)
print(aviary)
aquarium = Habitat("Deep Blue Aquarium", "aquatic", 20)
print(aquarium)
