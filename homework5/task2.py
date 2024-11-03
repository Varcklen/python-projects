# Task 2
# Напишіть скрипт для визначення суми цілих непарних чисел від 1 до 99 за допомогою оператора for. Використовуйте цілочисельні змінні summa і count.

numbers = [1, 3, 5, 6, 7, 8, 9, 99]

sum_result = 0

for number in numbers:
    if number % 2 != 0:
        sum_result += number

print(f"Result: {sum_result}")