class Zoo:
    """The top-level container that manages habitats and keepers."""
    
    def __init__(self, name):
        """Initialize the zoo with lists for habitats and keepers."""
        self.name = name
        self.habitats = []
        self.keepers = []

    def add_habitat(self, habitat):
        """Adds a habitat object to the zoo."""
        self.habitats.append(habitat)

    def hire_keeper(self, keeper):
        """Adds a zookeeper object to the zoo."""
        self.keepers.append(keeper)

    def total_animals(self):
        """Calculates the total number of animals across all habitats."""
        return sum(len(h.animals) for h in self.habitats)

    def all_entities(self):
        """
        Gathers all keepers and all animals from all habitats into one list.
        This is used for the GUI simulation.
        """
        combined_list = []
        
        # 1. Add all the hired keepers (Sarah, Larry, Garwin)
        combined_list.extend(self.keepers)
        
        # 2. Add all animals from every habitat
        for hab in self.habitats:
            combined_list.extend(hab.animals)
            
        return combined_list

    def full_report(self):
        """Prints a clean, structured dashboard of the entire zoo."""
        print("\n" + "="*50)
        print(f"{self.name.upper():^50}")
        print("="*50)
        print(f"Habitats: {len(self.habitats)} | Animals: {self.total_animals()} | Keepers: {len(self.keepers)}")
        print("-" * 50)
        
        for hab in self.habitats:
            # This calls the __str__ method in Habitat.py
            print(f"\n{hab}")
            # This calls the roll_call method in Habitat.py
            hab.roll_call()
            
        print("\n" + "="*50)