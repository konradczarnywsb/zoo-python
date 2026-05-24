#Gra symulująca zoo – klasy Animal, Enclosure, ZooKeeper; przydzielanie zwierząt do wybiegów i opiekunów, karmienie.

class Animal:
    def __init__(self, animal_type, age):
        self.animal_type = animal_type
        self.age = age
        self.keeper
    def feed(self):
        print("Zwierzę zostało nakarmione")
    def assign_keeper(self, keeper):
        self.keeper = keeper

    

class Enclosure:
    def __init__(self):
        self.animal_list = []
    def add_animal(self, animal):
        self.animal_list.append(animal)
    def get_animals(self):
        for animal in self.animal_list:
            print(animal)

class ZooKeeper:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
def main():
    print("hello")

main()