# Task 5
# Напишіть програму, яка приймає рядок та підраховує кількість слів у ній.

text = input("Напиши текст: ")

words = text.split()
amount = len(words)

print(f"Тут {amount} слiв.")