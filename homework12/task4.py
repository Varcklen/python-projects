# Task 4
# Створіть міксин DiscountMixin, який буде мати метод apply_discount.
# Метод повинен приймати інстанс дисконту і застосовувати його до всіх товарів у кошику.
# Клас Cart має успадковуватися від класу DiscountMixin.

class DiscountMixin:
    def apply_discount(self, discount_percent):
        pass
        for product in self.products:
            product.cost *= discount_percent / 100

class Product:
    def __init__(self, name:str, cost:int):
        self.name = name
        self.cost = cost

class Cart(DiscountMixin):
    def __init__(self):
        self.products = []

    def add_product(self, product:Product):
        self.products.append(product)

    def check_total_cost(self) -> int:
        total = 0
        for product in self.products:
            total += product.cost
        return total

cart = Cart()
cart.add_product(Product('Some Product', 10))
cart.add_product(Product('Some Product2', 15))
print(cart.check_total_cost())
cart.apply_discount(50)
print(cart.check_total_cost())