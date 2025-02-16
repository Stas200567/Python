import math
import cmath  

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Два реальні корені: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Один реальний корінь: {root}"
    else:
    
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        return f"Комплексні корені: {root1}, {root2}"


a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))


result = solve_quadratic(a, b, c)
print(result)
