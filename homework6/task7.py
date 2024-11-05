# Task 7
# Напишіть програму, яка приймає рядок і видаляє всі символи, окрім літер і цифр.

text = input("Напиши текст: ")

text1 = "".join(c for c in text if c.isalnum())

print(text1)