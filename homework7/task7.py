# Task 7
# Напишіть програму, яка конвертуватиме суму з однієї валюти в іншу, використовуючи словник з курсами обміну.

conversion = {
    'US => UA': 41,
    'US => EU': 0.95,
    'US => PL': 6.8
}

dollar = float( input("Напишiть суму у долларах: ") )

for convert_type, value in conversion.items():
    print(f'{convert_type}: {value * dollar}')