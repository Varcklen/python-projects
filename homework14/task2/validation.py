class ValueLimitError(Exception):
    def __init__(self, cost, discount):
        super().__init__(f'discount {discount} must be less than the cost {cost}')