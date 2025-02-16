def power(base, exponent):
    result = 1  
    if exponent < 0:  
        base = 1 / base  
        exponent = -exponent  

    for _ in range(exponent):  
        result *= base  

    return result


base = float(input("Введіть число: "))
exponent = int(input("Введіть степінь: "))

print(f"{base}^{exponent} = {power(base, exponent)}")
