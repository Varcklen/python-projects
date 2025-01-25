class Product:
    def __init__(self, name:str, cost:int):
        if not isinstance(name, str):
            raise TypeError(f'name {name} must be str')
        if not isinstance(cost, int):
            raise TypeError(f'cost {cost} must be int')

        self.name = name
        self.cost = cost