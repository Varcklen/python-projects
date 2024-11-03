# Task 3
# Напишіть скрипт, який виводить цілі числа від 1 до 200, використовуючи цикл while. В одному рядку необхідно виведити лише п’ять цілих чисел.
# Наприклад,
# 1 2 3 4 5
# 6 7 8 9 10
# 11 12 13 14 15
# ...

MAX_MUNBERS_PER_LINE = 5

i = 1
next_symbol_type = ""

while i <= 200:
    next_symbol_type = "\n" if i % 5 == 0 else " "
    print(i, end = next_symbol_type)
    i += 1