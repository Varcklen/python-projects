# Task 3
# Число-паліндром з обох сторін (справа ліворуч і ліворуч) читається однаково.
# Найбільше число-паліндром, одержане множенням двох двозначних чисел: 9009 = 91 × 99. Знайдіть найбільший паліндром, одержаний множенням двох трицифрових чисел.
# Виведіть значення цього паліндрому і те, множенням яких чисел він є.

def is_palindrom(number):
    number_str = str(number)
    half_length = len(number_str) // 2
    i = 0
    while i <= half_length:
        if number_str[i] != number_str[- i - 1]:
            return False
        i += 1
    return True

a = 1000
b = 999
result = 123
while not is_palindrom(result):
    a -= 1
    if a < 900:
        a = 999
        b -= 1
    result = a * b
    #print(result)

print(f'result: {result}, a: {a}, b: {b}')