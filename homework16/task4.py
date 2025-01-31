# Task 4
# Напишіть генераторну функцію, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана параметром цієї функції.

def simple(limit): 
    start = 1
    while start <= limit:
        is_simple = True
        for i in range(2, start):
            if start % i == 0:
                is_simple = False
                break
        if is_simple:
            yield start

        start += 1

for i in simple(10):
    print(i)