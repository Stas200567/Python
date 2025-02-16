def average_nonnegative(numbers):
    nonnegative_numbers = [num for num in numbers if num >= 0]
    if not nonnegative_numbers:
        return "Немає невід'ємних чисел у списку."
    return sum(nonnegative_numbers) / len(nonnegative_numbers)

# Введення списку від користувача
numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
result = average_nonnegative(numbers)
print("Середнє арифметичне невід’ємних чисел:", result)
