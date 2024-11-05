# Task 8
# Напишіть програму, яка приймає рядок і виводить найдовше слово у ній.

text = input("Напиши текст: ")

words = text.split()
max_word = ""

for word in words:
    if len(word) >= len(max_word):
        max_word = word

print(max_word)