def is_prime(n):
    """Перевіряє, чи є число простим."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_previous_prime(n):
    """Знаходить перше просте число, яке передує заданому."""
    if n <= 2:
        return "Простих чисел немає перед цим числом."
    
    n -= 1  
    while n > 1:
        if is_prime(n):
            return n
        n -= 1


num = int(input("Введіть ціле число: "))
result = find_previous_prime(num)
print(f"Перше просте число, яке передує {num}: {result}")
