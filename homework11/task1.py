# Task 1
# Створіть  клас Product, який буде описувати товар. У якості атрибутів товару використовуйте назву, ціну та опис товару. У класі має бути визначений метод __str__, який повертатиме строкове представлення товару.

class Product:
    def __init__(self, name:str, cost:int, description:str):
        self.name = name
        self.cost = cost
        self.description = description

    def __str__(self) -> str:
        return f'{self.name} {self.cost} {self.description}'

product1 = Product('My Product', 123, 'Some Desc')
        
print(product1)