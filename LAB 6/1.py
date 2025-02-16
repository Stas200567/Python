class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("Engine started")


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"Car {self.brand} {self.model} engine started")


class Motorcycle(Vehicle):
    def __init__(self, brand, type_):
        super().__init__(brand)
        self.type = type_

    def start_engine(self):
        print(f"Motorcycle {self.brand} {self.type} engine started")


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        print(f"Battery of {self.brand} {self.model} is charging")


class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def start_all_engines(self):
        for vehicle in self.vehicles:
            vehicle.start_engine()


def create_vehicle():
    vehicle_type = input("Введіть тип транспорту (car/motorcycle/electric): ").strip().lower()

    brand = input("Введіть марку транспорту: ").strip()

    if vehicle_type == "car":
        model = input("Введіть модель автомобіля: ").strip()
        return Car(brand, model)

    elif vehicle_type == "motorcycle":
        type_ = input("Введіть тип мотоцикла: ").strip()
        return Motorcycle(brand, type_)

    elif vehicle_type == "electric":
        model = input("Введіть модель електромобіля: ").strip()
        battery_capacity = input("Введіть ємність батареї: ").strip()
        return ElectricCar(brand, model, battery_capacity)

    else:
        print("Невідомий тип транспорту!")
        return None


garage = Garage()

num_vehicles = int(input("Скільки транспортних засобів додати в гараж? "))

for _ in range(num_vehicles):
    vehicle = create_vehicle()
    if vehicle:
        garage.add_vehicle(vehicle)

garage.start_all_engines()

for vehicle in garage.vehicles:
    if isinstance(vehicle, ElectricCar):
        vehicle.charge_battery()
