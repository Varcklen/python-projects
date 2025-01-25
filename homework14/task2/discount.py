import logger
import validation

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
            raise validation.ValueLimitError(cost, discount)

        return cost - discount

class DiscountMixin:
    def apply_discount(self, discount:Discount, discount_amount):
        logger.main.info(f'User uses discount {discount} to cart.')
        for product in self.products:
            product.cost = discount.apply(product.cost, discount_amount)