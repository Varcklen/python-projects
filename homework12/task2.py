# Task 2
# Додайте метод pay до класу Cart, який прийматиме інстанс процесора оплати і використовуватиме його для здійснення оплати загальної вартості кошика.

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

class Product:
    def __init__(self, name:str, cost:int):
        self.name = name
        self.cost = cost

class Cart:
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


cart = Cart()
cart.add_product(Product('Some Product', 10))
credit = CreditCardProcessor()
cart.pay(credit)