# Task 4
# Напишіть декоратор, який вимірює час виконання функції.

import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        length = end - start
        return f'Пройшло {length:.4f} секунд.'
    return wrapper

@measure_time
def some_function():
    time.sleep(2)
    
print(some_function())