def capitalize_words(text):
    words = text.split()  
    capitalized_words = [word[0].upper() + word[1:] if word else "" for word in words]  
    return " ".join(capitalized_words)  

text = input("Введіть рядок: ")
print(capitalize_words(text))
