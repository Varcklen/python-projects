from cart import Cart
from product import Product
from validation import ValueLimitError
import payment
import discount
import logger

#зроблено на основi task5.py
try:
    cart = Cart()
    cart.add_product(Product('Milk', 10))
    #cart.add_product(Product('Milk', '10'))            #продукт з помилкою для перевiрки logger.error
    cart.add_product(Product('Apples', 15))

    bank = payment.BankTransferProcessor()
    paypal = payment.PayPalProcessor()
    discount_perc = discount.PercentageDiscount()

    #print(cart.pay(bank))                              #розкоментувати, щоб отримати бiльше iнформацii
    logger.main.info(f'User pays card via {bank}')
    cart.apply_discount(discount_perc, 50)
    #print(cart.pay(paypal))                            #розкоментувати, щоб отримати бiльше iнформацii
    logger.main.info(f'User pays card via {paypal}')
except TypeError as error:
    logger.main.error(error)
    #print(error)
except ValueLimitError as error:
    logger.main.error(error)
    #print(error)