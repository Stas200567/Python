class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
    
    def is_proper(self):
        return abs(self.numerator) < abs(self.denominator)
    
    def __repr__(self):
        return f"Fraction({self.numerator}/{self.denominator})"


numerator = int(input("Введіть чисельник: "))
denominator = int(input("Введіть знаменник: "))

fraction = Fraction(numerator, denominator)
print(f"Створений дріб: {fraction}")
print("Цей дріб правильний" if fraction.is_proper() else "Цей дріб неправильний")
