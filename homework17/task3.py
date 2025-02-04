# Task 3
# Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.

def action_sum(func, numbers):
    res = map(func, numbers)
    return sum(res)

def double(value):
    return value * 2

def lower(value):
    return value - 1

def set_one(value):
    return 1

numbers = [1, 5, -2, 3, 10, 12, 3]

print(sum(numbers))
print(action_sum(double, numbers))
print(action_sum(lower, numbers))
print(action_sum(set_one, numbers))