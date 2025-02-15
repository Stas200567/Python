palindrome_string = input("Введіть рядок для перевірки на паліндром: ")
if palindrome_string == palindrome_string[::-1]:
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")