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