# Task 6
# Напишіть декоратор, який обмежує кількість викликів функції.

def limit_calls(max_calls):
    call = [0]
    def decorator(func):
        def wrapper(*args, **kwargs):
            call[0] += 1
            if (call[0] > max_calls):
                raise ValueError('Привищена кiлькiсть викликiв функцii!')
            return func(*args, **kwargs)
        return wrapper
    return decorator

@limit_calls(3)
def some_function():
    print("Виклик функції")

some_function()
some_function()
some_function()
some_function()