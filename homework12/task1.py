# Task 1
# Створіть базовий клас PaymentProcessor з методом pay, який прийматиме суму для оплати. Цей метод повинен бути перевизначений у похідних класах.
# Реалізуйте класи для різних методів оплати, які успадковуються від PaymentProcessor:
# CreditCardProcessor - для оплати кредитною карткою.
# PayPalProcessor - для оплати через PayPal.
# BankTransferProcessor - для банківського переказу.

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

credit = CreditCardProcessor()
print(credit.pay(15))

paypal = PayPalProcessor()
print(paypal.pay(25))

bank = BankTransferProcessor()
print(bank.pay(35))