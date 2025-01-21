# Task 2
# Створіть клас Cart, який буде виступати у якості кошика з товарами певного покупця. Кошик може містити декілька товарів певної кількості. Додайте метод для додавання товару у кошик. Реалізуйте метод обчислення загальної вартості кошика.
# У класі має бути визначений метод __str__, який повертатиме строкове представлення кошика.

class Product:
    def __init__(self, name:str, cost:int) -> None:
        if not isinstance(name, str):
            raise TypeError('name must be str')
        if not isinstance(cost, int):
            raise TypeError('cost must be int')
        
        self.name = name
        self.cost = cost

class Cart:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product:Product):
        if product == 0:
            raise ValueError(f'Product {product} is null')
        if product in self.products:
            raise ValueError(f'Product {product} already exists')
        self.products.append(product)

    def check_total_cost(self) -> int:
        total = 0
        for product in self.products:
            total += product.cost
        return total

cart = Cart()
product = Product('Some Product', 10)

cart.add_product(product)
#cart.add_product(product)
#cart.add_product(0)
cart.add_product(Product('Some Product2', 15))
print(cart.check_total_cost())
