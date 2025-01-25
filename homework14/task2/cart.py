from discount import DiscountMixin 
from product import Product
from payment import PaymentProcessor
import logger

class Cart(DiscountMixin):
    def __init__(self):
        self.products = []

    def add_product(self, product:Product):
        self.products.append(product)
        logger.main.info(f'User add {product.name} to cart')

    def check_total_cost(self) -> int:
        total = 0
        for product in self.products:
            total += product.cost
        return total

    def pay(self, payment_type:PaymentProcessor):
        text = 'Товари до сплати:'
        for product in self.products:
            text += f'\n{product.name}'
        text += f'\n{payment_type.pay(self.check_total_cost())}'
        return text