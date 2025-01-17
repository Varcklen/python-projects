# Task 5
# Перевірити працездатність застосунку:
# - створіть кілька товарів і додайте їх у кошик.
# - застосуйте різні типи дисконту до кошика.
# - виконайте оплату за допомогою різних методів оплати.

# ============= Payments =============
class PaymentProcessor:
    def pay(self, payment_amount):
        return 'Не можливо сплатити!'

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
        return cost

class PercentageDiscount(Discount):
    def apply(self, cost: int | float, discount: int):
        return cost * discount / 100

class FixedAmountDiscount(Discount):
    def apply(self, cost: int | float, discount: int):
        return max(cost - discount, 0)

class DiscountMixin:
    def apply_discount(self, discount:Discount, discount_amount):
        pass
        for product in self.products:
            product.cost = discount.apply(product.cost, discount_amount)

# ============= Product =============
class Product:
    def __init__(self, name:str, cost:int):
        self.name = name
        self.cost = cost

# ============= Cart =============
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

    def pay(self, payment_type:PaymentProcessor):
        print('Товари до сплати:')
        for product in self.products:
            print(product.name)
        print(payment_type.pay(self.check_total_cost()))

# ============= Actions =============
cart = Cart()
cart.add_product(Product('Milk', 10))
cart.add_product(Product('Apples', 15))

bank = BankTransferProcessor()
paypal = PayPalProcessor()
discount_perc = PercentageDiscount()

cart.pay(bank)
print('')
cart.apply_discount(discount_perc, 50)
cart.pay(paypal)