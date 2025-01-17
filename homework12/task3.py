# Task 3
# Реалізуйте базовий клас Discount з методом apply, який буде приймати ціну і повертати нову ціну після застосування дисконту. Цей метод повинен бути перевизначений у похідних класах.
# Реалізація різних типів дисконту через спадкування:
# - Створіть клас PercentageDiscount, який успадковується від класу Discount і реалізує дисконт у вигляді відсотка.
# - Створіть клас FixedAmountDiscount, який успадковується від класу Discount і реалізує фіксовану знижку у вигляді певної суми.

class Discount:
    def apply(self, cost:int|float, discount: int):
        return cost

class PercentageDiscount(Discount):
    def apply(self, cost: int | float, discount: int):
        return cost * discount / 100

class FixedAmountDiscount(Discount):
    def apply(self, cost: int | float, discount: int):
        return max(cost - discount, 0)

perc = PercentageDiscount()
print(perc.apply(100, 70))

fixed = FixedAmountDiscount()
print(fixed.apply(100, 70))