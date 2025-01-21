# Task 1
# Створіть  клас Product, який буде описувати товар. У якості атрибутів товару використовуйте назву, ціну та опис товару. У класі має бути визначений метод __str__, який повертатиме строкове представлення товару.

class Product:
    def __init__(self, name:str, cost:int, description:str):
        if not isinstance(name, str):
            raise TypeError('name must be str')
        if not isinstance(cost, int):
            raise TypeError('cost must be int')
        if not isinstance(description, str):
            raise TypeError('description must be str')

        self.name = name
        self.cost = cost
        self.description = description

    def __str__(self) -> str:
        return f'{self.name} {self.cost} {self.description}'

try:
    product1 = Product('My Product', 123, 'Some Desc')
    #product1 = Product('My Product', '123', 'Some Desc')
    print(product1)
except TypeError as error:
    print(error)