# Напишіть декоратор, який перехоплює та обробляє виключення, що виникають у функції.

def Validator(func):
    def wrapper(*args, **kwargs):
        if len(args) != 2:
            raise ValueError
        if not isinstance(args[0], int | float) or not isinstance(args[1], int | float):
            raise TypeError
        if args[1] == 0:
            raise ZeroDivisionError
        return func(*args, **kwargs)
    return wrapper

@Validator
def Divide(a, b):
    return a / b

print(Divide(6, 2))
#print(Divide(6, '2'))
#print(Divide(2, 0))