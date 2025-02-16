def factorial(n):
    if n < 0:
        return "Факторіал визначений лише для невід'ємних чисел"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


num = int(input("Введіть число: "))
print(f"{num}! = {factorial(num)}")
