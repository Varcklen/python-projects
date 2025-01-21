# Task 3
# Реалізуйте базовий клас Discount з методом apply, який буде приймати ціну і повертати нову ціну після застосування дисконту. Цей метод повинен бути перевизначений у похідних класах.
# Реалізація різних типів дисконту через спадкування:
# - Створіть клас PercentageDiscount, який успадковується від класу Discount і реалізує дисконт у вигляді відсотка.
# - Створіть клас FixedAmountDiscount, який успадковується від класу Discount і реалізує фіксовану знижку у вигляді певної суми.

class ValueLimitError(Exception):
    def __init__(self, cost, discount):
        super().__init__(f'discount {discount} must be less than the cost {cost}')

class Discount:
    def apply(self, cost:int|float, discount: int):
        raise NotImplementedError

class PercentageDiscount(Discount):
    def apply(self, cost: int | float, discount: int):
        if not isinstance(cost, int | float):
            raise TypeError('cost must be int or float')
        if not isinstance(discount, int):
            raise TypeError('discount must be int')

        return cost * discount / 100

class FixedAmountDiscount(Discount):
    def apply(self, cost: int | float, discount: int):
        if not isinstance(cost, int | float):
            raise TypeError('cost must be int or float')
        if not isinstance(discount, int):
            raise TypeError('discount must be int')
        if discount >= cost:
            raise ValueLimitError(cost, discount)

        return cost - discount

perc = PercentageDiscount()
print(perc.apply(100, 70))

fixed = FixedAmountDiscount()
print(fixed.apply(100, 70))
print(fixed.apply(100, 110))