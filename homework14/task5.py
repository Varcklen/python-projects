# Task 5
# Перевірити працездатність застосунку:
# - створіть кілька товарів і додайте їх у кошик.
# - застосуйте різні типи дисконту до кошика.
# - виконайте оплату за допомогою різних методів оплати.

# ============= Validation =============
class ValueLimitError(Exception):
    def __init__(self, cost, discount):
        super().__init__(f'discount {discount} must be less than the cost {cost}')

# ============= Logger =============
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# ============= Payments =============
class PaymentProcessor:
    def pay(self, payment_amount):
        raise NotImplementedError

class CreditCardProcessor(PaymentProcessor):
    def pay(self, payment_amount):
        return f'Сплачено {payment_amount} кредитною карткою.'

class PayPalProcessor(PaymentProcessor):
    def pay(self, payment_amount):
        return f'Сплачено {payment_amount} завдяки PayPal.'

class BankTransferProcessor(PaymentProcessor):
    def pay(self, payment_amount):
        return f'Сплачено {payment_amount} банкiвским переказом.'


# ============= Discounts =============
class Discount:
    def apply(self, cost:int|float, discount: int):
        raise NotImplementedError

class PercentageDiscount(Discount):
    def apply(self, cost: int | float, discount: int):
        if not isinstance(cost, int | float):
            raise TypeError(f'cost {cost} must be int or float')
        if not isinstance(discount, int):
            raise TypeError(f'discount {discount} must be int')

        return cost * discount / 100

class FixedAmountDiscount(Discount):
    def apply(self, cost: int | float, discount: int):
        if not isinstance(cost, int | float):
            raise TypeError(f'cost {cost} must be int or float')
        if not isinstance(discount, int):
            raise TypeError(f'discount {discount} must be int')
        if discount >= cost:
            raise ValueLimitError(cost, discount)

        return cost - discount

class DiscountMixin:
    def apply_discount(self, discount:Discount, discount_amount):
        logger.info(f'User uses discount {discount} to cart.')
        for product in self.products:
            product.cost = discount.apply(product.cost, discount_amount)

# ============= Product =============
class Product:
    def __init__(self, name:str, cost:int):
        if not isinstance(name, str):
            raise TypeError(f'name {name} must be str')
        if not isinstance(cost, int):
            raise TypeError(f'cost {cost} must be int')


        self.name = name
        self.cost = cost

# ============= Cart =============
class Cart(DiscountMixin):
    def __init__(self):
        self.products = []

    def add_product(self, product:Product):
        self.products.append(product)
        logger.info(f'User add {product.name} to cart')

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

# ============= Actions =============
try:
    cart = Cart()
    cart.add_product(Product('Milk', 10))
    #cart.add_product(Product('Milk', '10')) #продукт з помилкою для перевiрки logger.error
    cart.add_product(Product('Apples', 15))

    bank = BankTransferProcessor()
    paypal = PayPalProcessor()
    discount_perc = PercentageDiscount()

    print(cart.pay(bank))
    logger.info(f'User pays card via {bank}')
    cart.apply_discount(discount_perc, 50)
    print(cart.pay(paypal))
    logger.info(f'User pays card via {paypal}')
except TypeError as error:
    logger.error(error)
    #print(error)
except ValueLimitError as error:
    logger.error(error)
    #print(error)