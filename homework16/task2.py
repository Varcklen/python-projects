# Task 2
# Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії.

def geometric(n, start = 1, step = 1):
    result = 0
    for _ in range(n):
        result = (start - 1) / start 
        yield result
        start += step

y = geometric(5, 3, 2)

print(next(y))
print(next(y))
print(next(y))