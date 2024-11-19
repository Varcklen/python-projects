# Task 1
# Напишіть функцію, яка приймає суму доходу користувача і податкову ставку у відсотках, а повертає розраховану суму податку, яку потрібно сплатити.

def tax_netto(salary, tax):
    if not 0 <= tax <= 1:
        Exception(f"tax повинен бути у дiапазонi [0:1]. Зараз: {tax}.")
    return tax * salary

summary = int(input("Напишiть суму: "))
tax_point = float(input("Напишiть податкову ставку (у %): ")) / 100

tax = tax_netto(summary, tax_point)
print(f"До сплати: {tax}.")