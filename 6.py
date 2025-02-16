def longest_word(text):
    words = text.split()  
    if not words:  
        return None
    return max(words, key=len)  

text = input("Введіть рядок: ")
print(f"Найдовше слово: {longest_word(text)}")
