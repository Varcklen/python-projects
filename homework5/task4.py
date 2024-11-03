# Task 4
# Напишіть скрипт, який обчислює за допомогою циклу факторіал числа n (n вводиться з клавіатури).

n = int( input("Введiть число: ") )

i = 1
result = 1
while i <= n:
    result *= i
    i += 1

print(f"Result: {result}.")