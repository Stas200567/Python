def km_to_miles(km):
    return km * 0.621371

try:
    km = float(input("Введіть відстань у кілометрах: "))
    miles = km_to_miles(km)
    print(f"{km} км = {miles:.2f} миль")
except ValueError:
    print("Будь ласка, введіть числове значення!")
