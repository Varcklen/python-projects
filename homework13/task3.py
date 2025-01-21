# Перевірити працездатність застосунку:
# - створіть кілька товарів
# - додайте створені товари у кошик
# - поверніть користувачу вміст кошика та його вартість

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

    def print_all_products(self):
        for product in self.products:
            print(product.name)

cart = Cart()
cart.add_product(Product('Some Product', 10))
cart.add_product(Product('Some Product2', 15))
cart.add_product(Product('Some Product3', 25))

cart.print_all_products()
print(f'total cost: {cart.check_total_cost()}')
