# Task 7
# Напишіть декоратор, який кешує результати обчислення функції і повертає їх з кешу при наступних викликах з тими самими аргументами.

def cache_results():
    cache = {}
    def wrapper(n):
        if not n in cache:
            cache[n] = fibonacci(n)
        return cache[n]
    return wrapper

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

c = cache_results()
print(c(5))  # Обчислюється
print(c(10))  # Використання кешу