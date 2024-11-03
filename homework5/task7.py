# Task 7
# Є список [0, 5, 2, 4, 7, 1, 3, 19].
# Напишіть скрипт для підрахунку непарних цифр у ньому.

numbers = [0, 5, 2, 4, 7, 1, 3, 19]

for number in numbers:
    if number % 2 != 0:
        print(number)