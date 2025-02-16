def factorial(n):
    if n < 0:
        return "Факторіал визначений лише для невід'ємних чисел"
    
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


num = int(input("Введіть число: "))
print(f"{num}! = {factorial(num)}")
