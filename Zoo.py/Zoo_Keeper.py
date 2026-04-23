from Habitat import aviary, aquarium, savanna

class Zookeeper:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.assigned_habitats = []

    def assign(self, habitat):
        """Assigns habitat to keeper silently."""
        self.assigned_habitats.append(habitat)
        return f"{self.name} now manages {habitat.name}"

    def daily_report(self):
        """Prints the keeper's personal assigned habitats and roll calls."""
        print(f"Keeper: {self.name} ({self.specialty})")
        for hab in self.assigned_habitats:
            print(f"  {hab}")
            hab.roll_call()
            
sarah = Zookeeper("Sarah", "Marine Biology")
sarah.assign(aquarium)  # Actual call
sarah.assign(aviary)    # Actual call
sarah.assign(savanna)   # Actual call

Larry = Zookeeper("Larry", "Savanna Specialist")
Larry.assign(savanna)   # Actual call
Larry.assign(aviary)   # Actual call
Larry.assign(aquarium) # Actual call

Garwin = Zookeeper("Garwin", "Aviary Expert")
Garwin.assign(aviary)  # Actual call
Garwin.assign(savanna) # Actual call
Garwin.assign(aquarium) # Actual call