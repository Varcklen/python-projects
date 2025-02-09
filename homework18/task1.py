# Домашнє завдання
# Task 1
# Напишіть декоратор, який виконує певну дію перед і після виконанням функції.

class Decor:
    def __init__(self, func):
        self.func = func

    def __before(self):
        print('Я спрацював до функцii!')

    def __after(self):
        print('Я спрацював пiсля функцii!')

    def __call__(self, *args, **kwargs):
        self.__before()
        res = self.func(*args, **kwargs)
        self.__after()
        return res

@Decor
def greeting(name):
    return f'Hello {name}!'

print(greeting('World'))