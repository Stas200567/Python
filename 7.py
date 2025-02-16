def word_count(text):
    words = text.split()  
    return len(words)  

text = input("Введіть рядок: ")
print(f"Кількість слів у рядку: {word_count(text)}")
