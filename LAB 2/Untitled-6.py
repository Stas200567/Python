char_string = input("Введіть рядок для підрахунку унікальних символів: ")
char_count = {}
for char in char_string:
    char_count[char] = char_count.get(char, 0) + 1
print("Унікальні символи та їх кількість:", char_count)