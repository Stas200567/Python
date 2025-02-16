class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name
    
    def __repr__(self):
        return f"{self.species} ({self.name})"

class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal} додано до зоопарку.")
    
    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal} вилучено з зоопарку.")
        else:
            print("Тварина не знайдена у зоопарку.")
    
    def __repr__(self):
        return f"Зоопарк: {', '.join(str(animal) for animal in self.animals)}"

if __name__ == "__main__":
    zoo = Zoo()
    
    while True:
        action = input("Оберіть дію (додати, вилучити, показати, вихід): ").strip().lower()
        
        if action == "додати":
            species = input("Введіть вид тварини: ")
            name = input("Введіть ім'я тварини: ")
            zoo.add_animal(Animal(species, name))
        elif action == "вилучити":
            name = input("Введіть ім'я тварини для вилучення: ")
            animal_to_remove = next((a for a in zoo.animals if a.name == name), None)
            if animal_to_remove:
                zoo.remove_animal(animal_to_remove)
            else:
                print("Тварина не знайдена.")
        elif action == "показати":
            print(zoo)
        elif action == "вихід":
            break
        else:
            print("Невідома команда. Спробуйте ще раз.")
