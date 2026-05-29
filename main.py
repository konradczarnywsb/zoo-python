class Animal:
    def __init__(self, animal_type, age, keeper):
        self.animal_type = animal_type
        self.age = age
        self.keeper = keeper

    def feed(self):
        print(f"zwierzę: {self.animal_type} zostało nakarmione.")

    def __str__(self):
        return f"Gatunek: {self.animal_type}, wiek: {self.age}, opiekun: {self.keeper}"


class ZooKeeper:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enclosure:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_animals(self):
        print(f"\n=== {self.name} ===")

        if not self.animals:
            print("Brak zwierząt.")
            return

        for animal in self.animals:
            print(animal)


def main():
    keepers = []
    enclosures = []

    while True:
        print("\n===== ZOO =====")
        print("1. Dodaj opiekuna")
        print("2. Dodaj wybieg")
        print("3. Dodaj zwierzę")
        print("4. Wyświetl wybiegi")
        print("5. Nakarm wszystkie zwierzęta")
        print("0. Wyjście")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            first_name = input("Imię: ")
            last_name = input("Nazwisko: ")
            age = int(input("Wiek: "))

            keeper = ZooKeeper(first_name, last_name, age)
            keepers.append(keeper)

            print("Dodano opiekuna.")

        elif choice == "2":
            name = input("Nazwa wybiegu: ")

            enclosure = Enclosure(name)
            enclosures.append(enclosure)

            print("Dodano wybieg.")

        elif choice == "3":

            if not keepers:
                print("Najpierw dodaj opiekuna.")
                continue

            if not enclosures:
                print("Najpierw dodaj wybieg.")
                continue

            animal_type = input("Gatunek zwierzęcia: ")
            age = int(input("Wiek zwierzęcia: "))

            print("\nDostępni opiekunowie:")
            for i, keeper in enumerate(keepers):
                print(f"{i}. {keeper}")

            keeper_index = int(input("Wybierz opiekuna: "))
            keeper = keepers[keeper_index]

            print("\nDostępne wybiegi:")
            for i, enclosure in enumerate(enclosures):
                print(f"{i}. {enclosure.name}")

            enclosure_index = int(input("Wybierz wybieg: "))
            enclosure = enclosures[enclosure_index]

            animal = Animal(animal_type, age, keeper)
            enclosure.add_animal(animal)

            print("Dodano zwierzę.")

        elif choice == "4":

            if not enclosures:
                print("Brak wybiegów.")
                continue

            for enclosure in enclosures:
                enclosure.show_animals()

        elif choice == "5":

            for enclosure in enclosures:
                for animal in enclosure.animals:
                    animal.feed()

        elif choice == "0":
            print("Koniec programu.")
            break

        else:
            print("Nieprawidłowa opcja.")


main()
