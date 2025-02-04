# Task 1
# Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається за допомогою функції користувача. Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, що видаються послідовностю. Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.


def consiquence(func, loop_limit, *args, **kwargs):
    sum = 0
    for _ in range(loop_limit):
        sum += func(*args, **kwargs)
        yield sum

def plus(a, b):
    return a + b

def double_plus(a, b):
    return a + 2 * b


for i in consiquence(plus, 5, 1, 1):
    print(i)

print()

for i in consiquence(double_plus, 5, 1, 1):
    print(i)