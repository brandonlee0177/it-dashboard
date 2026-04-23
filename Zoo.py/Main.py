from Animals import Dog, Bird, Fish, Cat, Elephant, Giraffe, Rhinoceros, Zebra
from Habitat import Habitat
from Zoo_Keeper import Zookeeper
from Zoo import Zoo
from Zoo_Sim import start_simulation

def main():
    # 1. CREATE the variable here
    my_zoo = Zoo("Hexworth Wildlife Park")

    # 2. Create Habitats
    savanna = Habitat("Savanna Exhibit", "tropical", 6)
    aviary = Habitat("Sky Dome Aviary", "temperate", 10)
    aquarium = Habitat("Deep Blue Aquarium", "aquatic", 20)
    
    my_zoo.add_habitat(savanna)
    my_zoo.add_habitat(aviary)
    my_zoo.add_habitat(aquarium)

    # 3. Create Animals
    rex = Dog("Rex", "German Shepherd")
    dumbo = Elephant("Dumbo", "African")
    rifiki = Rhinoceros("Rafiki", "White")
    simba = Giraffe("Simba", "Masai")
    stripes = Zebra("Stripes", "Grassland")
    tweety = Bird("Tweety", "Canary")
    nemo = Fish("Nemo", "Clownfish")
    moxie = Cat("Moxie", "Siamese")

    # 4. Add Animals 
    savanna.add_animal(rex)
    savanna.add_animal(dumbo)
    savanna.add_animal(moxie)
    aviary.add_animal(tweety)
    aquarium.add_animal(nemo)
    savanna.add_animal(rifiki)
    savanna.add_animal(simba)
    savanna.add_animal(stripes)

    # 5. Assign Keeper
    sarah = Zookeeper("Sarah", "Marine Biology")
    larry = Zookeeper("Larry", "Savanna Specialist")
    garwin = Zookeeper("Garwin", "Aviary Expert")
    
    my_zoo.hire_keeper(sarah)
    my_zoo.hire_keeper(larry)
    my_zoo.hire_keeper(garwin)
    
    sarah.assign(aquarium)
    sarah.assign(aviary)
    larry.assign(savanna)
    garwin.assign(aviary)
    garwin.assign(savanna)
    garwin.assign(aquarium)

    # 6. Final Clean Report
    my_zoo.full_report()

    # --- THE FIX IS HERE ---
    # Move this line INSIDE main() so it can see the 'my_zoo' variable.
    start_simulation(my_zoo.all_entities())

if __name__ == "__main__":
    main()